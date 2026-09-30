## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3515.7.1.0.0
-  __TEXT.__text: 0x7cba4
-  __TEXT.__auth_stubs: 0x1160
-  __TEXT.__objc_methlist: 0x37e8
+3520.49.1.0.0
+  __TEXT.__text: 0x82744
+  __TEXT.__auth_stubs: 0x1140
+  __TEXT.__objc_methlist: 0x3918
   __TEXT.__const: 0x1c0
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__cstring: 0xb8a3
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x67
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_fieldmd: 0x1c
-  __TEXT.__oslogstring: 0xed1c
+  __TEXT.__cstring: 0xb9a0
+  __TEXT.__oslogstring: 0xec85
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x15d0
-  __TEXT.__unwind_info: 0x13f0
-  __TEXT.__objc_classname: 0x4a2
-  __TEXT.__objc_methname: 0xa480
-  __TEXT.__objc_methtype: 0x10ef
-  __TEXT.__objc_stubs: 0x84e0
-  __DATA_CONST.__got: 0x580
-  __DATA_CONST.__const: 0x1ec0
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __TEXT.__gcc_except_tab: 0x1694
+  __TEXT.__unwind_info: 0x1570
+  __TEXT.__objc_classname: 0x50e
+  __TEXT.__objc_methname: 0xaa47
+  __TEXT.__objc_methtype: 0x1115
+  __TEXT.__objc_stubs: 0x8760
+  __DATA_CONST.__got: 0x588
+  __DATA_CONST.__const: 0x1e58
+  __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27a0
+  __DATA_CONST.__objc_selrefs: 0x2860
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x130
-  __AUTH_CONST.__auth_got: 0x8c0
-  __AUTH_CONST.__const: 0x668
+  __AUTH_CONST.__auth_got: 0x8b0
+  __AUTH_CONST.__const: 0x648
   __AUTH_CONST.__cfstring: 0x4c20
-  __AUTH_CONST.__objc_const: 0x4658
-  __AUTH_CONST.__objc_intobj: 0x240
+  __AUTH_CONST.__objc_const: 0x4928
+  __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x430
+  __AUTH.__objc_data: 0x408
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x33c
-  __DATA.__data: 0x288
-  __DATA.__bss: 0x50
-  __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0xc30
+  __DATA.__objc_ivar: 0x370
+  __DATA.__data: 0x290
+  __DATA.__bss: 0x48
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0xca8
   __DATA_DIRTY.__bss: 0x2f0
-  __DATA_DIRTY.__common: 0x58
+  __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
-  - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  - /usr/lib/swift/libswiftQuartzCore.dylib
-  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 39A05B71-9BE0-378B-90A3-3A526FF8D15B
-  Functions: 1563
-  Symbols:   5718
-  CStrings:  4639
+  UUID: 0D86A331-E43C-3F1A-8679-232F95B5AFC2
+  Functions: 1582
+  Symbols:   5766
+  CStrings:  4685
 
Symbols:
+ +[UAFAutoAssetManager lockLatestAssetSet:atomicInstance:]
+ +[UAFAutoAssetManager lockLatestAssetSet:atomicInstance:completion:]
+ +[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:fallbackAlter:atomicInstanceMetadata:]
+ +[UAFBiomeInstrumenter _collectAssetOriginMetadata:atomicInstanceOriginMetadata:entries:]
+ +[UAFBiomeInstrumenter _getAssetOriginType:]
+ +[UAFBiomeInstrumenter _getBiomeAssetSetStatus:atomicInstanceMetadata:entries:errorCodes:]
+ +[UAFBiomeInstrumenter _getBiomeStreamForAssetSetStatus:atomicInstanceMetadata:entries:errorCodes:assetSetDailyStatusEventType:]
+ +[UAFBiomeInstrumenter _getBiomeUAFAssetSet:atomicInstanceMetadata:entries:errorCodes:]
+ +[UAFBiomeInstrumenter logAssetSetDownloadEvent:atomicInstanceMetadata:entries:errorCodes:assetSetDailyStatusEventType:]
+ +[UAFCommonUtilities assistantModeDescription:]
+ +[UAFCommonUtilities assistantModeFromDescription:mode:]
+ +[UAFCommonUtilities currentAssistantMode]
+ +[UAFExpiredAssets unarchiveToken:error:]
+ +[UAFInstrumentationProvider _emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetSetDailyStatusEventType:]
+ +[UAFInstrumentationProvider _getMADownloadErrors:newerVersionError:assetSetName:assetSetID:]
+ +[UAFInstrumentationProvider logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetSetDailyStatusEventType:]
+ +[UAFManagedSubscriptions isOnDemandAssetSubscriptionAllowed]
+ +[UAFManagedSubscriptions manageAssistantSubscription:withMode:subscriber:subscriptionName:shouldReport:]
+ +[UAFManagedSubscriptions manageNLSystemLanguageSubscription:subscriber:subscriptionName:]
+ +[UAFSubscriptionStoreManager errorForSQLite:]
+ -[UAFAssetSet assetSetIdForSELF:assetSetOrigin:]
+ -[UAFAtomicInstanceMetadata .cxx_destruct]
+ -[UAFAtomicInstanceMetadata assetSetId]
+ -[UAFAtomicInstanceMetadata availableForUseError]
+ -[UAFAtomicInstanceMetadata initWithStatus:]
+ -[UAFAtomicInstanceMetadata latestDownloadedAtomicInstance]
+ -[UAFAtomicInstanceMetadata newerVersionError]
+ -[UAFAtomicInstanceMetadata originFactory]
+ -[UAFAtomicInstanceMetadata originPSUS]
+ -[UAFAtomicInstanceMetadata originType]
+ -[UAFConfigurationManager _directoryContainsPlist:]
+ -[UAFConfigurationManager _getDeprecatedDirectoriesForUsageAlias:baseURL:]
+ -[UAFConfigurationManager _getDeprecatedFilesForUsageAlias:baseURL:]
+ -[UAFConfigurationManager _getDeprecatedUsageAlias:usageAliasValue:]
+ -[UAFConfigurationManager _getURLForDeprecatedUsageAlias:usageAliasValue:]
+ -[UAFConfigurationManager _getURLForUsageAlias:usageAliasName:usageAliasValue:]
+ -[UAFConfigurationManager _getUsageAlias:usageAliasValue:]
+ -[UAFConfigurationManager getAssetSetUsagesForUsageAlias:usageAliasValue:]
+ -[UAFConfigurationManager getUsageAlias:usageAliasValue:]
+ -[UAFXPCConnection lockLatestAtomicInstance:atomicInstance:completion:]
+ -[UAFXPCService _assistantCapabilitiesUpdate]
+ -[UAFXPCService _assistantModeChanged]
+ -[UAFXPCService _assistantUpdate]
+ -[UAFXPCService assistantMode]
+ -[UAFXPCService lockLatestAtomicInstance:atomicInstance:completion:]
+ -[UAFXPCService queue]
+ GCC_except_table76
+ GCC_except_table91
+ _NSLocalizedFailureErrorKey
+ _OBJC_CLASS_$_MAAutoAssetSetAssetOriginEntry
+ _OBJC_CLASS_$_UAFAtomicInstanceMetadata
+ _OBJC_IVAR_$_UAFAtomicInstanceMetadata._assetSetId
+ _OBJC_IVAR_$_UAFAtomicInstanceMetadata._availableForUseError
+ _OBJC_IVAR_$_UAFAtomicInstanceMetadata._latestDownloadedAtomicInstance
+ _OBJC_IVAR_$_UAFAtomicInstanceMetadata._newerVersionError
+ _OBJC_IVAR_$_UAFAtomicInstanceMetadata._originFactory
+ _OBJC_IVAR_$_UAFAtomicInstanceMetadata._originPSUS
+ _OBJC_IVAR_$_UAFAtomicInstanceMetadata._originType
+ _OBJC_IVAR_$_UAFXPCService._assistantCapabilitiesChangeToken
+ _OBJC_IVAR_$_UAFXPCService._assistantLangChangeToken
+ _OBJC_IVAR_$_UAFXPCService._assistantMode
+ _OBJC_IVAR_$_UAFXPCService._assistantPrefChangeToken
+ _OBJC_IVAR_$_UAFXPCService._gmsAvailabilityToken
+ _OBJC_IVAR_$_UAFXPCService._systemLangChangeToken
+ _OBJC_METACLASS_$_UAFAtomicInstanceMetadata
+ __OBJC_$_INSTANCE_METHODS_UAFAtomicInstanceMetadata
+ __OBJC_$_INSTANCE_VARIABLES_UAFAtomicInstanceMetadata
+ __OBJC_$_PROP_LIST_UAFAtomicInstanceMetadata
+ __OBJC_CLASS_RO_$_UAFAtomicInstanceMetadata
+ __OBJC_METACLASS_RO_$_UAFAtomicInstanceMetadata
+ ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.335
+ ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.370
+ ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.371
+ ___105+[UAFManagedSubscriptions manageAssistantSubscription:withMode:subscriber:subscriptionName:shouldReport:]_block_invoke
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.460
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.461
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.471
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.472
+ ___27-[UAFXPCService runUpdates]_block_invoke.380
+ ___29+[UAFUserManager removeUser:]_block_invoke.302
+ ___31-[UAFXPCConnection _connection]_block_invoke.299
+ ___32-[UAFXPCService _startObservers]_block_invoke
+ ___32-[UAFXPCService _startObservers]_block_invoke_2
+ ___32-[UAFXPCService _startObservers]_block_invoke_3
+ ___32-[UAFXPCService _startObservers]_block_invoke_4
+ ___32-[UAFXPCService _startObservers]_block_invoke_5
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.311
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.313
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.317
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.318
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.319
+ ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke.318
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.424
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.426
+ ___40-[UAFXPCConnection expireSubscriptions:]_block_invoke.307
+ ___41-[UAFXPCService _updateShadowSiriLocale:]_block_invoke.435
+ ___42-[UAFXPCConnection diagnosticInformation:]_block_invoke.302
+ ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.359
+ ___45-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke.345
+ ___45-[UAFAutoAssetSet mapAsset:queue:completion:]_block_invoke.343
+ ___46-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke.337
+ ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke.301
+ ___48-[UAFAssetUtilities _assistantPreferencesUpdate]_block_invoke.350
+ ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.409
+ ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.411
+ ___49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke.305
+ ___50-[UAFAutoAssetSet invalidateWithQueue:completion:]_block_invoke.323
+ ___51-[UAFXPCConnection operationWithConfig:completion:]_block_invoke.301
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.350
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.351
+ ___53-[UAFAssetUtilities _downloadSiriAssetsOverCellular:]_block_invoke.340
+ ___57+[UAFAutoAssetManager lockLatestAssetSet:atomicInstance:]_block_invoke
+ ___57+[UAFAutoAssetManager lockLatestAssetSet:atomicInstance:]_block_invoke.410
+ ___57+[UAFUserManager updateLastSeenForUser:queue:completion:]_block_invoke.298
+ ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.434
+ ___61-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke.308
+ ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke.326
+ ___63-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke.322
+ ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.319
+ ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke.341
+ ___68+[UAFAutoAssetManager lockLatestAssetSet:atomicInstance:completion:]_block_invoke
+ ___68+[UAFAutoAssetManager lockLatestAssetSet:atomicInstance:completion:]_block_invoke_2
+ ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.425
+ ___68-[UAFXPCService lockLatestAtomicInstance:atomicInstance:completion:]_block_invoke
+ ___68-[UAFXPCService lockLatestAtomicInstance:atomicInstance:completion:]_block_invoke.420
+ ___70-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke.306
+ ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke.309
+ ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke_2.310
+ ___71-[UAFXPCConnection lockLatestAtomicInstance:atomicInstance:completion:]_block_invoke
+ ___71-[UAFXPCConnection lockLatestAtomicInstance:atomicInstance:completion:]_block_invoke.304
+ ___71-[UAFXPCConnection lockLatestAtomicInstance:atomicInstance:completion:]_block_invoke_2
+ ___75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke.320
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.326
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.337
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.339
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke_2.340
+ ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke.309
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.411
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.418
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.419
+ ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.443
+ ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.420
+ ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.447
+ ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.473
+ ___97+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:fallbackAlter:atomicInstanceMetadata:]_block_invoke
+ ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.327
+ ____RegisterPeriodicUAFSubscriptionActivity_block_invoke.328
+ ____RegisterXPCActivity_block_invoke.309
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___block_descriptor_73_e8_32s40s48bs56r64r_e5_v8?0ls32l8r56l8r64l8s48l8s40l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.298
+ ___block_literal_global.311
+ ___block_literal_global.313
+ ___block_literal_global.317
+ ___block_literal_global.318
+ ___block_literal_global.327
+ ___block_literal_global.329
+ ___block_literal_global.332
+ ___block_literal_global.334
+ ___block_literal_global.346
+ ___block_literal_global.349
+ ___block_literal_global.377
+ ___block_literal_global.379
+ ___block_literal_global.382
+ ___block_literal_global.407
+ ___block_literal_global.409
+ ___block_literal_global.423
+ ___block_literal_global.428
+ ___block_literal_global.430
+ ___block_literal_global.433
+ ___getAFSiriAvailabilityClass_block_invoke
+ ___getNSStringFromAFSiriOrchestrationModeSymbolLoc_block_invoke
+ ___getkAFSiriCapabilitiesDidChangeNotificationSymbolLoc_block_invoke
+ _dispatch_activate
+ _dispatch_workloop_create_inactive
+ _dispatch_workloop_set_autorelease_frequency
+ _getAFSiriAvailabilityClass.softClass
+ _getNSStringFromAFSiriOrchestrationModeSymbolLoc.ptr
+ _kUAFABCXPCFallback
+ _objc_msgSend$_assistantCapabilitiesUpdate
+ _objc_msgSend$_assistantModeChanged
+ _objc_msgSend$_assistantUpdate
+ _objc_msgSend$_collectAssetOriginMetadata:atomicInstanceOriginMetadata:entries:
+ _objc_msgSend$_directoryContainsPlist:
+ _objc_msgSend$_emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetSetDailyStatusEventType:
+ _objc_msgSend$_getAssetOriginType:
+ _objc_msgSend$_getBiomeAssetSetStatus:atomicInstanceMetadata:entries:errorCodes:
+ _objc_msgSend$_getBiomeStreamForAssetSetStatus:atomicInstanceMetadata:entries:errorCodes:assetSetDailyStatusEventType:
+ _objc_msgSend$_getBiomeUAFAssetSet:atomicInstanceMetadata:entries:errorCodes:
+ _objc_msgSend$_getDeprecatedDirectoriesForUsageAlias:baseURL:
+ _objc_msgSend$_getDeprecatedFilesForUsageAlias:baseURL:
+ _objc_msgSend$_getDeprecatedUsageAlias:usageAliasValue:
+ _objc_msgSend$_getMADownloadErrors:newerVersionError:assetSetName:assetSetID:
+ _objc_msgSend$_getURLForDeprecatedUsageAlias:usageAliasValue:
+ _objc_msgSend$_getURLForUsageAlias:usageAliasName:usageAliasValue:
+ _objc_msgSend$_getUsageAlias:usageAliasValue:
+ _objc_msgSend$assetAvailableOSBuild
+ _objc_msgSend$assetDownloadedOSBuild
+ _objc_msgSend$assetOriginEntries
+ _objc_msgSend$assetOriginType
+ _objc_msgSend$assetSetIdForSELF:assetSetOrigin:
+ _objc_msgSend$assistantModeDescription:
+ _objc_msgSend$basicOriginType:
+ _objc_msgSend$currentAssistantMode
+ _objc_msgSend$desiredOrchestrationMode
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$errorForSQLite:
+ _objc_msgSend$fromPreferences
+ _objc_msgSend$getAssetSetUsagesForUsageAlias:usageAliasValue:
+ _objc_msgSend$getUsageAlias:usageAliasValue:
+ _objc_msgSend$initWithStatus:
+ _objc_msgSend$isOnDemandAssetSubscriptionAllowed
+ _objc_msgSend$latestDownloadedAtomicInstanceFromFactoryPreinstalled
+ _objc_msgSend$lockLatestAssetSet:atomicInstance:
+ _objc_msgSend$lockLatestAssetSet:atomicInstance:completion:
+ _objc_msgSend$lockLatestAtomicInstance:atomicInstance:completion:
+ _objc_msgSend$lockedAtomicEntriesOriginReportSync:forLockedAtomicInstance:oflockedAtomicEntries:error:
+ _objc_msgSend$logAssetSetDownloadEvent:atomicInstanceMetadata:entries:errorCodes:assetSetDailyStatusEventType:
+ _objc_msgSend$logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetSetDailyStatusEventType:
+ _objc_msgSend$manageAssistantSubscription:withMode:subscriber:subscriptionName:shouldReport:
+ _objc_msgSend$manageNLSystemLanguageSubscription:subscriber:subscriptionName:
+ _objc_msgSend$originFactory
+ _objc_msgSend$originPSUS
+ _objc_msgSend$setLatestAtomicInstance:autoAssetSet:fallbackAlter:atomicInstanceMetadata:
+ _objc_msgSend$unarchiveToken:error:
- +[UAFAutoAssetManager lockLatestAssetSet:]
- +[UAFAutoAssetManager lockLatestAssetSet:completion:]
- +[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:fallbackAlter:]
- +[UAFBiomeInstrumenter _getBiomeAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:]
- +[UAFBiomeInstrumenter _getBiomeStreamForAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:assetSetDailyStatusEventType:]
- +[UAFBiomeInstrumenter _getBiomeUAFAssetSet:assetSetId:entries:errorCodes:fromPSUS:]
- +[UAFBiomeInstrumenter logAssetSetDownloadEvent:assetSetId:entries:errorCodes:fromPSUS:assetSetDailyStatusEventType:]
- +[UAFCommonUtilities deviceSupportAssistantEngine]
- +[UAFCommonUtilities gmsAllowsAssets]
- +[UAFCommonUtilities isTop13Locale:]
- +[UAFCommonUtilities isUODAttentionRequired:]
- +[UAFConfiguration sharedIpadSupported]
- +[UAFConfiguration subscriptionServiceEnabled]
- +[UAFInstrumentationProvider _emitAssetDailyStatusEvent:entries:assetSetDailyStatusEventType:]
- +[UAFInstrumentationProvider _getMADownloadErrors:assetSetName:assetSetID:]
- +[UAFInstrumentationProvider logUAFAssetSetDailyStatus:entries:assetSetDailyStatusEventType:]
- +[UAFXPCService _currentAssistantMode:]
- +[UAFXPCService _isOnDemandAssetSubscriptionAllowed]
- -[UAFAssetSet assetSetIdForSELF:stagedDuringSU:]
- -[UAFConfigurationManager getUsageAlias:includeDeprecatedValues:]
- -[UAFXPCConnection lockLatestAtomicInstance:completion:]
- -[UAFXPCService lockLatestAtomicInstance:completion:]
- GCC_except_table57
- GCC_except_table79
- _OBJC_CLASS_$__PASDeviceState
- _XPC_ACTIVITY_REQUIRES_CLASS_C
- __GMSAvailabilityDidChangeCallback
- __LanguageChangedCallback
- ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.327
- ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.361
- ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.362
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.453
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.454
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.464
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.465
- ___27-[UAFXPCService runUpdates]_block_invoke.375
- ___27-[UAFXPCService runUpdates]_block_invoke.379
- ___27-[UAFXPCService runUpdates]_block_invoke_3
- ___29+[UAFUserManager removeUser:]_block_invoke.293
- ___31-[UAFXPCConnection _connection]_block_invoke.291
- ___36+[UAFUserManager performUserCleanup]_block_invoke.302
- ___36+[UAFUserManager performUserCleanup]_block_invoke.304
- ___36+[UAFUserManager performUserCleanup]_block_invoke.308
- ___36+[UAFUserManager performUserCleanup]_block_invoke.309
- ___36+[UAFUserManager performUserCleanup]_block_invoke.310
- ___37+[UAFCommonUtilities gmsAllowsAssets]_block_invoke
- ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke.310
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.415
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.417
- ___40-[UAFXPCConnection expireSubscriptions:]_block_invoke.299
- ___41-[UAFXPCService _updateShadowSiriLocale:]_block_invoke.436
- ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke
- ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.401
- ___42-[UAFXPCConnection diagnosticInformation:]_block_invoke.294
- ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.350
- ___43+[UAFSubscriptionStoreManager writeManager]_block_invoke_2
- ___45-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke.336
- ___45-[UAFAutoAssetSet mapAsset:queue:completion:]_block_invoke.334
- ___46-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke.328
- ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke.292
- ___48-[UAFAssetUtilities _assistantPreferencesUpdate]_block_invoke.341
- ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.410
- ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.412
- ___49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke.297
- ___50-[UAFAutoAssetSet invalidateWithQueue:completion:]_block_invoke.314
- ___51-[UAFXPCConnection operationWithConfig:completion:]_block_invoke.293
- ___53+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke
- ___53+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke_2
- ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.341
- ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.342
- ___53-[UAFAssetUtilities _downloadSiriAssetsOverCellular:]_block_invoke.331
- ___53-[UAFXPCService lockLatestAtomicInstance:completion:]_block_invoke
- ___53-[UAFXPCService lockLatestAtomicInstance:completion:]_block_invoke.421
- ___56-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke
- ___56-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke.296
- ___56-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke_2
- ___57+[UAFUserManager updateLastSeenForUser:queue:completion:]_block_invoke.289
- ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.425
- ___61-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke.300
- ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke.317
- ___63-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke.313
- ___64+[UAFManagedSubscriptions manageAssistantSubscription:withMode:]_block_invoke
- ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.310
- ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke.332
- ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.407
- ___70-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke.298
- ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke.300
- ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke_2.301
- ___74+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:fallbackAlter:]_block_invoke
- ___75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke.312
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.317
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.328
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.330
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke_2.331
- ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke.300
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.402
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.403
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.404
- ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.425
- ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.405
- ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.438
- ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.466
- ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.319
- ____RegisterPeriodicUAFSubscriptionActivity_block_invoke.320
- ____RegisterXPCActivity_block_invoke.301
- ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_64_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_65_e8_32s40s48bs56r_e5_v8?0ls32l8r56l8s48l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.289
- ___block_literal_global.303
- ___block_literal_global.304
- ___block_literal_global.305
- ___block_literal_global.307
- ___block_literal_global.309
- ___block_literal_global.310
- ___block_literal_global.324
- ___block_literal_global.326
- ___block_literal_global.331
- ___block_literal_global.333
- ___block_literal_global.337
- ___block_literal_global.340
- ___block_literal_global.368
- ___block_literal_global.370
- ___block_literal_global.373
- ___block_literal_global.398
- ___block_literal_global.401
- ___block_literal_global.410
- ___block_literal_global.414
- ___block_literal_global.421
- ___block_literal_global.424
- ___getAFIsTop13LocaleSymbolLoc_block_invoke
- ___getAFSiriCapabilitiesServiceClientClass_block_invoke
- ___getAFUODAttentionRequiredSymbolLoc_block_invoke
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_UnifiedAssetFramework
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_UnifiedAssetFramework
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreAudio_$_UnifiedAssetFramework
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_UnifiedAssetFramework
- __swift_FORCE_LOAD_$_swiftCoreLocation
- __swift_FORCE_LOAD_$_swiftCoreLocation_$_UnifiedAssetFramework
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCoreMIDI_$_UnifiedAssetFramework
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_UnifiedAssetFramework
- __swift_FORCE_LOAD_$_swiftMetal
- __swift_FORCE_LOAD_$_swiftMetal_$_UnifiedAssetFramework
- __swift_FORCE_LOAD_$_swiftQuartzCore
- __swift_FORCE_LOAD_$_swiftQuartzCore_$_UnifiedAssetFramework
- __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
- __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_UnifiedAssetFramework
- __swift_FORCE_LOAD_$_swiftsimd
- __swift_FORCE_LOAD_$_swiftsimd_$_UnifiedAssetFramework
- _getAFIsTop13LocaleSymbolLoc.ptr
- _getAFSiriCapabilitiesServiceClientClass.softClass
- _getAFUODAttentionRequiredSymbolLoc.ptr
- _getGMAvailabilityWrapperClass
- _gmsAllowsAssets.assetsAllowed
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_currentAssistantMode:
- _objc_msgSend$_emitAssetDailyStatusEvent:entries:assetSetDailyStatusEventType:
- _objc_msgSend$_getBiomeAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:
- _objc_msgSend$_getBiomeStreamForAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:assetSetDailyStatusEventType:
- _objc_msgSend$_getBiomeUAFAssetSet:assetSetId:entries:errorCodes:fromPSUS:
- _objc_msgSend$_getMADownloadErrors:assetSetName:assetSetID:
- _objc_msgSend$_isOnDemandAssetSubscriptionAllowed
- _objc_msgSend$addDeprecatedValues:
- _objc_msgSend$assetSetIdForSELF:stagedDuringSU:
- _objc_msgSend$deviceSupportAssistantEngine
- _objc_msgSend$getShouldNotDownloadOrServeAppleIntelligenceAssetsWithCompletionHandler:
- _objc_msgSend$getUsageAlias:includeDeprecatedValues:
- _objc_msgSend$gmsAllowsAssets
- _objc_msgSend$isClassCLocked
- _objc_msgSend$lockLatestAssetSet:
- _objc_msgSend$lockLatestAssetSet:completion:
- _objc_msgSend$lockLatestAtomicInstance:completion:
- _objc_msgSend$logAssetSetDownloadEvent:assetSetId:entries:errorCodes:fromPSUS:assetSetDailyStatusEventType:
- _objc_msgSend$logUAFAssetSetDailyStatus:entries:assetSetDailyStatusEventType:
- _objc_msgSend$new
- _objc_msgSend$runBlockWhenDeviceIsClassCUnlocked:
- _objc_msgSend$setLatestAtomicInstance:autoAssetSet:fallbackAlter:
- _objc_msgSend$sharedIpadSupported
- _objc_msgSend$shouldDownloadAssetsForSiriSystemAssistantExperienceSync
- _objc_msgSend$subjectToAppleIntelligenceWaitlist
- _objc_msgSend$subscriptionServiceEnabled
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "%s Assistant mode changed to : %{public}@"
+ "%s Could not create new subscription database: %d %@"
+ "%s Could not load usage alias %{public}@ with value %{public}@"
+ "%s Could not open database (%@): %{public}@"
+ "%s Could not prepare statements after database recreation: %{public}@"
+ "%s Could not retrieve subscriptions, device is currently locked"
+ "%s Could not retrieve the asset origin metadata for auto asset set %{public}@ atomic instance %{public}@ : %{public}@"
+ "%s Creating AutoAssetSet %{public}@ for staging."
+ "%s Emitting daily status scheduled event for asset set %{public}@, Asset Set Preinstallation type: %ld"
+ "%s Failed to load UAFUsageAliasConfiguration %@ with usageAliasValue %@"
+ "%s Failed to load deprecated UAFUsageAliasConfiguration %@ with usageAliasValue %@"
+ "%s Finished changing subscriptions for user: '%@', subscriber: '%{public}@': error: %{public}@, subscriptions: '%{public}@'"
+ "%s Input atomic instance '%{public}@' for asset set '%{public}@' matches short term locker atomic instance '%{public}@', skipping"
+ "%s Loading deprecated values to process usage alias %{public}@ with value %{public}@"
+ "%s Missing atomic entry for specifier %{public}@ in asset set %{public}@ (atomic instance: %{public}@)"
+ "%s Not updating Assistant mode as it is unchanged from : %{public}@"
+ "%s Performing database upgrade check"
+ "%s Processing update to assistant capabilities"
+ "%s Running subscription update"
+ "%s Unable to identify current user, falling back to daemon to determine user: %@"
+ "+[UAFAutoAssetManager lockLatestAssetSet:atomicInstance:]"
+ "+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:fallbackAlter:atomicInstanceMetadata:]"
+ "+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:fallbackAlter:atomicInstanceMetadata:]_block_invoke"
+ "+[UAFBiomeInstrumenter _collectAssetOriginMetadata:atomicInstanceOriginMetadata:entries:]"
+ "+[UAFBiomeInstrumenter _getBiomeUAFAssetSet:atomicInstanceMetadata:entries:errorCodes:]"
+ "+[UAFBiomeInstrumenter logAssetSetDownloadEvent:atomicInstanceMetadata:entries:errorCodes:assetSetDailyStatusEventType:]"
+ "+[UAFInstrumentationProvider _emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetSetDailyStatusEventType:]"
+ "+[UAFInstrumentationProvider _getMADownloadErrors:newerVersionError:assetSetName:assetSetID:]"
+ "+[UAFInstrumentationProvider logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetSetDailyStatusEventType:]"
+ "+[UAFManagedSubscriptions manageAssistantSubscription:withMode:subscriber:subscriptionName:shouldReport:]"
+ "-[UAFAssetSet assetSetIdForSELF:assetSetOrigin:]"
+ "-[UAFConfigurationManager _getDeprecatedUsageAlias:usageAliasValue:]"
+ "-[UAFConfigurationManager _getUsageAlias:usageAliasValue:]"
+ "-[UAFConfigurationManager getUsageAlias:usageAliasValue:]"
+ "-[UAFXPCConnection lockLatestAtomicInstance:atomicInstance:completion:]_block_invoke"
+ "-[UAFXPCConnection lockLatestAtomicInstance:atomicInstance:completion:]_block_invoke_2"
+ "-[UAFXPCService _assistantCapabilitiesUpdate]"
+ "-[UAFXPCService _assistantModeChanged]"
+ "-[UAFXPCService lockLatestAtomicInstance:atomicInstance:completion:]"
+ "-[UAFXPCService lockLatestAtomicInstance:atomicInstance:completion:]_block_invoke"
+ "-[UAFXPCService runUpdates]_block_invoke_2"
+ "@20@0:8i16"
+ "@28@0:8B16^q20"
+ "@44@0:8@16@24B32^@36"
+ "@56@0:8@16@24@32@40Q48"
+ "AFSiriAvailability"
+ "B32@0:8@16^Q24"
+ "Collection of Auto Asset Set Origin"
+ "Database version mismatch"
+ "NSStringFromAFSiriOrchestrationMode"
+ "T@\"NSError\",R,V_availableForUseError"
+ "T@\"NSError\",R,V_newerVersionError"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "T@\"NSString\",R,V_assetSetId"
+ "T@\"NSString\",R,V_latestDownloadedAtomicInstance"
+ "TB,R,V_originFactory"
+ "TB,R,V_originPSUS"
+ "TQ,R,N,V_assistantMode"
+ "Tq,R,V_originType"
+ "UAFAtomicInstanceMetadata"
+ "XPCProxy Fallback"
+ "_assetSetId"
+ "_assistantCapabilitiesChangeToken"
+ "_assistantCapabilitiesUpdate"
+ "_assistantLangChangeToken"
+ "_assistantMode"
+ "_assistantModeChanged"
+ "_assistantPrefChangeToken"
+ "_assistantUpdate"
+ "_availableForUseError"
+ "_collectAssetOriginMetadata:atomicInstanceOriginMetadata:entries:"
+ "_directoryContainsPlist:"
+ "_emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetSetDailyStatusEventType:"
+ "_getAssetOriginType:"
+ "_getBiomeAssetSetStatus:atomicInstanceMetadata:entries:errorCodes:"
+ "_getBiomeStreamForAssetSetStatus:atomicInstanceMetadata:entries:errorCodes:assetSetDailyStatusEventType:"
+ "_getBiomeUAFAssetSet:atomicInstanceMetadata:entries:errorCodes:"
+ "_getDeprecatedDirectoriesForUsageAlias:baseURL:"
+ "_getDeprecatedFilesForUsageAlias:baseURL:"
+ "_getDeprecatedUsageAlias:usageAliasValue:"
+ "_getMADownloadErrors:newerVersionError:assetSetName:assetSetID:"
+ "_getURLForDeprecatedUsageAlias:usageAliasValue:"
+ "_getURLForUsageAlias:usageAliasName:usageAliasValue:"
+ "_getUsageAlias:usageAliasValue:"
+ "_gmsAvailabilityToken"
+ "_latestDownloadedAtomicInstance"
+ "_newerVersionError"
+ "_originFactory"
+ "_originPSUS"
+ "_originType"
+ "_systemLangChangeToken"
+ "assetAvailableOSBuild"
+ "assetDownloadedOSBuild"
+ "assetOriginEntries"
+ "assetOriginType"
+ "assetSetIdForSELF:assetSetOrigin:"
+ "assistantMode"
+ "assistantModeDescription:"
+ "assistantModeFromDescription:mode:"
+ "basicOriginType:"
+ "consoleuser"
+ "currentAssistantMode"
+ "currentuser"
+ "database"
+ "desiredOrchestrationMode"
+ "dictionaryWithCapacity:"
+ "errorForSQLite:"
+ "fromPreferences"
+ "getAssetSetUsagesForUsageAlias:usageAliasValue:"
+ "getUsageAlias:usageAliasValue:"
+ "i24@0:8q16"
+ "initWithStatus:"
+ "isOnDemandAssetSubscriptionAllowed"
+ "kAFSiriCapabilitiesDidChangeNotification"
+ "latestDownloadedAtomicInstanceFromFactoryPreinstalled"
+ "lockLatestAssetSet:atomicInstance:"
+ "lockLatestAssetSet:atomicInstance:completion:"
+ "lockLatestAtomicInstance:atomicInstance:completion:"
+ "lockedAtomicEntriesOriginReportSync:forLockedAtomicInstance:oflockedAtomicEntries:error:"
+ "logAssetSetDownloadEvent:atomicInstanceMetadata:entries:errorCodes:assetSetDailyStatusEventType:"
+ "logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetSetDailyStatusEventType:"
+ "manageAssistantSubscription:withMode:subscriber:subscriptionName:shouldReport:"
+ "manageNLSystemLanguageSubscription:subscriber:subscriptionName:"
+ "nil database file name"
+ "originFactory"
+ "originPSUS"
+ "originType"
+ "q"
+ "q16@0:8"
+ "queue"
+ "setLatestAtomicInstance:autoAssetSet:fallbackAlter:atomicInstanceMetadata:"
+ "unarchiveToken:error:"
+ "v48@0:8@16@24@32Q40"
+ "v52@0:8@16Q24@32@40B48"
+ "v56@0:8@16@24@32@40Q48"
- "%s Asset set %{public}@ is not allowed on this device"
- "%s Attempt to open database before class c unlock"
- "%s AutoAssetSet %{public}@ not previously initialized. Creating a new one for staging."
- "%s Changed subscriptions for user: '%@', subscriber: '%{public}@': '%{public}@'"
- "%s Could not create new subscription database: %d"
- "%s Could not get AFSiriCapabilitiesServiceClient class"
- "%s Could not initialize a new AFSiriCapabilitiesClient"
- "%s Could not prepare statements after database recreation"
- "%s Could not process subscription for usage alias %{public}@"
- "%s Device doesn't support PASDeviceState. Performing database upgrade check"
- "%s Device has been unlocked, performing database upgrade check"
- "%s Device has been unlocked, running subscription update"
- "%s Device is locked, scheduling subscription update for unlock"
- "%s Device is unlocked, running subscription update"
- "%s Emitting daily status scheduled event for asset set %{public}@, pre-staged: %d"
- "%s Failed to add deprecated values from %{public}@"
- "%s Failed to determine if Apple Intelligence Assets allowed: %{public}@"
- "%s Loading deprecated values to process subscription for usage alias %{public}@ with value %{public}@"
- "%s Not trying to load %@ as a deprecated usage alias configuration file as it for usage alias %{public}@, not %{public}@"
- "%s Not trying to load %@ as a deprecated usage alias configuration file as it lacks the \"plist\" extension"
- "%s Received request from pid %d while subscription service disabled"
- "%s Subscription %@ references unknown usage alias %@"
- "%s Unable to identify current user, falling back to daemon determing user: %@"
- "%s nil database filename"
- "+[UAFAutoAssetManager lockLatestAssetSet:]"
- "+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:fallbackAlter:]"
- "+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:fallbackAlter:]_block_invoke"
- "+[UAFBiomeInstrumenter logAssetSetDownloadEvent:assetSetId:entries:errorCodes:fromPSUS:assetSetDailyStatusEventType:]"
- "+[UAFCommonUtilities deviceSupportAssistantEngine]"
- "+[UAFCommonUtilities gmsAllowsAssets]_block_invoke"
- "+[UAFInstrumentationProvider _emitAssetDailyStatusEvent:entries:assetSetDailyStatusEventType:]"
- "+[UAFInstrumentationProvider _getMADownloadErrors:assetSetName:assetSetID:]"
- "+[UAFInstrumentationProvider logUAFAssetSetDailyStatus:entries:assetSetDailyStatusEventType:]"
- "+[UAFManagedSubscriptions manageAssistantSubscription:withMode:]"
- "+[UAFSubscriptionStoreManager writeManager]_block_invoke_2"
- "-[UAFAssetSet assetSetIdForSELF:stagedDuringSU:]"
- "-[UAFConfigurationManager getUsageAlias:includeDeprecatedValues:]"
- "-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke"
- "-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke_2"
- "-[UAFXPCService lockLatestAtomicInstance:completion:]"
- "-[UAFXPCService lockLatestAtomicInstance:completion:]_block_invoke"
- "-[UAFXPCService runUpdates]_block_invoke_3"
- "@28@0:8B16^B20"
- "@52@0:8@16@24@32@40B48"
- "@60@0:8@16@24@32@40B48Q52"
- "AFIsTop13Locale"
- "AFSiriCapabilitiesServiceClient"
- "AFUODAttentionRequired"
- "Carry"
- "Q24@0:8^@16"
- "Request to UAF subscription service when subscription service is disabled"
- "Subscription %@ references unknown usage alias %@"
- "UAFRegisterXPCActivities"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "_currentAssistantMode:"
- "_emitAssetDailyStatusEvent:entries:assetSetDailyStatusEventType:"
- "_getBiomeAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:"
- "_getBiomeStreamForAssetSetStatus:assetSetId:entries:errorCodes:fromPSUS:assetSetDailyStatusEventType:"
- "_getBiomeUAFAssetSet:assetSetId:entries:errorCodes:fromPSUS:"
- "_getMADownloadErrors:assetSetName:assetSetID:"
- "_isOnDemandAssetSubscriptionAllowed"
- "assetSetIdForSELF:stagedDuringSU:"
- "assistantengine"
- "deviceSupportAssistantEngine"
- "full"
- "getShouldNotDownloadOrServeAppleIntelligenceAssetsWithCompletionHandler:"
- "getUsageAlias:includeDeprecatedValues:"
- "gmsAllowsAssets"
- "hybrid"
- "isClassCLocked"
- "isTop13Locale:"
- "isUODAttentionRequired:"
- "legacy"
- "lockLatestAssetSet:"
- "lockLatestAssetSet:completion:"
- "lockLatestAtomicInstance:completion:"
- "logAssetSetDownloadEvent:assetSetId:entries:errorCodes:fromPSUS:assetSetDailyStatusEventType:"
- "logUAFAssetSetDailyStatus:entries:assetSetDailyStatusEventType:"
- "new"
- "runBlockWhenDeviceIsClassCUnlocked:"
- "setLatestAtomicInstance:autoAssetSet:fallbackAlter:"
- "sharedIpadSupported"
- "shared_ipad_support"
- "shouldDownloadAssetsForSiriSystemAssistantExperienceSync"
- "subscriptionServiceEnabled"
- "subscription_service"
- "v40@0:8@16@24Q32"
- "v60@0:8@16@24@32@40B48Q52"

```
