## HealthDaemonFoundation

> `/System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation`

```diff

-7027.1.45.2.4
-  __TEXT.__text: 0x73460
-  __TEXT.__objc_methlist: 0x3e0c
+7027.1.54.2.3
+  __TEXT.__text: 0x743c4
+  __TEXT.__objc_methlist: 0x3e34
   __TEXT.__const: 0x23a2
-  __TEXT.__cstring: 0x4b4b
-  __TEXT.__oslogstring: 0x3775
-  __TEXT.__gcc_except_tab: 0x30a8
+  __TEXT.__cstring: 0x4b6b
+  __TEXT.__oslogstring: 0x37e5
+  __TEXT.__gcc_except_tab: 0x3118
   __TEXT.__swift5_typeref: 0xd2c
   __TEXT.__swift5_reflstr: 0x90b
   __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__constg_swiftt: 0xce4
+  __TEXT.__constg_swiftt: 0xcec
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_fieldmd: 0xa04
   __TEXT.__swift5_proto: 0x100

   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_mpenum: 0x24
   __TEXT.__swift5_types2: 0xc
-  __TEXT.__unwind_info: 0x3180
+  __TEXT.__unwind_info: 0x31b8
   __TEXT.__eh_frame: 0x1548
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x11c0
+  __DATA_CONST.__const: 0x11e8
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21e0
+  __DATA_CONST.__objc_selrefs: 0x21f8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x6f0
   __AUTH_CONST.__const: 0x2a60
-  __AUTH_CONST.__cfstring: 0x4100
-  __AUTH_CONST.__objc_const: 0x8970
+  __AUTH_CONST.__cfstring: 0x4140
+  __AUTH_CONST.__objc_const: 0x8988
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3131
-  Symbols:   4006
-  CStrings:  912
+  Functions: 3144
+  Symbols:   4016
+  CStrings:  916
 
Symbols:
+ +[HDSQLiteSchemaEntity hasStaticJoinClauses]
+ -[HDSQLiteQueryDescriptor _uncachedJoinClauseForProperties:predicateJoinClauses:]
+ -[HDXPCProcess isFirstParty]
+ -[HDXPCProcess unitTest_copyProcessWithBundleIdentifier:]
+ GCC_except_table117
+ GCC_except_table120
+ GCC_except_table44
+ GCC_except_table67
+ GCC_except_table83
+ GCC_except_table88
+ GCC_except_table90
+ GCC_except_table96
+ __ZZL25_HDSQLiteCachedJoinClauseP10objc_classP7NSArrayIP8NSStringEU13block_pointerFS3_vEE15joinClauseCache
+ __ZZL25_HDSQLiteCachedJoinClauseP10objc_classP7NSArrayIP8NSStringEU13block_pointerFS3_vEE19joinClauseCacheLock
+ __ZZL25_HDSQLiteCachedJoinClauseP10objc_classP7NSArrayIP8NSStringEU13block_pointerFS3_vEE25reportedSaturatedEntities
+ ___52-[HDSQLiteQueryDescriptor _joinClauseForProperties:]_block_invoke
+ ___block_descriptor_56_ea8_32s40s48s_e15_"NSString"8?0ls32l8s40l8s48l8
- GCC_except_table113
- GCC_except_table118
- GCC_except_table84
- GCC_except_table87
- GCC_except_table89
- GCC_except_table92
- GCC_except_table95
CStrings:
+ "@\"NSString\"8@?0"
+ "Join clause memo reached its ceiling of %lu shapes for %{public}@; fragments for this entity are now rebuilt per query"
+ "[%s] Unable to open or prepare database due to error: %@"
+ "com.apple."
+ "com.appleinternal."
- "[%s] Unable to prepare database due to error: %@"
```
