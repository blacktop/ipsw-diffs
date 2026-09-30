## HealthDaemonFoundation

> `/System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/Versions/A/HealthDaemonFoundation`

```diff

-7027.0.72.1.1
-  __TEXT.__text: 0x7527c
-  __TEXT.__objc_methlist: 0x3d8c
-  __TEXT.__const: 0x22f2
-  __TEXT.__cstring: 0x496a
-  __TEXT.__oslogstring: 0x35f6
-  __TEXT.__gcc_except_tab: 0x3010
-  __TEXT.__swift5_typeref: 0xc12
+7027.1.36.1.2
+  __TEXT.__text: 0x7600c
+  __TEXT.__objc_methlist: 0x3dc4
+  __TEXT.__const: 0x2302
+  __TEXT.__cstring: 0x4a8a
+  __TEXT.__oslogstring: 0x3686
+  __TEXT.__gcc_except_tab: 0x3084
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
-  __TEXT.__unwind_info: 0x30e8
-  __TEXT.__eh_frame: 0x1490
+  __TEXT.__swift5_types2: 0xc
+  __TEXT.__unwind_info: 0x3138
+  __TEXT.__eh_frame: 0x14d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2178
+  __DATA_CONST.__objc_selrefs: 0x2190
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x698
-  __AUTH_CONST.__const: 0x3688
-  __AUTH_CONST.__cfstring: 0x4000
+  __DATA_CONST.__got: 0x6a8
+  __AUTH_CONST.__const: 0x37c8
+  __AUTH_CONST.__cfstring: 0x40a0
   __AUTH_CONST.__objc_const: 0x86d0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xef0
+  __AUTH_CONST.__auth_got: 0xef8
   __AUTH.__objc_data: 0xa60
   __AUTH.__data: 0x150
   __DATA.__objc_ivar: 0x568

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3126
-  Symbols:   4680
-  CStrings:  895
+  Functions: 3156
+  Symbols:   4688
+  CStrings:  903
 
Symbols:
+ -[HDDatabaseAssertionManager _lock_releaseBackgroundAccessForFiles:]
+ -[HDSQLiteDatabase truncateWriteAheadLogWithBusyTimeout:contended:error:]
+ GCC_except_table117
+ GCC_except_table122
+ GCC_except_table94
+ __CLASS_METHODS_HDFastPassBackgroundTask
+ __CLASS_METHODS_HDOneShotBackgroundTask
+ __ZZ25HDSQLiteEntityForPropertyE18propertyOwnerCache
+ __ZZ25HDSQLiteEntityForPropertyE23_propertyOwnerCacheLock
+ ___73-[HDSQLiteDatabase truncateWriteAheadLogWithBusyTimeout:contended:error:]_block_invoke
+ ___swift_project_boxed_opaque_existential_0
+ _objc_msgSend$mapTableWithKeyOptions:valueOptions:
+ _objc_msgSend$unsignedLongLongValue
+ _symbolic $s22HealthDaemonFoundation0B14PluginProviderP
- GCC_except_table115
- GCC_except_table118
- GCC_except_table119
- GCC_except_table78
- GCC_except_table79
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
