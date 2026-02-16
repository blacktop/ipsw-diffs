## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-3882.82.1.0.0
-  __TEXT.__text: 0x133428
-  __TEXT.__auth_stubs: 0x1d30
-  __TEXT.__objc_methlist: 0xe5ac
+4018.100.236.0.0
+  __TEXT.__text: 0x13a43c
+  __TEXT.__auth_stubs: 0x1ce0
+  __TEXT.__objc_methlist: 0xe6f4
   __TEXT.__const: 0x88a
-  __TEXT.__gcc_except_tab: 0xa3f0
-  __TEXT.__cstring: 0x145f2
-  __TEXT.__oslogstring: 0xdcfa
-  __TEXT.__dlopen_cstrs: 0x79f
+  __TEXT.__gcc_except_tab: 0x9cf8
+  __TEXT.__cstring: 0x14ac4
+  __TEXT.__oslogstring: 0xdea1
+  __TEXT.__dlopen_cstrs: 0x793
   __TEXT.__ustring: 0x21e
   __TEXT.__swift5_typeref: 0xb4
   __TEXT.__constg_swiftt: 0x60

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0x5990
+  __TEXT.__unwind_info: 0x5d40
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_classname: 0x2045
-  __TEXT.__objc_methname: 0x23fa5
-  __TEXT.__objc_methtype: 0x6910
-  __TEXT.__objc_stubs: 0x13fe0
+  __TEXT.__objc_methname: 0x24475
+  __TEXT.__objc_methtype: 0x69e2
+  __TEXT.__objc_stubs: 0x14240
   __DATA_CONST.__got: 0xac0
-  __DATA_CONST.__const: 0x6098
+  __DATA_CONST.__const: 0x6100
   __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6de0
+  __DATA_CONST.__objc_selrefs: 0x6ea0
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0xab0
-  __AUTH_CONST.__auth_got: 0xea8
-  __AUTH_CONST.__const: 0x1ca8
-  __AUTH_CONST.__cfstring: 0x111a0
-  __AUTH_CONST.__objc_const: 0x24840
+  __AUTH_CONST.__auth_got: 0xe80
+  __AUTH_CONST.__const: 0x1cc8
+  __AUTH_CONST.__cfstring: 0x11360
+  __AUTH_CONST.__objc_const: 0x24a38
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x198
-  __AUTH.__objc_data: 0x500
+  __AUTH.__objc_data: 0x4b0
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x1088
+  __DATA.__objc_ivar: 0x10a0
   __DATA.__data: 0x20c8
-  __DATA.__bss: 0xac0
+  __DATA.__bss: 0xae0
   __DATA.__common: 0x39
-  __DATA_DIRTY.__objc_data: 0x3ca0
+  __DATA_DIRTY.__objc_data: 0x3cf0
   __DATA_DIRTY.__data: 0x2c1
   __DATA_DIRTY.__bss: 0x3c0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: AA2B3101-41B0-3E1A-8832-104B94023C61
-  Functions: 7274
-  Symbols:   23526
-  CStrings:  12304
+  UUID: A6ED1382-3865-3BD3-9CE9-36A29B0EAEF8
+  Functions: 7381
+  Symbols:   24077
+  CStrings:  12380
 
Symbols:
+ +[NSURL(CopyFile) copyfileFlagsForSourceMode:sourceDevID:targetDevID:rootDevID:replacePlaceholder:]
+ -[FPDaemonConnection sendTelemetryWithCompletionHandler:]
+ -[FPFetchRegularItemThumbnailsOperation initWithDictionary:desiredSizeToScale:itemManager:operationServicer:]
+ -[FPFetchThumbnailsOperation initWithItem:versions:desiredSize:screenScale:itemManager:operationServicer:]
+ -[FPItem effectiveNamespacePolicy]
+ -[FPItem inheritedNamespacePolicy]
+ -[FPItem namespacePolicy]
+ -[FPItem overrideFields:ofItem:].cold.67
+ -[FPItem overrideFields:ofItem:].cold.68
+ -[FPItem overrideFields:ofItem:].cold.69
+ -[FPItem setEffectiveNamespacePolicy:]
+ -[FPItem setInheritedNamespacePolicy:]
+ -[FPItem setNamespacePolicy:]
+ -[FPItemManager _fetchURLForItemID:creatingPlaceholderIfMissing:synchronously:completionHandlerWithInfo:]
+ -[FPItemManager fetchOperationServiceForProviderDomainID:handler:].cold.1
+ -[FPItemManager hasEnumerateEntitlement]
+ -[FPItemManager hasEnumerateEntitlement].cold.1
+ -[FPItemManager thumbnailsFetchOperationForItem:withVersions:withSize:scale:operationServicer:]
+ -[FPItemManager urlForItem:creatingPlaceholderIfMissing:error:]
+ -[FPItemManager urlForItem:error:]
+ -[FPItemManager urlForItemID:creatingPlaceholderIfMissing:error:]
+ -[FPItemManager urlForItemID:error:]
+ -[FPProviderDomain hasItemsWithPermissionsIssuesToRepair]
+ -[FPProviderDomain launchItemsPermissionsRepairWithCompletionHandler:]
+ -[FPProviderDomain setHasItemsWithPermissionsIssuesToRepair:]
+ -[FPSpotlightIndexer reportDonationProgress:completionHandler:]
+ -[FPXServiceDescriptor description]
+ -[NSError(FPAdditions) fp_isPermissionError]
+ -[NSInvocation(FPExtensions) fp_lastErrorOfCompletionHandler]
+ -[NSURL(FPFSHelpers) fp_URLWithoutNoFollow]
+ GCC_except_table100
+ GCC_except_table104
+ GCC_except_table291
+ GCC_except_table300
+ GCC_except_table310
+ GCC_except_table317
+ GCC_except_table320
+ GCC_except_table324
+ GCC_except_table326
+ GCC_except_table332
+ GCC_except_table340
+ GCC_except_table342
+ GCC_except_table346
+ GCC_except_table350
+ GCC_except_table352
+ GCC_except_table355
+ GCC_except_table357
+ GCC_except_table361
+ GCC_except_table368
+ GCC_except_table374
+ GCC_except_table376
+ GCC_except_table383
+ GCC_except_table388
+ GCC_except_table391
+ GCC_except_table410
+ GCC_except_table412
+ GCC_except_table414
+ GCC_except_table427
+ GCC_except_table429
+ GCC_except_table433
+ GCC_except_table74
+ _FPExtractFrameworkNameFromPath
+ _FPGetCallingFramework
+ _FPIsAddressWithinFileProviderFramework
+ _OBJC_IVAR_$_FPFetchRegularItemThumbnailsOperation._servicer
+ _OBJC_IVAR_$_FPFetchThumbnailsOperation._servicer
+ _OBJC_IVAR_$_FPItem._effectiveNamespacePolicy
+ _OBJC_IVAR_$_FPItem._inheritedNamespacePolicy
+ _OBJC_IVAR_$_FPItem._namespacePolicy
+ _OBJC_IVAR_$_FPProviderDomain._hasItemsWithPermissionsIssuesToRepair
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _SpotlightIndexLibrary
+ _SpotlightIndexLibrary.cold.1
+ _SpotlightIndexLibraryCore.frameworkLibrary
+ ___105-[FPItemManager _fetchURLForItemID:creatingPlaceholderIfMissing:synchronously:completionHandlerWithInfo:]_block_invoke
+ ___37-[FPListRemoteVersionsOperation main]_block_invoke.16
+ ___37-[FPListRemoteVersionsOperation main]_block_invoke.7
+ ___37-[FPListRemoteVersionsOperation main]_block_invoke_3
+ ___40-[FPItemManager hasEnumerateEntitlement]_block_invoke
+ ___40-[FPItemManager hasEnumerateEntitlement]_block_invoke.cold.1
+ ___45-[FPFetchRegularItemThumbnailsOperation main]_block_invoke_3
+ ___63-[FPItemManager urlForItem:creatingPlaceholderIfMissing:error:]_block_invoke
+ ___63-[FPSpotlightIndexer reportDonationProgress:completionHandler:]_block_invoke
+ ___63-[FPSpotlightIndexer reportDonationProgress:completionHandler:]_block_invoke.cold.1
+ ___63-[FPSpotlightIndexer reportDonationProgress:completionHandler:]_block_invoke.cold.2
+ ___65-[FPItemManager urlForItemID:creatingPlaceholderIfMissing:error:]_block_invoke
+ ___FILEPROVIDER_BAD_NAMESPACE_POLICY__
+ ___SpotlightIndexLibraryCore_block_invoke
+ ___block_descriptor_243_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_40_e8_32s_e40_v16?0"FPService<FPXOperationService>"8ls32l8
+ ___block_descriptor_48_e8_32r40r_e30_v28?0"NSURL"8B16"NSError"20lr32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e40_v32?0"FPItem"8"NSArray"16"NSError"24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e30_v28?0"NSURL"8B16"NSError"20ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v24?0Q8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e109_v48?0"<FPXOperationService>"8"NSXPCListenerEndpoint"16"<FPDLifetimeServicing>"24"NSString"32"NSError"40ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.231
+ ___block_literal_global.263
+ ___block_literal_global.301
+ ___block_literal_global.324
+ ___block_literal_global.436
+ ___block_literal_global.445
+ ___block_literal_global.509
+ ___block_literal_global.51
+ ___block_literal_global.591
+ ___block_literal_global.593
+ ___fpfs_supports_items_permissions_repair_block_invoke
+ ___fpfs_supports_namespace_policy_block_invoke
+ _audit_stringSpotlightIndex
+ _dyld_image_header_containing_address
+ _fpfs_is_seed_build.is_seed_build
+ _fpfs_remove_sharing_xattrs
+ _fpfs_remove_sharing_xattrs.cold.1
+ _fpfs_remove_sharing_xattrs.cold.2
+ _fpfs_remove_sharing_xattrs.cold.3
+ _fpfs_remove_sharing_xattrs.cold.4
+ _fpfs_supports_items_permissions_repair
+ _fpfs_supports_items_permissions_repair.cold.1
+ _fpfs_supports_items_permissions_repair.feature_enabled
+ _fpfs_supports_items_permissions_repair.once_token
+ _fpfs_supports_namespace_policy
+ _fpfs_supports_namespace_policy.cold.1
+ _fpfs_supports_namespace_policy.feature_enabled
+ _fpfs_supports_namespace_policy.once_token
+ _hasEnumerateEntitlement.isEntitled
+ _hasEnumerateEntitlement.onceToken
+ _kFileProviderLaunchItemsPermissionsRepairEntitlement
+ _objc_msgSend$_fetchURLForItemID:creatingPlaceholderIfMissing:synchronously:completionHandlerWithInfo:
+ _objc_msgSend$checkDomainsCanBeStored:onVolumeAtURL:unsupportedReason:error:
+ _objc_msgSend$copyfileFlagsForSourceMode:sourceDevID:targetDevID:rootDevID:replacePlaceholder:
+ _objc_msgSend$effectiveNamespacePolicy
+ _objc_msgSend$fp_URLWithoutNoFollow
+ _objc_msgSend$fp_isPermissionError
+ _objc_msgSend$fp_lastErrorOfCompletionHandler
+ _objc_msgSend$hasEnumerateEntitlement
+ _objc_msgSend$inheritedNamespacePolicy
+ _objc_msgSend$initWithDictionary:desiredSizeToScale:itemManager:operationServicer:
+ _objc_msgSend$initWithItem:versions:desiredSize:screenScale:itemManager:operationServicer:
+ _objc_msgSend$namespacePolicy
+ _objc_msgSend$reportDonationProgress:completionHandler:
+ _objc_msgSend$sendTelemetryWithCompletionHandler:
+ _objc_msgSend$setEffectiveNamespacePolicy:
+ _objc_msgSend$setInheritedNamespacePolicy:
+ _objc_msgSend$setNamespacePolicy:
+ _objc_msgSend$startAccessingOperationServiceForItemAtURL:handler:
+ _objc_msgSend$thumbnailsFetchOperationForItem:withVersions:withSize:scale:operationServicer:
+ _objc_msgSend$urlForItem:creatingPlaceholderIfMissing:error:
+ _objc_msgSend$urlForItemID:creatingPlaceholderIfMissing:error:
+ _xfield_identity_encode
+ _xfield_identity_encode.cold.1
- -[FPFetchRegularItemThumbnailsOperation initWithDictionary:desiredSizeToScale:itemManager:]
- GCC_except_table108
- GCC_except_table290
- GCC_except_table297
- GCC_except_table309
- GCC_except_table316
- GCC_except_table318
- GCC_except_table323
- GCC_except_table325
- GCC_except_table331
- GCC_except_table339
- GCC_except_table341
- GCC_except_table345
- GCC_except_table349
- GCC_except_table351
- GCC_except_table354
- GCC_except_table356
- GCC_except_table360
- GCC_except_table366
- GCC_except_table373
- GCC_except_table375
- GCC_except_table382
- GCC_except_table387
- GCC_except_table390
- GCC_except_table409
- GCC_except_table411
- GCC_except_table413
- GCC_except_table425
- GCC_except_table428
- GCC_except_table432
- GCC_except_table77
- GCC_except_table99
- _FPIgnoresForcedKeyChecks
- _FPIgnoresForcedKeyChecks.areForcedKeysIgnored
- _FPIgnoresForcedKeyChecks.cold.1
- _FPIgnoresForcedKeyChecks.onceToken
- _MobileSpotlightIndexLibrary
- _MobileSpotlightIndexLibrary.cold.1
- _MobileSpotlightIndexLibraryCore.frameworkLibrary
- ___129-[NSURL(CopyFile) fp_copyToURL:queue:precomputedItemSize:replacePlaceholder:shouldCopyAppleDouble:ignoreVFSSkipMtime:completion:]_block_invoke.cold.1
- ___37-[FPListRemoteVersionsOperation main]_block_invoke.15
- ___37-[FPListRemoteVersionsOperation main]_block_invoke.8
- ___91-[FPItemManager _fetchURLForItemID:creatingPlaceholderIfMissing:completionHandlerWithInfo:]_block_invoke
- ___FPIgnoresForcedKeyChecks_block_invoke
- ___MobileSpotlightIndexLibraryCore_block_invoke
- ____fpfs_evict_legacy_block_invoke
- ____fpfs_evict_legacy_block_invoke.26
- ___block_descriptor_243_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8s40l8s48l8r72l8s56l8s64l8
- ___block_descriptor_32_e36_i28?0i8^{dirent=QQSSC[1024c]}12r*20l
- ___block_descriptor_40_e8_32s_e40_v32?0"FPItem"8"NSArray"16"NSError"24ls32l8
- ___block_descriptor_48_e34_i16?0^{fpfs_item_handle=QQII*iI}8l
- ___block_descriptor_48_e8_32s40bs_e20_v24?0Q8"NSError"16ls32l8s40l8
- ___block_literal_global.299
- ___block_literal_global.322
- ___block_literal_global.432
- ___block_literal_global.441
- ___block_literal_global.587
- ___block_literal_global.589
- ___block_literal_global.80
- __fpfs_remove_sharing_xattrs
- __fpfs_remove_sharing_xattrs.cold.1
- __fpfs_remove_sharing_xattrs.cold.2
- __fpfs_remove_sharing_xattrs.cold.3
- __fpfs_remove_sharing_xattrs.cold.4
- __fset_dataless_cmpfs_xattr.cold.1
- __fset_dataless_cmpfs_xattr_only.cold.1
- _audit_stringMobileSpotlightIndex
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$initWithDictionary:desiredSizeToScale:itemManager:
- _objc_msgSend$thumbnailsFetchOperationForItem:withVersions:withSize:scale:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ " namespacePolicy:%lu"
+ "%@ (%s)"
+ ",fixPerms"
+ "/.nofollow"
+ "/Library/Caches/com.apple.xbs/82521204-28BD-47EF-84F0-29FFF4B5EEE4/TemporaryDirectory.bLDf03/Sources/FileProvider/extension/FPXDomainContext.m"
+ "/Library/Caches/com.apple.xbs/82521204-28BD-47EF-84F0-29FFF4B5EEE4/TemporaryDirectory.bLDf03/Sources/FileProvider/extension/FPXEnumerator.m"
+ "/Library/Caches/com.apple.xbs/82521204-28BD-47EF-84F0-29FFF4B5EEE4/TemporaryDirectory.bLDf03/Sources/FileProvider/extension/FPXExtensionContext.m"
+ "/Library/Caches/com.apple.xbs/82521204-28BD-47EF-84F0-29FFF4B5EEE4/TemporaryDirectory.bLDf03/Sources/FileProvider/extension/FPXFakeDefaultDomainExtension.m"
+ "/Library/Caches/com.apple.xbs/82521204-28BD-47EF-84F0-29FFF4B5EEE4/TemporaryDirectory.bLDf03/Sources/FileProvider/extension/search-on-server/FPXSearchEnumeratorObserver.m"
+ "/Library/Caches/com.apple.xbs/82521204-28BD-47EF-84F0-29FFF4B5EEE4/TemporaryDirectory.bLDf03/Sources/FileProvider/fileproviderd/action operation engine/FPActionOperationLocator.m"
+ "/Library/Caches/com.apple.xbs/82521204-28BD-47EF-84F0-29FFF4B5EEE4/TemporaryDirectory.bLDf03/Sources/FileProvider/framework/FPDaemonConnection.m"
+ "/Library/Caches/com.apple.xbs/82521204-28BD-47EF-84F0-29FFF4B5EEE4/TemporaryDirectory.bLDf03/Sources/FileProvider/framework/FPItem.m"
+ "/Library/Caches/com.apple.xbs/82521204-28BD-47EF-84F0-29FFF4B5EEE4/TemporaryDirectory.bLDf03/Sources/FileProvider/framework/FPTestingOperations.m"
+ "/Library/Caches/com.apple.xbs/82521204-28BD-47EF-84F0-29FFF4B5EEE4/TemporaryDirectory.bLDf03/Sources/FileProvider/framework/FPXPCSanitizer.m"
+ "/Library/Caches/com.apple.xbs/82521204-28BD-47EF-84F0-29FFF4B5EEE4/TemporaryDirectory.bLDf03/Sources/FileProvider/framework/NSFileProviderManager.m"
+ "/Library/Caches/com.apple.xbs/82521204-28BD-47EF-84F0-29FFF4B5EEE4/TemporaryDirectory.bLDf03/Sources/FileProvider/framework/NSURL+FPAdditions.m"
+ "/Library/Caches/com.apple.xbs/82521204-28BD-47EF-84F0-29FFF4B5EEE4/TemporaryDirectory.bLDf03/Sources/FileProvider/framework/NSXPCConnection+FPAdditions.m"
+ "4018.100.236"
+ "<%@: %p (%@)>"
+ "<%@: %p (%@, requires %@)>"
+ "<%@:%p id:\"%@\" name:\"%@\" urls(%d%s):%@ db:%@%@ state:%s%s%s%s%s%s%s%s features:%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%@>"
+ "@56@0:8@16{CGSize=dd}24@40@48"
+ "@72@0:8@16@24{CGSize=dd}32d48@56@64"
+ "I36@0:8S16i20i24i28B32"
+ "Provider returned invalid namespace policy %ld"
+ "TB,N,V_hasItemsWithPermissionsIssuesToRepair"
+ "Tq,N,V_effectiveNamespacePolicy"
+ "Tq,N,V_inheritedNamespacePolicy"
+ "Tq,N,V_namespacePolicy"
+ "[CRIT] INVALID_CALLER_TO_START_ACCESSING_OPERATION_SERVICER"
+ "[CRIT] Provider returned invalid namespace policy %ld"
+ "[DEBUG] Successfully reported donation progress"
+ "[DEBUG] copyfile: %{public}@ -> %{public}@ AD-copy: %d useThreadedCopier: %d isRegularFile: %d isCompressed: %d flags: %x"
+ "[DEBUG] ┣%llx sending %{public}@ to %@ on behalf of %@[%d] (from %@)"
+ "[DEBUG] ┳%llx ipc: %@, reply of %s (error: %@)"
+ "[ERROR] Failed getting enumerate info: %@"
+ "[ERROR] Failed to report donation progress: %@"
+ "[INFO] Process is %sentitled for enumeration"
+ "__FILEPROVIDER_BAD_NAMESPACE_POLICY__"
+ "_effectiveNamespacePolicy"
+ "_fetchURLForItemID:creatingPlaceholderIfMissing:synchronously:completionHandlerWithInfo:"
+ "_hasItemsWithPermissionsIssuesToRepair"
+ "_inheritedNamespacePolicy"
+ "_namespacePolicy"
+ "_servicer"
+ "com.apple.private.fileprovider.launch-items-permissions-repair"
+ "copyfileFlagsForSourceMode:sourceDevID:targetDevID:rootDevID:replacePlaceholder:"
+ "effectiveNamespacePolicy"
+ "fp_URLWithoutNoFollow"
+ "fp_isPermissionError"
+ "fp_lastErrorOfCompletionHandler"
+ "hasEnumerateEntitlement"
+ "hasItemsWithPermissionsIssuesToRepair"
+ "inheritedNamespacePolicy"
+ "initWithDictionary:desiredSizeToScale:itemManager:operationServicer:"
+ "initWithItem:versions:desiredSize:screenScale:itemManager:operationServicer:"
+ "itemsPermissionsRepair"
+ "launchItemsPermissionsRepairWithCompletionHandler:"
+ "namespacePolicy"
+ "not "
+ "reportDonationProgress:completionHandler:"
+ "sendTelemetryWithCompletionHandler:"
+ "setEffectiveNamespacePolicy:"
+ "setHasItemsWithPermissionsIssuesToRepair:"
+ "setInheritedNamespacePolicy:"
+ "setNamespacePolicy:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SpotlightIndex.framework/SpotlightIndex"
+ "startAccessingOperationServiceForItemAtURL:handler:"
+ "thumbnailsFetchOperationForItem:withVersions:withSize:scale:operationServicer:"
+ "urlForItem:creatingPlaceholderIfMissing:error:"
+ "urlForItem:error:"
+ "urlForItemID:creatingPlaceholderIfMissing:error:"
+ "urlForItemID:error:"
+ "v16@?0@\"FPService<FPXOperationService>\"8"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"<FPXOperationService>\"@\"NSXPCListenerEndpoint\"@\"<FPDLifetimeServicing>\"@\"NSString\"@\"NSError\">24"
+ "void *SpotlightIndexLibrary(void)"
+ "{NSError=#}"
- "/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXDomainContext.m"
- "/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXEnumerator.m"
- "/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXExtensionContext.m"
- "/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXFakeDefaultDomainExtension.m"
- "/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/search-on-server/FPXSearchEnumeratorObserver.m"
- "/Library/Caches/com.apple.xbs/Sources/FileProvider/fileproviderd/action operation engine/FPActionOperationLocator.m"
- "/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPDaemonConnection.m"
- "/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPItem.m"
- "/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPTestingOperations.m"
- "/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPXPCSanitizer.m"
- "/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/NSFileProviderManager.m"
- "/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/NSURL+FPAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/NSXPCConnection+FPAdditions.m"
- "3882.82.1"
- "<%@:%p id:\"%@\" name:\"%@\" urls(%d%s):%@ db:%@%@ state:%s%s%s%s%s%s%s%s features:%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%@%@>"
- "@48@0:8@16{CGSize=dd}24@40"
- "ESTALE: item gen_count changed during _fpfs_evict_legacy [%d, %llu, %u, %u]"
- "IgnoreForcedKeyChecksInInternalOS"
- "[DEBUG] copyfile: %@ -> %@ AD-copy: %d"
- "i28@?0i8^{dirent=QQSSC[1024c]}12r*20"
- "initWithDictionary:desiredSizeToScale:itemManager:"
- "softlink:r:path:/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex"
- "void *MobileSpotlightIndexLibrary(void)"

```
