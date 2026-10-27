# Review notes: macOS Golden Gate 27.0.1 → 27.2

This comparison uses the public `UniversalMac_27.0.1_26A434_Restore.ipsw` and `UniversalMac_27.2_26B123_Restore.ipsw` images. The generated [`ipsw diff` index](README.md) links to per-binary changes. The firmware selection was **Mac15,6**; results for other hardware variants may differ.

## Reproducibility

| IPSW | SHA-256 |
| --- | --- |
| 27.0.1 (26A434) | `2f016638293c3e641b8b25391a76fbc16563b3711915a5551cf8aa0f5598a5c1` |
| 27.2 (26B123) | `6613b34e8589db2202a01ec37a2648afb141ece13428175183f8f3e38438534f` |

Both source ZIP archives passed CRC validation. The comparison was generated with [blacktop/ipsw](https://github.com/blacktop/ipsw) and its [ipsw-skill](https://github.com/blacktop/ipsw-skill) workflow. The source IPSWs are not included here.

## What changed

The generated report lists 284 updated kernel extensions and 2,523 updated dyld shared-cache libraries. The accessible filesystem comparison found 2,676 updated standalone Mach-O binaries, 37 additions, and 11 removals. At the outer IPSW level, 1,114 entries changed, 27 were added, and 55 were removed. These counts describe artifacts, not source-code changes or necessarily user-visible features.

Selected examples:

- The Shortcuts binary version moved from `5037.0.19` to `5114.0.6.204`; new `Show Actions` and `Show Describe` strings appear. See [Apple's Shortcuts release notes](https://support.apple.com/en-us/149045) for supported behavior.
- The WebKit version moved from `625.1.29.11.28` to `625.2.8.11.9`.
- `StorageKit`'s `-[SKIOMedia initWithDevName:]` function grew from 296 to 432 bytes and includes a new log message about refusing a nonconforming IO entry. This observation does not establish a connection to any particular security fix.

For the user-facing feature list, consult [Apple's macOS 27.2 release notes](https://support.apple.com/en-us/127257). [Apple's security content](https://support.apple.com/en-us/149521) is the authoritative list of published fixes. New private-framework names alone do not prove that their features are enabled.

## Offline line-by-line review

The [offline review archive](https://github.com/appleforever11/ipsw-diffs/releases/download/macos-27.0.1-27.2-26A434-26B123/macOS-Golden-Gate-27.0.1-vs-27.2-offline-review.tar.gz) contains a searchable HTML mirror of this report, 21,972 per-file text-diff browser pages, compressed raw text diffs, an IPSW entry-change CSV, and a representative assembly diff. Open `review/START-HERE.html` after extraction. The archive is attached to a release on the contributor's fork because those browser pages are substantially larger than the Markdown report.

## Scope and limits

Apple's private source code is not in an IPSW. `ipsw diff` compares firmware contents, binary metadata, symbols, and disassembly where available; the text browser compares extractable files line by line. Binary changes cannot be represented as the original source-code lines. Three protected template/visudo paths were inaccessible during filesystem extraction, and the Exclave image could not be mounted; those gaps are listed in the offline archive. No claim of complete Apple source coverage is made.
