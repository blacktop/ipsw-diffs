## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3500.96.1.0.0
-  __TEXT.__text: 0x6fb38
+3500.99.1.0.0
+  __TEXT.__text: 0x6fb14
   __TEXT.__auth_stubs: 0xbf0
   __TEXT.__objc_methlist: 0x34b8
   __TEXT.__const: 0x110
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__gcc_except_tab: 0x14ac
+  __TEXT.__gcc_except_tab: 0x14a8
   __TEXT.__cstring: 0xab86
   __TEXT.__oslogstring: 0xd2de
   __TEXT.__unwind_info: 0x1250

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 2BAB2E0D-C863-30CD-BC9C-85C141484DB8
+  UUID: 011AFEE0-A3D2-35A8-9705-419095969626
   Functions: 1442
   Symbols:   5305
   CStrings:  4290
Symbols:
+ ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.323
+ ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.358
+ ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.359
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.445
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.446
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.456
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.457
+ ___27-[UAFXPCService runUpdates]_block_invoke.372
+ ___27-[UAFXPCService runUpdates]_block_invoke.373
+ ___29+[UAFUserManager removeUser:]_block_invoke.285
+ ___31-[UAFXPCConnection _connection]_block_invoke.288
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.295
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.297
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.301
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.302
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.303
+ ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke.307
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.404
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.406
+ ___40-[UAFXPCConnection expireSubscriptions:]_block_invoke.296
+ ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.389
+ ___42-[UAFXPCConnection diagnosticInformation:]_block_invoke.291
+ ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.346
+ ___45-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke.333
+ ___45-[UAFAutoAssetSet mapAsset:queue:completion:]_block_invoke.331
+ ___46-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke.325
+ ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke.289
+ ___48-[UAFAssetUtilities _assistantPreferencesUpdate]_block_invoke.338
+ ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.406
+ ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.408
+ ___49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke.294
+ ___50-[UAFAutoAssetSet invalidateWithQueue:completion:]_block_invoke.311
+ ___51-[UAFXPCConnection operationWithConfig:completion:]_block_invoke.290
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.338
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.339
+ ___53-[UAFAssetUtilities _downloadSiriAssetsOverCellular:]_block_invoke.328
+ ___53-[UAFXPCService lockLatestAtomicInstance:completion:]_block_invoke.417
+ ___56-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke.293
+ ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.414
+ ___61-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke.297
+ ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke.314
+ ___63-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke.310
+ ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.307
+ ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke.329
+ ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.403
+ ___70-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke.295
+ ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke.297
+ ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke_2.298
+ ___75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke.309
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.314
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.325
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.327
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke_2.328
+ ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke.297
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.398
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.399
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.400
+ ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.421
+ ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.401
+ ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.430
+ ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.458
+ ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.316
+ ____RegisterPeriodicUAFSubscriptionActivity_block_invoke.312
+ ____RegisterXPCActivity_block_invoke.301
+ ___block_literal_global.286
+ ___block_literal_global.300
+ ___block_literal_global.302
+ ___block_literal_global.304
+ ___block_literal_global.306
+ ___block_literal_global.316
+ ___block_literal_global.318
+ ___block_literal_global.320
+ ___block_literal_global.325
+ ___block_literal_global.327
+ ___block_literal_global.334
+ ___block_literal_global.364
+ ___block_literal_global.382
+ ___block_literal_global.386
+ ___block_literal_global.394
+ ___block_literal_global.402
+ ___block_literal_global.406
+ ___block_literal_global.410
- ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.326
- ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.361
- ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.362
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.448
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.449
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.459
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.460
- ___27-[UAFXPCService runUpdates]_block_invoke.376
- ___27-[UAFXPCService runUpdates]_block_invoke.378
- ___29+[UAFUserManager removeUser:]_block_invoke.288
- ___31-[UAFXPCConnection _connection]_block_invoke.291
- ___36+[UAFUserManager performUserCleanup]_block_invoke.298
- ___36+[UAFUserManager performUserCleanup]_block_invoke.300
- ___36+[UAFUserManager performUserCleanup]_block_invoke.304
- ___36+[UAFUserManager performUserCleanup]_block_invoke.305
- ___36+[UAFUserManager performUserCleanup]_block_invoke.306
- ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke.310
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.407
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.409
- ___40-[UAFXPCConnection expireSubscriptions:]_block_invoke.299
- ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.392
- ___42-[UAFXPCConnection diagnosticInformation:]_block_invoke.294
- ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.349
- ___45-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke.336
- ___45-[UAFAutoAssetSet mapAsset:queue:completion:]_block_invoke.334
- ___46-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke.328
- ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke.292
- ___48-[UAFAssetUtilities _assistantPreferencesUpdate]_block_invoke.341
- ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.409
- ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.411
- ___49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke.297
- ___50-[UAFAutoAssetSet invalidateWithQueue:completion:]_block_invoke.314
- ___51-[UAFXPCConnection operationWithConfig:completion:]_block_invoke.293
- ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.341
- ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.342
- ___53-[UAFAssetUtilities _downloadSiriAssetsOverCellular:]_block_invoke.331
- ___53-[UAFXPCService lockLatestAtomicInstance:completion:]_block_invoke.420
- ___56-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke.296
- ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.417
- ___61-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke.300
- ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke.317
- ___63-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke.313
- ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.310
- ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke.332
- ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.406
- ___70-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke.298
- ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke.300
- ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke_2.301
- ___75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke.312
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.317
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.328
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.330
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke_2.331
- ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke.300
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.401
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.402
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.403
- ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.424
- ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.404
- ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.433
- ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.461
- ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.319
- ____RegisterPeriodicUAFSubscriptionActivity_block_invoke.315
- ____RegisterXPCActivity_block_invoke.304
- ___block_literal_global.289
- ___block_literal_global.303
- ___block_literal_global.305
- ___block_literal_global.312
- ___block_literal_global.313
- ___block_literal_global.319
- ___block_literal_global.324
- ___block_literal_global.326
- ___block_literal_global.328
- ___block_literal_global.333
- ___block_literal_global.337
- ___block_literal_global.370
- ___block_literal_global.385
- ___block_literal_global.389
- ___block_literal_global.397
- ___block_literal_global.405
- ___block_literal_global.409
- ___block_literal_global.416
Functions:
~ -[UAFSubscriptionStoreManager getAllSubscriptions:] : 312 -> 272
~ +[UAFAssetSetManager configureAssetDelivery:configurationManager:lockIfUnchanged:oldSubscriptions:newSubscriptions:userInitiated:] : 612 -> 616

```
