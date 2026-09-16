## Siri

> `/System/Library/DataClassMigrators/Siri.migrator/Siri`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-3600.68.61.11.11
-  __TEXT.__text: 0x3f14
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_stubs: 0xbc0
-  __TEXT.__objc_methlist: 0x1d0
+3605.23.1.1.1
+  __TEXT.__text: 0x40fc
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__objc_stubs: 0xb20
+  __TEXT.__objc_methlist: 0x1c4
   __TEXT.__const: 0x34
-  __TEXT.__cstring: 0x90c
-  __TEXT.__oslogstring: 0xa79
+  __TEXT.__cstring: 0x968
+  __TEXT.__oslogstring: 0xc42
   __TEXT.__objc_classname: 0xd
-  __TEXT.__objc_methname: 0x9d3
+  __TEXT.__objc_methname: 0x965
   __TEXT.__objc_methtype: 0x47
-  __TEXT.__unwind_info: 0x108
+  __TEXT.__unwind_info: 0x100
   __DATA_CONST.__const: 0x10
-  __DATA_CONST.__cfstring: 0x680
+  __DATA_CONST.__cfstring: 0x6e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x240
+  __DATA_CONST.__auth_got: 0x258
   __DATA_CONST.__got: 0x130
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x318
+  __DATA.__objc_selrefs: 0x2f0
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 40
-  Symbols:   121
-  CStrings:  234
+  Functions: 39
+  Symbols:   124
+  CStrings:  238
 
Symbols:
+ _AFIsHomePod
+ _AFIsLinwoodEnabled
+ _TCCAccessReset
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retain_x27
- _AFIsHorseman
- _objc_release_x25
- _objc_retain_x25
CStrings:
+ "%s App Clips: \"Learn from App Clips\" is OFF — adding com.apple.app-clips to deny set."
+ "%s App Clips: \"Learn from App Clips\" is ON (or unset/default) — not adding from this signal."
+ "%s Failed to reset kTCCServiceSiriAccess entries. Proceeding with migration anyway (writes are idempotent)."
+ "%s Failed to set TCC denial for bundle %@. [sources: LFTA=%@, ShowContent=%@, ShowApp=%@]"
+ "%s Marked %@ as denied in kTCCServiceSiriAccess. [sources: LFTA=%@, ShowContent=%@, ShowApp=%@]"
+ "%s Pre-migration reset check: hasV1Flag=%{BOOL}d, isLinwoodEnabled=%{BOOL}d"
+ "%s Resetting all kTCCServiceSiriAccess entries."
+ "%s Source counts — LFTA-off: %lu, Show-Content-off: %lu, Show-App-off: %lu, Locked (excluded): %lu, AppClips-Learn-off: %@, union to migrate: %lu."
+ "%s Successfully reset kTCCServiceSiriAccess entries."
+ "AppAccessExclusionListMigrationPerformedV2"
+ "SuggestionsLearnFromAppClips"
+ "com.apple.app-clips"
+ "isEnabledForDataclass:"
- "%s Failed to set TCC denial for bundle %@. [sources: LFTA=%@, ShowContent=%@, ShowApp=%@, Locked=%@]"
- "%s Marked %@ as denied in kTCCServiceSiriAccess. [sources: LFTA=%@, ShowContent=%@, ShowApp=%@, Locked=%@]"
- "%s Source counts — LFTA-off: %lu, Show-Content-off: %lu, Show-App-off: %lu, Locked: %lu, Hidden (excluded): %lu, union to migrate: %lu."
- "_bundleIdsWithHiddenApps"
- "cloudSyncEnabled"
- "hiddenAppBundleIdentifiers"
- "saveAccount:withCompletionHandler:"
- "set"
- "setEnabled:forDataclass:"
```
