"""Validate Jekyll output without browser automation or external requests."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

parser = argparse.ArgumentParser()
parser.add_argument('--site', default='_site')
parser.add_argument('--baseurl', default='')
args = parser.parse_args()
root = Path(args.site)

class Homepage(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.ids = []
        self.refs = []
        self.section = None
        self.counts = {}
        self.h1_count = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h1':
            self.h1_count += 1
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'section':
            self.section = attrs.get('id')
            self.counts[self.section] = 0
        if tag == 'li' and self.section:
            self.counts[self.section] += 1
        if tag == 'img':
            assert attrs.get('alt'), 'Image missing alternative text'
        for key in ('src', 'href'):
            if key in attrs:
                self.refs.append(attrs[key])
        if tag not in {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        assert self.stack and self.stack[-1] == tag, (tag, self.stack)
        self.stack.pop()
        if tag == 'section':
            self.section = None

html = (root / 'index.html').read_text()
assert '{{' not in html and '{%' not in html, 'Unrendered Liquid markup'
for placeholder in ('Your Name', 'your@email.com', 'Bicolor cat', 'your_github_id', 'xFmQpf4AAAAJ'):
    assert placeholder not in html, placeholder
for marker in ('Template: https://github.com/luost26/academic-homepage', 'assets/css/global.css', 'assets/css/custom.css', 'profile-sidebar', 'corner-image', 'Jakobi 2'):
    assert marker in html, marker
page = Homepage()
page.feed(html)
assert not page.stack, page.stack
assert len(page.ids) == len(set(page.ids)), 'Duplicate IDs'
assert page.h1_count == 1, 'Expected one primary heading'
expected = {'publications': 9, 'projects': 7, 'teaching': 4, 'supervision': 4, 'education': 5, 'career': 9}
for section, count in expected.items():
    assert page.counts[section] == count, (section, page.counts[section], count)
for ref in page.refs:
    url = urlsplit(ref)
    if url.scheme or url.netloc:
        continue
    pathname = unquote(url.path)
    if args.baseurl and pathname.startswith('/'):
        assert pathname.startswith(args.baseurl + '/'), 'Missing base path: ' + ref
    if args.baseurl and pathname.startswith(args.baseurl + '/'):
        pathname = pathname[len(args.baseurl):]
    if url.fragment and pathname in ('', '/', '/index.html'):
        assert url.fragment in page.ids, ref
    if pathname and pathname != '/':
        assert (root / pathname.lstrip('/')).is_file(), ref
for forbidden in ('Gemfile', 'Gemfile.lock', 'scripts', 'vendor', 'README.md', '.openai', 'styles.css'):
    assert not (root / forbidden).exists(), 'Source leaked into output: ' + forbidden
print('PASS: real Jekyll theme, all 38 academic records, valid HTML, local assets, navigation and no demo profile.')
