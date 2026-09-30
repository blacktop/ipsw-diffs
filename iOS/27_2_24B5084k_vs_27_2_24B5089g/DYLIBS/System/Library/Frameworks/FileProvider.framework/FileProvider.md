## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-4838.40.53.502.1
-  __TEXT.__text: 0x128a40
-  __TEXT.__objc_methlist: 0xe9f4
+4838.40.92.502.1
+  __TEXT.__text: 0x1290c4
+  __TEXT.__objc_methlist: 0xea4c
   __TEXT.__const: 0x89a
-  __TEXT.__cstring: 0x14ea3
-  __TEXT.__gcc_except_tab: 0x8b34
+  __TEXT.__cstring: 0x14f02
+  __TEXT.__gcc_except_tab: 0x8b64
   __TEXT.__oslogstring: 0xe394
   __TEXT.__dlopen_cstrs: 0x793
   __TEXT.__ustring: 0x21e

   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x6e88
+  __TEXT.__unwind_info: 0x6eb8
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6228
+  __DATA_CONST.__const: 0x6240
   __DATA_CONST.__objc_classlist: 0x698
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x70f0
+  __DATA_CONST.__objc_selrefs: 0x7128
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0xab0
   __DATA_CONST.__got: 0xb18
   __AUTH_CONST.__const: 0x1da8
-  __AUTH_CONST.__cfstring: 0x115e0
+  __AUTH_CONST.__cfstring: 0x11640
   __AUTH_CONST.__objc_const: 0x25030
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__auth_got: 0xeb0
-  __AUTH.__objc_data: 0x25f8
+  __AUTH.__objc_data: 0x1a90
   __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x10d0
   __DATA.__data: 0x23f0
   __DATA.__common: 0x39
-  __DATA_DIRTY.__objc_data: 0x1bf8
+  __DATA_DIRTY.__objc_data: 0x2760
   __DATA_DIRTY.__data: 0x1
-  __DATA_DIRTY.__bss: 0x2e8
+  __DATA_DIRTY.__bss: 0x2d0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 7469
-  Symbols:   13849
-  CStrings:  4062
+  Functions: 7478
+  Symbols:   13866
+  CStrings:  4065
 
Symbols:
+ -[FPItemManager _fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:]
+ -[FPItemManager _fetchParentItemIDsForItemID:recursively:synchronously:completionHandler:]
+ -[FPItemManager _fetchParentsForItemID:recursively:synchronously:completionHandler:]
+ -[FPItemManager fetchOperationServiceForProviderDomainID:synchronously:handler:]
+ -[FPItemManager parentItemIDsForItemID:recursively:error:]
+ -[FPItemManager parentsForItemID:recursively:error:]
+ -[NSURL(FPFSHelpers) fp_URLWithNoFollow]
+ -[NSURL(FPFSHelpers) fp_hasNoFollow]
+ GCC_except_table144
+ _FPKnownFolderTransitionedCategoryIdentifier
+ _FPKnownFolderTransitionedPreviousPathKey
+ _FPKnownFolderTransitionedShowActionIdentifier
+ ___52-[FPItemManager parentsForItemID:recursively:error:]_block_invoke
+ ___58-[FPItemManager parentItemIDsForItemID:recursively:error:]_block_invoke
+ ___80-[FPItemManager fetchOperationServiceForProviderDomainID:synchronously:handler:]_block_invoke
+ ___84-[FPItemManager _fetchParentsForItemID:recursively:synchronously:completionHandler:]_block_invoke
+ ___90-[FPItemManager _fetchParentItemIDsForItemID:recursively:synchronously:completionHandler:]_block_invoke
+ ___90-[FPItemManager _fetchParentItemIDsForItemID:recursively:synchronously:completionHandler:]_block_invoke_2
+ ___92-[FPItemManager _fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:]_block_invoke
+ ___92-[FPItemManager _fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:]_block_invoke_2
+ ___92-[FPItemManager _fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:]_block_invoke_3
+ ___block_descriptor_58_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_66_e8_32s40s48bs_e52_v24?0"FPService<FPXOperationService>"8"NSError"16ls48l8s32l8s40l8
+ _objc_msgSend$_fetchHierarchyForItemID:recursively:synchronously:depth:completionHandler:
+ _objc_msgSend$_fetchParentItemIDsForItemID:recursively:synchronously:completionHandler:
+ _objc_msgSend$_fetchParentsForItemID:recursively:synchronously:completionHandler:
+ _objc_msgSend$daemonConnectionOverride
+ _objc_msgSend$fetchOperationServiceForProviderDomainID:synchronously:handler:
+ _objc_msgSend$fp_URLWithNoFollow
+ _objc_msgSend$fp_hasNoFollow
- -[FPItemManager _fetchHierarchyForItemID:recursively:depth:completionHandler:]
- GCC_except_table104
- GCC_except_table137
- ___66-[FPItemManager fetchOperationServiceForProviderDomainID:handler:]_block_invoke
- ___70-[FPItemManager _fetchParentsForItemID:recursively:completionHandler:]_block_invoke
- ___75-[FPItemManager fetchParentItemIDsForItemID:recursively:completionHandler:]_block_invoke
- ___75-[FPItemManager fetchParentItemIDsForItemID:recursively:completionHandler:]_block_invoke_2
- ___78-[FPItemManager _fetchHierarchyForItemID:recursively:depth:completionHandler:]_block_invoke
- ___78-[FPItemManager _fetchHierarchyForItemID:recursively:depth:completionHandler:]_block_invoke_2
- ___78-[FPItemManager _fetchHierarchyForItemID:recursively:depth:completionHandler:]_block_invoke_3
- ___block_descriptor_57_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
- ___block_descriptor_65_e8_32s40s48bs_e52_v24?0"FPService<FPXOperationService>"8"NSError"16ls48l8s32l8s40l8
- _objc_msgSend$_fetchHierarchyForItemID:recursively:depth:completionHandler:
CStrings:
+ "4838.40.92.502.1"
+ "SHOW_FOLDER"
+ "com.apple.FileProvider.knownFolderTransitioned"
+ "knownFolderTransitionedPreviousPath"
- "4838.40.53.502.1"
```
