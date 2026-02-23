## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3520.49.1.0.0
-  __TEXT.__text: 0x82744
+3520.53.1.0.0
+  __TEXT.__text: 0x83aa0
   __TEXT.__auth_stubs: 0x1140
-  __TEXT.__objc_methlist: 0x3918
-  __TEXT.__const: 0x1c0
+  __TEXT.__objc_methlist: 0x3968
+  __TEXT.__const: 0x1c8
   __TEXT.__dlopen_cstrs: 0x296
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x67
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_fieldmd: 0x1c
-  __TEXT.__cstring: 0xb9a0
-  __TEXT.__oslogstring: 0xec85
+  __TEXT.__cstring: 0xba7e
+  __TEXT.__oslogstring: 0xf0e9
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x1694
-  __TEXT.__unwind_info: 0x1570
+  __TEXT.__gcc_except_tab: 0x16c4
+  __TEXT.__unwind_info: 0x1590
   __TEXT.__objc_classname: 0x50e
-  __TEXT.__objc_methname: 0xaa47
-  __TEXT.__objc_methtype: 0x1115
-  __TEXT.__objc_stubs: 0x8760
+  __TEXT.__objc_methname: 0xaba1
+  __TEXT.__objc_methtype: 0x116a
+  __TEXT.__objc_stubs: 0x88a0
   __DATA_CONST.__got: 0x588
-  __DATA_CONST.__const: 0x1e58
+  __DATA_CONST.__const: 0x1ea0
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2860
+  __DATA_CONST.__objc_selrefs: 0x28a8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x130
   __AUTH_CONST.__auth_got: 0x8b0
-  __AUTH_CONST.__const: 0x648
-  __AUTH_CONST.__cfstring: 0x4c20
-  __AUTH_CONST.__objc_const: 0x4928
+  __AUTH_CONST.__const: 0x6c8
+  __AUTH_CONST.__cfstring: 0x4d00
+  __AUTH_CONST.__objc_const: 0x4958
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x408
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x370
+  __DATA.__objc_ivar: 0x374
   __DATA.__data: 0x290
   __DATA.__bss: 0x48
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xca8
-  __DATA_DIRTY.__bss: 0x2f0
+  __DATA_DIRTY.__bss: 0x310
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0D86A331-E43C-3F1A-8679-232F95B5AFC2
-  Functions: 1582
-  Symbols:   5766
-  CStrings:  4685
+  UUID: 5CE4A078-1809-39AF-BE9A-62E84FEB8538
+  Functions: 1596
+  Symbols:   5812
+  CStrings:  4731
 
Symbols:
+ +[UAFAssetSetManager _subscriptionDiffersFromDB:subscriber:user:expirationOnlyCount:error:]
+ +[UAFAssetSetManager isSubscriptionExpirationIgnorable:subscriber:user:]
+ +[UAFAutoAssetManager removeDeprecatedAutoAssetSets]
+ +[UAFBiomeInstrumenter _createBiomeAssetSet:withAssets:sourceType:]
+ +[UAFBiomeInstrumenter logAlterFromAtomicInstance:sourceType:addedAssets:removedAssets:]
+ +[UAFCommonUtilities setUAFPopulation:url:assetSet:]
+ +[UAFCommonUtilities setUAFPopulationForAssetType:forType:withURL:]
+ +[UAFCommonUtilities validatePopulation:resolvedPopulation:isNamedString:isDefault:]
+ +[UAFInstrumentationProvider logAlterFromAtomicInstance:sourceType:alterSetData:]
+ -[UAFAssetSetManager removeDeprecatedAssetSets]
+ -[UAFAssetSetSubscription isEqualWithoutExpiration:]
+ -[UAFConfigurationManager getAllAssetSetsWithDeprecated:]
+ -[UAFConfigurationManager getAllDeprecatedAssetSets]
+ -[UAFConfigurationManager getAssetSetNoCache:deprecated:]
+ -[UAFInstrumentationAlterSetData setSourceType:]
+ -[UAFInstrumentationAlterSetData sourceType]
+ GCC_except_table108
+ GCC_except_table131
+ GCC_except_table75
+ GCC_except_table79
+ GCC_except_table92
+ _OBJC_IVAR_$_UAFInstrumentationAlterSetData._sourceType
+ ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.375
+ ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.409
+ ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.410
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.505
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.506
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.516
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.517
+ ___27-[UAFXPCService runUpdates]_block_invoke.416
+ ___27-[UAFXPCService runUpdates]_block_invoke.419
+ ___29+[UAFUserManager removeUser:]_block_invoke.341
+ ___31-[UAFXPCConnection _connection]_block_invoke.338
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.350
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.352
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.356
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.357
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.358
+ ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke.357
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.463
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.465
+ ___40-[UAFXPCConnection expireSubscriptions:]_block_invoke.346
+ ___41-[UAFXPCService _updateShadowSiriLocale:]_block_invoke.477
+ ___42-[UAFXPCConnection diagnosticInformation:]_block_invoke.341
+ ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.399
+ ___45-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke.384
+ ___45-[UAFAutoAssetSet mapAsset:queue:completion:]_block_invoke.382
+ ___46-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke.376
+ ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke.340
+ ___48-[UAFAssetUtilities _assistantPreferencesUpdate]_block_invoke.389
+ ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.451
+ ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.453
+ ___49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke.344
+ ___50-[UAFAutoAssetSet invalidateWithQueue:completion:]_block_invoke.362
+ ___51-[UAFXPCConnection operationWithConfig:completion:]_block_invoke.340
+ ___52+[UAFAutoAssetManager removeDeprecatedAutoAssetSets]_block_invoke
+ ___52+[UAFAutoAssetManager removeDeprecatedAutoAssetSets]_block_invoke.491
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.389
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.390
+ ___53-[UAFAssetUtilities _downloadSiriAssetsOverCellular:]_block_invoke.379
+ ___57+[UAFAutoAssetManager lockLatestAssetSet:atomicInstance:]_block_invoke.449
+ ___57+[UAFUserManager updateLastSeenForUser:queue:completion:]_block_invoke.337
+ ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.473
+ ___61-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke.347
+ ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke.365
+ ___63-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke.361
+ ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.358
+ ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke.380
+ ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.466
+ ___68-[UAFXPCService lockLatestAtomicInstance:atomicInstance:completion:]_block_invoke.462
+ ___70-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke.345
+ ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke.348
+ ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke_2.349
+ ___71-[UAFXPCConnection lockLatestAtomicInstance:atomicInstance:completion:]_block_invoke.343
+ ___72+[UAFAssetSetManager isSubscriptionExpirationIgnorable:subscriber:user:]_block_invoke
+ ___75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke.359
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.365
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.376
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.378
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke_2.379
+ ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke.348
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.451
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.458
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.459
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.460
+ ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.484
+ ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.461
+ ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.486
+ ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.518
+ ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.366
+ ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.370
+ ____RegisterPeriodicUAFSubscriptionActivity_block_invoke.367
+ ____RegisterXPCActivity_block_invoke.348
+ ___block_descriptor_32_e41_v32?0"UAFAssetSetConfiguration"8Q16^B24l
+ ___block_descriptor_56_e8_32s40s48r_e40_v32?0"UAFAssetSetSubscription"8Q16^B24ls32l8s40l8r48l8
+ ___block_literal_global.337
+ ___block_literal_global.350
+ ___block_literal_global.352
+ ___block_literal_global.354
+ ___block_literal_global.356
+ ___block_literal_global.357
+ ___block_literal_global.358
+ ___block_literal_global.366
+ ___block_literal_global.368
+ ___block_literal_global.371
+ ___block_literal_global.373
+ ___block_literal_global.375
+ ___block_literal_global.385
+ ___block_literal_global.388
+ ___block_literal_global.416
+ ___block_literal_global.418
+ ___block_literal_global.421
+ ___block_literal_global.429
+ ___block_literal_global.447
+ ___block_literal_global.462
+ ___block_literal_global.469
+ ___block_literal_global.472
+ ___block_literal_global.490
+ ___block_literal_global.494
+ ___block_literal_global.534
+ ___block_literal_global.537
+ ___kUAFDeprecatedPopulationStrings_block_invoke
+ ___kUAFValidPopulationStrings_block_invoke
+ _objc_msgSend$_createBiomeAssetSet:withAssets:sourceType:
+ _objc_msgSend$_subscriptionDiffersFromDB:subscriber:user:expirationOnlyCount:error:
+ _objc_msgSend$getAllAssetSetsWithDeprecated:
+ _objc_msgSend$getAllDeprecatedAssetSets
+ _objc_msgSend$getAssetSetNoCache:deprecated:
+ _objc_msgSend$isEqualWithoutExpiration:
+ _objc_msgSend$isSubscriptionExpirationIgnorable:subscriber:user:
+ _objc_msgSend$logAlterFromAtomicInstance:sourceType:addedAssets:removedAssets:
+ _objc_msgSend$logAlterFromAtomicInstance:sourceType:alterSetData:
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$removeDeprecatedAssetSets
+ _objc_msgSend$removeDeprecatedAutoAssetSets
+ _objc_msgSend$setSourceType:
+ _objc_msgSend$setUAFPopulation:url:
+ _objc_msgSend$setUAFPopulation:url:assetSet:
+ _objc_msgSend$setUAFPopulationForAssetType:forType:withURL:
+ _objc_msgSend$sourceType
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$validatePopulation:resolvedPopulation:isNamedString:isDefault:
- +[UAFAssetSetManager _subscriptionDiffersFromDB:subscriber:user:error:]
- +[UAFBiomeInstrumenter _createBiomeAssetSet:withAssets:]
- +[UAFBiomeInstrumenter logAlterSetFromPSUSAtomicInstance:addedAssets:removedAssets:]
- +[UAFCommonUtilities _getInternalBaseConfigDir]
- +[UAFCommonUtilities _getInternalConfigFilePath]
- +[UAFCommonUtilities _getPopulationMapping:toAudience:toServer:]
- +[UAFCommonUtilities _setUAFPopulation:forAssetTypes:url:]
- +[UAFInstrumentationProvider logAlterSetFromPSUSAtomicInstance:alterSetData:]
- GCC_except_table105
- GCC_except_table128
- GCC_except_table76
- GCC_except_table77
- GCC_except_table89
- GCC_except_table91
- ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.335
- ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.370
- ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.371
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.460
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.461
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.471
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.472
- ___27-[UAFXPCService runUpdates]_block_invoke.377
- ___27-[UAFXPCService runUpdates]_block_invoke.380
- ___29+[UAFUserManager removeUser:]_block_invoke.302
- ___31-[UAFXPCConnection _connection]_block_invoke.299
- ___36+[UAFUserManager performUserCleanup]_block_invoke.311
- ___36+[UAFUserManager performUserCleanup]_block_invoke.313
- ___36+[UAFUserManager performUserCleanup]_block_invoke.317
- ___36+[UAFUserManager performUserCleanup]_block_invoke.318
- ___36+[UAFUserManager performUserCleanup]_block_invoke.319
- ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke.318
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.424
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.426
- ___40-[UAFXPCConnection expireSubscriptions:]_block_invoke.307
- ___41-[UAFXPCService _updateShadowSiriLocale:]_block_invoke.435
- ___42-[UAFXPCConnection diagnosticInformation:]_block_invoke.302
- ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.359
- ___45-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke.345
- ___45-[UAFAutoAssetSet mapAsset:queue:completion:]_block_invoke.343
- ___46-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke.337
- ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke.301
- ___48-[UAFAssetUtilities _assistantPreferencesUpdate]_block_invoke.350
- ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.409
- ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.411
- ___49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke.305
- ___50-[UAFAutoAssetSet invalidateWithQueue:completion:]_block_invoke.323
- ___51-[UAFXPCConnection operationWithConfig:completion:]_block_invoke.301
- ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.350
- ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.351
- ___53-[UAFAssetUtilities _downloadSiriAssetsOverCellular:]_block_invoke.340
- ___57+[UAFAutoAssetManager lockLatestAssetSet:atomicInstance:]_block_invoke.410
- ___57+[UAFUserManager updateLastSeenForUser:queue:completion:]_block_invoke.298
- ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.434
- ___61-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke.308
- ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke.326
- ___63-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke.322
- ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.319
- ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke.341
- ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.425
- ___68-[UAFXPCService lockLatestAtomicInstance:atomicInstance:completion:]_block_invoke.420
- ___70-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke.306
- ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke.309
- ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke_2.310
- ___71-[UAFXPCConnection lockLatestAtomicInstance:atomicInstance:completion:]_block_invoke.304
- ___75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke.320
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.326
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.337
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.339
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke_2.340
- ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke.309
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.411
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.418
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.419
- ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.443
- ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.420
- ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.447
- ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.473
- ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.327
- ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke_4
- ____RegisterPeriodicUAFSubscriptionActivity_block_invoke.328
- ____RegisterXPCActivity_block_invoke.309
- ___block_literal_global.298
- ___block_literal_global.311
- ___block_literal_global.313
- ___block_literal_global.315
- ___block_literal_global.317
- ___block_literal_global.318
- ___block_literal_global.319
- ___block_literal_global.327
- ___block_literal_global.329
- ___block_literal_global.332
- ___block_literal_global.334
- ___block_literal_global.336
- ___block_literal_global.346
- ___block_literal_global.349
- ___block_literal_global.377
- ___block_literal_global.379
- ___block_literal_global.382
- ___block_literal_global.405
- ___block_literal_global.407
- ___block_literal_global.409
- ___block_literal_global.423
- ___block_literal_global.428
- ___block_literal_global.430
- _objc_msgSend$_createBiomeAssetSet:withAssets:
- _objc_msgSend$_getInternalBaseConfigDir
- _objc_msgSend$_getInternalConfigFilePath
- _objc_msgSend$_getPopulationMapping:toAudience:toServer:
- _objc_msgSend$_setUAFPopulation:forAssetTypes:url:
- _objc_msgSend$_subscriptionDiffersFromDB:subscriber:user:error:
- _objc_msgSend$initWithString:
- _objc_msgSend$logAlterSetFromPSUSAtomicInstance:addedAssets:removedAssets:
- _objc_msgSend$logAlterSetFromPSUSAtomicInstance:alterSetData:
CStrings:
+ "%s Asset_Arrived, checking subscription completeness for %{public}@"
+ "%s Attempting force removing asset set %{public}@ after soft remove failure of: %{public}@"
+ "%s CNGuardrail asset arrived, routing to CoreAnalytics with %lu entries"
+ "%s Finished processing removal of deprecated asset sets"
+ "%s Invalid population when trying to set it %{public}@"
+ "%s Processing removal of deprecated asset sets"
+ "%s Removing deprecated asset set '%{public}@'"
+ "%s SiriAnalytics unavailable, aborting"
+ "%s Subscriptions differ only by expiration at less than expiration interval for subscriber: '%{public}@' and subscriptions '%{public}@' user: '%@'"
+ "%s Subscriptions for subscriber %{public}@ for user '%@' for changed by expiration only, skipping configure and updating db"
+ "%s Unexpectedly couldn't retrieve subscription user '%@' subscriber '%{public}@' subscription: '%{public}@': %{public}@"
+ "%s assetSet=%{public}@ eventType=%lu entryCount=%lu"
+ "%s assetSet=%{public}@ source=%{public}@ addedCount=%lu removedCount=%lu"
+ "%s computed assetSetIdentifiers=%{public}@ specifierCount=%lu"
+ "%s emitted for assetSet=%{public}@"
+ "%s emitted for assetSet=%{public}@ source=%{public}@"
+ "%s emitting SADImmediateDownloadTriggered convertedLocale=%{public}@"
+ "%s languageCode=%{public}@ hasExistingAssets=%d retryCount=%u"
+ "%s logAlterFromAtomicInstance: Biome unavailable for %{public}@, aborting"
+ "%s logAlterFromAtomicInstance: assetSet=%{public}@ subscription=%{public}@ addedCount=%lu removedCount=%lu"
+ "%s logAlterFromAtomicInstance: nil assetSetName for %{public}@, aborting"
+ "%s logAlterFromAtomicInstance: sending Biome event for %{public}@ assetSet=%{public}@"
+ "%s logAssetSetDownloadEvent: Biome unavailable, aborting"
+ "%s logAssetSetDownloadEvent: assetSet=%{public}@ eventType=%lu entryCount=%lu errorCount=%lu"
+ "%s logAssetSetDownloadEvent: sending Biome event for assetSet=%{public}@"
+ "%s logScheduledDailyAssetStatus: Biome unavailable, aborting"
+ "%s logScheduledDailyAssetStatus: sending Biome event"
+ "%s logScheduledDailyAssetStatus: starting"
+ "%s no assetSetSubscription provided, skipping usages"
+ "%s routing to logAssetSetDownloadEvent for assetSet=%{public}@ eventType=%lu"
+ "%s routing to logScheduledDailyAssetStatus (eventType=Scheduled)"
+ "%s sent to AIR"
+ "%s subscriber=%{public}@ user=%{public}@ subscriptionCount=%lu"
+ "%s subscription=%{public}@ complete, emitting for assetSets=%{public}@"
+ "%s subscription=%{public}@ incomplete, skipping"
+ "%s subscription=%{public}@ subscriber=%{public}@ userId=%u locale=%{public}@ mode=%ld unsubscribed=%d"
+ "+[UAFAssetSetManager _subscriptionDiffersFromDB:subscriber:user:expirationOnlyCount:error:]"
+ "+[UAFAssetSetManager isSubscriptionExpirationIgnorable:subscriber:user:]_block_invoke"
+ "+[UAFAutoAssetManager removeDeprecatedAutoAssetSets]_block_invoke"
+ "+[UAFBiomeInstrumenter _createBiomeAssetSet:withAssets:sourceType:]"
+ "+[UAFBiomeInstrumenter logAlterFromAtomicInstance:sourceType:addedAssets:removedAssets:]"
+ "+[UAFCommonUtilities setUAFPopulationForAssetType:forType:withURL:]"
+ "+[UAFInstrumentationProvider logAlterFromAtomicInstance:sourceType:alterSetData:]"
+ "-[UAFConfigurationManager getAllAssetSetsWithDeprecated:]"
+ "-[UAFConfigurationManager getAssetSetNoCache:deprecated:]"
+ "@40@0:8@16@24Q32"
+ "@56@0:8@16@24@32^q40^@48"
+ "B48@0:8@16^@24^B32^B40"
+ "FactoryAlteredAssetSet"
+ "PSUS"
+ "TQ,N,V_sourceType"
+ "_createBiomeAssetSet:withAssets:sourceType:"
+ "_sourceType"
+ "_subscriptionDiffersFromDB:subscriber:user:expirationOnlyCount:error:"
+ "carry"
+ "com.apple.Settings.AppleIntelligence"
+ "could not determine user for uid %u"
+ "customer"
+ "default"
+ "external-pre-release"
+ "getAllAssetSetsWithDeprecated:"
+ "getAllDeprecatedAssetSets"
+ "getAssetSetNoCache:deprecated:"
+ "gp"
+ "isEqualWithoutExpiration:"
+ "isSubscriptionExpirationIgnorable:subscriber:user:"
+ "livable"
+ "logAlterFromAtomicInstance:sourceType:addedAssets:removedAssets:"
+ "logAlterFromAtomicInstance:sourceType:alterSetData:"
+ "lowercaseString"
+ "model-catalog"
+ "removeDeprecatedAssetSets"
+ "removeDeprecatedAutoAssetSets"
+ "seed-staging"
+ "setSourceType:"
+ "setUAFPopulation:url:assetSet:"
+ "setUAFPopulationForAssetType:forType:withURL:"
+ "sourceType"
+ "timeIntervalSinceDate:"
+ "uat"
+ "untested"
+ "v32@?0@\"UAFAssetSetConfiguration\"8Q16^B24"
+ "v48@0:8@16Q24@32@40"
+ "validatePopulation:resolvedPopulation:isNamedString:isDefault:"
- "%s #settings Emitting SADSchemaSADImmediateDownloadTriggered event: language=%{public}@ hasExistingAssets=%u retryCount=%d"
- "%s %{public}@ is not a valid population"
- "%s Can't log %{public}@ as this system doesn't support Biome."
- "%s Can't log asset set download event as this system doesn't support Biome."
- "%s Can't log daily asset status as this system doesn't support Biome."
- "%s Can't log download trigger event with language as this system doesn't support SiriAnalytics."
- "%s Cannot log %{public}@ with nil asset set name"
- "%s Emitted DailyStatusEvent message for asset set: %{public}@"
- "%s Emitted alter set from PSUS event for asset set: %{public}@"
- "%s Failed to load %@ %@"
- "%s Invalid Pallas override URL: %{public}@ population: %{public}@"
- "%s Invalid Pallas server URL: %{public}@ population: %{public}@"
- "%s Logging alter set from PSUS for asset set: %{public}@"
- "%s Sent Siri subscription state to AIR"
- "%s Setting nil default for Pallas server URL for population %{public}@"
- "%s Skipping setUAFPopulation due to nil AssetTypes"
- "%s Using Biome for logging asset status"
- "%s Using Biome to send %{public}@ for asset set: %{public}@ with %lu removed specifiers and %lu added specifiers"
- "%s Using Biome to send asset set event for :%{public}@"
- "%s Using Biome to send scheduled daily status event"
- "%s Writing Siri subscription state to AIR for user: %u. SubscriptionStatus: %{public}@"
- "+[UAFAssetSetManager _subscriptionDiffersFromDB:subscriber:user:error:]"
- "+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke_4"
- "+[UAFBiomeInstrumenter _createBiomeAssetSet:withAssets:]"
- "+[UAFBiomeInstrumenter logAlterSetFromPSUSAtomicInstance:addedAssets:removedAssets:]"
- "+[UAFCommonUtilities _getPopulationMapping:toAudience:toServer:]"
- "+[UAFCommonUtilities _setUAFPopulation:forAssetTypes:url:]"
- "+[UAFInstrumentationProvider logAlterSetFromPSUSAtomicInstance:alterSetData:]"
- "-[UAFConfigurationManager getAllAssetSets]"
- "/Pallas/pallas_internal.plist"
- "0c88076f-c292-4dad-95e7-304db9d29d34"
- "Audience"
- "Subscribed"
- "URL"
- "Unsubscribed"
- "_createBiomeAssetSet:withAssets:"
- "_getInternalBaseConfigDir"
- "_getInternalConfigFilePath"
- "_getPopulationMapping:toAudience:toServer:"
- "_setUAFPopulation:forAssetTypes:url:"
- "_subscriptionDiffersFromDB:subscriber:user:error:"
- "initWithString:"
- "logAlterSetFromPSUSAtomicInstance:addedAssets:removedAssets:"
- "logAlterSetFromPSUSAtomicInstance:alterSetData:"
- "prod"

```
