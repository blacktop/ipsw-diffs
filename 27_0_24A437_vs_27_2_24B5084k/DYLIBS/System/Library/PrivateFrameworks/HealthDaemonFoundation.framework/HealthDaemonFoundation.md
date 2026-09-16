## HealthDaemonFoundation

> `/System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation`

```diff

-7027.0.72.2.7
-  __TEXT.__text: 0x7107c
-  __TEXT.__objc_methlist: 0x3d8c
-  __TEXT.__const: 0x2322
-  __TEXT.__cstring: 0x49ba
-  __TEXT.__oslogstring: 0x3696
-  __TEXT.__gcc_except_tab: 0x3034
-  __TEXT.__swift5_typeref: 0xc12
+7027.1.36.2.7
+  __TEXT.__text: 0x71d6c
+  __TEXT.__objc_methlist: 0x3dc4
+  __TEXT.__const: 0x2332
+  __TEXT.__cstring: 0x4ada
+  __TEXT.__oslogstring: 0x3726
+  __TEXT.__gcc_except_tab: 0x30a8
+  __TEXT.__swift5_typeref: 0xc40
   __TEXT.__swift5_reflstr: 0x88b
   __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__constg_swiftt: 0xbb0
+  __TEXT.__constg_swiftt: 0xbdc
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_fieldmd: 0x938
+  __TEXT.__swift5_fieldmd: 0x948
   __TEXT.__swift5_proto: 0x10c
   __TEXT.__swift5_types: 0xb8
-  __TEXT.__swift5_capture: 0x494
-  __TEXT.__swift5_protos: 0x2c
-  __TEXT.__swift5_types2: 0xc
+  __TEXT.__swift5_capture: 0x4e4
+  __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x30b8
-  __TEXT.__eh_frame: 0x14c8
+  __TEXT.__swift5_types2: 0xc
+  __TEXT.__unwind_info: 0x3110
+  __TEXT.__eh_frame: 0x1510
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21c8
+  __DATA_CONST.__objc_selrefs: 0x21e0
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x6d8
-  __AUTH_CONST.__const: 0x2820
-  __AUTH_CONST.__cfstring: 0x4060
+  __DATA_CONST.__got: 0x6e8
+  __AUTH_CONST.__const: 0x2960
+  __AUTH_CONST.__cfstring: 0x4100
   __AUTH_CONST.__objc_const: 0x86f0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1120
+  __AUTH_CONST.__auth_got: 0x1128
   __AUTH.__objc_data: 0xa60
   __AUTH.__data: 0x150
   __DATA.__objc_ivar: 0x56c
   __DATA.__data: 0xc50
   __DATA_DIRTY.__objc_data: 0x16d8
-  __DATA_DIRTY.__data: 0xa80
+  __DATA_DIRTY.__data: 0xa70
   __DATA_DIRTY.__bss: 0xd0
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3089
-  Symbols:   4709
-  CStrings:  901
+  Functions: 3118
+  Symbols:   4717
+  CStrings:  909
 
Symbols:
+ -[HDDatabaseAssertionManager _lock_releaseBackgroundAccessForFiles:]
+ -[HDSQLiteDatabase truncateWriteAheadLogWithBusyTimeout:contended:error:]
+ GCC_except_table109
+ GCC_except_table110
+ __CLASS_METHODS_HDFastPassBackgroundTask
+ __CLASS_METHODS_HDOneShotBackgroundTask
+ __ZZ25HDSQLiteEntityForPropertyE18propertyOwnerCache
+ __ZZ25HDSQLiteEntityForPropertyE23_propertyOwnerCacheLock
+ ___73-[HDSQLiteDatabase truncateWriteAheadLogWithBusyTimeout:contended:error:]_block_invoke
+ ___swift_project_boxed_opaque_existential_0
+ _objc_msgSend$mapTableWithKeyOptions:valueOptions:
+ _objc_msgSend$unsignedLongLongValue
+ _symbolic $s22HealthDaemonFoundation0B14PluginProviderP
- GCC_except_table105
- GCC_except_table106
- GCC_except_table112
- GCC_except_table67
- ___swift_destroy_boxed_opaque_existential_1Tm
CStrings:
+ "\" entitlement: got "
+ "%{public}@: Failed to open a database file to release the assertion: %d"
+ "/locked-access"
+ "<%@ %@ %@ %@%@ ctx:%ld%@: %@>"
+ "Cannot resolve process identifier for empty application identifier."
+ "Failed to continue activity"
+ "Failed to open a database file to request the assertion: %d"
+ "Failed to publish XPC event for %llu with error: %d"
+ "Failed to request the assertion: %d"
+ "HDXPCClient connection is nil; cannot validate \""
+ "PRAGMA wal_checkpoint(truncate)"
+ "Published XPC event for %llu"
- "<%@ %@ %@ %@%@: %@>"
- "Failed to publish XPC event for %ld with error: %d"
- "Published XPC event for %ld"
- "\x91"
```
