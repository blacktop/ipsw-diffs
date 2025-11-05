## SpotlightResources

> `/System/Library/PrivateFrameworks/SpotlightResources.framework/Versions/A/SpotlightResources`

```diff

-2328.7.8.7.0
-  __TEXT.__text: 0x1cb0c
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_methlist: 0xf44
-  __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x138d
-  __TEXT.__oslogstring: 0x16ab
-  __TEXT.__gcc_except_tab: 0x770
-  __TEXT.__unwind_info: 0x530
-  __TEXT.__objc_classname: 0x131
-  __TEXT.__objc_methname: 0x2b76
-  __TEXT.__objc_methtype: 0x4af
-  __TEXT.__objc_stubs: 0x2dc0
-  __DATA_CONST.__got: 0x1c8
+2333.22.13.7.0
+  __TEXT.__text: 0x26c60
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__objc_methlist: 0x13e8
+  __TEXT.__const: 0xc8
+  __TEXT.__gcc_except_tab: 0x964
+  __TEXT.__cstring: 0x169e
+  __TEXT.__oslogstring: 0x1a57
+  __TEXT.__unwind_info: 0x780
+  __TEXT.__objc_classname: 0x1b4
+  __TEXT.__objc_methname: 0x3254
+  __TEXT.__objc_methtype: 0x57f
+  __TEXT.__objc_stubs: 0x3340
+  __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0xa0
-  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd28
-  __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__objc_arraydata: 0x970
-  __AUTH_CONST.__auth_got: 0x1e8
-  __AUTH_CONST.__const: 0x700
-  __AUTH_CONST.__cfstring: 0x3b60
-  __AUTH_CONST.__objc_const: 0x19e8
+  __DATA_CONST.__objc_selrefs: 0xf40
+  __DATA_CONST.__objc_superrefs: 0x90
+  __DATA_CONST.__objc_arraydata: 0x980
+  __AUTH_CONST.__auth_got: 0x2b8
+  __AUTH_CONST.__const: 0xe60
+  __AUTH_CONST.__cfstring: 0x3d40
+  __AUTH_CONST.__objc_const: 0x1e98
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x130
-  __DATA.__data: 0x248
-  __DATA.__bss: 0x290
+  __AUTH.__objc_data: 0x690
+  __DATA.__objc_ivar: 0x178
+  __DATA.__data: 0x3d8
+  __DATA.__bss: 0x308
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  - /System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreParsec.framework/Versions/A/CoreParsec
   - /System/Library/PrivateFrameworks/DataDeliveryServices.framework/Versions/A/DataDeliveryServices
   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/Versions/A/MetadataUtilities
+  - /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset
   - /System/Library/PrivateFrameworks/SearchFoundation.framework/Versions/A/SearchFoundation
   - /System/Library/PrivateFrameworks/Trial.framework/Versions/A/Trial
   - /System/Library/PrivateFrameworks/TrialProto.framework/Versions/A/TrialProto
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 28FC8284-26B6-3C70-B0A8-A71D445B60E5
-  Functions: 500
-  Symbols:   1350
-  CStrings:  1754
+  UUID: C299A416-304E-3665-BFFD-A429ACF1D379
+  Functions: 740
+  Symbols:   1818
+  CStrings:  1947
 
Symbols:
+ +[SRAssetBundleCache cacheFilePath]
+ +[SRAssetBundleCache sharedInstance]
+ +[SRAssetBundleCache sharedInstance].cold.1
+ +[SRDefaultsManager sharedDefaultsManager].cold.1
+ +[SRLanguageConfiguration configuration]
+ +[SRLanguageConfiguration configuration].cold.1
+ +[SRParameter boolNil].cold.1
+ +[SRParameter boolNo].cold.1
+ +[SRParameter boolYes].cold.1
+ +[SRParameter doubleMin].cold.1
+ +[SRParameter doubleNil].cold.1
+ +[SRParameter filePathNil].cold.1
+ +[SRParameter longNil].cold.1
+ +[SRParameter longZero].cold.1
+ +[SRParameter stringNil].cold.1
+ +[SRResourcesManager fetchOverrideList].cold.1
+ +[SRResourcesManager fetchParameterList].cold.1
+ +[SRResourcesManager resourcePath]
+ +[SRResourcesManager sharedResourcesManager].cold.1
+ +[SRXPCConnection sharedConnection]
+ +[SRXPCConnection sharedConnection].cold.1
+ +[SRXPCListener handleMessage:error:]
+ +[SRXPCListener handleMessage:error:].cold.1
+ +[SSTrialManager setTrialOverridePath].cold.1
+ +[SSTrialManager sharedSpotlightKnowledgeTrialClient].cold.1
+ +[SSTrialManager sharedSpotlightKnowledgeTrialManager].cold.1
+ +[SSTrialManager sharedSpotlightMailTrialManager].cold.1
+ +[SSTrialManager sharedSpotlightModelTrialManager].cold.1
+ +[SSTrialManager sharedSpotlightPolicyTrialManager].cold.1
+ +[SSTrialManager sharedSpotlightRankingTrialManager].cold.1
+ +[SSTrialManager sharedSpotlightTrialClient].cold.1
+ +[SSTrialManager sharedSpotlightUITrialManager].cold.1
+ -[SRAssertion .cxx_destruct]
+ -[SRAssertion assertionID]
+ -[SRAssertion assetType]
+ -[SRAssertion deliveryType]
+ -[SRAssertion hash]
+ -[SRAssertion initWithAssertionID:]
+ -[SRAssertion initWithAssertionID:].cold.1
+ -[SRAssertion initWithAssetType:language:deliveryType:]
+ -[SRAssertion isEqual:]
+ -[SRAssertion language]
+ -[SRAsset deliveryTypeString]
+ -[SRAssetBundle initWithLocale:contentVersions:]
+ -[SRAssetBundle shouldUpdateForContentVersions:]
+ -[SRAssetBundleCache .cxx_destruct]
+ -[SRAssetBundleCache dumpCache]
+ -[SRAssetBundleCache flushCacheToFile]
+ -[SRAssetBundleCache flushCacheToFile].cold.1
+ -[SRAssetBundleCache init]
+ -[SRAssetBundleCache loadCacheFromFile]
+ -[SRAssetBundleCache loadCacheFromFile].cold.1
+ -[SRAssetBundleCache queryCache:]
+ -[SRAssetBundleCache queryServerCache:completion:]
+ -[SRAssetBundleCache removeAssetBundleWithAssetType:language:deliveryType:]
+ -[SRAssetBundleCache updateCacheWithResults:]
+ -[SRAssetBundleCache upsertAssetBundleWithAssetType:language:deliveryType:contentVersion:path:]
+ -[SRAssetBundleCacheEntry .cxx_destruct]
+ -[SRAssetBundleCacheEntry assetTypeString]
+ -[SRAssetBundleCacheEntry assetType]
+ -[SRAssetBundleCacheEntry contentVersion]
+ -[SRAssetBundleCacheEntry deliveryTypeString]
+ -[SRAssetBundleCacheEntry deliveryType]
+ -[SRAssetBundleCacheEntry initWithAssetType:language:deliveryType:]
+ -[SRAssetBundleCacheEntry isResultNone]
+ -[SRAssetBundleCacheEntry isResult]
+ -[SRAssetBundleCacheEntry language]
+ -[SRAssetBundleCacheEntry makeResultNone]
+ -[SRAssetBundleCacheEntry makeResultNone].cold.1
+ -[SRAssetBundleCacheEntry makeResultWithContentVersion:path:]
+ -[SRAssetBundleCacheEntry makeResultWithContentVersion:path:].cold.1
+ -[SRAssetBundleCacheEntry makeResultWithContentVersion:path:].cold.2
+ -[SRAssetBundleCacheEntry makeResultWithContentVersion:path:].cold.3
+ -[SRAssetBundleCacheEntry makeResultWithContentVersion:path:].cold.4
+ -[SRAssetBundleCacheEntry path]
+ -[SRAssetBundleQuery .cxx_destruct]
+ -[SRAssetBundleQuery addQueryEntriesForLanguage:assetType:deliveryTypes:]
+ -[SRAssetBundleQuery addQueryEntriesForLanguage:assetType:deliveryTypes:].cold.1
+ -[SRAssetBundleQuery count]
+ -[SRAssetBundleQuery enumerateEntriesForLanguage:block:]
+ -[SRAssetBundleQuery initWithXPCObject:isResult:]
+ -[SRAssetBundleQuery initWithXPCObject:isResult:].cold.1
+ -[SRAssetBundleQuery init]
+ -[SRAssetBundleQuery queryEntries]
+ -[SRAssetBundleQuery xpcObject]
+ -[SRDefaultsManager _loadAssets:shouldUpdate:]
+ -[SRDefaultsManager addFetchForLanguage:]
+ -[SRDefaultsManager assetBundleForLocale:client:force:]
+ -[SRDefaultsManager cachedOTALanguages]
+ -[SRDefaultsManager fetchedLanguages]
+ -[SRDefaultsManager loadDefaultsForLocale:reload:force:]
+ -[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]
+ -[SRDefaultsManager loadSystemAssetsForLanguage:assetTypes:]
+ -[SRDefaultsManager loadSystemAssetsForLanguage:assetTypes:].cold.1
+ -[SRDefaultsManager loadTestAssetsForLanguage:assetTypes:]
+ -[SRDefaultsManager notifyObserversWithLanguage:contentVersions:]
+ -[SRDefaultsManager notifyQueue]
+ -[SRDefaultsManager refreshCacheForLanguages:completion:]
+ -[SRDefaultsManager refreshCacheForLanguages:completion:].cold.1
+ -[SRDefaultsManager requestedOTALanguages]
+ -[SRDefaultsManager shouldReloadLanguage:forContentVersions:]
+ -[SRDefaultsManager updateContentVersions:forLanguage:]
+ -[SRDefaultsManager updateFetchedLanguages:]
+ -[SRLanguageConfiguration .cxx_destruct]
+ -[SRLanguageConfiguration description]
+ -[SRLanguageConfiguration init]
+ -[SRLanguageConfiguration isSupportedLanguage:deliveryType:]
+ -[SRLanguageConfiguration loadSupportedLanguages:]
+ -[SRResources didUpdateDefaultsWithLanguage:contentVersions:trial:]
+ -[SRResources forceLoad]
+ -[SRResourcesManager fetchAllParametersForLanguages:]
+ -[SRResourcesManager handleAssetsCommand:]
+ -[SRResourcesManager handleAssetsCommand:].cold.1
+ -[SRXPCConnection .cxx_destruct]
+ -[SRXPCConnection init]
+ -[SRXPCConnection init].cold.1
+ -[SRXPCConnection sendMessageAsync:completion:]
+ -[SRXPCConnection sendMessageAsync:completion:].cold.1
+ GCC_except_table103
+ GCC_except_table116
+ GCC_except_table13
+ GCC_except_table130
+ GCC_except_table132
+ GCC_except_table134
+ GCC_except_table140
+ GCC_except_table142
+ GCC_except_table147
+ GCC_except_table150
+ GCC_except_table152
+ GCC_except_table155
+ GCC_except_table156
+ GCC_except_table157
+ GCC_except_table158
+ GCC_except_table30
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table4
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table55
+ GCC_except_table85
+ GCC_except_table86
+ GCC_except_table9
+ GCC_except_table94
+ OBJC_IVAR_$_SRAssertion._assertionID
+ OBJC_IVAR_$_SRAssertion._assetType
+ OBJC_IVAR_$_SRAssertion._deliveryType
+ OBJC_IVAR_$_SRAssertion._isSR
+ OBJC_IVAR_$_SRAssertion._language
+ OBJC_IVAR_$_SRAssetBundle._contentVersions
+ OBJC_IVAR_$_SRAssetBundleCache._cache
+ OBJC_IVAR_$_SRAssetBundleCacheEntry._assetType
+ OBJC_IVAR_$_SRAssetBundleCacheEntry._contentVersion
+ OBJC_IVAR_$_SRAssetBundleCacheEntry._deliveryType
+ OBJC_IVAR_$_SRAssetBundleCacheEntry._isResult
+ OBJC_IVAR_$_SRAssetBundleCacheEntry._language
+ OBJC_IVAR_$_SRAssetBundleCacheEntry._path
+ OBJC_IVAR_$_SRAssetBundleQuery._queryEntries
+ OBJC_IVAR_$_SRDefaultsManager._cachedOTALanguages
+ OBJC_IVAR_$_SRDefaultsManager._fetchedLanguages
+ OBJC_IVAR_$_SRDefaultsManager._langConfig
+ OBJC_IVAR_$_SRDefaultsManager._loadedContentVersions
+ OBJC_IVAR_$_SRDefaultsManager._notifyQueue
+ OBJC_IVAR_$_SRDefaultsManager._requestedOTALanguages
+ OBJC_IVAR_$_SRLanguageConfiguration._supportedLanguageMap
+ OBJC_IVAR_$_SRResources._forceLoad
+ OBJC_IVAR_$_SRXPCConnection._queue
+ SRGetResourcePath.cold.1
+ SRGetResourcePath.onceToken
+ SRGetResourcePath.sResourcePath
+ SRIsAppleInternalInstall.cold.1
+ SRIsRunningInServer.cold.1
+ SRIsRunningInServer.onceToken
+ SRIsRunningInServer.sRunningInServer
+ SRLogCategoryAssets.assetsLog
+ SRLogCategoryAssets.cold.1
+ SRLogCategoryAssets.onceToken
+ SRLogCategoryGeneral.cold.1
+ SRLogCategoryLifeCycle.cold.1
+ SRLogCategorySafety.cold.1
+ SRLogCategoryTrial.cold.1
+ SRLogCategoryTrial.onceToken
+ SRLogCategoryTrial.trialLog
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetLocalCenter
+ _OBJC_CLASS_$_CSXPCConnection
+ _OBJC_CLASS_$_MAAsset
+ _OBJC_CLASS_$_SRAssertion
+ _OBJC_CLASS_$_SRAssetBundleCache
+ _OBJC_CLASS_$_SRAssetBundleCacheEntry
+ _OBJC_CLASS_$_SRAssetBundleQuery
+ _OBJC_CLASS_$_SRLanguageConfiguration
+ _OBJC_CLASS_$_SRXPCConnection
+ _OBJC_CLASS_$_SRXPCListener
+ _OBJC_METACLASS_$_CSXPCConnection
+ _OBJC_METACLASS_$_SRAssertion
+ _OBJC_METACLASS_$_SRAssetBundleCache
+ _OBJC_METACLASS_$_SRAssetBundleCacheEntry
+ _OBJC_METACLASS_$_SRAssetBundleQuery
+ _OBJC_METACLASS_$_SRLanguageConfiguration
+ _OBJC_METACLASS_$_SRXPCConnection
+ _OBJC_METACLASS_$_SRXPCListener
+ _OUTLINED_FUNCTION_6
+ _SRGetResourcePath
+ _SRIsRunningInServer
+ _SRLogCategoryAssets
+ _SRLogCategoryTrial
+ __38-[SRAssetBundleCache flushCacheToFile]_block_invoke.189
+ __38-[SRAssetBundleCache flushCacheToFile]_block_invoke.189.cold.1
+ __38-[SRAssetBundleCache flushCacheToFile]_block_invoke_2.cold.1
+ __39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.180
+ __39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.180.cold.1
+ __39-[SRAssetBundleCache loadCacheFromFile]_block_invoke_2.cold.1
+ __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.445
+ __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.445.cold.1
+ __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.445.cold.10
+ __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.445.cold.11
+ __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.445.cold.12
+ __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.445.cold.2
+ __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.445.cold.3
+ __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.445.cold.4
+ __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.445.cold.5
+ __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.445.cold.6
+ __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.445.cold.7
+ __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.445.cold.8
+ __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.445.cold.9
+ __47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.411
+ __47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.411.cold.1
+ __47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.423
+ __47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.423.cold.1
+ __47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.424
+ __47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.429
+ __47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.429.cold.1
+ __47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke_2.412
+ __47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke_2.425
+ __47-[SRXPCConnection sendMessageAsync:completion:]_block_invoke.cold.1
+ __49-[SRAssetBundleQuery initWithXPCObject:isResult:]_block_invoke.cold.1
+ __51-[SRDefaultsManager loadDefaultsFromDefaultAssets:]_block_invoke.392
+ __64-[SRResourcesManager loadAllParametersForClient:locale:options:]_block_invoke.cold.1
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.451
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.451.cold.1
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.451.cold.2
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.451.cold.3
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.451.cold.4
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.452
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.454
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.454.cold.1
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.454.cold.2
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.458
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.462
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.462.cold.1
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.463
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.463.cold.1
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.463.cold.2
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.464
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.467
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.467.cold.1
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.470
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.470.cold.1
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.470.cold.2
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.470.cold.3
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.471
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.472
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.473
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.473.cold.1
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.474
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.474.cold.1
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.475
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.479
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.479.cold.1
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.459
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.459.cold.1
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.476
+ __70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.476.cold.1
+ __73-[SRAssetBundleQuery addQueryEntriesForLanguage:assetType:deliveryTypes:]_block_invoke.cold.1
+ __OBJC_$_CLASS_METHODS_SRAssetBundleCache
+ __OBJC_$_CLASS_METHODS_SRLanguageConfiguration
+ __OBJC_$_CLASS_METHODS_SRXPCConnection
+ __OBJC_$_CLASS_METHODS_SRXPCListener
+ __OBJC_$_INSTANCE_METHODS_SRAssertion
+ __OBJC_$_INSTANCE_METHODS_SRAssetBundleCache
+ __OBJC_$_INSTANCE_METHODS_SRAssetBundleCacheEntry
+ __OBJC_$_INSTANCE_METHODS_SRAssetBundleQuery
+ __OBJC_$_INSTANCE_METHODS_SRLanguageConfiguration
+ __OBJC_$_INSTANCE_METHODS_SRXPCConnection
+ __OBJC_$_INSTANCE_VARIABLES_SRAssertion
+ __OBJC_$_INSTANCE_VARIABLES_SRAssetBundleCache
+ __OBJC_$_INSTANCE_VARIABLES_SRAssetBundleCacheEntry
+ __OBJC_$_INSTANCE_VARIABLES_SRAssetBundleQuery
+ __OBJC_$_INSTANCE_VARIABLES_SRLanguageConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_SRXPCConnection
+ __OBJC_$_PROP_LIST_SRAssertion
+ __OBJC_$_PROP_LIST_SRAssetBundleCacheEntry
+ __OBJC_$_PROP_LIST_SRAssetBundleQuery
+ __OBJC_$_PROP_LIST_SRDefaultsManagerDelegate
+ __OBJC_CLASS_RO_$_SRAssertion
+ __OBJC_CLASS_RO_$_SRAssetBundleCache
+ __OBJC_CLASS_RO_$_SRAssetBundleCacheEntry
+ __OBJC_CLASS_RO_$_SRAssetBundleQuery
+ __OBJC_CLASS_RO_$_SRLanguageConfiguration
+ __OBJC_CLASS_RO_$_SRXPCConnection
+ __OBJC_CLASS_RO_$_SRXPCListener
+ __OBJC_METACLASS_RO_$_SRAssertion
+ __OBJC_METACLASS_RO_$_SRAssetBundleCache
+ __OBJC_METACLASS_RO_$_SRAssetBundleCacheEntry
+ __OBJC_METACLASS_RO_$_SRAssetBundleQuery
+ __OBJC_METACLASS_RO_$_SRLanguageConfiguration
+ __OBJC_METACLASS_RO_$_SRXPCConnection
+ __OBJC_METACLASS_RO_$_SRXPCListener
+ ___27-[SRAssetBundleQuery count]_block_invoke
+ ___27-[SRAssetBundleQuery count]_block_invoke_2
+ ___31-[SRAssetBundleCache dumpCache]_block_invoke
+ ___31-[SRAssetBundleCache dumpCache]_block_invoke_2
+ ___31-[SRAssetBundleCache dumpCache]_block_invoke_3
+ ___31-[SRAssetBundleQuery xpcObject]_block_invoke
+ ___31-[SRAssetBundleQuery xpcObject]_block_invoke_2
+ ___31-[SRAssetBundleQuery xpcObject]_block_invoke_3
+ ___33-[SRAssetBundleCache queryCache:]_block_invoke
+ ___33-[SRAssetBundleCache queryCache:]_block_invoke_2
+ ___33-[SRAssetBundleCache queryCache:]_block_invoke_3
+ ___35+[SRXPCConnection sharedConnection]_block_invoke
+ ___36+[SRAssetBundleCache sharedInstance]_block_invoke
+ ___37-[SRDefaultsManager fetchedLanguages]_block_invoke
+ ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke
+ ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke_2
+ ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke
+ ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke_2
+ ___40+[SRLanguageConfiguration configuration]_block_invoke
+ ___41-[SRDefaultsManager addFetchForLanguage:]_block_invoke
+ ___44-[SRDefaultsManager updateFetchedLanguages:]_block_invoke
+ ___45-[SRAssetBundleCache updateCacheWithResults:]_block_invoke
+ ___45-[SRAssetBundleCache updateCacheWithResults:]_block_invoke_2
+ ___45-[SRAssetBundleCache updateCacheWithResults:]_block_invoke_3
+ ___46-[SRDefaultsManager _loadAssets:shouldUpdate:]_block_invoke
+ ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke_3
+ ___47-[SRXPCConnection sendMessageAsync:completion:]_block_invoke
+ ___48-[SRAssetBundle shouldUpdateForContentVersions:]_block_invoke
+ ___48-[SRAssetBundle shouldUpdateForContentVersions:]_block_invoke_2
+ ___49-[SRAssetBundleQuery initWithXPCObject:isResult:]_block_invoke
+ ___50-[SRAssetBundleCache queryServerCache:completion:]_block_invoke
+ ___55-[SRDefaultsManager assetBundleForLocale:client:force:]_block_invoke
+ ___55-[SRDefaultsManager updateContentVersions:forLanguage:]_block_invoke
+ ___55-[SRDefaultsManager updateContentVersions:forLanguage:]_block_invoke_2
+ ___56-[SRAssetBundleQuery enumerateEntriesForLanguage:block:]_block_invoke
+ ___56-[SRAssetBundleQuery enumerateEntriesForLanguage:block:]_block_invoke_2
+ ___57-[SRDefaultsManager refreshCacheForLanguages:completion:]_block_invoke
+ ___57-[SRDefaultsManager refreshCacheForLanguages:completion:]_block_invoke_2
+ ___57-[SRDefaultsManager refreshCacheForLanguages:completion:]_block_invoke_3
+ ___57-[SRDefaultsManager refreshCacheForLanguages:completion:]_block_invoke_4
+ ___57-[SRDefaultsManager refreshCacheForLanguages:completion:]_block_invoke_5
+ ___58-[SRDefaultsManager loadTestAssetsForLanguage:assetTypes:]_block_invoke
+ ___60-[SRDefaultsManager loadSystemAssetsForLanguage:assetTypes:]_block_invoke
+ ___61-[SRDefaultsManager shouldReloadLanguage:forContentVersions:]_block_invoke
+ ___61-[SRDefaultsManager shouldReloadLanguage:forContentVersions:]_block_invoke_2
+ ___61-[SRDefaultsManager shouldReloadLanguage:forContentVersions:]_block_invoke_3
+ ___64-[SRResourcesManager loadAllParametersForClient:locale:options:]_block_invoke
+ ___65-[SRDefaultsManager notifyObserversWithLanguage:contentVersions:]_block_invoke
+ ___65-[SRDefaultsManager notifyObserversWithLanguage:contentVersions:]_block_invoke_2
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2
+ ___73-[SRAssetBundleQuery addQueryEntriesForLanguage:assetType:deliveryTypes:]_block_invoke
+ ___SRGetResourcePath_block_invoke
+ ___SRIsRunningInServer_block_invoke
+ ___SRLogCategoryAssets_block_invoke
+ ___SRLogCategoryTrial_block_invoke
+ ___block_descriptor_40_e8_32bs_e39_v32?0"NSString"8"NSDictionary"16^B24l
+ ___block_descriptor_40_e8_32bs_e40_v24?0"SRAssetBundleQuery"8"NSError"16l
+ ___block_descriptor_40_e8_32bs_e50_v32?0"NSString"8"SRAssetBundleCacheEntry"16^B24l
+ ___block_descriptor_40_e8_32r_e33_v16?0"SRAssetBundleCacheEntry"8l
+ ___block_descriptor_40_e8_32r_e39_v32?0"NSString"8"NSDictionary"16^B24l
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32s_e22_v24?0"NSString"8^B16l
+ ___block_descriptor_40_e8_32s_e39_v32?0"NSString"8"NSDictionary"16^B24l
+ ___block_descriptor_40_e8_32s_e50_v32?0"NSString"8"SRAssetBundleCacheEntry"16^B24l
+ ___block_descriptor_41_e8_32s_e36_B24?0Q8"NSObject<OS_xpc_object>"16l
+ ___block_descriptor_42_e8_32s_e24_v32?0"SRAsset"8Q16^B24l
+ ___block_descriptor_48_e8_32bs40r_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_48_e8_32bs_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_48_e8_32s40s_e39_v32?0"NSString"8"NSDictionary"16^B24l
+ ___block_descriptor_56_e8_32s40r48r_e33_v16?0"SRAssetBundleCacheEntry"8l
+ ___block_descriptor_56_e8_32s40r_e40_v24?0"SRAssetBundleQuery"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48r_e39_v32?0"NSString"8"NSDictionary"16^B24l
+ ___block_descriptor_56_e8_32s40s48s_e35_v32?0"NSString"8"NSNumber"16^B24l
+ ___block_descriptor_56_e8_32s40s48s_e50_v32?0"NSString"8"SRAssetBundleCacheEntry"16^B24l
+ ___block_descriptor_56_e8_32s40s_e40_v24?0"SRAssetBundleQuery"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48bs56w_e40_v24?0"SRAssetBundleQuery"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48r_e35_v32?0"NSString"8"NSNumber"16^B24l
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48s56r_e25_v32?0"DDSAsset"8Q16^B24l
+ ___block_descriptor_64_e8_32s40s48s_e25_v32?0"NSNumber"8Q16^B24l
+ ___block_descriptor_64_e8_32s40s48s_e39_v32?0"NSString"8"NSDictionary"16^B24l
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48r56r_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56r64r_e25_v32?0"DDSAsset"8Q16^B24l
+ ___block_descriptor_72_e8_32s40s48s56r64w_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56r_e35_v32?0"NSString"8"NSNumber"16^B24l
+ ___block_descriptor_72_e8_32s40s48s56w_e5_v8?0l
+ ___block_descriptor_80_e8_32s40r48r56r64r72r_e24_v32?0"SRAsset"8Q16^B24l
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0l
+ ___block_descriptor_82_e8_32s40s48r56r64w_e5_v8?0l
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80w_e5_v8?0l
+ ___block_descriptor_90_e8_32s40s48s56r64r72w_e5_v8?0l
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80r88w_e20_v20?0B8"NSError"12l
+ ___copy_helper_block_e8_32b
+ ___copy_helper_block_e8_32b40r
+ ___copy_helper_block_e8_32s40r48r
+ ___copy_helper_block_e8_32s40r48r56r64r72r
+ ___copy_helper_block_e8_32s40s48b56w
+ ___copy_helper_block_e8_32s40s48r56r
+ ___copy_helper_block_e8_32s40s48s56b64w
+ ___copy_helper_block_e8_32s40s48s56r64r
+ ___copy_helper_block_e8_32s40s48s56r64r72w
+ ___copy_helper_block_e8_32s40s48s56r64w
+ ___copy_helper_block_e8_32s40s48s56s64s72b80w
+ ___copy_helper_block_e8_32s40s48s56s64s72r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80r88w
+ ___copy_helper_block_e8_32s40s48s56w
+ ___destroy_helper_block_e8_32s40r48r
+ ___destroy_helper_block_e8_32s40r48r56r64r72r
+ ___destroy_helper_block_e8_32s40s48r56r
+ ___destroy_helper_block_e8_32s40s48s56r64r
+ ___destroy_helper_block_e8_32s40s48s56r64r72w
+ ___destroy_helper_block_e8_32s40s48s56r64w
+ ___destroy_helper_block_e8_32s40s48s56s64s72r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80r88w
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80w
+ ___destroy_helper_block_e8_32s40s48s56s64w
+ ___destroy_helper_block_e8_32s40s48s56w
+ ___refreshCacheWithQuery_block_invoke
+ __block_literal_global.101
+ __block_literal_global.12
+ __block_literal_global.2
+ __block_literal_global.35
+ __block_literal_global.414
+ __block_literal_global.438
+ __block_literal_global.483
+ __block_literal_global.486
+ __block_literal_global.504
+ __block_literal_global.9
+ __xpc_error_connection_interrupted
+ __xpc_error_connection_invalid
+ __xpc_runtime_is_app_sandboxed
+ __xpc_type_array
+ __xpc_type_dictionary
+ _assetBundleCacheQuery
+ _assetTypeID
+ _assetTypeString
+ _assetUUIDFromPath
+ _ddsAssetQuery
+ _deliveryTypeID
+ _deliveryTypeString
+ _dispatch_activate
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
+ _dispatch_queue_create_with_target$V2
+ _dispatch_workloop_create
+ _getContentVersionFromPath
+ _kCFLocaleCurrentLocaleDidChangeNotification
+ _localeChangeCallback
+ _objc_msgSend$_loadAssets:shouldUpdate:
+ _objc_msgSend$addFetchForLanguage:
+ _objc_msgSend$addQueryEntriesForLanguage:assetType:deliveryTypes:
+ _objc_msgSend$assertionID
+ _objc_msgSend$assetBundleForLocale:client:force:
+ _objc_msgSend$assetTypeString
+ _objc_msgSend$assetsForQuery:error:
+ _objc_msgSend$cacheFilePath
+ _objc_msgSend$cachedOTALanguages
+ _objc_msgSend$code
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$connection
+ _objc_msgSend$deliveryType
+ _objc_msgSend$deliveryTypeString
+ _objc_msgSend$didUpdateDefaultsWithLanguage:contentVersions:trial:
+ _objc_msgSend$dumpCache
+ _objc_msgSend$enumerateEntriesForLanguage:block:
+ _objc_msgSend$fetchedLanguages
+ _objc_msgSend$flushCacheToFile
+ _objc_msgSend$getLocalFileUrl
+ _objc_msgSend$handleMessage:error:
+ _objc_msgSend$hash
+ _objc_msgSend$initWithAssertionID:
+ _objc_msgSend$initWithAssetType:language:deliveryType:
+ _objc_msgSend$initWithAttributes:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithLocale:contentVersions:
+ _objc_msgSend$initWithMachServiceName:
+ _objc_msgSend$initWithXPCObject:isResult:
+ _objc_msgSend$intValue
+ _objc_msgSend$isResult
+ _objc_msgSend$isResultNone
+ _objc_msgSend$isSupportedLanguage:deliveryType:
+ _objc_msgSend$language
+ _objc_msgSend$loadCacheFromFile
+ _objc_msgSend$loadDefaultsForLocale:reload:force:
+ _objc_msgSend$loadOTAAssetsForLanguage:reload:assetTypes:force:
+ _objc_msgSend$loadSupportedLanguages:
+ _objc_msgSend$loadSystemAssetsForLanguage:assetTypes:
+ _objc_msgSend$loadTestAssetsForLanguage:assetTypes:
+ _objc_msgSend$localURL
+ _objc_msgSend$makeResultNone
+ _objc_msgSend$makeResultWithContentVersion:path:
+ _objc_msgSend$notifyObserversWithLanguage:contentVersions:
+ _objc_msgSend$notifyQueue
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$preferredLanguages
+ _objc_msgSend$queryCache:
+ _objc_msgSend$queryEntries
+ _objc_msgSend$queryServerCache:completion:
+ _objc_msgSend$refreshCacheForLanguages:completion:
+ _objc_msgSend$removeAssetBundleWithAssetType:language:deliveryType:
+ _objc_msgSend$requestedOTALanguages
+ _objc_msgSend$sendMessageAsync:completion:
+ _objc_msgSend$setLatestOnly:
+ _objc_msgSend$sharedConnection
+ _objc_msgSend$shouldReloadLanguage:forContentVersions:
+ _objc_msgSend$shouldUpdateForContentVersions:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$updateCacheWithResults:
+ _objc_msgSend$updateContentVersions:forLanguage:
+ _objc_msgSend$updateFetchedLanguages:
+ _objc_msgSend$upsertAssetBundleWithAssetType:language:deliveryType:contentVersion:path:
+ _objc_msgSend$xpcObject
+ _refreshCacheWithQuery
+ _sCacheLock
+ _sIndex
+ _sLanguagesLock
+ _sMessageID
+ _xpc_array_append_value
+ _xpc_array_apply
+ _xpc_array_create_empty
+ _xpc_connection_send_message
+ _xpc_connection_send_message_with_reply
+ _xpc_dictionary_create_empty
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_get_array
+ _xpc_dictionary_get_int64
+ _xpc_dictionary_get_remote_connection
+ _xpc_dictionary_get_string
+ _xpc_dictionary_get_uint64
+ _xpc_dictionary_get_value
+ _xpc_dictionary_set_int64
+ _xpc_dictionary_set_string
+ _xpc_dictionary_set_uint64
+ _xpc_dictionary_set_value
+ _xpc_get_type
+ assetTypeString.cold.1
+ cacheFilePath.sCachePath
+ configuration.onceToken
+ configuration.sLanguageConfig
+ deliveryTypeString.cold.1
+ getContentVersionFromPath.cold.1
+ getMobileAssetPropertiesFromPath.cold.1
+ getValidRegions.cold.1
+ loadAssetsFromResourcePath.cold.1
+ loadOTAAssetsForLanguage:reload:assetTypes:force:.onceToken
+ refreshCacheWithQuery.cold.1
+ refreshCacheWithQuery.cold.2
+ sAssetServer_block_invoke_2.onceToken1
+ sharedConnection.onceToken
+ sharedConnection.sConnection
+ sharedInstance.cache
+ sharedInstance.onceToken
+ trialFlagsForProcess.cold.1
- +[SRAsset deliveryTypeFromString:]
- +[SRAsset deliveryTypeString:]
- +[SRAsset deliveryTypeString:].cold.1
- -[SRAssetBundle initWithLocale:]
- -[SRAssetConfiguration isValidLocale:deliveryType:]
- -[SRAssetConfiguration setLocales:]
- -[SRAssetConfiguration supportedLocalesVersion]
- -[SRDefaultsManager _loadAssets:deliveryType:shouldUpdate:]
- -[SRDefaultsManager addFetchForLocale:]
- -[SRDefaultsManager assetBundleForLocale:client:]
- -[SRDefaultsManager fetchedLocales]
- -[SRDefaultsManager forceLoad]
- -[SRDefaultsManager loadDefaultsForLocale:reload:]
- -[SRDefaultsManager loadSupportedLocalesFromFile:]
- -[SRDefaultsManager notifyObservers]
- -[SRDefaultsManager removeFetchForLocale:]
- -[SRDefaultsManager requestAssetsForLanguages:resourcePath:]
- -[SRDefaultsManager setForceLoad:]
- -[SRDefaultsManager setOptions:]
- -[SRDefaultsManager updateFetchedLocales:]
- -[SRResources didUpdateDefaults]
- -[SRResourcesManager fetchAllParametersForLanguages:resourcePath:]
- GCC_except_table104
- GCC_except_table108
- GCC_except_table111
- GCC_except_table113
- GCC_except_table3
- GCC_except_table31
- GCC_except_table35
- GCC_except_table37
- GCC_except_table41
- GCC_except_table43
- GCC_except_table53
- GCC_except_table56
- GCC_except_table7
- GCC_except_table71
- GCC_except_table92
- GCC_except_table96
- OBJC_IVAR_$_SRAssetConfiguration._localeMap
- OBJC_IVAR_$_SRAssetConfiguration._localesVersion
- OBJC_IVAR_$_SRDefaultsManager._fetchedLocales
- OBJC_IVAR_$_SRDefaultsManager._forceLoad
- OBJC_IVAR_$_SRDefaultsManager._supportedLocalesPath
- __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434
- __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.1
- __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.10
- __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.11
- __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.12
- __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.2
- __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.3
- __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.4
- __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.5
- __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.6
- __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.7
- __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.8
- __43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.9
- __47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.159
- __47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.159.cold.1
- __49-[SRDefaultsManager assetBundleForLocale:client:]_block_invoke.cold.1
- __50-[SRDefaultsManager loadDefaultsForLocale:reload:]_block_invoke.164
- __50-[SRDefaultsManager loadDefaultsForLocale:reload:]_block_invoke.168
- __50-[SRDefaultsManager loadDefaultsForLocale:reload:]_block_invoke.173
- __50-[SRDefaultsManager loadDefaultsForLocale:reload:]_block_invoke.175
- __50-[SRDefaultsManager loadDefaultsForLocale:reload:]_block_invoke_2.174
- __50-[SRDefaultsManager loadDefaultsForLocale:reload:]_block_invoke_2.176
- __51-[SRDefaultsManager loadDefaultsFromDefaultAssets:]_block_invoke.123
- __60-[SRDefaultsManager requestAssetsForLanguages:resourcePath:]_block_invoke.148
- ___35-[SRDefaultsManager fetchedLocales]_block_invoke
- ___36-[SRDefaultsManager notifyObservers]_block_invoke
- ___39-[SRDefaultsManager addFetchForLocale:]_block_invoke
- ___42-[SRDefaultsManager removeFetchForLocale:]_block_invoke
- ___42-[SRDefaultsManager updateFetchedLocales:]_block_invoke
- ___49-[SRDefaultsManager assetBundleForLocale:client:]_block_invoke
- ___50-[SRDefaultsManager loadDefaultsForLocale:reload:]_block_invoke
- ___50-[SRDefaultsManager loadDefaultsForLocale:reload:]_block_invoke_2
- ___59-[SRDefaultsManager _loadAssets:deliveryType:shouldUpdate:]_block_invoke
- ___60-[SRDefaultsManager requestAssetsForLanguages:resourcePath:]_block_invoke
- ___60-[SRDefaultsManager requestAssetsForLanguages:resourcePath:]_block_invoke_2
- ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12l
- ___block_descriptor_49_e8_32s40s_e24_v32?0"SRAsset"8Q16^B24l
- ___block_descriptor_72_e8_32r40r48r56r64r_e24_v32?0"SRAsset"8Q16^B24l
- ___block_descriptor_72_e8_32s40s48r56r64w_e5_v8?0l
- ___block_descriptor_80_e8_32s40s48s56s64r72w_e5_v8?0l
- ___copy_helper_block_e8_32r40r48r56r64r
- ___copy_helper_block_e8_32s40s48s56s64r72w
- ___destroy_helper_block_e8_32r40r48r56r64r
- ___destroy_helper_block_e8_32s40s48s56s64r72w
- __block_literal_global.427
- __block_literal_global.472
- __block_literal_global.475
- __block_literal_global.493
- __dispatch_main_q
- _assetQueryForLocale
- _dispatch_group_async
- _objc_msgSend$_loadAssets:deliveryType:shouldUpdate:
- _objc_msgSend$addFetchForLocale:
- _objc_msgSend$allContentItemsMatchingQuery:error:
- _objc_msgSend$assetBundleForLocale:client:
- _objc_msgSend$assetConfig
- _objc_msgSend$assetWithLocaleIdentifier:contentType:deliveryType:path:
- _objc_msgSend$copyItemAtURL:toURL:error:
- _objc_msgSend$deliveryTypeFromString:
- _objc_msgSend$deliveryTypeString:
- _objc_msgSend$fetchedLocales
- _objc_msgSend$fileName
- _objc_msgSend$forceLoad
- _objc_msgSend$initWithLocale:
- _objc_msgSend$isValidLocale:deliveryType:
- _objc_msgSend$loadAllParametersForClient:locale:
- _objc_msgSend$loadDefaultsForLocale:reload:
- _objc_msgSend$loadSupportedLocalesFromFile:
- _objc_msgSend$notifyObservers
- _objc_msgSend$parentAsset
- _objc_msgSend$requestAssetsForLanguages:resourcePath:
- _objc_msgSend$setByAddingObject:
- _objc_msgSend$setLocales:
- _objc_msgSend$setOptions:
- _objc_msgSend$supportedLocalesVersion
- _objc_msgSend$unloadDefaultsForLocale:
- _objc_msgSend$updateFetchedLocales:
- _sLastLoadedContentVersion
- _sSafetyDDSLoadSignpostID
- loadDefaultsForLocale:reload:.onceToken
- requestAssetsForLanguages:resourcePath:.onceToken
CStrings:
+ "!!"
+ "%@\nSupported Languages:\n%@\nCache:\n%@\n"
+ "%@/assetBundleCache.plist"
+ "%@:%@:%@:%@"
+ "%s does not exist at %s"
+ "%s does not exist at path <%s>"
+ "(%ld, %s)"
+ "(%llu, %@) for asset (%@, %@, %@)"
+ "(AssetServerInit) configure asset type: %s (%lu)"
+ "(AssetServerInit) configuring asset type: %s (%lu)"
+ "(_loadAssets) loading asset: %s, %s, %s, %s"
+ "(_loadAssets) skipping over asset: %s, %s"
+ "(_unloadAssetsForLocale) unloading assets for locale: %s"
+ "(assertions) (version %ld) removing assertion: %s"
+ "(assertions) adding assertion : %s"
+ "(assertions) keeping assertion : %s"
+ "(assertions) removing assertion : %s"
+ "(fetchedLanguages) add fetch for language: %s"
+ "(fetchedLanguages) remove fetch for language: %s"
+ "(fetchedLanguages) update fetched languages: %@ --> %@"
+ "(forceLoad) Failed to get assets from server: %@"
+ "(forceLoad) Got asset bundles from server for %s"
+ "(forceLoad) Sending query to server for %s"
+ "/Library/Metadata/Assets"
+ "9999.99.99"
+ ":"
+ "@\"SRLanguageConfiguration\""
+ "@32@0:8@16B24B28"
+ "@36@0:8@16@24B32"
+ "@40@0:8@16B24@28B36"
+ "@40@0:8q16@24q32"
+ "Add query entry (%@, %@, %@)"
+ "Asset bundle (%@, %@, %@) at %@ is not a directory"
+ "Asset bundle (%@, %@, %@) does not exist at path %@"
+ "AssetAddedProperties"
+ "AssetId"
+ "AssetPurpose"
+ "AssetState"
+ "Assets"
+ "B24@?0Q8@\"NSObject<OS_xpc_object>\"16"
+ "B32@0:8Q16@24"
+ "ContentVersion"
+ "Defaults are null"
+ "Error fetching content version from %@"
+ "Error handling message: %@"
+ "Error loading asset properties: %@"
+ "Error loading cache %@"
+ "Error refreshing cache for languages %@: %@"
+ "Error writing to cache: %@"
+ "Failed to get assets from server: %@"
+ "Failed to set up client connection"
+ "Got asset bundles from server for %s"
+ "Got updated assets from DDS for %s"
+ "Handle message %p"
+ "Has SRA roots installed, setting content version to 9999 for %@"
+ "Invalid asset type %@ for (%@, %@)"
+ "Invalid assetType %@ for %@"
+ "Invalid assetType %@ in cache"
+ "Invalid assetType %@ in cache file"
+ "Invalid delivery type %@ for (%@, %@)"
+ "Invalid deliveryType %@ in cache"
+ "Invalid deliveryType %@ in cache file"
+ "Invalid query entry type %d"
+ "Invalid query type %d"
+ "LinguisticAssetType"
+ "Loading %s at path <%s>"
+ "Loading RequiredAssets_root at path <%s>"
+ "Locale changed!"
+ "Malformed assertionID %@"
+ "No assets for (%@, %@, %@)"
+ "Null content version for asset (%@, %@, %@)"
+ "Null path for asset bundle (%@, %@, %@)"
+ "Parser"
+ "Path"
+ "Q"
+ "Refreshed cache for %@"
+ "Refreshing cache!"
+ "Reply for message[%llu] = %p"
+ "SRAssertion"
+ "SRAssetBundleCache"
+ "SRAssetBundleCacheEntry"
+ "SRAssetBundleQuery"
+ "SRLanguageConfiguration"
+ "SRResources dealloc (%@, %@): %p"
+ "SRResources init (%@, %@): %p"
+ "SRXPCConnection"
+ "SRXPCListener"
+ "Sandboxed client"
+ "Sending message[%llu] = %p"
+ "Sending query to server for %s"
+ "Should not refresh cache in Spotlight daemon"
+ "T@\"NSMutableDictionary\",R,N,V_queryEntries"
+ "T@\"NSMutableSet\",R,N,V_cachedOTALanguages"
+ "T@\"NSMutableSet\",R,N,V_requestedOTALanguages"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_notifyQueue"
+ "T@\"NSString\",R,N,V_assetType"
+ "T@\"NSString\",R,N,V_deliveryType"
+ "T@\"NSString\",R,N,V_language"
+ "T@\"NSString\",R,N,V_path"
+ "TB,R,N,V_isResult"
+ "TQ,R,N,V_contentVersion"
+ "Tq,R,N,V_assetType"
+ "Unknown asset type %ld"
+ "_assertionID"
+ "_cache"
+ "_cachedOTALanguages"
+ "_contentVersion"
+ "_contentVersions"
+ "_fetchedLanguages"
+ "_isResult"
+ "_isSR"
+ "_langConfig"
+ "_language"
+ "_loadAssets:shouldUpdate:"
+ "_loadedContentVersions"
+ "_notifyQueue"
+ "_path"
+ "_queryEntries"
+ "_queue"
+ "_requestedOTALanguages"
+ "_supportedLanguageMap"
+ "a"
+ "addFetchForLanguage:"
+ "addQueryEntriesForLanguage:assetType:deliveryTypes:"
+ "assertionID"
+ "assetBundleForLocale:client:force:"
+ "assetTypeString"
+ "assets"
+ "assetsForQuery:error:"
+ "cacheFilePath"
+ "cachedOTALanguages"
+ "code"
+ "com.apple.MobileAsset.LinguisticData"
+ "com.apple.spotlight.IndexAgent"
+ "com.apple.spotlight.resources.assetsQuery.queue"
+ "com.apple.spotlight.resources.assetsQuery.workloop"
+ "com.apple.spotlightresources.notifyDelegates"
+ "command"
+ "componentsSeparatedByString:"
+ "connection"
+ "d"
+ "default_factors_%@.pb"
+ "deliveryTypeString"
+ "didUpdateDefaultsWithLanguage:contentVersions:trial:"
+ "dumpCache"
+ "e"
+ "enumerateEntriesForLanguage:block:"
+ "fetchAllParametersForLanguages:"
+ "fetchedLanguages"
+ "flushCacheToFile"
+ "getLocalFileUrl"
+ "handleAssetsCommand:"
+ "handleMessage:error:"
+ "initWithAssertionID:"
+ "initWithAssetType:language:deliveryType:"
+ "initWithAttributes:"
+ "initWithDomain:code:userInfo:"
+ "initWithLocale:contentVersions:"
+ "initWithMachServiceName:"
+ "initWithXPCObject:isResult:"
+ "intValue"
+ "isResult"
+ "isResultNone"
+ "isSupportedLanguage:deliveryType:"
+ "l"
+ "language"
+ "loadCacheFromFile"
+ "loadDefaultsForLocale:reload:force:"
+ "loadOTAAssetsForLanguage:reload:assetTypes:force:"
+ "loadOTA[%llu] (%@, %d, %d, %@)"
+ "loadOTA[%llu] client 1"
+ "loadOTA[%llu] client 2"
+ "loadOTA[%llu] client 2.1"
+ "loadOTA[%llu] client 2.2"
+ "loadOTA[%llu] client 2.3"
+ "loadOTA[%llu] client 3"
+ "loadOTA[%llu] client 3.1"
+ "loadOTA[%llu] client 3.2"
+ "loadOTA[%llu] client 3.3"
+ "loadOTA[%llu] load"
+ "loadOTA[%llu] server 1"
+ "loadOTA[%llu] server 2"
+ "loadOTA[%llu] server 2.1"
+ "loadOTA[%llu] server 3"
+ "loadOTA[%llu] server 3.1"
+ "loadOTA[%llu] server 3.2"
+ "loadSupportedLanguages:"
+ "loadSystemAssetsForLanguage:assetTypes:"
+ "loadTestAssetsForLanguage:assetTypes:"
+ "localURL"
+ "makeResultNone"
+ "makeResultWithContentVersion:path:"
+ "notifyObserversWithLanguage:contentVersions:"
+ "notifyQueue"
+ "numberWithUnsignedInteger:"
+ "numberWithUnsignedLongLong:"
+ "objectAtIndexedSubscript:"
+ "p"
+ "preferredLanguages"
+ "qi"
+ "queryCache:"
+ "queryEntries"
+ "queryServerCache:completion:"
+ "refreshCacheForLanguages:completion:"
+ "removeAssetBundleWithAssetType:language:deliveryType:"
+ "requestAssets update for %@"
+ "requestedOTALanguages"
+ "resourcePath"
+ "ri"
+ "sendMessageAsync:completion:"
+ "setLatestOnly:"
+ "sharedConnection"
+ "shouldReloadLanguage:forContentVersions:"
+ "shouldUpdateForContentVersions:"
+ "stringByAppendingString:"
+ "stringByDeletingLastPathComponent"
+ "stringByDeletingPathExtension"
+ "stringWithUTF8String:"
+ "unsignedIntegerValue"
+ "updateCacheWithResults:"
+ "updateContentVersions:forLanguage:"
+ "updateFetchedLanguages:"
+ "upsertAssetBundleWithAssetType:language:deliveryType:contentVersion:path:"
+ "v"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
+ "v16@?0@\"SRAssetBundleCacheEntry\"8"
+ "v24@?0@\"NSString\"8^B16"
+ "v24@?0@\"SRAssetBundleQuery\"8@\"NSError\"16"
+ "v32@0:8@16@?24"
+ "v32@0:8@16^@24"
+ "v32@?0@\"DDSAsset\"8Q16^B24"
+ "v32@?0@\"NSNumber\"8Q16^B24"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"
+ "v32@?0@\"NSString\"8@\"SRAssetBundleCacheEntry\"16^B24"
+ "v36@0:8@\"NSString\"16@\"NSDictionary\"24B32"
+ "v56@0:8@16@24@32Q40@48"
+ "xpcObject"
- "%@/locales.plist"
- "(forceLoad on) Error fetching assets for query (%s, %s, %s): %@"
- "(forceLoad on) Invalid dds asset (%@, %@, %@, %@)"
- "(forceLoad on) Not fetching asset with type %s for deliveryType %s"
- "(forceLoad=off) type %@, deliveryType %@"
- "(forceLoad=on) type %@, deliveryType %@"
- "."
- "Copy supported locales from %@ to %@"
- "Error fetching assets for query (%s, %s, %s): %@"
- "Invalid dds asset (%@, %@, %@, %@)"
- "Not fetching asset with type %s for deliveryType %s"
- "SRResources dealloc (%@, %@)"
- "SRResources init (%@, %@)"
- "SRSafetyDDSForceLoad"
- "SRSafetyDDSLoad"
- "SpotlightResources:%@:%@"
- "SpotlightResources:%@:%@:%@"
- "Supported locales copy from %@ to %@ failed with %@"
- "TB,N,V_forceLoad"
- "[SR_INFO][DefaultsManager] (AssetServerInit) configure asset type: %s (%lu)"
- "[SR_INFO][DefaultsManager] (_loadAssets) loading asset: %s, %s, %s, %s"
- "[SR_INFO][DefaultsManager] (_unloadAssetsForLocale) unloading assets for locale: %s"
- "[SR_INFO][DefaultsManager] (addAssertionWithIdentifier) adding assertion: %s"
- "[SR_INFO][DefaultsManager] (addAssertionWithIdentifier) keeping assertion: %s"
- "[SR_INFO][DefaultsManager] (addFetchForLocale) asset fetch for locale: %s"
- "[SR_INFO][DefaultsManager] (fetchedLocales) update fetched locales: %@ --> %@"
- "[SR_INFO][DefaultsManager] (removeAssertionWithIdentifier) (%ld) removing assertion: %s"
- "[SR_INFO][DefaultsManager] (removeAssertionWithIdentifier) removing assertion: %s"
- "[SR_INFO][DefaultsManager] (removeFetchForLanguage) remove asset fetch for language: %s"
- "[SR_INFO][DefaultsManager] (removeFetchForLocale) remove asset fetch for locale: %s"
- "[SR_INFO][DefaultsManager] did update assets with type %s"
- "[SR_INFO][DefaultsManager] loading assets at path <%s>"
- "[SR_INFO][DefaultsManager] loading defaults at path <%s>"
- "_fetchedLocales"
- "_loadAssets:deliveryType:shouldUpdate:"
- "_localeMap"
- "_localesVersion"
- "_supportedLocalesPath"
- "addFetchForLocale:"
- "allContentItemsMatchingQuery:error:"
- "assetBundleForLocale:client:"
- "copyItemAtURL:toURL:error:"
- "deliveryTypeFromString:"
- "deliveryTypeString:"
- "fetchAllParametersForLanguages:resourcePath:"
- "fetchedLocales"
- "fileName"
- "initWithLocale:"
- "isValidLocale:deliveryType:"
- "loadDefaultsForLocale:reload:"
- "loadSupportedLocalesFromFile:"
- "loc:%s, v:%lu"
- "localeMap: %@\n"
- "notifyObservers"
- "parentAsset"
- "removeFetchForLocale:"
- "requestAssetsForLanguages:resourcePath:"
- "setByAddingObject:"
- "setForceLoad:"
- "setLocales:"
- "setOptions:"
- "supportedLocalesVersion"
- "updateFetchedLocales:"

```
