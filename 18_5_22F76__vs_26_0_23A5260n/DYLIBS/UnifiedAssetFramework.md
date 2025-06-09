## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3405.8.1.0.0
-  __TEXT.__text: 0x69098
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x3518
-  __TEXT.__const: 0xf8
+3500.87.2.0.0
+  __TEXT.__text: 0x6f600
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__objc_methlist: 0x3498
+  __TEXT.__const: 0x110
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__gcc_except_tab: 0x1358
-  __TEXT.__cstring: 0x9f24
-  __TEXT.__oslogstring: 0xbd31
-  __TEXT.__unwind_info: 0x1108
-  __TEXT.__objc_classname: 0x424
-  __TEXT.__objc_methname: 0xa091
-  __TEXT.__objc_methtype: 0xfe4
-  __TEXT.__objc_stubs: 0x81e0
-  __DATA_CONST.__got: 0x4e0
-  __DATA_CONST.__const: 0x1b68
-  __DATA_CONST.__objc_classlist: 0x160
-  __DATA_CONST.__objc_catlist: 0x8
+  __TEXT.__gcc_except_tab: 0x144c
+  __TEXT.__cstring: 0xab36
+  __TEXT.__oslogstring: 0xd208
+  __TEXT.__unwind_info: 0x11d0
+  __TEXT.__objc_classname: 0x45d
+  __TEXT.__objc_methname: 0x9a82
+  __TEXT.__objc_methtype: 0x1091
+  __TEXT.__objc_stubs: 0x7ca0
+  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__const: 0x1c68
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2730
+  __DATA_CONST.__objc_selrefs: 0x2578
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__auth_got: 0x5b0
-  __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x4100
-  __AUTH_CONST.__objc_const: 0x4300
-  __AUTH_CONST.__objc_intobj: 0x240
-  __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x350
-  __DATA.__data: 0x230
+  __DATA_CONST.__objc_superrefs: 0xe0
+  __DATA_CONST.__objc_arraydata: 0xd0
+  __AUTH_CONST.__auth_got: 0x5f8
+  __AUTH_CONST.__const: 0x5a0
+  __AUTH_CONST.__cfstring: 0x4600
+  __AUTH_CONST.__objc_const: 0x4270
+  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x324
+  __DATA.__data: 0x238
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0xc30
-  __DATA_DIRTY.__bss: 0x2f0
-  __DATA_DIRTY.__common: 0x60
+  __DATA_DIRTY.__bss: 0x2c0
+  __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
+  - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: D65F7E73-BD5D-35C8-A37C-A67C59312C57
-  Functions: 1414
-  Symbols:   5244
-  CStrings:  4140
+  UUID: 54F62409-AE5D-3B11-B6C4-E14C844FE823
+  Functions: 1437
+  Symbols:   5285
+  CStrings:  4281
 
Symbols:
+ +[UAFAssetSetManager _subscriptionDiffersFromDB:subscriber:user:error:]
+ +[UAFAssetSetManager configureAssetDelivery:configurationManager:lockIfUnchanged:oldSubscriptions:newSubscriptions:userInitiated:]
+ +[UAFAssetSetManager createProxyXPCConnection]
+ +[UAFAssetSetManager createSubscriptionXPCConnection]
+ +[UAFAssetSetManager createXPCConnection]
+ +[UAFAssetSetManager resetAssetSets:]
+ +[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]
+ +[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]
+ +[UAFAssetSetSubscriptionManager daemonSubscriptionMigration]
+ +[UAFAssetSetSubscriptionManager getSubscribers:storeManager:error:]
+ +[UAFAssetSetSubscriptionManager getSubscription:subscriber:user:storeManager:error:]
+ +[UAFAssetSetSubscriptionManager getSubscriptions:user:storeManager:error:]
+ +[UAFAssetSetSubscriptionManager migrateMBSetupUserSubscriptions:user:node:]
+ +[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]
+ +[UAFAutoAssetManager allowRemoves]
+ +[UAFAutoAssetManager cacheDeleteStatusChange:]
+ +[UAFAutoAssetManager configureAutoAssetsFromNewSubscriptions:oldSubscriptions:configurationManager:lockIfUnchanged:userInitiated:]
+ +[UAFAutoAssetManager consistencyTokenFromConfig:atomicInstance:experiment:]
+ +[UAFAutoAssetManager findDiffBetweenOldAssetSetUsages:newAssetSetUsages:knownAssetSets:usedAssetSets:configurationManager:]
+ +[UAFAutoAssetManager isLatestConsistencyToken:]
+ +[UAFAutoAssetManager removeAutoAssetSet:fallbackAlter:]
+ +[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:fallbackAlter:]
+ +[UAFAutoAssetManager setMinimalSpecifiers:]
+ +[UAFAutoAssetManager stageAssetsWithNewSubscriptions:oldSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:]
+ +[UAFAutoBugCapture isSymptomDiagnosticReporterAvailable]
+ +[UAFBiomeInstrumenter _constructBiomeAssetSet:storeManager:]
+ +[UAFBiomeInstrumenter _getAssetSource:]
+ +[UAFBiomeInstrumenter _getBiomeAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:]
+ +[UAFBiomeInstrumenter _getBiomeEventDeviceMetadata]
+ +[UAFBiomeInstrumenter _getBiomeStreamForAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:assetSetArrived:]
+ +[UAFBiomeInstrumenter _getBiomeStreamForScheduledDailyAssetStatus]
+ +[UAFBiomeInstrumenter _getBiomeUAFAssetSet:assetSetId:entries:errorCodes:fromPSUS:]
+ +[UAFBiomeInstrumenter _getSubscriptionsStatus]
+ +[UAFBiomeInstrumenter defaultDeviceId]
+ +[UAFBiomeInstrumenter isBiomeAvailable]
+ +[UAFBiomeInstrumenter logAssetSetDownloadEvent:assetSetId:entries:errorCodes:fromPSUS:assetSetArrived:]
+ +[UAFBiomeInstrumenter logScheduledDailyAssetStatus]
+ +[UAFCommonUtilities bestEffortSerializeDictToJSONStr:error:]
+ +[UAFCommonUtilities getPWUID:error:]
+ +[UAFCommonUtilities getUserDefaultStoragePath]
+ +[UAFCommonUtilities getenv:]
+ +[UAFCommonUtilities geteuid]
+ +[UAFCommonUtilities isSiriknowledgedSupported]
+ +[UAFCommonUtilities isTrialAvailable]
+ +[UAFCommonUtilities sandboxCheckMachEndpoint:]
+ +[UAFConfiguration sharedIpadSupported]
+ +[UAFConfiguration subscriptionServiceEnabled]
+ +[UAFCoreAnalyticsInstrumenter logUAFAssetSetState:assetSpecifiersAndVersions:]
+ +[UAFCoreAnalyticsInstrumenter sendCAEvent:assetSpecifier:assetVersion:]
+ +[UAFInstrumentationProvider _emitAssetDailyStatusEvent:autoAssetSet:entries:assetSetArrived:]
+ +[UAFInstrumentationProvider _getMADownloadErrors:assetSetName:assetSetID:]
+ +[UAFInstrumentationProvider isSiriAnalyticsAvailable]
+ +[UAFInstrumentationProvider logUAFAssetSetDailyStatus:entries:assetSetArrived:]
+ +[UAFSubscriptionStoreManager flattenSubscriptions:]
+ +[UAFSubscriptionStoreManager sendNotificationDBReset]
+ +[UAFUser currentConsoleUserWithUID:]
+ +[UAFUser currentUserWithNode:error:]
+ +[UAFUser isMultiUser]
+ +[UAFUser isSystemUser:error:]
+ +[UAFUser isSystemUserUsingUID:]
+ +[UAFUser nameForUser:error:]
+ +[UAFUser nodeForUser:error:]
+ +[UAFUser pwdNameForUser:error:]
+ +[UAFUser pwdNodeForUser:error:]
+ +[UAFUser pwdUIDToUserID:]
+ +[UAFUser pwdUserIDToUID:withError:]
+ +[UAFUser pwdUserWithNodeForUID:uid:error:]
+ +[UAFUser systemUserWithNode:error:]
+ +[UAFUser umCurrentUMUserWithNode:error:]
+ +[UAFUser umEntitlementPresent]
+ +[UAFUser umNameForUser:error:]
+ +[UAFUser umNodeForUser:error:]
+ +[UAFUser umUserWithDSID:withUid:withError:]
+ +[UAFUser umUserWithNodeForUID:uid:error:]
+ +[UAFUser userWithNodeForUID:uid:error:]
+ +[UAFUser validLocalNode]
+ +[UAFUser validLocalUsers:error:]
+ +[UAFUser validNodesWithError:]
+ +[UAFUserManager getConcurrentQueue]
+ +[UAFUserManager performUserCleanupOnQueue:completion:]
+ +[UAFUserManager performUserCleanup]
+ +[UAFUserManager removeUser:]
+ +[UAFUserManager removeUser:queue:completion:]
+ +[UAFUserManager updateLastSeenForCurrentUserOnQueue:completion:]
+ +[UAFUserManager updateLastSeenForUser:queue:completion:]
+ +[UAFXPCActivity maintenanceTaskWithCompletion:]
+ +[UAFXPCConnection getUserServiceXPCEndpoint]
+ +[UAFXPCConnection selectXPCEndpoint]
+ -[UAFAssetSetConfiguration description]
+ -[UAFAssetSetConsistencyToken experimentActivated]
+ -[UAFAssetSetConsistencyToken experimentId]
+ -[UAFAssetSetConsistencyToken initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:bootUUID:experimentActivated:]
+ -[UAFAssetSetConsistencyToken instanceUUID]
+ -[UAFAssetSetConsistencyToken setExperimentActivated:]
+ -[UAFAssetSetConsistencyToken setInstanceUUID:]
+ -[UAFAssetSetManager assetSetUsagesForSubscribers:storeManager:configurationManager:anyUnknown:error:]
+ -[UAFAssetSetManager isLatestConsistencyToken:]
+ -[UAFAssetSetManager resetAssetSets:queue:completion:]
+ -[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]
+ -[UAFAssetSetManager subscriptions:subscriber:user:storeManager:error:]
+ -[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]
+ -[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:internalProgress:completion:storeManager:configurationManager:]
+ -[UAFAssetSetProgress progress:completed:total:status:context:]
+ -[UAFAssetUtilitiesService resume]
+ -[UAFAssetUtilitiesService suspend]
+ -[UAFAutoAssetProgress errors]
+ -[UAFAutoAssetProgress finished:withStatus:withError:]
+ -[UAFAutoAssetProgress initWithAssetSetUsages:configurationManager:internalProgressWithStatus:]
+ -[UAFAutoAssetProgress internalProgressCompletion]
+ -[UAFAutoAssetProgress setErrors:]
+ -[UAFAutoAssetProgress setInternalProgressCompletion:]
+ -[UAFSubscriptionStoreManager _acquireAssertion]
+ -[UAFSubscriptionStoreManager _checkDbVersion:storedVersion:]
+ -[UAFSubscriptionStoreManager _finalizeStatements]
+ -[UAFSubscriptionStoreManager _getAllSubscriptions:]
+ -[UAFSubscriptionStoreManager _getSubscribers:subscribers:]
+ -[UAFSubscriptionStoreManager _getSubscription:subscription:user:]
+ -[UAFSubscriptionStoreManager _getSubscriptions:user:]
+ -[UAFSubscriptionStoreManager _getUser:lastSeen:nodeName:]
+ -[UAFSubscriptionStoreManager _releaseAssertion]
+ -[UAFSubscriptionStoreManager _removeUser:]
+ -[UAFSubscriptionStoreManager _setUserLastSeenTime:node:time:]
+ -[UAFSubscriptionStoreManager _store]
+ -[UAFSubscriptionStoreManager _subscribeSubscription:subscriptionName:assetSetSubscription:expires:user:]
+ -[UAFSubscriptionStoreManager _unsubscribeSubscription:subscription:user:]
+ -[UAFSubscriptionStoreManager databaseName]
+ -[UAFSubscriptionStoreManager getAllSystemConfiguration:]
+ -[UAFSubscriptionStoreManager getSubscribers:error:]
+ -[UAFSubscriptionStoreManager getSubscription:subscriber:user:error:]
+ -[UAFSubscriptionStoreManager getSubscriptions:user:error:]
+ -[UAFSubscriptionStoreManager getUserLastSeenTime:error:]
+ -[UAFSubscriptionStoreManager getUserNodeName:error:]
+ -[UAFSubscriptionStoreManager getUsers:]
+ -[UAFSubscriptionStoreManager getUsersOlderThanDate:error:]
+ -[UAFSubscriptionStoreManager performDbUpgrade]
+ -[UAFSubscriptionStoreManager readDate:col:]
+ -[UAFSubscriptionStoreManager removeAllUsers]
+ -[UAFSubscriptionStoreManager removeUser:]
+ -[UAFSubscriptionStoreManager setUserLastSeenTime:node:time:]
+ -[UAFSubscriptionStoreManager subscribe:subscriptions:user:node:]
+ -[UAFSubscriptionStoreManager unsubscribe:subscriptions:user:node:]
+ -[UAFXPCConnection expireSubscriptions:]
+ -[UAFXPCConnection initWithDefaultService]
+ -[UAFXPCConnection initWithSubscriptionServiceName]
+ -[UAFXPCConnection initWithUserService]
+ -[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]
+ -[UAFXPCConnection subscriptions:subscriber:user:completion:]
+ -[UAFXPCService expireSubscriptions:]
+ -[UAFXPCService initSubscriptionService]
+ -[UAFXPCService initWithMachServiceName:subscriptionService:]
+ -[UAFXPCService initWithXPCListener:subscriptionService:]
+ -[UAFXPCService setSystemConfigurationForKey:withValue:completion:]
+ -[UAFXPCService subscribeWithConfig:userInitiated:completion:]
+ -[UAFXPCService subscriptions:subscriber:user:completion:]
+ -[UAFXPCService unsubscribeWithConfig:userInitiated:completion:]
+ GCC_except_table102
+ GCC_except_table111
+ GCC_except_table14
+ GCC_except_table20
+ GCC_except_table21
+ GCC_except_table24
+ GCC_except_table28
+ GCC_except_table42
+ GCC_except_table45
+ GCC_except_table53
+ GCC_except_table67
+ GCC_except_table69
+ GCC_except_table73
+ GCC_except_table82
+ GCC_except_table85
+ GCC_except_table88
+ GCC_except_table90
+ GCC_except_table94
+ GCC_except_table96
+ _AnalyticsSendEventLazy
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMAssetDeliveryDailyStatus
+ _OBJC_CLASS_$_BMUAFAsset
+ _OBJC_CLASS_$_BMUAFAssetSet
+ _OBJC_CLASS_$_BMUAFAssetSetStatus
+ _OBJC_CLASS_$_BMUAFAssetSetSubscription
+ _OBJC_CLASS_$_BMUAFAssetSetUsage
+ _OBJC_CLASS_$_BMUAFAssetSubscriberSubscriptions
+ _OBJC_CLASS_$_BMUAFAssetUsageAlias
+ _OBJC_CLASS_$_BMUAFAvailableAssetDailyStatus
+ _OBJC_CLASS_$_BMUAFDeviceMetadata
+ _OBJC_CLASS_$_BMUAFISOLocale
+ _OBJC_CLASS_$_BMUAFMobileAssetDownloadErrorCodeFrequency
+ _OBJC_CLASS_$_RBSAssertion
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_CLASS_$_RBSProcessHandle
+ _OBJC_CLASS_$_RBSTarget
+ _OBJC_CLASS_$_UAFAssetSetSubscriptionManager
+ _OBJC_CLASS_$_UAFBiomeInstrumenter
+ _OBJC_CLASS_$_UAFCoreAnalyticsInstrumenter
+ _OBJC_CLASS_$_UAFUser
+ _OBJC_CLASS_$_UAFUserManager
+ _OBJC_CLASS_$_UAFXPCActivity
+ _OBJC_CLASS_$_UMUserManager
+ _OBJC_IVAR_$_UAFAssetSetConsistencyToken._experimentActivated
+ _OBJC_IVAR_$_UAFAssetSetConsistencyToken._instanceUUID
+ _OBJC_IVAR_$_UAFAssetUtilitiesService._queuesArePaused
+ _OBJC_IVAR_$_UAFAutoAssetProgress._errors
+ _OBJC_IVAR_$_UAFAutoAssetProgress._internalProgressCompletion
+ _OBJC_IVAR_$_UAFSubscriptionStoreManager._deleteDbVersion
+ _OBJC_IVAR_$_UAFSubscriptionStoreManager._rbassertion
+ _OBJC_IVAR_$_UAFSubscriptionStoreManager._readAllUsers
+ _OBJC_IVAR_$_UAFSubscriptionStoreManager._readSubscriptionsForUser
+ _OBJC_IVAR_$_UAFSubscriptionStoreManager._readUser
+ _OBJC_IVAR_$_UAFSubscriptionStoreManager._readUsersOlderThan
+ _OBJC_IVAR_$_UAFSubscriptionStoreManager._removeAllUsers
+ _OBJC_IVAR_$_UAFSubscriptionStoreManager._removeUser
+ _OBJC_IVAR_$_UAFSubscriptionStoreManager._writeUserLastSeen
+ _OBJC_IVAR_$_UAFXPCService._subscriptionService
+ _OBJC_METACLASS_$_UAFAssetSetSubscriptionManager
+ _OBJC_METACLASS_$_UAFBiomeInstrumenter
+ _OBJC_METACLASS_$_UAFCoreAnalyticsInstrumenter
+ _OBJC_METACLASS_$_UAFUser
+ _OBJC_METACLASS_$_UAFUserManager
+ _OBJC_METACLASS_$_UAFXPCActivity
+ _UAFRegisterSubscriptionXPCActivities
+ _XPC_ACTIVITY_INTERVAL_7_DAYS
+ _XPC_ACTIVITY_PRIORITY_MAINTENANCE
+ __OBJC_$_CLASS_METHODS_UAFAssetSetSubscriptionManager
+ __OBJC_$_CLASS_METHODS_UAFBiomeInstrumenter
+ __OBJC_$_CLASS_METHODS_UAFCoreAnalyticsInstrumenter
+ __OBJC_$_CLASS_METHODS_UAFUser
+ __OBJC_$_CLASS_METHODS_UAFUserManager
+ __OBJC_$_CLASS_METHODS_UAFXPCActivity
+ __OBJC_$_CLASS_METHODS_UAFXPCConnection
+ __OBJC_CLASS_RO_$_UAFAssetSetSubscriptionManager
+ __OBJC_CLASS_RO_$_UAFBiomeInstrumenter
+ __OBJC_CLASS_RO_$_UAFCoreAnalyticsInstrumenter
+ __OBJC_CLASS_RO_$_UAFUser
+ __OBJC_CLASS_RO_$_UAFUserManager
+ __OBJC_CLASS_RO_$_UAFXPCActivity
+ __OBJC_METACLASS_RO_$_UAFAssetSetSubscriptionManager
+ __OBJC_METACLASS_RO_$_UAFBiomeInstrumenter
+ __OBJC_METACLASS_RO_$_UAFCoreAnalyticsInstrumenter
+ __OBJC_METACLASS_RO_$_UAFUser
+ __OBJC_METACLASS_RO_$_UAFUserManager
+ __OBJC_METACLASS_RO_$_UAFXPCActivity
+ __RegisterOnBootUAFActivity
+ __RegisterPeriodicUAFSubscriptionActivity
+ __RegisterPostUpgradeUAFActivity
+ ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke
+ ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.314
+ ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke_2
+ ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke
+ ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.358
+ ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.359
+ ___123+[UAFAutoAssetManager stageAssetsWithNewSubscriptions:oldSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:]_block_invoke
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.455
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.456
+ ___131+[UAFAutoAssetManager configureAutoAssetsFromNewSubscriptions:oldSubscriptions:configurationManager:lockIfUnchanged:userInitiated:]_block_invoke
+ ___152-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:internalProgress:completion:storeManager:configurationManager:]_block_invoke
+ ___152-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:internalProgress:completion:storeManager:configurationManager:]_block_invoke_2
+ ___152-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:internalProgress:completion:storeManager:configurationManager:]_block_invoke_3
+ ___152-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:internalProgress:completion:storeManager:configurationManager:]_block_invoke_4
+ ___152-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:internalProgress:completion:storeManager:configurationManager:]_block_invoke_5
+ ___152-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:internalProgress:completion:storeManager:configurationManager:]_block_invoke_6
+ ___27-[UAFXPCService runUpdates]_block_invoke.372
+ ___27-[UAFXPCService runUpdates]_block_invoke.373
+ ___27-[UAFXPCService runUpdates]_block_invoke.375
+ ___27-[UAFXPCService runUpdates]_block_invoke_2
+ ___27-[UAFXPCService runUpdates]_block_invoke_3
+ ___29+[UAFUserManager removeUser:]_block_invoke
+ ___29+[UAFUserManager removeUser:]_block_invoke.285
+ ___31-[UAFXPCConnection _connection]_block_invoke.288
+ ___36+[UAFUserManager getConcurrentQueue]_block_invoke
+ ___36+[UAFUserManager performUserCleanup]_block_invoke
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.295
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.297
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.301
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.302
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.303
+ ___37+[UAFAssetSetManager resetAssetSets:]_block_invoke
+ ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke.307
+ ___37-[UAFXPCService expireSubscriptions:]_block_invoke
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.405
+ ___39+[UAFBiomeInstrumenter defaultDeviceId]_block_invoke
+ ___40-[UAFSubscriptionStoreManager getUsers:]_block_invoke
+ ___40-[UAFXPCConnection expireSubscriptions:]_block_invoke
+ ___40-[UAFXPCConnection expireSubscriptions:]_block_invoke.296
+ ___40-[UAFXPCConnection expireSubscriptions:]_block_invoke_2
+ ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.390
+ ___42-[UAFSubscriptionStoreManager removeUser:]_block_invoke
+ ___42-[UAFXPCConnection diagnosticInformation:]_block_invoke.291
+ ___42-[UAFXPCConnection initWithDefaultService]_block_invoke
+ ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.337
+ ___45-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke.333
+ ___45-[UAFAutoAssetSet mapAsset:queue:completion:]_block_invoke.331
+ ___45-[UAFSubscriptionStoreManager removeAllUsers]_block_invoke
+ ___46+[UAFUserManager removeUser:queue:completion:]_block_invoke
+ ___46+[UAFUserManager removeUser:queue:completion:]_block_invoke_2
+ ___46-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke.325
+ ___46-[UAFXPCService markAssetsExpired:completion:]_block_invoke
+ ___47+[UAFBiomeInstrumenter _getSubscriptionsStatus]_block_invoke
+ ___47+[UAFCommonUtilities isSiriknowledgedSupported]_block_invoke
+ ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke.289
+ ___47-[UAFSubscriptionStoreManager performDbUpgrade]_block_invoke
+ ___48-[UAFAssetUtilities _assistantPreferencesUpdate]_block_invoke.338
+ ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.406
+ ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.408
+ ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke_2
+ ___49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke.294
+ ___50-[UAFAutoAssetSet invalidateWithQueue:completion:]_block_invoke.311
+ ___51+[UAFAssetSetManager generateInformationWithError:]_block_invoke
+ ___51+[UAFAssetSetManager generateInformationWithError:]_block_invoke_2
+ ___51+[UAFAssetSetManager generateInformationWithError:]_block_invoke_3
+ ___51-[UAFXPCConnection operationWithConfig:completion:]_block_invoke.290
+ ___52+[UAFSubscriptionStoreManager flattenSubscriptions:]_block_invoke
+ ___52+[UAFSubscriptionStoreManager flattenSubscriptions:]_block_invoke_2
+ ___52-[UAFSubscriptionStoreManager getSubscribers:error:]_block_invoke
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.338
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.339
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke_2
+ ___53-[UAFAssetUtilities _downloadSiriAssetsOverCellular:]_block_invoke.328
+ ___53-[UAFSubscriptionStoreManager getUserNodeName:error:]_block_invoke
+ ___53-[UAFXPCService lockLatestAtomicInstance:completion:]_block_invoke.417
+ ___54-[UAFAssetSetManager resetAssetSets:queue:completion:]_block_invoke
+ ___54-[UAFAssetSetManager resetAssetSets:queue:completion:]_block_invoke_2
+ ___54-[UAFAutoAssetProgress finished:withStatus:withError:]_block_invoke
+ ___55+[UAFUserManager performUserCleanupOnQueue:completion:]_block_invoke
+ ___55+[UAFUserManager performUserCleanupOnQueue:completion:]_block_invoke_2
+ ___56-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke.293
+ ___57+[UAFUserManager updateLastSeenForUser:queue:completion:]_block_invoke
+ ___57+[UAFUserManager updateLastSeenForUser:queue:completion:]_block_invoke_2
+ ___57-[UAFSubscriptionStoreManager getAllSystemConfiguration:]_block_invoke
+ ___57-[UAFSubscriptionStoreManager getUserLastSeenTime:error:]_block_invoke
+ ___59-[UAFSubscriptionStoreManager getSubscriptions:user:error:]_block_invoke
+ ___59-[UAFSubscriptionStoreManager getUsersOlderThanDate:error:]_block_invoke
+ ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.412
+ ___61+[UAFAssetSetSubscriptionManager daemonSubscriptionMigration]_block_invoke
+ ___61-[UAFSubscriptionStoreManager setUserLastSeenTime:node:time:]_block_invoke
+ ___61-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke
+ ___61-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke.297
+ ___61-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke_2
+ ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke.314
+ ___63-[UAFAssetSetProgress progress:completed:total:status:context:]_block_invoke
+ ___63-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke.310
+ ___65+[UAFUserManager updateLastSeenForCurrentUserOnQueue:completion:]_block_invoke
+ ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.307
+ ___65-[UAFSubscriptionStoreManager subscribe:subscriptions:user:node:]_block_invoke
+ ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke.329
+ ___67-[UAFSubscriptionStoreManager unsubscribe:subscriptions:user:node:]_block_invoke
+ ___67-[UAFXPCService setSystemConfigurationForKey:withValue:completion:]_block_invoke
+ ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.406
+ ___69-[UAFSubscriptionStoreManager getSubscription:subscriber:user:error:]_block_invoke
+ ___70-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke
+ ___70-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke.295
+ ___70-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke_2
+ ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke
+ ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke.297
+ ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke_2
+ ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke_2.298
+ ___71-[UAFAssetSetManager subscriptions:subscriber:user:storeManager:error:]_block_invoke
+ ___71-[UAFAssetSetManager subscriptions:subscriber:user:storeManager:error:]_block_invoke_2
+ ___72+[UAFCoreAnalyticsInstrumenter sendCAEvent:assetSpecifier:assetVersion:]_block_invoke
+ ___74+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:fallbackAlter:]_block_invoke
+ ___74+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:fallbackAlter:]_block_invoke.374
+ ___75+[UAFAssetSetSubscriptionManager getSubscriptions:user:storeManager:error:]_block_invoke
+ ___75+[UAFAssetSetSubscriptionManager getSubscriptions:user:storeManager:error:]_block_invoke_2
+ ___75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke.309
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.314
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.325
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.327
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke_2.328
+ ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke.297
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.401
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.402
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.403
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke_2
+ ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.424
+ ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke
+ ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.404
+ ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke_2
+ ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.428
+ ___97+[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:]_block_invoke
+ ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.457
+ ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke
+ ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.307
+ ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke_2
+ ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke_3
+ ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke_4
+ ____RegisterPeriodicUAFSubscriptionActivity_block_invoke.312
+ ____RegisterUserCleanupUAFActivity_block_invoke
+ ____RegisterUserCleanupUAFActivity_block_invoke_2
+ ____RegisterXPCActivity_block_invoke.301
+ ___block_descriptor_33_e42_v24?0"NSObject<OS_xpc_object>"8?<v?>16l
+ ___block_descriptor_40_e8_32r_e39_v32?0"NSString"8"NSDictionary"16^B24lr32l8
+ ___block_descriptor_40_e8_32s_e22_v24?0"NSString"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e23_v52?0d8Q16Q24Q32B4044ls32l8
+ ___block_descriptor_40_e8_32s_e25_v32?0"NSString"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e42_v32?0"NSString"8"NSArray"16"NSError"24ls32l8
+ ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e8_32s40bs_e8_v16?0Q8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e40_v32?0"UAFAssetSetSubscription"8Q16^B24ls32l8r40l8
+ ___block_descriptor_56_e8_32r40r48r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e25_v32?0"NSString"8Q16^B24ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e41_v32?0"NSString"8"NSMutableArray"16^B24ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e19_"NSDictionary"8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e34_v32?0"NSString"8"NSArray"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40bs48bs56bs_e23_v52?0d8Q16Q24Q32B4044ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e17_v16?0"NSError"8ls32l8s40l8r56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_i8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e40_v32?0"UAFAssetSetSubscription"8Q16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48bs56r_e5_v8?0ls32l8r56l8s48l8s40l8
+ ___block_descriptor_66_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_i8?0lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_B8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_i8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8r64l8s56l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72r_e17_v16?0"NSError"8ls32l8s64l8s40l8s48l8s56l8r72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e17_v16?0"NSError"8ls32l8s72l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_i8?0ls32l8r72l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_81_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8s48l8s56l8r72l8s64l8
+ ___block_descriptor_97_e8_32s40bs48bs56bs_e5_v8?0ls40l8s32l8s48l8s56l8
+ ___block_literal_global.306
+ ___block_literal_global.309
+ ___block_literal_global.310
+ ___block_literal_global.316
+ ___block_literal_global.318
+ ___block_literal_global.320
+ ___block_literal_global.321
+ ___block_literal_global.323
+ ___block_literal_global.327
+ ___block_literal_global.330
+ ___block_literal_global.334
+ ___block_literal_global.364
+ ___block_literal_global.367
+ ___block_literal_global.382
+ ___block_literal_global.386
+ ___block_literal_global.403
+ ___block_literal_global.408
+ ___block_literal_global.409
+ ___block_literal_global.411
+ _dispatch_resume
+ _dispatch_suspend
+ _getenv
+ _getpid
+ _getpwuid_r
+ _kDefaultUAFSubscriptionServiceName
+ _kUAFAssetMetadataPrerequisiteBuildsKey
+ _kUAFAutoAssetMetadataPrerequisiteBuilds
+ _kUAFBaseUUID
+ _kUAFConfHasMigrated
+ _kUAFDefaultStorageAbsoluteDirectoryPath
+ _kUAFEmbeddedUser
+ _kUAFEmbeddedUserNode
+ _kUAFInhibitRemoves
+ _kUAFNotificationDBReset
+ _kUAFPasswdHomeDir
+ _kUAFPasswdUsername
+ _kUAFProgressContext
+ _kUAFSubscriptionServiceStarted
+ _kUAFSystemNode
+ _kUAFSystemUser
+ _kUAFUMMultiUserNode
+ _kUAFUserLastSeen
+ _kUAFUserNode
+ _kUAFUserTimeout
+ _kUAFValidationAssetSet
+ _kUAFValidationSubscriber
+ _kUAFValidationSubscription
+ _kUAFXPCAssetSets
+ _kUAFXPCMigrateSubscriptions
+ _kUAFXPCRemoveUser
+ _kUAFXPCResetAssetSets
+ _kUAFXPCRunMaintenanceTask
+ _kUAFXPCSubscriptionUser
+ _kUAFXPCSubscriptionsToMigrate
+ _kUAFXPCUpdateLastSeen
+ _kUAFXPCUserCleanup
+ _objc_msgSend$AssetDelivery
+ _objc_msgSend$DailyStatus
+ _objc_msgSend$UAF
+ _objc_msgSend$_acquireAssertion
+ _objc_msgSend$_checkDbVersion:storedVersion:
+ _objc_msgSend$_constructBiomeAssetSet:storeManager:
+ _objc_msgSend$_emitAssetDailyStatusEvent:autoAssetSet:entries:assetSetArrived:
+ _objc_msgSend$_finalizeStatements
+ _objc_msgSend$_getAllSubscriptions:
+ _objc_msgSend$_getBiomeAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:
+ _objc_msgSend$_getBiomeEventDeviceMetadata
+ _objc_msgSend$_getBiomeStreamForAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:assetSetArrived:
+ _objc_msgSend$_getBiomeStreamForScheduledDailyAssetStatus
+ _objc_msgSend$_getBiomeUAFAssetSet:assetSetId:entries:errorCodes:fromPSUS:
+ _objc_msgSend$_getMADownloadErrors:assetSetName:assetSetID:
+ _objc_msgSend$_getSubscribers:subscribers:
+ _objc_msgSend$_getSubscription:subscription:user:
+ _objc_msgSend$_getSubscriptions:user:
+ _objc_msgSend$_getSubscriptionsStatus
+ _objc_msgSend$_getUser:lastSeen:nodeName:
+ _objc_msgSend$_releaseAssertion
+ _objc_msgSend$_removeUser:
+ _objc_msgSend$_setUserLastSeenTime:node:time:
+ _objc_msgSend$_store
+ _objc_msgSend$_subscribeSubscription:subscriptionName:assetSetSubscription:expires:user:
+ _objc_msgSend$_subscriptionDiffersFromDB:subscriber:user:error:
+ _objc_msgSend$_unsubscribeSubscription:subscription:user:
+ _objc_msgSend$acquireWithError:
+ _objc_msgSend$allUsers
+ _objc_msgSend$allowRemoves
+ _objc_msgSend$alternateDSID
+ _objc_msgSend$assetSetUsagesForSubscribers:storeManager:configurationManager:anyUnknown:error:
+ _objc_msgSend$attributeWithDomain:name:
+ _objc_msgSend$bestEffortSerializeDictToJSONStr:error:
+ _objc_msgSend$cacheDeleteStatusChange:
+ _objc_msgSend$configureAssetDelivery:configurationManager:lockIfUnchanged:oldSubscriptions:newSubscriptions:userInitiated:
+ _objc_msgSend$configureAutoAssetsFromNewSubscriptions:oldSubscriptions:configurationManager:lockIfUnchanged:userInitiated:
+ _objc_msgSend$consistencyTokenFromConfig:atomicInstance:experiment:
+ _objc_msgSend$createProxyXPCConnection
+ _objc_msgSend$createSubscriptionXPCConnection
+ _objc_msgSend$createXPCConnection
+ _objc_msgSend$currentConnection
+ _objc_msgSend$currentConsoleUserWithUID:
+ _objc_msgSend$currentProcess
+ _objc_msgSend$currentUser
+ _objc_msgSend$currentUserWithNode:error:
+ _objc_msgSend$daemonSubscriptionMigration
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$distantFuture
+ _objc_msgSend$effectiveUserIdentifier
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$errors
+ _objc_msgSend$expireSubscriptions:
+ _objc_msgSend$findDiffBetweenOldAssetSetUsages:newAssetSetUsages:knownAssetSets:usedAssetSets:configurationManager:
+ _objc_msgSend$finished:withStatus:withError:
+ _objc_msgSend$flattenSubscriptions:
+ _objc_msgSend$getAllSystemConfiguration:
+ _objc_msgSend$getPWUID:error:
+ _objc_msgSend$getSubscribers:error:
+ _objc_msgSend$getSubscription:subscriber:user:error:
+ _objc_msgSend$getSubscription:subscriber:user:storeManager:error:
+ _objc_msgSend$getSubscriptions:storeManager:
+ _objc_msgSend$getSubscriptions:user:error:
+ _objc_msgSend$getSubscriptions:user:storeManager:error:
+ _objc_msgSend$getUUIDBytes:
+ _objc_msgSend$getUserDefaultStoragePath
+ _objc_msgSend$getUserNodeName:error:
+ _objc_msgSend$getUserServiceXPCEndpoint
+ _objc_msgSend$getUsersOlderThanDate:error:
+ _objc_msgSend$getenv:
+ _objc_msgSend$geteuid
+ _objc_msgSend$init
+ _objc_msgSend$initWithAliasName:aliasValue:
+ _objc_msgSend$initWithAssetName:assetSpecifier:assetVersion:assetLocale:assetSource:isAssetPathValid:assetPath:assetDownloadSizeInBytes:assetUnarchivedSizeInBytes:
+ _objc_msgSend$initWithAssetSetName:assets:assetType:assetSetId:audienceId:mobileAssetDownloadErrorCodeFrequency:fromPreSoftwareUpdateStaging:expensiveCellularDownloadRequested:
+ _objc_msgSend$initWithAssetSetStatus:statusReason:
+ _objc_msgSend$initWithAssetSetUsages:configurationManager:internalProgressWithStatus:
+ _objc_msgSend$initWithDefaultService
+ _objc_msgSend$initWithDeviceId:deviceType:programCode:systemBuild:inputLocale:nanoSecondsSinceLastBoot:
+ _objc_msgSend$initWithDeviceMetadata:availableAssetDailyStatus:
+ _objc_msgSend$initWithExplanation:target:attributes:
+ _objc_msgSend$initWithLanguageCode:countryCode:
+ _objc_msgSend$initWithMachServiceName:subscriptionService:
+ _objc_msgSend$initWithMobileAssetDownloadErrorCode:timesOccurred:
+ _objc_msgSend$initWithSubscriberName:subscriptions:
+ _objc_msgSend$initWithSubscriptionName:assetSetIndices:assetSetUsages:usageAliases:
+ _objc_msgSend$initWithSubscriptionServiceName
+ _objc_msgSend$initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:bootUUID:experimentActivated:
+ _objc_msgSend$initWithUafAssetSets:uafAssetSubscriptions:allAssets:
+ _objc_msgSend$initWithUsageName:usageValue:
+ _objc_msgSend$initWithUserService
+ _objc_msgSend$initWithXPCListener:subscriptionService:
+ _objc_msgSend$instanceUUID
+ _objc_msgSend$invalidateSyncWithError:
+ _objc_msgSend$isBiomeAvailable
+ _objc_msgSend$isLatestConsistencyToken:
+ _objc_msgSend$isManaged
+ _objc_msgSend$isMultiUser
+ _objc_msgSend$isSharedIPad
+ _objc_msgSend$isSiriAnalyticsAvailable
+ _objc_msgSend$isSiriknowledgedSupported
+ _objc_msgSend$isSymptomDiagnosticReporterAvailable
+ _objc_msgSend$isSystemUser:error:
+ _objc_msgSend$isSystemUserUsingUID:
+ _objc_msgSend$logAssetSetDownloadEvent:assetSetId:entries:errorCodes:fromPSUS:assetSetArrived:
+ _objc_msgSend$logScheduledDailyAssetStatus
+ _objc_msgSend$logUAFAssetSetDailyStatus:entries:assetSetArrived:
+ _objc_msgSend$logUAFAssetSetState:assetSpecifiersAndVersions:
+ _objc_msgSend$loginUser
+ _objc_msgSend$maintenanceTaskWithCompletion:
+ _objc_msgSend$migrateMBSetupUserSubscriptions:user:node:
+ _objc_msgSend$migrateSubscriptions:user:completion:
+ _objc_msgSend$nodeForUser:error:
+ _objc_msgSend$performDbUpgrade
+ _objc_msgSend$performUserCleanup
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$progress:completed:total:status:context:
+ _objc_msgSend$pwdNameForUser:error:
+ _objc_msgSend$pwdNodeForUser:error:
+ _objc_msgSend$pwdUIDToUserID:
+ _objc_msgSend$pwdUserIDToUID:withError:
+ _objc_msgSend$pwdUserWithNodeForUID:uid:error:
+ _objc_msgSend$readDate:col:
+ _objc_msgSend$regionCode
+ _objc_msgSend$removeAutoAssetSet:fallbackAlter:
+ _objc_msgSend$removeUser:
+ _objc_msgSend$resetAssetSets:
+ _objc_msgSend$sandboxCheckMachEndpoint:
+ _objc_msgSend$selectXPCEndpoint
+ _objc_msgSend$sendCAEvent:assetSpecifier:assetVersion:
+ _objc_msgSend$sendEvent:
+ _objc_msgSend$sendNotificationDBReset
+ _objc_msgSend$setExperimentActivated:
+ _objc_msgSend$setLatestAtomicInstance:autoAssetSet:fallbackAlter:
+ _objc_msgSend$setMinimalSpecifiers:
+ _objc_msgSend$setSystemConfigurationForKey:withValue:completion:
+ _objc_msgSend$setUserLastSeenTime:node:time:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$sharedIpadSupported
+ _objc_msgSend$shortTermLockFileName
+ _objc_msgSend$source
+ _objc_msgSend$stageAssetsWithNewSubscriptions:oldSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:
+ _objc_msgSend$subscribe:subscriptions:user:node:
+ _objc_msgSend$subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:
+ _objc_msgSend$subscribe:subscriptions:user:userInitiated:queue:completion:
+ _objc_msgSend$subscribeWithConfig:userInitiated:completion:
+ _objc_msgSend$subscriptionServiceEnabled
+ _objc_msgSend$subscriptions:subscriber:user:completion:
+ _objc_msgSend$subscriptions:subscriber:user:storeManager:error:
+ _objc_msgSend$synchronize
+ _objc_msgSend$systemUserWithNode:error:
+ _objc_msgSend$uid
+ _objc_msgSend$umCurrentUMUserWithNode:error:
+ _objc_msgSend$umEntitlementPresent
+ _objc_msgSend$umNodeForUser:error:
+ _objc_msgSend$umUserWithDSID:withUid:withError:
+ _objc_msgSend$umUserWithNodeForUID:uid:error:
+ _objc_msgSend$unsubscribe:subscriptionNames:user:userInitiated:queue:completion:
+ _objc_msgSend$unsubscribe:subscriptions:user:node:
+ _objc_msgSend$unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:
+ _objc_msgSend$unsubscribeWithConfig:userInitiated:completion:
+ _objc_msgSend$updateAssetsForSubscribers:policies:queue:progress:detailedProgress:internalProgress:completion:storeManager:configurationManager:
+ _objc_msgSend$updateLastSeenForCurrentUserOnQueue:completion:
+ _objc_msgSend$updateLastSeenForUser:queue:completion:
+ _objc_msgSend$userWithNodeForUID:uid:error:
+ _objc_msgSend$username
+ _objc_msgSend$validLocalNode
+ _objc_msgSend$validLocalUsers:error:
+ _objc_msgSend$validNodesWithError:
+ _os_transaction_create
+ _sandbox_check
+ _sqlite3_column_double
+ _sysconf
+ _upgradeBlocks_block_invoke_2
- +[TRIClient(UAFTrialClient) UAFCacheUpdate]
- +[TRIClient(UAFTrialClient) _addFactorLevelsToCache:namespaceName:withFactorLevelsCache:withLevelCache:]
- +[TRIClient(UAFTrialClient) _addLevelToCache:namespaceName:factorName:withCache:]
- +[TRIClient(UAFTrialClient) _cachedLevelForFactor:withNamespaceName:withLanguage:withCache:]
- +[TRIClient(UAFTrialClient) _cachedLevelForFactorAnyLanguage:withNamespaceName:withCache:]
- +[TRIClient(UAFTrialClient) _factoryFactorLevelsWithNamespaceName:onDemandClient:]
- +[TRIClient(UAFTrialClient) _factoryLevelForFactor:withNamespaceName:withLanguage:]
- +[TRIClient(UAFTrialClient) _levelKeyForCache:withFactorName:withLanguage:]
- +[TRIClient(UAFTrialClient) _queryAssetsWithNamespaceName:factorName:language:isRoot:withError:]
- +[TRIClient(UAFTrialClient) _rootFactorLevelsWithNamespaceName:]
- +[TRIClient(UAFTrialClient) _rootLevelForFactor:withNamespaceName:withLanguage:]
- +[UAFAssetSet getEntitledTrialAssets:usages:]
- +[UAFAssetSet getTrialPurgeabilityLevel:]
- +[UAFAssetSetConfiguration fromContentsOfURL:applyFeatureFlags:error:]
- +[UAFAssetSetManager _subscriptionDiffersFromDB:subscriber:error:]
- +[UAFAssetSetManager configureAssetDelivery:configurationManager:lockIfUnchanged:subscriptions:assetSetUsages:userInitiated:]
- +[UAFAssetSetManager shouldConfigure:newUsages:]
- +[UAFAssetSetManager subscribe:subscriptions:queue:completion:]
- +[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:userInitiated:]
- +[UAFAssetSetManager unsubscribe:subscriptions:queue:completion:]
- +[UAFAssetSetManager unsubscribe:subscriptions:storeManager:configurationManager:userInitiated:]
- +[UAFAutoAssetManager _logDailyStatusEventForAssetSetArrived:entries:assetSetArrived:]
- +[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:userInitiated:]
- +[UAFAutoAssetManager removeAutoAssetSet:completion:]
- +[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]
- +[UAFAutoAssetManager stageAssetsWithSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:]
- +[UAFCommonUtilities getPWUID:]
- +[UAFCommonUtilities isChinaDeviceRegionCode]
- +[UAFConfiguration autoAssetFeatureEnabled:]
- +[UAFConfiguration trialFeatureEnabled:]
- +[UAFInstrumentationProvider _constructNamespaceStatusEventForNamespace:withClient:]
- +[UAFInstrumentationProvider _constructSelfAssetSet:storeManager:]
- +[UAFInstrumentationProvider _emitAssetDailyStatusEvent:]
- +[UAFInstrumentationProvider _getAssetSource:]
- +[UAFInstrumentationProvider defaultDeviceId]
- +[UAFInstrumentationProvider getDeviceMetadata]
- +[UAFInstrumentationProvider getPersistedDeviceId]
- +[UAFInstrumentationProvider logAvailableAssetDailyStatusWithFeedbackLogger:completion:]
- +[UAFInstrumentationProvider logSubscriptionsStatus]
- +[UAFInstrumentationProvider logUAFAssetSetDailyStatus:assetSetArrived:]
- +[UAFManagedSubscriptions manageXRSubscription:subscribe:]
- +[UAFTrialConversions assetTypeFromNamespaceName:]
- +[UAFTrialConversions namespaceNameFromAssetType:]
- +[UAFTrialUpdateManager checkForOutOfSpace:updateProgress:]
- +[UAFTrialUpdateManager filterOnDemandFactors:namespaceName:trialClient:]
- +[UAFTrialUpdateManager getConcurrentQueue]
- +[UAFTrialUpdateManager getKnownFactors:namespace:knownFactors:onDemandFactors:]
- +[UAFTrialUpdateManager getSerialQueue]
- +[UAFTrialUpdateManager getTrialDownloadStatusForUsages:configurationManager:]
- +[UAFTrialUpdateManager getTrialFactors:configurationManager:includeAllAssetSets:noRemovalNamespaces:assetSetNamespaces:]
- +[UAFTrialUpdateManager isOnDemand:]
- +[UAFTrialUpdateManager isPresent:]
- +[UAFTrialUpdateManager isRemoveAllowed]
- +[UAFTrialUpdateManager isSubscribed:]
- +[UAFTrialUpdateManager sizeFromLevel:]
- +[UAFTrialUpdateManager trialClientWithProject:]
- +[UAFTrialUpdateManager updateNamespaces:missingRolloutsOnly:expensiveNetworking:assetSetNamespaces:updateProgress:]
- +[UAFTrialUpdateManager updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]
- +[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]
- +[UAFTrialUpdateManager updateTrialFromAssetSetUsages:rolloutUpdateMode:expensiveNetworking:storeManager:configurationManager:progress:completion:]
- +[UAFTrialUpdateManager updateTrialFromAssetSetUsages:storeManager:configurationManager:]
- +[UAFTrialUpdateManager updateTrialProject:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]
- +[UAFTrialUpdateProgress getSerialQueue]
- -[TRIClient(UAFTrialClient) UAFFactorLevelsWithNamespaceName:]
- -[TRIClient(UAFTrialClient) UAFLevelForFactor:withNamespaceName:withLanguage:]
- -[TRIClient(UAFTrialClient) _initOnce]
- -[TRIClient(UAFTrialClient) _trialLevelForFactor:withNamespaceName:withLanguage:]
- -[UAFAssetConfiguration getTrialFactorFallbackName:]
- -[UAFAssetConfiguration getTrialFactorName:]
- -[UAFAssetConfiguration setTrialMAAssetType:]
- -[UAFAssetConfiguration setTrialMATargetingTemplate:]
- -[UAFAssetConfiguration setTrialNamespace:]
- -[UAFAssetConfiguration trialMAAssetType]
- -[UAFAssetConfiguration trialMATargetingTemplate]
- -[UAFAssetConfiguration trialNamespace]
- -[UAFAssetExpansion getTrialFactorFallbackName:]
- -[UAFAssetExpansion getTrialFactorName:]
- -[UAFAssetExpansion setTrialFactorFallbackTemplate:]
- -[UAFAssetExpansion setTrialFactorTemplate:]
- -[UAFAssetExpansion trialFactorFallbackTemplate]
- -[UAFAssetExpansion trialFactorTemplate]
- -[UAFAssetSet _createAssetFromTrialInfo:assetName:fallback:validPathOnly:]
- -[UAFAssetSet createAssetFromTrialInfo:assetName:]
- -[UAFAssetSet getTrialAssets]
- -[UAFAssetSet markAssetsPromoted:error:]
- -[UAFAssetSet markAssetsProvisional:error:]
- -[UAFAssetSet namespacesOfAssetNames:error:]
- -[UAFAssetSetConfiguration applyFeatureFlags]
- -[UAFAssetSetConfiguration getTrialAssets:]
- -[UAFAssetSetConfiguration isTrialAvailable]
- -[UAFAssetSetConfiguration setIsTrialAvailable:]
- -[UAFAssetSetConfiguration setTrialProject:]
- -[UAFAssetSetConfiguration trialProject]
- -[UAFAssetSetConsistencyToken initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:bootUUID:]
- -[UAFAssetSetManager assetSetUsagesForSubscribers:storeManager:configurationManager:anyUnknown:]
- -[UAFAssetSetManager subscriptionsForSubscriber:storeManager:]
- -[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]
- -[UAFAssetSetObserver namespaceHasChanged:]
- -[UAFAssetSetObserver namespaceTokens]
- -[UAFAssetSetObserver namespaceUpdateDate]
- -[UAFAssetSetObserver namespacesToIgnore]
- -[UAFAssetSetObserver namespaces]
- -[UAFAssetSetObserver resetNamespacesToIgnore:]
- -[UAFAssetSetObserver setNamespaceTokens:]
- -[UAFAssetSetObserver setNamespaceUpdateDate:]
- -[UAFAssetSetObserver setNamespaces:]
- -[UAFAssetSetObserver setNamespacesToIgnore:]
- -[UAFAssetSetObserver setTrial:]
- -[UAFAssetSetObserver trial]
- -[UAFAssetSetProgress progress:completed:total:status:]
- -[UAFAutoAssetProgress detailedProgressWithStatus]
- -[UAFAutoAssetProgress finished:withStatus:]
- -[UAFAutoAssetProgress initWithAssetSetUsages:configurationManager:detailedProgressWithStatus:]
- -[UAFAutoAssetProgress setDetailedProgressWithStatus:]
- -[UAFConfigurationManager shouldApplyFeatureFlags]
- -[UAFSubscriptionStoreManager _checkDbVersion]
- -[UAFSubscriptionStoreManager _createDbVersionTable]
- -[UAFSubscriptionStoreManager _getSubscription:subscription:]
- -[UAFSubscriptionStoreManager _getSubscriptions:]
- -[UAFSubscriptionStoreManager _subscribeSubscription:subscriptionName:assetSetSubscription:expires:]
- -[UAFSubscriptionStoreManager _unsubscribeSubscription:subscription:]
- -[UAFSubscriptionStoreManager getAllSystemConfiguration]
- -[UAFSubscriptionStoreManager getSubscribers]
- -[UAFSubscriptionStoreManager getSubscription:subscriber:]
- -[UAFSubscriptionStoreManager getSubscriptions:error:]
- -[UAFSubscriptionStoreManager performDbUpgradeToVersion:]
- -[UAFSubscriptionStoreManager subscribe:subscriptions:expires:]
- -[UAFSubscriptionStoreManager unsubscribe:subscriptions:]
- -[UAFTrialUpdateProgress .cxx_destruct]
- -[UAFTrialUpdateProgress completedWork]
- -[UAFTrialUpdateProgress detailedProgressWithStatus]
- -[UAFTrialUpdateProgress factors]
- -[UAFTrialUpdateProgress getFactorProgressKey:factor:]
- -[UAFTrialUpdateProgress initWithTrialFactors:detailedProgressWithStatus:]
- -[UAFTrialUpdateProgress name]
- -[UAFTrialUpdateProgress onDemandFactorsHaveStarted]
- -[UAFTrialUpdateProgress onDemandFactorsStarted]
- -[UAFTrialUpdateProgress outOfSpaceEncountered]
- -[UAFTrialUpdateProgress outOfSpace]
- -[UAFTrialUpdateProgress reportStatus:]
- -[UAFTrialUpdateProgress reportedCompletedWork]
- -[UAFTrialUpdateProgress reportedStatus]
- -[UAFTrialUpdateProgress reportedTotalWork]
- -[UAFTrialUpdateProgress setCompletedWork:]
- -[UAFTrialUpdateProgress setDetailedProgressWithStatus:]
- -[UAFTrialUpdateProgress setFactors:]
- -[UAFTrialUpdateProgress setName:]
- -[UAFTrialUpdateProgress setOnDemandFactorsHaveStarted:]
- -[UAFTrialUpdateProgress setOutOfSpace:]
- -[UAFTrialUpdateProgress setReportedCompletedWork:]
- -[UAFTrialUpdateProgress setReportedStatus:]
- -[UAFTrialUpdateProgress setReportedTotalWork:]
- -[UAFTrialUpdateProgress setStatuses:]
- -[UAFTrialUpdateProgress setTotalWork:]
- -[UAFTrialUpdateProgress statuses]
- -[UAFTrialUpdateProgress summarize]
- -[UAFTrialUpdateProgress totalWork]
- -[UAFTrialUpdateProgress trialFactorFinished:namespace:]
- -[UAFTrialUpdateProgress trialFactorProgress:namespace:fractionCompleted:status:]
- -[UAFTrialUpdateProgress trialFactorStarted:namespace:size:status:]
- -[UAFTrialUpdateProgress updateFinished:]
- -[UAFTrialUpdateProgress updateStarted]
- -[UAFUsageAliasConfiguration getTrialAssets:]
- -[UAFXPCConnection subscriptionsForSubscriber:completion:]
- -[UAFXPCService initWithMachServiceName:]
- -[UAFXPCService initWithXPCListener:]
- -[UAFXPCService subscribeWithConfig:completion:]
- -[UAFXPCService subscriptionsForSubscriber:completion:]
- -[UAFXPCService unsubscribeWithConfig:completion:]
- GCC_except_table19
- GCC_except_table25
- GCC_except_table26
- GCC_except_table29
- GCC_except_table33
- GCC_except_table34
- GCC_except_table39
- GCC_except_table47
- GCC_except_table68
- GCC_except_table74
- GCC_except_table76
- GCC_except_table77
- GCC_except_table86
- _OBJC_CLASS_$_FLLogger
- _OBJC_CLASS_$_SADSchemaSADAvailableAssetDailyStatus
- _OBJC_CLASS_$_SADSchemaSADTrialNamespaceStatus
- _OBJC_CLASS_$_SADSchemaSADTrialRollout
- _OBJC_CLASS_$_SISchemaAsset
- _OBJC_CLASS_$_SISchemaUUID
- _OBJC_CLASS_$_SISchemaVersion
- _OBJC_CLASS_$_SIUtilities
- _OBJC_CLASS_$_TRIAsset
- _OBJC_CLASS_$_TRIDownloadOptions
- _OBJC_CLASS_$_TRIFactor
- _OBJC_CLASS_$_TRIFactorLevel
- _OBJC_CLASS_$_TRIFile
- _OBJC_CLASS_$_TRILevel
- _OBJC_CLASS_$_UAFSchemaUAFAsset
- _OBJC_CLASS_$_UAFSchemaUAFAssetDailyStatusWithDeviceProperties
- _OBJC_CLASS_$_UAFSchemaUAFAssetSet
- _OBJC_CLASS_$_UAFSchemaUAFAssetSetStatus
- _OBJC_CLASS_$_UAFSchemaUAFAssetSetSubscription
- _OBJC_CLASS_$_UAFSchemaUAFAssetSetUsage
- _OBJC_CLASS_$_UAFSchemaUAFAssetSubscriberSubscriptions
- _OBJC_CLASS_$_UAFSchemaUAFAssetUsageAlias
- _OBJC_CLASS_$_UAFSchemaUAFClientEvent
- _OBJC_CLASS_$_UAFSchemaUAFClientEventMetadata
- _OBJC_CLASS_$_UAFSchemaUAFDeviceMetadata
- _OBJC_CLASS_$_UAFSchemaUAFMobileAssetDownloadErrorCodeFrequency
- _OBJC_CLASS_$_UAFTrialUpdateManager
- _OBJC_CLASS_$_UAFTrialUpdateProgress
- _OBJC_IVAR_$_UAFAssetConfiguration._trialMAAssetType
- _OBJC_IVAR_$_UAFAssetConfiguration._trialMATargetingTemplate
- _OBJC_IVAR_$_UAFAssetConfiguration._trialNamespace
- _OBJC_IVAR_$_UAFAssetExpansion._trialFactorFallbackTemplate
- _OBJC_IVAR_$_UAFAssetExpansion._trialFactorTemplate
- _OBJC_IVAR_$_UAFAssetSet._assetNameToTrial
- _OBJC_IVAR_$_UAFAssetSet._client
- _OBJC_IVAR_$_UAFAssetSetConfiguration._isTrialAvailable
- _OBJC_IVAR_$_UAFAssetSetConfiguration._trialProject
- _OBJC_IVAR_$_UAFAssetSetObserver._namespaceTokens
- _OBJC_IVAR_$_UAFAssetSetObserver._namespaceUpdateDate
- _OBJC_IVAR_$_UAFAssetSetObserver._namespaces
- _OBJC_IVAR_$_UAFAssetSetObserver._namespacesToIgnore
- _OBJC_IVAR_$_UAFAssetSetObserver._trial
- _OBJC_IVAR_$_UAFAutoAssetProgress._detailedProgressWithStatus
- _OBJC_IVAR_$_UAFTrialUpdateProgress._completedWork
- _OBJC_IVAR_$_UAFTrialUpdateProgress._detailedProgressWithStatus
- _OBJC_IVAR_$_UAFTrialUpdateProgress._factors
- _OBJC_IVAR_$_UAFTrialUpdateProgress._name
- _OBJC_IVAR_$_UAFTrialUpdateProgress._onDemandFactorsHaveStarted
- _OBJC_IVAR_$_UAFTrialUpdateProgress._outOfSpace
- _OBJC_IVAR_$_UAFTrialUpdateProgress._reportedCompletedWork
- _OBJC_IVAR_$_UAFTrialUpdateProgress._reportedStatus
- _OBJC_IVAR_$_UAFTrialUpdateProgress._reportedTotalWork
- _OBJC_IVAR_$_UAFTrialUpdateProgress._statuses
- _OBJC_IVAR_$_UAFTrialUpdateProgress._totalWork
- _OBJC_METACLASS_$_UAFTrialUpdateManager
- _OBJC_METACLASS_$_UAFTrialUpdateProgress
- _UAFLogContextTrialCategory
- __MapTrialProjectsToNamespacesFromConfig
- __OBJC_$_CATEGORY_CLASS_METHODS_TRIClient_$_UAFTrialClient
- __OBJC_$_CATEGORY_INSTANCE_METHODS_TRIClient_$_UAFTrialClient
- __OBJC_$_CATEGORY_TRIClient_$_UAFTrialClient
- __OBJC_$_CLASS_METHODS_UAFTrialUpdateManager
- __OBJC_$_CLASS_METHODS_UAFTrialUpdateProgress
- __OBJC_$_INSTANCE_METHODS_UAFTrialUpdateProgress
- __OBJC_$_INSTANCE_VARIABLES_UAFTrialUpdateProgress
- __OBJC_$_PROP_LIST_UAFTrialUpdateProgress
- __OBJC_CLASS_RO_$_UAFTrialUpdateManager
- __OBJC_CLASS_RO_$_UAFTrialUpdateProgress
- __OBJC_METACLASS_RO_$_UAFTrialUpdateManager
- __OBJC_METACLASS_RO_$_UAFTrialUpdateProgress
- __ProjectToNamespacesMapping
- ___103+[UAFAutoAssetManager stageAssetsWithSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:]_block_invoke
- ___106-[UAFAssetSetObserver initWithAssetSet:ignoreMobileAssetStartup:configurationDirURLs:queue:updateHandler:]_block_invoke.305
- ___126+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:userInitiated:]_block_invoke
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.433
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.434
- ___135-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke
- ___135-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_2
- ___135-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_3
- ___135-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_4
- ___135-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_5
- ___135-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_6
- ___135-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_7
- ___135-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_8
- ___147+[UAFTrialUpdateManager updateTrialFromAssetSetUsages:rolloutUpdateMode:expensiveNetworking:storeManager:configurationManager:progress:completion:]_block_invoke
- ___170+[UAFTrialUpdateManager updateTrialProject:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]_block_invoke
- ___173+[UAFTrialUpdateManager updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]_block_invoke
- ___173+[UAFTrialUpdateManager updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]_block_invoke.296
- ___173+[UAFTrialUpdateManager updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]_block_invoke.298
- ___173+[UAFTrialUpdateManager updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]_block_invoke.299
- ___173+[UAFTrialUpdateManager updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]_block_invoke.300
- ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke
- ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke.312
- ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke.315
- ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_2
- ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_2.313
- ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_3
- ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_4
- ___27-[UAFXPCService runUpdates]_block_invoke.341
- ___29-[UAFAssetSet getTrialAssets]_block_invoke
- ___31-[UAFXPCConnection _connection]_block_invoke.284
- ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke.303
- ___38-[TRIClient(UAFTrialClient) _initOnce]_block_invoke
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.391
- ___39+[UAFTrialUpdateManager getSerialQueue]_block_invoke
- ___39-[UAFTrialUpdateProgress updateStarted]_block_invoke
- ___40+[UAFTrialUpdateProgress getSerialQueue]_block_invoke
- ___41-[UAFTrialUpdateProgress updateFinished:]_block_invoke
- ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.376
- ___42-[UAFXPCConnection diagnosticInformation:]_block_invoke.287
- ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.340
- ___43+[UAFTrialUpdateManager getConcurrentQueue]_block_invoke
- ___44-[UAFAutoAssetProgress finished:withStatus:]_block_invoke
- ___45+[UAFInstrumentationProvider defaultDeviceId]_block_invoke
- ___45-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke.330
- ___45-[UAFAutoAssetSet mapAsset:queue:completion:]_block_invoke.328
- ___45-[UAFSubscriptionStoreManager getSubscribers]_block_invoke
- ___46+[UAFCommonUtilities resetAutoAsset:userInfo:]_block_invoke_2
- ___46-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke.322
- ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke.286
- ___47-[UAFTrialUpdateProgress outOfSpaceEncountered]_block_invoke
- ___48+[UAFAssetSetManager shouldConfigure:newUsages:]_block_invoke
- ___48-[UAFAssetUtilities _assistantPreferencesUpdate]_block_invoke.335
- ___48-[UAFTrialUpdateProgress onDemandFactorsStarted]_block_invoke
- ___49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke.290
- ___50-[UAFAutoAssetSet invalidateWithQueue:completion:]_block_invoke.308
- ___51-[UAFXPCConnection operationWithConfig:completion:]_block_invoke.286
- ___52+[UAFInstrumentationProvider logSubscriptionsStatus]_block_invoke
- ___53+[UAFAutoAssetManager removeAutoAssetSet:completion:]_block_invoke
- ___53-[UAFAssetUtilities _downloadSiriAssetsOverCellular:]_block_invoke.325
- ___54-[UAFSubscriptionStoreManager getSubscriptions:error:]_block_invoke
- ___55-[UAFAssetSetProgress progress:completed:total:status:]_block_invoke
- ___56-[UAFSubscriptionStoreManager getAllSystemConfiguration]_block_invoke
- ___56-[UAFTrialUpdateProgress trialFactorFinished:namespace:]_block_invoke
- ___56-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke.289
- ___57+[UAFInstrumentationProvider _emitAssetDailyStatusEvent:]_block_invoke
- ___57-[UAFSubscriptionStoreManager performDbUpgradeToVersion:]_block_invoke
- ___57-[UAFSubscriptionStoreManager unsubscribe:subscriptions:]_block_invoke
- ___58-[UAFSubscriptionStoreManager getSubscription:subscriber:]_block_invoke
- ___58-[UAFXPCConnection subscriptionsForSubscriber:completion:]_block_invoke
- ___58-[UAFXPCConnection subscriptionsForSubscriber:completion:]_block_invoke.291
- ___58-[UAFXPCConnection subscriptionsForSubscriber:completion:]_block_invoke_2
- ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.398
- ___60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke
- ___60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke.361
- ___62-[UAFAssetSetManager subscriptionsForSubscriber:storeManager:]_block_invoke
- ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke.311
- ___63+[UAFAssetSetManager subscribe:subscriptions:queue:completion:]_block_invoke
- ___63+[UAFAssetSetManager subscribe:subscriptions:queue:completion:]_block_invoke.302
- ___63+[UAFAssetSetManager subscribe:subscriptions:queue:completion:]_block_invoke.305
- ___63+[UAFAssetSetManager subscribe:subscriptions:queue:completion:]_block_invoke_2
- ___63-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke.307
- ___63-[UAFSubscriptionStoreManager subscribe:subscriptions:expires:]_block_invoke
- ___65+[UAFAssetSetManager unsubscribe:subscriptions:queue:completion:]_block_invoke
- ___65+[UAFAssetSetManager unsubscribe:subscriptions:queue:completion:]_block_invoke_2
- ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.304
- ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke.326
- ___67-[UAFTrialUpdateProgress trialFactorStarted:namespace:size:status:]_block_invoke
- ___75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke.305
- ___76+[UAFAutoAssetManager releaseIncompatibleAssetSet:specifiers:configuration:]_block_invoke
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.311
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.322
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.324
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke_2.325
- ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke.294
- ___81-[UAFTrialUpdateProgress trialFactorProgress:namespace:fractionCompleted:status:]_block_invoke
- ___88+[UAFInstrumentationProvider logAvailableAssetDailyStatusWithFeedbackLogger:completion:]_block_invoke
- ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.415
- ___89+[UAFTrialUpdateManager updateTrialFromAssetSetUsages:storeManager:configurationManager:]_block_invoke
- ___90+[TRIClient(UAFTrialClient) _cachedLevelForFactorAnyLanguage:withNamespaceName:withCache:]_block_invoke
- ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.414
- ___94+[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke
- ___94+[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke.314
- ___94+[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke_2
- ___94+[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke_3
- ___94+[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke_4
- ___94+[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke_5
- ___96+[UAFAssetSetManager unsubscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke
- ___96+[UAFAssetSetManager unsubscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke.319
- ___96+[UAFAssetSetManager unsubscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke_2
- ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.446
- ____RegisterXPCActivity_block_invoke.291
- ___block_descriptor_40_e8_32r_e24_v32?0"NSArray"8Q16^B24lr32l8
- ___block_descriptor_40_e8_32s_e14_v32?0Q8Q16Q24ls32l8
- ___block_descriptor_40_e8_32s_e24_v32?0"NSArray"8Q16^B24ls32l8
- ___block_descriptor_48_e8_32s40r_e29_v24?0"NSArray"8"NSError"16ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e35_v32?0"NSString"8"TRILevel"16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_48_e8_32s_e42_v32?0"NSString"8"NSArray"16"NSError"24ls32l8
- ___block_descriptor_52_e8_32s40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_56_e8_32s40bs48bs_e17_v40?0d8Q16Q24Q32ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48r_e20_v20?0B8"NSError"12lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e32_v32?0"NSString"8"NSSet"16^B24ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48s_e11_v24?0d8Q16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_58_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40bs48r_e8_v16?0Q8lr48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56w_e38_v16?0"<TRINamespaceUpdateProtocol>"8lw56l8s32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e20_v20?0B8"NSError"12lr56l8s32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e5_i8?0ls32l8r56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e5_B8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_65_e8_32s40s48bs56r_e5_v8?0ls32l8r56l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls32l8s64l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e20_v20?0B8"NSError"12lr64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_73_e8_32s40s48s56s64r_e5_v8?0ls32l8r64l8s40l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32bs40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_80_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_81_e8_32s40s48s56bs64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_98_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.280
- ___block_literal_global.292
- ___block_literal_global.294
- ___block_literal_global.295
- ___block_literal_global.296
- ___block_literal_global.299
- ___block_literal_global.301
- ___block_literal_global.305
- ___block_literal_global.307
- ___block_literal_global.317
- ___block_literal_global.352
- ___block_literal_global.354
- ___block_literal_global.368
- ___block_literal_global.388
- ___block_literal_global.389
- ___block_literal_global.394
- ___block_literal_global.400
- ___levelFromAsset_block_invoke
- __initOnce.initOnce
- _createError
- _factorLevelsFromAssets
- _getpwuid
- _kUAFPolicyForceUpdateNamespaces
- _kUAFPolicyUpdateNamespaces
- _kUAFProgressTrial
- _kUAFTrialFactorFractionCompleted
- _kUAFTrialFactorSize
- _kUAFTrialUpdate
- _levelHasValidPath
- _mach_absolute_time
- _newFactorLevelWithLevel
- _objc_msgSend$_addFactorLevelsToCache:namespaceName:withFactorLevelsCache:withLevelCache:
- _objc_msgSend$_addLevelToCache:namespaceName:factorName:withCache:
- _objc_msgSend$_cachedLevelForFactor:withNamespaceName:withLanguage:withCache:
- _objc_msgSend$_checkDbVersion
- _objc_msgSend$_constructNamespaceStatusEventForNamespace:withClient:
- _objc_msgSend$_constructSelfAssetSet:storeManager:
- _objc_msgSend$_createAssetFromTrialInfo:assetName:fallback:validPathOnly:
- _objc_msgSend$_createDbVersionTable
- _objc_msgSend$_emitAssetDailyStatusEvent:
- _objc_msgSend$_factoryFactorLevelsWithNamespaceName:onDemandClient:
- _objc_msgSend$_getSubscription:subscription:
- _objc_msgSend$_getSubscriptions:
- _objc_msgSend$_initOnce
- _objc_msgSend$_levelKeyForCache:withFactorName:withLanguage:
- _objc_msgSend$_logDailyStatusEventForAssetSetArrived:entries:assetSetArrived:
- _objc_msgSend$_queryAssetsWithNamespaceName:factorName:language:isRoot:withError:
- _objc_msgSend$_rootFactorLevelsWithNamespaceName:
- _objc_msgSend$_subscribeSubscription:subscriptionName:assetSetSubscription:expires:
- _objc_msgSend$_subscriptionDiffersFromDB:subscriber:error:
- _objc_msgSend$_trialLevelForFactor:withNamespaceName:withLanguage:
- _objc_msgSend$_unsubscribeSubscription:subscription:
- _objc_msgSend$addAssetSetStatus:
- _objc_msgSend$addAssets:
- _objc_msgSend$addNamespaceStatus:
- _objc_msgSend$applyFeatureFlags
- _objc_msgSend$asset
- _objc_msgSend$assetSetUsagesForSubscribers:storeManager:configurationManager:anyUnknown:
- _objc_msgSend$assetSource
- _objc_msgSend$assetTypeFromNamespaceName:
- _objc_msgSend$autoAssetExistsWithEntries:
- _objc_msgSend$autoAssetFeatureEnabled:
- _objc_msgSend$capitalizedString
- _objc_msgSend$checkForOutOfSpace:updateProgress:
- _objc_msgSend$compatibilityVersionWithNamespaceName:
- _objc_msgSend$configureAssetDelivery:configurationManager:lockIfUnchanged:subscriptions:assetSetUsages:userInitiated:
- _objc_msgSend$configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:userInitiated:
- _objc_msgSend$convertLanguageCodeToSchemaLocale:
- _objc_msgSend$createAssetFromTrialInfo:assetName:
- _objc_msgSend$deploymentId
- _objc_msgSend$deregisterUpdateWithToken:
- _objc_msgSend$dictionaryWithObjects:forKeys:
- _objc_msgSend$disableAssetRemoval
- _objc_msgSend$distantPast
- _objc_msgSend$doubleValue
- _objc_msgSend$downloadLevelsForFactors:withNamespace:queue:options:progress:completion:
- _objc_msgSend$factor
- _objc_msgSend$factorLevelsWithNamespaceName:
- _objc_msgSend$factorPackId
- _objc_msgSend$factors
- _objc_msgSend$fileValue
- _objc_msgSend$filterOnDemandFactors:namespaceName:trialClient:
- _objc_msgSend$finished:withStatus:
- _objc_msgSend$firstObject
- _objc_msgSend$fromContentsOfURL:applyFeatureFlags:error:
- _objc_msgSend$fromPreSoftwareUpdateStaging
- _objc_msgSend$getAllSystemConfiguration
- _objc_msgSend$getDeviceMetadata
- _objc_msgSend$getEntitledTrialAssets:usages:
- _objc_msgSend$getFactorProgressKey:factor:
- _objc_msgSend$getKnownFactors:namespace:knownFactors:onDemandFactors:
- _objc_msgSend$getPWUID:
- _objc_msgSend$getPersistedDeviceId
- _objc_msgSend$getSubscribers
- _objc_msgSend$getSubscription:subscriber:
- _objc_msgSend$getSubscriptions:error:
- _objc_msgSend$getTrialAssets
- _objc_msgSend$getTrialAssets:
- _objc_msgSend$getTrialDownloadStatusForUsages:configurationManager:
- _objc_msgSend$getTrialFactorFallbackName:
- _objc_msgSend$getTrialFactorName:
- _objc_msgSend$getTrialFactors:configurationManager:includeAllAssetSets:noRemovalNamespaces:assetSetNamespaces:
- _objc_msgSend$hasAsset
- _objc_msgSend$hasAssetId
- _objc_msgSend$hasFactor
- _objc_msgSend$hasLevel
- _objc_msgSend$immediateDownloadForNamespaceNames:allowExpensiveNetworking:error:
- _objc_msgSend$initWithAllowsCellular:discretionaryBehavior:
- _objc_msgSend$initWithAssetSetUsages:configurationManager:detailedProgressWithStatus:
- _objc_msgSend$initWithNSUUID:
- _objc_msgSend$initWithTrialFactors:detailedProgressWithStatus:
- _objc_msgSend$initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:bootUUID:
- _objc_msgSend$initWithXPCListener:
- _objc_msgSend$intersectsSet:
- _objc_msgSend$isOnDemand
- _objc_msgSend$isOnDemand:
- _objc_msgSend$isPresent:
- _objc_msgSend$isRemoveAllowed
- _objc_msgSend$isSubscribed:
- _objc_msgSend$level
- _objc_msgSend$localizedFailureReason
- _objc_msgSend$logAvailableAssetDailyStatusWithFeedbackLogger:completion:
- _objc_msgSend$logSubscriptionsStatus
- _objc_msgSend$logUAFAssetSetDailyStatus:assetSetArrived:
- _objc_msgSend$namespaceHasChanged:
- _objc_msgSend$namespaceIdFromName:
- _objc_msgSend$namespacesOfAssetNames:error:
- _objc_msgSend$numberWithDouble:
- _objc_msgSend$objectAtIndex:
- _objc_msgSend$onDemandFactorsStarted
- _objc_msgSend$outOfSpaceEncountered
- _objc_msgSend$performDbUpgradeToVersion:
- _objc_msgSend$progress:completed:total:status:
- _objc_msgSend$promoteFactorsForNamespace:error:
- _objc_msgSend$removeAutoAssetSet:completion:
- _objc_msgSend$removeLevelsForFactors:withNamespace:queue:completion:
- _objc_msgSend$reportSiriInstrumentationEvent:forBundleID:completion:
- _objc_msgSend$resetNamespacesToIgnore:
- _objc_msgSend$rolloutId
- _objc_msgSend$rolloutIdentifiersWithNamespaceName:
- _objc_msgSend$setAliasName:
- _objc_msgSend$setAliasValue:
- _objc_msgSend$setAsset:
- _objc_msgSend$setAssetDownloadSizeInBytes:
- _objc_msgSend$setAssetId:
- _objc_msgSend$setAssetLocale:
- _objc_msgSend$setAssetName:
- _objc_msgSend$setAssetSetId:
- _objc_msgSend$setAssetSetIndices:
- _objc_msgSend$setAssetSetName:
- _objc_msgSend$setAssetSetUsages:
- _objc_msgSend$setAssetSource:
- _objc_msgSend$setAssetSpecifier:
- _objc_msgSend$setAssetUnarchivedSizeInBytes:
- _objc_msgSend$setAssetVersion:
- _objc_msgSend$setAssets:
- _objc_msgSend$setAvailableAssetDailyStatus:
- _objc_msgSend$setDeployment:
- _objc_msgSend$setDeviceId:
- _objc_msgSend$setDeviceMetadata:
- _objc_msgSend$setDeviceType:
- _objc_msgSend$setDirectoryValue:
- _objc_msgSend$setEventMetadata:
- _objc_msgSend$setFactor:
- _objc_msgSend$setFactorPack:
- _objc_msgSend$setFactorsProvisionalForNamespace:error:
- _objc_msgSend$setFromPreSoftwareUpdateStaging:
- _objc_msgSend$setHasAlias:
- _objc_msgSend$setHasId_p:
- _objc_msgSend$setHasLevel:
- _objc_msgSend$setHasPath:
- _objc_msgSend$setInputLocale:
- _objc_msgSend$setIsAssetPathValid:
- _objc_msgSend$setIsOnDemand:
- _objc_msgSend$setLatestAtomicInstance:autoAssetSet:
- _objc_msgSend$setLevel:
- _objc_msgSend$setMajor:
- _objc_msgSend$setMetadata:
- _objc_msgSend$setMinor:
- _objc_msgSend$setMobileAssetDownloadErrorCode:
- _objc_msgSend$setMobileAssetDownloadErrorCodeFrequencys:
- _objc_msgSend$setName:
- _objc_msgSend$setNamespaceCompatabilityVersion:
- _objc_msgSend$setNamespaceId:
- _objc_msgSend$setNamespaceName:
- _objc_msgSend$setNanoSecondsSinceLastBoot:
- _objc_msgSend$setOnDemandFactorsHaveStarted:
- _objc_msgSend$setOutOfSpace:
- _objc_msgSend$setPatch:
- _objc_msgSend$setPath:
- _objc_msgSend$setPrerelease:
- _objc_msgSend$setProgramCode:
- _objc_msgSend$setRollout:
- _objc_msgSend$setRolloutId:
- _objc_msgSend$setStatusReason:
- _objc_msgSend$setSubscriberName:
- _objc_msgSend$setSubscriptionName:
- _objc_msgSend$setSubscriptions:
- _objc_msgSend$setSystemBuild:
- _objc_msgSend$setTimesOccurred:
- _objc_msgSend$setTrialNamespace:
- _objc_msgSend$setType:
- _objc_msgSend$setUafAssetDailyStatus:
- _objc_msgSend$setUafAssetSets:
- _objc_msgSend$setUafAssetSubscriptions:
- _objc_msgSend$setUafId:
- _objc_msgSend$setUsageAliases:
- _objc_msgSend$setUsageName:
- _objc_msgSend$setUsageValue:
- _objc_msgSend$sharedLoggerWithPersistenceConfiguration:
- _objc_msgSend$shouldApplyFeatureFlags
- _objc_msgSend$shouldConfigure:newUsages:
- _objc_msgSend$size
- _objc_msgSend$sizeFromLevel:
- _objc_msgSend$stageAssetsWithSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:
- _objc_msgSend$statusOfDownloadForFactors:withNamespace:token:queue:progress:completion:
- _objc_msgSend$subscribe:subscriptions:expires:
- _objc_msgSend$subscribe:subscriptions:storeManager:configurationManager:userInitiated:
- _objc_msgSend$subscribeWithConfig:completion:
- _objc_msgSend$subscriptionsForSubscriber:completion:
- _objc_msgSend$subscriptionsForSubscriber:storeManager:
- _objc_msgSend$timeIntervalSinceDate:
- _objc_msgSend$trialFactorFallbackTemplate
- _objc_msgSend$trialFactorFinished:namespace:
- _objc_msgSend$trialFactorProgress:namespace:fractionCompleted:status:
- _objc_msgSend$trialFactorStarted:namespace:size:status:
- _objc_msgSend$trialFactorTemplate
- _objc_msgSend$trialFeatureEnabled:
- _objc_msgSend$trialMAAssetType
- _objc_msgSend$unsubscribe:subscriptions:
- _objc_msgSend$unsubscribe:subscriptions:queue:completion:
- _objc_msgSend$unsubscribe:subscriptions:storeManager:configurationManager:userInitiated:
- _objc_msgSend$unsubscribeWithConfig:completion:
- _objc_msgSend$updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:
- _objc_msgSend$updateCount
- _objc_msgSend$updateNamespaces:missingRolloutsOnly:expensiveNetworking:assetSetNamespaces:updateProgress:
- _objc_msgSend$updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:
- _objc_msgSend$updateStarted
- _objc_msgSend$updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:
- _objc_msgSend$updateTrialFromAssetSetUsages:rolloutUpdateMode:expensiveNetworking:storeManager:configurationManager:progress:completion:
- _objc_msgSend$updateTrialFromAssetSetUsages:storeManager:configurationManager:
- _objc_msgSend$updateTrialProject:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:
- _objc_msgSend$uppercaseLetterCharacterSet
- _objc_msgSend$valueForKey:
- _objc_msgSend$wrapAsAnyEvent
CStrings:
+ "            BEGIN EXCLUSIVE TRANSACTION;             CREATE TABLE IF NOT EXISTS Subscriptions_v2 (k0 TEXT NOT NULL, k1 TEXT NOT NULL, k2 BLOB, k3 REAL, k4 TEXT NOT NULL, k5 REAL);             INSERT INTO Subscriptions_v2 (k0, k1, k2, k3, k4, k5) SELECT k0, k1, k2, k3, '%@', %f FROM Subscriptions;             DROP TABLE Subscriptions;             ALTER TABLE Subscriptions_v2 RENAME TO Subscriptions;             CREATE UNIQUE INDEX IF NOT EXISTS subscriptionIndex on Subscriptions (k0, k1, k4);             CREATE TABLE IF NOT EXISTS UserInformation (k0 TEXT PRIMARY KEY NOT NULL, k1 REAL, k2 TEXT NOT NULL);             INSERT OR REPLACE INTO UserInformation (k0, k1, k2) VALUES ( '%@', %f, '%@' );             COMMIT;"
+ "%08X"
+ "%s #settings Download Siri assets for language:%{public}@ cellular:%d"
+ "%s #settings Download legacy Siri assets for language:%{public}@ cellular:%d"
+ "%s #settings download XPC"
+ "%s #settings download cellular XPC"
+ "%s #settings download dictation XPC"
+ "%s #settings service resumed"
+ "%s #settings service suspended"
+ "%s %{public}@"
+ "%s %{public}@: Could not initialize auto asset set %{public}@ : %{public}@"
+ "%s %{public}@: Could not load asset set %{public}@ as _autoAssetSetStatus is unexpectedly nil"
+ "%s %{public}@: Could not load asset set %{public}@ as autoAssets is unexpectedly nil"
+ "%s %{public}@: Could not lock asset set %{public}@ with atomic instance %{public}@: %{public}@"
+ "%s %{public}@: Locked asset set %{public}@ atomic instance %{public}@"
+ "%s API MISUSE: Unsupported call subcriber = '%{public}@' and user is nil"
+ "%s API MISUSE: subscriptionName provided without a subscriber"
+ "%s Adding subscription %{public}@ for subscriber %{public}@ for user %@"
+ "%s Already unsubscribed for user '%@', subscriber '%{public}@', subscriptions '%{public}@'"
+ "%s Asset Set '%@' is not a string"
+ "%s Asset set %{public}@ has no configuration"
+ "%s Asset set %{public}@ has no metadata asset, skipping"
+ "%s Asset set configuration error %{public}@ metadata asset defined but not found"
+ "%s Auto asset set %{public}@ has expected specifiers after inhibiting removal %{public}@"
+ "%s Auto asset set %{public}@ is %{public}@ and has expected specifiers %{public}@"
+ "%s AutoAssetType for Asset \"%@\" is invalid"
+ "%s Beginning expiration removal of %@"
+ "%s Beginning user expiration"
+ "%s Beginning user validation"
+ "%s Binding creation field to the write subscription sql query failed for Subscriber: '%{public}@', SubscriptionName: '%@', User: '%@' SQLite error: %d (%s, Extended: %d)"
+ "%s Binding date to UserInformation: '%@' SQLite error: %d (%s, Extended: %d)"
+ "%s Binding node to UserInformation: '%@' SQLite error: %d (%s, Extended: %d)"
+ "%s Binding of subscriber name failed in remove subscription query for User: '%@', Subscriber: '%{public}@', Subscription: '%{public}@' SQLite error: %d (%s, Extended: %d)"
+ "%s Binding of subscription name failed in remove subscription query for User: '%@', Subscriber: '%{public}@', Subscription: '%{public}@' SQLite error: %d (%s, Extended: %d)"
+ "%s Binding of user failed in remove subscription query for user '%@', Subscriber: '%{public}@', Subscription: '%{public}@' SQLite error: %d (%s, Extended: %d)"
+ "%s Binding of user failed: '%@' SQLite error: %d (%s, Extended: %d)"
+ "%s Binding subscription name to the get subscriptions query failed for Subscriber: '%{public}@' and user: '%@' SQLite error: %d (%s, Extended: %d)"
+ "%s Binding user to UserInformation: '%@' SQLite error: %d (%s, Extended: %d)"
+ "%s Binding user to the get subscriptions query failed for Subscriber: '%{public}@' and user: '%@' SQLite error: %d (%s, Extended: %d)"
+ "%s Binding user to the get subscriptions query failed for user: '%@' SQLite error: %d (%s, Extended: %d)"
+ "%s Binding user to the write subscription sql query failed for Subscriber: %{public}@, SubscriptionName: '%@', user: '%@' SQLite error: %d (%s, Extended: %d)"
+ "%s Can't log asset set download event as this system doesn't support Biome."
+ "%s Can't log daily asset status as this system doesn't support Biome."
+ "%s Can't log download trigger event with language as this system doesn't support SiriAnalytics."
+ "%s Cannot invalidate token with no atomic instance and roots installed: '%{public}@'"
+ "%s Changed subscriptions for user: '%@', subscriber: '%{public}@': '%{public}@'"
+ "%s Changing subscriptions for user: '%@', subscriber: '%{public}@': '%{public}@'"
+ "%s Completed migration of all subscriptions for user '%@', configuring"
+ "%s Completed migration of subscriptions for user '%@', migrating system subscriptions"
+ "%s Completed proxying '%{public}@' request on behalf of pid %d"
+ "%s Completed proxying request on behalf of pid %d"
+ "%s Completing removal of user '%@' with: %{public}@"
+ "%s Configuration manager: %{public}@: Need to configure following asset sets: %{public}@"
+ "%s Configuring asset set %{public}@ for minimal specifiers"
+ "%s Consistency token  has no asset set name: %{public}@"
+ "%s Could not create new subscription database: %d"
+ "%s Could not create platform asset subscription"
+ "%s Could not determine console user, trying via XPC"
+ "%s Could not determine console user, trying with XPC"
+ "%s Could not determine current user, falling back to XPC: %{public}@"
+ "%s Could not determine current user: %{public}@"
+ "%s Could not determine if '%@' is system user, skipping: %{public}@"
+ "%s Could not determine system user, failing to create platform subscription: %{public}@"
+ "%s Could not determine user: %{public}@"
+ "%s Could not find user: %{public}@"
+ "%s Could not get subscriptions for %@ subscriber %{public}@: %{public}@"
+ "%s Could not get subscriptions for User: '%@', Subscriber: '%{public}@': %{public}@"
+ "%s Could not get subscriptions: %{public}@"
+ "%s Could not get system user: %{public}@"
+ "%s Could not get valid nodes: %{public}@"
+ "%s Could not lookup console user"
+ "%s Could not move existing database aside"
+ "%s Could not read lastSeen date SQLite error: %d (%s, Extended: %d)"
+ "%s Could not read nodeName SQLite error: %d (%s, Extended: %d)"
+ "%s Could not retrieve all subscriptions: %d"
+ "%s Could not retrieve all subscriptions: %{public}@"
+ "%s Could not retrieve all user subscriptions: %{public}@"
+ "%s Could not retrieve current user: %@"
+ "%s Could not retrieve homedir: %{public}@"
+ "%s Could not retrieve subscription for user '%@', subscriber '%{public}@', subscription '%{public}@': %{public}@"
+ "%s Could not retrieve subscriptions, falling back to XPC: %{public}@"
+ "%s Could not retrieve valid local users for %@: %{public}@"
+ "%s Could not set database version after recreation"
+ "%s Couldn't upgrade the database even after %d attempts, moving database aside and creating new"
+ "%s Current boot UUID is empty when creating consistency token for asset set %{public}@"
+ "%s Current process cannot access %{public}@ XPC endpoint.  Falling back to proxying through old endpoint.  Please update entitlements/sandbox to allow access to %{public}@ XPC endpoint."
+ "%s Current process is RB managed, acquiring assertion"
+ "%s Database in need of upgrade.  Attempting DB upgrade."
+ "%s Denying open due to upgrade failure: %d"
+ "%s Denying open due to version mismatch, %d vs %d"
+ "%s Denying removal of unused asset sets due to inhibiting asset removal"
+ "%s Denying subscription due to exceeding usage limits for subscriber \"%{public}@\""
+ "%s Detected non-UI build. Setting inhibitremoval to NO."
+ "%s Device doesn't support PASDeviceState. Performing database upgrade check"
+ "%s Discovered newer instance of %{public}@: %{public}@ vs %{public}@, XPC'ing to UAF service to lock"
+ "%s Emitted DailyStatusEvent message for asset set: %{public}@"
+ "%s Emitted scheduled AvailableAssetDailyStatus message"
+ "%s Emitting asset set state CA event for %{public}@"
+ "%s Emitting asset set state CA event for specifier: %{public}@ with version: %{public}@ from asset set: %{public}@"
+ "%s End of user cleanup"
+ "%s Error binding read subscriber for user '%@', subscriber '%{public}@', subscription '%{public}@' SQLite error: %d (%s, Extended: %d)"
+ "%s Error binding read subscription for user '%@', subscriber '%{public}@', subscription '%{public}@' SQLite error: %d (%s, Extended: %d)"
+ "%s Error binding read user for '%@' SQLite error: %d (%s, Extended: %d)"
+ "%s Error binding read user for user '%@', subscriber '%{public}@', subscription '%{public}@' SQLite error: %d (%s, Extended: %d)"
+ "%s Error deleting existing entries SQLite error: %d (%s, Extended: %d)"
+ "%s Error executing SQL statement during %{public}@, SQLite error: %d (%s, Extended: %d)"
+ "%s Error executing read UserInformation key for '%@' SQLite error: %d (%s, Extended: %d)"
+ "%s Error executing read subscription for user '%@', subscriber '%{public}@', subscription '%{public}@' SQLite error: %d (%s, Extended: %d)"
+ "%s Error finding uid: %d: %{public}@"
+ "%s Error getting all system subscriptions for migration: %{public}@"
+ "%s Error invalidating assertion: %{public}@"
+ "%s Error removing %@:%{public}@subscriber:%{public}@subscriptionNames"
+ "%s Error retrieving all subscriptions: %@"
+ "%s Error retrieving all users: %{public}@"
+ "%s Error retrieving current console user: %@"
+ "%s Error retrieving subscribers for user '%@': %{public}@"
+ "%s Error retrieving users older than timeout: %{public}@"
+ "%s Error updating last seen time for current user: %@"
+ "%s Executing set UserInformation failed for: '%@' SQLite error: %d (%s, Extended: %d)"
+ "%s Failed at creating hold subscription: %@"
+ "%s Failed at subscribing: %@"
+ "%s Failed at unsubscribing: %@"
+ "%s Failed to allocate memory for boot session UUID: %{darwin.errno}d"
+ "%s Failed to determine node for user '%@': %{public}@"
+ "%s Failed to get all subscriptions due to error: %{public}@. Stopping staging"
+ "%s Failed to get kern.bootsessionuuid data: %{darwin.errno}d"
+ "%s Failed to get kern.bootsessionuuid length: %{darwin.errno}d"
+ "%s Failed to read user, SQL error: %s"
+ "%s Failed to update storage to reflect subscriptions %{public}@ for subscriber %{public}@ and user: %@"
+ "%s Incrementing DB version to %d"
+ "%s Inhibiting removal of the following specifiers for %{public}@: %{public}@"
+ "%s Local Node is nil"
+ "%s Maintenance task complete"
+ "%s Migrated subscriptions for user '%@'"
+ "%s Migrating subscriptions for user '%@'"
+ "%s Migrating the following additional subscriptions: '%@': '%{public}@': %{public}@"
+ "%s Migration XPC for user '%@' complete with error: %{public}@"
+ "%s No changes found for subscriptions %{public}@ for subscriber %{public}@ and user: %@"
+ "%s No existing subscriptions for user %@ subscriber %{public}@, migrating all subscriptions: %{public}@"
+ "%s No subscription changes for subscriber '%{public}@' and subscriptions '%{public}@' user: '%@'"
+ "%s No subscription changes for subscriptions %{public}@ for subscriber %{public}@ and user: %@"
+ "%s No user received and could not look up user for uid %d: %{public}@"
+ "%s No user received and request is from uid 0, looking up console user"
+ "%s No user received, looking up %d"
+ "%s Node '%@' removed, removing all users from node"
+ "%s Not attempting to update subscriptions for subscriptions %{public}@ for subscriber %{public}@ and user: %@: %{public}@"
+ "%s Not attempting to update subscriptions for user '%@' subscriptions: %{public}@: %{public}@"
+ "%s Not removing user, failed removing all subscriptions"
+ "%s Not scheduling user cleanup task, device is not multiuser"
+ "%s Opened database (%@), database existed:%d, result: %d"
+ "%s Overriding XPC endpoint with environment variable: %{public}@"
+ "%s Overriding mach sandbox check for %{public}@ due to environment variable"
+ "%s Performing %{public}@"
+ "%s Post-Upgrade performing user subscription migration"
+ "%s Posting notification of assetsubscriptiond availability"
+ "%s Process is not entitled to UMUserManager framework."
+ "%s Process is not entitled to UMUserManager framework. %@"
+ "%s Process is not entitled to UMUserManager framework. Cannot determine current user"
+ "%s Ran expireSubscriptions as requested via XPC"
+ "%s Ran setSystemConfigurationForKey:%{public}@ withValue:%{public}@ as requested via XPC"
+ "%s Received '%{public}@' request, proxying to subscription service on behalf of pid %d"
+ "%s Received MAAutoAssetErrorSetAtomicInstanceUnknown from invalidate, suppressing error: '%{public}@'"
+ "%s Received request from pid %d while subscription service disabled"
+ "%s Received request from pid %d, proxying to subscription service"
+ "%s Received request to migrate subscriptions for user '%@'"
+ "%s Received subscription request without user from pid %d for subscriber: %{public}@, could not determine console user"
+ "%s Releasing RB assertion"
+ "%s Removal of subscription failed for User: '%@', Subscriber: '%{public}@', Subscription: '%{public}@' SQLite error: %d (%s, Extended: %d)"
+ "%s Removal of user failed: '%@' SQLite error: %d (%s, Extended: %d)"
+ "%s Remove complete for %@: %{public}@"
+ "%s Removing deleted local user '%@'"
+ "%s Removing expired sub '%{public}@' from subscriber '%{public}@' at '%{public}@' for user '%@'"
+ "%s Removing user '%@'"
+ "%s Removing user '%@' from database"
+ "%s Removing user '%@' from removed node '%@'"
+ "%s Removing user that has no subscriptions: '%@'"
+ "%s Removing users failed SQLite error: %d (%s, Extended: %d)"
+ "%s RunningBoard not available, not pursuing assertion"
+ "%s Scheduling user cleanup task, device is multiuser"
+ "%s Sending notification of DB reset"
+ "%s Sent asset set state CA event for %{public}@"
+ "%s Setting DB version to %d"
+ "%s Setting DB version to %d failed: %d"
+ "%s Starting maintenance task"
+ "%s Subscriptions exist for user '%@' subscriber '%{public}@'"
+ "%s Successfully invalidating empty token: '%{public}@'"
+ "%s System AssetSetUsages: %{public}@, error = %{public}@"
+ "%s System Configuration: %{public}@, error = %{public}@"
+ "%s This system doesn't support Trial. Returning nil."
+ "%s Token '%{public}@' invalidated successfully"
+ "%s Token '%{public}@' invalidated with: %{public}@"
+ "%s Treating empty boot UUID as current when creating consistency token for asset set %{public}@"
+ "%s Unable to acquire RB assertion: %{public}@"
+ "%s Unable to get asset set usages for uid: %d Subscribers: '%{public}@': %{public}@"
+ "%s Unable to get subscriptions for uid: %d Subscriber: '%{public}@' Subscription Name: '%{public}@': %{public}@"
+ "%s Unable to identify current user, falling back to daemon determing user: %@"
+ "%s Unable to identify current user: %@"
+ "%s Underlying error: %u found while logging MA download error for asset set %{public}@ with ID: %{public}@:"
+ "%s Unexpectedly retrieved a nil date from UserInformation"
+ "%s Unexpectedly retrieved a nil node from UserInformation"
+ "%s Unexpectedly retrieved a nil user from UserInformation"
+ "%s Unsubscribed for user '%@', subscriber '%{public}@', subscription '%{public}@' with error: %{public}@"
+ "%s Unsubscribing for user '%@', subscriber '%{public}@', subscription '%{public}@'"
+ "%s Update complete for %@: %{public}@"
+ "%s Updated last seen time for user %@ on node %@ with result: %{public}@"
+ "%s Updated storage to reflect removal of subscriptions %{public}@ for subscriber %{public}@ and user: %@"
+ "%s Updated storage to reflect subscriptions %{public}@ for subscriber %{public}@ and user: %@"
+ "%s Updating last seen time for %@"
+ "%s User '%@' is expired, but system user, keeping"
+ "%s User cleanup complete: %{public}@"
+ "%s User database subscriptions have already migrated, skipping"
+ "%s Using Biome for logging asset status"
+ "%s Using Biome to send asset set event for :%{public}@"
+ "%s Using Biome to send scheduled daily status event"
+ "%s Using XPC endpoint: %{public}@"
+ "%s Using user '%@' for uid %d"
+ "%s Using user '%@' for uid %d querying subscription: %{public}@ for subscriber: %{public}@"
+ "%s XPC received and not subscription service"
+ "%s XPC: Done triggering disabled UAF Post-Upgrade activity"
+ "%s XPC: Done triggering disabled UAF subscription maintenance"
+ "%s XPC: Registering the UserCleanup UAF XPC Activity"
+ "%s complete with error: %{public}@"
+ "%s expireSubscriptions complete"
+ "%s invalidate request for %{public}@"
+ "%s performing db upgrade"
+ "%s readDbVersion prepared statement is null"
+ "%s reset asset sets '%{public}@'"
+ "%s setSystemConfigurationForKey:%{}@ withValue:%{public}@ complete"
+ "("
+ "+[UAFAssetSetConfiguration fromContentsOfURL:error:]"
+ "+[UAFAssetSetManager _subscriptionDiffersFromDB:subscriber:user:error:]"
+ "+[UAFAssetSetManager configureAssetDelivery:configurationManager:lockIfUnchanged:oldSubscriptions:newSubscriptions:userInitiated:]"
+ "+[UAFAssetSetManager getSubscriptions:storeManager:]"
+ "+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke"
+ "+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke_4"
+ "+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke"
+ "+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke_2"
+ "+[UAFAssetSetSubscriptionManager daemonSubscriptionMigration]"
+ "+[UAFAssetSetSubscriptionManager daemonSubscriptionMigration]_block_invoke"
+ "+[UAFAssetSetSubscriptionManager getSubscription:subscriber:user:storeManager:error:]"
+ "+[UAFAssetSetSubscriptionManager getSubscriptions:user:storeManager:error:]"
+ "+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]"
+ "+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke"
+ "+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke_2"
+ "+[UAFAutoAssetManager cacheDeleteStatusChange:]"
+ "+[UAFAutoAssetManager configureAutoAssetsFromNewSubscriptions:oldSubscriptions:configurationManager:lockIfUnchanged:userInitiated:]"
+ "+[UAFAutoAssetManager configureAutoAssetsFromNewSubscriptions:oldSubscriptions:configurationManager:lockIfUnchanged:userInitiated:]_block_invoke"
+ "+[UAFAutoAssetManager findDiffBetweenOldAssetSetUsages:newAssetSetUsages:knownAssetSets:usedAssetSets:configurationManager:]"
+ "+[UAFAutoAssetManager isLatestConsistencyToken:]"
+ "+[UAFAutoAssetManager removeAutoAssetSet:fallbackAlter:]"
+ "+[UAFAutoAssetManager removeUnusedAutoAssetSets:usedAutoAssetSets:]"
+ "+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:fallbackAlter:]"
+ "+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:fallbackAlter:]_block_invoke"
+ "+[UAFAutoAssetManager setMinimalSpecifiers:]"
+ "+[UAFAutoAssetManager stageAssetsWithNewSubscriptions:oldSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:]"
+ "+[UAFBiomeInstrumenter _constructBiomeAssetSet:storeManager:]"
+ "+[UAFBiomeInstrumenter _getBiomeEventDeviceMetadata]"
+ "+[UAFBiomeInstrumenter _getSubscriptionsStatus]_block_invoke"
+ "+[UAFBiomeInstrumenter logAssetSetDownloadEvent:assetSetId:entries:errorCodes:fromPSUS:assetSetArrived:]"
+ "+[UAFBiomeInstrumenter logScheduledDailyAssetStatus]"
+ "+[UAFCommonUtilities copyBootSessionUUID]_block_invoke"
+ "+[UAFCommonUtilities getPWUID:error:]"
+ "+[UAFCommonUtilities getUserDefaultStoragePath]"
+ "+[UAFCoreAnalyticsInstrumenter logUAFAssetSetState:assetSpecifiersAndVersions:]"
+ "+[UAFInstrumentationProvider _emitAssetDailyStatusEvent:autoAssetSet:entries:assetSetArrived:]"
+ "+[UAFInstrumentationProvider _getMADownloadErrors:assetSetName:assetSetID:]"
+ "+[UAFInstrumentationProvider logUAFAssetSetDailyStatus:entries:assetSetArrived:]"
+ "+[UAFManagedSubscriptions managePlatformSubscription]"
+ "+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke"
+ "+[UAFSubscriptionStoreManager sendNotificationDBReset]"
+ "+[UAFSubscriptionStoreManager writeManager]_block_invoke"
+ "+[UAFUser currentConsoleUserWithUID:]"
+ "+[UAFUser pwdNameForUser:error:]"
+ "+[UAFUser pwdUserWithNodeForUID:uid:error:]"
+ "+[UAFUser umCurrentUMUserWithNode:error:]"
+ "+[UAFUser umUserWithDSID:withUid:withError:]"
+ "+[UAFUser validLocalUsers:error:]"
+ "+[UAFUserManager performUserCleanupOnQueue:completion:]_block_invoke_2"
+ "+[UAFUserManager performUserCleanup]"
+ "+[UAFUserManager performUserCleanup]_block_invoke"
+ "+[UAFUserManager removeUser:]"
+ "+[UAFUserManager removeUser:]_block_invoke"
+ "+[UAFUserManager removeUser:]_block_invoke_2"
+ "+[UAFUserManager removeUser:queue:completion:]"
+ "+[UAFUserManager removeUser:queue:completion:]_block_invoke_2"
+ "+[UAFUserManager updateLastSeenForCurrentUserOnQueue:completion:]"
+ "+[UAFUserManager updateLastSeenForUser:queue:completion:]"
+ "+[UAFUserManager updateLastSeenForUser:queue:completion:]_block_invoke_2"
+ "+[UAFXPCActivity maintenanceTaskWithCompletion:]"
+ "+[UAFXPCConnection selectXPCEndpoint]"
+ "-[UAFAssetSetConsistencyToken initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:bootUUID:experimentActivated:]"
+ "-[UAFAssetSetConsistencyToken invalidate:completion:]"
+ "-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke"
+ "-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke_2"
+ "-[UAFAssetSetExperiment initWithExperimentId:assetSpecifiers:]"
+ "-[UAFAssetSetManager assetSetUsagesForSubscribers:storeManager:configurationManager:anyUnknown:error:]"
+ "-[UAFAssetSetManager resetAssetSets:queue:completion:]_block_invoke"
+ "-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]"
+ "-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke"
+ "-[UAFAssetSetManager subscriptions:subscriber:user:storeManager:error:]"
+ "-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]"
+ "-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke"
+ "-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:internalProgress:completion:storeManager:configurationManager:]"
+ "-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:internalProgress:completion:storeManager:configurationManager:]_block_invoke"
+ "-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:internalProgress:completion:storeManager:configurationManager:]_block_invoke_6"
+ "-[UAFAssetSetProgress progress:completed:total:status:context:]"
+ "-[UAFAssetUtilitiesService _downloadSiriAssetsWithCellular:]_block_invoke"
+ "-[UAFAssetUtilitiesService downloadDictationAssetsForLanguage:]"
+ "-[UAFAssetUtilitiesService downloadSiriAssetsOverCellular]"
+ "-[UAFAssetUtilitiesService downloadSiriAssets]"
+ "-[UAFAssetUtilitiesService resume]"
+ "-[UAFAssetUtilitiesService suspend]"
+ "-[UAFAutoAssetProgress finished:withStatus:withError:]_block_invoke"
+ "-[UAFAutoAssetProgress initWithAssetSetUsages:configurationManager:internalProgressWithStatus:]"
+ "-[UAFSubscriptionStoreManager _acquireAssertion]"
+ "-[UAFSubscriptionStoreManager _checkDbVersion:storedVersion:]"
+ "-[UAFSubscriptionStoreManager _getAllSubscriptions:]"
+ "-[UAFSubscriptionStoreManager _getSubscribers:subscribers:]"
+ "-[UAFSubscriptionStoreManager _getSubscription:subscription:user:]"
+ "-[UAFSubscriptionStoreManager _getSubscriptions:user:]"
+ "-[UAFSubscriptionStoreManager _getUser:lastSeen:nodeName:]"
+ "-[UAFSubscriptionStoreManager _isUsageLimitExceeded:]"
+ "-[UAFSubscriptionStoreManager _releaseAssertion]"
+ "-[UAFSubscriptionStoreManager _removeUser:]"
+ "-[UAFSubscriptionStoreManager _setUserLastSeenTime:node:time:]"
+ "-[UAFSubscriptionStoreManager _subscribeSubscription:subscriptionName:assetSetSubscription:expires:user:]"
+ "-[UAFSubscriptionStoreManager _unsubscribeSubscription:subscription:user:]"
+ "-[UAFSubscriptionStoreManager getAllSystemConfiguration:]_block_invoke"
+ "-[UAFSubscriptionStoreManager getUsers:]_block_invoke"
+ "-[UAFSubscriptionStoreManager getUsersOlderThanDate:error:]_block_invoke"
+ "-[UAFSubscriptionStoreManager removeAllUsers]_block_invoke"
+ "-[UAFSubscriptionStoreManager subscribe:subscriptions:user:node:]_block_invoke"
+ "-[UAFXPCConnection expireSubscriptions:]_block_invoke"
+ "-[UAFXPCConnection expireSubscriptions:]_block_invoke_2"
+ "-[UAFXPCConnection initWithDefaultService]"
+ "-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke"
+ "-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke_2"
+ "-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke"
+ "-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke_2"
+ "-[UAFXPCService checkAssetStatus:]"
+ "-[UAFXPCService diskSpaceNeededInBytesForLanguage:forClient:completion:]"
+ "-[UAFXPCService downloadDictationAssetsForLanguage:]"
+ "-[UAFXPCService downloadSiriAssetsOverCellular]"
+ "-[UAFXPCService downloadSiriAssets]"
+ "-[UAFXPCService expireSubscriptions:]"
+ "-[UAFXPCService expireSubscriptions:]_block_invoke"
+ "-[UAFXPCService lockLatestAtomicInstance:completion:]_block_invoke"
+ "-[UAFXPCService markAssetsExpired:completion:]"
+ "-[UAFXPCService markAssetsExpired:completion:]_block_invoke"
+ "-[UAFXPCService operationWithConfig:completion:]_block_invoke"
+ "-[UAFXPCService postAssetNotificationIfNeeded]"
+ "-[UAFXPCService postDictationAssetNotificationForLanguage:]"
+ "-[UAFXPCService runUpdates]_block_invoke_3"
+ "-[UAFXPCService setSystemConfigurationForKey:withValue:completion:]"
+ "-[UAFXPCService setSystemConfigurationForKey:withValue:completion:]_block_invoke"
+ "-[UAFXPCService subscribeWithConfig:userInitiated:completion:]"
+ "-[UAFXPCService subscriptions:subscriber:user:completion:]"
+ "-[UAFXPCService unsubscribeWithConfig:userInitiated:completion:]"
+ "/private/var/db/assetsubscriptiond"
+ "/usr/libexec/siriknowledged"
+ "@\"NSDictionary\"8@?0"
+ "@\"RBSAssertion\""
+ "@20@0:8I16"
+ "@24@0:8^I16"
+ "@24@0:8^i16"
+ "@32@0:8^@16^@24"
+ "@36@0:8@16I24^@28"
+ "@36@0:8^@16I24^@28"
+ "@52@0:8@16@24@32@40B48"
+ "@56@0:8@16@24@32@40B48B52"
+ "@56@0:8@16@24@32@40^@48"
+ "@56@0:8@16@24@32^B40^@48"
+ "@60@0:8@16^@24B32^B36^B44^@52"
+ "@68@0:8@16@24@32@40@48@56B64"
+ "Asset Set '%@' is not a string"
+ "Asset Set Consistency Token %@ for assetSet %@ with atomic instance %@ (%@ with ref count %lld) experimentActivated %@ bootUUID %@ isBootUUIDCurrent %d object instance %@ experiment %@ preinstalledAssetsSummary %@"
+ "AssetDelivery"
+ "AutoAssetType for Asset \"%@\" is invalid"
+ "B32@0:8^B16^i24"
+ "B56@0:8@16@24@32@40@48"
+ "B60@0:8@16@24@32@40@48B56"
+ "Both subscriptionName and subscriber must be provided"
+ "CAReportingAssetSet"
+ "CREATE TABLE IF NOT EXISTS Subscriptions (k0 TEXT NOT NULL, k1 TEXT NOT NULL, k2 BLOB, k3 REAL, k4 TEXT NOT NULL, k5 REAL)"
+ "CREATE TABLE IF NOT EXISTS UserInformation (k0 TEXT PRIMARY KEY NOT NULL, k1 REAL, k2 TEXT NOT NULL)"
+ "CREATE UNIQUE INDEX IF NOT EXISTS subscriptionIndex on Subscriptions (k0, k1, k4)"
+ "Cannot find user with dsid %@"
+ "Cannot find user with uid %u"
+ "Context"
+ "Could not get config"
+ "Could not lookup console user"
+ "Current user ID is nil in UMUserManager framework"
+ "DB Upgrade from 1 to 2"
+ "DELETE FROM DbVersion"
+ "DELETE FROM Subscriptions WHERE k0 = ? AND k1 = ? AND k4 = ?"
+ "DELETE FROM UserInformation"
+ "DELETE FROM UserInformation WHERE k0 = ?"
+ "DailyStatus"
+ "Errors"
+ "FFFFEEEE-DDDD-CCCC-BBBB-AAAA"
+ "FFFFEEEE-DDDD-CCCC-BBBB-AAAA00000000"
+ "Failed to parse UID from string %@"
+ "Failed to retrieve user info for UID %@: %s"
+ "FinishTaskUninterruptable"
+ "HasMigrated"
+ "HomeDirectory"
+ "I32@0:8@16^@24"
+ "INSERT OR REPLACE INTO Subscriptions (k0, k1, k2, k3, k4, k5) VALUES (?, ?, ?, ?, ?, ?)"
+ "INSERT OR REPLACE INTO UserInformation (k0, k1, k2) VALUES (?, ?, ?)"
+ "InhibitRemoval"
+ "LastSeen"
+ "Memory allocation failed while looking for uid %@"
+ "MigrateSubscriptions"
+ "No errors detected"
+ "No user found for uid %d"
+ "No username for %@"
+ "Node"
+ "Preferences"
+ "PrerequisiteAssetBuilds"
+ "Process is not entitled to UMUserManager framework"
+ "Process is not entitled to UMUserManager framework. %@"
+ "RemoveUser"
+ "Request to UAF subscription service when subscription service is disabled"
+ "ResetAssetSets"
+ "RunMaintenanceTask"
+ "SELECT DISTINCT k0 FROM Subscriptions WHERE k4 = ?"
+ "SELECT DISTINCT k4 FROM Subscriptions"
+ "SELECT k0, k1, k2 FROM UserInformation WHERE k1 <= ?"
+ "SELECT k0, k2, k4 FROM Subscriptions WHERE k3 <> 0.0 AND datetime(k3, 'unixepoch') < datetime('now')"
+ "SELECT k1, k2 FROM UserInformation WHERE k0 = ?"
+ "SELECT k2 FROM Subscriptions WHERE k0 = ? AND k4 = ?"
+ "SELECT k2 FROM Subscriptions WHERE k4 = ?"
+ "SELECT k2, k0, k4 FROM Subscriptions"
+ "SELECT k2, k5 FROM Subscriptions WHERE k0 = ? AND k1 = ? AND k4 = ?"
+ "Status"
+ "SubscriptionUser"
+ "SubscriptionsToMigrate"
+ "SystemNode"
+ "T@\"NSMutableDictionary\",&,N,V_errors"
+ "T@\"NSString\",R,V_databaseName"
+ "T@\"NSUUID\",&,N,V_instanceUUID"
+ "T@?,C,N,V_internalProgressCompletion"
+ "TB,N,V_experimentActivated"
+ "There are no underlying assets (neither atomic instance nor asset roots) for consistency token for asset set %@"
+ "UAF"
+ "UAF DB write"
+ "UAF database access"
+ "UAFAssetSetSubscriptionManager"
+ "UAFBiomeInstrumenter"
+ "UAFCoreAnalyticsInstrumenter"
+ "UAFRegisterSubscriptionXPCActivities"
+ "UAFUser"
+ "UAFUserManager"
+ "UAFUserManager.Concurrent"
+ "UAFXPCActivity"
+ "UAF_FAIL_MACH_SANDBOX_CHECK"
+ "UAF_XPC_ENDPOINT"
+ "UMMultiUserNode"
+ "Unsubscribe failed"
+ "UpdateLastSeen"
+ "UserCleanup"
+ "Username"
+ "Vv24@0:8@?<v@?@\"NSError\">16"
+ "Vv40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "Vv40@0:8@16@24@?32"
+ "XPC sent to wrong endpoint"
+ "^v16@0:8"
+ "_RegisterUserCleanupUAFActivity"
+ "_acquireAssertion"
+ "_checkDbVersion:storedVersion:"
+ "_constructBiomeAssetSet:storeManager:"
+ "_deleteDbVersion"
+ "_emitAssetDailyStatusEvent:autoAssetSet:entries:assetSetArrived:"
+ "_errors"
+ "_finalizeStatements"
+ "_getAllSubscriptions:"
+ "_getBiomeAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:"
+ "_getBiomeEventDeviceMetadata"
+ "_getBiomeStreamForAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:assetSetArrived:"
+ "_getBiomeStreamForScheduledDailyAssetStatus"
+ "_getBiomeUAFAssetSet:assetSetId:entries:errorCodes:fromPSUS:"
+ "_getMADownloadErrors:assetSetName:assetSetID:"
+ "_getSubscribers:subscribers:"
+ "_getSubscription:subscription:user:"
+ "_getSubscriptions:user:"
+ "_getSubscriptionsStatus"
+ "_getUser:lastSeen:nodeName:"
+ "_instanceUUID"
+ "_internalProgressCompletion"
+ "_queuesArePaused"
+ "_rbassertion"
+ "_readAllUsers"
+ "_readSubscriptionsForUser"
+ "_readUser"
+ "_readUsersOlderThan"
+ "_releaseAssertion"
+ "_removeAllUsers"
+ "_removeUser"
+ "_removeUser:"
+ "_setUserLastSeenTime:node:time:"
+ "_subscribeSubscription:subscriptionName:assetSetSubscription:expires:user:"
+ "_subscriptionDiffersFromDB:subscriber:user:error:"
+ "_subscriptionService"
+ "_unsubscribeSubscription:subscription:user:"
+ "_writeUserLastSeen"
+ "acquireWithError:"
+ "all"
+ "allUsers"
+ "allowRemoves"
+ "alternateDSID"
+ "assetSetUsagesForSubscribers:storeManager:configurationManager:anyUnknown:error:"
+ "assetdelivery-validation"
+ "attributeWithDomain:name:"
+ "bestEffortSerializeDictToJSONStr:error:"
+ "cacheDeleteStatusChange:"
+ "com.apple.UnifiedAssetFramework.PrerequisiteBuilds"
+ "com.apple.UnifiedAssetFramework.assetsubscriptiond.started"
+ "com.apple.common"
+ "com.apple.siri.uaf.reset"
+ "com.apple.siri.uaf.subscription.service"
+ "com.apple.siri.uaf.validation.general"
+ "com.apple.siri.xpc_activity.uaf-system-post-upgrade"
+ "com.apple.siri.xpc_activity.uaf-system-subscription-maintenance"
+ "com.apple.siri.xpc_activity.uaf-usercleanup"
+ "com.apple.uaf.AssetSetState"
+ "configureAssetDelivery:configurationManager:lockIfUnchanged:oldSubscriptions:newSubscriptions:userInitiated:"
+ "configureAutoAssetsFromNewSubscriptions:oldSubscriptions:configurationManager:lockIfUnchanged:userInitiated:"
+ "consistencyTokenFromConfig:atomicInstance:experiment:"
+ "could not determine console user"
+ "could not serialize to JSON"
+ "createProxyXPCConnection"
+ "createSubscriptionXPCConnection"
+ "createXPCConnection"
+ "currentConnection"
+ "currentConsoleUserWithUID:"
+ "currentProcess"
+ "currentUser"
+ "currentUserWithNode:error:"
+ "daemonSubscriptionMigration"
+ "dataUsingEncoding:"
+ "databaseName"
+ "dateWithTimeIntervalSince1970:"
+ "decodeBoolForKey:"
+ "dictionaryRepresentation"
+ "distantFuture"
+ "effectiveUserIdentifier"
+ "encodeBool:forKey:"
+ "errors"
+ "expireSubscriptions:"
+ "findDiffBetweenOldAssetSetUsages:newAssetSetUsages:knownAssetSets:usedAssetSets:configurationManager:"
+ "finished:withStatus:withError:"
+ "flattenSubscriptions:"
+ "get users"
+ "getAllSystemConfiguration:"
+ "getPWUID:error:"
+ "getSubscribers:error:"
+ "getSubscribers:storeManager:error:"
+ "getSubscription:subscriber:user:error:"
+ "getSubscription:subscriber:user:storeManager:error:"
+ "getSubscriptions:user:error:"
+ "getSubscriptions:user:storeManager:error:"
+ "getUUIDBytes:"
+ "getUserDefaultStoragePath"
+ "getUserLastSeenTime:error:"
+ "getUserNodeName:error:"
+ "getUserServiceXPCEndpoint"
+ "getUsers:"
+ "getUsersOlderThanDate:error:"
+ "getenv:"
+ "geteuid"
+ "getting user last seen"
+ "getting user node name"
+ "getting users older than"
+ "i32@0:8@16^@24"
+ "i40@0:8@16@24@32"
+ "i40@0:8@16^@24^@32"
+ "initSubscriptionService"
+ "initWithAliasName:aliasValue:"
+ "initWithAssetName:assetSpecifier:assetVersion:assetLocale:assetSource:isAssetPathValid:assetPath:assetDownloadSizeInBytes:assetUnarchivedSizeInBytes:"
+ "initWithAssetSetName:assets:assetType:assetSetId:audienceId:mobileAssetDownloadErrorCodeFrequency:fromPreSoftwareUpdateStaging:expensiveCellularDownloadRequested:"
+ "initWithAssetSetStatus:statusReason:"
+ "initWithAssetSetUsages:configurationManager:internalProgressWithStatus:"
+ "initWithDefaultService"
+ "initWithDeviceId:deviceType:programCode:systemBuild:inputLocale:nanoSecondsSinceLastBoot:"
+ "initWithDeviceMetadata:availableAssetDailyStatus:"
+ "initWithExplanation:target:attributes:"
+ "initWithLanguageCode:countryCode:"
+ "initWithMachServiceName:subscriptionService:"
+ "initWithMobileAssetDownloadErrorCode:timesOccurred:"
+ "initWithSubscriberName:subscriptions:"
+ "initWithSubscriptionName:assetSetIndices:assetSetUsages:usageAliases:"
+ "initWithSubscriptionServiceName"
+ "initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:bootUUID:experimentActivated:"
+ "initWithUafAssetSets:uafAssetSubscriptions:allAssets:"
+ "initWithUsageName:usageValue:"
+ "initWithUserService"
+ "initWithXPCListener:subscriptionService:"
+ "instanceUUID"
+ "internalProgressCompletion"
+ "invalidateSyncWithError:"
+ "isBiomeAvailable"
+ "isLatestConsistencyToken:"
+ "isManaged"
+ "isMultiUser"
+ "isSharedIPad"
+ "isSiriAnalyticsAvailable"
+ "isSiriknowledgedSupported"
+ "isSymptomDiagnosticReporterAvailable"
+ "isSystemUser:error:"
+ "isSystemUserUsingUID:"
+ "latest"
+ "logAssetSetDownloadEvent:assetSetId:entries:errorCodes:fromPSUS:assetSetArrived:"
+ "logScheduledDailyAssetStatus"
+ "logUAFAssetSetDailyStatus:entries:assetSetArrived:"
+ "logUAFAssetSetState:assetSpecifiersAndVersions:"
+ "loginUser"
+ "mach-lookup"
+ "maintenanceTaskWithCompletion:"
+ "migrateMBSetupUserSubscriptions:user:node:"
+ "migrateSubscriptions:user:completion:"
+ "mobile"
+ "nameForUser:error:"
+ "nodeForUser:error:"
+ "performDbUpgrade"
+ "performUserCleanup"
+ "performUserCleanupOnQueue:completion:"
+ "processIdentifier"
+ "progress:completed:total:status:context:"
+ "pwdNameForUser:error:"
+ "pwdNodeForUser:error:"
+ "pwdUIDToUserID:"
+ "pwdUserIDToUID:withError:"
+ "pwdUserWithNodeForUID:uid:error:"
+ "q24@0:8@16"
+ "readDate:col:"
+ "regionCode"
+ "remove user"
+ "removeAllUsers"
+ "removeAutoAssetSet:fallbackAlter:"
+ "removeUser:"
+ "removeUser:queue:completion:"
+ "removing all users"
+ "resetAssetSets:"
+ "resetAssetSets:queue:completion:"
+ "sandboxCheckMachEndpoint:"
+ "selectXPCEndpoint"
+ "sendCAEvent:assetSpecifier:assetVersion:"
+ "sendEvent:"
+ "sendNotificationDBReset"
+ "set last seen time"
+ "setErrors:"
+ "setExperimentActivated:"
+ "setInstanceUUID:"
+ "setInternalProgressCompletion:"
+ "setLatestAtomicInstance:autoAssetSet:fallbackAlter:"
+ "setMinimalSpecifiers:"
+ "setSystemConfigurationForKey:withValue:completion:"
+ "setUserLastSeenTime:node:time:"
+ "setWithObject:"
+ "sharedIpadSupported"
+ "shared_ipad_support"
+ "shortTermLockFileName"
+ "source"
+ "stageAssetsWithNewSubscriptions:oldSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:"
+ "subscribe:subscriptions:user:node:"
+ "subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:"
+ "subscribe:subscriptions:user:userInitiated:queue:completion:"
+ "subscribeWithConfig:userInitiated:completion:"
+ "subscriptionServiceEnabled"
+ "subscription_service"
+ "subscriptions:subscriber:user:completion:"
+ "subscriptions:subscriber:user:storeManager:error:"
+ "synchronize"
+ "system"
+ "systemUserWithNode:error:"
+ "uid"
+ "umCurrentUMUserWithNode:error:"
+ "umEntitlementPresent"
+ "umNameForUser:error:"
+ "umNodeForUser:error:"
+ "umUserWithDSID:withUid:withError:"
+ "umUserWithNodeForUID:uid:error:"
+ "unsubscribe:subscriptionNames:user:userInitiated:queue:completion:"
+ "unsubscribe:subscriptions:user:node:"
+ "unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:"
+ "unsubscribeWithConfig:userInitiated:completion:"
+ "updateAssetsForSubscribers:policies:queue:progress:detailedProgress:internalProgress:completion:storeManager:configurationManager:"
+ "updateLastSeenForCurrentUserOnQueue:completion:"
+ "updateLastSeenForUser:queue:completion:"
+ "upgradeBlocks_block_invoke_2"
+ "userWithNodeForUID:uid:error:"
+ "username"
+ "v24@?0@\"NSString\"8^B16"
+ "v36@0:8@16B24@?28"
+ "v40@0:8@16Q24@32"
+ "v40@0:8B16@20@28B36"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v52@?0d8Q16Q24Q32B40@44"
+ "v56@0:8@16Q24Q32Q40@48"
+ "v60@0:8@16@24@32B40@44@?52"
+ "v88@0:8@16@24@32@?40@?48@?56@?64@72@80"
+ "validLocalNode"
+ "validLocalUsers:error:"
+ "validNodesWithError:"
+ "validation-assets"
- "%@:%@"
- "%llu"
- "%s #settings Download requested for Siri assets (%{public}@)..."
- "%s #settings Download requested for legacy Siri for language %{public}@..."
- "%s %{public}@: %{public}@ Could not initialize auto asset set %{public}@ : %{public}@"
- "%s %{public}@: %{public}@ Could not load asset set %{public}@ as _autoAssetSetStatus is unexpectedly nil"
- "%s %{public}@: %{public}@ Could not load asset set %{public}@ as autoAssets is unexpectedly nil"
- "%s %{public}@: %{public}@ Could not lock asset set %{public}@ with atomic instance %{public}@: %{public}@"
- "%s %{public}@: %{public}@ Locked asset set %{public}@ atomic instance %{public}@"
- "%s %{public}@: Asset name %@ does not exist in asset set %@"
- "%s %{public}@: No level for factor %@"
- "%s %{public}@: Preferring trial assets over preinstalled assets for assetset %{public}@"
- "%s %{public}@: TRILevel is not a directory or file type: %@ %d"
- "%s %{public}@: Using AutoAsset configuration instead of Trial for asset set %{public}@"
- "%s %{public}@: _createAssetFromTrialInfo using fallback for assetName %@ with valid path"
- "%s %{public}@: _createAssetFromTrialInfo using fallback for assetName %@ without valid path"
- "%s %{public}@: _createAssetFromTrialInfo using primary for assetName %@ with valid path"
- "%s %{public}@: _createAssetFromTrialInfo using primary for assetName %@ without valid path"
- "%s %{public}@: nil path for factor %@"
- "%s %{public}@: setAssetsPromoted: No namespaces for assets"
- "%s %{public}@: setAssetsPromoted: Not supported for MAAutoAssetSet assets"
- "%s %{public}@: setAssetsPromoted: promoteFactorsForNamespace failed for namespace %@: %ld %@"
- "%s %{public}@: setAssetsProvisional: No namespaces for assets"
- "%s %{public}@: setAssetsProvisional: Not supported for MAAutoAssetSet assets"
- "%s %{public}@: setAssetsProvisional: setFactorsProvisionalForNamespace failed for namespace %@: %ld %@"
- "%s %{public}@: validPathOnly nil path for factor %@"
- "%s Active rollout exists for %@, skipping factory asset check"
- "%s Adding level with key %@ to cache"
- "%s All per-project updates complete as part of update for of all trial assets"
- "%s All trial factors now %{public}@"
- "%s All updates for on-demand factors in project %{public}@ complete"
- "%s All updating of trial assets in project %{public}@ complete"
- "%s Attempting to download needed factors for namespace %{public}@"
- "%s Attempting to remove unneeded factors for namespace %{public}@"
- "%s Auto Asset Feature disabled for %@"
- "%s Auto Asset Feature enabled for %@"
- "%s Auto asset set %{public}@ has expected specifiers %{public}@ and is %{public}@"
- "%s Binding of subscriber name failed in remove subscription query for Subscriber: '%@', Subscription: '%@' SQLite error: %d (%s, Extended: %d)"
- "%s Binding of subscription name failed in remove subscription query for Subscriber: '%@', Subscription: '%@' SQLite error: %d (%s, Extended: %d)"
- "%s Binding subscription name to the get subscriptions query failed for Subscriber: '%{public}@' SQLite error: %d (%s, Extended: %d)"
- "%s Callback for downloading factors %{public}@ called more than once!"
- "%s Callback for removing factors %{public}@ called more than once!"
- "%s Cannot update downloaded on-demand factor %{public}@"
- "%s Cannot update regular factor %{public}@"
- "%s Cannot update unknown factor %{public}@"
- "%s Changed subscriptions for '%{public}@': '%{public}@'"
- "%s Changing subscriptions for '%{public}@': '%{public}@'"
- "%s Completion Callback for status of factors %{public}@ called more than once!"
- "%s Configuring Trial from asset set usages"
- "%s Could get trial assets for asset set %{public}@"
- "%s Could not create trial client for asset set %{public}s"
- "%s Could not find TRIProject for %{public}s for asset set %{public}s"
- "%s Could not read system usages from database: %@"
- "%s Could not retrieve pwent: %d %{public}s"
- "%s Couldn't upgrade the database even after %d attempts"
- "%s Creating DbVersion table failed SQLite error: %d (%s, Extended: %d)"
- "%s Creation or checking of DbVersion table failed"
- "%s Denying %{public}@ due to version mismatch"
- "%s Denying subscription due to exceeding usage limits for subscriber \"%@\""
- "%s Discovered newer instance of %{public}@: %{public}@ vs %{public}@, XPC'ing to siriknowledged to lock"
- "%s Emitted SADAvailableAssetDailyStatus message for asset sets"
- "%s Emitted scheduled SADAvailableAssetDailyStatus message"
- "%s Emitting asset set arrived daily status event for auto asset set %{public}@, pre-staged:%d"
- "%s Error binding read subscription for '%{public}@' '%{public}@' SQLite error: %d (%s, Extended: %d)"
- "%s Error executing read subscription for '%{public}@' '%{public}@' SQLite error: %d (%s, Extended: %d)"
- "%s Factor %{public}@ removed"
- "%s Factors %{public}@ downloaded"
- "%s Failed to download factors %{public}@: %{public}@"
- "%s Failed to get all subscriptions due to error: %@. Stopping staging"
- "%s Failed to remove factor %{public}@: %{public}@"
- "%s Failed to update namespaces %{public}@: %{public}@"
- "%s Failed to update storage to reflect subscriptions %{public}@ for subscriber %{public}@"
- "%s Finished configuring Trial from asset set usages"
- "%s Got an unknown namespaceId: %d"
- "%s Ignoring update to namespace %@ while observing asset set %@"
- "%s Issuing %{public}@ update notification due to %{public}@ update"
- "%s MAQuery for factorLevels roots %@ failed: %@"
- "%s MAQuery for factory assets %@ failed: %@"
- "%s Missing version info for asset %@"
- "%s Namespace updates complete"
- "%s Need to download desired on demand factor %{public}@"
- "%s Need to remove undesired on demand factor %{public}@"
- "%s No active rollout for %@ exists, performing factory check"
- "%s No changes found for subscriber %{public}@ subscriptions: %{public}@"
- "%s No level found for %@(nil), but found %@"
- "%s No need to remove desired on demand factor %{public}@"
- "%s No subscription changes for subscriber '%{public}@' and subscriptions '%{public}@'"
- "%s No trial assets for asset set %{public}@ for observer"
- "%s No trial assets to update"
- "%s No trial assets to update for %{public}@"
- "%s Not attempting to remove unneeded factors"
- "%s Not attempting to update subscriptions for %{public}@: %{public}@"
- "%s Not generating trial factors for asset set %{public}@ as it using auto assets"
- "%s Not including %{public}@ as its trial factor isn't specified"
- "%s Not including asset %{public}@ in asset set %{public}@ due to lack of entitlement for Namespace %{public}@"
- "%s Not updating the following namespaces, as at least one already exists within the same assetset: %{public}@"
- "%s Opened database (%@), database existed:%d"
- "%s Possible beginning of sequence of notifications to ignore while observing asset set %@, starting with update to namespace %@"
- "%s Post-Upgrade registering for startup complete notification"
- "%s Process is not entitled for %@, skipping"
- "%s Process is not entitled for any trial namespaces, skipping cache population"
- "%s Processing any factory factorlevels in %@ for cache"
- "%s Processing any root factorlevels in %@ for cache"
- "%s Query preparation to create DbVersion table failed SQLite error: %d (%s, Extended: %d)"
- "%s Received finished status for unknown factor %{public}@ in namespace %{public}@"
- "%s Received progress for unknown factor %{public}@ in namespace %{public}@ with fraction completed %f and status %{public}@"
- "%s Removal of subscription failed for Subscriber: '%@', Subscription: '%@' SQLite error: %d (%s, Extended: %d)"
- "%s Removes temporarily disallowed, skipping remove"
- "%s Removing expired sub '%{public}@' from subscriber '%{public}@' at '%{public}@'"
- "%s Returning trial for levelForFactor:%@:%@:%@"
- "%s Running UAFCacheUpdate"
- "%s Siri & Dictation are turned off, so using Feedback logger for logging asset status"
- "%s Skipping %{public}@ update notification from %{public}@ due to no actual change"
- "%s Store update count mismatch: %llu vs %llu, skipping removes"
- "%s Store update count: %llu vs %llu and removeUnneededFactors: %d"
- "%s Subscriptions for subscriber: %{public}@: %{public}@"
- "%s System AssetSetUsages: %{public}@"
- "%s System Configuration: %{public}@"
- "%s The subscribers on this device: %{public}@"
- "%s Trial Feature disabled for %@"
- "%s Trial Feature enabled for %@"
- "%s Trial reports %{public}lu status for %{public}@:%{public}@"
- "%s UAFSchemaUAFClientEvent uploaded to Feedback logger"
- "%s Underlying error: %u found while logging MA download error for asset set %{public}@:"
- "%s Unsubscribing for '%{public}@'"
- "%s Update of trial assets in project %{public}@ complete as part of update of all trial assets"
- "%s UpdateTrialFactors complete"
- "%s Updated namespaces %{public}@"
- "%s Updated storage to reflect removal of subscriptions %{public}@ for subscriber %{public}@"
- "%s Updated storage to reflect subscriptions %{public}@ for subscriber %{public}@"
- "%s Updated subscriptions results in no usage changes, skipping reconfiguration"
- "%s Updating %lu on-demand factors in project %{public}@"
- "%s Updating namespaces"
- "%s Updating namespaces %{public}@"
- "%s Updating namespaces for %{public}@ prior to on-demand factor downloading"
- "%s Updating on demand factors in project %{public}@"
- "%s Updating trial assets in project %{public}@ as part of update of all trial assets"
- "%s Updating trial factors %{public}@ for %{public}@"
- "%s Upload of UAFSchemaUAFClientEvent to Feedback logger failed with error: %@"
- "%s Using Feedback logger"
- "%s Version info is malformed for asset %@, version %@"
- "%s could not serialize persisted asset info array to json, not including in output"
- "%s downloadLevelsForFactors for %{public}@ with namespace %{public}@"
- "%s old and new usages cover different asset sets, requiring configure"
- "%s old and new usages equal, skipping configure"
- "%s resulting specifiers different, requiring configure"
- "%s statusOfDownload for %{public}@:%{public}@ status: %{public}@"
- "%s subscriptionsForSubscriber complete with error: %{public}@"
- "'"
- "+[TRIClient(UAFTrialClient) UAFCacheUpdate]"
- "+[TRIClient(UAFTrialClient) _addLevelToCache:namespaceName:factorName:withCache:]"
- "+[TRIClient(UAFTrialClient) _cachedLevelForFactorAnyLanguage:withNamespaceName:withCache:]_block_invoke"
- "+[TRIClient(UAFTrialClient) _factoryFactorLevelsWithNamespaceName:onDemandClient:]"
- "+[TRIClient(UAFTrialClient) _rootFactorLevelsWithNamespaceName:]"
- "+[UAFAssetSet getEntitledTrialAssets:usages:]"
- "+[UAFAssetSetConfiguration fromContentsOfURL:applyFeatureFlags:error:]"
- "+[UAFAssetSetManager _subscriptionDiffersFromDB:subscriber:error:]"
- "+[UAFAssetSetManager configureAssetDelivery:configurationManager:lockIfUnchanged:subscriptions:assetSetUsages:userInitiated:]"
- "+[UAFAssetSetManager shouldConfigure:newUsages:]"
- "+[UAFAssetSetManager shouldConfigure:newUsages:]_block_invoke"
- "+[UAFAssetSetManager subscribe:subscriptions:queue:completion:]"
- "+[UAFAssetSetManager subscribe:subscriptions:queue:completion:]_block_invoke"
- "+[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke"
- "+[UAFAssetSetManager subscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke_5"
- "+[UAFAssetSetManager unsubscribe:subscriptions:queue:completion:]"
- "+[UAFAssetSetManager unsubscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke"
- "+[UAFAssetSetManager unsubscribe:subscriptions:storeManager:configurationManager:userInitiated:]_block_invoke_2"
- "+[UAFAutoAssetManager _logDailyStatusEventForAssetSetArrived:entries:assetSetArrived:]"
- "+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:userInitiated:]"
- "+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:userInitiated:]_block_invoke"
- "+[UAFAutoAssetManager releaseIncompatibleAssetSet:specifiers:configuration:]_block_invoke"
- "+[UAFAutoAssetManager removeAutoAssetSet:completion:]"
- "+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]"
- "+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke"
- "+[UAFAutoAssetManager stageAssetsWithSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:]"
- "+[UAFCommonUtilities getDefaultStoragePath]"
- "+[UAFCommonUtilities resetAutoAsset:userInfo:]_block_invoke_2"
- "+[UAFConfiguration autoAssetFeatureEnabled:]"
- "+[UAFConfiguration trialFeatureEnabled:]"
- "+[UAFInstrumentationProvider _constructNamespaceStatusEventForNamespace:withClient:]"
- "+[UAFInstrumentationProvider _constructSelfAssetSet:storeManager:]"
- "+[UAFInstrumentationProvider _emitAssetDailyStatusEvent:]"
- "+[UAFInstrumentationProvider _emitAssetDailyStatusEvent:]_block_invoke"
- "+[UAFInstrumentationProvider getDeviceMetadata]"
- "+[UAFInstrumentationProvider logAvailableAssetDailyStatusWithFeedbackLogger:completion:]"
- "+[UAFInstrumentationProvider logSubscriptionsStatus]_block_invoke"
- "+[UAFInstrumentationProvider logUAFAssetSetDailyStatus:assetSetArrived:]"
- "+[UAFTrialUpdateManager getTrialDownloadStatusForUsages:configurationManager:]"
- "+[UAFTrialUpdateManager getTrialFactors:configurationManager:includeAllAssetSets:noRemovalNamespaces:assetSetNamespaces:]"
- "+[UAFTrialUpdateManager trialClientWithProject:]"
- "+[UAFTrialUpdateManager updateNamespaces:missingRolloutsOnly:expensiveNetworking:assetSetNamespaces:updateProgress:]"
- "+[UAFTrialUpdateManager updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]"
- "+[UAFTrialUpdateManager updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]_block_invoke"
- "+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]"
- "+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke"
- "+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_2"
- "+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_4"
- "+[UAFTrialUpdateManager updateTrialFromAssetSetUsages:rolloutUpdateMode:expensiveNetworking:storeManager:configurationManager:progress:completion:]"
- "+[UAFTrialUpdateManager updateTrialFromAssetSetUsages:rolloutUpdateMode:expensiveNetworking:storeManager:configurationManager:progress:completion:]_block_invoke"
- "+[UAFTrialUpdateManager updateTrialFromAssetSetUsages:storeManager:configurationManager:]"
- "+[UAFTrialUpdateManager updateTrialFromAssetSetUsages:storeManager:configurationManager:]_block_invoke"
- "+[UAFTrialUpdateManager updateTrialProject:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]"
- "+[UAFTrialUpdateManager updateTrialProject:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]_block_invoke"
- "-[TRIClient(UAFTrialClient) UAFLevelForFactor:withNamespaceName:withLanguage:]"
- "-[UAFAssetSet _createAssetFromTrialInfo:assetName:fallback:validPathOnly:]"
- "-[UAFAssetSet createAssetFromTrialInfo:assetName:]"
- "-[UAFAssetSet markAssetsPromoted:error:]"
- "-[UAFAssetSet markAssetsProvisional:error:]"
- "-[UAFAssetSet namespacesOfAssetNames:error:]"
- "-[UAFAssetSetManager assetSetUsagesForSubscribers:storeManager:configurationManager:anyUnknown:]"
- "-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]"
- "-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke"
- "-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_8"
- "-[UAFAssetSetObserver namespaceHasChanged:]"
- "-[UAFAssetSetObserver resetNamespacesToIgnore:]"
- "-[UAFAssetSetProgress progress:completed:total:status:]"
- "-[UAFAssetUtilitiesService _downloadSiriAssetsWithCellular:]"
- "-[UAFAutoAssetProgress finished:withStatus:]_block_invoke"
- "-[UAFAutoAssetProgress initWithAssetSetUsages:configurationManager:detailedProgressWithStatus:]"
- "-[UAFSubscriptionStoreManager _checkDbVersion]"
- "-[UAFSubscriptionStoreManager _createDbVersionTable]"
- "-[UAFSubscriptionStoreManager _getSubscription:subscription:]"
- "-[UAFSubscriptionStoreManager _getSubscriptions:]"
- "-[UAFSubscriptionStoreManager _subscribeSubscription:subscriptionName:assetSetSubscription:expires:]"
- "-[UAFSubscriptionStoreManager _unsubscribeSubscription:subscription:]"
- "-[UAFSubscriptionStoreManager getAllSubscriptions:]_block_invoke"
- "-[UAFSubscriptionStoreManager getAllSystemConfiguration]_block_invoke"
- "-[UAFSubscriptionStoreManager getSubscribers]_block_invoke"
- "-[UAFSubscriptionStoreManager performDbUpgradeToVersion:]_block_invoke"
- "-[UAFSubscriptionStoreManager subscribe:subscriptions:expires:]_block_invoke"
- "-[UAFTrialUpdateProgress reportStatus:]"
- "-[UAFTrialUpdateProgress trialFactorFinished:namespace:]_block_invoke"
- "-[UAFTrialUpdateProgress trialFactorProgress:namespace:fractionCompleted:status:]_block_invoke"
- "-[UAFXPCConnection subscriptionsForSubscriber:completion:]_block_invoke"
- "-[UAFXPCConnection subscriptionsForSubscriber:completion:]_block_invoke_2"
- "-[UAFXPCService subscribeWithConfig:completion:]"
- "-[UAFXPCService subscriptionsForSubscriber:completion:]"
- "-[UAFXPCService unsubscribeWithConfig:completion:]"
- ":%@:"
- ":%@:%@"
- "@\"NSMutableArray\""
- "@\"TRIClient\""
- "@28@0:8I16@20"
- "@32@0:8@16@?24"
- "@48@0:8@16@24@32^B40"
- "@52@0:8@16@24@32B40^@44"
- "@52@0:8@16@24B32^@36^@44"
- "@60@0:8@16@24B32^B36^B44^@52"
- "@64@0:8@16@24@32@40@48@56"
- "Asset Set Consistency Token %@ for assetSet %@ with atomic instance %@ (%@ with ref count %lld) experiment %@ preinstalledAssetsSummary %@ bootUUID %@ isBootUUIDCurrent %d"
- "B20@0:8i16"
- "B48@0:8@16B24B28@32@40"
- "B52@0:8@16@24@32@40B48"
- "CH"
- "CREATE TABLE IF NOT EXISTS Subscriptions (k0 TEXT, k1 TEXT, k2 BLOB, k3 REAL)"
- "CREATE UNIQUE INDEX IF NOT EXISTS subscriptionIndex on Subscriptions (k0, k1)"
- "Cannot invalidate a token without an underlying atomic instance"
- "DELETE FROM Subscriptions WHERE k0 = ? AND k1 = ?"
- "Factor"
- "ForceUpdateNamespaces"
- "INSERT OR REPLACE INTO Subscriptions (k0, k1, k2, k3) VALUES (?, ?, ?, ?)"
- "L"
- "MA query for %@ failed with result: %ld"
- "MA query for AssetType %@, factorName: %@, language: %@ had no results"
- "MA query for roots of AssetType %@, factorName: %@, language: %@ had multiple results.  This is commonly due to multiple roots being installed.  Unclear which one to return."
- "N"
- "NL"
- "No namespaces for assets"
- "RegionCode"
- "SELECT DISTINCT k0 FROM Subscriptions"
- "SELECT k0, k2 FROM Subscriptions WHERE k3 <> 0.0 AND datetime(k3, 'unixepoch') < datetime('now')"
- "SELECT k2 FROM Subscriptions WHERE k0 = ?"
- "SELECT k2 FROM Subscriptions WHERE k0 = ? AND k1 = ?"
- "SELECT k2, k0 FROM Subscriptions"
- "T@\"NSDate\",&,N,V_namespaceUpdateDate"
- "T@\"NSDictionary\",&,N,V_trialMATargetingTemplate"
- "T@\"NSMutableArray\",&,N,V_namespaceTokens"
- "T@\"NSMutableDictionary\",&,N,V_factors"
- "T@\"NSMutableSet\",&,N,V_namespacesToIgnore"
- "T@\"NSSet\",&,N,V_namespaces"
- "T@\"NSString\",&,N,V_trialFactorFallbackTemplate"
- "T@\"NSString\",&,N,V_trialFactorTemplate"
- "T@\"NSString\",&,N,V_trialMAAssetType"
- "T@\"NSString\",&,N,V_trialNamespace"
- "T@\"NSString\",&,N,V_trialProject"
- "T@\"TRIClient\",&,N,V_trial"
- "T@?,C,N,V_detailedProgressWithStatus"
- "TB,N,V_isTrialAvailable"
- "TB,N,V_onDemandFactorsHaveStarted"
- "TB,N,V_outOfSpace"
- "TRIClient init"
- "There are no underlying assets (neither atomic instance nor asset roots)"
- "Trial Assets"
- "TrialEntitlements"
- "TrialFactorFractionCompleted"
- "TrialFactorSize"
- "TrialUpdate"
- "UAFCacheUpdate"
- "UAFFactorLevelsWithNamespaceName:"
- "UAFLevelForFactor:withNamespaceName:withLanguage:"
- "UAFTrialClient"
- "UAFTrialUpdateManager"
- "UAFTrialUpdateManager.Concurrent"
- "UAFTrialUpdateManager.Serial"
- "UAFTrialUpdateProgress"
- "UpdateNamespaces"
- "^{passwd=**IIq****q}24@0:8@16"
- "_%@"
- "_RegisterPeriodicUAFSubscriptionActivity_block_invoke"
- "_addFactorLevelsToCache:namespaceName:withFactorLevelsCache:withLevelCache:"
- "_addLevelToCache:namespaceName:factorName:withCache:"
- "_assetNameToTrial"
- "_cachedLevelForFactor:withNamespaceName:withLanguage:withCache:"
- "_cachedLevelForFactorAnyLanguage:withNamespaceName:withCache:"
- "_checkDbVersion"
- "_client"
- "_constructNamespaceStatusEventForNamespace:withClient:"
- "_constructSelfAssetSet:storeManager:"
- "_createAssetFromTrialInfo:assetName:fallback:validPathOnly:"
- "_createDbVersionTable"
- "_detailedProgressWithStatus"
- "_emitAssetDailyStatusEvent:"
- "_factors"
- "_factoryFactorLevelsWithNamespaceName:onDemandClient:"
- "_factoryLevelForFactor:withNamespaceName:withLanguage:"
- "_getSubscription:subscription:"
- "_getSubscriptions:"
- "_initOnce"
- "_isTrialAvailable"
- "_levelKeyForCache:withFactorName:withLanguage:"
- "_logDailyStatusEventForAssetSetArrived:entries:assetSetArrived:"
- "_namespaceTokens"
- "_namespaceUpdateDate"
- "_namespaces"
- "_namespacesToIgnore"
- "_onDemandFactorsHaveStarted"
- "_outOfSpace"
- "_queryAssetsWithNamespaceName:factorName:language:isRoot:withError:"
- "_rootFactorLevelsWithNamespaceName:"
- "_rootLevelForFactor:withNamespaceName:withLanguage:"
- "_subscribeSubscription:subscriptionName:assetSetSubscription:expires:"
- "_subscriptionDiffersFromDB:subscriber:error:"
- "_trial"
- "_trialFactorFallbackTemplate"
- "_trialFactorTemplate"
- "_trialLevelForFactor:withNamespaceName:withLanguage:"
- "_trialMAAssetType"
- "_trialMATargetingTemplate"
- "_unsubscribeSubscription:subscription:"
- "addAssetSetStatus:"
- "addAssets:"
- "addNamespaceStatus:"
- "all rollouts"
- "applyFeatureFlags"
- "asset"
- "assetSetUsagesForSubscribers:storeManager:configurationManager:anyUnknown:"
- "assetSource"
- "assetTypeFromNamespaceName:"
- "atomic_instance_%@.locker"
- "atomic_instance_latest.locker"
- "autoAssetFeatureEnabled:"
- "autoasset"
- "capitalizedString"
- "checkForOutOfSpace:updateProgress:"
- "com.apple.MobileAsset.Trial.Siri."
- "com.apple.siri.asr.hammer"
- "com.apple.siri.assistant.xr"
- "com.apple.siri.dialog"
- "com.apple.siri.findmy"
- "com.apple.siri.tts"
- "com.apple.siri.understanding.nl.overrides"
- "compatibilityVersionWithNamespaceName:"
- "configureAssetDelivery:configurationManager:lockIfUnchanged:subscriptions:assetSetUsages:userInitiated:"
- "configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:userInitiated:"
- "convertLanguageCodeToSchemaLocale:"
- "createAssetFromTrialInfo:assetName:"
- "deploymentId"
- "deregisterUpdateWithToken:"
- "detailedProgressWithStatus"
- "dictionaryWithObjects:forKeys:"
- "disable_trial_com_apple_siri_asr_hammer"
- "disable_trial_com_apple_siri_dialog"
- "disable_trial_com_apple_siri_findmy"
- "disable_trial_com_apple_siri_tts"
- "disable_trial_com_apple_siri_understanding"
- "disable_trial_com_apple_siri_understanding_nl_overrides"
- "distantPast"
- "doubleValue"
- "downloadLevelsForFactors:withNamespace:queue:options:progress:completion:"
- "factor"
- "factorLevelsWithNamespaceName:"
- "factorPackId"
- "factors"
- "failed to convert namespace %@ to asset type"
- "failed to create MAAssetQuery for %@:%@:%@, assetType: %@"
- "fileValue"
- "filterOnDemandFactors:namespaceName:trialClient:"
- "finished:withStatus:"
- "firstObject"
- "force all rollouts"
- "fromContentsOfURL:applyFeatureFlags:error:"
- "fromPreSoftwareUpdateStaging"
- "getAllSystemConfiguration"
- "getDeviceMetadata"
- "getEntitledTrialAssets:usages:"
- "getFactorProgressKey:factor:"
- "getKnownFactors:namespace:knownFactors:onDemandFactors:"
- "getPWUID:"
- "getPersistedDeviceId"
- "getSubscribers"
- "getSubscription:subscriber:"
- "getSubscriptions:error:"
- "getTrialAssets"
- "getTrialAssets:"
- "getTrialDownloadStatusForUsages:configurationManager:"
- "getTrialFactorFallbackName:"
- "getTrialFactorName:"
- "getTrialFactors:configurationManager:includeAllAssetSets:noRemovalNamespaces:assetSetNamespaces:"
- "getTrialPurgeabilityLevel:"
- "hasAsset"
- "hasAssetId"
- "hasFactor"
- "hasLevel"
- "immediateDownloadForNamespaceNames:allowExpensiveNetworking:error:"
- "initWithAllowsCellular:discretionaryBehavior:"
- "initWithAssetSetUsages:configurationManager:detailedProgressWithStatus:"
- "initWithNSUUID:"
- "initWithTrialFactors:detailedProgressWithStatus:"
- "initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:bootUUID:"
- "initWithXPCListener:"
- "intersectsSet:"
- "isChinaDeviceRegionCode"
- "isOnDemand"
- "isOnDemand:"
- "isPresent:"
- "isRemoveAllowed"
- "isSubscribed:"
- "level"
- "locale"
- "localizedFailureReason"
- "logAvailableAssetDailyStatusWithFeedbackLogger:completion:"
- "logSubscriptionsStatus"
- "logUAFAssetSetDailyStatus:assetSetArrived:"
- "manageXRSubscription:subscribe:"
- "markAssetsPromoted:error:"
- "markAssetsProvisional:error:"
- "missing rollouts only"
- "mobileasset_com_apple_siri_asr_hammer"
- "mobileasset_com_apple_siri_dialog"
- "mobileasset_com_apple_siri_findmy"
- "mobileasset_com_apple_siri_tts"
- "mobileasset_com_apple_siri_understanding"
- "mobileasset_com_apple_siri_understanding_nl_overrides"
- "namespaceHasChanged:"
- "namespaceIdFromName:"
- "namespaceNameFromAssetType:"
- "namespaceTokens"
- "namespaceUpdateDate"
- "namespaces"
- "namespacesOfAssetNames:error:"
- "namespacesToIgnore"
- "numberWithDouble:"
- "objectAtIndex:"
- "onDemandFactorsHaveStarted"
- "onDemandFactorsStarted"
- "outOfSpace"
- "outOfSpaceEncountered"
- "performDbUpgradeToVersion:"
- "progress:completed:total:status:"
- "promoteFactorsForNamespace:error:"
- "removeAutoAssetSet:completion:"
- "removeLevelsForFactors:withNamespace:queue:completion:"
- "reportSiriInstrumentationEvent:forBundleID:completion:"
- "resetNamespacesToIgnore:"
- "rolloutId"
- "rolloutIdentifiersWithNamespaceName:"
- "setAliasName:"
- "setAliasValue:"
- "setAsset:"
- "setAssetDownloadSizeInBytes:"
- "setAssetId:"
- "setAssetLocale:"
- "setAssetName:"
- "setAssetSetId:"
- "setAssetSetIndices:"
- "setAssetSetUsages:"
- "setAssetSource:"
- "setAssetSpecifier:"
- "setAssetUnarchivedSizeInBytes:"
- "setAssetVersion:"
- "setAvailableAssetDailyStatus:"
- "setDeployment:"
- "setDetailedProgressWithStatus:"
- "setDeviceId:"
- "setDeviceMetadata:"
- "setDeviceType:"
- "setDirectoryValue:"
- "setEventMetadata:"
- "setFactor:"
- "setFactorPack:"
- "setFactors:"
- "setFactorsProvisionalForNamespace:error:"
- "setFromPreSoftwareUpdateStaging:"
- "setHasAlias:"
- "setHasId_p:"
- "setHasLevel:"
- "setHasPath:"
- "setInputLocale:"
- "setIsAssetPathValid:"
- "setIsOnDemand:"
- "setIsTrialAvailable:"
- "setLatestAtomicInstance:autoAssetSet:"
- "setLevel:"
- "setMajor:"
- "setMetadata:"
- "setMinor:"
- "setMobileAssetDownloadErrorCode:"
- "setMobileAssetDownloadErrorCodeFrequencys:"
- "setNamespaceCompatabilityVersion:"
- "setNamespaceId:"
- "setNamespaceName:"
- "setNamespaceTokens:"
- "setNamespaceUpdateDate:"
- "setNamespaces:"
- "setNamespacesToIgnore:"
- "setNanoSecondsSinceLastBoot:"
- "setOnDemandFactorsHaveStarted:"
- "setOutOfSpace:"
- "setPatch:"
- "setPath:"
- "setPrerelease:"
- "setProgramCode:"
- "setRollout:"
- "setRolloutId:"
- "setStatusReason:"
- "setSubscriberName:"
- "setSubscriptionName:"
- "setSubscriptions:"
- "setSystemBuild:"
- "setTimesOccurred:"
- "setTrial:"
- "setTrialFactorFallbackTemplate:"
- "setTrialFactorTemplate:"
- "setTrialMAAssetType:"
- "setTrialMATargetingTemplate:"
- "setType:"
- "setUafAssetDailyStatus:"
- "setUafAssetSets:"
- "setUafAssetSubscriptions:"
- "setUafId:"
- "setUsageAliases:"
- "setUsageName:"
- "setUsageValue:"
- "sharedLoggerWithPersistenceConfiguration:"
- "shared_locks"
- "shouldApplyFeatureFlags"
- "shouldConfigure:newUsages:"
- "size"
- "sizeFromLevel:"
- "stageAssetsWithSubscriptions:knownAutoAssetSets:usedAutoAssetSets:autoAssetSets:"
- "statusOfDownloadForFactors:withNamespace:token:queue:progress:completion:"
- "subscribe:subscriptions:expires:"
- "subscribe:subscriptions:storeManager:configurationManager:userInitiated:"
- "subscribeWithConfig:completion:"
- "subscriptionsForSubscriber:completion:"
- "subscriptionsForSubscriber:storeManager:"
- "timeIntervalSinceDate:"
- "trialFactorFallbackTemplate"
- "trialFactorFinished:namespace:"
- "trialFactorProgress:namespace:fractionCompleted:status:"
- "trialFactorStarted:namespace:size:status:"
- "trialFactorTemplate"
- "trialFeatureEnabled:"
- "trialMAAssetType"
- "trialMATargetingTemplate"
- "unsubscribe:subscriptions:"
- "unsubscribe:subscriptions:queue:completion:"
- "unsubscribe:subscriptions:storeManager:configurationManager:userInitiated:"
- "unsubscribeWithConfig:completion:"
- "updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:"
- "updateNamespaces:missingRolloutsOnly:expensiveNetworking:assetSetNamespaces:updateProgress:"
- "updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:"
- "updateStarted"
- "updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:"
- "updateTrialFromAssetSetUsages:rolloutUpdateMode:expensiveNetworking:storeManager:configurationManager:progress:completion:"
- "updateTrialFromAssetSetUsages:storeManager:configurationManager:"
- "updateTrialProject:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:"
- "uppercaseLetterCharacterSet"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@16Q24"
- "v32@?0@\"NSArray\"8Q16^B24"
- "v32@?0@\"NSString\"8@\"NSSet\"16^B24"
- "v32@?0@\"NSString\"8@\"TRILevel\"16^B24"
- "v32@?0Q8Q16Q24"
- "v40@?0d8Q16Q24Q32"
- "v48@0:8@16@24Q32Q40"
- "v48@0:8@16@24^@32^@40"
- "v48@0:8@16@24d32Q40"
- "v48@0:8@16Q24Q32Q40"
- "v68@0:8@16q24B32@36@44@?52@?60"
- "v80@0:8@16@24@32@?40@?48@?56@64@72"
- "v80@0:8@16@24B32B36Q40@48@56@64@?72"
- "v88@0:8@16q24B32B36Q40@48@56@64@?72@?80"
- "valueForKey:"
- "wrapAsAnyEvent"
- "\xf0R"

```
