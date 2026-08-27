# Kristiina Vaik — academic-homepage

See leht kasutab päriselt [luost26/academic-homepage](https://github.com/luost26/academic-homepage) Jekylli malli. Algse teema paigutused, komponendid, stiilid ja Gemfile on projektis olemas. Versiooni ja kohanduste kohta vaata THEME.md. Algne MIT litsents on failis LICENSE.

## Käivitamine

Ruby 3.4 ja Bundler peavad olema paigaldatud. Selles Macis on need juba paigaldatud. Projekti kaustas:

```sh
bash scripts/jekyll.sh install
bash scripts/jekyll.sh serve --host 127.0.0.1 --port 4000
```

Ava brauseris http://127.0.0.1:4000/. Leht tuleb ehitada Jekylliga: lähtefaili index.html topeltklõps ei kuva valmis lehte.

Sõltuvused paigaldatakse projekti vendor/bundle kausta. Selle Maci käivitusskript leiab Homebrew Ruby automaatselt; mujal kasutab PATH-is olevat Rubyt. Süsteemi Ruby seadistust ega shelli käivitusfaile pole muudetud.

## Sisu muutmine

| Fail | Sisu |
| --- | --- |
| _data/profile.yml | Nimi, amet, foto, e-post, aadress ja tutvustus |
| _data/navigation.yml | Menüü |
| _includes/academic-content.html | Uurimisteemad, 9 publikatsiooni, 7 projekti, 4 kursust, 4 juhendamist, 5 hariduskirjet ja 9 töökirjet |
| _includes/widgets/profile_card_mini.html | Teema vasak profiili- ja kontaktipaneel |
| _includes/widgets/profile_card_bio_only.html | Teema tutvustuspaneel koos meemiga paremas ülanurgas |
| assets/css/custom.css | Väikesed isiklikud kohandused algse teema stiilidele |
| _config.yml | Lehe pealkiri, kirjeldus, avalik aadress ja alamkaust |

Profiilipildiks on kasutaja lisatud kosmosekass failis images/space-cat.png. Pilt kuvatakse tervikuna, ilma kärpimata.
Pildi vahetamiseks laadi uus pilt images-kausta ja muuda profile.yml välju portrait_url ja portrait_alt.
Meem asub images/bell-curve.webp. Selle all on allkiri “The more I learn, the further right I go.”; teksti saab muuta failis _includes/widgets/profile_card_bio_only.html.

Aadress on instituudi avalik aadress, mitte kodune aadress. Akadeemiliste kirjete sisu säilitati eelmisest versioonist; see ei uuene automaatselt.

## GitHub Pages

See versioon vajab Jekylli ehitust. Ära kasuta eelmise staatilise versiooni .nojekyll-faili.

1. Paki academic-homepage-jekyll.zip lahti.
2. Laadi selle sisu oma GitHubi lehe hoidla juurkausta. Kaasa ka punktiga algav .github-kaust, Gemfile, Gemfile.lock, _config.yml, _data, _includes, _layouts, assets, images ja public.
3. Kustuta hoidlasse varem laaditud .nojekyll-fail. Vana styles.css ei ole enam kasutusel.
4. Vali hoidlas Settings → Pages → Source: GitHub Actions.
5. Kaasas olev töövoog ehitab lehe Jekylliga ja avaldab selle. Seda töövoogu pole sinu GitHubi kontol veel käivitatud.

Töövoog võtab õige avaliku aadressi GitHub Pagesi seadetest, et alamkausta lingid ja jagamiskaart töötaksid. Kohalikuks käsitsi avaldamiseks määra _config.yml failis url (nt sinu tegelik https://kasutaja.github.io) ja baseurl (tühi isikliku avalehe korral, /hoidla projektilehe korral).

[GitHubi juhend kohandatud Pagesi töövoogude kohta](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Kontroll ja ehitus

```sh
bash scripts/jekyll.sh build
python3 scripts/verify.py
```

Valmis HTML tekib _site-kausta. Seda ei muudeta käsitsi. Eelvaade laadib algse teema Bootstrapi, ikoonid, fondid ja JavaScripti CDN-idest, seega on algse kujunduse jaoks vaja internetiühendust.

## Varukoopia ja Sites

Eelmise staatilise versiooni failid on alles tööruumi .previous-draft/static-v2 kaustas ja academic-website-v2.zip paketis. Neid ei ole uue teemaga segatud.

Varasem Sitesi avaldamine jäi üleslaadimisloa taha. Selle paigalduse käigus ei saadeta sinu lehe sisu välisele serverile ega muudeta avalikku lehte. scripts/build.mjs oskab vajaduse korral pakkida Jekylli väljundi varasema Sitesi majutuse jaoks.

Jagamiskaart public/og.png säilitati eelmisest versioonist. See sisaldab teksti “Kristiina Vaik” ja “Language, text & digital humanities.”. Jekyll lisab jagamiskaardi absoluutse URL-i, kui lehe url on seadistatud.
