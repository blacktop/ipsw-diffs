# Manual control for the automated firmware-diff pipeline (.github/workflows/diff.yml).
#
# Use these when a new iOS/macOS build drops and you want to start a diff now
# instead of waiting for the cron. Build numbers are resolved locally with
# `ipsw` so you can see exactly what will be diffed before dispatching to CI.
#
# Requires: just, gh (authenticated), jq, ipsw.

set shell := ["bash", "-euo", "pipefail", "-c"]

repo := "blacktop/ipsw-diffs"

# Show available recipes.
default:
    @just --list

# AppleDB device id used per OS — keep in sync with the workflow matrix.
_device os:
    @case "{{ os }}" in \
      iOS) echo "iPhone18,1" ;; \
      macOS) echo "Mac17,6" ;; \
      *) echo "unknown os '{{ os }}' (use 'iOS' or 'macOS')" >&2; exit 1 ;; \
    esac

# Latest version/build AppleDB has for an OS (iOS | macOS).
latest os:
    #!/usr/bin/env bash
    set -euo pipefail
    dev="$(just _device '{{ os }}')"
    ipsw dl appledb --os '{{ os }}' --device "$dev" --show-latest --no-color

# What each OS would diff next: recorded baseline (per major) vs AppleDB latest.
status:
    #!/usr/bin/env bash
    set -euo pipefail
    for os in iOS macOS; do
      dev="$(just _device "$os")"
      latest="$(ipsw dl appledb --os "$os" --device "$dev" --show-latest --no-color)"
      ver="$(jq -r '.version' <<<"$latest")"
      next="$(jq -r '.build' <<<"$latest")"
      major="$(grep -oE '^[0-9]+' <<<"$ver")"
      prev="$(jq -r --arg m "$major" '.[$m].build // empty' ".cache/${os}.json" 2>/dev/null || true)"
      if [ -z "$prev" ]; then
        state="NEW MAJOR ${major} (baseline would be seeded, no diff)"
      elif [ "$prev" = "$next" ]; then
        state="up to date"
      else
        state="PENDING: ${prev} -> ${next}"
      fi
      printf '%-6s %-16s latest=%s  %s\n' "$os" "$ver" "$next" "$state"
    done

# Kick off a diff for a freshly-dropped build (iOS | macOS).
#
# Resolves the baseline->latest pair locally for confirmation, then dispatches
# the workflow's auto-detect run, which re-derives the same pair and advances
# the cache on success.

# Start a diff for a freshly-dropped iOS|macOS build (auto-detect on CI).
diff os:
    #!/usr/bin/env bash
    set -euo pipefail
    os='{{ os }}'
    dev="$(just _device "$os")"
    latest="$(ipsw dl appledb --os "$os" --device "$dev" --show-latest --no-color)"
    ver="$(jq -r '.version' <<<"$latest")"
    next="$(jq -r '.build' <<<"$latest")"
    major="$(grep -oE '^[0-9]+' <<<"$ver")"
    prev="$(jq -r --arg m "$major" '.[$m].build // empty' ".cache/${os}.json" 2>/dev/null || true)"
    if [ -z "$prev" ]; then
      echo "No ${os} baseline for major ${major}; the workflow will seed it (no diff)." >&2
      echo "For a cross-major milestone diff, use: just diff-build ${os} <prev> ${next}" >&2
      exit 1
    fi
    if [ "$prev" = "$next" ]; then
      echo "${os} already current at ${ver} (${next}); nothing to diff."
      exit 0
    fi
    echo "${os}: ${prev} -> ${next}  (${ver}, major ${major})"
    read -rp "Dispatch this diff? [y/N] " ans
    case "$ans" in [yY]*) ;; *) echo "aborted"; exit 1 ;; esac
    gh workflow run Diff --repo '{{ repo }}' -f os="$os"
    echo "Dispatched. Follow it with: just watch"

# Dispatch an explicit diff of two known builds; use for backfills/milestones.
# Note: an explicit override does NOT advance the cache baseline.

# Dispatch an explicit prev->next diff (iOS|macOS); for backfills/milestones.
diff-build os prev next:
    #!/usr/bin/env bash
    set -euo pipefail
    echo "{{ os }}: {{ prev }} -> {{ next }} (explicit override)"
    read -rp "Dispatch this diff? [y/N] " ans
    case "$ans" in [yY]*) ;; *) echo "aborted"; exit 1 ;; esac
    gh workflow run Diff --repo '{{ repo }}' \
      -f os='{{ os }}' -f prev_build='{{ prev }}' -f next_build='{{ next }}'
    echo "Dispatched. Follow it with: just watch"

# List recent workflow runs.
runs:
    gh run list --repo '{{ repo }}' --workflow Diff --limit 10

# Watch the most recent workflow run until it finishes.
watch:
    gh run watch --repo '{{ repo }}' "$(gh run list --repo '{{ repo }}' --workflow Diff --limit 1 --json databaseId --jq '.[0].databaseId')"
