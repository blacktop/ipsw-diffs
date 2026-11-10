## ecosystemd

> `/System/Library/PrivateFrameworks/Ecosystem.framework/Support/ecosystemd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__info_plist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-56.0.0.0.0
-  __TEXT.__text: 0xa912c
+59.3.0.0.0
+  __TEXT.__text: 0xa908c
   __TEXT.__auth_stubs: 0x1ee0
-  __TEXT.__objc_stubs: 0xa60
+  __TEXT.__objc_stubs: 0xaa0
   __TEXT.__objc_methlist: 0x134
-  __TEXT.__const: 0x45e2
-  __TEXT.__oslogstring: 0x5951
-  __TEXT.__cstring: 0x8736
+  __TEXT.__const: 0x4622
+  __TEXT.__oslogstring: 0x5bf1
+  __TEXT.__cstring: 0x8636
   __TEXT.__swift5_typeref: 0x1918
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x413
-  __TEXT.__objc_methname: 0x11e5
+  __TEXT.__objc_methname: 0x1205
   __TEXT.__objc_methtype: 0x239
   __TEXT.__constg_swiftt: 0x1c28
   __TEXT.__swift5_reflstr: 0x1d8b
   __TEXT.__swift5_fieldmd: 0x1bac
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_assocty: 0x168
-  __TEXT.__swift5_capture: 0x884
+  __TEXT.__swift5_capture: 0x7f8
   __TEXT.__swift5_proto: 0x2cc
   __TEXT.__swift5_types: 0x16c
   __TEXT.__swift5_protos: 0x38

   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0x4
   __TEXT.__info_plist: 0x41e
-  __TEXT.__unwind_info: 0x1c00
+  __TEXT.__unwind_info: 0x1bf0
   __TEXT.__eh_frame: 0x1d14
-  __DATA_CONST.__const: 0x4824
+  __DATA_CONST.__const: 0x475c
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__got: 0x460
   __DATA_CONST.__auth_ptr: 0x570
   __DATA.__objc_const: 0x19a8
-  __DATA.__objc_selrefs: 0x338
+  __DATA.__objc_selrefs: 0x348
   __DATA.__objc_data: 0x328
   __DATA.__data: 0x3288
   __DATA.__common: 0x98

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2058
+  Functions: 2047
   Symbols:   749
-  CStrings:  1290
+  CStrings:  1283
 
Symbols:
+ _$s10Foundation22_convertErrorToNSErrorySo0E0Cs0C0_pF
- _$sSo13os_log_type_ta0A0E4infoABvgZ
CStrings:
+ "<ecosystemd: PathParsers> ERROR: path not a proper URL: %{public}s"
+ "<ecosystemd: PathParsers>: handleSanitizedPath: Path escapes /Applications/: %{public}s"
+ "<ecosystemd: PathParsers>: handleSanitizedPath: Unable to find: %{public}s"
+ "<ecosystemd:PLDS> mirror to disk: failed to insert row for productKey: %{public}s uid: %{public}u"
+ "<ecosystemd:PLDS> shouldShowRosettaDeprecationWarning: launchedWithinSeconds: disabled (0)"
+ "<ecosystemd:SpotlightScanner> [SPOTLIGHT] found=%{public}ld knownFromLS=%{public}ld extracted=%{public}ld withMetadata=%{public}ld"
+ "<ecosystemd:UnsupportedAppsHandler> Inner binary (%{public}s) inside native parent (%{public}s) no longer x86-only or missing, excluding: %{public}s"
+ "<ecosystemd:UnsupportedAppsHandler> Rosetta app no longer on disk, excluding: %{public}s"
+ "<ecosystemd:UnsupportedAppsHandler> Rosetta app not in LS and not found/no longer x86_64-only on disk, excluding: %{public}s"
+ "<ecosystemd:UnsupportedAppsHandler> Rosetta app not in LS by path, bundleID matched different path (%{public}s), keeping: %{public}s"
+ "<ecosystemd:UnsupportedAppsHandler> Rosetta app not in LS, verified x86_64-only on disk: %{public}s"
+ "<ecosystemd:UnsupportedAppsHandler> Rosetta app still x86_64-only: %{public}s"
+ "<ecosystemd:UnsupportedAppsHandler> Rosetta app updated to universal, excluding: %{public}s"
+ "<ecosystemd:UnsupportedAppsHandler> Rosetta event for inner binary (%{public}s) inside native parent (%{public}s), verified still x86-only"
+ "<ecosystemd:UnsupportedAppsHandler> [APPS_LIST] uid=%{public}u admin=%{bool,public}d lsApps=%{public}ld lsByPath=%{public}ld lsByBundleID=%{public}ld rosettaRows=%{public}ld rosettaKept=%{public}ld rosettaProducts=%{public}ld afterLSMerge=%{public}ld spotlightAdded=%{public}ld afterBundleIDDedup=%{public}ld returned=%{public}ld"
+ "<ecosystemd:UnsupportedAppsHandler> [APPS_LIST] uid=%{public}u admin=%{bool,public}d lsComplete=false returned=%{public}ld"
+ "<ecosystemd:UnsupportedAppsHandler> [ROSETTA_FILTER] rows=%{public}ld kept=%{public}ld excludedMissing=%{public}ld excludedUniversal=%{public}ld excludedInnerBinaryNative=%{public}ld excludedUnresolvable=%{public}ld"
+ "<ecosystemd> Registered database sync timer (every %{public}ld seconds)"
+ "<ecosystemd> [SAVE_FAILED] signal=SIGHUP error=%@"
+ "<ecosystemd> [SAVE_FAILED] signal=SIGINT error=%@"
+ "<ecosystemd> [SAVE_FAILED] signal=SIGTERM error=%@"
+ "FAILED to create database directory at %{public}s error: %{public}s code=%{public}ld"
+ "Loaded %{public}ld mappings"
+ "Loaded %{public}ld mappings (%{public}ld invalid entries skipped)"
+ "Loaded %{public}ld product mapping rules"
+ "Loaded %{public}ld rules"
+ "Loaded %{public}ld rules (%{public}ld invalid entries skipped)"
+ "Loaded policy from Trial experiment (experiment:%{public}s deployment:%{public}s treatment:%{public}s)"
+ "Loaded policy from Trial rollout (rollout:%{public}s deployment:%{public}s factorPack:%{public}s)"
+ "[CATEGORY] code=%{public}ld name=%{public}s"
+ "[GPCACHE:CALLBACK] fetchInstalledGames() returned %{public}ld games for UID %{public}u"
+ "[GPCACHE:CALLBACK] fetchInstalledGames() returned nil for UID %{public}u!"
+ "[GPCACHE:CALLBACK] installedGamesDidChangeHandler FIRED for UID %{public}u - received %{public}ld games"
+ "[GPCACHE:INIT] Refusing to create library for invalid UID %{public}u"
+ "[GPCACHE:QUERY] Retrieved %{public}ld total apps from unified cache"
+ "[GPCACHE:STATS] uid=%{public}u received=%{public}ld new=%{public}ld upgraded=%{public}ld keptAsGame=%{public}ld updatedNonGame=%{public}ld totalApps=%{public}ld totalGames=%{public}ld"
+ "[GPCACHE:UPDATE] Processing %{public}ld apps from GamePolicy for UID %{public}u"
+ "[GPCACHE] Cache not initialized for '%{public}s'"
+ "[GPCACHE] No library for UID %{public}u"
+ "code"
+ "domain"
- "<ecosystemd: PathParsers> ERROR: path not a proper URL: %s"
- "<ecosystemd: PathParsers>: handleSanitizedPath: Path escapes /Applications/: %s"
- "<ecosystemd: PathParsers>: handleSanitizedPath: Unable to find: %s"
- "<ecosystemd:PLDS> mirror to disk: failed to insert row for productKey: %s uid: %u"
- "<ecosystemd:SpotlightScanner> %ld apps need metadata extraction (%ld already known from LS)"
- "<ecosystemd:SpotlightScanner> Scan complete: %ld new x86_64-only apps with metadata"
- "<ecosystemd:SpotlightScanner> Spotlight found %ld x86_64-only apps"
- "<ecosystemd:SpotlightScanner> Starting Spotlight scan for all apps"
- "<ecosystemd:UnsupportedAppsHandler> %ld Rosetta apps still x86_64-only"
- "<ecosystemd:UnsupportedAppsHandler> %ld total unique apps after LS merge"
- "<ecosystemd:UnsupportedAppsHandler> %ld total unique apps after Spotlight catch-all"
- "<ecosystemd:UnsupportedAppsHandler> %ld unique Rosetta apps after deduplication"
- "<ecosystemd:UnsupportedAppsHandler> Inner binary (%s) inside native parent (%s) no longer x86-only or missing, excluding: %s"
- "<ecosystemd:UnsupportedAppsHandler> Returning %ld total unsupported apps"
- "<ecosystemd:UnsupportedAppsHandler> Rosetta app no longer on disk, excluding: %s"
- "<ecosystemd:UnsupportedAppsHandler> Rosetta app not in LS and not found/no longer x86_64-only on disk, excluding: %s"
- "<ecosystemd:UnsupportedAppsHandler> Rosetta app not in LS by path, bundleID matched different path (%s), keeping: %s"
- "<ecosystemd:UnsupportedAppsHandler> Rosetta app not in LS, verified x86_64-only on disk: %s"
- "<ecosystemd:UnsupportedAppsHandler> Rosetta app still x86_64-only: %s"
- "<ecosystemd:UnsupportedAppsHandler> Rosetta app updated to universal, excluding: %s"
- "<ecosystemd:UnsupportedAppsHandler> Rosetta event for inner binary (%s) inside native parent (%s), verified still x86-only"
- "<ecosystemd> Failed to save database on SIGHUP: \\(error)"
- "<ecosystemd> Failed to save database on SIGINT: \\(error)"
- "<ecosystemd> Failed to save database on SIGTERM: \\(error)"
- "<ecosystemd> Registered database sync timer (every \\(Int(interval)) seconds)"
- "FAILED to create database directory at %s error: %@."
- "Loaded %ld mappings"
- "Loaded %ld mappings (%ld invalid entries skipped)"
- "Loaded %ld product mapping rules"
- "Loaded %ld rules"
- "Loaded %ld rules (%ld invalid entries skipped)"
- "Loaded policy from Trial experiment (experiment:%s deployment:%s treatment:%s)"
- "Loaded policy from Trial rollout (rollout:%s deployment:%s factorPack:%s)"
- "[GPCACHE:CALLBACK] fetchInstalledGames() returned %ld games for UID %u"
- "[GPCACHE:CALLBACK] fetchInstalledGames() returned nil for UID %u!"
- "[GPCACHE:CALLBACK] installedGamesDidChangeHandler FIRED for UID %u - received %ld games"
- "[GPCACHE:INIT] Refusing to create library for invalid UID %u"
- "[GPCACHE:QUERY] Retrieved %ld total apps from unified cache"
- "[GPCACHE:STATS]    Cache now initialized: true"
- "[GPCACHE:STATS]    Kept as game (protected): %ld"
- "[GPCACHE:STATS]    New apps: %ld"
- "[GPCACHE:STATS]    Total in cache: %ld apps (%ld games)"
- "[GPCACHE:STATS]    Updated non-games: %ld"
- "[GPCACHE:STATS]    Upgraded to game: %ld"
- "[GPCACHE:UPDATE] Finished processing for UID %u"
- "[GPCACHE:UPDATE] Processing %ld apps from GamePolicy for UID %u"
- "[GPCACHE] Cache not initialized for '%s'"
- "[GPCACHE] No library for UID %u"
```
