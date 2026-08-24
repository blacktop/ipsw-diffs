## promotedcontentd

> `/usr/libexec/promotedcontentd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`

```diff

-557.1.26.0.0
-  __TEXT.__text: 0x34eb5c
-  __TEXT.__auth_stubs: 0x57c0
+557.1.32.0.0
+  __TEXT.__text: 0x34c6a0
+  __TEXT.__auth_stubs: 0x5830
   __TEXT.__objc_stubs: 0x19980
-  __TEXT.__objc_methlist: 0x15210
-  __TEXT.__const: 0x7455a
+  __TEXT.__objc_methlist: 0x151e0
+  __TEXT.__const: 0x7437a
   __TEXT.__gcc_except_tab: 0x12a0
-  __TEXT.__cstring: 0x155e5
-  __TEXT.__objc_methname: 0x26dad
-  __TEXT.__oslogstring: 0x103ec
-  __TEXT.__objc_classname: 0x4bb7
-  __TEXT.__objc_methtype: 0x513d
-  __TEXT.__constg_swiftt: 0x61ec
-  __TEXT.__swift5_typeref: 0x41e8
-  __TEXT.__swift5_reflstr: 0x3656
-  __TEXT.__swift5_fieldmd: 0x47c4
+  __TEXT.__cstring: 0x15615
+  __TEXT.__objc_methname: 0x26d4d
+  __TEXT.__oslogstring: 0x1065c
+  __TEXT.__objc_classname: 0x4ba7
+  __TEXT.__objc_methtype: 0x514d
+  __TEXT.__constg_swiftt: 0x6184
+  __TEXT.__swift5_typeref: 0x41ae
+  __TEXT.__swift5_reflstr: 0x3636
+  __TEXT.__swift5_fieldmd: 0x4778
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_assocty: 0x3a8
   __TEXT.__swift5_proto: 0x7d8
-  __TEXT.__swift5_types: 0x598
-  __TEXT.__swift5_capture: 0x11ec
+  __TEXT.__swift5_types: 0x594
+  __TEXT.__swift5_capture: 0xfa8
   __TEXT.__swift5_protos: 0x124
-  __TEXT.__swift_as_entry: 0xe8
-  __TEXT.__swift_as_ret: 0x10c
-  __TEXT.__swift_as_cont: 0x258
+  __TEXT.__swift_as_entry: 0xd0
+  __TEXT.__swift_as_ret: 0xf8
+  __TEXT.__swift_as_cont: 0x244
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x6e30
-  __TEXT.__eh_frame: 0x495c
-  __DATA_CONST.__const: 0x168d0
-  __DATA_CONST.__cfstring: 0xf320
+  __TEXT.__unwind_info: 0x6d50
+  __TEXT.__eh_frame: 0x45ec
+  __DATA_CONST.__const: 0x163c8
+  __DATA_CONST.__cfstring: 0xf340
   __DATA_CONST.__objc_classlist: 0xfe8
   __DATA_CONST.__objc_catlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x310
+  __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x158
+  __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x738
   __DATA_CONST.__linkguard: 0x15
   __DATA_CONST.__objc_intobj: 0x19e0

   __DATA_CONST.__objc_dictobj: 0xa50
   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x2bf0
-  __DATA_CONST.__got: 0x1810
-  __DATA_CONST.__auth_ptr: 0x1528
-  __DATA.__objc_const: 0x2b3b8
-  __DATA.__objc_selrefs: 0x9398
+  __DATA_CONST.__auth_got: 0x2c28
+  __DATA_CONST.__got: 0x1830
+  __DATA_CONST.__auth_ptr: 0x1538
+  __DATA.__objc_const: 0x2b308
+  __DATA.__objc_selrefs: 0x9378
   __DATA.__objc_ivar: 0x1458
   __DATA.__objc_data: 0x97b8
-  __DATA.__data: 0xda48
+  __DATA.__data: 0xd8e8
   __DATA.__common: 0xc30
   __DATA.__bss: 0xcfb0
   - /AppleInternal/Library/Frameworks/TestHookService.framework/Versions/A/TestHookService

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11438
-  Symbols:   2192
+  Functions: 11373
+  Symbols:   2193
   CStrings:  11508
 
Symbols:
+ __exit
CStrings:
+ "@28@0:8B16@20"
+ "APMetricStorageEC can't be used outside of PCD."
+ "APMetricStorageEC created without a database manager; proto metric pipeline disabled."
+ "Metrics.ProtoMetricHandler"
+ "[EligibilitySnapshotRefresher] Built snapshot from a real keychain record (attempt %ld) — protoU13: %{bool}d, eduMode: %{bool}d, isChild: %{bool}d, maidEducation: %{bool}d"
+ "[EligibilitySnapshotRefresher] Keychain record still unavailable after %ld retries — leaving fail-closed default snapshot persisted; will correct on the next apAccountChanged"
+ "[EligibilitySnapshotRefresher] Keychain record unavailable (default account) — persisted fail-closed default snapshot (isChild=true); scheduling retries to correct once AdCore's write lands"
+ "[EligibilitySnapshotRefresher] Scheduling snapshot retry %ld/%ld in %fs"
+ "[EligibilitySnapshotRefresher] seedUserDefaultsIfMissing — UserDefaults empty; building initial snapshot from keychain + AdCore and writing"
+ "enableTelemetry=YES"
+ "initWithIsChild:databaseManager:"
+ "isPromotedContentDaemon"
+ "personalizedAdsEnforcementAgeSource"
- "APDatabasePathProvider"
- "[EligibilitySnapshotRefresher] Built snapshot — protoU13: %{bool}d, eduMode: %{bool}d, isChild: %{bool}d, maidEducation: %{bool}d"
- "[EligibilitySnapshotRefresher] seedUserDefaultsIfMissing — UserDefaults empty; building snapshot from keychain + AdCore and writing"
- "closeDatabaseConnection"
- "closeDatabaseConnectionWithCompletionHandler:"
- "connectionOpen"
- "databaseFilePath"
- "databaseName"
- "databasePath"
- "idleTimer"
- "migrationScriptsPath"
- "openDatabaseConnectionWithPath:"
- "v28@?0@\"NSNumber\"8B16@\"NSError\"20"
```
