# Kristiina Vaik — academic homepage

## 1. The plan

Use one English-language page, with About, Research, Selected publications, Selected projects, Teaching, and Contact. A short navigation list jumps to the relevant section on that same page. ETIS remains the full CV and publication record, so there is less information to maintain in two places.

The reference, [Peeter Tinits’s website](https://peetertinits.github.io/), uses a white background, restrained typography, ordinary text links, a short biography, a profile sidebar, and navigation to separate academic sections. This homepage keeps the clear hierarchy and generous whitespace, but uses a single column and a single page. No text, portrait, theme, or layout code was copied.

The delivered website is plain HTML and CSS. There is no JavaScript, framework, analytics, contact form, external font, image download, or build step. HTML holds the content; CSS controls its appearance. GitHub Pages is the service that makes these files available as a website.

## 2. Website files

Upload only these three files, keeping their names exactly as shown:

| File | What it does |
| --- | --- |
| `index.html` | The complete homepage. Edit this to update your text and links. |
| `styles.css` | Font sizes, colours, spacing, and mobile layout. Usually no editing needed. |
| `.nojekyll` | An empty file that tells GitHub to publish the files without Jekyll, a site-generation tool. |

This README is your instruction sheet. Uploading it is optional; the website does not depend on it. The ready-to-upload ZIP contains these three files and this README. Unzip it first; uploading the ZIP itself will not publish a website.

**Earlier project files:** this workspace also retains tools from the earlier draft. Do not upload the entire workspace, `app`, `node_modules`, `public`, `scripts`, `.openai`, `.previous-draft`, or `dist`. They are not needed for this website. Edit `index.html` directly; do not regenerate it from the old draft. The earlier content has been preserved locally in `.previous-draft`.

## 3. Content and sources

Professional information was checked on 27 August 2026 against [your ETIS profile](https://www.etis.ee/CV/Kristiina_Vaik), including its [English version](https://www.etis.ee/CV/Kristiina_Vaik/eng/).

- **Position:** Research Fellow in Digital Humanities, University of Tartu, Institute of Estonian and General Linguistics. The dated career record gives 1 October 2025–28 February 2030. The Estonian profile’s headline still says computational linguistics researcher; the site follows the dated record and its English title.
- **Education:** PhD, University of Tartu, 2024. Dissertation: *Beyond Genres: A Dimensional Text Model for Text Classification*. Supervisors: Kadri Muischnek and Kairit Sirts.
- **Research topics:** editorial summaries of the thesis, publications, and projects, not a quoted self-description. Please review the emphasis before publishing.
- **Publications:** four selected ETIS entries, not a claim to list every publication. The multilingual analogy paper was also checked in the [ACL Anthology](https://aclanthology.org/2020.lrec-1.501/). The long author list for the 2023 paper is explicitly abbreviated with “et al.”, meaning “and others”.
- **Projects:** Center for Digital Text Scholarship (2025–2030) and Estonian Universal Syntax: Resources and Applications (2018–2022). These are project dates, not your personal participation dates. No project-leadership role is asserted. ETIS lists other projects too; two are enough for this short homepage.
- **Project websites:** DigiTS now links directly to its [official homepage](https://digits.ut.ee/) in About and Selected projects; its [team contact page](https://digits.ut.ee/contact/) also lists Kristiina Vaik. A separate ETIS record link is retained. No standalone homepage was verified for the older syntax project: the [TartuNLP research-group page](https://tartunlp.ai/branches/automatic-processing) itself links that project to ETIS, so its original ETIS link remains. To add another project website, replace the project's title link with the verified official URL and keep its ETIS record as a separate link. Do not label a general research-group page as a project's own homepage.
- **Contact:** `kristiina.vaik@ut.ee`, as shown in ETIS.

- **Teaching:** four courses from the English ETIS profile, with recorded years or year ranges, course codes, and ECTS credits. The plain dated lists follow the approach of [the reference teaching page](https://peetertinits.github.io/teaching/). No teaching-language, co-teacher, semester, or course-material link has been inferred. To update teaching, find `id="teaching"` in `index.html`, then edit or copy a year heading and its list. Keep date ranges unless you have confirmed individual years.

No birth date, private address, invented biography, portrait, ORCID, Google Scholar profile, GitHub username, award, or missing identifier has been added. Supervision remains available through ETIS rather than a separate section.

## 4. Review locally before publishing

1. Unzip `academic-website.zip` into a folder on your computer.
2. Keep `index.html` and `styles.css` together in that folder.
3. Double-click `index.html`. Your normal browser will show the website. If it opens in a text editor, right-click it and choose **Open With** → your browser.
4. Check the title, biography, research wording, papers, project list, and email. You can publish this version as-is if those are the details you want to share.
5. Try each navigation link and make the browser window narrower to see the mobile layout.

Opening the file on your computer does not publish it. The email link uses your installed mail application; if none is configured, visitors can copy the visible address.

## 5. Create your GitHub account and repository

A **repository** is a folder stored on GitHub, with a history of changes. A **branch** is a version of that folder; we will use only the default branch, `main`. A **commit** saves a change in that history.

1. Go to [GitHub](https://github.com/) and create an account, or sign in. Verify your email when GitHub asks.
2. Note your exact **username**. This is your account handle, not your full display name. Do not assume it is `Kristiina_Vaik` just because that is your ETIS address.
3. Click the **+** menu near the upper-right corner, then **New repository**. You can also go to [Create a new repository](https://github.com/new).
4. Choose your own account as **Owner**.
5. Enter `YOUR-USERNAME.github.io` as the repository name, replacing `YOUR-USERNAME` with your actual username. For example, a hypothetical username `researcher-example` would use `researcher-example.github.io`.
6. Select **Public**. The website and uploaded files will be visible to anyone. Do not upload private information, passwords, or unpublished material you do not want to share.
7. Turn **Add README** on. Leave the other optional settings unchanged.
8. Click **Create repository**. The README creates the initial `main` branch.

If that repository already exists, open it and inspect its contents first. Do not replace an existing website without backing it up.

See [GitHub’s Pages quickstart](https://docs.github.com/en/pages/quickstart).

## 6. Add your files

1. Open the repository’s **Code** tab. Make sure `main` is selected above the file list.
2. Click **Add file** → **Upload files**.
3. Drag `index.html` and `styles.css` from the unzipped folder into the upload area. Upload the individual files, not the containing folder or ZIP.
4. In the commit message box, write `Add academic homepage`.
5. Choose **Commit directly to the main branch** if asked, then click **Commit changes**. This saves the files. No pull request or additional branch is needed for this personal site.
6. Add `.nojekyll`. Because files beginning with a dot may be hidden on your computer, the simplest method is **Add file** → **Create new file**. Enter exactly `.nojekyll` as the filename, leave the contents empty, and use **Commit changes** to save it to `main`. If you already uploaded that file, skip this step.
7. Confirm that `index.html`, `styles.css`, and `.nojekyll` appear directly in the file list, alongside README.md. This top level is called the **root**. They must not be inside another folder.

See [GitHub’s file-upload instructions](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).

## 7. Enable GitHub Pages

1. Inside your repository, open **Settings**. This is the repository’s Settings tab, not your account settings.
2. In the left sidebar, find **Pages** under **Code and automation**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
4. Under **Branch**, select `main` and `/ (root)`.
5. Click **Save**. Leave **Custom domain** empty; you do not need to buy a domain.
6. Wait for publication. GitHub says changes can take up to 10 minutes. Refresh the Pages settings page and use **Visit site** when it appears.
7. Your homepage will be at `https://YOUR-USERNAME.github.io/`, with your real username. The `github.com/...` address shows your files; the `github.io` address shows your website.
8. On the published page, test the six navigation links, publication links, and email. Check it once on your phone too.

See [GitHub’s publishing-source instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) and [publication timing](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).

## 8. Update the website later

You can do all routine editing in your browser:

1. Open your repository on GitHub and click `index.html`.
2. Click the pencil button (**Edit this file**).
3. Search for `EDIT:` to find the marked editing areas. Text between `<!--` and `-->` is a comment: guidance for you, invisible on the website. Comments are still public in the source, so do not put private notes there.
4. Change the relevant wording. Keep the surrounding HTML tags intact. For example, change only the words between `<p>` and `</p>` to edit a paragraph.
5. For a new publication, copy an existing whole block from `<li>` through `</li>` in the publications section and replace its authors, date, title, venue, and link. Do not invent a link if no online record is available; plain text is fine.
6. A link looks like `<a href="https://example.org/">Visible text</a>`. Change the address inside the quotation marks and, if necessary, the visible text. For email, update both the `mailto:` address and the address visitors see.
7. Update the footer date in two places: `datetime="2026-08-27"` uses year-month-day, while `27 August 2026` is the visible version.
8. Click **Commit changes**, write a short explanation such as `Add publication`, choose the `main` branch, and confirm **Commit changes**.
9. Wait for GitHub Pages to republish, then refresh your `github.io` website. You do not need to enable Pages again.

GitHub’s code preview shows source or a comparison of changes, not necessarily the finished HTML page. Use your local browser copy or the published website to inspect the layout. Changing ETIS does **not** automatically update this website.

If you make a mistake, open the file’s **History**, view a known-good version, and copy its text back into the current file using the editor. Commit the correction. For a separate backup, use **Code** → **Download ZIP** before larger edits.

See [GitHub’s editing instructions](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).

### Optional portrait — only if you want one later

No picture is required. If you decide to add one, upload a small `portrait.jpg` that you have permission to use, to the same root folder. Replace the `OPTIONAL PHOTO` comment in `index.html` with:

```html
<img class="portrait" src="portrait.jpg" alt="Kristiina Vaik" width="400" height="500">
```

Use the image’s actual pixel dimensions in `width` and `height`; 400 × 500 above is only an example. A file under about 200 KB is plenty for this small portrait. Do not add the HTML before uploading the image. No other decorative images are needed.

## 9. If something does not work

| What you see | What to check |
| --- | --- |
| 404 / page not found | Wait up to 10 minutes. Confirm the repository name matches your username, the file is exactly `index.html` (lowercase), and Pages uses `main` and `/ (root)`. |
| The page has no styling | Check that `styles.css` is beside `index.html`, with exactly that spelling and no `.txt` extension. |
| A list of code instead of a website | You may be on `github.com` instead of your `github.io` address. |
| Changes have not appeared | Check that you committed to `main`. Wait, then hard-refresh: Command–Shift–R on Mac or Ctrl–Shift–R on Windows. |
| A navigation link does not work | Keep `href="#research"` matched to `id="research"`, and likewise for the other sections. Changing a heading’s visible wording is fine. |
| GitHub says deployment failed | Open the repository’s **Actions** tab and inspect the latest Pages run for the error. Check **Settings → Pages** again and verify your account email. |
| A publication page fails to open | Try the full ETIS profile link. External sites may be temporarily unavailable even when your own page works. |

No terminal commands, package installation, Jekyll theme, paid hosting, custom domain, or GitHub Actions workflow file are needed for this setup.
