## DataDeliveryServices

> `/System/Library/PrivateFrameworks/DataDeliveryServices.framework/DataDeliveryServices`

```diff

-96.5.0.0.0
-  __TEXT.__text: 0x27828
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x279c
-  __TEXT.__const: 0x168
-  __TEXT.__gcc_except_tab: 0x6e4
-  __TEXT.__cstring: 0x1413
-  __TEXT.__oslogstring: 0x32b7
-  __TEXT.__unwind_info: 0xb90
-  __TEXT.__objc_classname: 0x520
-  __TEXT.__objc_methname: 0x52e9
-  __TEXT.__objc_methtype: 0x146b
-  __TEXT.__objc_stubs: 0x4720
-  __DATA_CONST.__got: 0x2e8
-  __DATA_CONST.__const: 0xe28
+110.0.0.0.0
+  __TEXT.__text: 0x2992c
+  __TEXT.__objc_methlist: 0x2a3c
+  __TEXT.__const: 0x180
+  __TEXT.__gcc_except_tab: 0x618
+  __TEXT.__cstring: 0x1671
+  __TEXT.__oslogstring: 0x3c81
+  __TEXT.__unwind_info: 0xc68
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xf70
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1410
+  __DATA_CONST.__objc_selrefs: 0x15e0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x2e8
-  __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x16c0
-  __AUTH_CONST.__objc_const: 0x8b18
+  __DATA_CONST.__got: 0x320
+  __AUTH_CONST.__const: 0x360
+  __AUTH_CONST.__cfstring: 0x1920
+  __AUTH_CONST.__objc_const: 0x8de0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x20c
-  __DATA.__data: 0xbd0
-  __DATA.__bss: 0x78
-  __DATA_DIRTY.__objc_data: 0xc30
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0xe8
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x690
+  __DATA.__objc_ivar: 0x228
+  __DATA.__data: 0xbd8
+  __DATA.__bss: 0x88
+  __DATA_DIRTY.__objc_data: 0x780
+  __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
   - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 81D81568-BCAF-36D1-AA15-F9FFD5A1CC83
-  Functions: 954
-  Symbols:   3728
-  CStrings:  1809
+  UUID: 1D1285AF-E937-399A-B4E0-018C7F141E52
+  Functions: 1035
+  Symbols:   3979
+  CStrings:  753
 
Symbols:
+ -[DDSAssertionTracker addAssertionsForQueries:policies:assertionIDs:clientID:]
+ -[DDSAssetCenter addAssertionsForAssetsWithQueries:policies:assertionIDs:clientID:]
+ -[DDSAssetCenter addAssertionsForAssetsWithQueries:policies:assertionIDs:clientID:].cold.1
+ -[DDSAssetCenter initWithQueue:provider:trialManager:autoAssetManager:createXPCInterface:uafManager:]
+ -[DDSAssetCenter uafManager]
+ -[DDSInterface addAssertionsForQueries:policies:assertionIDs:clientID:]
+ -[DDSManager _nonUAFCompatibleAssertions]
+ -[DDSManager _removeLegacyLinguisticDataAssets]
+ -[DDSManager _uafCompatibleAssertions]
+ -[DDSManager addAssertionsForQueries:policies:assertionIDs:clientID:]
+ -[DDSManager checkAndNotifyTriggerUpdateCompletion]
+ -[DDSManager fetchUAFAssetUpdateStatusForQuery:callback:]
+ -[DDSManager updateUAFAssetForAssertion:callback:]
+ -[DDSUAFAssetProvider observeAssetSet:handler:]
+ -[DDSUAFAssetProvider requestSandboxExtension:completion:]
+ -[DDSUAFAssetProvider requestSandboxExtension:completion:].cold.1
+ -[DDSUAFAssetProvider retrieveAssetSet:usages:]
+ -[DDSUAFAssetProvider retrieveAssetSet:usages:].cold.1
+ -[DDSUAFAssetProvider updateAssetsForSubscriber:subscriptionName:policies:completion:]
+ -[DDSUAFManager _createRunningBoardAssertion]
+ -[DDSUAFManager _createRunningBoardAssertion].cold.1
+ -[DDSUAFManager _createRunningBoardAssertion].cold.2
+ -[DDSUAFManager _ensureSandboxAccess]
+ -[DDSUAFManager _hasSandboxAccess]
+ -[DDSUAFManager _hasSandboxAccess].cold.1
+ -[DDSUAFManager _isProcessManagedByRunningBoard]
+ -[DDSUAFManager _isProcessManagedByRunningBoard].cold.1
+ -[DDSUAFManager _mergeAssetMetadata:withUAFMetadata:]
+ -[DDSUAFManager _readInfoPlistAtURL:]
+ -[DDSUAFManager _readInfoPlistAtURL:].cold.1
+ -[DDSUAFManager _readInfoPlistAtURL:].cold.2
+ -[DDSUAFManager _readInfoPlistAtURL:].cold.3
+ -[DDSUAFManager _readInfoPlistAtURL:].cold.4
+ -[DDSUAFManager addAssertionsForAssetsWithQueries:assertionIDs:clientID:]
+ -[DDSUAFManager addAssertionsForAssetsWithQueries:assertionIDs:clientID:].cold.1
+ -[DDSUAFManager addAssertionsForAssetsWithQueries:assertionIDs:clientID:].cold.2
+ -[DDSUAFManager addAssertionsForAssetsWithQueries:assertionIDs:clientID:].cold.3
+ -[DDSUAFManager assetsForQuery:]
+ -[DDSUAFManager assetsForQuery:].cold.1
+ -[DDSUAFManager assetsForQuery:].cold.2
+ -[DDSUAFManager fetchAssetUpdateStatusForQuery:callback:]
+ -[DDSUAFManager hasGrantedSandboxExtension]
+ -[DDSUAFManager observer]
+ -[DDSUAFManager registerAssetObserver:]
+ -[DDSUAFManager sandboxExtensionRequestInProgress]
+ -[DDSUAFManager sandboxQueue]
+ -[DDSUAFManager setHasGrantedSandboxExtension:]
+ -[DDSUAFManager setObserver:]
+ -[DDSUAFManager setSandboxExtensionRequestInProgress:]
+ -[DDSUAFManager setSandboxQueue:]
+ -[DDSUAFManager supportsQuery:]
+ -[DDSUAFManager updateAssetsForAssertionWithIdentifier:clientID:callback:]
+ -[DDSUAFManagerLDDataSource _addRegionalUAFUsagesTo:forAllowedRegions:]
+ -[DDSUAFManagerLDDataSource _regionalUAFUsagesFrom:country:province:city:]
+ -[DDSUAFManagerLDDataSource assetDataURLForUAFAsset:]
+ -[DDSUAFManagerLDDataSource assetMetadataURLForUAFAsset:]
+ -[DDSUAFManagerLDDataSource assetNamesForQuery:]
+ -[DDSUAFManagerStub addAssertionsForAssetsWithQueries:assertionIDs:clientID:]
+ -[DDSUAFManagerStub addAssertionsForAssetsWithQueries:assertionIDs:clientID:].cold.1
+ -[DDSUAFManagerStub assetsForQuery:]
+ -[DDSUAFManagerStub assetsForQuery:].cold.1
+ -[DDSUAFManagerStub registerAssetObserver:]
+ -[DDSUAFManagerStub registerAssetObserver:].cold.1
+ -[DDSUAFManagerStub supportsQuery:]
+ GCC_except_table19
+ GCC_except_table21
+ GCC_except_table22
+ GCC_except_table25
+ GCC_except_table27
+ GCC_except_table42
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table69
+ GCC_except_table70
+ GCC_except_table74
+ GCC_except_table76
+ _DDSUAFForceUpdateCompleteNotification
+ _DDS_USE_UAF_MANAGER
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_RBSAssertion
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_CLASS_$_RBSProcessHandle
+ _OBJC_CLASS_$_RBSTarget
+ _OBJC_IVAR_$_DDSAssetCenter._uafManager
+ _OBJC_IVAR_$_DDSManager._completedCatalogBasedAssetUpdate
+ _OBJC_IVAR_$_DDSManager._completedNonCatalogBasedAssetUpdate
+ _OBJC_IVAR_$_DDSUAFManager._hasGrantedSandboxExtension
+ _OBJC_IVAR_$_DDSUAFManager._observer
+ _OBJC_IVAR_$_DDSUAFManager._sandboxExtensionRequestInProgress
+ _OBJC_IVAR_$_DDSUAFManager._sandboxQueue
+ __OBJC_$_PROP_LIST_DDSMobileAssetv2ProviderDataSource.411
+ __OBJC_$_PROP_LIST_DDSTrialClient.98
+ __OBJC_$_PROP_LIST_DDSTrialManager.87
+ ___27-[DDSManager triggerUpdate]_block_invoke.389
+ ___27-[DDSManager triggerUpdate]_block_invoke.389.cold.1
+ ___27-[DDSManager triggerUpdate]_block_invoke.390
+ ___32-[DDSUAFManager assetsForQuery:]_block_invoke
+ ___32-[DDSUAFManager assetsForQuery:]_block_invoke.365
+ ___32-[DDSUAFManager assetsForQuery:]_block_invoke.cold.1
+ ___34-[DDSUAFManager _hasSandboxAccess]_block_invoke
+ ___37-[DDSUAFManager _ensureSandboxAccess]_block_invoke
+ ___37-[DDSUAFManager _ensureSandboxAccess]_block_invoke.387
+ ___37-[DDSUAFManager _ensureSandboxAccess]_block_invoke_2
+ ___37-[DDSUAFManager _ensureSandboxAccess]_block_invoke_2.cold.1
+ ___38-[DDSManager _uafCompatibleAssertions]_block_invoke
+ ___39-[DDSUAFManager registerAssetObserver:]_block_invoke
+ ___41-[DDSManager _nonUAFCompatibleAssertions]_block_invoke
+ ___43-[DDSManager updateAssetForQuery:callback:]_block_invoke.406
+ ___43-[DDSManager updateAssetForQuery:callback:]_block_invoke.407
+ ___47-[DDSUAFAssetProvider observeAssetSet:handler:]_block_invoke
+ ___48-[DDSAssetCenter serverDidUpdateAssetsWithType:]_block_invoke.384
+ ___48-[DDSServer listener:shouldAcceptNewConnection:]_block_invoke.382
+ ___48-[DDSServer listener:shouldAcceptNewConnection:]_block_invoke.382.cold.1
+ ___48-[DDSUAFManager _isProcessManagedByRunningBoard]_block_invoke
+ ___50-[DDSManager updateUAFAssetForAssertion:callback:]_block_invoke
+ ___50-[DDSManager updateUAFAssetForAssertion:callback:]_block_invoke.cold.1
+ ___51-[DDSManager didEndUpdateCycleWithAssetType:error:]_block_invoke.393
+ ___54-[DDSManager fetchAssetUpdateStatusForQuery:callback:]_block_invoke.402
+ ___54-[DDSManager fetchAssetUpdateStatusForQuery:callback:]_block_invoke.403
+ ___54-[DDSManager fetchAssetUpdateStatusForQuery:callback:]_block_invoke.404
+ ___57-[DDSManager fetchUAFAssetUpdateStatusForQuery:callback:]_block_invoke
+ ___58-[DDSUAFAssetProvider requestSandboxExtension:completion:]_block_invoke
+ ___58-[DDSUAFAssetProvider requestSandboxExtension:completion:]_block_invoke.cold.1
+ ___59-[DDSManager updateCatalogBasedAssetForAssertion:callback:]_block_invoke.405
+ ___59-[DDSManager updateCatalogBasedAssetForAssertion:callback:]_block_invoke.405.cold.1
+ ___59-[DDSManager updateCatalogBasedAssetForAssertion:callback:]_block_invoke.405.cold.2
+ ___71-[DDSInterface addAssertionsForQueries:policies:assertionIDs:clientID:]_block_invoke
+ ___72-[DDSManager beginUpdateCycleForAssetType:forced:discretionaryDownload:]_block_invoke.368
+ ___73-[DDSUAFManager addAssertionsForAssetsWithQueries:assertionIDs:clientID:]_block_invoke
+ ___73-[DDSUAFManager addAssertionsForAssetsWithQueries:assertionIDs:clientID:]_block_invoke.cold.1
+ ___74-[DDSUAFManager updateAssetsForAssertionWithIdentifier:clientID:callback:]_block_invoke
+ ___78-[DDSAssertionTracker addAssertionsForQueries:policies:assertionIDs:clientID:]_block_invoke
+ ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.381
+ ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.381.cold.1
+ ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.381.cold.2
+ ___86-[DDSUAFAssetProvider updateAssetsForSubscriber:subscriptionName:policies:completion:]_block_invoke
+ ___86-[DDSUAFAssetProvider updateAssetsForSubscriber:subscriptionName:policies:completion:]_block_invoke.357
+ ___block_descriptor_40_e8_32bs_e20_v24?0q8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32s_e39_B24?0"DDSAssertion"8"NSDictionary"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSNumber"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e30_v24?0"NSNumber"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e27_v16?0"UAFAssetSetStatus"8ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40bs48r56r64r_e17_v16?0"NSError"8ls32l8r48l8r56l8r64l8s40l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_literal_global.21
+ ___block_literal_global.357
+ ___block_literal_global.373
+ ___block_literal_global.382
+ __hasSandboxAccess.hasSandboxAccess
+ __hasSandboxAccess.onceToken
+ __isProcessManagedByRunningBoard.isProcessManaged
+ __isProcessManagedByRunningBoard.onceToken
+ _dispatch_get_global_queue
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _getpid
+ _kUAFPolicyUseCellular
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_addRegionalUAFUsagesTo:forAllowedRegions:
+ _objc_msgSend$_createRunningBoardAssertion
+ _objc_msgSend$_ensureSandboxAccess
+ _objc_msgSend$_hasSandboxAccess
+ _objc_msgSend$_isProcessManagedByRunningBoard
+ _objc_msgSend$_mergeAssetMetadata:withUAFMetadata:
+ _objc_msgSend$_nonUAFCompatibleAssertions
+ _objc_msgSend$_readInfoPlistAtURL:
+ _objc_msgSend$_regionalUAFUsagesFrom:country:province:city:
+ _objc_msgSend$_removeLegacyLinguisticDataAssets
+ _objc_msgSend$_uafCompatibleAssertions
+ _objc_msgSend$acquireWithError:
+ _objc_msgSend$addAssertionsForAssetsWithQueries:assertionIDs:clientID:
+ _objc_msgSend$addAssertionsForAssetsWithQueries:policies:assertionIDs:clientID:
+ _objc_msgSend$addAssertionsForQueries:policies:assertionIDs:clientID:
+ _objc_msgSend$assetDataURLForUAFAsset:
+ _objc_msgSend$assetMetadataURLForUAFAsset:
+ _objc_msgSend$assetNamed:
+ _objc_msgSend$assetNamesForQuery:
+ _objc_msgSend$assets
+ _objc_msgSend$attributeWithDomain:name:
+ _objc_msgSend$checkAndNotifyTriggerUpdateCompletion
+ _objc_msgSend$completedPercent
+ _objc_msgSend$containsString:
+ _objc_msgSend$currentProcess
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$downloadStatus
+ _objc_msgSend$fetchUAFAssetUpdateStatusForQuery:callback:
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$hasGrantedSandboxExtension
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$initWithExplanation:target:attributes:
+ _objc_msgSend$initWithQueue:provider:trialManager:autoAssetManager:createXPCInterface:uafManager:
+ _objc_msgSend$invalidateWithQueue:completion:
+ _objc_msgSend$isManaged
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$location
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$metadata
+ _objc_msgSend$observeAssetSet:handler:
+ _objc_msgSend$observeAssetSet:queue:handler:
+ _objc_msgSend$observer
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$registerAssetObserver:
+ _objc_msgSend$removeAssetsForAssertions:
+ _objc_msgSend$requestSandboxExtension:completion:
+ _objc_msgSend$requestSandboxExtension:queue:completion:
+ _objc_msgSend$retrieveAssetSet:usages:
+ _objc_msgSend$sandboxExtensionRequestInProgress
+ _objc_msgSend$sandboxQueue
+ _objc_msgSend$setHasGrantedSandboxExtension:
+ _objc_msgSend$setObserver:
+ _objc_msgSend$setSandboxExtensionRequestInProgress:
+ _objc_msgSend$targetWithPid:
+ _objc_msgSend$totalBytes
+ _objc_msgSend$updateAssetsForAssertionWithIdentifier:clientID:callback:
+ _objc_msgSend$updateAssetsForSubscriber:subscriptionName:policies:completion:
+ _objc_msgSend$updateAssetsForSubscriber:subscriptionName:policies:queue:detailedProgress:completion:
+ _objc_msgSend$updateUAFAssetForAssertion:callback:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
+ _objc_retain_x9
+ _objc_sync_enter
+ _objc_sync_exit
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _sandbox_check
- -[DDSAssetCenter addAssertionForAssetsWithQuery:policy:assertionID:clientID:].cold.1
- -[DDSAssetCenter initWithQueue:provider:trialManager:autoAssetManager:createXPCInterface:]
- -[DDSManager triggerDumpWithReply:].cold.2
- -[DDSUAFManager addAssertionForAssetsWithQuery:assertionID:clientID:]
- -[DDSUAFManager addAssertionForAssetsWithQuery:assertionID:clientID:].cold.1
- -[DDSUAFManager addAssertionForAssetsWithQuery:assertionID:clientID:].cold.2
- -[DDSUAFManagerStub addAssertionForAssetsWithQuery:assertionID:clientID:]
- -[DDSUAFManagerStub addAssertionForAssetsWithQuery:assertionID:clientID:].cold.1
- GCC_except_table20
- GCC_except_table26
- GCC_except_table32
- GCC_except_table4
- GCC_except_table51
- GCC_except_table52
- GCC_except_table57
- GCC_except_table58
- GCC_except_table60
- GCC_except_table61
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- __OBJC_$_PROP_LIST_DDSMobileAssetv2ProviderDataSource.390
- __OBJC_$_PROP_LIST_DDSTrialClient.99
- __OBJC_$_PROP_LIST_DDSTrialManager.88
- ___43-[DDSManager updateAssetForQuery:callback:]_block_invoke.365
- ___48-[DDSAssetCenter serverDidUpdateAssetsWithType:]_block_invoke.358
- ___48-[DDSServer listener:shouldAcceptNewConnection:]_block_invoke.361
- ___48-[DDSServer listener:shouldAcceptNewConnection:]_block_invoke.361.cold.1
- ___51-[DDSManager didEndUpdateCycleWithAssetType:error:]_block_invoke.352
- ___54-[DDSManager fetchAssetUpdateStatusForQuery:callback:]_block_invoke.361
- ___54-[DDSManager fetchAssetUpdateStatusForQuery:callback:]_block_invoke.363
- ___59-[DDSManager updateCatalogBasedAssetForAssertion:callback:]_block_invoke.364
- ___59-[DDSManager updateCatalogBasedAssetForAssertion:callback:]_block_invoke.364.cold.1
- ___59-[DDSManager updateCatalogBasedAssetForAssertion:callback:]_block_invoke.364.cold.2
- ___69-[DDSUAFManager addAssertionForAssetsWithQuery:assertionID:clientID:]_block_invoke
- ___69-[DDSUAFManager addAssertionForAssetsWithQuery:assertionID:clientID:]_block_invoke.cold.1
- ___72-[DDSAssertionTracker addAssertionForQuery:policy:assertionID:clientID:]_block_invoke
- ___72-[DDSManager beginUpdateCycleForAssetType:forced:discretionaryDownload:]_block_invoke.341
- ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.360
- ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.360.cold.1
- ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.360.cold.2
- ___block_descriptor_64_e8_32s40s48s56s_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_96_e8_32s40s48s56s64s72r80r88r_e5_v8?0ls32l8s40l8s48l8s56l8r72l8s64l8r80l8r88l8
- ___block_literal_global.15
- ___block_literal_global.20
- ___block_literal_global.336
- ___block_literal_global.349
- _assetUUIDWithLocalURL
- _objc_msgSend$addAssertionForAssetsWithQuery:assertionID:clientID:
- _objc_msgSend$initWithQueue:provider:trialManager:autoAssetManager:createXPCInterface:
CStrings:
+ "\n\n\n"
+ "#### Non UAF Compatible Assertion Details ####\n"
+ "#### UAF Compatible Assertion Details ####\n"
+ "##########################################\n"
+ "##############################################\n"
+ "%@: %@\n"
+ "-[DDSUAFManager addAssertionsForAssetsWithQueries:assertionIDs:clientID:]"
+ "/private/var/MobileAsset/AssetsV2/"
+ "Add batch assertions: %lu queries for clientID: (%{public}@)"
+ "Asset update failure"
+ "Asset update request for subscriber: %@ subscriptionName: %@ failed with status: %lu"
+ "Asset update requested for clientID: %{public}@, assertionID: %{public}@"
+ "Asset update status fetched successfully for query: %{public}@, status: %ld"
+ "AssetSetName: %@ have been updated"
+ "Assets updated successfully for subscriber: %@ subscriptionName: %@"
+ "B24@?0@\"DDSAssertion\"8@\"NSDictionary\"16"
+ "Batch assertion arrays must be equal length: queries=%lu assertionIDs=%lu"
+ "Batch assertion arrays must be equal length: queries=%lu policies=%lu assertionIDs=%lu"
+ "Cannot add batch assertions, manager interface is nil for asset type: %@"
+ "DDSUAFForceUpdateCompleteNotification"
+ "DDSUAFManagerStub: addAssertionsForAssetsWithQueries called (no-op)"
+ "DDSUAFManagerStub: assetsForQuery called (no-op)"
+ "DDSUAFManagerStub: registerAssetObserver called (no-op)"
+ "DataDeliveryServicesUAFAssetSet"
+ "Failed to grant sandbox extension: %{public}@"
+ "Failed to parse Info.plist from URL: %{public}@, error: %{public}@"
+ "Failed to read Info.plist data from URL: %{public}@, error: %{public}@"
+ "Fetch asset update status for: %{public}@"
+ "Fetch asset update status request failed for query: %{public}@"
+ "FinishTaskUninterruptable"
+ "Info.plist file does not exist at path: %{public}@"
+ "Info.plist root object is not a dictionary at URL: %{public}@"
+ "MobileAssetProperties is missing in asset metadata hence skip enumerating asset for : %@"
+ "No UAF supported locale found for query: %@"
+ "No asset found for UAF Usages: %@"
+ "No asset found for UAF Usages: %@, Asset Name: %@"
+ "No supported asset name found for query: %@"
+ "Observe update notification for assetSetName: %@"
+ "RBSAssertion: Failed to acquire assertion: %{public}@"
+ "RBSAssertion: Failed to create RBSAssertion"
+ "RBSAssertion: Invalidating assertion"
+ "RBSAssertion: Successfully acquired assertion"
+ "Removing legacy LinguisticData assets due to UAF migration"
+ "Removing legacy LinguisticDataAuto assets due to UAF migration"
+ "Request sandbox extension for UAF asset set: %@"
+ "Retrieving assets for asset set name: %@ and usages: %@"
+ "Sandbox access is already granted using entitlements"
+ "Sandbox extension request for asset set: %{public}@ completed successfully"
+ "Sandbox extension request for asset set: %{public}@ failed with error: %{public}@"
+ "Subscribe request failed with error: %{public}@ for %lu queries"
+ "Successfully granted sandbox extension"
+ "Successfully subscribed client %{public}@ with %lu subscriptions from %lu queries:\n%{public}@"
+ "Triggered UAF assets update via ddsutil completed successfully for query: %@"
+ "Triggered UAF assets update via ddsutil for query: %@ failed with error: %@"
+ "Triggered auto assets update via ddsutil completed successfully for query: %@"
+ "Triggered auto assets update via ddsutil for query: %@ failed with error: %@"
+ "UAF"
+ "UAF Asset Download Status for subscriber: %@ subscriptionName: %@ TotalBytes: %lu, CompletedPercentage: %f, Status: %lu"
+ "UAFAssetDelivery"
+ "UAFAssetSet invalidation error: %{public}@"
+ "Update assets for subscriber: %@ subscriptionName: %@ with policies: %@"
+ "any"
+ "assetsForQuery: %{public}@ final result: %{public}@"
+ "com.apple.common"
+ "com.apple.datadeliveryservices.uafmanager.sandbox"
+ "delta"
+ "file-read-data"
+ "ld.city"
+ "ld.country"
+ "ld.province"
+ "optional"
+ "precompiled"
+ "regional"
+ "v16@?0@\"UAFAssetSetStatus\"8"
- "#16@0:8"
- "%@: %@"
- "-[DDSUAFManager addAssertionForAssetsWithQuery:assertionID:clientID:]"
- ".cxx_destruct"
- "@\"<DDSAssertionDataHandling>\""
- "@\"<DDSAssetObserving>\""
- "@\"<DDSAssetObservingDelegate>\""
- "@\"<DDSAssetObservingDelegate>\"16@0:8"
- "@\"<DDSAssetProviding>\""
- "@\"<DDSAssetProvidingDelegate>\""
- "@\"<DDSAssetProvidingDelegate>\"16@0:8"
- "@\"<DDSAssetTracking>\""
- "@\"<DDSAssetTrackingDelegate>\""
- "@\"<DDSAssetTrackingDelegate>\"16@0:8"
- "@\"<DDSBackgroundActivitySchedulerDelegate>\""
- "@\"<DDSCache>\""
- "@\"<DDSMAAutoAssetManagerDataSource>\""
- "@\"<DDSMAAutoAssetProvider>\""
- "@\"<DDSManagerDataSource>\""
- "@\"<DDSManaging>\""
- "@\"<DDSManagingDelegate>\""
- "@\"<DDSManagingDelegate>\"16@0:8"
- "@\"<DDSMobileAssetv2ProviderDataSource>\""
- "@\"<DDSRemoteSyncStateDelegate>\""
- "@\"<DDSTRIClient>\""
- "@\"<DDSTrialClient>\"32@0:8@\"NSObject<OS_dispatch_queue>\"16@\"DDSTrialQuery\"24"
- "@\"<DDSTrialClientDelegate>\""
- "@\"<DDSTrialClientDelegate>\"16@0:8"
- "@\"<DDSTrialManager>\""
- "@\"<DDSTrialManagerDataSource>\""
- "@\"<DDSTrialManagerDelegate>\""
- "@\"<DDSTrialManagerDelegate>\"16@0:8"
- "@\"<DDSUAFAssetProvider>\""
- "@\"<DDSUAFManager>\""
- "@\"<DDSUAFManagerDataSource>\""
- "@\"<TRINotificationToken>\""
- "@\"<TRINotificationToken>\"40@0:8@\"NSString\"16@\"NSObject<OS_dispatch_queue>\"24@?<v@?@\"<TRINamespaceUpdateProtocol>\">32"
- "@\"DDSAssertion\"24@0:8@\"DDSAssetQuery\"16"
- "@\"DDSAsset\""
- "@\"DDSAsset\"40@0:8@\"MAAutoAsset\"16@\"NSString\"24^@32"
- "@\"DDSAssetPolicy\""
- "@\"DDSAssetQuery\""
- "@\"DDSAssetQueryResultCache\""
- "@\"DDSAttributeFilter\""
- "@\"DDSBackgroundActivityScheduler\""
- "@\"DDSInterface\""
- "@\"DDSMAAutoAssetManager\""
- "@\"DDSTrialExperimentIdentifiers\""
- "@\"MAAsset\""
- "@\"MAAssetQuery\"44@0:8@\"DDSAssetQuery\"16q24@\"NSString\"32B40"
- "@\"MAAutoAsset\"24@0:8@\"DDSMAAutoAssetSelector\"16"
- "@\"MAAutoAssetSelector\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"24@0:8@\"DDSAssetQuery\"16"
- "@\"NSArray\"24@0:8@\"NSDate\"16"
- "@\"NSArray\"24@0:8@\"NSString\"16"
- "@\"NSArray\"32@0:8@\"DDSAssetQuery\"16^@24"
- "@\"NSArray\"32@0:8@\"NSArray\"16@\"DDSAttributeFilter\"24"
- "@\"NSDate\""
- "@\"NSDate\"16@0:8"
- "@\"NSDate\"24@0:8@\"NSString\"16"
- "@\"NSDateComponents\""
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSSet\"16@0:8"
- "@\"NSSet\"24@0:8@\"DDSAssertion\"16"
- "@\"NSSet\"24@0:8@\"NSString\"16"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@\"TRIClient\""
- "@\"TRIExperimentIdentifiers\"24@0:8@\"NSString\"16"
- "@\"TRILevel\"32@0:8@\"NSString\"16@\"NSString\"24"
- "@\"UAFAssetSetManager\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8i16I20"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@36@0:8@16@24i32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16@24^@32"
- "@44@0:8@16q24@32B40"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24B32B36B40B44"
- "@56@0:8@16@24@32@40@?48"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"DDSAssetQuery\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "B36@0:8@16@24B32"
- "B40@0:8@16@24@?32"
- "B40@0:8@16@24B32B36"
- "Cannot add assertion, manager interface is nil for asset type: %@"
- "DDSAnalytics"
- "DDSAssertDescriptor"
- "DDSAssertion"
- "DDSAssertionDataHandler"
- "DDSAssertionDataHandling"
- "DDSAssertionTracker"
- "DDSAsset"
- "DDSAssetCenter"
- "DDSAssetDownloadAnalytic"
- "DDSAssetObserver"
- "DDSAssetObserving"
- "DDSAssetObservingDelegate"
- "DDSAssetPolicy"
- "DDSAssetProviding"
- "DDSAssetProvidingDelegate"
- "DDSAssetQuery"
- "DDSAssetQueryResultCache"
- "DDSAssetTracking"
- "DDSAssetTrackingDelegate"
- "DDSAttributeFilter"
- "DDSBackgroundActivityScheduler"
- "DDSBackgroundActivitySchedulerDelegate"
- "DDSCache"
- "DDSContentItem"
- "DDSContentItemMatcher"
- "DDSInterface"
- "DDSLinguisticAssetQuery"
- "DDSLinguisticAttributeFilter"
- "DDSMAAsset"
- "DDSMAAutoAssetManager"
- "DDSMAAutoAssetManagerDataSource"
- "DDSMAAutoAssetProvider"
- "DDSMAAutoAssetSelector"
- "DDSManager"
- "DDSManagerDataSource"
- "DDSManaging"
- "DDSManagingDelegate"
- "DDSMobileAssetv2Provider"
- "DDSMobileAssetv2ProviderDataSource"
- "DDSMobileAssetv2QueryAdapter"
- "DDSRemoteSyncState"
- "DDSRemoteSyncStateDelegate"
- "DDSServer"
- "DDSServerConfiguration"
- "DDSTRIClient"
- "DDSTimedAnalytic"
- "DDSTrialAsset"
- "DDSTrialClient"
- "DDSTrialClientDelegate"
- "DDSTrialExperimentIdentifiers"
- "DDSTrialManager"
- "DDSTrialManagerDataSource"
- "DDSTrialManagerDelegate"
- "DDSTrialQuery"
- "DDSUAFAssetProvider"
- "DDSUAFManager"
- "DDSUAFManagerDataSource"
- "DDSUAFManagerLDDataSource"
- "DDSUAFManagerStub"
- "DDSUAFManagerStub: addAssertionForAssetsWithQuery called (no-op)"
- "Error occurred!!!"
- "Failed to update auto asset for query: %{public}@"
- "I"
- "I16@0:8"
- "Locale not found in query"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "Subscribe request failed with error: %{public}@ for query: %{public}@"
- "Successfully subscribed client %{public}@ with assertion %{public}@ for subscriptions: \n%{public}@"
- "T#,R"
- "T@\"<DDSAssertionDataHandling>\",R,N,V_dataHandler"
- "T@\"<DDSAssetObserving>\",R,N,V_assetObserver"
- "T@\"<DDSAssetObservingDelegate>\",W"
- "T@\"<DDSAssetObservingDelegate>\",W,V_delegate"
- "T@\"<DDSAssetProviding>\",R,N,V_provider"
- "T@\"<DDSAssetProviding>\",R,V_provider"
- "T@\"<DDSAssetProvidingDelegate>\",&,N"
- "T@\"<DDSAssetProvidingDelegate>\",&,N,Vdelegate"
- "T@\"<DDSAssetTracking>\",R,N,V_tracker"
- "T@\"<DDSAssetTrackingDelegate>\",&,N"
- "T@\"<DDSAssetTrackingDelegate>\",&,N,V_delegate"
- "T@\"<DDSBackgroundActivitySchedulerDelegate>\",&,N,V_delegate"
- "T@\"<DDSCache>\",R,N,V_cache"
- "T@\"<DDSMAAutoAssetManagerDataSource>\",R,N,V_dataSource"
- "T@\"<DDSMAAutoAssetProvider>\",R,N,V_provider"
- "T@\"<DDSManagerDataSource>\",R,N,V_dataSource"
- "T@\"<DDSManaging>\",&,N,V_serverOverride"
- "T@\"<DDSManaging>\",R,N,V_manager"
- "T@\"<DDSManagingDelegate>\",W"
- "T@\"<DDSManagingDelegate>\",W,V_delegate"
- "T@\"<DDSMobileAssetv2ProviderDataSource>\",R,N,V_dataSource"
- "T@\"<DDSRemoteSyncStateDelegate>\",W,N,V_delegate"
- "T@\"<DDSTRIClient>\",R,V_triClient"
- "T@\"<DDSTrialClientDelegate>\",W"
- "T@\"<DDSTrialClientDelegate>\",W,V_delegate"
- "T@\"<DDSTrialManager>\",R,N,V_trialManager"
- "T@\"<DDSTrialManagerDataSource>\",R,V_dataSource"
- "T@\"<DDSTrialManagerDelegate>\",W"
- "T@\"<DDSTrialManagerDelegate>\",W,V_delegate"
- "T@\"<DDSUAFAssetProvider>\",&,N,V_assetProvider"
- "T@\"<DDSUAFManager>\",R,N,V_uafManager"
- "T@\"<DDSUAFManagerDataSource>\",R,N,V_dataSource"
- "T@\"<TRINotificationToken>\",&,V_notificationToken"
- "T@\"DDSAsset\",&,N,V_asset"
- "T@\"DDSAsset\",&,N,V_parentAsset"
- "T@\"DDSAssetPolicy\",&,N,V_policy"
- "T@\"DDSAssetPolicy\",R,N"
- "T@\"DDSAssetQuery\",R,N,V_query"
- "T@\"DDSAssetQueryResultCache\",R,N,V_assetQueryResultsCache"
- "T@\"DDSAttributeFilter\",R,N,V_filter"
- "T@\"DDSBackgroundActivityScheduler\",&,N,V_scheduler"
- "T@\"DDSInterface\",R,N,V_sharedInstance"
- "T@\"DDSLinguisticAttributeFilter\",R,D,N"
- "T@\"DDSMAAutoAssetManager\",R,N,V_autoAssetManager"
- "T@\"DDSTrialExperimentIdentifiers\",R,C,V_experimentIdentifiers"
- "T@\"MAAsset\",R,N,V_maAsset"
- "T@\"MAAutoAssetSelector\",R,N,V_assetSelector"
- "T@\"NSDate\",&,N,V_date"
- "T@\"NSDate\",&,N,V_lastUpdated"
- "T@\"NSDate\",R,C"
- "T@\"NSDateComponents\",&,N,V_idleUsageEvictionPeriod"
- "T@\"NSDictionary\",&,N,V_contents"
- "T@\"NSDictionary\",R,N"
- "T@\"NSDictionary\",R,N,V_attributes"
- "T@\"NSMutableArray\",R,N,V_trackedAssertions"
- "T@\"NSMutableDictionary\",&,N,V_filters"
- "T@\"NSMutableDictionary\",&,N,V_schedulerByIdentifier"
- "T@\"NSMutableDictionary\",R,N,V_analyticByIdentifier"
- "T@\"NSMutableDictionary\",R,N,V_assertionUpdateStatus"
- "T@\"NSMutableDictionary\",R,N,V_cache"
- "T@\"NSMutableDictionary\",R,N,V_compatibilityVersionByAssetType"
- "T@\"NSMutableDictionary\",R,N,V_downloadStateByAssetID"
- "T@\"NSMutableDictionary\",R,N,V_pendingAssertionsToUpdateByAssetType"
- "T@\"NSMutableDictionary\",R,N,V_remoteSyncStateByAssetType"
- "T@\"NSMutableDictionary\",R,N,V_trackedAssertionSets"
- "T@\"NSMutableDictionary\",R,V_managerInterfaceByAssetType"
- "T@\"NSMutableDictionary\",R,V_trialClientByQuery"
- "T@\"NSMutableSet\",&,N,V_descriptors"
- "T@\"NSMutableSet\",R,N,V_clientConnections"
- "T@\"NSMutableSet\",R,N,V_typesToObserve"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_analyticQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_connectionUsageQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_workQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,V_workQueue"
- "T@\"NSSet\",C,N,V_notificationDownloadTriggers"
- "T@\"NSSet\",R"
- "T@\"NSSet\",R,C"
- "T@\"NSSet\",R,N"
- "T@\"NSSet\",R,N,V_autoAssetTypes"
- "T@\"NSString\",&,N,V_assertionIdentifier"
- "T@\"NSString\",&,N,V_buildVersion"
- "T@\"NSString\",&,N,V_clientIdentifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_downloadCompletionNotification"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,V_triNamespaceName"
- "T@\"NSString\",R,C,V_xpcServiceName"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_assetType"
- "T@\"NSString\",R,N,V_assetUUID"
- "T@\"NSString\",R,N,V_dataType"
- "T@\"NSString\",R,N,V_debuggingID"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_installDate"
- "T@\"NSString\",R,N,V_locale"
- "T@\"NSString\",R,N,V_shortName"
- "T@\"NSString\",R,N,V_uniqueIdentifier"
- "T@\"NSURL\",R,C,V_assertionStorageDirectoryURL"
- "T@\"NSURL\",R,C,V_assertionStorageFileURL"
- "T@\"NSURL\",R,N"
- "T@\"NSURL\",R,N,V_localURL"
- "T@\"NSXPCConnection\",&,N,V_remoteServer"
- "T@\"NSXPCListener\",R,N,V_listener"
- "T@\"TRIClient\",R,V_client"
- "T@\"UAFAssetSetManager\",R,N,V_assetSetManager"
- "T@?,R,C,V_createXPCInterface"
- "TB,N,V_downloadOverCellular"
- "TB,N,V_downloadWithoutPower"
- "TB,N,V_success"
- "TB,R"
- "TB,V_cachedOnly"
- "TB,V_installedOnly"
- "TB,V_latestOnly"
- "TB,V_localOnly"
- "TI,R,V_namespaceId"
- "TQ,N,V_attemptCount"
- "TQ,N,V_retries"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_assetState"
- "TQ,R,N,V_compatibilityVersion"
- "TQ,R,N,V_contentVersion"
- "Td,N,V_endTime"
- "Td,N,V_startTime"
- "Ti,N,V_lastAction"
- "Ti,R,V_projectId"
- "Tq,N,V_preferredDownloadFrequency"
- "Tq,N,V_syncStatus"
- "Tq,R"
- "URLByAppendingPathComponent:"
- "URLForResource:withExtension:"
- "Unexpected error dumping assets: %{public}@"
- "Utils"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_analyticByIdentifier"
- "_analyticQueue"
- "_anyDictionaryIn:matches:shouldLenientlyMatch:"
- "_anyStringIn:matches:acceptUnspecifiedValue:"
- "_assertionIdentifier"
- "_assertionStorageDirectoryURL"
- "_assertionStorageFileURL"
- "_assertionUpdateStatus"
- "_asset"
- "_assetObserver"
- "_assetProvider"
- "_assetQueryResultsCache"
- "_assetSelector"
- "_assetSetManager"
- "_assetState"
- "_assetType"
- "_assetUUID"
- "_attemptCount"
- "_attributes"
- "_autoAssetManager"
- "_autoAssetTypes"
- "_buildVersion"
- "_cache"
- "_cachedOnly"
- "_client"
- "_clientConnections"
- "_clientIdentifier"
- "_compatibilityVersion"
- "_compatibilityVersionByAssetType"
- "_connectionUsageQueue"
- "_contentVersion"
- "_contents"
- "_createAssetSetUsagesFromQuery:"
- "_createXPCInterface"
- "_dataHandler"
- "_dataSource"
- "_dataType"
- "_date"
- "_debuggingID"
- "_delegate"
- "_delegates"
- "_description"
- "_descriptors"
- "_deviceType"
- "_dictionary:matches:acceptUnspecifiedAttribute:lenientMatch:"
- "_downloadCompletionNotification"
- "_downloadOverCellular"
- "_downloadStateByAssetID"
- "_downloadWithoutPower"
- "_endTime"
- "_experimentIdentifiers"
- "_filter"
- "_filters"
- "_identifier"
- "_idleUsageEvictionPeriod"
- "_installDate"
- "_installedOnly"
- "_lastAction"
- "_lastUpdated"
- "_latestOnly"
- "_listener"
- "_localOnly"
- "_localURL"
- "_locale"
- "_lock"
- "_maAsset"
- "_manager"
- "_managerInterfaceByAssetType"
- "_namespaceId"
- "_notificationDownloadTriggers"
- "_notificationToken"
- "_parentAsset"
- "_pendingAssertionsToUpdateByAssetType"
- "_policy"
- "_preferredDownloadFrequency"
- "_projectId"
- "_provider"
- "_query"
- "_queue"
- "_remoteServer"
- "_remoteSyncStateByAssetType"
- "_retries"
- "_scheduler"
- "_schedulerByIdentifier"
- "_serverOverride"
- "_setAdditionalXPCActivityProperties:"
- "_setForKey:"
- "_setQueue:"
- "_sharedInstance"
- "_shortName"
- "_startTime"
- "_string:matches:acceptUnspecifiedValue:"
- "_success"
- "_syncStatus"
- "_teardownXPCConnection"
- "_trackedAssertionSets"
- "_trackedAssertions"
- "_tracker"
- "_triClient"
- "_triNamespaceName"
- "_trialClientByQuery"
- "_trialManager"
- "_typesToObserve"
- "_uafManager"
- "_uniqueIdentifier"
- "_workQueue"
- "_xpcServiceName"
- "addAllowedValue:forKey:"
- "addAllowedValues:forKey:"
- "addAssertionForAssetsWithQuery:assertionID:clientID:"
- "addAssertionForAssetsWithQuery:policy:assertionID:clientID:"
- "addAssertionForQuery:policy:assertionID:clientID:"
- "addAssetLocale:"
- "addContentItemLocale:"
- "addContentType:"
- "addDescriptorWithAssertionID:clientID:policy:"
- "addEntriesFromDictionary:"
- "addEntriesFromFilter:"
- "addKeyValueArray:with:"
- "addKeyValueNull:"
- "addKeyValuePair:with:"
- "addLinguisticAssetType:"
- "addObject:"
- "addObjectsFromArray:"
- "addRegionWithCountry:province:city:"
- "addUpdateHandlerForNamespaceName:queue:usingBlock:"
- "allAssertions"
- "allContentItemsMatchingQuery:error:"
- "allKeys"
- "allObjects"
- "allSupportedLinguisticAssetTypeForAssetType:"
- "allValues"
- "allocWithZone:"
- "allowedValuesForKey:"
- "analyticByIdentifier"
- "analyticQueue"
- "anyObject"
- "appendFormat:"
- "appendString:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayWithObjects:count:"
- "assertionDueForUpdateFrom:SinceDate:"
- "assertionDueForUpdateSinceDate:"
- "assertionForQuery:"
- "assertionIDsForClientID:"
- "assertionIDsForClientID:assetType:"
- "assertionIDsForClientID:reply:"
- "assertionIdentifier"
- "assertionIdentifiers"
- "assertionStorageDirectoryURL"
- "assertionStorageFileURL"
- "assertionUpdateStatus"
- "asset"
- "assetContentItemsMatching:contentItems:parentAsset:"
- "assetDownloadDurationBuckets"
- "assetObserver"
- "assetPolicy"
- "assetProvider"
- "assetQueryResultsCache"
- "assetSelector"
- "assetSetManager"
- "assetSetName"
- "assetSets"
- "assetSpecifier"
- "assetState"
- "assetType"
- "assetUUID"
- "assetUpdateStatusForAssertion:"
- "assetsAvailableOnDeviceForQuery:"
- "assetsForQuery:"
- "assetsForQuery:error:"
- "assetsForQuery:errorPtr:"
- "assetsInCatalogForQuery:errorPtr:"
- "attachProgressCallBack:"
- "attemptCount"
- "attributeFilter"
- "attributeFilterWithDictionary:"
- "attributes"
- "attributesWithLocalURL:"
- "autoAssetForAssetSelector:"
- "autoAssetManager"
- "autoAssetQueryForAssertion:"
- "autoAssetSelectorsForQuery:"
- "autoAssetTypeForAsserType:"
- "autoAssetTypes"
- "autoAssetsForQuery:"
- "autorelease"
- "availableForUseAttributes"
- "beganUpdateCycle"
- "beginDownloadForAssertion:discretionaryDownload:handler:"
- "beginDownloadForAssertions:discretionaryDownload:"
- "beginDownloadForAssets:withPolicy:discretionaryDownload:error:handler:"
- "beginObservingType:"
- "beginUpdateCycleForAssetType:forced:discretionaryDownload:"
- "boolValue"
- "bucketForValue:fromBuckets:"
- "buildVersion"
- "buildVersionString"
- "bundleWithURL:"
- "cStringUsingEncoding:"
- "cache"
- "cacheAssets:forQuery:"
- "cacheKey"
- "cacheObject:forKey:"
- "cachedAssetsForQuery:"
- "cachedOnly"
- "calendarWithIdentifier:"
- "cancelActivityWithIdentifier:"
- "cancelRecordingForAsset:"
- "caseInsensitiveCompare:"
- "catalogUpdateDateForAssetType:"
- "class"
- "clearCache"
- "clearCacheForAssetType:"
- "client"
- "clientConnections"
- "clientIdentifier"
- "clientIdentifiers"
- "clientWithIdentifier:"
- "code"
- "compare:"
- "compatabilityVersionForAssetType:"
- "compatibilityVersionByAssetType"
- "completedUpdateCycleWithError:"
- "components:fromDate:"
- "conformsToProtocol:"
- "connectionUsageQueue"
- "containsObject:"
- "contentItemsFromAssets:matchingFilter:"
- "contents"
- "contentsOfDirectoryAtPath:error:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAutoAssetAssertionForExistingAssertions"
- "createConnectionIfNecessary"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "createRemoteSyncStateForAssetType:"
- "createTrialClientWithWorkQueue:query:"
- "createUAFSubscriptionsForTrackedAssertions"
- "createWithExperimentIdentifiers:localURL:"
- "createWithQuery:supportedAssetSpecifiers:"
- "createWithWorkQueue:query:"
- "createXPCInterface"
- "currentLockUsage"
- "currentStatus:"
- "currentStatusSync:"
- "d"
- "d16@0:8"
- "d24@0:8Q16"
- "d24@0:8q16"
- "dataHandler"
- "dataSource"
- "dataType"
- "dataWithContentsOfURL:options:error:"
- "date"
- "dateByAddingComponents:toDate:options:"
- "dateByAddingTimeInterval:"
- "dateForPreferenceKey:"
- "dateFromComponents:"
- "dds_dateForKey:"
- "dds_numberForKey:"
- "dds_stringForKey:"
- "dealloc"
- "debugDescription"
- "debuggingID"
- "debuggingIDsForAssets:"
- "decodeInt32ForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeTopLevelObjectOfClasses:forKey:error:"
- "defaultCenter"
- "defaultManager"
- "defaultQuery"
- "delegate"
- "delegates"
- "deleteV1AssetsIfNecessary"
- "description"
- "descriptors"
- "determineIfAvailable:withTimeout:completion:"
- "dictionary"
- "dictionaryWithContentsOfURL:"
- "dictionaryWithObjects:forKeys:count:"
- "didBeginUpdateCatalog"
- "didChangeDownloadState:forAsset:"
- "didCompleteDownloadForAssertion:error:"
- "didCompleteDownloadForAssertions:error:"
- "didEndUpdateCycleWithAssetType:error:"
- "didStartUpdateCycleForAssetType:"
- "didUpdateAssertion:atDate:"
- "didUpdateAssetsWithType:"
- "didUpdateCatalogWithAssetType:error:"
- "directoryValue"
- "doesContainAttributes:"
- "doubleValue"
- "downloadCompletionNotification"
- "downloadOptionsForCatalogWithType:discretionaryDownload:"
- "downloadOptionsForPolicy:discretionaryDownload:"
- "downloadOverCellular"
- "downloadStateByAssetID"
- "downloadWithoutPower"
- "dumpAssetLogWithAssertions:installedAssets:"
- "dumpDescription"
- "durationInSec"
- "earlierDate:"
- "eliminateAllForSelector:completion:"
- "eliminateInterestForAutoAsset:"
- "encodeInt32:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endLockUsage:completion:"
- "endObservingTypes:"
- "endTime"
- "entriesMatchingAttributes:"
- "enumerateAllowedValuesAndKeys:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "experimentIdentifiersWithNamespaceName:"
- "fetchAssetUpdateStatusDateForAutoAsset:"
- "fetchAssetUpdateStatusForQuery:callback:"
- "fetchAssetWithCallback:"
- "fetchCatalogBasedAssetUpdateStatusForAssertion:callback:"
- "fetchLockReasonCountForAutoAsset:callback:"
- "fetchTrialAssetForQuery:callback:"
- "fetchUpdateStatusForAutoAsset:completion:"
- "fileExistsAtPath:"
- "fileName"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "filter"
- "filters"
- "firstObject"
- "getLocalUrl"
- "handleAddedNewDescriptor:forAssertion:"
- "handleEndedConnection:"
- "handleNewAssertions:"
- "handleRemovedAssertions:"
- "hasAsset"
- "hasPath"
- "hasPrefix:"
- "hash"
- "hashDictionary:"
- "hashObject:"
- "hashSet:"
- "hashTableWithOptions:"
- "i16@0:8"
- "identifier"
- "idleUsageEvictionPeriod"
- "init"
- "initForAssetType:withAssetSpecifier:"
- "initForClientName:selectingAsset:error:"
- "initWithArray:"
- "initWithAssertionStorageFileURL:"
- "initWithAsset:"
- "initWithAssetProvider:dataSource:"
- "initWithAssetSetManager:"
- "initWithAssetType:assetSpecifier:"
- "initWithAssetType:filter:"
- "initWithAssetType:filter:localOnly:installedOnly:latestOnly:cachedOnly:"
- "initWithAssetType:languageIdentifier:"
- "initWithAttributes:localURL:"
- "initWithClient:"
- "initWithCoder:"
- "initWithContentsOfFile:options:error:"
- "initWithDataHandler:uafManager:"
- "initWithDataSource:"
- "initWithDelegate:assetType:"
- "initWithDictionary:"
- "initWithExperimentId:deploymentId:treatmentId:"
- "initWithExperimentId:treatmentId:deploymentId:"
- "initWithExperimentIdentifiers:attributes:localURL:"
- "initWithFormat:"
- "initWithIdentifier:"
- "initWithInteger:"
- "initWithLanguageIdentifier:"
- "initWithMAAsset:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithName:assetSets:usageAliases:"
- "initWithParentAsset:contents:"
- "initWithPolicy:assertionID:clientID:"
- "initWithProjectId:namespaceId:"
- "initWithProvider:dataSource:"
- "initWithProvider:tracker:"
- "initWithProvider:tracker:dataSource:"
- "initWithProvider:tracker:dataSource:autoAssetManager:"
- "initWithQuery:"
- "initWithQueue:provider:trialManager:autoAssetManager:createXPCInterface:"
- "initWithString:"
- "initWithTimeIntervalSince1970:"
- "initWithType:"
- "initWithUnsignedInteger:"
- "initWithWorkQueue:"
- "initWithWorkQueue:dataSource:"
- "initWithWorkQueue:triClient:triNamespaceName:"
- "initWithXPCServiceName:"
- "initWithXPCServiceName:assertionStorageDirectoryURL:"
- "initWithXPCServiceName:assertionStorageFileURL:"
- "installDate"
- "installedOnly"
- "intValue"
- "integerValue"
- "interestInContent:completion:"
- "interestInContentForAutoAsset:completion:"
- "interface"
- "interfaceWithProtocol:"
- "intervalForDownloadFrequency:"
- "invalidate"
- "invalidateDescription"
- "isAutoAssetType:"
- "isEnabled"
- "isEqual:"
- "isEqualToAssertion:"
- "isEqualToAssetPolicy:"
- "isEqualToAssetQuery:"
- "isEqualToContentItem:"
- "isEqualToDate:"
- "isEqualToDescriptor:"
- "isEqualToQueryFilter:"
- "isEqualToString:"
- "isInteger:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isStalled"
- "languageCode"
- "lastAction"
- "lastUpdated"
- "latestAssetsOnlyFromAssets:"
- "latestBetweenAssetA:AssetB:"
- "latestOnly"
- "length"
- "levelForFactor:withNamespaceName:"
- "linguisticAssetCompatabilityVersion"
- "listener"
- "listener:shouldAcceptNewConnection:"
- "loadAssertionData"
- "loadState"
- "loadStateAndScheduleUpdate"
- "localOnly"
- "locale"
- "localeWithLocaleIdentifier:"
- "lockAssetsForQuery:"
- "lockAutoAsset:forReason:withTimeout:completion:"
- "lockAutoAssetSync:forReason:error:"
- "lockContent:withUsagePolicy:withTimeout:completion:"
- "lockContentSync:withTimeout:lockedAssetSelector:newerInProgress:error:"
- "maAsset"
- "maAssetQueryForDDSAssetQuery:compatabilityVersion:platformVersion:internalInstall:"
- "maAssetQueryForddsAssetQuery:compatiblilityVersion:platformVersion:internalInstall:"
- "manager"
- "managerInterfaceByAssetType"
- "managerInterfaceForAssetType:"
- "managerInterfaces"
- "mecabraDictionaryRapidUpdatesAssetCompatabilityVersion"
- "metadataSyncStatePreferenceKey"
- "minusSet:"
- "modifyAssetUpdateStatusForAssertion:status:"
- "modifyUpdateStatusForAssertion:toStatus:"
- "mutableCopy"
- "name"
- "namespaceNameFromId:"
- "newerVersionAttributes"
- "newerVersionDiscovered"
- "nextUpdateTimeIntervalForAttemptCount:"
- "notificationDownloadTriggers"
- "notificationToken"
- "notifications"
- "notifyObserversAssetsUpdatedForType:"
- "notifyRegistrationName:forAssetType:"
- "now"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "objCType"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeAssetType:"
- "parentAsset"
- "path"
- "pathComponents"
- "pendingAssertionsToUpdateByAssetType"
- "performScheduledActivityWithIdentifier:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "policy"
- "postNotificationName:object:"
- "preferredDownloadFrequency"
- "processInfo"
- "processName"
- "propertyListWithData:options:format:error:"
- "provider"
- "purge:"
- "q"
- "q16@0:8"
- "q24@0:8@\"DDSAssertion\"16"
- "q24@0:8@16"
- "q32@0:8@16q24"
- "query"
- "queryMetaDataSync"
- "queue"
- "recordAssetAction:forAsset:"
- "recordUpdateCycleState:"
- "refresh"
- "region"
- "registerDelegate:"
- "registerInterestInContentForQuery:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "remoteServer"
- "remoteSyncStateByAssetType"
- "remoteSyncStateRequestsResetForAssetType:"
- "remoteSyncStateRequestsRetryForAssetType:"
- "remoteSyncStateRequestsUpdateForAssetType:"
- "removeAllObjects"
- "removeAllowedValue:forKey:"
- "removeAllowedValues:forKey:"
- "removeAssertionWithID:"
- "removeAssertionWithIdentifier:"
- "removeAssertionWithIdentifier:assetType:"
- "removeAssertionWithIdentifier:clientID:"
- "removeAssets:"
- "removeAssetsForAssertions:"
- "removeDescriptorWithAssertionID:"
- "removeDescriptorWithClientID:"
- "removeEntriesWithPrefixKey:"
- "removeObject:"
- "removeObjectForKey:"
- "removeOldAssets"
- "removeOldAssetsForAssertions:"
- "removeUpdateHandlerForToken:"
- "reportAssetDownloadAnalytic:"
- "reportUpdateCycleAnalytic:"
- "requestCompleteRefresh"
- "requestRetry"
- "requestUpdate"
- "resetAssertionDueDatesForAssetType:"
- "resetState"
- "respondsToSelector:"
- "results"
- "resume"
- "retain"
- "retainCount"
- "returnTypes:"
- "roundNumber:toSignificantDigits:"
- "saveAssertionData:"
- "saveState"
- "scheduleActivityWithIdentifier:interval:tolerance:"
- "scheduleRegularUpdate"
- "scheduleRetry"
- "scheduleRetryIdentifier"
- "scheduleUpdateIdentifier"
- "scheduleWithBlock:"
- "scheduler"
- "schedulerByIdentifier"
- "self"
- "server"
- "serverDidUpdateAssetsWithType:"
- "serverOverride"
- "serviceObjectProxy"
- "set"
- "setAllowsCellularAccess:"
- "setAllowsExpensiveAccess:"
- "setAssertionIdentifier:"
- "setAsset:"
- "setAssetProvider:"
- "setAssetTypesForDelegates:"
- "setAttemptCount:"
- "setBuildVersion:"
- "setCachedOnly:"
- "setCatalogUpdateDate:forAssetType:"
- "setClass:forSelector:argumentIndex:ofReply:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClientIdentifier:"
- "setCompatabilityVersion:forAssetType:"
- "setContents:"
- "setDate:"
- "setDate:forPreferenceKey:"
- "setDateFormat:"
- "setDay:"
- "setDelay:"
- "setDelegate:"
- "setDescriptors:"
- "setDiscretionary:"
- "setDoNotBlockBeforeFirstUnlock:"
- "setDoNotBlockOnNetworkStatus:"
- "setDownloadCompletionNotification:"
- "setDownloadOverCellular:"
- "setDownloadWithoutPower:"
- "setEndTime:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFetchAssetUpdateStatusDateForAutoAsset:"
- "setFilters:"
- "setHour:"
- "setIdleUsageEvictionPeriod:"
- "setInstalledOnly:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLastAction:"
- "setLastUpdated:"
- "setLatestOnly:"
- "setLocalOnly:"
- "setLocale:"
- "setMinute:"
- "setNotificationDownloadTriggers:"
- "setNotificationToken:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setParentAsset:"
- "setPolicy:"
- "setPreferredDownloadFrequency:"
- "setQualityOfService:"
- "setRemoteObjectInterface:"
- "setRemoteServer:"
- "setRepeats:"
- "setRequiresPowerPluggedIn:"
- "setRetries:"
- "setScheduler:"
- "setSchedulerByIdentifier:"
- "setServerOverride:"
- "setStartTime:"
- "setSuccess:"
- "setSyncStatus:"
- "setTolerance:"
- "setUpAssertionStorageDirectory"
- "setUpTrialForQuery:"
- "setUserInitiated:"
- "setWithArray:"
- "setWithObject:"
- "setWithObjects:"
- "setXPCServiceName:forAssetType:"
- "sharedInstance"
- "sharedInstanceWithConfiguration:"
- "sharedManager"
- "sharedProvider"
- "shortName"
- "shouldDownloadAutoAsset"
- "shouldInitiateRegularUpdateCycle"
- "shouldLenientlyMatchWithContentItemsForRegion:"
- "shouldMatchAttributeValue:givenValue:"
- "shouldRequestCompleteRefresh"
- "start"
- "startCatalogDownload:options:then:"
- "startCatalogDownloadForAssetType:withDownloadOptions:withCompletion:"
- "startDownload:then:"
- "startDownloadForAsset:withOptions:progress:handler:"
- "startTime"
- "state"
- "string"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByAppendingPathExtension:"
- "stringByAppendingString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringForAction:"
- "stringForAssetDownloadFrequency:"
- "stringFromDate:"
- "stringFromInteger:"
- "stringValue"
- "stringWithFormat:"
- "subscribe:subscriptions:completion:"
- "subscribe:subscriptions:queue:completion:"
- "subscriberNameForClientID:"
- "subscriptionNameForAssertionID:withIndex:"
- "subscriptionNamePrefixForAssertionID:"
- "subscriptionsForSubscriber:"
- "superclass"
- "supportedAutoAssetSpecifiers"
- "supportedLocales"
- "supportsQuery:"
- "supportsSecureCoding"
- "syncServer"
- "syncServiceObjectProxy"
- "syncStatus"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "systemLocale"
- "teardownXPCConnection"
- "timeBetweenSyncs"
- "timeIntervalSince1970"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "timeIntervalUntilNextRegularUpdate"
- "totalExpected"
- "totalWritten"
- "trackedAssertionSets"
- "trackedAssertions"
- "trackedAssetTypes"
- "tracker"
- "triClient"
- "triNamespaceName"
- "trialClient:didReceiveAsset:"
- "trialClientByQuery"
- "trialClientDidStop:"
- "trialDidReceiveAsset:forQuery:"
- "trialDidStopForQuery:"
- "trialManager"
- "triggerDumpWithReply:"
- "triggerUpdate"
- "type"
- "typesToObserve"
- "uafManager"
- "uafUsagesForQuery:"
- "unarchivedObjectOfClasses:fromData:error:"
- "unionSet:"
- "uniqueIdentifier"
- "unlockAutoAsset:forReason:"
- "unregisterDelegate:"
- "unregisterInterestInContentForAssetSelector:"
- "unsignedIntegerValue"
- "unsubscribe:subscriptionNames:completion:"
- "unsubscribe:subscriptionNames:queue:completion:"
- "updatableAssetsForAssertion:"
- "updateAssetForQuery:callback:"
- "updateAutoAsset:forReason:completion:"
- "updateAutoAssetForAssetType:"
- "updateCatalogBasedAssetForAssertion:callback:"
- "updateCatalogForAssetType:discretionaryDownload:withCompletion:"
- "updateCatalogForAssetType:withCompletion:"
- "updateCatalogMetadataKeyForAssetType:"
- "updateStatusForAssertion:"
- "updateWithAction:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"<DDSAssetObservingDelegate>\"16"
- "v24@0:8@\"<DDSAssetProvidingDelegate>\"16"
- "v24@0:8@\"<DDSAssetTrackingDelegate>\"16"
- "v24@0:8@\"<DDSManagingDelegate>\"16"
- "v24@0:8@\"<DDSTrialClient>\"16"
- "v24@0:8@\"<DDSTrialClientDelegate>\"16"
- "v24@0:8@\"<DDSTrialManagerDelegate>\"16"
- "v24@0:8@\"<TRINotificationToken>\"16"
- "v24@0:8@\"DDSAssetQuery\"16"
- "v24@0:8@\"DDSMAAutoAssetSelector\"16"
- "v24@0:8@\"DDSTrialQuery\"16"
- "v24@0:8@\"MAAutoAssetSelector\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSString\">16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"NSSet\"16B24"
- "v28@0:8@16B24"
- "v28@0:8i16@20"
- "v32@0:8@\"<DDSTrialClient>\"16@\"DDSTrialAsset\"24"
- "v32@0:8@\"DDSAssertDescriptor\"16@\"DDSAssertion\"24"
- "v32@0:8@\"DDSAssertion\"16@\"NSDate\"24"
- "v32@0:8@\"DDSAssertion\"16@\"NSError\"24"
- "v32@0:8@\"DDSAssertion\"16q24"
- "v32@0:8@\"DDSAssetQuery\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
- "v32@0:8@\"DDSAssetQuery\"16@?<v@?q@\"NSError\">24"
- "v32@0:8@\"DDSTrialAsset\"16@\"DDSTrialQuery\"24"
- "v32@0:8@\"DDSTrialQuery\"16@?<v@?@\"DDSTrialAsset\"@\"NSError\">24"
- "v32@0:8@\"MAAutoAsset\"16@\"NSString\"24"
- "v32@0:8@\"MAAutoAsset\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"MAAutoAsset\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
- "v32@0:8@\"MAAutoAsset\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSDate\"16@\"NSString\"24"
- "v32@0:8@\"NSSet\"16@\"NSError\"24"
- "v32@0:8@\"NSString\"16@\"NSError\"24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSSet\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16B24B28"
- "v32@0:8@16q24"
- "v32@0:8Q16@\"DDSAsset\"24"
- "v32@0:8Q16@24"
- "v32@0:8q16@\"NSString\"24"
- "v32@0:8q16@24"
- "v36@0:8@\"DDSAssertion\"16B24@?<v@?@\"DDSAssertion\"@\"NSError\">28"
- "v36@0:8@\"NSString\"16B24@?<v@?@\"NSError\">28"
- "v36@0:8@16B24@?28"
- "v40@0:8@\"DDSAssetQuery\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@\"MAAutoAsset\"16@\"NSString\"24@?<v@?@\"NSURL\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"MADownloadOptions\"24@?<v@?q>32"
- "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16d24d32"
- "v48@0:8@\"DDSAsset\"16@\"MADownloadOptions\"24@?<v@?@\"MAProgressNotification\">32@?<v@?q>40"
- "v48@0:8@\"DDSAssetQuery\"16@\"DDSAssetPolicy\"24@\"NSString\"32@\"NSString\"40"
- "v48@0:8@\"MAAutoAsset\"16@\"NSString\"24q32@?<v@?@\"NSURL\"@\"NSError\">40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@?32@?40"
- "v48@0:8@16@24q32@?40"
- "v52@0:8@16@24B32^@36@?44"
- "willRetryUpdateCycle"
- "workQueue"
- "writeToURL:options:error:"
- "xpcConnectionOptionsForServer"
- "xpcServiceName"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
