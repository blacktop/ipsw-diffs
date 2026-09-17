## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/Versions/A/FileProvider`

```diff

-4838.0.125.0.0
-  __TEXT.__text: 0x13abec
-  __TEXT.__objc_methlist: 0xe90c
+4838.40.92.501.1
+  __TEXT.__text: 0x13b360
+  __TEXT.__objc_methlist: 0xe974
   __TEXT.__const: 0x8aa
-  __TEXT.__cstring: 0x1504f
-  __TEXT.__gcc_except_tab: 0x8958
+  __TEXT.__cstring: 0x150af
+  __TEXT.__gcc_except_tab: 0x8998
   __TEXT.__oslogstring: 0xe0ea
   __TEXT.__dlopen_cstrs: 0x6ba
   __TEXT.__ustring: 0x21e

   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x6e80
+  __TEXT.__unwind_info: 0x6ec0
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1668
+  __DATA_CONST.__const: 0x1688
   __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7020
+  __DATA_CONST.__objc_selrefs: 0x7068
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x548
   __DATA_CONST.__objc_arraydata: 0xab0
   __DATA_CONST.__got: 0xb50
   __AUTH_CONST.__const: 0x6fb8
-  __AUTH_CONST.__cfstring: 0x11960
-  __AUTH_CONST.__objc_const: 0x25028
+  __AUTH_CONST.__cfstring: 0x119c0
+  __AUTH_CONST.__objc_const: 0x24ff8
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__auth_got: 0xf18
   __AUTH.__objc_data: 0x2490
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x10cc
+  __DATA.__objc_ivar: 0x10c4
   __DATA.__data: 0x23f0
   __DATA.__common: 0x2b
   __DATA_DIRTY.__objc_data: 0x1d10

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 7528
-  Symbols:   14262
-  CStrings:  4085
+  Functions: 7539
+  Symbols:   14284
+  CStrings:  4088
 
Symbols:
+ -[FPItemManager _fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:]
+ -[FPItemManager _fetchParentItemIDsForItemID:recursively:synchronously:completionHandler:]
+ -[FPItemManager _fetchParentsForItemID:recursively:synchronously:completionHandler:]
+ -[FPItemManager fetchOperationServiceForProviderDomainID:synchronously:handler:]
+ -[FPItemManager parentItemIDsForItemID:recursively:error:]
+ -[FPItemManager parentsForItemID:recursively:error:]
+ -[FPProviderDomain spotlightIndexName]
+ -[FPProviderDomainChangesReceiver _t_setCachedProviderDomainsByID:]
+ -[NSURL(FPFSHelpers) fp_URLWithNoFollow]
+ -[NSURL(FPFSHelpers) fp_hasNoFollow]
+ GCC_except_table138
+ GCC_except_table60
+ _FPKnownFolderTransitionedCategoryIdentifier
+ _FPKnownFolderTransitionedPreviousPathKey
+ _FPKnownFolderTransitionedShowActionIdentifier
+ _FPSpotlightIndexNamePrefix
+ __92-[FPItemManager _fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:]_block_invoke_3
+ ___52-[FPItemManager parentsForItemID:recursively:error:]_block_invoke
+ ___58-[FPItemManager parentItemIDsForItemID:recursively:error:]_block_invoke
+ ___80-[FPItemManager fetchOperationServiceForProviderDomainID:synchronously:handler:]_block_invoke
+ ___84-[FPItemManager _fetchParentsForItemID:recursively:synchronously:completionHandler:]_block_invoke
+ ___90-[FPItemManager _fetchParentItemIDsForItemID:recursively:synchronously:completionHandler:]_block_invoke
+ ___90-[FPItemManager _fetchParentItemIDsForItemID:recursively:synchronously:completionHandler:]_block_invoke_2
+ ___92-[FPItemManager _fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:]_block_invoke
+ ___92-[FPItemManager _fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:]_block_invoke_2
+ ___92-[FPItemManager _fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:]_block_invoke_3
+ ___block_descriptor_58_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_66_e8_32s40s48bs_e52_v24?0"FPService<FPXOperationService>"8"NSError"16l
+ _objc_msgSend$_fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:
+ _objc_msgSend$_fetchParentItemIDsForItemID:recursively:synchronously:completionHandler:
+ _objc_msgSend$_fetchParentsForItemID:recursively:synchronously:completionHandler:
+ _objc_msgSend$daemonConnectionOverride
+ _objc_msgSend$fetchOperationServiceForProviderDomainID:synchronously:handler:
+ _objc_msgSend$fp_URLWithNoFollow
+ _objc_msgSend$fp_hasNoFollow
+ _objc_msgSend$spotlightIndexName
+ fp_bundleRecord.kFPBundleRecordAssociatedObjectKey
+ fpfs_is_seed_build.is_seed_build
- -[FPItemManager _fetchHierarchyForItemID:recursively:depth:completionHandler:]
- GCC_except_table114
- OBJC_IVAR_$_FPXPCAutomaticErrorProxy._retainCounter
- OBJC_IVAR_$_FPXPCAutomaticErrorProxy._retainSelfWhileMessageIsPending
- __78-[FPItemManager _fetchHierarchyForItemID:recursively:depth:completionHandler:]_block_invoke_3
- ___66-[FPItemManager fetchOperationServiceForProviderDomainID:handler:]_block_invoke
- ___70-[FPItemManager _fetchParentsForItemID:recursively:completionHandler:]_block_invoke
- ___75-[FPItemManager fetchParentItemIDsForItemID:recursively:completionHandler:]_block_invoke
- ___75-[FPItemManager fetchParentItemIDsForItemID:recursively:completionHandler:]_block_invoke_2
- ___78-[FPItemManager _fetchHierarchyForItemID:recursively:depth:completionHandler:]_block_invoke
- ___78-[FPItemManager _fetchHierarchyForItemID:recursively:depth:completionHandler:]_block_invoke_2
- ___78-[FPItemManager _fetchHierarchyForItemID:recursively:depth:completionHandler:]_block_invoke_3
- ___block_descriptor_57_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_65_e8_32s40s48bs_e52_v24?0"FPService<FPXOperationService>"8"NSError"16l
- _kFPBundleRecordAssociatedObjectKey
- _objc_msgSend$_fetchHierarchyForItemID:recursively:depth:completionHandler:
CStrings:
+ "4838.40.92.501.1"
+ "SHOW_FOLDER"
+ "com.apple.FileProvider.knownFolderTransitioned"
+ "com.apple.FileProvider/"
+ "knownFolderTransitionedPreviousPath"
- "4838.0.125"
- "com.apple.FileProvider/%@"
```
