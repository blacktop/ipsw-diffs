## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3500.87.2.0.0
-  __TEXT.__text: 0x6f600
-  __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_methlist: 0x3498
+3500.92.1.0.0
+  __TEXT.__text: 0x6f984
+  __TEXT.__auth_stubs: 0xbf0
+  __TEXT.__objc_methlist: 0x34a8
   __TEXT.__const: 0x110
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__gcc_except_tab: 0x144c
-  __TEXT.__cstring: 0xab36
-  __TEXT.__oslogstring: 0xd208
-  __TEXT.__unwind_info: 0x11d0
+  __TEXT.__gcc_except_tab: 0x14ac
+  __TEXT.__cstring: 0xab76
+  __TEXT.__oslogstring: 0xd294
+  __TEXT.__unwind_info: 0x11f0
   __TEXT.__objc_classname: 0x45d
   __TEXT.__objc_methname: 0x9a82
   __TEXT.__objc_methtype: 0x1091

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0x5f8
-  __AUTH_CONST.__const: 0x5a0
+  __AUTH_CONST.__auth_got: 0x608
+  __AUTH_CONST.__const: 0x5c0
   __AUTH_CONST.__cfstring: 0x4600
   __AUTH_CONST.__objc_const: 0x4270
   __AUTH_CONST.__objc_intobj: 0xa8

   __DATA.__data: 0x238
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0xc30
-  __DATA_DIRTY.__bss: 0x2c0
+  __DATA_DIRTY.__bss: 0x2d0
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 54F62409-AE5D-3B11-B6C4-E14C844FE823
-  Functions: 1437
-  Symbols:   5285
-  CStrings:  4281
+  UUID: 428FF6DA-6D3D-3BE0-B2D8-F45C2EAFF684
+  Functions: 1442
+  Symbols:   5301
+  CStrings:  4285
 
Symbols:
+ +[UAFInstrumentationProvider getSerialQueue]
+ GCC_except_table39
+ GCC_except_table74
+ GCC_except_table86
+ ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.317
+ ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.361
+ ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.362
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.449
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.450
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.460
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.461
+ ___27-[UAFXPCService runUpdates]_block_invoke.376
+ ___27-[UAFXPCService runUpdates]_block_invoke.378
+ ___29+[UAFUserManager removeUser:]_block_invoke.288
+ ___31-[UAFXPCConnection _connection]_block_invoke.291
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.298
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.300
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.304
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.305
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.306
+ ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke.310
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.408
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.410
+ ___40-[UAFXPCConnection expireSubscriptions:]_block_invoke.299
+ ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.393
+ ___42-[UAFXPCConnection diagnosticInformation:]_block_invoke.294
+ ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.340
+ ___44+[UAFInstrumentationProvider getSerialQueue]_block_invoke
+ ___45-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke.336
+ ___45-[UAFAutoAssetSet mapAsset:queue:completion:]_block_invoke.334
+ ___46-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke.328
+ ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke.292
+ ___48-[UAFAssetUtilities _assistantPreferencesUpdate]_block_invoke.341
+ ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.409
+ ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.411
+ ___49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke.297
+ ___50-[UAFAutoAssetSet invalidateWithQueue:completion:]_block_invoke.314
+ ___51-[UAFXPCConnection operationWithConfig:completion:]_block_invoke.293
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.341
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.342
+ ___53-[UAFAssetUtilities _downloadSiriAssetsOverCellular:]_block_invoke.331
+ ___53-[UAFXPCService lockLatestAtomicInstance:completion:]_block_invoke.420
+ ___56-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke.296
+ ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.418
+ ___61-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke.300
+ ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke.317
+ ___63-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke.313
+ ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.310
+ ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke.332
+ ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.409
+ ___70-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke.298
+ ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke.300
+ ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke_2.301
+ ___74+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:fallbackAlter:]_block_invoke.377
+ ___75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke.312
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.317
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.328
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.330
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke_2.331
+ ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke.300
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.404
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.405
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.406
+ ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.427
+ ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.407
+ ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.434
+ ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.462
+ ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.310
+ ____RegisterPeriodicUAFSubscriptionActivity_block_invoke.315
+ ____RegisterXPCActivity_block_invoke.304
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_literal_global.289
+ ___block_literal_global.301
+ ___block_literal_global.303
+ ___block_literal_global.305
+ ___block_literal_global.307
+ ___block_literal_global.312
+ ___block_literal_global.313
+ ___block_literal_global.319
+ ___block_literal_global.324
+ ___block_literal_global.326
+ ___block_literal_global.328
+ ___block_literal_global.333
+ ___block_literal_global.337
+ ___block_literal_global.370
+ ___block_literal_global.385
+ ___block_literal_global.389
+ ___block_literal_global.400
+ ___block_literal_global.406
+ ___block_literal_global.412
+ ___block_literal_global.414
+ ___block_literal_global.417
+ _os_transaction_get_description
+ _os_transaction_get_timestamp
- GCC_except_table73
- GCC_except_table85
- ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.314
- ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.358
- ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.359
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.444
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.445
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.455
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.456
- ___27-[UAFXPCService runUpdates]_block_invoke.372
- ___27-[UAFXPCService runUpdates]_block_invoke.373
- ___29+[UAFUserManager removeUser:]_block_invoke.285
- ___31-[UAFXPCConnection _connection]_block_invoke.288
- ___36+[UAFUserManager performUserCleanup]_block_invoke.295
- ___36+[UAFUserManager performUserCleanup]_block_invoke.297
- ___36+[UAFUserManager performUserCleanup]_block_invoke.301
- ___36+[UAFUserManager performUserCleanup]_block_invoke.302
- ___36+[UAFUserManager performUserCleanup]_block_invoke.303
- ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke.307
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.405
- ___40-[UAFXPCConnection expireSubscriptions:]_block_invoke.296
- ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.390
- ___42-[UAFXPCConnection diagnosticInformation:]_block_invoke.291
- ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.337
- ___45-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke.333
- ___45-[UAFAutoAssetSet mapAsset:queue:completion:]_block_invoke.331
- ___46-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke.325
- ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke.289
- ___48-[UAFAssetUtilities _assistantPreferencesUpdate]_block_invoke.338
- ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.406
- ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.408
- ___49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke.294
- ___50-[UAFAutoAssetSet invalidateWithQueue:completion:]_block_invoke.311
- ___51-[UAFXPCConnection operationWithConfig:completion:]_block_invoke.290
- ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.338
- ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.339
- ___53-[UAFAssetUtilities _downloadSiriAssetsOverCellular:]_block_invoke.328
- ___53-[UAFXPCService lockLatestAtomicInstance:completion:]_block_invoke.417
- ___56-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke.293
- ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.412
- ___61-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke.297
- ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke.314
- ___63-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke.310
- ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.307
- ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke.329
- ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.406
- ___70-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke.295
- ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke.297
- ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke_2.298
- ___74+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:fallbackAlter:]_block_invoke.374
- ___75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke.309
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.314
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.325
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.327
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke_2.328
- ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke.297
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.401
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.402
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.403
- ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.424
- ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.404
- ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.428
- ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.457
- ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.307
- ____RegisterPeriodicUAFSubscriptionActivity_block_invoke.312
- ____RegisterXPCActivity_block_invoke.301
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- ___block_literal_global.286
- ___block_literal_global.298
- ___block_literal_global.300
- ___block_literal_global.302
- ___block_literal_global.304
- ___block_literal_global.306
- ___block_literal_global.310
- ___block_literal_global.316
- ___block_literal_global.318
- ___block_literal_global.320
- ___block_literal_global.325
- ___block_literal_global.327
- ___block_literal_global.334
- ___block_literal_global.364
- ___block_literal_global.382
- ___block_literal_global.386
- ___block_literal_global.397
- ___block_literal_global.403
- ___block_literal_global.408
- ___block_literal_global.409
- ___block_literal_global.411
CStrings:
+ "%s Completing transaction %s from %llu to lock latest for asset set %@"
+ "%s Creating transaction %s from %llu to lock latest for asset set %@"
+ "UAFInstrumentationProvider.Serial"
+ "com.apple.siri.uaf.locklatest"

```
