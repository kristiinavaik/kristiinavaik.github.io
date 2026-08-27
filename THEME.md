# Installed theme

This site installs the actual Jekyll template from:
https://github.com/luost26/academic-homepage

Upstream commit: `163ee122886f5835ca139851623b38f5ab8d398e`.
Downloaded on 27 August 2026. License: MIT; see LICENSE.

The upstream Gemfile, layouts, includes, data structure and assets are installed locally.
Jekyll renders index.html through _layouts/default.html and the upstream profile widgets.
This is a source-template installation, as documented by the repository, not a gem theme or a visual imitation.

Customizations:
- Profile and navigation data for Kristiina Vaik.
- Contact/address and placeholder-photo attribution in profile_card_mini.html.
- The supplied meme in profile_card_bio_only.html.
- Preserved academic records in _includes/academic-content.html.
- Site metadata, accessible navigation, and assets/css/custom.css.
- Demo publication, news, blog, and showcase content was not installed.
- Extra Ruby compatibility dependencies are declared in Gemfile.

The previous static version remains in the parent workspace at .previous-draft/static-v2
and in academic-website-v2.zip.
