## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-4838.60.42.0.0
-  __TEXT.__text: 0x129474
-  __TEXT.__objc_methlist: 0xeabc
+4838.60.55.0.0
+  __TEXT.__text: 0x1299e8
+  __TEXT.__objc_methlist: 0xead4
   __TEXT.__const: 0x88a
-  __TEXT.__cstring: 0x15006
-  __TEXT.__gcc_except_tab: 0x8b64
+  __TEXT.__cstring: 0x151ad
+  __TEXT.__gcc_except_tab: 0x8b68
   __TEXT.__oslogstring: 0xe394
   __TEXT.__dlopen_cstrs: 0x793
-  __TEXT.__ustring: 0x288
+  __TEXT.__ustring: 0x2be
   __TEXT.__swift5_typeref: 0xb4
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_reflstr: 0x45

   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x6ee0
+  __TEXT.__unwind_info: 0x6f08
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x62a8
+  __DATA_CONST.__const: 0x62b0
   __DATA_CONST.__objc_classlist: 0x698
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7160
+  __DATA_CONST.__objc_selrefs: 0x7170
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0xab0
   __DATA_CONST.__got: 0xb20
-  __AUTH_CONST.__const: 0x1dc8
-  __AUTH_CONST.__cfstring: 0x11720
-  __AUTH_CONST.__objc_const: 0x25128
+  __AUTH_CONST.__const: 0x1de8
+  __AUTH_CONST.__cfstring: 0x11820
+  __AUTH_CONST.__objc_const: 0x25158
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__auth_got: 0xeb0
   __AUTH.__objc_data: 0x1a90
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x10d8
+  __DATA.__objc_ivar: 0x10dc
   __DATA.__data: 0x23f0
   __DATA.__common: 0x39
   __DATA_DIRTY.__objc_data: 0x2760

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 7491
-  Symbols:   11249
-  CStrings:  4076
+  Functions: 7501
+  Symbols:   11259
+  CStrings:  4088
 
Symbols:
+ -[FPProviderDomain owningApplicationIsOffloaded]
+ -[FPProviderDomain setOwningApplicationIsOffloaded:]
+ GCC_except_table91
+ _FPExcludedCloudDocsContainerQueryStringFragment
+ _FPExcludedRootContainersQueryStringFragment
+ _FPFeatureFlagIndexDomainRootLocationsIsEnabled
+ _FPIsFileProviderExtensionRecordIncludingOffloaded
+ _FPShouldOmitFileProviderIDFilter
+ _OBJC_IVAR_$_FPProviderDomain._owningApplicationIsOffloaded
+ ___fpfs_supports_offloadedDomainsAreVisible_block_invoke
+ _fpfs_supports_offloadedDomainsAreVisible
+ _fpfs_supports_offloadedDomainsAreVisible.feature_enabled
+ _fpfs_supports_offloadedDomainsAreVisible.once_token
- GCC_except_table115
- GCC_except_table90
- GCC_except_table95
CStrings:
+ "%@ && %@ && %@ && (%@)"
+ "(%@) && %@"
+ "(%@) && (%@) && (%@) && (%@)"
+ "(%@) && (%@) && (%@) && (%@) && (%@) && (%@)"
+ "(%@) && (%@) && ((%@) || ((%@) && (%@)))"
+ "((%@) && %@ && %@ && %@)"
+ "((kMDItemFileProviderID != \"%s\" && kMDItemFileProviderID != \"%s\") || kMDItemFileItemID != \"*/%@\")"
+ "(FPEvictable == \"1\") && (%@)"
+ "(kMDItemFavoriteRank == \"*\" && kMDItemContentTypeTree == \"public.folder\") && (%@) && (%@) && (%@)"
+ "(kMDItemFileItemID != \"*/%@\")"
+ "(kMDItemIsShared = \"1\") && (%@) && (%@) && (%@) && (FPIsTopLevelSharedItem = \"1\") && (%@) && (%@) && (%@)"
+ "(true) && (%@)"
+ "(⏹  application offloaded)"
+ ",appOffloaded"
+ ",offloaded"
+ "4838.60.55"
+ "<%@:%p id:\"%@\" name:\"%@\" urls(%d%s):%@ db:%@%@ state:%s%s%s%s%s%s%s%s%s%s features:%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%@>"
+ "BOOL FPIsAnyDocumentRecentlyUsed(NSArray<NSString *> *__strong _Nonnull, NSArray<NSString *> *__strong _Nonnull, NSArray<NSString *> *__strong _Nonnull)"
+ "DISCONNECTION_REASON_APPLICATION_OFFLOADED_%@"
+ "IndexDomainRootLocations"
+ "NSExtensionPointIdentifier"
+ "OffloadedDomainsAreVisible"
+ "_owningApplicationIsOffloaded"
- "%@ && %@ && (%@)"
- "(%@) && (%@) && (%@)"
- "(%@) && (%@) && (%@) && (%@) && (%@)"
- "(%@) && ((%@) || ((%@) && (%@)))"
- "((%@) && %@ && %@)"
- "(FPEvictable == \"1\")"
- "(kMDItemFavoriteRank == \"*\" && kMDItemContentTypeTree == \"public.folder\") && (%@) && (%@)"
- "(kMDItemIsShared = \"1\") && (%@) && (%@) && (%@) && (FPIsTopLevelSharedItem = \"1\") && (%@) && (%@)"
- "4838.60.42"
- "<%@:%p id:\"%@\" name:\"%@\" urls(%d%s):%@ db:%@%@ state:%s%s%s%s%s%s%s%s%s features:%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%@>"
- "BOOL FPIsAnyDocumentRecentlyUsed(NSArray<NSString *> *__strong, NSArray<NSString *> *__strong, NSArray<NSString *> *__strong)"
```
