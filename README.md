# Pomio Legal

Public legal pages for the **Pomio** iOS app (Bundle ID: `com.pomodoro.six11`).

## App Store Connect URLs

After GitHub Pages is live:

- **Privacy Policy:** https://opheliasfather.github.io/Pomio-Legal/privacy-policy.html
- **Terms of Use:** https://opheliasfather.github.io/Pomio-Legal/terms-of-use.html

## Publish (one-time)

1. In **GitHub Desktop**, click **Publish repository** → name `Pomio-Legal` → Public.
2. On GitHub: **Settings → Pages → Build and deployment → Branch: `gh-pages` / `/ (root)`**.
3. Push to `main` (workflow publishes to `gh-pages` automatically).

The workflow in `.github/workflows/pages.yml` deploys on every push to `main`.

## Regenerate pages

After editing `generate_pages.py`:

```bash
python3 generate_pages.py
```
