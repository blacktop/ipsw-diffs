# ipsw-diff social publisher

This package polls the public [`ipsw-diffs/catalog`](https://github.com/ipsw-diffs/catalog)
index, renders one 1600×900 card for each new immutable diff, and publishes it to X.
The workflow runs every five minutes, but calls X and OpenAI only when the catalog contains
a previously unseen entry.

The supplied brand art is always usable as a deterministic fallback. When `OPENAI_API_KEY`
is present, GPT-Image edits that art using only parsed diff facts; Pillow then draws the exact
release names, build identifiers, device, and counts. Generated text is never trusted.

## One-time setup

1. In the X developer console, create a project/app for the bot account, enable OAuth 1.0a
   user authentication with read/write permissions, and generate an access token after those
   permissions are enabled.
2. In `blacktop/ipsw-diffs`, create a GitHub Actions environment named `social`.
3. Ensure GitHub Issues are enabled; one bot-authored issue holds non-secret de-duplication state.
4. Add these environment secrets:

   - `X_API_KEY`
   - `X_API_SECRET`
   - `X_ACCESS_TOKEN`
   - `X_ACCESS_TOKEN_SECRET`
   - `OPENAI_API_KEY`

Do not give organization members write or admin access to this personal publisher repository.
GitHub does not reveal stored secret values in its UI, but someone who can change an authorized
workflow can attempt to exfiltrate them. Keep branch protection enabled, require review for
workflow changes, restrict the `social` environment to the default branch, and leave required
environment reviewers disabled so scheduled runs can proceed unattended. Pull requests from
forks do not receive these secrets, and this workflow has no `pull_request` trigger.

The first scheduled run creates a machine-managed GitHub issue and records the current immutable
catalog revision without posting. This prevents an accidental historical flood. Later runs compare
catalog revisions, enqueue only newly added IDs, and retain bounded pending work and recent X post
receipts. The issue body is public and never contains credentials.

## Operations

Render one exact entry without posting:

```fish
gh workflow run social.yml --repo blacktop/ipsw-diffs \
  -f mode=dry-run \
  -f entry_id=ios-27.0-24A5418b-24A5424a
```

The completed run includes an `ipsw-diff-social-preview` artifact retained for seven days.
An explicit immutable ID is required because `catalog.json` is grouped by filename rather than
chronological publication time.

Suppress all currently visible catalog entries (for example, after intentionally replacing the
state issue):

```fish
gh workflow run social.yml --repo blacktop/ipsw-diffs -f mode=bootstrap
```

Run locally without AI by omitting `OPENAI_API_KEY`:

```fish
uv sync --project social --locked --all-groups
uv run --project social ipsw-diff-social --mode dry-run \
  --entry-id ios-27.0-24A5418b-24A5424a \
  --output-dir /tmp/ipsw-social
open /tmp/ipsw-social/(path basename (find /tmp/ipsw-social -name '*.png' | tail -n 1))
```

If preparation or an X request has an ambiguous outcome, the entry remains in `pending` and later
queued entries stay publishable. Check the bot account, then edit the state issue: add the X post ID
to `posts` and remove the entry from `pending` if it succeeded, or move the entry ID from `pending`
back into `queue` to retry. This manual step intentionally favors no duplicate posts.

Mastodon and Bluesky can later be added as publisher adapters while sharing catalog detection,
rendering, and state. Give each network separate credentials and per-network post state.
