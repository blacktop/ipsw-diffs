## DataDeliveryServices

> `/System/Library/PrivateFrameworks/DataDeliveryServices.framework/DataDeliveryServices`

```diff

-64.0.0.0.0
-  __TEXT.__text: 0x1ea30
+64.8.0.0.0
+  __TEXT.__text: 0x23850
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x1cd4
-  __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0x3b4
-  __TEXT.__cstring: 0xfdb
-  __TEXT.__oslogstring: 0x237e
-  __TEXT.__unwind_info: 0x938
+  __TEXT.__objc_methlist: 0x1e58
+  __TEXT.__const: 0xf0
+  __TEXT.__gcc_except_tab: 0x4d4
+  __TEXT.__cstring: 0x11c1
+  __TEXT.__oslogstring: 0x2c46
+  __TEXT.__unwind_info: 0xa00
   __TEXT.__objc_classname: 0x4ce
-  __TEXT.__objc_methname: 0x4bc2
-  __TEXT.__objc_methtype: 0x11f8
-  __TEXT.__objc_stubs: 0x4100
+  __TEXT.__objc_methname: 0x504e
+  __TEXT.__objc_methtype: 0x136c
+  __TEXT.__objc_stubs: 0x44c0
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0xb58
+  __DATA_CONST.__const: 0xcc0
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x73f8
-  __DATA_CONST.__objc_selrefs: 0x11e0
-  __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__objc_const: 0x10d8
-  __AUTH_CONST.__cfstring: 0x1240
+  __DATA_CONST.__objc_const: 0x75a8
+  __DATA_CONST.__objc_selrefs: 0x12e0
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x268
+  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_arraydata: 0x70
+  __AUTH_CONST.__objc_const: 0x1168
+  __AUTH_CONST.__cfstring: 0x1400
   __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__auth_got: 0x330
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x260
-  __DATA.__objc_superrefs: 0x108
-  __DATA.__objc_ivar: 0x1fc
-  __DATA.__data: 0xaa8
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x20c
+  __DATA.__data: 0xab0
   __DATA.__bss: 0x38
-  __DATA_DIRTY.__objc_data: 0xbe0
+  __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 830
-  Symbols:   3265
-  CStrings:  1442
+  Functions: 886
+  Symbols:   3434
+  CStrings:  1549
 
Symbols:
+ +[DDSMAAutoAssetManager isAutoAssetType:]
+ +[DDSMAAutoAssetProvider fetchAssetUpdateStatusDateForAutoAsset:]
+ +[DDSMAAutoAssetProvider setFetchAssetUpdateStatusDateForAutoAsset:]
+ +[DDSMAAutoAssetSelector allSupportedLinguisticAssetTypeForAssetType:]
+ +[DDSMAAutoAssetSelector allSupportedLinguisticAssetTypeForAssetType:].cold.1
+ +[DDSMAAutoAssetSelector createWithQuery:].cold.3
+ -[DDSAssetCenter autoAssetManager]
+ -[DDSAssetCenter initWithQueue:provider:trialManager:autoAssetManager:createXPCInterface:]
+ -[DDSAssetObserver autoAssetTypes]
+ -[DDSLinguisticAttributeFilter addLinguisticAssetType:]
+ -[DDSMAAutoAssetManager assetQueryResultsCache]
+ -[DDSMAAutoAssetManager assetsAvailableOnDeviceForQuery:]
+ -[DDSMAAutoAssetManager assetsForQuery:]
+ -[DDSMAAutoAssetManager autoAssetSelectorsForQuery:]
+ -[DDSMAAutoAssetManager autoAssetTypeForAsserType:]
+ -[DDSMAAutoAssetManager autoAssetsForQuery:]
+ -[DDSMAAutoAssetManager fetchAssetUpdateStatusForQuery:callback:]
+ -[DDSMAAutoAssetManager lockAssetsForQuery:]
+ -[DDSMAAutoAssetManager registerInterestInContentForQuery:]
+ -[DDSMAAutoAssetManager serverDidUpdateAssetsWithType:]
+ -[DDSMAAutoAssetManager unregisterInterestInContentForAssetSelector:]
+ -[DDSMAAutoAssetManager updateAssetForQuery:callback:]
+ -[DDSMAAutoAssetManager workQueue]
+ -[DDSMAAutoAssetProvider autoAssetForAssetSelector:]
+ -[DDSMAAutoAssetProvider autoAssetForAssetSelector:].cold.1
+ -[DDSMAAutoAssetProvider eliminateInterestForAutoAsset:]
+ -[DDSMAAutoAssetProvider fetchUpdateStatusForAutoAsset:completion:]
+ -[DDSMAAutoAssetProvider fetchUpdateStatusForAutoAsset:completion:].cold.1
+ -[DDSMAAutoAssetProvider interestInContentForAutoAsset:completion:]
+ -[DDSMAAutoAssetProvider lockAutoAsset:forReason:withTimeout:completion:]
+ -[DDSMAAutoAssetProvider lockAutoAssetSync:forReason:error:]
+ -[DDSMAAutoAssetProvider unlockAutoAsset:forReason:]
+ -[DDSMAAutoAssetProvider updateAutoAsset:forReason:completion:]
+ -[DDSMAAutoAssetSelector description]
+ -[DDSMAAutoAssetSelector hash]
+ -[DDSMAAutoAssetSelector isEqual:]
+ -[DDSManager assetUpdateStatusForAssertion:].cold.1
+ -[DDSManager autoAssetQueryForAssertion:]
+ -[DDSManager createAutoAssetAssertionForExistingAssertions]
+ -[DDSManager fetchCatalogBasedAssetUpdateStatusForAssertion:callback:]
+ -[DDSManager modifyAssetUpdateStatusForAssertion:status:]
+ -[DDSManager updateAutoAssetForAssetType:]
+ -[DDSManager updateCatalogBasedAssetForAssertion:callback:]
+ GCC_except_table17
+ GCC_except_table31
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table57
+ GCC_except_table58
+ _AutoAssetErrorCodeUpdateFailed
+ _DDSAssetDownloadUIError
+ _DDSAttributeLinguisticAssetType
+ _DDSAutoAssetFetchAssetUpdateStatusInterval
+ _DDSAutoAssetPreferencesKey
+ _DDSAutoAssetProviderErrorDomain
+ _DDSClientId
+ _OBJC_CLASS_$_MAAutoAssetNotifications
+ _OBJC_IVAR_$_DDSAssetCenter._autoAssetManager
+ _OBJC_IVAR_$_DDSAssetObserver._autoAssetTypes
+ _OBJC_IVAR_$_DDSMAAutoAssetManager._assetQueryResultsCache
+ _OBJC_IVAR_$_DDSMAAutoAssetManager._workQueue
+ __OBJC_$_CLASS_METHODS_DDSMAAutoAssetManager
+ __OBJC_$_CLASS_METHODS_DDSMAAutoAssetProvider
+ __OBJC_$_PROP_LIST_DDSManagerDataSource.52
+ __OBJC_$_PROP_LIST_DDSMobileAssetv2ProviderDataSource.298
+ __OBJC_$_PROP_LIST_DDSTrialClient.99
+ __OBJC_$_PROP_LIST_DDSTrialManager.88
+ __OBJC_$_PROP_LIST_DDSTrialManagerDataSource.49
+ ___40-[DDSMAAutoAssetManager assetsForQuery:]_block_invoke
+ ___43-[DDSManager updateAssetForQuery:callback:]_block_invoke.262
+ ___43-[DDSManager updateAssetForQuery:callback:]_block_invoke_3
+ ___43-[DDSManager updateAssetForQuery:callback:]_block_invoke_4
+ ___48-[DDSAssetCenter serverDidUpdateAssetsWithType:]_block_invoke.256
+ ___48-[DDSServer listener:shouldAcceptNewConnection:]_block_invoke.258
+ ___48-[DDSServer listener:shouldAcceptNewConnection:]_block_invoke.258.cold.1
+ ___51-[DDSManager didEndUpdateCycleWithAssetType:error:]_block_invoke.250
+ ___52-[DDSMAAutoAssetProvider unlockAutoAsset:forReason:]_block_invoke
+ ___54-[DDSMAAutoAssetManager updateAssetForQuery:callback:]_block_invoke
+ ___54-[DDSManager fetchAssetUpdateStatusForQuery:callback:]_block_invoke.258
+ ___54-[DDSManager fetchAssetUpdateStatusForQuery:callback:]_block_invoke.260
+ ___54-[DDSManager fetchAssetUpdateStatusForQuery:callback:]_block_invoke_3
+ ___56-[DDSMAAutoAssetProvider eliminateInterestForAutoAsset:]_block_invoke
+ ___56-[DDSMAAutoAssetProvider eliminateInterestForAutoAsset:]_block_invoke.cold.1
+ ___59-[DDSMAAutoAssetManager registerInterestInContentForQuery:]_block_invoke
+ ___59-[DDSMAAutoAssetManager registerInterestInContentForQuery:]_block_invoke.9
+ ___59-[DDSManager updateCatalogBasedAssetForAssertion:callback:]_block_invoke
+ ___59-[DDSManager updateCatalogBasedAssetForAssertion:callback:]_block_invoke.261
+ ___59-[DDSManager updateCatalogBasedAssetForAssertion:callback:]_block_invoke.261.cold.1
+ ___59-[DDSManager updateCatalogBasedAssetForAssertion:callback:]_block_invoke.261.cold.2
+ ___63-[DDSMAAutoAssetProvider updateAutoAsset:forReason:completion:]_block_invoke
+ ___63-[DDSMAAutoAssetProvider updateAutoAsset:forReason:completion:]_block_invoke.39
+ ___65-[DDSMAAutoAssetManager fetchAssetUpdateStatusForQuery:callback:]_block_invoke
+ ___65-[DDSMAAutoAssetManager fetchAssetUpdateStatusForQuery:callback:]_block_invoke.cold.1
+ ___67-[DDSMAAutoAssetProvider fetchUpdateStatusForAutoAsset:completion:]_block_invoke
+ ___67-[DDSMAAutoAssetProvider fetchUpdateStatusForAutoAsset:completion:]_block_invoke.36
+ ___67-[DDSMAAutoAssetProvider fetchUpdateStatusForAutoAsset:completion:]_block_invoke.37
+ ___67-[DDSMAAutoAssetProvider interestInContentForAutoAsset:completion:]_block_invoke
+ ___67-[DDSMAAutoAssetProvider interestInContentForAutoAsset:completion:]_block_invoke.cold.1
+ ___70-[DDSManager fetchCatalogBasedAssetUpdateStatusForAssertion:callback:]_block_invoke
+ ___70-[DDSManager fetchCatalogBasedAssetUpdateStatusForAssertion:callback:]_block_invoke.cold.1
+ ___72-[DDSManager beginUpdateCycleForAssetType:forced:discretionaryDownload:]_block_invoke.242
+ ___73-[DDSMAAutoAssetProvider lockAutoAsset:forReason:withTimeout:completion:]_block_invoke
+ ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.261
+ ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.261.cold.1
+ ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.261.cold.2
+ ___block_descriptor_40_e8_32bs_e27_v24?0"NSURL"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e39_v24?0"MAAutoAssetStatus"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e41_v24?0"MAAutoAssetSelector"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v24?0q8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e41_v24?0"MAAutoAssetSelector"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e58_v32?0"MAAutoAssetSelector"8"NSDictionary"16"NSError"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e76_v44?0"MAAutoAssetSelector"8B16"NSURL"20"MAAutoAssetStatus"28"NSError"36ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e58_v32?0"MAAutoAssetSelector"8"NSDictionary"16"NSError"24ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40bs48r56r64r_e20_v20?0B8"NSError"12lr48l8r56l8s32l8r64l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e20_v24?0q8"NSError"16ls32l8s48l8r56l8r64l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e30_v24?0"NSNumber"8"NSError"16ls32l8r56l8s40l8s48l8r64l8
+ ___block_descriptor_80_e8_32s40s48bs56r64r72w_e5_v8?0ls32l8r56l8w72l8s40l8s48l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r72r_e27_v24?0"NSURL"8"NSError"16lr64l8s32l8s40l8s48l8r72l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r72r_e8_v16?0q8ls32l8s40l8r64l8s48l8r72l8s56l8
+ ___block_descriptor_88_e8_32s40s48bs56r64r72w_e5_v8?0ls32l8s48l8r56l8r64l8w72l8s40l8
+ ___block_literal_global.247
+ __unnamed_array_storage.25
+ __unnamed_array_storage.30
+ __unnamed_array_storage.31
+ __unnamed_array_storage.37
+ __unnamed_array_storage.38
+ __unnamed_array_storage.44
+ __unnamed_array_storage.45
+ __unnamed_array_storage.51
+ __unnamed_array_storage.52
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$allSupportedLinguisticAssetTypeForAssetType:
+ _objc_msgSend$assetsAvailableOnDeviceForQuery:
+ _objc_msgSend$assetsForQuery:
+ _objc_msgSend$autoAssetForAssetSelector:
+ _objc_msgSend$autoAssetQueryForAssertion:
+ _objc_msgSend$autoAssetSelectorsForQuery:
+ _objc_msgSend$autoAssetTypeForAsserType:
+ _objc_msgSend$autoAssetTypes
+ _objc_msgSend$autoAssetsForQuery:
+ _objc_msgSend$availableForUseAttributes
+ _objc_msgSend$createAutoAssetAssertionForExistingAssertions
+ _objc_msgSend$currentStatusSync:
+ _objc_msgSend$determineIfAvailable:withTimeout:completion:
+ _objc_msgSend$eliminateAllForSelector:completion:
+ _objc_msgSend$eliminateInterestForAutoAsset:
+ _objc_msgSend$endLockUsage:completion:
+ _objc_msgSend$fetchAssetUpdateStatusDateForAutoAsset:
+ _objc_msgSend$fetchCatalogBasedAssetUpdateStatusForAssertion:callback:
+ _objc_msgSend$fetchUpdateStatusForAutoAsset:completion:
+ _objc_msgSend$initWithAttributes:localURL:
+ _objc_msgSend$initWithQueue:provider:trialManager:autoAssetManager:createXPCInterface:
+ _objc_msgSend$interestInContent:completion:
+ _objc_msgSend$interestInContentForAutoAsset:completion:
+ _objc_msgSend$isAutoAssetType:
+ _objc_msgSend$lockAssetsForQuery:
+ _objc_msgSend$lockAutoAsset:forReason:withTimeout:completion:
+ _objc_msgSend$lockAutoAssetSync:forReason:error:
+ _objc_msgSend$lockContentSync:withTimeout:lockedAssetSelector:newerInProgress:error:
+ _objc_msgSend$modifyAssetUpdateStatusForAssertion:status:
+ _objc_msgSend$newerVersionAttributes
+ _objc_msgSend$newerVersionDiscovered
+ _objc_msgSend$notifications
+ _objc_msgSend$notifyRegistrationName:forAssetType:
+ _objc_msgSend$registerInterestInContentForQuery:
+ _objc_msgSend$setFetchAssetUpdateStatusDateForAutoAsset:
+ _objc_msgSend$unlockAutoAsset:forReason:
+ _objc_msgSend$unregisterInterestInContentForAssetSelector:
+ _objc_msgSend$updateAutoAsset:forReason:completion:
+ _objc_msgSend$updateAutoAssetForAssetType:
+ _objc_msgSend$updateCatalogBasedAssetForAssertion:callback:
+ _objc_retain_x28
- +[DDSManager errorForDDSAssetDownloadUIErrorCode:]
- -[DDSAssetCenter initWithQueue:provider:trialManager:createXPCInterface:]
- -[DDSMAAutoAssetManager downloadAssetForQuery:clientID:]
- -[DDSMAAutoAssetManager downloadAssetForQuery:clientID:].cold.1
- -[DDSMAAutoAssetManager downloadAssetForQuery:clientID:].cold.2
- -[DDSMAAutoAssetManager shouldDownloadAutoAssetForClient:]
- -[DDSMAAutoAssetProvider autoAssetForAssetSelector:clientID:]
- -[DDSMAAutoAssetProvider autoAssetForAssetSelector:clientID:].cold.1
- -[DDSMAAutoAssetProvider lockAutoAsset:callback:]
- -[DDSManager downloadAutoAssetForAssertions:]
- GCC_except_table30
- GCC_except_table45
- __OBJC_$_PROP_LIST_DDSManagerDataSource.51
- __OBJC_$_PROP_LIST_DDSMobileAssetv2ProviderDataSource.273
- __OBJC_$_PROP_LIST_DDSTrialClient.98
- __OBJC_$_PROP_LIST_DDSTrialManager.87
- __OBJC_$_PROP_LIST_DDSTrialManagerDataSource.48
- ___43-[DDSManager updateAssetForQuery:callback:]_block_invoke.263
- ___43-[DDSManager updateAssetForQuery:callback:]_block_invoke_2.cold.1
- ___43-[DDSManager updateAssetForQuery:callback:]_block_invoke_2.cold.2
- ___48-[DDSAssetCenter serverDidUpdateAssetsWithType:]_block_invoke.229
- ___48-[DDSServer listener:shouldAcceptNewConnection:]_block_invoke.234
- ___48-[DDSServer listener:shouldAcceptNewConnection:]_block_invoke.234.cold.1
- ___49-[DDSMAAutoAssetProvider lockAutoAsset:callback:]_block_invoke
- ___51-[DDSManager didEndUpdateCycleWithAssetType:error:]_block_invoke.225
- ___54-[DDSManager fetchAssetUpdateStatusForQuery:callback:]_block_invoke.262
- ___54-[DDSManager fetchAssetUpdateStatusForQuery:callback:]_block_invoke_2.cold.1
- ___56-[DDSMAAutoAssetManager downloadAssetForQuery:clientID:]_block_invoke
- ___56-[DDSMAAutoAssetManager downloadAssetForQuery:clientID:]_block_invoke.7
- ___56-[DDSMAAutoAssetManager downloadAssetForQuery:clientID:]_block_invoke.7.cold.1
- ___56-[DDSMAAutoAssetManager downloadAssetForQuery:clientID:]_block_invoke.cold.1
- ___72-[DDSManager beginUpdateCycleForAssetType:forced:discretionaryDownload:]_block_invoke.218
- ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.237
- ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.237.cold.1
- ___84-[DDSMobileAssetv2Provider beginDownloadForAssertion:discretionaryDownload:handler:]_block_invoke.237.cold.2
- ___block_descriptor_40_e8_32bs_e76_v44?0"MAAutoAssetSelector"8B16"NSURL"20"MAAutoAssetStatus"28"NSError"36ls32l8
- ___block_descriptor_40_e8_32s_e44_v28?0"MAAutoAssetSelector"8B16"NSError"20ls32l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56s_e30_v24?0"NSNumber"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64bs72r80r_e8_v16?0q8ls32l8s40l8r72l8s48l8s56l8r80l8s64l8
- ___block_descriptor_96_e8_32s40s48s56bs64r72r80w_e5_v8?0ls32l8r64l8s40l8w80l8s48l8r72l8s56l8
- ___block_literal_global.222
- __unnamed_array_storage.233
- __unnamed_array_storage.238
- __unnamed_array_storage.239
- __unnamed_array_storage.245
- __unnamed_array_storage.246
- __unnamed_array_storage.252
- __unnamed_array_storage.253
- _objc_msgSend$autoAssetForAssetSelector:clientID:
- _objc_msgSend$clientIdentifiers
- _objc_msgSend$downloadAssetForQuery:clientID:
- _objc_msgSend$downloadAutoAssetForAssertions:
- _objc_msgSend$errorForDDSAssetDownloadUIErrorCode:
- _objc_msgSend$fetchLockReasonCountForAutoAsset:callback:
- _objc_msgSend$initWithQueue:provider:trialManager:createXPCInterface:
- _objc_msgSend$isEqualToNumber:
- _objc_msgSend$lockAutoAsset:callback:
- _objc_msgSend$setLockInhibitsEmergencyRemoval:
- _objc_msgSend$shouldDownloadAutoAssetForClient:
- _objc_retain_x10
CStrings:
+ "\x18"
+ "\""
+ "%@-%@-%@"
+ "@\"DDSAsset\"40@0:8@\"MAAutoAsset\"16@\"NSString\"24^@32"
+ "@\"MAAutoAsset\"24@0:8@\"DDSMAAutoAssetSelector\"16"
+ "@\"NSArray\"24@0:8@\"DDSAssetQuery\"16"
+ "@40@0:8@16@24^@32"
+ "@56@0:8@16@24@32@40@?48"
+ "ASSET_VERSION_DOWNLOADED"
+ "Asked to remove assertions for auto asset"
+ "Auto Asset: %@, Attributes: %@"
+ "Auto asset content is downloaded now unlock the auto asset: %{public}@"
+ "Auto asset content is updated, now unlock the auto asset: %{public}@"
+ "Auto asset lock failed for asset: %{public}@ with error: %{public}@"
+ "Auto asset object cannot be created for asset selector: %{public}@"
+ "Auto asset update status: (%ld) for query: (%{public}@)"
+ "Auto asset: %@, determineIfAvailable failed with error: %@"
+ "Auto asset: %{public}@ present at path: %{public}@"
+ "Auto asset: %{public}@ unlocked successfully"
+ "AutoAsset support is disabled"
+ "Begin update cycle for auto asset corresponding to asset type %@ ..."
+ "Cannot create auto asset for asset selector: %@ due to error: %@"
+ "Cannot create auto asset instance with selector: %@, error: %@"
+ "Cannot determine the latest auto asset version due to error: %@"
+ "Cannot eliminate interest in content for asset selector: %{public}@"
+ "Cannot fetch the asset update status"
+ "Cannot fetch the current status of auto asset due to error: %@"
+ "Catalog based asset update status: (%ld) for query: (%{public}@)"
+ "Create auto asset assertions for existing assertions"
+ "Created DDSMAAutoAssetSelectors: %@ for query: %@"
+ "DDSAutoAssetPreferences"
+ "DDSAutoAssetProviderErrorDomain"
+ "Determine latest version of auto asset: %@ on server"
+ "Did server lookup for auto asset: %@ on %@"
+ "Download latest version of auto asset: %@"
+ "Eliminate interest in content for asset selector: %{public}@"
+ "EnableLinguisticDataAutoAsset"
+ "End lock for auto asset: %{public}@ failed with error: %{public}@"
+ "Failed to get content localContentURL for: %{public}@ with error: %{public}@"
+ "Failed to lock the auto asset: %{public}@, with error: %{public}@"
+ "Fetch asset update status for auto asset: %@"
+ "Fetch asset update status for query: %{public}@"
+ "Fetch asset update status for query: (%{public}@)"
+ "Fetch auto asset update status failed for asset: %{public}@ with error: %{public}@"
+ "Fetch status for locked auto asset: %@ completed with error: %@"
+ "Handle new assertion for auto asset with override asset type: %{public}@, assertion: %{public}@"
+ "Handle new assertion for auto asset: %{public}@"
+ "Interest in auto asset: %{public}@ submitted, now lock the auto asset to download the content"
+ "LinguisticAssetType is not provided in the query: %@"
+ "LinguisticAssetType is provided in the query does not support auto asset: %@"
+ "Lock auto asset: %@"
+ "Locking auto asset for query: %{public}@"
+ "Register interest in auto assets for query: %{public}@"
+ "Supported linguistic asset types are not provided for asset type: %@"
+ "T@\"NSSet\",R,N,V_autoAssetTypes"
+ "T@\"NSString\",?,R,C"
+ "Unlocking auto asset: %{public}@"
+ "Update auto asset for query: %{public}@"
+ "Updated cache for query: %{public}@ assets: %{public}@ was cached: %d, cachedOnly: %d"
+ "Updated the assets for asset type: %@"
+ "User info in callback: %@"
+ "_autoAssetTypes"
+ "addEntriesFromDictionary:"
+ "addLinguisticAssetType:"
+ "allSupportedLinguisticAssetTypeForAssetType:"
+ "assetsAvailableOnDeviceForQuery:"
+ "assetsForQuery:"
+ "autoAssetForAssetSelector:"
+ "autoAssetQueryForAssertion:"
+ "autoAssetSelectorsForQuery:"
+ "autoAssetTypeForAsserType:"
+ "autoAssetTypes"
+ "autoAssetsForQuery:"
+ "availableForUseAttributes"
+ "com.apple.DataDeliveryServices.DDSAutoAssetManager"
+ "createAutoAssetAssertionForExistingAssertions"
+ "currentStatusSync:"
+ "data-delivery-service"
+ "dds-add-assertion-lock"
+ "dds-asset-download-ui-determine-if-available"
+ "dds-asset-download-ui-lock"
+ "dds-asset-for-query"
+ "dds-auto-asset-interest"
+ "dds-periodic-update-lock"
+ "determineIfAvailable:withTimeout:completion:"
+ "eliminateAllForSelector failed for auto asset selector: %@"
+ "eliminateAllForSelector successful for asset selector: %@"
+ "eliminateAllForSelector:completion:"
+ "eliminateInterestForAutoAsset:"
+ "endLockUsage:completion:"
+ "fetchAssetUpdateStatusDateForAutoAsset:"
+ "fetchCatalogBasedAssetUpdateStatusForAssertion:callback:"
+ "fetchUpdateStatusForAutoAsset:completion:"
+ "fil"
+ "initWithQueue:provider:trialManager:autoAssetManager:createXPCInterface:"
+ "interestInContent failed for auto asset: %@"
+ "interestInContent successful for asset selector: %@"
+ "interestInContent:completion:"
+ "interestInContentForAutoAsset:completion:"
+ "isAutoAssetType:"
+ "lockAssetsForQuery:"
+ "lockAutoAsset:forReason:withTimeout:completion:"
+ "lockAutoAssetSync:forReason:error:"
+ "lockContentSync completed for auto asset: %@ with error: %@"
+ "lockContentSync failed for auto asset: %@ with error: %@"
+ "lockContentSync:withTimeout:lockedAssetSelector:newerInProgress:error:"
+ "modifyAssetUpdateStatusForAssertion:status:"
+ "newerVersionAttributes"
+ "newerVersionDiscovered"
+ "notifications"
+ "notifyRegistrationName:forAssetType:"
+ "q32@0:8@16q24"
+ "registerInterestInContentForQuery:"
+ "setFetchAssetUpdateStatusDateForAutoAsset:"
+ "tl"
+ "unlockAutoAsset:forReason:"
+ "unregisterInterestInContentForAssetSelector:"
+ "updateAutoAsset:forReason:completion:"
+ "updateAutoAssetForAssetType:"
+ "updateCatalogBasedAssetForAssertion:callback:"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@\"DDSAssetQuery\"16"
+ "v24@0:8@\"DDSMAAutoAssetSelector\"16"
+ "v24@0:8@\"MAAutoAssetSelector\"16"
+ "v24@?0@\"MAAutoAssetSelector\"8@\"NSError\"16"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
+ "v24@?0q8@\"NSError\"16"
+ "v32@0:8@\"MAAutoAsset\"16@\"NSString\"24"
+ "v32@0:8@\"MAAutoAsset\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"MAAutoAsset\"16@?<v@?B@\"NSError\">24"
+ "v32@?0@\"MAAutoAssetSelector\"8@\"NSDictionary\"16@\"NSError\"24"
+ "v40@0:8@\"MAAutoAsset\"16@\"NSString\"24@?<v@?@\"NSURL\"@\"NSError\">32"
+ "v48@0:8@\"MAAutoAsset\"16@\"NSString\"24q32@?<v@?@\"NSURL\"@\"NSError\">40"
+ "v48@0:8@16@24q32@?40"
+ "visionOS"
- "\x17"
- "!"
- "@\"MAAutoAsset\"32@0:8@\"DDSMAAutoAssetSelector\"16@\"NSString\"24"
- "@48@0:8@16@24@32@?40"
- "Auto asset bundle is downloaded with assetSelector: %{public}@"
- "Auto asset is already downloaded for query: %{public}@"
- "Auto asset object cannot be created for query: %{public}@"
- "Download auto asset bundles for existing assertions"
- "Download auto asset content for client: %{public}@ and query: %{public}@"
- "DownloadEmptyAutoAssetBundles"
- "Empty auto asset download is not supported for asset type: %@"
- "Empty auto asset download is supported only if query contains single locale, but it contains: %@"
- "Skip downloading auto asset for client: %{public}@ and query: %{public}@"
- "Unexpected error while getting status of auto asset for query: %{public}@"
- "autoAssetForAssetSelector:clientID:"
- "com.apple.TextInput"
- "downloadAssetForQuery:clientID:"
- "downloadAutoAssetForAssertions:"
- "errorForDDSAssetDownloadUIErrorCode:"
- "initWithQueue:provider:trialManager:createXPCInterface:"
- "isEqualToNumber:"
- "lockAutoAsset:callback:"
- "lockContent is failed for assetType: %{public}@ assetSpecifier: %{public}@ with error: %{public}@"
- "setLockInhibitsEmergencyRemoval:"
- "shouldDownloadAutoAssetForClient:"
- "v28@?0@\"MAAutoAssetSelector\"8B16@\"NSError\"20"
- "v32@0:8@\"DDSAssetQuery\"16@\"NSString\"24"
- "v32@0:8@\"MAAutoAsset\"16@?<v@?@\"MAAutoAssetSelector\"B@\"NSError\">24"

```
