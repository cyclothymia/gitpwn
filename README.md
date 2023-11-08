# gitpwn

A Python OSINT tool to obtain leaked information from commits on a single or multiple GitHub profiles.

## GitHub preventative measures

All GitHub commits and other activities, uses the email address verified to a GitHub account to link those activities with a GitHub profile on repositories. This means whenever a GitHub user commits to a public repository, their linked email address will become pseudo-publically accessible, via the [GitHub API](https://developer.github.com/v3/activity/events/). 

GitHub has provided a [help article](https://help.github.com/articles/setting-your-email-in-git/) on how to prevent this from happening, and instead obfuscating your email address with a `@users.noreply.github.com` when performing operations on GitHub.

"As [@pielco11](https://github.com/pielco11/) [warned](https://twitter.com/noneprivacy/status/1373164632756604934), emails and other data can be spoofed in commits." - [GitRecon](https://github.com/GONZOsint/gitrecon/)

### Configurations on Github:

- Settings url: https://github.com/settings/emails

  - ✔️ Keep my email addresses private

  - ✔️ Block command line pushes that expose my email

---

## Prerequisites
- [Python 3](https://www.python.org/downloads/)
- `pip`
  - fade
  - rich
  - dotenv
  - pystyle
  - requests
  - colorama
- [GitHub Access Token](https://github.com/settings/tokens)

---

## Installation
```bash
git clone https://github.com/cyclothymia/gitpwn.git
cd gitpwn/
python3 -m pip install -r requirements.txt
```
Create a `.env` file in the following folder path: `gitpwn/modules/`.

Edit the `.env` file to have the following data:
```bash
GH_TOKEN=Your Token Here
```

Run `gitpwn.py` for single username search or `multipwn.py` for bulk file search. All results will output a {username}.json file in `gitpwn/results/`.

---

## Obtainable Information
GitHub Info | Obtainability
------------ | -------------
Username | Yes
Name | Yes
User ID | Yes
Node ID | Yes
Email | Yes
Location | Yes
Bio | Yes
Company | Yes
Blog | Yes
Twitter | Yes
Gravatar | Yes
Hireable | Yes
User Type | Yes
Admin Status | Yes
Public Repos | Yes
Public Gists | Yes
Followers | Yes
Following | Yes
Created At | Yes
Updated At | Yes
URLs | Yes
SSH Keys | Yes
Git Leaked Emails | Yes

---

## Sources and Inspiration
> Source 1: https://thedatapack.com/tools/find-github-user-email/

> Source 2: https://github.com/GONZOsint/gitrecon/

> Source 3: https://github.com/s0md3v/Zen
