## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/Versions/A/UnifiedAssetFramework`

```diff

-3402.65.1.14.1
-  __TEXT.__text: 0x6d330
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_methlist: 0x30f0
+3404.60.2.0.0
+  __TEXT.__text: 0x73c04
+  __TEXT.__auth_stubs: 0x980
+  __TEXT.__objc_methlist: 0x34f8
   __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0x10f4
-  __TEXT.__cstring: 0x95de
-  __TEXT.__oslogstring: 0xb08c
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__unwind_info: 0x10a8
-  __TEXT.__objc_classname: 0x411
-  __TEXT.__objc_methname: 0x9922
-  __TEXT.__objc_methtype: 0xeae
-  __TEXT.__objc_stubs: 0x7bc0
-  __DATA_CONST.__got: 0x4d0
-  __DATA_CONST.__const: 0x7f8
-  __DATA_CONST.__objc_classlist: 0x158
+  __TEXT.__gcc_except_tab: 0x13a4
+  __TEXT.__cstring: 0x9f14
+  __TEXT.__oslogstring: 0xbf32
+  __TEXT.__unwind_info: 0x1138
+  __TEXT.__objc_classname: 0x424
+  __TEXT.__objc_methname: 0x9ff6
+  __TEXT.__objc_methtype: 0xfe4
+  __TEXT.__objc_stubs: 0x81e0
+  __DATA_CONST.__got: 0x4d8
+  __DATA_CONST.__const: 0x850
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24f0
+  __DATA_CONST.__objc_selrefs: 0x2720
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x498
-  __AUTH_CONST.__const: 0x1a70
-  __AUTH_CONST.__cfstring: 0x3e60
-  __AUTH_CONST.__objc_const: 0x44d0
+  __DATA_CONST.__objc_arraydata: 0x108
+  __AUTH_CONST.__auth_got: 0x4d0
+  __AUTH_CONST.__const: 0x1b30
+  __AUTH_CONST.__cfstring: 0x40e0
+  __AUTH_CONST.__objc_const: 0x42d0
   __AUTH_CONST.__objc_intobj: 0x240
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0xd70
-  __DATA.__objc_ivar: 0x338
+  __AUTH.__objc_data: 0xdc0
+  __DATA.__objc_ivar: 0x34c
   __DATA.__data: 0x230
-  __DATA.__bss: 0x308
+  __DATA.__bss: 0x318
   __DATA.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 7A99113F-41CB-3145-B94A-A406FC93B108
-  Functions: 1412
-  Symbols:   3714
-  CStrings:  3947
+  UUID: 24E21A14-9163-3C69-AF97-06C9B114EFD6
+  Functions: 1468
+  Symbols:   3852
+  CStrings:  4145
 
Symbols:
+ +[UAFAutoAssetManager atomicInstanceFromLockPath:]
+ +[UAFAutoAssetManager backgroundNeedPolicy]
+ +[UAFAutoAssetManager configureAssetSet:specifiers:changed:downloaded:currentPolicy:]
+ +[UAFAutoAssetManager currentLockURLForAssetSet:]
+ +[UAFAutoAssetManager defaultCheckPolicy]
+ +[UAFAutoAssetManager fileLockPolicy]
+ +[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:]
+ +[UAFAutoAssetManager getSpecifiers:assetSetUsages:experiment:]
+ +[UAFAutoAssetManager immediateNeedPolicy]
+ +[UAFAutoAssetManager latestAtomicInstanceForClients:]
+ +[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]
+ +[UAFAutoAssetManager releaseIncompatibleAssetSet:specifiers:configuration:]
+ +[UAFAutoAssetManager setBackgroundNeedPolicy:configuration:]
+ +[UAFAutoAssetManager shouldCheckAssetSet:autoAssetSet:changed:downloaded:experiment:locked:userInitiated:removalNeeded:]
+ +[UAFAutoAssetManager stageAssetSet:targets:]
+ +[UAFAutoAssetSet autoAssetSetStatus:]
+ +[UAFCommonUtilities _setUAFPopulation:forAssetTypes:url:]
+ +[UAFCommonUtilities copyBootSessionUUID]
+ +[UAFCommonUtilities setUAFPopulation:url:]
+ +[UAFConfigurationManager getDeprecatedUsageAliasNameFromPath:]
+ +[UAFExpiredAssets assetsExpired:error:]
+ +[UAFExpiredAssets expiredTokens:]
+ +[UAFExpiredAssets loadToken:error:]
+ +[UAFExpiredAssets markAssetsExpired:error:]
+ +[UAFExpiredAssets removeToken:]
+ +[UAFExpiredAssets tokenDir:]
+ +[UAFExpiredAssets tokenFilename:]
+ +[UAFManagedSubscriptions _assistantUsageAliasForMode:]
+ +[UAFManagedSubscriptions manageGMSSiriLanguageSubscription:language:mode:]
+ +[UAFXPCService _currentAssistantMode:]
+ -[UAFAssetSet assetSetIdForSELF:stagedDuringSU:]
+ -[UAFAssetSetConsistencyToken bootUUIDError]
+ -[UAFAssetSetConsistencyToken bootUUID]
+ -[UAFAssetSetConsistencyToken exlock:]
+ -[UAFAssetSetConsistencyToken hasIdenticalAssets:]
+ -[UAFAssetSetConsistencyToken hasIdenticalAssets:includeBootUUID:]
+ -[UAFAssetSetConsistencyToken initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:bootUUID:]
+ -[UAFAssetSetConsistencyToken isBootUUIDCurrent]
+ -[UAFAssetSetConsistencyToken jsonDictionary]
+ -[UAFAssetSetConsistencyToken nolock:]
+ -[UAFAssetSetConsistencyToken processIdIsLockingToken:statBuffer:error:]
+ -[UAFAssetSetConsistencyToken processIdsLockingToken:]
+ -[UAFAssetSetConsistencyToken rapidLock]
+ -[UAFAssetSetConsistencyToken refCount]
+ -[UAFAssetSetConsistencyToken setRefCount:]
+ -[UAFAssetSetConsistencyToken unlockableTokenError]
+ -[UAFAssetSetExperiment jsonDictionary]
+ -[UAFAssetSetManager assetSetUsagesForSubscribers:storeManager:configurationManager:anyUnknown:]
+ -[UAFAssetSetManager diskSpaceNeededForSubscribers:error:]
+ -[UAFAssetSetManager diskSpaceNeededForSubscribers:storeManager:configurationManager:error:]
+ -[UAFAssetSetManager downloadStatusForSubscribers:]
+ -[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]
+ -[UAFAssetSetManager markAssetsExpired:completion:]
+ -[UAFAssetSetManager observeAssetSet:policies:queue:handler:]
+ -[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:detailedProgress:completion:]
+ -[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]
+ -[UAFAssetSetObserver initWithAssetSet:ignoreMobileAssetStartup:configurationDirURLs:queue:updateHandler:]
+ -[UAFAssetSetProgress updateFinished:]
+ -[UAFConfigurationManager getUsageAlias:includeDeprecatedValues:]
+ -[UAFSubscriptionStoreManager _dropTable:]
+ -[UAFSubscriptionStoreManager _openDatabaseFile:existed:]
+ -[UAFSubscriptionStoreManager _prepareStatements]
+ -[UAFTrialUpdateProgress updateFinished:]
+ -[UAFUsageAliasConfiguration addDeprecatedValues:]
+ -[UAFXPCConnection markAssetsExpired:completion:]
+ -[UAFXPCService markAssetsExpired:completion:]
+ GCC_except_table19
+ GCC_except_table29
+ GCC_except_table39
+ GCC_except_table41
+ GCC_except_table48
+ GCC_except_table50
+ GCC_except_table55
+ GCC_except_table63
+ GCC_except_table79
+ GCC_except_table83
+ GCC_except_table86
+ OBJC_IVAR_$_UAFAssetSetConsistencyToken._bootUUID
+ OBJC_IVAR_$_UAFAssetSetConsistencyToken._isBootUUIDCurrent
+ OBJC_IVAR_$_UAFAssetSetConsistencyToken._rapidLock
+ OBJC_IVAR_$_UAFAssetSetConsistencyToken._refCount
+ OBJC_IVAR_$_UAFAssetUtilitiesService._completionWatchdogInProgress
+ _OBJC_CLASS_$_MAAutoAssetSetRapidLock
+ _OBJC_CLASS_$_UAFExpiredAssets
+ _OBJC_METACLASS_$_UAFExpiredAssets
+ __106-[UAFAssetSetObserver initWithAssetSet:ignoreMobileAssetStartup:configurationDirURLs:queue:updateHandler:]_block_invoke.305
+ __129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.457
+ __129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.468
+ __129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.471
+ __135-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke.338
+ __135-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke.342
+ __135-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke.347
+ __135-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_2.343
+ __135-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_2.348
+ __188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke.319
+ __27-[UAFXPCService runUpdates]_block_invoke.341
+ __37-[UAFXPCConnection checkAssetStatus:]_block_invoke.317
+ __39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.400
+ __42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.383
+ __43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.364
+ __45-[UAFAutoAssetSet mapAsset:queue:completion:]_block_invoke.336
+ __49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke.299
+ __50-[UAFAutoAssetSet invalidateWithQueue:completion:]_block_invoke.315
+ __53+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke.381
+ __58-[UAFXPCConnection subscriptionsForSubscriber:completion:]_block_invoke.302
+ __60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke.362
+ __63+[UAFAssetSetManager subscribe:subscriptions:queue:completion:]_block_invoke.305
+ __65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.304
+ __65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.306
+ __65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.307
+ __68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.424
+ __75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke.321
+ __88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.450
+ __90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.429
+ __94+[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke.315
+ __94+[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke.325
+ __96+[UAFAssetSetManager unsubscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke.327
+ __97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.477
+ __OBJC_$_CLASS_METHODS_UAFExpiredAssets
+ __OBJC_CLASS_RO_$_UAFExpiredAssets
+ __OBJC_METACLASS_RO_$_UAFExpiredAssets
+ ___103+[UAFAutoAssetManager stageAssetsWithSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:]_block_invoke
+ ___106-[UAFAssetSetObserver initWithAssetSet:ignoreMobileAssetStartup:configurationDirURLs:queue:updateHandler:]_block_invoke
+ ___106-[UAFAssetSetObserver initWithAssetSet:ignoreMobileAssetStartup:configurationDirURLs:queue:updateHandler:]_block_invoke_2
+ ___135-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke
+ ___135-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_2
+ ___135-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_3
+ ___38-[UAFAssetSetProgress updateFinished:]_block_invoke
+ ___41+[UAFCommonUtilities copyBootSessionUUID]_block_invoke
+ ___41-[UAFTrialUpdateProgress updateFinished:]_block_invoke
+ ___49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke
+ ___49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke_2
+ ___51-[UAFAssetSetManager markAssetsExpired:completion:]_block_invoke
+ ___52+[UAFInstrumentationProvider logSubscriptionsStatus]_block_invoke
+ ___58-[UAFXPCConnection subscriptionsForSubscriber:completion:]_block_invoke_2
+ ___63+[UAFAutoAssetManager getSpecifiers:assetSetUsages:experiment:]_block_invoke
+ ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke_2
+ ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke
+ ___76+[UAFAutoAssetManager releaseIncompatibleAssetSet:specifiers:configuration:]_block_invoke
+ ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40r_e25_v32?0"NSString"8Q16^B24l
+ ___block_descriptor_48_e8_32s40r_e41_v32?0"NSString"8"NSMutableArray"16^B24l
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40s48r_e25_v32?0"NSString"8Q16^B24l
+ ___block_descriptor_56_e8_32s40s48s_e25_v32?0"NSString"8Q16^B24l
+ ___block_descriptor_64_e8_32s40bs48r_e8_v16?0Q8l
+ ___copy_helper_block_e8_32s40b48r
+ ___getAFSiriCapabilitiesServiceClientClass_block_invoke
+ __block_literal_global.299
+ __block_literal_global.301
+ __block_literal_global.309
+ __block_literal_global.311
+ __block_literal_global.316
+ __block_literal_global.370
+ __block_literal_global.398
+ __block_literal_global.405
+ __block_literal_global.417
+ __block_literal_global.435
+ _fcntl
+ _kUAFAutoAssetDiscretionaryReason
+ _kUAFCacheDir
+ _kUAFDeprecatedConfigurationDir
+ _kUAFDeprecatedSeparator
+ _kUAFExpiredAssetsDir
+ _kUAFObservePolicyIgnoreMobileAssetStartup
+ _kUAFTokenExtension
+ _malloc_type_calloc
+ _malloc_type_malloc
+ _objc_msgSend$URLForDirectory:inDomain:appropriateForURL:create:error:
+ _objc_msgSend$_assistantUsageAliasForMode:
+ _objc_msgSend$_currentAssistantMode:
+ _objc_msgSend$_openDatabaseFile:existed:
+ _objc_msgSend$_prepareStatements
+ _objc_msgSend$_setUAFPopulation:forAssetTypes:url:
+ _objc_msgSend$acquireShortTermLockSync
+ _objc_msgSend$addDeprecatedValues:
+ _objc_msgSend$assetSetIdForSELF:stagedDuringSU:
+ _objc_msgSend$assetSetUsagesForSubscribers:storeManager:configurationManager:anyUnknown:
+ _objc_msgSend$assetsExpired:error:
+ _objc_msgSend$atomicInstanceFromLockPath:
+ _objc_msgSend$autoAssetSetStatus:
+ _objc_msgSend$backgroundNeedPolicy
+ _objc_msgSend$bootUUID
+ _objc_msgSend$bootUUIDError
+ _objc_msgSend$configureAssetSet:specifiers:changed:downloaded:currentPolicy:
+ _objc_msgSend$consistencyToken
+ _objc_msgSend$copyBootSessionUUID
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$currentLockURLForAssetSet:
+ _objc_msgSend$defaultCheckPolicy
+ _objc_msgSend$destinationOfSymbolicLinkAtPath:error:
+ _objc_msgSend$diskSpaceNeededForSubscribers:storeManager:configurationManager:error:
+ _objc_msgSend$downloadStatusForSubscribers:
+ _objc_msgSend$downloadStatusForSubscribers:queue:completion:
+ _objc_msgSend$endShortTermLockSync
+ _objc_msgSend$expiredTokens:
+ _objc_msgSend$fileLockPolicy
+ _objc_msgSend$fromPreSoftwareUpdateStaging
+ _objc_msgSend$getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:
+ _objc_msgSend$getDeprecatedUsageAliasNameFromPath:
+ _objc_msgSend$getSpecifiers:assetSetUsages:experiment:
+ _objc_msgSend$getUsageAlias:includeDeprecatedValues:
+ _objc_msgSend$hasIdenticalAssets:
+ _objc_msgSend$hasIdenticalAssets:includeBootUUID:
+ _objc_msgSend$immediateNeedPolicy
+ _objc_msgSend$init:assetSetIdentifier:assetSetAtomicInstance:
+ _objc_msgSend$initWithAssetSet:ignoreMobileAssetStartup:configurationDirURLs:queue:updateHandler:
+ _objc_msgSend$initWithUTF8String:
+ _objc_msgSend$initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:bootUUID:
+ _objc_msgSend$isBootUUIDCurrent
+ _objc_msgSend$jsonDictionary
+ _objc_msgSend$latestAtomicInstanceForClients:
+ _objc_msgSend$latestDownloadedAtomicInstanceFromPreSUStaging
+ _objc_msgSend$loadToken:error:
+ _objc_msgSend$manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:
+ _objc_msgSend$manageGMSSiriLanguageSubscription:language:mode:
+ _objc_msgSend$markAssetsExpired:completion:
+ _objc_msgSend$markAssetsExpired:error:
+ _objc_msgSend$new
+ _objc_msgSend$observeAssetSet:policies:queue:handler:
+ _objc_msgSend$processIdIsLockingToken:statBuffer:error:
+ _objc_msgSend$releaseIncompatibleAssetSet:specifiers:configuration:
+ _objc_msgSend$removeToken:
+ _objc_msgSend$setAtomicInstance:
+ _objc_msgSend$setBackgroundNeedPolicy:configuration:
+ _objc_msgSend$setFromPreSoftwareUpdateStaging:
+ _objc_msgSend$shouldCheckAssetSet:autoAssetSet:changed:downloaded:experiment:locked:userInitiated:removalNeeded:
+ _objc_msgSend$shouldDownloadAssetsForSiriSystemAssistantExperienceSync
+ _objc_msgSend$stageAssetSet:targets:
+ _objc_msgSend$tokenDir:
+ _objc_msgSend$tokenFilename:
+ _objc_msgSend$unlockableTokenError
+ _objc_msgSend$updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:
+ _objc_msgSend$userInitiated
+ _objc_msgSend$vendingAtomicInstanceForConfiguredEntries
+ _objc_msgSend$writeToURL:options:error:
+ _proc_listpidspath
+ _proc_pidfdinfo
+ _proc_pidinfo
+ _sysctlbyname
+ getAFSiriCapabilitiesServiceClientClass.softClass
- +[UAFAssetSetManager updateAssets:policies:queue:progress:completion:]
- +[UAFAssetSetManager updateAssets:policies:queue:progress:completion:storeManager:configurationManager:]
- +[UAFAssetSetManager updateAssets:subscription:policies:queue:progress:completion:]
- +[UAFAssetSetManager updateAssets:subscription:policies:queue:progress:completion:storeManager:configurationManager:]
- +[UAFAssetSetManager updateAssets:subscription:policies:queue:progressWithStatus:completion:]
- +[UAFAutoAssetManager configureAssetSet:specifiers:changed:]
- +[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:]
- +[UAFAutoAssetManager getSpecifiers:assetSetUsages:]
- +[UAFAutoAssetManager getSpecifiers:assetSetUsages:disableExperimentation:]
- +[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:]
- +[UAFAutoAssetManager shouldCheckAssetSet:autoAssetSet:changed:locked:]
- +[UAFAutoAssetManager stageAssetSet:targets:autoAssetSet:]
- +[UAFAutoAssetSet catalogAssetSetID:]
- +[UAFCommonUtilities _setUAFPopulation:forAssetTypes:]
- +[UAFManagedSubscriptions manageGMSSiriLanguageSubscription:language:]
- -[UAFAssetSet assetSetIdForSELF:]
- -[UAFAssetSetConsistencyToken setLocked:]
- -[UAFAssetSetManager assetSetUsagesForStatusForSubscriber:subscriptionName:status:]
- -[UAFAssetSetManager diskSpaceNeededForSubscriber:subscriptionName:storeManager:configurationManager:error:]
- -[UAFConfigurationManager getUsageAlias:]
- -[UAFTrialUpdateProgress updateFinished]
- GCC_except_table36
- GCC_except_table38
- GCC_except_table42
- GCC_except_table45
- GCC_except_table58
- GCC_except_table71
- GCC_except_table77
- _XPC_ACTIVITY_PRIORITY_MAINTENANCE
- __126+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:userInitiated:]_block_invoke.433
- __129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.444
- __129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.445
- __129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.455
- __151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke.338
- __151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke.342
- __151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke.347
- __151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_2.343
- __151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_2.348
- __27-[UAFXPCService runUpdates]_block_invoke.335
- __37-[UAFXPCConnection checkAssetStatus:]_block_invoke.314
- __39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.401
- __42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.384
- __43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.363
- __45-[UAFAutoAssetSet mapAsset:queue:completion:]_block_invoke.328
- __50-[UAFAutoAssetSet invalidateWithQueue:completion:]_block_invoke.308
- __53+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke.382
- __58-[UAFXPCConnection subscriptionsForSubscriber:completion:]_block_invoke.299
- __60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke.363
- __63+[UAFAssetSetManager subscribe:subscriptions:queue:completion:]_block_invoke.299
- __65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.303
- __75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke.318
- __79+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:]_block_invoke.422
- __81-[UAFAssetSetObserver initWithAssetSet:configurationDirURLs:queue:updateHandler:]_block_invoke.305
- __84-[UAFAssetSetManager downloadStatusForSubscriber:subscriptionName:queue:completion:]_block_invoke.416
- __88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.442
- __94+[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke.312
- __94+[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke.316
- __96+[UAFAssetSetManager unsubscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke.324
- __97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.464
- ___117+[UAFAssetSetManager updateAssets:subscription:policies:queue:progress:completion:storeManager:configurationManager:]_block_invoke
- ___151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke
- ___151-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_2
- ___40-[UAFTrialUpdateProgress updateFinished]_block_invoke
- ___75+[UAFAutoAssetManager getSpecifiers:assetSetUsages:disableExperimentation:]_block_invoke
- ___79+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:]_block_invoke
- ___81-[UAFAssetSetObserver initWithAssetSet:configurationDirURLs:queue:updateHandler:]_block_invoke
- ___81-[UAFAssetSetObserver initWithAssetSet:configurationDirURLs:queue:updateHandler:]_block_invoke_2
- ___83+[UAFAssetSetManager updateAssets:subscription:policies:queue:progress:completion:]_block_invoke
- ___84-[UAFAssetSetManager downloadStatusForSubscriber:subscriptionName:queue:completion:]_block_invoke
- ___93+[UAFAssetSetManager updateAssets:subscription:policies:queue:progressWithStatus:completion:]_block_invoke
- ___block_descriptor_40_e8_32bs_e11_v24?0d8Q16l
- ___block_descriptor_48_e8_32s40r_e35_v32?0"NSString"8"NSString"16^B24l
- ___block_descriptor_72_e8_32s40s48bs56r_e8_v16?0Q8l
- ___getAFDeviceSupportsSAESymbolLoc_block_invoke
- __block_literal_global.289
- __block_literal_global.293
- __block_literal_global.306
- __block_literal_global.308
- __block_literal_global.310
- __block_literal_global.399
- __block_literal_global.406
- __block_literal_global.409
- __block_literal_global.426
- _objc_msgSend$_setUAFPopulation:forAssetTypes:
- _objc_msgSend$assetSetIdForSELF:
- _objc_msgSend$assetSetUsagesForStatusForSubscriber:subscriptionName:status:
- _objc_msgSend$catalogAssetSetID:
- _objc_msgSend$checkResourceIsReachableAndReturnError:
- _objc_msgSend$configureAssetSet:specifiers:changed:
- _objc_msgSend$diskSpaceNeededForSubscriber:subscriptionName:storeManager:configurationManager:error:
- _objc_msgSend$getAutoAssetSet:specifiers:addEntries:configured:
- _objc_msgSend$getSpecifiers:assetSetUsages:
- _objc_msgSend$getSpecifiers:assetSetUsages:disableExperimentation:
- _objc_msgSend$getUsageAlias:
- _objc_msgSend$initFileURLWithPath:
- _objc_msgSend$initWithAssetSet:queue:updateHandler:
- _objc_msgSend$manageAssetSet:specifiers:lockIfUnchanged:userInitiated:
- _objc_msgSend$manageGMSSiriLanguageSubscription:language:
- _objc_msgSend$shouldCheckAssetSet:autoAssetSet:changed:locked:
- _objc_msgSend$stageAssetSet:targets:autoAssetSet:
- _objc_msgSend$updateAssets:subscription:policies:queue:progress:completion:storeManager:configurationManager:
- _objc_msgSend$updateFinished
- getAFDeviceSupportsSAESymbolLoc.ptr
CStrings:
+ "%s #settings Auto retry skipped due to need for inexpensive network"
+ "%s #settings Download API call"
+ "%s #settings Skipping due to one attempt already in progress"
+ "%s %{public}@: MA AutoAssetSet's downloadedCatalogCachedAssetSetID is nil for asset set - %{public}@"
+ "%s %{public}@: updateAssets for subscribers '%{public}@'"
+ "%s Asset set %{public}@ incompatible with current OS, removing"
+ "%s AssetSet Token: %{public}@: %{public}@"
+ "%s Attempting force remove of asset set '%{public}@'"
+ "%s Auto asset set %{public}@ has expected specifiers %{public}@ and is %{public}@"
+ "%s Auto asset set %{public}@ is configured, has atomic instance %{public}@, is available to clients, and current OS supported but current assets %{public}@ are marked as expired"
+ "%s Can't unlock %{public}@: already unlocked"
+ "%s Cannot add deprecated values from %{public}@ to %{public}@"
+ "%s Commit of exclusive transaction of tables creation failed"
+ "%s Could not get AFSiriCapabilitiesServiceClient class"
+ "%s Could not initialize a new AFSiriCapabilitiesClient"
+ "%s Could not parse atomic instance from '%{public}@': uuid: '%{public}@'"
+ "%s Could not prepare statements after database recreation"
+ "%s Could not rename %@ to %@: %{public}@"
+ "%s Could not set discretionary policy for asset set %{public}@ : %{public}@"
+ "%s Deprecated value %{public}@ already defined"
+ "%s Detected database corruption.  Deleting database and recreating: %d"
+ "%s Download status of assets for subscribers: %{public}@"
+ "%s Emitting asset set arrived daily status event for auto asset set %{public}@, pre-staged:%d"
+ "%s Emitting daily status scheduled event for asset set %{public}@, pre-staged: %d"
+ "%s Exlocked %{public}@"
+ "%s Expired Asset Set Token: %{public}@"
+ "%s Expired assets token from %{public}@ does match %{public}@: %{public}@"
+ "%s Expired assets token from %{public}@ does not match %{public}@: %{public}@"
+ "%s Failed fcntl %{public}@ to check nature of lock: %{public}@"
+ "%s Failed to add deprecated values from %{public}@"
+ "%s Failed to archive expired assets token %{public}@: %{public}@"
+ "%s Failed to create expired assets token dir %{public}@ for token %{public}@: %{public}@"
+ "%s Failed to get expired assets token dir for %{public}@: %{public}@"
+ "%s Failed to get expired assets token dir: %{public}@"
+ "%s Failed to lock %{public}@: %{public}@"
+ "%s Failed to open %{public}@ to check nature of lock: %{public}@"
+ "%s Failed to open %{public}@: %{public}@"
+ "%s Failed to read expired assets token from %{public}@: %{public}@"
+ "%s Failed to remove token at %{public}@: %{public}@"
+ "%s Failed to unarchive expired assets token from %{public}@: %{public}@"
+ "%s Failed to unlock %{public}@: %{public}@"
+ "%s Failed to write expired assets token %{public}@ to %{public}@: %{public}@"
+ "%s Force remove of asset set '%{public}@' failed: %@"
+ "%s Found pids %{public}@ locking %{public}@"
+ "%s Generating expired asset set tokens"
+ "%s Invalid Pallas override URL: %{public}@ population: %{public}@"
+ "%s Invalid Pallas server URL: %{public}@ population: %{public}@"
+ "%s Latest atomic instance for '%{public}@': %{public}@"
+ "%s Loading deprecated values to process subscription for usage alias %{public}@ with value %{public}@"
+ "%s Locked %{public}@"
+ "%s Marking token %{public}@ expired completed (error = %{public}@)"
+ "%s No destination for current lock for asset set '%{public}@' at path '%{public}@': %{public}@"
+ "%s Not actually locking %{public}@ and instead incrementing ref count to %lld"
+ "%s Not actually locking %{public}@ as there is no atomic instance but roots are present"
+ "%s Not actually unlocking %{public}@ and instead decrementing ref count to %lld"
+ "%s Not actually unlocking %{public}@ as there is no atomic instance"
+ "%s Not trying to load %@ as a deprecated usage alias configuration file as it for usage alias %{public}@, not %{public}@"
+ "%s Not trying to load %@ as a deprecated usage alias configuration file as it lacks the \"plist\" extension"
+ "%s Opened %{public}@"
+ "%s Reconfiguration of %{public}@ produced no autoAssetSet"
+ "%s Removal of incompatible asset set %{public}@ complete, reconfiguring"
+ "%s Returning asset download status: %lu for subscribers: %{public}@"
+ "%s Returning status: %lu for subscribers: %{public}@ as the asset set usages are nil"
+ "%s Rollback exclusive transaction of tables creation failed"
+ "%s Rolling back exclusive transaction of tables creation"
+ "%s SQL error while executing statement: '%{public}@': (%d) '%{public}s"
+ "%s Setting need policy for asset set '%{public}@' to not user initiated"
+ "%s Setting nil default for Pallas server URL for population %{public}@"
+ "%s Siri IE is now: wants assets: %d, language: %{public}@, mode: %{public}@"
+ "%s Siri configured for: language %{public}@, mode: %{public}@ (assistant enabled: %d, assistant language: %{public}@)"
+ "%s Unlocked %{public}@"
+ "%s UpdateTrialFactors complete"
+ "%s Wrote expired assets token %{public}@ to %{public}@"
+ "%s markAssetsExpired of %{public}@ complete"
+ "%s markAssetsExpired of %{public}@ failed with: %@"
+ "%s proc_listpidspath of %{public}@ failed: %{public}@"
+ "%s proc_pidinfo for pid %lld for file %{public}@ failed: %{public}@"
+ "%s stat of %{public}@ failed: %{public}@"
+ "'"
+ "+[UAFAutoAssetManager atomicInstanceFromLockPath:]"
+ "+[UAFAutoAssetManager configureAssetSet:specifiers:changed:downloaded:currentPolicy:]"
+ "+[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:]"
+ "+[UAFAutoAssetManager latestAtomicInstanceForClients:]"
+ "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]"
+ "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke"
+ "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke_2"
+ "+[UAFAutoAssetManager releaseIncompatibleAssetSet:specifiers:configuration:]"
+ "+[UAFAutoAssetManager releaseIncompatibleAssetSet:specifiers:configuration:]_block_invoke"
+ "+[UAFAutoAssetManager setBackgroundNeedPolicy:configuration:]"
+ "+[UAFAutoAssetManager shouldCheckAssetSet:autoAssetSet:changed:downloaded:experiment:locked:userInitiated:removalNeeded:]"
+ "+[UAFAutoAssetManager stageAssetSet:targets:]"
+ "+[UAFAutoAssetSet autoAssetSetStatus:]"
+ "+[UAFCommonUtilities _setUAFPopulation:forAssetTypes:url:]"
+ "+[UAFCommonUtilities deviceSupportAssistantEngine]"
+ "+[UAFExpiredAssets assetsExpired:error:]"
+ "+[UAFExpiredAssets expiredTokens:]"
+ "+[UAFExpiredAssets loadToken:error:]"
+ "+[UAFExpiredAssets markAssetsExpired:error:]"
+ "+[UAFExpiredAssets removeToken:]"
+ "+[UAFInstrumentationProvider _constructSelfAssetSet:storeManager:]"
+ "+[UAFInstrumentationProvider logSubscriptionsStatus]_block_invoke"
+ "-[UAFAssetSet assetSetIdForSELF:stagedDuringSU:]"
+ "-[UAFAssetSetConsistencyToken exlock:]"
+ "-[UAFAssetSetConsistencyToken nolock:]"
+ "-[UAFAssetSetConsistencyToken processIdIsLockingToken:statBuffer:error:]"
+ "-[UAFAssetSetConsistencyToken processIdsLockingToken:]"
+ "-[UAFAssetSetManager assetSetUsagesForSubscribers:storeManager:configurationManager:anyUnknown:]"
+ "-[UAFAssetSetManager diskSpaceNeededForSubscribers:storeManager:configurationManager:error:]"
+ "-[UAFAssetSetManager downloadStatusForSubscribers:]"
+ "-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]"
+ "-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke"
+ "-[UAFAssetSetManager markAssetsExpired:completion:]_block_invoke"
+ "-[UAFAssetSetManager observeAssetSet:policies:queue:handler:]"
+ "-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]"
+ "-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke"
+ "-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_3"
+ "-[UAFAssetSetObserver initWithAssetSet:ignoreMobileAssetStartup:configurationDirURLs:queue:updateHandler:]"
+ "-[UAFAssetSetObserver initWithAssetSet:ignoreMobileAssetStartup:configurationDirURLs:queue:updateHandler:]_block_invoke"
+ "-[UAFAssetSetObserver initWithAssetSet:ignoreMobileAssetStartup:configurationDirURLs:queue:updateHandler:]_block_invoke_2"
+ "-[UAFAssetUtilities _downloadSiriAssetsWithDelay:]"
+ "-[UAFAssetUtilities downloadSiriAssetsIfNeeded]"
+ "-[UAFAssetUtilities downloadSiriAssetsOverCellular]"
+ "-[UAFAssetUtilities downloadSiriAssets]"
+ "-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]"
+ "-[UAFConfigurationManager getUsageAlias:includeDeprecatedValues:]"
+ "-[UAFSubscriptionStoreManager _dropTable:]"
+ "-[UAFSubscriptionStoreManager _openDatabaseFile:existed:]"
+ "-[UAFSubscriptionStoreManager _prepareStatements]"
+ "-[UAFUsageAliasConfiguration addDeprecatedValues:]"
+ "-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke"
+ "-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke_2"
+ "-[UAFXPCConnection subscriptionsForSubscriber:completion:]_block_invoke_2"
+ ".corrupt"
+ ".deprecated"
+ "@\"MAAutoAssetSetRapidLock\""
+ "@28@0:8B16^B20"
+ "@32@0:8@16^B24"
+ "@48@0:8@16@24@32^B40"
+ "@48@0:8@16@24B32B36@40"
+ "@52@0:8@16B24@28@36@?44"
+ "@56@0:8@16@24^B32^B40^@48"
+ "@60@0:8@16@24B32^B36^B44^@52"
+ "@64@0:8@16@24@32@40@48@56"
+ "AFSiriCapabilitiesServiceClient"
+ "Asset Set Consistency Token %@ for assetSet %@ with atomic instance %@ (%@ with ref count %lld) experiment %@ preinstalledAssetsSummary %@ bootUUID %@ isBootUUIDCurrent %d"
+ "AssetSetTokens"
+ "B36@0:8i16^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}20^@28"
+ "B72@0:8@16@24B32B36@40^B48^B56^B64"
+ "DROP TABLE IF EXISTS %@"
+ "Deprecated"
+ "ExpiredAssetSetTokens"
+ "ExpiredAssets"
+ "IgnoreMobileAssetStartup"
+ "T@\"MAAutoAssetSetRapidLock\",R,N,V_rapidLock"
+ "T@\"NSString\",R,N,V_bootUUID"
+ "TB,R,N,V_isBootUUIDCurrent"
+ "TB,R,N,V_locked"
+ "The bootUUID doesn't match the current bootUUID"
+ "There are no underlying assets (neither atomic instance nor asset roots)"
+ "Ti,N,V_refCount"
+ "UAFExpiredAssets"
+ "URLForDirectory:inDomain:appropriateForURL:create:error:"
+ "Vv32@0:8@\"UAFAssetSetConsistencyToken\"16@?<v@?@\"NSError\">24"
+ "_assistantUsageAliasForMode:"
+ "_bootUUID"
+ "_completionWatchdogInProgress"
+ "_currentAssistantMode:"
+ "_dropTable:"
+ "_isBootUUIDCurrent"
+ "_openDatabaseFile:existed:"
+ "_prepareStatements"
+ "_rapidLock"
+ "_refCount"
+ "_setUAFPopulation:forAssetTypes:url:"
+ "acquireShortTermLockSync"
+ "addDeprecatedValues:"
+ "assetSetIdForSELF:stagedDuringSU:"
+ "assetSetUsagesForSubscribers:storeManager:configurationManager:anyUnknown:"
+ "assetsExpired:error:"
+ "atomicInstanceFromLockPath:"
+ "atomic_instance_"
+ "atomic_instance_latest.locker"
+ "autoAssetSetStatus:"
+ "backgroundNeedPolicy"
+ "bootUUID"
+ "bootUUIDError"
+ "configureAssetSet:specifiers:changed:downloaded:currentPolicy:"
+ "copyBootSessionUUID"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "currentLockURLForAssetSet:"
+ "defaultCheckPolicy"
+ "destinationOfSymbolicLinkAtPath:error:"
+ "discretionary"
+ "diskSpaceNeededForSubscribers:error:"
+ "diskSpaceNeededForSubscribers:storeManager:configurationManager:error:"
+ "downloadStatusForSubscribers:"
+ "downloadStatusForSubscribers:queue:completion:"
+ "downloaded"
+ "endShortTermLockSync"
+ "exlock:"
+ "expiredTokens:"
+ "fileLockPolicy"
+ "fromPreSoftwareUpdateStaging"
+ "getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:"
+ "getDeprecatedUsageAliasNameFromPath:"
+ "getSpecifiers:assetSetUsages:experiment:"
+ "getUsageAlias:includeDeprecatedValues:"
+ "hasIdenticalAssets:"
+ "hasIdenticalAssets:includeBootUUID:"
+ "immediateNeedPolicy"
+ "init:assetSetIdentifier:assetSetAtomicInstance:"
+ "initWithAssetSet:ignoreMobileAssetStartup:configurationDirURLs:queue:updateHandler:"
+ "initWithUTF8String:"
+ "initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:bootUUID:"
+ "isBootUUIDCurrent"
+ "jsonDictionary"
+ "kern.bootsessionuuid"
+ "latestAtomicInstanceForClients:"
+ "latestDownloadedAtomicInstanceFromPreSUStaging"
+ "loadToken:error:"
+ "manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:"
+ "manageGMSSiriLanguageSubscription:language:mode:"
+ "markAssetsExpired:completion:"
+ "markAssetsExpired:error:"
+ "new"
+ "nolock:"
+ "not downloaded"
+ "observeAssetSet:policies:queue:handler:"
+ "processIdIsLockingToken:statBuffer:error:"
+ "processIdsLockingToken:"
+ "q24@0:8^@16"
+ "rapidLock"
+ "refCount"
+ "releaseIncompatibleAssetSet:specifiers:configuration:"
+ "removeToken:"
+ "setBackgroundNeedPolicy:configuration:"
+ "setFromPreSoftwareUpdateStaging:"
+ "setRefCount:"
+ "setUAFPopulation:url:"
+ "shouldCheckAssetSet:autoAssetSet:changed:downloaded:experiment:locked:userInitiated:removalNeeded:"
+ "shouldDownloadAssetsForSiriSystemAssistantExperienceSync"
+ "stageAssetSet:targets:"
+ "tokenDir:"
+ "tokenFilename:"
+ "uaftoken"
+ "unlockableTokenError"
+ "updateAssetsForSubscribers:policies:queue:detailedProgress:completion:"
+ "updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:"
+ "userInitiated"
+ "v32@?0@\"NSString\"8@\"NSMutableArray\"16^B24"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "v36@0:8B16@20q28"
+ "v80@0:8@16@24@32@?40@?48@?56@64@72"
+ "vendingAtomicInstanceForConfiguredEntries"
+ "writeToURL:options:error:"
- "%@/%@"
- "%@: %@"
- "%s %{public}@: updateAssets for subscriber '%{public}@' with subscription '%{public}@'"
- "%s Auto asset set %{public}@ has expected specifiers %{public}@"
- "%s AutoAssetSet %{public}@ not provided, creating a new one for staging."
- "%s Can't unlock %@: already unlocked"
- "%s Could not create array from '%{public}@'"
- "%s Could not get auto asset type of auto asset set %{public}@: no config file found"
- "%s Downloading assets for subscriber: %{public}@ and subscription: %{public}@"
- "%s Emitting asset set arrived daily status event for auto asset set %{public}@:"
- "%s Experimentation not enabled for asset set %{public}@"
- "%s Failed to lock %@: %@"
- "%s Failed to unlock %@: %@"
- "%s Locked %@"
- "%s MA AutoAssetSet's downloadedCatalogCachedAssetSetID is nil for asset set - %{public}@"
- "%s No subscriptions for %{public}@ %{public}@: %{public}@"
- "%s Returning asset download status: %lu for subscriber: %{public}@ and subscription: %{public}@"
- "%s Returning status: %lu for subscriber: %{public}@ and subscription: %{public}@ as the asset set usages are nil"
- "%s Siri IE is now: wants assets: %d, language: %@"
- "%s Siri configured for: language %{public}@, mode: %{public}@"
- "%s Subscriptions for %{public}@ %{public}@: %{public}@"
- "%s Unexpected experiment file content for Asset Set %{public}@"
- "%s Unlocked %@"
- "+[UAFAutoAssetManager configureAssetSet:specifiers:changed:]"
- "+[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:]"
- "+[UAFAutoAssetManager getSpecifiers:assetSetUsages:disableExperimentation:]"
- "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:]"
- "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:]_block_invoke"
- "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:]_block_invoke_2"
- "+[UAFAutoAssetManager shouldCheckAssetSet:autoAssetSet:changed:locked:]"
- "+[UAFAutoAssetManager stageAssetSet:targets:autoAssetSet:]"
- "+[UAFAutoAssetSet catalogAssetSetID:]"
- "+[UAFCommonUtilities _setUAFPopulation:forAssetTypes:]"
- "+[UAFInstrumentationProvider logSubscriptionsStatus]"
- "-[UAFAssetSetManager assetSetUsagesForStatusForSubscriber:subscriptionName:status:]"
- "-[UAFAssetSetManager diskSpaceNeededForSubscriber:subscriptionName:storeManager:configurationManager:error:]"
- "-[UAFAssetSetManager downloadStatusForSubscriber:subscriptionName:]"
- "-[UAFAssetSetManager downloadStatusForSubscriber:subscriptionName:queue:completion:]"
- "-[UAFAssetSetManager downloadStatusForSubscriber:subscriptionName:queue:completion:]_block_invoke"
- "-[UAFAssetSetManager observeAssetSet:queue:handler:]"
- "-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]"
- "-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_2"
- "-[UAFAssetSetObserver initWithAssetSet:configurationDirURLs:queue:updateHandler:]"
- "-[UAFAssetSetObserver initWithAssetSet:configurationDirURLs:queue:updateHandler:]_block_invoke"
- "-[UAFAssetSetObserver initWithAssetSet:configurationDirURLs:queue:updateHandler:]_block_invoke_2"
- "-[UAFConfigurationManager getUsageAlias:]"
- "@40@0:8@16@24^Q32"
- "@44@0:8@16@24B32^B36"
- "@56@0:8@16@24@32@40^@48"
- "AFDeviceSupportsSAE"
- "Asset Set Consistency Token %@ for assetSet %@ with atomic instance %@ (%@) experiment %@ preinstalledAssetsSummary %@"
- "B44@0:8@16@24B32^B36"
- "TB,N,V_locked"
- "_setUAFPopulation:forAssetTypes:"
- "assetSetIdForSELF:"
- "assetSetUsagesForStatusForSubscriber:subscriptionName:status:"
- "catalogAssetSetID:"
- "checkResourceIsReachableAndReturnError:"
- "configureAssetSet:specifiers:changed:"
- "diskSpaceNeededForSubscriber:subscriptionName:storeManager:configurationManager:error:"
- "getAutoAssetSet:specifiers:addEntries:configured:"
- "getSpecifiers:assetSetUsages:"
- "getSpecifiers:assetSetUsages:disableExperimentation:"
- "getUsageAlias:"
- "initFileURLWithPath:"
- "manageAssetSet:specifiers:lockIfUnchanged:userInitiated:"
- "manageGMSSiriLanguageSubscription:language:"
- "setLocked:"
- "shouldCheckAssetSet:autoAssetSet:changed:locked:"
- "stageAssetSet:targets:autoAssetSet:"
- "updateAssets:policies:queue:progress:completion:"
- "updateAssets:policies:queue:progress:completion:storeManager:configurationManager:"
- "updateAssets:subscription:policies:queue:progress:completion:"
- "updateAssets:subscription:policies:queue:progress:completion:storeManager:configurationManager:"
- "updateAssets:subscription:policies:queue:progressWithStatus:completion:"
- "updateFinished"
- "v72@0:8@16@24@32@?40@?48@56@64"
- "v80@0:8@16@24@32@40@?48@?56@64@72"

```
