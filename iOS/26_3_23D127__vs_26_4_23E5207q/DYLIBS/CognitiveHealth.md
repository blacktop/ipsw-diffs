## CognitiveHealth

> `/System/Library/PrivateFrameworks/CognitiveHealth.framework/CognitiveHealth`

```diff

 26.0.0.0.0
-  __TEXT.__text: 0x3ec8
-  __TEXT.__auth_stubs: 0x420
+  __TEXT.__text: 0x4098
+  __TEXT.__auth_stubs: 0x3b0
   __TEXT.__objc_methlist: 0x3f8
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0xf0
+  __TEXT.__gcc_except_tab: 0xec
   __TEXT.__oslogstring: 0x240
   __TEXT.__cstring: 0xa91
-  __TEXT.__unwind_info: 0x190
+  __TEXT.__unwind_info: 0x198
   __TEXT.__objc_classname: 0x13d
   __TEXT.__objc_methname: 0xf83
   __TEXT.__objc_methtype: 0x29f

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x220
+  __AUTH_CONST.__auth_got: 0x1e8
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0x880
   __AUTH_CONST.__objc_const: 0xb80

   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5EAD0DE6-979D-3B0E-83D4-C903348505E1
+  UUID: BB8445E9-1F28-31E4-B6DF-91B14C0C6A21
   Functions: 96
-  Symbols:   537
+  Symbols:   530
   CStrings:  355
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ -[CHXPCClientHelper synchronousRemoteObjectProxyWithErrorHandler:] : 116 -> 120
~ -[CHXPCClientHelper remoteObjectProxyWithErrorHandler:] : 116 -> 120
~ -[CHXPCClientHelper _locked_establishConnection] : 540 -> 544
~ ___48-[CHXPCClientHelper _locked_establishConnection]_block_invoke : 204 -> 208
~ ___48-[CHXPCClientHelper _locked_establishConnection]_block_invoke.7 : 232 -> 236
~ -[CHXPCClientHelper initWithServiceName:whitelistedServerInterface:clientExportedObject:interruptionHandler:invalidationHandler:] : 280 -> 252
~ -[CHIntegrationTestClient populateSampleAppLaunchEmbeddingWithCompletion:] : 252 -> 256
~ ___74-[CHIntegrationTestClient populateSampleAppLaunchEmbeddingWithCompletion:]_block_invoke : 228 -> 236
~ -[CHIntegrationTestClient init] : 272 -> 276
~ ___31-[CHIntegrationTestClient init]_block_invoke.10 : 172 -> 176
~ ___31-[CHIntegrationTestClient init]_block_invoke : 172 -> 176
~ _ch_xpc_handle : 84 -> 100
~ _ch_sensor_data_handle : 84 -> 100
~ _ch_test_handle : 84 -> 100
~ ___60-[CHSensorDataClient embeddingVectorForBundleId:completion:]_block_invoke : 232 -> 240
~ -[CHSensorDataClient aggregatedMotionAndAppLaunchDataFromDate:toDate:completion:] : 300 -> 296
~ ___81-[CHSensorDataClient aggregatedMotionAndAppLaunchDataFromDate:toDate:completion:]_block_invoke : 232 -> 240
~ -[CHSensorDataClient init] : 472 -> 476
~ ___26-[CHSensorDataClient init]_block_invoke.25 : 172 -> 176
~ ___26-[CHSensorDataClient init]_block_invoke : 172 -> 176
~ -[CHIntegrationTest populateSampleAppLaunchEmbeddingWithCompletion:] : 140 -> 144
~ -[CHSensorData aggregatedMotionAndAppLaunchDataFromDate:toDate:completion:] : 188 -> 184
~ -[CHMobileAssetBridge autoAssetEndAllLocksForAssetType:assetSpecifier:completion:] : 256 -> 244
~ ___82-[CHMobileAssetBridge autoAssetEndAllLocksForAssetType:assetSpecifier:completion:]_block_invoke : 164 -> 160
~ -[CHMobileAssetBridge autoAssetEndLockContentForAssetType:assetSpecifier:endLockReason:completion:] : 368 -> 352
~ ___99-[CHMobileAssetBridge autoAssetEndLockContentForAssetType:assetSpecifier:endLockReason:completion:]_block_invoke : 164 -> 160
~ -[CHMobileAssetBridge autoAssetLockContentForAssetType:assetSpecifier:lockReason:completion:] : 404 -> 392
~ ___93-[CHMobileAssetBridge autoAssetLockContentForAssetType:assetSpecifier:lockReason:completion:]_block_invoke : 908 -> 948
~ -[CHMobileAssetBridge autoAssetInterestInContentForAssetType:assetSpecifier:completion:] : 344 -> 332
~ ___88-[CHMobileAssetBridge autoAssetInterestInContentForAssetType:assetSpecifier:completion:]_block_invoke : 164 -> 160
~ -[CHMobileAssetBridge autoAssetAvailableForUseForAssetType:assetSpecifier:completion:] : 340 -> 324
~ ___86-[CHMobileAssetBridge autoAssetAvailableForUseForAssetType:assetSpecifier:completion:]_block_invoke : 224 -> 232
~ -[CHAppLaunchSensorData description] : 192 -> 200
~ -[CHAppLaunchSensorData initWithCoder:] : 628 -> 652
~ -[CHAppLaunchSensorData encodeWithCoder:] : 168 -> 176
~ -[CHAppLaunchSensorData initWithBundleId:embeddingVector:modelVersion:algorithmType:trainingDate:] : 256 -> 236
~ -[CHCustomCategories setIntToUUIDMapping:] : 12 -> 64
~ -[CHCustomCategories setPersistentContainer:] : 12 -> 64
~ -[CHCustomCategories setCoreDataController:] : 12 -> 64
~ -[CHCustomCategories setFetchError:] : 12 -> 64
~ -[CHCustomCategories resetTimer] : 196 -> 200
~ ___72-[CHCustomCategories lockAssetAndReturnAssetPathForFile:withLockReason:]_block_invoke : 160 -> 168
~ -[CHCustomCategories loadMappingFromFile] : 548 -> 572
~ -[CHCustomCategories extractDataFromCoreDataResult:] : 360 -> 372
~ -[CHCustomCategories fetchCategoriesForBundleId:] : 360 -> 368
~ -[CHCustomCategories categoryForBundleId:] : 112 -> 132
~ -[CHCustomCategories categoriesForBundleIdSet:completion:] : 364 -> 368
~ -[CHCustomCategories categoriesForBundleId:completion:] : 128 -> 132
~ -[CHCustomCategories customCategoryVersion] : 240 -> 248
~ -[CHCustomCategories init] : 176 -> 188
~ +[CHCustomCategories downloadDatabaseAssetIfNeededWithCompletion:] : 184 -> 180
~ ___66+[CHCustomCategories downloadDatabaseAssetIfNeededWithCompletion:]_block_invoke : 100 -> 112
~ +[CHCustomCategories databaseAssetAvailableStatusWithCompletion:] : 184 -> 180
~ ___65+[CHCustomCategories databaseAssetAvailableStatusWithCompletion:]_block_invoke : 112 -> 120
~ -[CHCoreDataController addPersistentStoreFromDatabase] : 736 -> 760
~ ___54-[CHCoreDataController addPersistentStoreFromDatabase]_block_invoke : 160 -> 168
~ -[CHCoreDataController persistentContainer] : 288 -> 308
~ ___43-[CHCoreDataController persistentContainer]_block_invoke : 128 -> 140

```
