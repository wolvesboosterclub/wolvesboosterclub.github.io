# Wolves Booster Club Website

This site is being hosted at https://wolvesboosterclub.org (points to https://wolvesboosterclub.github.io)

This repo contains the code for the Wolves Booster Club newsletter/events website. The organization maintains this public, open-source website to maintain outreach and updates with the members of the organization. Updates/corrections/discussions should take place in pull requests and/or the discussions sections of the repo.

## Development

In order to help develop/maintain this website, there are some technologies in play that you should be familiar with, namely:

- HTML, CSS, Javascript (of course)
- Tailwind CSS (static, standalone version used. See below)
- Jinja2 (staticjinja used for compiled templating)
- Python3 virtualenv (to maintain jinja2)

### Setup

Pull the repo with git

```
git clone git@github.com:wolvesboosterclub/wolvesboosterclub.github.io.git
```

Activate the python virtual environment (make sure python3 > 3.8 is installed)

```
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

You will also need the Tailwindcss standalone builder (make sure to get the version for your platform)

https://tailwindcss.com/blog/standalone-cli

### Doing

The code is going to look gross. It's the nature of using Jinja2 and Tailwind but these two technologies together make building websites _very_ fast.

Most of the dynamic content has been separated out to make it easier to update and not mess with the larger website design. As you work, have a terminal open and running tailwindcss in the background:

```
tailwindcss -i <input file> -o <output file> -mw
```

For example, when workisng on the Holiday Party subpage, at the root of the project directory (you don't have to be at the root, just use proper paths to the files you care about), I use:

```
tailwindcss -i ./css/index.tw.css -o ./css/index.css -mw
```

You can also have staticjinja watch the templates as you work

```
(.venv) # staticjinja watch
```

After you've made your changes, rebuild the static site by running (if not watching the files):

```
(.venv) # staticjinja build
```

Preview the site locally by running

```
python3 -m http.server
```

And gonig to the url it is serving on.

Then add, commit, and push your changes.

```
git add .
git commit -m "<commit message>"
git push
```

#### Notes

Tailwindcss does not like being split over multiple files. The site uses only one minified CSS file that is generated from all seen html files. It will detect all HTML files in the project and generate the one CSS file for them all. If you need to add custom CSS, add it to [index.tw.css](css/index.tw.css). A post processing CSS plugin could be used to combine CSS files in the project before using tailwindcss on it but it has not yet been implemented.

Do not forget to minify the tailwindcss outputs with the `-m` switch. The file size is largely reduced:

```
-rw-rw-r-- 1 subcursion subcursion 12977 Nov 14 17:56 ./css/index.css
# vs.
-rw-rw-r-- 1 subcursion subcursion 5893 Nov 14 17:56 ./css/index.css
```

When testing locally, the contact us portion of the footer will not work correctly. This is due to the current implementation of the application listening for requests from the form being hardened. In order to bypass this security restriction temporarily, I would suggest using this (or similar) extension:
https://addons.mozilla.org/en-US/firefox/addon/cors-everywhere/
I then configured it to whitelist my local IP address so that the browser does not try to enforce the security while I am testing. DO NOT enable this extension globally as it disables a vital security feature HTTP made called Access-Control-Allow-Origin (https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin).
Go to `about:addons` and into Options for CORS Everywhere and add something like this to the whitelist:

```
/^http(s)?://10.0.0.4(:\d+)?.*/i
```

Where 10.0.0.4 is your IP of the machine running the Python3 http server locally, and save.
