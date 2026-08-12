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
-  __TEXT.__text: 0x3dd98c
-  __TEXT.__auth_stubs: 0x5ce0
+557.1.32.0.0
+  __TEXT.__text: 0x3db3d0
+  __TEXT.__auth_stubs: 0x5d50
   __TEXT.__objc_stubs: 0x1a1e0
-  __TEXT.__objc_methlist: 0x15228
-  __TEXT.__const: 0x2b3aa
+  __TEXT.__objc_methlist: 0x151f8
+  __TEXT.__const: 0x2b1da
   __TEXT.__gcc_except_tab: 0x1348
-  __TEXT.__cstring: 0x15dd5
-  __TEXT.__objc_methname: 0x2708d
-  __TEXT.__oslogstring: 0x10fdc
-  __TEXT.__objc_classname: 0x4c17
-  __TEXT.__objc_methtype: 0x512d
-  __TEXT.__constg_swiftt: 0x6488
-  __TEXT.__swift5_typeref: 0x43a0
-  __TEXT.__swift5_reflstr: 0x3726
-  __TEXT.__swift5_fieldmd: 0x4a24
+  __TEXT.__cstring: 0x15e05
+  __TEXT.__objc_methname: 0x2701d
+  __TEXT.__oslogstring: 0x1123c
+  __TEXT.__objc_classname: 0x4c07
+  __TEXT.__objc_methtype: 0x513d
+  __TEXT.__constg_swiftt: 0x6420
+  __TEXT.__swift5_typeref: 0x4366
+  __TEXT.__swift5_reflstr: 0x3706
+  __TEXT.__swift5_fieldmd: 0x49d8
   __TEXT.__swift5_builtin: 0x168
   __TEXT.__swift5_assocty: 0x3d8
   __TEXT.__swift5_proto: 0x850
-  __TEXT.__swift5_types: 0x5cc
-  __TEXT.__swift5_capture: 0x12bc
+  __TEXT.__swift5_types: 0x5c8
+  __TEXT.__swift5_capture: 0x1078
   __TEXT.__swift5_protos: 0x124
-  __TEXT.__swift_as_entry: 0xf0
-  __TEXT.__swift_as_ret: 0x11c
-  __TEXT.__swift_as_cont: 0x26c
+  __TEXT.__swift_as_entry: 0xd8
+  __TEXT.__swift_as_ret: 0x108
+  __TEXT.__swift_as_cont: 0x258
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x7178
-  __TEXT.__eh_frame: 0x4c5c
-  __DATA_CONST.__const: 0x1c908
-  __DATA_CONST.__cfstring: 0xf7e0
+  __TEXT.__unwind_info: 0x70a0
+  __TEXT.__eh_frame: 0x48ec
+  __DATA_CONST.__const: 0x1c400
+  __DATA_CONST.__cfstring: 0xf800
   __DATA_CONST.__objc_classlist: 0xfe8
   __DATA_CONST.__objc_catlist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x310
+  __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x158
+  __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x738
   __DATA_CONST.__linkguard: 0x15
   __DATA_CONST.__objc_intobj: 0x1a28

   __DATA_CONST.__objc_dictobj: 0xa50
   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x2e80
-  __DATA_CONST.__got: 0x18b8
-  __DATA_CONST.__auth_ptr: 0x1608
-  __DATA.__objc_const: 0x2b448
-  __DATA.__objc_selrefs: 0x94a0
+  __DATA_CONST.__auth_got: 0x2eb8
+  __DATA_CONST.__got: 0x18d8
+  __DATA_CONST.__auth_ptr: 0x1618
+  __DATA.__objc_const: 0x2b398
+  __DATA.__objc_selrefs: 0x9480
   __DATA.__objc_ivar: 0x1458
   __DATA.__objc_data: 0x9848
-  __DATA.__data: 0xe6c8
+  __DATA.__data: 0xe578
   __DATA.__common: 0xd70
   __DATA.__bss: 0xdec0
   - /AppleInternal/Library/Frameworks/TestHookService.framework/TestHookService

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11808
-  Symbols:   2297
+  Functions: 11744
+  Symbols:   2298
   CStrings:  11663
 
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
