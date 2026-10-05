## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-4838.40.92.502.1
-  __TEXT.__text: 0x1290c4
-  __TEXT.__objc_methlist: 0xea4c
-  __TEXT.__const: 0x89a
-  __TEXT.__cstring: 0x14f02
+4838.40.130.0.2
+  __TEXT.__text: 0x12940c
+  __TEXT.__objc_methlist: 0xeaa4
+  __TEXT.__const: 0x88a
+  __TEXT.__cstring: 0x14f9f
   __TEXT.__gcc_except_tab: 0x8b64
   __TEXT.__oslogstring: 0xe394
   __TEXT.__dlopen_cstrs: 0x793
-  __TEXT.__ustring: 0x21e
+  __TEXT.__ustring: 0x25a
   __TEXT.__swift5_typeref: 0xb4
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_reflstr: 0x45

   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x6eb8
+  __TEXT.__unwind_info: 0x6ee0
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6240
+  __DATA_CONST.__const: 0x62a0
   __DATA_CONST.__objc_classlist: 0x698
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7128
+  __DATA_CONST.__objc_selrefs: 0x7150
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0xab0
-  __DATA_CONST.__got: 0xb18
-  __AUTH_CONST.__const: 0x1da8
-  __AUTH_CONST.__cfstring: 0x11640
-  __AUTH_CONST.__objc_const: 0x25030
+  __DATA_CONST.__got: 0xb20
+  __AUTH_CONST.__const: 0x1dc8
+  __AUTH_CONST.__cfstring: 0x116c0
+  __AUTH_CONST.__objc_const: 0x250f8
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__auth_got: 0xeb0
   __AUTH.__objc_data: 0x1a90
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x10d0
+  __DATA.__objc_ivar: 0x10d4
   __DATA.__data: 0x23f0
   __DATA.__common: 0x39
   __DATA_DIRTY.__objc_data: 0x2760

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 7478
-  Symbols:   11232
-  CStrings:  4065
+  Functions: 7488
+  Symbols:   11246
+  CStrings:  4071
 
Symbols:
+ +[FPProviderDomain migrateAllDomainsFromProviderIdentifier:toProviderIdentifier:completionHandler:]
+ -[FPAccessControlManager transferAccessToAllItemsFromBundle:toBundle:completionHandler:]
+ -[FPAccessControlManager withServicerProxy:]
+ -[NSFileProviderDomain migrationState]
+ -[NSFileProviderDomain setMigrationState:]
+ _GSSTORAGE_FP_PROVIDER_CONTENT_VERSION_XATTR_NAME
+ _OBJC_IVAR_$_NSFileProviderDomain._migrationState
+ ___44-[FPAccessControlManager withServicerProxy:]_block_invoke
+ ___88-[FPAccessControlManager transferAccessToAllItemsFromBundle:toBundle:completionHandler:]_block_invoke
+ ___99+[FPProviderDomain migrateAllDomainsFromProviderIdentifier:toProviderIdentifier:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e37_v16?0"<FPDAccessControlServicing>"8ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e37_v16?0"<FPDAccessControlServicing>"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e37_v16?0"<FPDAccessControlServicing>"8ls32l8s48l8s40l8
+ ___fpfs_supports_appDomainMigration_block_invoke
+ _fpfs_supports_appDomainMigration
+ _fpfs_supports_appDomainMigration.feature_enabled
+ _fpfs_supports_appDomainMigration.once_token
+ _kFileProviderSupersededAppReplacementEntitlement
- GCC_except_table99
- ___76-[FPAccessControlManager revokeAccessToAllItemsForBundle:completionHandler:]_block_invoke_3
- ___80-[FPAccessControlManager bundleIdentifiersWithAccessToAnyItemCompletionHandler:]_block_invoke_2
- ___block_descriptor_56_e8_32s40s48bs_e49_v24?0"<FPDAccessControlServicing>"8"NSError"16ls48l8s32l8s40l8
CStrings:
+ "(⏹  superseded app migration)"
+ ",migrating"
+ "4838.40.130.0.2"
+ "DISCONNECTION_REASON_SUPERSEDED_APP_MIGRATION"
+ "access control servicer"
+ "appDomainMigration"
+ "com.apple.private.fileprovider.superseded-app-replacement"
+ "v16@?0@\"<FPDAccessControlServicing>\"8"
- "4838.40.92.502.1"
- "com.apple.genstore.fp_provider_cver#C"
```
