## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/Versions/A/FileProvider`

```diff

-4838.0.125.0.0
-  __TEXT.__text: 0x1402c0
-  __TEXT.__objc_methlist: 0xe90c
+4838.41.1.0.0
+  __TEXT.__text: 0x140dd4
+  __TEXT.__objc_methlist: 0xe9c4
   __TEXT.__const: 0x8aa
-  __TEXT.__cstring: 0x1504f
-  __TEXT.__gcc_except_tab: 0x8958
+  __TEXT.__cstring: 0x15146
+  __TEXT.__gcc_except_tab: 0x8998
   __TEXT.__oslogstring: 0xe0ea
   __TEXT.__dlopen_cstrs: 0x6ba
-  __TEXT.__ustring: 0x21e
+  __TEXT.__ustring: 0x25a
   __TEXT.__swift5_typeref: 0xb4
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_reflstr: 0x45

   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x5848
+  __TEXT.__unwind_info: 0x58a0
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1668
+  __DATA_CONST.__const: 0x1698
   __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7020
+  __DATA_CONST.__objc_selrefs: 0x7090
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x548
   __DATA_CONST.__objc_arraydata: 0xab0
-  __DATA_CONST.__got: 0xb50
-  __AUTH_CONST.__const: 0x6fb8
-  __AUTH_CONST.__cfstring: 0x11960
-  __AUTH_CONST.__objc_const: 0x25028
+  __DATA_CONST.__got: 0xb58
+  __AUTH_CONST.__const: 0x7008
+  __AUTH_CONST.__cfstring: 0x11a40
+  __AUTH_CONST.__objc_const: 0x250c0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__auth_got: 0xf18
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x2490
+  __AUTH.__objc_data: 0x1a40
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x10cc
+  __DATA.__objc_ivar: 0x10c8
   __DATA.__data: 0x23f0
-  __DATA.__bss: 0xbc0
+  __DATA.__bss: 0xbd0
   __DATA.__common: 0x2b
-  __DATA_DIRTY.__objc_data: 0x1d10
+  __DATA_DIRTY.__objc_data: 0x2760
   __DATA_DIRTY.__data: 0x1
-  __DATA_DIRTY.__bss: 0x348
+  __DATA_DIRTY.__bss: 0x340
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 7528
-  Symbols:   14262
-  CStrings:  4085
+  Functions: 7549
+  Symbols:   14302
+  CStrings:  4094
 
Symbols:
+ +[FPProviderDomain migrateAllDomainsFromProviderIdentifier:toProviderIdentifier:completionHandler:]
+ -[FPAccessControlManager transferAccessToAllItemsFromBundle:toBundle:completionHandler:]
+ -[FPAccessControlManager withServicerProxy:]
+ -[FPItemManager _fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:]
+ -[FPItemManager _fetchParentItemIDsForItemID:recursively:synchronously:completionHandler:]
+ -[FPItemManager _fetchParentsForItemID:recursively:synchronously:completionHandler:]
+ -[FPItemManager fetchOperationServiceForProviderDomainID:synchronously:handler:]
+ -[FPItemManager parentItemIDsForItemID:recursively:error:]
+ -[FPItemManager parentsForItemID:recursively:error:]
+ -[FPProviderDomain spotlightIndexName]
+ -[FPProviderDomainChangesReceiver _t_setCachedProviderDomainsByID:]
+ -[NSFileProviderDomain migrationState]
+ -[NSFileProviderDomain setMigrationState:]
+ -[NSURL(FPFSHelpers) fp_URLWithNoFollow]
+ -[NSURL(FPFSHelpers) fp_hasNoFollow]
+ GCC_except_table138
+ GCC_except_table60
+ OBJC_IVAR_$_NSFileProviderDomain._migrationState
+ _FPKnownFolderTransitionedCategoryIdentifier
+ _FPKnownFolderTransitionedPreviousPathKey
+ _FPKnownFolderTransitionedShowActionIdentifier
+ _FPSpotlightIndexNamePrefix
+ _GSSTORAGE_FP_PROVIDER_CONTENT_VERSION_XATTR_NAME
+ __92-[FPItemManager _fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:]_block_invoke_3
+ ___44-[FPAccessControlManager withServicerProxy:]_block_invoke
+ ___52-[FPItemManager parentsForItemID:recursively:error:]_block_invoke
+ ___58-[FPItemManager parentItemIDsForItemID:recursively:error:]_block_invoke
+ ___80-[FPItemManager fetchOperationServiceForProviderDomainID:synchronously:handler:]_block_invoke
+ ___84-[FPItemManager _fetchParentsForItemID:recursively:synchronously:completionHandler:]_block_invoke
+ ___88-[FPAccessControlManager transferAccessToAllItemsFromBundle:toBundle:completionHandler:]_block_invoke
+ ___90-[FPItemManager _fetchParentItemIDsForItemID:recursively:synchronously:completionHandler:]_block_invoke
+ ___90-[FPItemManager _fetchParentItemIDsForItemID:recursively:synchronously:completionHandler:]_block_invoke_2
+ ___92-[FPItemManager _fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:]_block_invoke
+ ___92-[FPItemManager _fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:]_block_invoke_2
+ ___92-[FPItemManager _fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:]_block_invoke_3
+ ___99+[FPProviderDomain migrateAllDomainsFromProviderIdentifier:toProviderIdentifier:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e37_v16?0"<FPDAccessControlServicing>"8l
+ ___block_descriptor_56_e8_32s40s48bs_e37_v16?0"<FPDAccessControlServicing>"8l
+ ___block_descriptor_58_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_66_e8_32s40s48bs_e52_v24?0"FPService<FPXOperationService>"8"NSError"16l
+ ___fpfs_supports_appDomainMigration_block_invoke
+ _fpfs_supports_appDomainMigration
+ _kFileProviderSupersededAppReplacementEntitlement
+ _objc_msgSend$_fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:
+ _objc_msgSend$_fetchParentItemIDsForItemID:recursively:synchronously:completionHandler:
+ _objc_msgSend$_fetchParentsForItemID:recursively:synchronously:completionHandler:
+ _objc_msgSend$daemonConnectionOverride
+ _objc_msgSend$fetchOperationServiceForProviderDomainID:synchronously:handler:
+ _objc_msgSend$fp_URLWithNoFollow
+ _objc_msgSend$fp_hasNoFollow
+ _objc_msgSend$migrateAllDomainsFromProviderIdentifier:toProviderIdentifier:completionHandler:
+ _objc_msgSend$migrationState
+ _objc_msgSend$spotlightIndexName
+ _objc_msgSend$transferAccessToAllItemsFromBundle:toBundle:completionHandler:
+ _objc_msgSend$withServicerProxy:
+ fp_bundleRecord.kFPBundleRecordAssociatedObjectKey
+ fpfs_supports_appDomainMigration
+ fpfs_supports_appDomainMigration.feature_enabled
+ fpfs_supports_appDomainMigration.once_token
- -[FPItemManager _fetchHierarchyForItemID:recursively:depth:completionHandler:]
- GCC_except_table114
- OBJC_IVAR_$_FPXPCAutomaticErrorProxy._retainCounter
- OBJC_IVAR_$_FPXPCAutomaticErrorProxy._retainSelfWhileMessageIsPending
- __78-[FPItemManager _fetchHierarchyForItemID:recursively:depth:completionHandler:]_block_invoke_3
- ___66-[FPItemManager fetchOperationServiceForProviderDomainID:handler:]_block_invoke
- ___70-[FPItemManager _fetchParentsForItemID:recursively:completionHandler:]_block_invoke
- ___75-[FPItemManager fetchParentItemIDsForItemID:recursively:completionHandler:]_block_invoke
- ___75-[FPItemManager fetchParentItemIDsForItemID:recursively:completionHandler:]_block_invoke_2
- ___76-[FPAccessControlManager revokeAccessToAllItemsForBundle:completionHandler:]_block_invoke_3
- ___78-[FPItemManager _fetchHierarchyForItemID:recursively:depth:completionHandler:]_block_invoke
- ___78-[FPItemManager _fetchHierarchyForItemID:recursively:depth:completionHandler:]_block_invoke_2
- ___78-[FPItemManager _fetchHierarchyForItemID:recursively:depth:completionHandler:]_block_invoke_3
- ___80-[FPAccessControlManager bundleIdentifiersWithAccessToAnyItemCompletionHandler:]_block_invoke_2
- ___block_descriptor_56_e8_32s40s48bs_e49_v24?0"<FPDAccessControlServicing>"8"NSError"16l
- ___block_descriptor_57_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_65_e8_32s40s48bs_e52_v24?0"FPService<FPXOperationService>"8"NSError"16l
- _kFPBundleRecordAssociatedObjectKey
- _objc_msgSend$_fetchHierarchyForItemID:recursively:depth:completionHandler:
CStrings:
+ "(⏹  superseded app migration)"
+ ",migrating"
+ "4838.41.1"
+ "DISCONNECTION_REASON_SUPERSEDED_APP_MIGRATION"
+ "SHOW_FOLDER"
+ "access control servicer"
+ "appDomainMigration"
+ "com.apple.FileProvider.knownFolderTransitioned"
+ "com.apple.FileProvider/"
+ "com.apple.private.fileprovider.superseded-app-replacement"
+ "knownFolderTransitionedPreviousPath"
+ "v16@?0@\"<FPDAccessControlServicing>\"8"
- "4838.0.125"
- "com.apple.FileProvider/%@"
- "com.apple.genstore.fp_provider_cver#C"
```
