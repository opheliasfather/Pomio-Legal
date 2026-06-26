# Pomio Legal

Public legal pages for the **Pomio** iOS app (Bundle ID: `com.pomodoro.six11`).

## App Store Connect URLs

After GitHub Pages is live:

- **Privacy Policy:** https://opheliasfather.github.io/Pomio-Legal/privacy-policy.html
- **Terms of Use:** https://opheliasfather.github.io/Pomio-Legal/terms-of-use.html

## Enable GitHub Pages (important)

`has_pages` must be turned on once in the repo settings:

1. Open: https://github.com/opheliasfather/Pomio-Legal/settings/pages
2. **Build and deployment → Source:** choose **Deploy from a branch** (not “GitHub Actions”).
3. **Branch:** `main` → folder **`/ (root)`** → **Save**.
4. Wait 1–3 minutes, then open the Privacy Policy URL above.

If you previously picked `gh-pages` or **GitHub Actions**, switch to **`main` / root** — all HTML files live on `main`.

## Regenerate pages

```bash
python3 generate_pages.py
git add -A && git commit -m "Update legal copy" && git push
```
