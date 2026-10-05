## Siri

> `/System/Library/DataClassMigrators/Siri.migrator/Siri`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-3605.24.1.1.1
-  __TEXT.__text: 0x40fc
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x1c4
+3605.30.1.1.1
+  __TEXT.__text: 0x46bc
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_stubs: 0xc60
+  __TEXT.__objc_methlist: 0x218
   __TEXT.__const: 0x34
-  __TEXT.__cstring: 0x968
-  __TEXT.__oslogstring: 0xc42
+  __TEXT.__cstring: 0xa14
+  __TEXT.__oslogstring: 0xf28
   __TEXT.__objc_classname: 0xd
-  __TEXT.__objc_methname: 0x965
-  __TEXT.__objc_methtype: 0x47
-  __TEXT.__unwind_info: 0x100
+  __TEXT.__objc_methname: 0xbc6
+  __TEXT.__objc_methtype: 0x90
+  __TEXT.__unwind_info: 0x118
   __DATA_CONST.__const: 0x10
-  __DATA_CONST.__cfstring: 0x6e0
+  __DATA_CONST.__cfstring: 0x740
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x258
-  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__auth_got: 0x268
+  __DATA_CONST.__got: 0x138
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x2f0
+  __DATA.__objc_selrefs: 0x340
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 39
-  Symbols:   124
-  CStrings:  238
+  Functions: 46
+  Symbols:   126
+  CStrings:  262
 
Symbols:
+ _objc_release_x28
+ _objc_retain_x5
CStrings:
+ "%s App Access exclusion list migration has already been performed (isRestorePass=%{BOOL}d). Skipping."
+ "%s Marking restore-pass App Access exclusion list migration as complete."
+ "%s Not recording the backed-up App Access exclusion list marker (disposition=0x%lx, alreadyPresent=%{BOOL}d)."
+ "%s Pre-migration reset check: hasV1Flag=%{BOOL}d, isLinwoodEnabled=%{BOOL}d, isRestorePass=%{BOOL}d"
+ "%s Recording the backed-up App Access exclusion list marker so a restore from this device skips re-derivation."
+ "%s Restore-from-backup pass (restoredBackupBuildVersion=%@, backedUpMigratedMarker=%{BOOL}d) — the backup already carries a curated exclusion list. Leaving the restored kTCCServiceSiriAccess records alone."
+ "%s Restore-from-backup pass (restoredBackupBuildVersion=%@, backedUpMigratedMarker=%{BOOL}d) — the backup predates the exclusion list. Re-deriving even though the standard one-shot flag may be set."
+ "(unknown)"
+ "-[SiriMigrator _markAppAccessExclusionListMigratedInBackedUpDomainForDisposition:]"
+ "AppAccessExclusionListMigrated"
+ "AppAccessExclusionListRestoreMigrationPerformed"
+ "B24@0:8@16"
+ "B24@0:8I16B20"
+ "B28@0:8@16B24"
+ "_appAccessExclusionListMigrationActionForRestorePass:restoreMigrationAlreadyPerformed:migrationAlreadyPerformed:restoredBackupBuildVersion:hasBackedUpMigratedMarker:"
+ "_backupBuildVersionPredatesAppAccessExclusionList:"
+ "_markAppAccessExclusionListMigratedInBackedUpDomain"
+ "_markAppAccessExclusionListMigratedInBackedUpDomainForDisposition:"
+ "_markAppAccessExclusionListRestoreMigrationPerformed"
+ "_shouldRederiveAppAccessExclusionListForRestoredBackupBuildVersion:hasBackedUpMigratedMarker:"
+ "_shouldWriteBackedUpAppAccessExclusionListMarkerForDisposition:markerAlreadyPresent:"
+ "characterAtIndex:"
+ "length"
+ "q40@0:8B16B20B24@28B36"
+ "uppercaseString"
+ "v20@0:8I16"
- "%s One-time App Access exclusion list migration has already been performed. Skipping."
- "%s Pre-migration reset check: hasV1Flag=%{BOOL}d, isLinwoodEnabled=%{BOOL}d"
```
