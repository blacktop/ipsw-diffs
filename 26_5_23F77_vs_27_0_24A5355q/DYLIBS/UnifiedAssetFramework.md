## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3525.2.1.0.0
-  __TEXT.__text: 0x83adc
-  __TEXT.__auth_stubs: 0x1140
-  __TEXT.__objc_methlist: 0x3970
-  __TEXT.__const: 0x1c8
-  __TEXT.__dlopen_cstrs: 0x296
+3600.61.1.0.0
+  __TEXT.__text: 0x77f64
+  __TEXT.__objc_methlist: 0x3628
+  __TEXT.__const: 0x190
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x67
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_fieldmd: 0x1c
-  __TEXT.__cstring: 0xbaa6
-  __TEXT.__oslogstring: 0xf0e9
+  __TEXT.__cstring: 0xb754
+  __TEXT.__oslogstring: 0xef4d
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x16c4
-  __TEXT.__unwind_info: 0x1590
-  __TEXT.__objc_classname: 0x50e
-  __TEXT.__objc_methname: 0xabbc
-  __TEXT.__objc_methtype: 0x116a
-  __TEXT.__objc_stubs: 0x88c0
-  __DATA_CONST.__got: 0x588
-  __DATA_CONST.__const: 0x1ea0
+  __TEXT.__gcc_except_tab: 0xf3c
+  __TEXT.__unwind_info: 0x11e8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1cd8
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x28b0
+  __DATA_CONST.__objc_selrefs: 0x2680
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x130
-  __AUTH_CONST.__auth_got: 0x8b0
-  __AUTH_CONST.__const: 0x6c8
-  __AUTH_CONST.__cfstring: 0x4d20
-  __AUTH_CONST.__objc_const: 0x4958
-  __AUTH_CONST.__objc_intobj: 0x270
+  __DATA_CONST.__got: 0x5c0
+  __AUTH_CONST.__const: 0x588
+  __AUTH_CONST.__cfstring: 0x5080
+  __AUTH_CONST.__objc_const: 0x4570
   __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x408
+  __AUTH_CONST.__auth_got: 0x858
+  __AUTH.__objc_data: 0x570
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x374
-  __DATA.__data: 0x290
-  __DATA.__bss: 0x48
-  __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0xca8
-  __DATA_DIRTY.__bss: 0x310
+  __DATA.__objc_ivar: 0x310
+  __DATA.__data: 0x2c0
+  __DATA.__bss: 0x38
+  __DATA.__common: 0x10
+  __DATA_DIRTY.__objc_data: 0xb40
+  __DATA_DIRTY.__bss: 0x230
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 9C220115-BB38-33C8-8A59-38E65A2841A8
-  Functions: 1597
-  Symbols:   5815
-  CStrings:  4734
+  UUID: 2F5631DC-FB12-3005-8D06-C0CFF9D684E3
+  Functions: 1448
+  Symbols:   5323
+  CStrings:  2753
 
Symbols:
+ +[UAFAssetInfoCache appendMetadataExtensionToPath:]
+ +[UAFAssetInfoCache assetSetPath:]
+ +[UAFAssetInfoCache atomicInstanceMetadataForAssetSet:atomicInstance:error:]
+ +[UAFAssetInfoCache atomicInstancePath:atomicInstance:]
+ +[UAFAssetInfoCache cachedAssetsForAssetSet:atomicInstance:autoAssets:experimentActivated:experiment:error:]
+ +[UAFAssetInfoCache getAtomicInstanceMetadataPath:atomicInstance:]
+ +[UAFAssetInfoCache getCachedAsset:specifier:atomicInstanceCachePath:experimentationEnabled:experimentId:error:]
+ +[UAFAssetInfoCache maintainCacheForAssetSet:latestAtomicInstance:]
+ +[UAFAssetInfoCache notReadyPath:atomicInstance:]
+ +[UAFAssetInfoCache setBasePath:]
+ +[UAFAssetInfoCache specifierDirectoryExistsOnDisk:atomicInstance:specifier:]
+ +[UAFAssetInfoCache specifierPath:atomicInstance:specifier:]
+ +[UAFAssetInfoCache updateCacheIfNeeded:atomicEntries:atomicInstance:]
+ +[UAFAssetInfoCache writeCacheForAssetSet:atomicInstance:atomicEntries:atomicInstanceMetadata:error:]
+ +[UAFAssetSetConfiguration getSpecifierToAssetNameMap:]
+ +[UAFAssetSetManager _subscriptionDiffersFromDB:subscriber:user:expirationOnlyCount:storeSubscriptions:error:]
+ +[UAFAssetSetManager isSubscriptionExpirationIgnorable:subscriber:user:storeSubscriptions:]
+ +[UAFAssetSetSubscriptionManager getSubscriptionsAsDictionary:storeManager:]
+ +[UAFAssetSetSubscriptionManager subscriptions:subscriber:user:completion:]
+ +[UAFAtomicInstanceMetadata supportsSecureCoding]
+ +[UAFAutoAssetManager checkPolicyForConfig:expensiveNetworking:]
+ +[UAFAutoAssetManager filterMetadata:specifiers:onDiskKeys:includeSpecifierKeys:]
+ +[UAFAutoAssetManager findDiffBetweenOldAssetSetUsages:newAssetSetUsages:configurationManager:]
+ +[UAFAutoAssetManager manageExperiment:config:consistencyToken:]
+ +[UAFAutoAssetManager manageExperimentFor:consistencyToken:]
+ +[UAFAutoAssetManager manageMetadataCacheForConfig:autoAssetSet:]
+ +[UAFAutoAssetManager metadataForAssetSetUsages:configurationManager:expensiveNetworking:localOnly:includeSpecifierKeys:queue:completion:]
+ +[UAFAutoAssetManager requestSandboxExtension:queue:completion:]
+ +[UAFAutoAssetManager stageAssetSet:targets:]
+ +[UAFAutoAssetManager stageAssetsWithConfigurationManager:version:token:]
+ +[UAFAutoAssetManager targetForAssetSet:specifiers:version:]
+ +[UAFBiomeInstrumenter _getBiomeAssetSetStatus:atomicInstanceMetadata:assetSetOriginReport:entries:errorCodes:]
+ +[UAFBiomeInstrumenter _getBiomeStreamForAssetSetStatus:atomicInstanceMetadata:assetSetOriginReport:entries:errorCodes:assetSetDailyStatusEventType:]
+ +[UAFBiomeInstrumenter _getBiomeUAFAssetSet:atomicInstanceMetadata:assetSetOriginReport:entries:errorCodes:]
+ +[UAFBiomeStreamWriter _constructBiomeAssetSet:storeManager:]
+ +[UAFBiomeStreamWriter _getAllAssetSets]
+ +[UAFBiomeStreamWriter _getAssetOriginType:]
+ +[UAFBiomeStreamWriter _getAssetSource:]
+ +[UAFBiomeStreamWriter _getBiomeUAFAssetSet:atomicInstanceMetadata:assetSetOriginReport:entries:errorCodes:]
+ +[UAFBiomeStreamWriter _getConfiguredAssetCountFor:]
+ +[UAFBiomeStreamWriter _getConfiguredAssetCountFor:autoAssetType:]
+ +[UAFBiomeStreamWriter isV2Available]
+ +[UAFBiomeStreamWriter logAlterFromAtomicInstance:sourceType:configuredSpecifiers:addedAssets:removedAssets:]
+ +[UAFBiomeStreamWriter logAssetSetArrivedEvent:atomicInstanceMetadata:assetSetOriginReport:entries:]
+ +[UAFBiomeStreamWriter logAssetSetDownloadErrorEvent:atomicInstanceMetadata:errorCodes:]
+ +[UAFBiomeStreamWriter logScheduledDailyAssetStatus]
+ +[UAFCommonUtilities _deepestUnderlyingError:]
+ +[UAFCommonUtilities activateExperimentId:trialNamespace:]
+ +[UAFCommonUtilities emptyLegacyStagingLogsDirectoryUnderStoragePath:]
+ +[UAFCommonUtilities experimentIdentifiersTrialClient:trialNamespace:staged:]
+ +[UAFCommonUtilities getMADownloadErrors:newerVersionError:assetSetName:assetSetID:]
+ +[UAFCommonUtilities isAssetInfoCacheSupported]
+ +[UAFCommonUtilities pathByResolvingSymlinksButKeepingPrivatePrefix:]
+ +[UAFCommonUtilities sandboxCheckFileRead:]
+ +[UAFCommonUtilities sandboxExtensionConsume:error:]
+ +[UAFCommonUtilities sandboxExtensionIssueFileToProcess:path:flags:auditToken:error:]
+ +[UAFCommonUtilities secTaskCopySigningIdentifier:error:]
+ +[UAFCommonUtilities secTaskCreateWithAllocator:auditToken:]
+ +[UAFCommonUtilities trialClient]
+ +[UAFCommonUtilities urlByResolvingSymlinksButKeepingPrivatePrefix:]
+ +[UAFInstrumentationProvider logAlterFromAtomicInstance:assetType:configuredSpecifiers:sourceType:alterSetData:]
+ +[UAFRootsV2AssetSet assetSetDirectoryForAssetSet:]
+ +[UAFRootsV2AssetSet currentRootsV2InstanceIdForAssetSet:]
+ +[UAFRootsV2AssetSet directoryEnumeratorAtPath:]
+ +[UAFRootsV2AssetSet disableMAAtomicInstanceForRootsV2:assetSetName:completion:]
+ +[UAFRootsV2AssetSet disabledByRootsV2MarkerPathForAtomicInstance:assetSetName:]
+ +[UAFRootsV2AssetSet getConcurrentQueue]
+ +[UAFRootsV2AssetSet hasInstalledRoots]
+ +[UAFRootsV2AssetSet invalidateRootsV2Instance:assetSetName:completion:]
+ +[UAFRootsV2AssetSet isMAAtomicInstanceDisabledByRootsV2:assetSetName:]
+ +[UAFRootsV2AssetSet lockFilePathForInstanceId:assetSetName:]
+ +[UAFRootsV2AssetSet lockRootsV2InstanceId:assetSetName:error:]
+ +[UAFRootsV2AssetSet maLockerPathForAtomicInstance:assetSetName:]
+ +[UAFRootsV2AssetSet removeDisabledByRootsV2MarkerForAtomicInstance:assetSetName:]
+ +[UAFRootsV2AssetSet removeDisabledByRootsV2MarkersForAssetSet:]
+ +[UAFRootsV2AssetSet requestDisableMAAtomicInstanceForRootsV2:assetSetName:queue:completion:]
+ +[UAFRootsV2AssetSet requestInvalidateRootsV2Instance:assetSetName:queue:completion:]
+ +[UAFRootsV2AssetSet rootsV2Directory]
+ +[UAFRootsV2AssetSet sendNotificationsForInstalledRoots]
+ -[UAFAssetSet assetSetIdForSELF:atomicInstanceMetadata:]
+ -[UAFAssetSet initializeRootsV2WithInstanceId:assetSet:consistencyToken:]
+ -[UAFAssetSet resolveConsistencyToken:]
+ -[UAFAssetSet rootsV2AssetSetError]
+ -[UAFAssetSet rootsV2AssetSet]
+ -[UAFAssetSet setRootsV2AssetSet:]
+ -[UAFAssetSet setRootsV2AssetSetError:]
+ -[UAFAssetSet setupExperiment:disableExperimentation:]
+ -[UAFAssetSetConsistencyToken initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:rootsV2InstanceId:]
+ -[UAFAssetSetConsistencyToken initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:rootsV2InstanceId:bootUUID:experimentActivated:]
+ -[UAFAssetSetConsistencyToken init]
+ -[UAFAssetSetConsistencyToken rootsV2InstanceId]
+ -[UAFAssetSetConsistencyToken rootsV2fd]
+ -[UAFAssetSetConsistencyToken setRootsV2InstanceId:]
+ -[UAFAssetSetConsistencyToken setRootsV2fd:]
+ -[UAFAssetSetExperiment isActivatedForAvailableSpecifiers:]
+ -[UAFAssetSetExperiment remapExperimentalAssets:specifierToAssetName:availableSpecifiers:experimentActivated:uafAssetForSpecifier:]
+ -[UAFAssetSetExperiment setStaged:]
+ -[UAFAssetSetExperiment setTrialNamespace:]
+ -[UAFAssetSetExperiment staged]
+ -[UAFAssetSetExperiment trialNamespace]
+ -[UAFAssetSetExperiment wantsRemapping]
+ -[UAFAssetSetManager _processSubscriptionDatabaseExtensionToken:xpcError:error:]
+ -[UAFAssetSetManager _sizeForSubscriptions:policies:sumByKey:queue:completion:]
+ -[UAFAssetSetManager _subscriptionDatabaseAccessIsGranted]
+ -[UAFAssetSetManager activateExperimentWithConsistencyToken:]
+ -[UAFAssetSetManager diskSpaceNeededForSubscriptions:policies:queue:completion:]
+ -[UAFAssetSetManager downloadSizeForSubscriptions:policies:queue:completion:]
+ -[UAFAssetSetManager ensureSubscriptionDatabaseAccessSync]
+ -[UAFAssetSetManager ensureSubscriptionDatabaseAccessWithQueue:completion:]
+ -[UAFAssetSetManager metadataForSubscriptions:policies:includeSpecifierKeys:queue:completion:]
+ -[UAFAssetSetManager requestSandboxExtension:queue:completion:]
+ -[UAFAssetSetManager sumMetadataEntries:forKey:]
+ -[UAFAtomicInstanceMetadata encodeWithCoder:]
+ -[UAFAtomicInstanceMetadata initWithCoder:]
+ -[UAFAtomicInstanceMetadata vendingAtomicInstanceForConfiguredEntries]
+ -[UAFAutoAssetSet atomicInstanceMetadata]
+ -[UAFAutoAssetSet initFromAssetInfoCache:autoAssets:experiment:atomicInstance:]
+ -[UAFAutoAssetSet isUsingAssetInfoCache]
+ -[UAFAutoAssetSet rapidLock]
+ -[UAFAutoAssetSet readAtomicInstanceInfoFromAssetInfoCache:autoAssets:experiment:atomicInstance:]
+ -[UAFAutoAssetSet setAtomicInstanceMetadata:]
+ -[UAFAutoAssetSet setIsUsingAssetInfoCache:]
+ -[UAFAutoAssetSet setRapidLock:]
+ -[UAFExperimentalAssetsConfiguration adopterExperimentActivation]
+ -[UAFExperimentalAssetsConfiguration setAdopterExperimentActivation:]
+ -[UAFMetadataWorkItem .cxx_destruct]
+ -[UAFMetadataWorkItem assetSetName]
+ -[UAFMetadataWorkItem assetSet]
+ -[UAFMetadataWorkItem onDiskKeys]
+ -[UAFMetadataWorkItem policy]
+ -[UAFMetadataWorkItem setAssetSet:]
+ -[UAFMetadataWorkItem setAssetSetName:]
+ -[UAFMetadataWorkItem setOnDiskKeys:]
+ -[UAFMetadataWorkItem setPolicy:]
+ -[UAFMetadataWorkItem setSpecifiers:]
+ -[UAFMetadataWorkItem specifiers]
+ -[UAFRootsV2AssetSet .cxx_destruct]
+ -[UAFRootsV2AssetSet assetSetName]
+ -[UAFRootsV2AssetSet assets]
+ -[UAFRootsV2AssetSet dealloc]
+ -[UAFRootsV2AssetSet experimentActivated]
+ -[UAFRootsV2AssetSet getAssetWithName:andSpecifier:experimentationEnabled:experimentId:]
+ -[UAFRootsV2AssetSet initWithAssetSetName:assets:uuid:rootsV2InstanceId:experiment:error:]
+ -[UAFRootsV2AssetSet instanceDirectoryForSpecifier:]
+ -[UAFRootsV2AssetSet loadAssets:experiment:]
+ -[UAFRootsV2AssetSet lockAssets:error:]
+ -[UAFRootsV2AssetSet lockFd]
+ -[UAFRootsV2AssetSet rootsV2InstanceId]
+ -[UAFRootsV2AssetSet setAssetSetName:]
+ -[UAFRootsV2AssetSet setAssets:]
+ -[UAFRootsV2AssetSet setExperimentActivated:]
+ -[UAFRootsV2AssetSet setLockFd:]
+ -[UAFRootsV2AssetSet setRootsV2InstanceId:]
+ -[UAFRootsV2AssetSet setUuid:]
+ -[UAFRootsV2AssetSet specifierDirectoryExistsOnDisk:]
+ -[UAFRootsV2AssetSet uuid]
+ -[UAFSubscriptionStoreManager _getSubscriptionsAsDictionary:subscriptionsFor:]
+ -[UAFSubscriptionStoreManager _getSubscriptionsAsDictionary:user:]
+ -[UAFSubscriptionStoreManager _prepareGetSubscriptionsStatement:user:]
+ -[UAFSubscriptionStoreManager getSubscriptionsAsDictionary:user:error:]
+ -[UAFXPCConnection disableMAAtomicInstanceForRootsV2:assetSetName:completion:]
+ -[UAFXPCConnection invalidateRootsV2Instance:assetSetName:completion:]
+ -[UAFXPCConnection requestSubscriptionDatabaseAccess:]
+ -[UAFXPCConnection requestSubscriptionDatabaseAccessSync:]
+ -[UAFXPCService disableMAAtomicInstanceForRootsV2:assetSetName:completion:]
+ -[UAFXPCService invalidateRootsV2Instance:assetSetName:completion:]
+ -[UAFXPCService isConnectionAppleSigned:error:]
+ -[UAFXPCService requestSubscriptionDatabaseAccess:]
+ GCC_except_table100
+ GCC_except_table106
+ GCC_except_table109
+ GCC_except_table112
+ GCC_except_table121
+ GCC_except_table125
+ GCC_except_table148
+ GCC_except_table18
+ GCC_except_table25
+ GCC_except_table26
+ GCC_except_table46
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table55
+ GCC_except_table57
+ GCC_except_table69
+ GCC_except_table76
+ GCC_except_table77
+ GCC_except_table86
+ GCC_except_table91
+ GCC_except_table97
+ GCC_except_table98
+ _APP_SANDBOX_READ
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _OBJC_CLASS_$_BMAssetDeliveryAssetSetAlterActivity
+ _OBJC_CLASS_$_BMAssetDeliveryAssetSetStatus
+ _OBJC_CLASS_$_BMAssetDeliveryDailyScheduledAssetStatus
+ _OBJC_CLASS_$_BMUAFAssetSetV2
+ _OBJC_CLASS_$_BMUAFAssetV2
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_UAFAssetInfoCache
+ _OBJC_CLASS_$_UAFBiomeStreamWriter
+ _OBJC_CLASS_$_UAFMetadataWorkItem
+ _OBJC_CLASS_$_UAFRootsV2AssetSet
+ _OBJC_IVAR_$_UAFAssetSet._rootsV2AssetSet
+ _OBJC_IVAR_$_UAFAssetSet._rootsV2AssetSetError
+ _OBJC_IVAR_$_UAFAssetSetConsistencyToken._rootsV2InstanceId
+ _OBJC_IVAR_$_UAFAssetSetConsistencyToken._rootsV2fd
+ _OBJC_IVAR_$_UAFAssetSetExperiment._staged
+ _OBJC_IVAR_$_UAFAssetSetExperiment._trialNamespace
+ _OBJC_IVAR_$_UAFAssetSetManager._databaseAccessGranted
+ _OBJC_IVAR_$_UAFAssetSetManager._sandboxExtensionRequestFailed
+ _OBJC_IVAR_$_UAFAtomicInstanceMetadata._vendingAtomicInstanceForConfiguredEntries
+ _OBJC_IVAR_$_UAFAutoAssetSet._atomicInstanceMetadata
+ _OBJC_IVAR_$_UAFAutoAssetSet._isUsingAssetInfoCache
+ _OBJC_IVAR_$_UAFAutoAssetSet._rapidLock
+ _OBJC_IVAR_$_UAFExperimentalAssetsConfiguration._adopterExperimentActivation
+ _OBJC_IVAR_$_UAFMetadataWorkItem._assetSet
+ _OBJC_IVAR_$_UAFMetadataWorkItem._assetSetName
+ _OBJC_IVAR_$_UAFMetadataWorkItem._onDiskKeys
+ _OBJC_IVAR_$_UAFMetadataWorkItem._policy
+ _OBJC_IVAR_$_UAFMetadataWorkItem._specifiers
+ _OBJC_IVAR_$_UAFRootsV2AssetSet._assetSetName
+ _OBJC_IVAR_$_UAFRootsV2AssetSet._assets
+ _OBJC_IVAR_$_UAFRootsV2AssetSet._experimentActivated
+ _OBJC_IVAR_$_UAFRootsV2AssetSet._lockFd
+ _OBJC_IVAR_$_UAFRootsV2AssetSet._rootsV2InstanceId
+ _OBJC_IVAR_$_UAFRootsV2AssetSet._uuid
+ _OBJC_METACLASS_$_UAFAssetInfoCache
+ _OBJC_METACLASS_$_UAFBiomeStreamWriter
+ _OBJC_METACLASS_$_UAFMetadataWorkItem
+ _OBJC_METACLASS_$_UAFRootsV2AssetSet
+ _SecTaskCopySigningIdentifier
+ _SecTaskCreateWithAuditToken
+ _UAFLogContextStaging
+ __OBJC_$_CLASS_METHODS_UAFAssetInfoCache
+ __OBJC_$_CLASS_METHODS_UAFAtomicInstanceMetadata
+ __OBJC_$_CLASS_METHODS_UAFBiomeStreamWriter
+ __OBJC_$_CLASS_METHODS_UAFRootsV2AssetSet
+ __OBJC_$_CLASS_PROP_LIST_UAFAtomicInstanceMetadata
+ __OBJC_$_INSTANCE_METHODS_UAFMetadataWorkItem
+ __OBJC_$_INSTANCE_METHODS_UAFRootsV2AssetSet
+ __OBJC_$_INSTANCE_VARIABLES_UAFMetadataWorkItem
+ __OBJC_$_INSTANCE_VARIABLES_UAFRootsV2AssetSet
+ __OBJC_$_PROP_LIST_UAFMetadataWorkItem
+ __OBJC_$_PROP_LIST_UAFRootsV2AssetSet
+ __OBJC_CLASS_PROTOCOLS_$_UAFAtomicInstanceMetadata
+ __OBJC_CLASS_RO_$_UAFAssetInfoCache
+ __OBJC_CLASS_RO_$_UAFBiomeStreamWriter
+ __OBJC_CLASS_RO_$_UAFMetadataWorkItem
+ __OBJC_CLASS_RO_$_UAFRootsV2AssetSet
+ __OBJC_METACLASS_RO_$_UAFAssetInfoCache
+ __OBJC_METACLASS_RO_$_UAFBiomeStreamWriter
+ __OBJC_METACLASS_RO_$_UAFMetadataWorkItem
+ __OBJC_METACLASS_RO_$_UAFRootsV2AssetSet
+ ___101+[UAFAssetInfoCache writeCacheForAssetSet:atomicInstance:atomicEntries:atomicInstanceMetadata:error:]_block_invoke
+ ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.413
+ ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.377
+ ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.378
+ ___108+[UAFAssetInfoCache cachedAssetsForAssetSet:atomicInstance:autoAssets:experimentActivated:experiment:error:]_block_invoke
+ ___108+[UAFAssetInfoCache cachedAssetsForAssetSet:atomicInstance:autoAssets:experimentActivated:experiment:error:]_block_invoke_2
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.584
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.585
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.595
+ ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.596
+ ___131-[UAFAssetSetExperiment remapExperimentalAssets:specifierToAssetName:availableSpecifiers:experimentActivated:uafAssetForSpecifier:]_block_invoke
+ ___131-[UAFAssetSetExperiment remapExperimentalAssets:specifierToAssetName:availableSpecifiers:experimentActivated:uafAssetForSpecifier:]_block_invoke_2
+ ___131-[UAFAssetSetExperiment remapExperimentalAssets:specifierToAssetName:availableSpecifiers:experimentActivated:uafAssetForSpecifier:]_block_invoke_3
+ ___131-[UAFAssetSetExperiment remapExperimentalAssets:specifierToAssetName:availableSpecifiers:experimentActivated:uafAssetForSpecifier:]_block_invoke_4
+ ___131-[UAFAssetSetExperiment remapExperimentalAssets:specifierToAssetName:availableSpecifiers:experimentActivated:uafAssetForSpecifier:]_block_invoke_5
+ ___138+[UAFAutoAssetManager metadataForAssetSetUsages:configurationManager:expensiveNetworking:localOnly:includeSpecifierKeys:queue:completion:]_block_invoke
+ ___138+[UAFAutoAssetManager metadataForAssetSetUsages:configurationManager:expensiveNetworking:localOnly:includeSpecifierKeys:queue:completion:]_block_invoke.614
+ ___138+[UAFAutoAssetManager metadataForAssetSetUsages:configurationManager:expensiveNetworking:localOnly:includeSpecifierKeys:queue:completion:]_block_invoke.622
+ ___138+[UAFAutoAssetManager metadataForAssetSetUsages:configurationManager:expensiveNetworking:localOnly:includeSpecifierKeys:queue:completion:]_block_invoke.629
+ ___138+[UAFAutoAssetManager metadataForAssetSetUsages:configurationManager:expensiveNetworking:localOnly:includeSpecifierKeys:queue:completion:]_block_invoke_2
+ ___138+[UAFAutoAssetManager metadataForAssetSetUsages:configurationManager:expensiveNetworking:localOnly:includeSpecifierKeys:queue:completion:]_block_invoke_2.624
+ ___138+[UAFAutoAssetManager metadataForAssetSetUsages:configurationManager:expensiveNetworking:localOnly:includeSpecifierKeys:queue:completion:]_block_invoke_3
+ ___138+[UAFAutoAssetManager metadataForAssetSetUsages:configurationManager:expensiveNetworking:localOnly:includeSpecifierKeys:queue:completion:]_block_invoke_3.625
+ ___27-[UAFXPCService runUpdates]_block_invoke.425
+ ___29+[UAFUserManager removeUser:]_block_invoke.362
+ ___31-[UAFXPCConnection _connection]_block_invoke.359
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.371
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.373
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.377
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.378
+ ___36+[UAFUserManager performUserCleanup]_block_invoke.379
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.537
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.539
+ ___40+[UAFBiomeStreamWriter _getAllAssetSets]_block_invoke
+ ___40+[UAFRootsV2AssetSet getConcurrentQueue]_block_invoke
+ ___40-[UAFXPCConnection expireSubscriptions:]_block_invoke.370
+ ___42-[UAFXPCConnection diagnosticInformation:]_block_invoke.362
+ ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.448
+ ___44-[UAFRootsV2AssetSet loadAssets:experiment:]_block_invoke
+ ___44-[UAFRootsV2AssetSet loadAssets:experiment:]_block_invoke_2
+ ___45-[UAFAutoAssetSet mapAsset:queue:completion:]_block_invoke.409
+ ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.459
+ ___49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke.366
+ ___50-[UAFAutoAssetSet invalidateWithQueue:completion:]_block_invoke.390
+ ___51-[UAFXPCConnection operationWithConfig:completion:]_block_invoke.361
+ ___52+[UAFAutoAssetManager removeDeprecatedAutoAssetSets]_block_invoke.564
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.411
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.415
+ ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.416
+ ___54-[UAFXPCConnection requestSubscriptionDatabaseAccess:]_block_invoke
+ ___54-[UAFXPCConnection requestSubscriptionDatabaseAccess:]_block_invoke.373
+ ___54-[UAFXPCConnection requestSubscriptionDatabaseAccess:]_block_invoke_2
+ ___57+[UAFAutoAssetManager lockLatestAssetSet:atomicInstance:]_block_invoke.523
+ ___57+[UAFAutoAssetManager lockLatestAssetSet:atomicInstance:]_block_invoke_2
+ ___57+[UAFUserManager updateLastSeenForUser:queue:completion:]_block_invoke.358
+ ___58+[UAFCommonUtilities activateExperimentId:trialNamespace:]_block_invoke
+ ___58-[UAFAssetSetManager ensureSubscriptionDatabaseAccessSync]_block_invoke
+ ___58-[UAFXPCConnection requestSubscriptionDatabaseAccessSync:]_block_invoke
+ ___58-[UAFXPCConnection requestSubscriptionDatabaseAccessSync:]_block_invoke.374
+ ___58-[UAFXPCConnection requestSubscriptionDatabaseAccessSync:]_block_invoke_2
+ ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.546
+ ___61-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke.371
+ ___64+[UAFAutoAssetManager requestSandboxExtension:queue:completion:]_block_invoke
+ ___64+[UAFAutoAssetManager requestSandboxExtension:queue:completion:]_block_invoke_2
+ ___65+[UAFAutoAssetManager manageMetadataCacheForConfig:autoAssetSet:]_block_invoke
+ ___65+[UAFAutoAssetManager manageMetadataCacheForConfig:autoAssetSet:]_block_invoke.572
+ ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.387
+ ___67+[UAFAssetInfoCache maintainCacheForAssetSet:latestAtomicInstance:]_block_invoke
+ ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.512
+ ___70+[UAFCommonUtilities emptyLegacyStagingLogsDirectoryUnderStoragePath:]_block_invoke
+ ___70-[UAFXPCConnection invalidateRootsV2Instance:assetSetName:completion:]_block_invoke
+ ___70-[UAFXPCConnection invalidateRootsV2Instance:assetSetName:completion:]_block_invoke.367
+ ___70-[UAFXPCConnection invalidateRootsV2Instance:assetSetName:completion:]_block_invoke_2
+ ___70-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke.369
+ ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke.369
+ ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke_2.370
+ ___71-[UAFSubscriptionStoreManager getSubscriptionsAsDictionary:user:error:]_block_invoke
+ ___71-[UAFXPCConnection lockLatestAtomicInstance:atomicInstance:completion:]_block_invoke.365
+ ___75-[UAFAssetSetManager ensureSubscriptionDatabaseAccessWithQueue:completion:]_block_invoke
+ ___75-[UAFAssetSetManager ensureSubscriptionDatabaseAccessWithQueue:completion:]_block_invoke.397
+ ___75-[UAFAssetSetManager ensureSubscriptionDatabaseAccessWithQueue:completion:]_block_invoke_2
+ ___78-[UAFXPCConnection disableMAAtomicInstanceForRootsV2:assetSetName:completion:]_block_invoke
+ ___78-[UAFXPCConnection disableMAAtomicInstanceForRootsV2:assetSetName:completion:]_block_invoke.368
+ ___78-[UAFXPCConnection disableMAAtomicInstanceForRootsV2:assetSetName:completion:]_block_invoke_2
+ ___79-[UAFAssetSetManager _sizeForSubscriptions:policies:sumByKey:queue:completion:]_block_invoke
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.498
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.505
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.506
+ ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.507
+ ___85+[UAFRootsV2AssetSet requestInvalidateRootsV2Instance:assetSetName:queue:completion:]_block_invoke
+ ___85+[UAFRootsV2AssetSet requestInvalidateRootsV2Instance:assetSetName:queue:completion:]_block_invoke_2
+ ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.529
+ ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.508
+ ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.558
+ ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.559
+ ___91+[UAFAssetSetManager isSubscriptionExpirationIgnorable:subscriber:user:storeSubscriptions:]_block_invoke
+ ___93+[UAFRootsV2AssetSet requestDisableMAAtomicInstanceForRootsV2:assetSetName:queue:completion:]_block_invoke
+ ___93+[UAFRootsV2AssetSet requestDisableMAAtomicInstanceForRootsV2:assetSetName:queue:completion:]_block_invoke_2
+ ___94-[UAFAssetSetManager metadataForSubscriptions:policies:includeSpecifierKeys:queue:completion:]_block_invoke
+ ___94-[UAFAssetSetManager metadataForSubscriptions:policies:includeSpecifierKeys:queue:completion:]_block_invoke.429
+ ___94-[UAFAssetSetManager metadataForSubscriptions:policies:includeSpecifierKeys:queue:completion:]_block_invoke_2
+ ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.597
+ ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.404
+ ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.408
+ ___Block_byref_object_copy_.612
+ ___Block_byref_object_dispose_.613
+ ____RegisterPeriodicUAFSubscriptionActivity_block_invoke.384
+ ____RegisterPostUpgradeUAFActivity_block_invoke.378
+ ____RegisterXPCActivity_block_invoke.365
+ ___block_descriptor_40_e8_32r_e27_B24?0"NSURL"8"NSError"16lr32l8
+ ___block_descriptor_40_e8_32s_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e34_v32?0"NSString"8"NSArray"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e41_"UAFAsset"24?0"NSString"8"NSString"16ls32l8s40l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e34_v32?0"NSString"8"NSArray"16^B24ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e29_v24?0"NSArray"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e30_v24?0"NSString"8"NSError"16ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e41_"UAFAsset"24?0"NSString"8"NSString"16ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e35_v32?0"NSString"8"NSString"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e17_B16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e25_v32?0"NSString"8Q16^B24ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e40_v32?0"UAFAssetSetSubscription"8Q16^B24ls32l8s40l8s48l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e37_v32?0"NSDictionary"8q16"NSError"24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40bs48r56r64r_e17_v16?0"NSArray"8lr48l8r56l8r64l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_81_e8_32s40s48s56bs64bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s56l8s64l8s40l8s48l8
+ ___block_descriptor_81_e8_32s40s48s56s64bs72bs_e37_v32?0"NSDictionary"8q16"NSError"24ls32l8s64l8s72l8s40l8s48l8s56l8
+ ___block_literal_global.374
+ ___block_literal_global.382
+ ___block_literal_global.383
+ ___block_literal_global.386
+ ___block_literal_global.390
+ ___block_literal_global.391
+ ___block_literal_global.393
+ ___block_literal_global.455
+ ___block_literal_global.458
+ ___block_literal_global.467
+ ___block_literal_global.495
+ ___block_literal_global.515
+ ___block_literal_global.536
+ ___block_literal_global.543
+ ___block_literal_global.545
+ ___block_literal_global.563
+ ___block_literal_global.567
+ ___block_literal_global.575
+ ___block_literal_global.577
+ _kCFAllocatorDefault
+ _kUAConfigurationStageSubdir
+ _kUAFABCAssetSourceUknownFailure
+ _kUAFABCInstrumentationFailure
+ _kUAFABCMissingAvailableOSBuildFailure
+ _kUAFABCMissingDownloadedOSBuildFailure
+ _kUAFABCSandboxExtensionFailure
+ _kUAFAdopterExperimentActivation
+ _kUAFAssetInfoCacheMetadataFileExt
+ _kUAFAssetMetadataSourceAssetRootsV2Value
+ _kUAFAssetRootsV2Directory
+ _kUAFAutoAssetMetadataKeyNotFound
+ _kUAFAutoAssetMetadataSpecifier
+ _kUAFAutoAssetMetadataTimestamp
+ _kUAFAutoAssetMetadataVersion
+ _kUAFCacheManagementOperation
+ _kUAFCacheManagementSpecifier
+ _kUAFDisabledByRootsV2Extension
+ _kUAFPolicyLocalOnly
+ _kUAFRootsV2LockExtension
+ _kUAFSlashPrivatePrefix
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$AssetSetAlterActivity
+ _objc_msgSend$AssetSetStatus
+ _objc_msgSend$DailyScheduledAssetStatus
+ _objc_msgSend$_getAllAssetSets
+ _objc_msgSend$_getBiomeAssetSetStatus:atomicInstanceMetadata:assetSetOriginReport:entries:errorCodes:
+ _objc_msgSend$_getBiomeStreamForAssetSetStatus:atomicInstanceMetadata:assetSetOriginReport:entries:errorCodes:assetSetDailyStatusEventType:
+ _objc_msgSend$_getBiomeUAFAssetSet:atomicInstanceMetadata:assetSetOriginReport:entries:errorCodes:
+ _objc_msgSend$_getConfiguredAssetCountFor:
+ _objc_msgSend$_getConfiguredAssetCountFor:autoAssetType:
+ _objc_msgSend$_getSubscriptionsAsDictionary:subscriptionsFor:
+ _objc_msgSend$_getSubscriptionsAsDictionary:user:
+ _objc_msgSend$_prepareGetSubscriptionsStatement:user:
+ _objc_msgSend$_processSubscriptionDatabaseExtensionToken:xpcError:error:
+ _objc_msgSend$_sizeForSubscriptions:policies:sumByKey:queue:completion:
+ _objc_msgSend$_subscriptionDatabaseAccessIsGranted
+ _objc_msgSend$_subscriptionDiffersFromDB:subscriber:user:expirationOnlyCount:storeSubscriptions:error:
+ _objc_msgSend$activateExperimentId:trialNamespace:
+ _objc_msgSend$adopterExperimentActivation
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendMetadataExtensionToPath:
+ _objc_msgSend$assetSet
+ _objc_msgSend$assetSetDirectoryForAssetSet:
+ _objc_msgSend$assetSetIdForSELF:atomicInstanceMetadata:
+ _objc_msgSend$assetSetPath:
+ _objc_msgSend$atomicInstanceMetadataForAssetSet:atomicInstance:error:
+ _objc_msgSend$atomicInstancePath:atomicInstance:
+ _objc_msgSend$auditToken
+ _objc_msgSend$cachedAssetsForAssetSet:atomicInstance:autoAssets:experimentActivated:experiment:error:
+ _objc_msgSend$checkDownloadSize:withLookupPolicy:completion:
+ _objc_msgSend$checkLocalDownloadSize:completion:
+ _objc_msgSend$checkPolicyForConfig:expensiveNetworking:
+ _objc_msgSend$client
+ _objc_msgSend$createFileAtPath:contents:attributes:
+ _objc_msgSend$createSymbolicLinkAtPath:withDestinationPath:error:
+ _objc_msgSend$currentRootsV2InstanceIdForAssetSet:
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$dictionaryWithObject:forKey:
+ _objc_msgSend$directoryEnumeratorAtPath:
+ _objc_msgSend$disableMAAtomicInstanceForRootsV2:assetSetName:completion:
+ _objc_msgSend$disabledByRootsV2MarkerPathForAtomicInstance:assetSetName:
+ _objc_msgSend$emptyLegacyStagingLogsDirectoryUnderStoragePath:
+ _objc_msgSend$ensureSubscriptionDatabaseAccessSync
+ _objc_msgSend$experimentIdentifiersTrialClient:trialNamespace:staged:
+ _objc_msgSend$filterMetadata:specifiers:onDiskKeys:includeSpecifierKeys:
+ _objc_msgSend$findDiffBetweenOldAssetSetUsages:newAssetSetUsages:configurationManager:
+ _objc_msgSend$getAssetWithName:andSpecifier:experimentationEnabled:experimentId:
+ _objc_msgSend$getAtomicInstanceMetadataPath:atomicInstance:
+ _objc_msgSend$getCachedAsset:specifier:atomicInstanceCachePath:experimentationEnabled:experimentId:error:
+ _objc_msgSend$getMADownloadErrors:newerVersionError:assetSetName:assetSetID:
+ _objc_msgSend$getSpecifierToAssetNameMap:
+ _objc_msgSend$getSubscriptionsAsDictionary:storeManager:
+ _objc_msgSend$getSubscriptionsAsDictionary:user:error:
+ _objc_msgSend$initFromAssetInfoCache:autoAssets:experiment:atomicInstance:
+ _objc_msgSend$initWithAssetSetName:assets:uuid:rootsV2InstanceId:experiment:error:
+ _objc_msgSend$initWithAssetSpecifier:assetVersion:assetSource:assetDownloadSizeInBytes:assetUnarchivedSizeInBytes:sourceOSBuild:promotedOSBuild:
+ _objc_msgSend$initWithAssetType:assetSetId:configuredAssets:assets:vendedConfiguredAssets:newerVersionErrorCode:availableForUseErrorCode:fromPreSoftwareUpdateStaging:fromFactory:
+ _objc_msgSend$initWithAssetType:configuredAssets:addedAssets:eliminatedAssets:assetSource:
+ _objc_msgSend$initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:rootsV2InstanceId:
+ _objc_msgSend$initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:rootsV2InstanceId:bootUUID:experimentActivated:
+ _objc_msgSend$initWithUafAssetSet:statusReason:
+ _objc_msgSend$initWithUafAssetSets:
+ _objc_msgSend$initializeRootsV2WithInstanceId:assetSet:consistencyToken:
+ _objc_msgSend$instanceDirectoryForSpecifier:
+ _objc_msgSend$invalidateRootsV2Instance:assetSetName:completion:
+ _objc_msgSend$isActivatedForAvailableSpecifiers:
+ _objc_msgSend$isAssetInfoCacheSupported
+ _objc_msgSend$isConnectionAppleSigned:error:
+ _objc_msgSend$isMAAtomicInstanceDisabledByRootsV2:assetSetName:
+ _objc_msgSend$isSubscriptionExpirationIgnorable:subscriber:user:storeSubscriptions:
+ _objc_msgSend$isV2Available
+ _objc_msgSend$loadAssets:experiment:
+ _objc_msgSend$lockAssets:error:
+ _objc_msgSend$lockFilePathForInstanceId:assetSetName:
+ _objc_msgSend$lockRootsV2InstanceId:assetSetName:error:
+ _objc_msgSend$logAlterFromAtomicInstance:assetType:configuredSpecifiers:sourceType:alterSetData:
+ _objc_msgSend$logAlterFromAtomicInstance:sourceType:configuredSpecifiers:addedAssets:removedAssets:
+ _objc_msgSend$logAssetSetArrivedEvent:atomicInstanceMetadata:assetSetOriginReport:entries:
+ _objc_msgSend$logAssetSetDownloadErrorEvent:atomicInstanceMetadata:errorCodes:
+ _objc_msgSend$maLockerPathForAtomicInstance:assetSetName:
+ _objc_msgSend$maintainCacheForAssetSet:latestAtomicInstance:
+ _objc_msgSend$manageExperiment:config:consistencyToken:
+ _objc_msgSend$manageExperimentFor:consistencyToken:
+ _objc_msgSend$manageMetadataCacheForConfig:autoAssetSet:
+ _objc_msgSend$metadataForAssetSetUsages:configurationManager:expensiveNetworking:localOnly:includeSpecifierKeys:queue:completion:
+ _objc_msgSend$metadataForSubscriptions:policies:includeSpecifierKeys:queue:completion:
+ _objc_msgSend$notReadyPath:atomicInstance:
+ _objc_msgSend$onDiskKeys
+ _objc_msgSend$originType
+ _objc_msgSend$pathByResolvingSymlinksButKeepingPrivatePrefix:
+ _objc_msgSend$policy
+ _objc_msgSend$readAtomicInstanceInfoFromAssetInfoCache:autoAssets:experiment:atomicInstance:
+ _objc_msgSend$remapExperimentalAssets:specifierToAssetName:availableSpecifiers:experimentActivated:uafAssetForSpecifier:
+ _objc_msgSend$removeDisabledByRootsV2MarkerForAtomicInstance:assetSetName:
+ _objc_msgSend$removeDisabledByRootsV2MarkersForAssetSet:
+ _objc_msgSend$requestDisableMAAtomicInstanceForRootsV2:assetSetName:queue:completion:
+ _objc_msgSend$requestExperimentActivationForNamespaceName:completion:
+ _objc_msgSend$requestInvalidateRootsV2Instance:assetSetName:queue:completion:
+ _objc_msgSend$requestSandboxExtension:
+ _objc_msgSend$requestSandboxExtension:queue:completion:
+ _objc_msgSend$requestSubscriptionDatabaseAccess:
+ _objc_msgSend$requestSubscriptionDatabaseAccessSync:
+ _objc_msgSend$resolveConsistencyToken:
+ _objc_msgSend$rootsV2Directory
+ _objc_msgSend$rootsV2InstanceId
+ _objc_msgSend$sandboxCheckFileRead:
+ _objc_msgSend$sandboxExtensionConsume:error:
+ _objc_msgSend$sandboxExtensionIssueFileToProcess:path:flags:auditToken:error:
+ _objc_msgSend$secTaskCopySigningIdentifier:error:
+ _objc_msgSend$secTaskCreateWithAllocator:auditToken:
+ _objc_msgSend$setAssetSet:
+ _objc_msgSend$setAssetSetName:
+ _objc_msgSend$setOnDiskKeys:
+ _objc_msgSend$setPolicy:
+ _objc_msgSend$setSpecifiers:
+ _objc_msgSend$setupExperiment:disableExperimentation:
+ _objc_msgSend$specifierDirectoryExistsOnDisk:
+ _objc_msgSend$specifierDirectoryExistsOnDisk:atomicInstance:specifier:
+ _objc_msgSend$specifierPath:atomicInstance:specifier:
+ _objc_msgSend$specifiers
+ _objc_msgSend$stageAssetSet:targets:
+ _objc_msgSend$staged
+ _objc_msgSend$stagedExperimentIdentifiersWithNamespaceName:
+ _objc_msgSend$stagedLevelForFactor:withNamespaceName:
+ _objc_msgSend$stringByAppendingPathExtension:
+ _objc_msgSend$stringByResolvingSymlinksInPath
+ _objc_msgSend$sumMetadataEntries:forKey:
+ _objc_msgSend$targetForAssetSet:specifiers:version:
+ _objc_msgSend$trialClient
+ _objc_msgSend$unsubscribe:subscriptionNames:queue:completion:
+ _objc_msgSend$updateCacheIfNeeded:atomicEntries:atomicInstance:
+ _objc_msgSend$wantsRemapping
+ _objc_msgSend$writeCacheForAssetSet:atomicInstance:atomicEntries:atomicInstanceMetadata:error:
+ _objc_msgSend$writeToFile:atomically:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x5
+ _objc_retain_x6
+ _sBasePath
+ _sandbox_extension_consume
+ _sandbox_extension_issue_file_to_process
+ _swift_release_x20
+ _swift_release_x22
+ _swift_release_x8
+ _swift_retain_x20
+ _swift_retain_x22
- +[UAFAssetSetManager _subscriptionDiffersFromDB:subscriber:user:expirationOnlyCount:error:]
- +[UAFAssetSetManager isSubscriptionExpirationIgnorable:subscriber:user:]
- +[UAFAssetStatus dictationAvailableForLanguage:]
- +[UAFAutoAssetInstance clear:path:]
- +[UAFAutoAssetInstance decomposeSaveFileURL:assetSetName:atomicInstance:]
- +[UAFAutoAssetInstance instanceDirURL]
- +[UAFAutoAssetInstance saveFileURL:]
- +[UAFAutoAssetManager findDiffBetweenOldAssetSetUsages:newAssetSetUsages:knownAssetSets:usedAssetSets:configurationManager:]
- +[UAFAutoAssetManager removeUnusedAutoAssetSets:usedAutoAssetSets:]
- +[UAFAutoAssetManager stageAssetSet:targets:platformAssetVersion:]
- +[UAFAutoAssetManager stageAssetsWithNewSubscriptions:oldSubscriptions:autoAssetSets:]
- +[UAFAutoAssetManager targetForAssetSet:specifiers:version:autoAssetSets:]
- +[UAFBiomeInstrumenter _getBiomeAssetSetStatus:atomicInstanceMetadata:entries:errorCodes:]
- +[UAFBiomeInstrumenter _getBiomeStreamForAssetSetStatus:atomicInstanceMetadata:entries:errorCodes:assetSetDailyStatusEventType:]
- +[UAFBiomeInstrumenter _getBiomeUAFAssetSet:atomicInstanceMetadata:entries:errorCodes:]
- +[UAFCommonUtilities assistantModeDescription:]
- +[UAFCommonUtilities assistantModeFromDescription:mode:]
- +[UAFCommonUtilities bestSupportedSiriLanguage]
- +[UAFCommonUtilities currentAssistantLanguage]
- +[UAFCommonUtilities currentAssistantMode]
- +[UAFCommonUtilities deviceSupportAndUseHybridASR]
- +[UAFCommonUtilities deviceSupportFullUOD]
- +[UAFCommonUtilities experimentIdentifiersTrialClient:trialNamespace:]
- +[UAFCommonUtilities getFreeDiskSpaceInBytes]
- +[UAFCommonUtilities getFreeDiskSpaceNeededInBytes:]
- +[UAFCommonUtilities gmsWantsAssets]
- +[UAFCommonUtilities isAssistantEnabled]
- +[UAFCommonUtilities isDictationEnabled]
- +[UAFCommonUtilities isFullUODSupportedForStatus:language:]
- +[UAFCommonUtilities isHybridUODSupportedForStatus:language:]
- +[UAFCommonUtilities systemLanguage]
- +[UAFCommonUtilities trialClientWithProject:]
- +[UAFInstrumentationProvider _getMADownloadErrors:newerVersionError:assetSetName:assetSetID:]
- +[UAFInstrumentationProvider logAlterFromAtomicInstance:sourceType:alterSetData:]
- +[UAFManagedSubscriptions _assistantUsageAliasForMode:]
- +[UAFManagedSubscriptions _deviceSupportsGenerativeModelSystems]
- +[UAFManagedSubscriptions _stageAssetsUponPlatformAssetSetUpdate]
- +[UAFManagedSubscriptions isOnDemandAssetSubscriptionAllowed]
- +[UAFManagedSubscriptions manageAssistantSubscription:withMode:]
- +[UAFManagedSubscriptions manageAssistantSubscription:withMode:subscriber:subscriptionName:shouldReport:]
- +[UAFManagedSubscriptions manageGMSSiriLanguageSubscription:language:mode:]
- +[UAFManagedSubscriptions manageMorphunSystemLocaleSubscription:]
- +[UAFManagedSubscriptions manageNLSystemLanguageSubscription:]
- +[UAFManagedSubscriptions manageNLSystemLanguageSubscription:subscriber:subscriptionName:]
- +[UAFManagedSubscriptions managePlatformSubscription]
- +[UAFManagedSubscriptions manageSummarizationKitSubscription]
- +[UAFManagedSubscriptions morphunUsagesForLocale:]
- +[UAFPlatform configurationManagers:]
- +[UAFPlatform platformAssetVersion:]
- +[UAFStagingLogManager createBuildVersionFile]
- +[UAFStagingLogManager createLogEntryWithInfo:]
- +[UAFStagingLogManager deleteItemAtURL:error:]
- +[UAFStagingLogManager deleteLoggedTargetsForEliminatedAssetSet:]
- +[UAFStagingLogManager findOrCreateDir:]
- +[UAFStagingLogManager getBuildVersionFromStagingLogsDir]
- +[UAFStagingLogManager getLastBuildStagingLogsDir]
- +[UAFStagingLogManager getLatestStagingLogsDir]
- +[UAFStagingLogManager getLogFileForTarget:andAssetSetName:]
- +[UAFStagingLogManager getRootStagingLogsDir]
- +[UAFStagingLogManager getSerialQueue]
- +[UAFStagingLogManager logTargetSync:withAssetSetName:withPlatformAssetVersion:]
- +[UAFStagingLogManager logTargets:withAssetSetName:withPlatformAssetVersion:]
- +[UAFStagingLogManager moveItemAtURL:toURL:]
- +[UAFStagingLogManager rollStagingLogsUponNewBuildVersion]
- +[UAFStagingLogManager serializeJSONObjectToData:]
- +[UAFStagingLogManager writeToFile:content:]
- -[UAFAssetSet assetSetIdForSELF:assetSetOrigin:]
- -[UAFAssetSetConfiguration isUsageLimitExceeded:]
- -[UAFAssetSetConfiguration setUsageLimits:]
- -[UAFAssetSetConfiguration usageLimits]
- -[UAFAssetSetConsistencyToken initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:]
- -[UAFAssetSetConsistencyToken initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:bootUUID:experimentActivated:]
- -[UAFAssetUtilities .cxx_destruct]
- -[UAFAssetUtilities _assistantLanguageUpdate]
- -[UAFAssetUtilities _assistantPreferencesUpdate]
- -[UAFAssetUtilities _checkFreeSpaceNeededForLanguage:forClient:]
- -[UAFAssetUtilities _createConnection]
- -[UAFAssetUtilities _downloadSiriAssetsOverCellular:]
- -[UAFAssetUtilities _downloadSiriAssetsRetry]
- -[UAFAssetUtilities _downloadSiriAssetsWithDelay:]
- -[UAFAssetUtilities _handleNetworkPathUpdate:]
- -[UAFAssetUtilities _networkIsExpensiveForPath:]
- -[UAFAssetUtilities _networkIsSatisfiedForPath:]
- -[UAFAssetUtilities _stopObservers]
- -[UAFAssetUtilities _triggerDelegateAssetStatusUpdated]
- -[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]
- -[UAFAssetUtilities assetAvailableCheckTimeout]
- -[UAFAssetUtilities assetStatus]
- -[UAFAssetUtilities assetsAreAvailableForLanguage:completion:]
- -[UAFAssetUtilities assistantEnabled]
- -[UAFAssetUtilities assistantGroup]
- -[UAFAssetUtilities assistantQueue]
- -[UAFAssetUtilities assistantUODStatus]
- -[UAFAssetUtilities autoRetryDelayOnFailureIncrement]
- -[UAFAssetUtilities autoRetryDelayOnFailure]
- -[UAFAssetUtilities autoRetryDelayOnSettingsChanged]
- -[UAFAssetUtilities autoRetryEnabled]
- -[UAFAssetUtilities autoRetryLimit]
- -[UAFAssetUtilities currentAssetStatus]
- -[UAFAssetUtilities dealloc]
- -[UAFAssetUtilities delegateQueue]
- -[UAFAssetUtilities delegate]
- -[UAFAssetUtilities downloadQueue]
- -[UAFAssetUtilities downloadSiriAssetsIfNeeded]
- -[UAFAssetUtilities downloadSiriAssetsOverCellular]
- -[UAFAssetUtilities downloadSiriAssets]
- -[UAFAssetUtilities getAssistantLanguageIfAvailableSync]
- -[UAFAssetUtilities getDiskSpaceNeededInBytesForLanguage:forClient:]
- -[UAFAssetUtilities hasSufficientDiskSpaceForClient:]
- -[UAFAssetUtilities hasSufficientDiskSpaceForDownload]
- -[UAFAssetUtilities init]
- -[UAFAssetUtilities networkExpensive]
- -[UAFAssetUtilities networkSatisfied]
- -[UAFAssetUtilities refreshUAFAssetStatusAsync]
- -[UAFAssetUtilities refreshUnderstandingOnDeviceAssetsAvailableAsync]
- -[UAFAssetUtilities retryState]
- -[UAFAssetUtilities setAssetAvailableCheckTimeout:]
- -[UAFAssetUtilities setAssetStatus:]
- -[UAFAssetUtilities setAssistantEnabled:]
- -[UAFAssetUtilities setAssistantGroup:]
- -[UAFAssetUtilities setAssistantQueue:]
- -[UAFAssetUtilities setAssistantUODStatus:]
- -[UAFAssetUtilities setAutoRetryDelayOnFailure:]
- -[UAFAssetUtilities setAutoRetryDelayOnFailureIncrement:]
- -[UAFAssetUtilities setAutoRetryDelayOnSettingsChanged:]
- -[UAFAssetUtilities setAutoRetryEnabled:]
- -[UAFAssetUtilities setAutoRetryLimit:]
- -[UAFAssetUtilities setDelegate:]
- -[UAFAssetUtilities setDelegateQueue:]
- -[UAFAssetUtilities setDownloadQueue:]
- -[UAFAssetUtilities setNetworkExpensive:]
- -[UAFAssetUtilities setNetworkSatisfied:]
- -[UAFAssetUtilities setRetryState:]
- -[UAFAssetUtilities setShowHybridAsUnsupported:]
- -[UAFAssetUtilities setSiriLanguage:]
- -[UAFAssetUtilities setStatusQueue:]
- -[UAFAssetUtilities setUnderstandingOnDeviceAssetsAvailable:]
- -[UAFAssetUtilities showHybridAsUnsupported]
- -[UAFAssetUtilities siriLanguage]
- -[UAFAssetUtilities startObserversWithOptions:]
- -[UAFAssetUtilities startObservers]
- -[UAFAssetUtilities statusQueue]
- -[UAFAssetUtilities understandingOnDeviceAssetsAvailable]
- -[UAFAssetUtilitiesService .cxx_destruct]
- -[UAFAssetUtilitiesService _checkFreeSpaceNeededForLanguage:isDictation:]
- -[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]
- -[UAFAssetUtilitiesService _downloadSiriAssetsWithCellular:]
- -[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]
- -[UAFAssetUtilitiesService _getDiskSpaceNeededInBytesForLanguage:isDictation:error:]
- -[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]
- -[UAFAssetUtilitiesService _handleDictationProgress:status:language:]
- -[UAFAssetUtilitiesService _handleUpdateProgress:status:language:]
- -[UAFAssetUtilitiesService _isLegacySiriDevice]
- -[UAFAssetUtilitiesService _postAssetStateChangedNotification]
- -[UAFAssetUtilitiesService _siriDownloadCompleteForLanguage:]
- -[UAFAssetUtilitiesService _stopObserver]
- -[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]
- -[UAFAssetUtilitiesService _updateAssetState:value:forLanguage:]
- -[UAFAssetUtilitiesService _updateDictationAvailabilityForLanguage:]
- -[UAFAssetUtilitiesService _updateDictationProgress:language:]
- -[UAFAssetUtilitiesService _updateDictationState:value:forLanguage:]
- -[UAFAssetUtilitiesService _updateProgress:forLanguage:]
- -[UAFAssetUtilitiesService _updateSiriAssetAvailability:forLanguage:]
- -[UAFAssetUtilitiesService assetStatus]
- -[UAFAssetUtilitiesService checkAssetStatus:]
- -[UAFAssetUtilitiesService dealloc]
- -[UAFAssetUtilitiesService dictationStatus]
- -[UAFAssetUtilitiesService diskSpaceNeededInBytesForLanguage:forClient:completion:]
- -[UAFAssetUtilitiesService downloadDictationAssetsForLanguage:]
- -[UAFAssetUtilitiesService downloadQueue]
- -[UAFAssetUtilitiesService downloadSiriAssetsOverCellular]
- -[UAFAssetUtilitiesService downloadSiriAssets]
- -[UAFAssetUtilitiesService getLanguage]
- -[UAFAssetUtilitiesService init]
- -[UAFAssetUtilitiesService postAssetNotificationIfNeeded]
- -[UAFAssetUtilitiesService postDictationAssetNotificationForLanguage:]
- -[UAFAssetUtilitiesService resume]
- -[UAFAssetUtilitiesService setAssetStatus:]
- -[UAFAssetUtilitiesService setDictationStatus:]
- -[UAFAssetUtilitiesService setDownloadQueue:]
- -[UAFAssetUtilitiesService setStatusGroup:]
- -[UAFAssetUtilitiesService setStatusQueue:]
- -[UAFAssetUtilitiesService setUodAvailable:]
- -[UAFAssetUtilitiesService startObserver]
- -[UAFAssetUtilitiesService statusGroup]
- -[UAFAssetUtilitiesService statusQueue]
- -[UAFAssetUtilitiesService suspend]
- -[UAFAssetUtilitiesService switchLanguage:]
- -[UAFAssetUtilitiesService uodAvailable]
- -[UAFAssetUtilitiesService updateAssetState:value:forLanguage:]
- -[UAFAssetUtilitiesService updateSiriAssetAvailabilityForLanguage:]
- -[UAFAssetUtilitiesService updateSiriAssetAvailabilityForLanguageSync:]
- -[UAFAssetUtilitiesService updateSiriAssetAvailabilityForObserver]
- -[UAFConfigurationManager isUsageLimitExceeded:]
- -[UAFSubscriptionStoreManager _isUsageLimitExceeded:]
- -[UAFXPCConnection checkAssetStatus:]
- -[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]
- -[UAFXPCConnection downloadDictationAssetsForLanguage:]
- -[UAFXPCConnection downloadSiriAssetsOverCellular]
- -[UAFXPCConnection downloadSiriAssets]
- -[UAFXPCConnection postAssetNotificationIfNeeded]
- -[UAFXPCConnection postDictationAssetNotificationForLanguage:]
- -[UAFXPCService _assistantCapabilitiesUpdate]
- -[UAFXPCService _assistantEnabledChanged]
- -[UAFXPCService _assistantGMSAvailabilityUpdate]
- -[UAFXPCService _assistantLanguageChanged]
- -[UAFXPCService _assistantLanguageUpdate]
- -[UAFXPCService _assistantModeChanged]
- -[UAFXPCService _assistantPreferencesUpdate]
- -[UAFXPCService _assistantUpdate]
- -[UAFXPCService _dictationEnabledChanged]
- -[UAFXPCService _gmsEnabledChanged]
- -[UAFXPCService _startObservers]
- -[UAFXPCService _stopObservers]
- -[UAFXPCService _systemLanguageChanged]
- -[UAFXPCService _systemLanguageUpdate]
- -[UAFXPCService _updateAssetUtilitiesLanguage]
- -[UAFXPCService _updateAssistantSubscription]
- -[UAFXPCService _updateGMSSiriLanguageSubscription]
- -[UAFXPCService _updateMorphunSystemLanguageSubscription]
- -[UAFXPCService _updateNLSystemLanguageSubscription]
- -[UAFXPCService _updateShadowSiriLocale:]
- -[UAFXPCService _updateShadowSiriLocaleIfNeeded]
- -[UAFXPCService assistantEnabled]
- -[UAFXPCService assistantLanguage]
- -[UAFXPCService assistantMode]
- -[UAFXPCService checkAssetStatus:]
- -[UAFXPCService dictationEnabled]
- -[UAFXPCService diskSpaceNeededInBytesForLanguage:forClient:completion:]
- -[UAFXPCService downloadDictationAssetsForLanguage:]
- -[UAFXPCService downloadSiriAssetsOverCellular]
- -[UAFXPCService downloadSiriAssets]
- -[UAFXPCService gmsEnabled]
- -[UAFXPCService postAssetNotificationIfNeeded]
- -[UAFXPCService postDictationAssetNotificationForLanguage:]
- -[UAFXPCService systemLanguage]
- GCC_except_table102
- GCC_except_table108
- GCC_except_table131
- GCC_except_table14
- GCC_except_table16
- GCC_except_table20
- GCC_except_table22
- GCC_except_table28
- GCC_except_table30
- GCC_except_table35
- GCC_except_table38
- GCC_except_table39
- GCC_except_table4
- GCC_except_table44
- GCC_except_table45
- GCC_except_table48
- GCC_except_table50
- GCC_except_table53
- GCC_except_table59
- GCC_except_table60
- GCC_except_table66
- GCC_except_table71
- GCC_except_table72
- GCC_except_table75
- GCC_except_table79
- GCC_except_table8
- GCC_except_table82
- GCC_except_table94
- _AFSiriXAssetDidChangeCallback
- _AssistantServicesLibrary
- _AssistantServicesLibraryCore.frameworkLibrary
- _CFNotificationCenterAddObserver
- _CFNotificationCenterGetDarwinNotifyCenter
- _CFNotificationCenterPostNotification
- _CFNotificationCenterRemoveObserver
- _MGGetBoolAnswer
- _NSFileSystemFreeSize
- _OBJC_CLASS_$_TRIProject
- _OBJC_CLASS_$_UAFAssetUtilities
- _OBJC_CLASS_$_UAFAssetUtilitiesService
- _OBJC_CLASS_$_UAFAutoAssetInstance
- _OBJC_CLASS_$_UAFStagingLogManager
- _OBJC_IVAR_$_UAFAssetSetConfiguration._usageLimits
- _OBJC_IVAR_$_UAFAssetUtilities._assetAvailableCheckTimeout
- _OBJC_IVAR_$_UAFAssetUtilities._assetStatus
- _OBJC_IVAR_$_UAFAssetUtilities._assistantEnabled
- _OBJC_IVAR_$_UAFAssetUtilities._assistantGroup
- _OBJC_IVAR_$_UAFAssetUtilities._assistantQueue
- _OBJC_IVAR_$_UAFAssetUtilities._assistantUODStatus
- _OBJC_IVAR_$_UAFAssetUtilities._autoRetryDelayOnFailure
- _OBJC_IVAR_$_UAFAssetUtilities._autoRetryDelayOnFailureIncrement
- _OBJC_IVAR_$_UAFAssetUtilities._autoRetryDelayOnSettingsChanged
- _OBJC_IVAR_$_UAFAssetUtilities._autoRetryEnabled
- _OBJC_IVAR_$_UAFAssetUtilities._autoRetryLimit
- _OBJC_IVAR_$_UAFAssetUtilities._delegate
- _OBJC_IVAR_$_UAFAssetUtilities._delegateQueue
- _OBJC_IVAR_$_UAFAssetUtilities._downloadQueue
- _OBJC_IVAR_$_UAFAssetUtilities._networkExpensive
- _OBJC_IVAR_$_UAFAssetUtilities._networkSatisfied
- _OBJC_IVAR_$_UAFAssetUtilities._observerOptions
- _OBJC_IVAR_$_UAFAssetUtilities._pathEvaluator
- _OBJC_IVAR_$_UAFAssetUtilities._retryState
- _OBJC_IVAR_$_UAFAssetUtilities._showHybridAsUnsupported
- _OBJC_IVAR_$_UAFAssetUtilities._siriLanguage
- _OBJC_IVAR_$_UAFAssetUtilities._statusQueue
- _OBJC_IVAR_$_UAFAssetUtilities._understandingOnDeviceAssetsAvailable
- _OBJC_IVAR_$_UAFAssetUtilitiesService._assetStatus
- _OBJC_IVAR_$_UAFAssetUtilitiesService._completionWatchdogInProgress
- _OBJC_IVAR_$_UAFAssetUtilitiesService._dictationStatus
- _OBJC_IVAR_$_UAFAssetUtilitiesService._downloadQueue
- _OBJC_IVAR_$_UAFAssetUtilitiesService._observerEnabled
- _OBJC_IVAR_$_UAFAssetUtilitiesService._queuesArePaused
- _OBJC_IVAR_$_UAFAssetUtilitiesService._retryCount
- _OBJC_IVAR_$_UAFAssetUtilitiesService._siriLanguage
- _OBJC_IVAR_$_UAFAssetUtilitiesService._statusGroup
- _OBJC_IVAR_$_UAFAssetUtilitiesService._statusQueue
- _OBJC_IVAR_$_UAFAssetUtilitiesService._uodAvailable
- _OBJC_IVAR_$_UAFXPCService._assetUtilitiesService
- _OBJC_IVAR_$_UAFXPCService._assistantCapabilitiesChangeToken
- _OBJC_IVAR_$_UAFXPCService._assistantEnabled
- _OBJC_IVAR_$_UAFXPCService._assistantLangChangeToken
- _OBJC_IVAR_$_UAFXPCService._assistantLanguage
- _OBJC_IVAR_$_UAFXPCService._assistantMode
- _OBJC_IVAR_$_UAFXPCService._assistantPrefChangeToken
- _OBJC_IVAR_$_UAFXPCService._dictationEnabled
- _OBJC_IVAR_$_UAFXPCService._gmsAvailabilityToken
- _OBJC_IVAR_$_UAFXPCService._gmsEnabled
- _OBJC_IVAR_$_UAFXPCService._platformAssetSetObserver
- _OBJC_IVAR_$_UAFXPCService._subscriptionService
- _OBJC_IVAR_$_UAFXPCService._systemLangChangeToken
- _OBJC_IVAR_$_UAFXPCService._systemLanguage
- _OBJC_METACLASS_$_UAFAssetUtilities
- _OBJC_METACLASS_$_UAFAssetUtilitiesService
- _OBJC_METACLASS_$_UAFAutoAssetInstance
- _OBJC_METACLASS_$_UAFStagingLogManager
- _TRIProject_ProjectId_IsValidValue
- __AFLanguageDidChangeCallback
- __AFPreferencesDidChangeCallback
- __OBJC_$_CLASS_METHODS_UAFAutoAssetInstance
- __OBJC_$_CLASS_METHODS_UAFStagingLogManager
- __OBJC_$_CLASS_PROP_LIST_UAFAssetSetStatus
- __OBJC_$_INSTANCE_METHODS_UAFAssetUtilities
- __OBJC_$_INSTANCE_METHODS_UAFAssetUtilitiesService
- __OBJC_$_INSTANCE_VARIABLES_UAFAssetUtilities
- __OBJC_$_INSTANCE_VARIABLES_UAFAssetUtilitiesService
- __OBJC_$_PROP_LIST_UAFAssetUtilities
- __OBJC_$_PROP_LIST_UAFAssetUtilitiesService
- __OBJC_CLASS_RO_$_UAFAssetUtilities
- __OBJC_CLASS_RO_$_UAFAssetUtilitiesService
- __OBJC_CLASS_RO_$_UAFAutoAssetInstance
- __OBJC_CLASS_RO_$_UAFStagingLogManager
- __OBJC_METACLASS_RO_$_UAFAssetUtilities
- __OBJC_METACLASS_RO_$_UAFAssetUtilitiesService
- __OBJC_METACLASS_RO_$_UAFAutoAssetInstance
- __OBJC_METACLASS_RO_$_UAFStagingLogManager
- __SiriXAssetDidChangeCallback
- __UAFAssetStatusDidChangeCallback
- ___101+[UAFAssetSetManager unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.375
- ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.409
- ___102+[UAFManagedSubscriptions manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:]_block_invoke.410
- ___105+[UAFManagedSubscriptions manageAssistantSubscription:withMode:subscriber:subscriptionName:shouldReport:]_block_invoke
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.505
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.506
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.516
- ___129+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:]_block_invoke.517
- ___27-[UAFXPCService runUpdates]_block_invoke.416
- ___27-[UAFXPCService runUpdates]_block_invoke.419
- ___27-[UAFXPCService runUpdates]_block_invoke_2
- ___29+[UAFUserManager removeUser:]_block_invoke.341
- ___31-[UAFXPCConnection _connection]_block_invoke.338
- ___32-[UAFAssetUtilities assetStatus]_block_invoke
- ___32-[UAFXPCService _startObservers]_block_invoke
- ___32-[UAFXPCService _startObservers]_block_invoke_2
- ___32-[UAFXPCService _startObservers]_block_invoke_3
- ___32-[UAFXPCService _startObservers]_block_invoke_4
- ___32-[UAFXPCService _startObservers]_block_invoke_5
- ___33-[UAFAssetUtilities siriLanguage]_block_invoke
- ___36+[UAFUserManager performUserCleanup]_block_invoke.350
- ___36+[UAFUserManager performUserCleanup]_block_invoke.352
- ___36+[UAFUserManager performUserCleanup]_block_invoke.356
- ___36+[UAFUserManager performUserCleanup]_block_invoke.357
- ___36+[UAFUserManager performUserCleanup]_block_invoke.358
- ___37-[UAFAssetUtilities assistantEnabled]_block_invoke
- ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke
- ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke.357
- ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke_2
- ___37-[UAFXPCService expireSubscriptions:]_block_invoke
- ___38+[UAFStagingLogManager getSerialQueue]_block_invoke
- ___38-[UAFXPCConnection downloadSiriAssets]_block_invoke
- ___38-[UAFXPCConnection downloadSiriAssets]_block_invoke_2
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.463
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.465
- ___39-[UAFAssetUtilities assistantUODStatus]_block_invoke
- ___39-[UAFAssetUtilities currentAssetStatus]_block_invoke
- ___39-[UAFAssetUtilities downloadSiriAssets]_block_invoke
- ___39-[UAFAssetUtilitiesService getLanguage]_block_invoke
- ___40-[UAFXPCConnection expireSubscriptions:]_block_invoke.346
- ___41-[UAFXPCService _updateShadowSiriLocale:]_block_invoke
- ___41-[UAFXPCService _updateShadowSiriLocale:]_block_invoke.477
- ___42-[UAFXPCConnection diagnosticInformation:]_block_invoke.341
- ___43+[UAFAssetSetManager getSystemUsageAssets:]_block_invoke.399
- ___43-[UAFAssetUtilitiesService switchLanguage:]_block_invoke
- ___45-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke
- ___45-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke.384
- ___45-[UAFAssetUtilities _downloadSiriAssetsRetry]_block_invoke
- ___45-[UAFAssetUtilitiesService checkAssetStatus:]_block_invoke
- ___45-[UAFAutoAssetSet mapAsset:queue:completion:]_block_invoke.382
- ___46-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke
- ___46-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke.376
- ___46-[UAFXPCService markAssetsExpired:completion:]_block_invoke
- ___47-[UAFAssetUtilities downloadSiriAssetsIfNeeded]_block_invoke
- ___47-[UAFAssetUtilities downloadSiriAssetsIfNeeded]_block_invoke_2
- ___47-[UAFAssetUtilities downloadSiriAssetsIfNeeded]_block_invoke_3
- ___47-[UAFAssetUtilities refreshUAFAssetStatusAsync]_block_invoke
- ___47-[UAFAssetUtilities refreshUAFAssetStatusAsync]_block_invoke_2
- ___47-[UAFAssetUtilities refreshUAFAssetStatusAsync]_block_invoke_3
- ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke
- ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke.340
- ___48-[UAFAssetUtilities _assistantPreferencesUpdate]_block_invoke
- ___48-[UAFAssetUtilities _assistantPreferencesUpdate]_block_invoke.389
- ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.451
- ___48-[UAFXPCService operationWithConfig:completion:]_block_invoke.453
- ___49-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke.344
- ___49-[UAFXPCConnection postAssetNotificationIfNeeded]_block_invoke
- ___49-[UAFXPCConnection postAssetNotificationIfNeeded]_block_invoke_2
- ___50-[UAFAssetUtilities _downloadSiriAssetsWithDelay:]_block_invoke
- ___50-[UAFAutoAssetSet invalidateWithQueue:completion:]_block_invoke.362
- ___50-[UAFXPCConnection downloadSiriAssetsOverCellular]_block_invoke
- ___50-[UAFXPCConnection downloadSiriAssetsOverCellular]_block_invoke_2
- ___51-[UAFAssetUtilities downloadSiriAssetsOverCellular]_block_invoke
- ___51-[UAFXPCConnection operationWithConfig:completion:]_block_invoke.340
- ___52+[UAFAutoAssetManager removeDeprecatedAutoAssetSets]_block_invoke.491
- ___53+[UAFManagedSubscriptions managePlatformSubscription]_block_invoke
- ___53+[UAFManagedSubscriptions managePlatformSubscription]_block_invoke_2
- ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.389
- ___53-[UAFAssetSetConsistencyToken invalidate:completion:]_block_invoke.390
- ___53-[UAFAssetUtilities _downloadSiriAssetsOverCellular:]_block_invoke
- ___53-[UAFAssetUtilities _downloadSiriAssetsOverCellular:]_block_invoke.379
- ___55-[UAFAssetUtilities _triggerDelegateAssetStatusUpdated]_block_invoke
- ___55-[UAFXPCConnection downloadDictationAssetsForLanguage:]_block_invoke
- ___55-[UAFXPCConnection downloadDictationAssetsForLanguage:]_block_invoke_2
- ___57+[UAFAutoAssetManager lockLatestAssetSet:atomicInstance:]_block_invoke.449
- ___57+[UAFUserManager updateLastSeenForUser:queue:completion:]_block_invoke.337
- ___57-[UAFAssetUtilities understandingOnDeviceAssetsAvailable]_block_invoke
- ___58+[UAFStagingLogManager rollStagingLogsUponNewBuildVersion]_block_invoke
- ___60+[UAFAutoAssetManager observeAssetSetExperimentalNamespace:]_block_invoke.473
- ___60-[UAFAssetUtilitiesService _downloadSiriAssetsWithCellular:]_block_invoke
- ___61-[UAFXPCConnection subscriptions:subscriber:user:completion:]_block_invoke.347
- ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke
- ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke.365
- ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke_2
- ___62-[UAFAssetUtilities assetsAreAvailableForLanguage:completion:]_block_invoke
- ___62-[UAFXPCConnection postDictationAssetNotificationForLanguage:]_block_invoke
- ___62-[UAFXPCConnection postDictationAssetNotificationForLanguage:]_block_invoke_2
- ___63-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke
- ___63-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke.361
- ___63-[UAFAssetUtilitiesService downloadDictationAssetsForLanguage:]_block_invoke
- ___63-[UAFAssetUtilitiesService updateAssetState:value:forLanguage:]_block_invoke
- ___64+[UAFManagedSubscriptions _deviceSupportsGenerativeModelSystems]_block_invoke
- ___65+[UAFStagingLogManager deleteLoggedTargetsForEliminatedAssetSet:]_block_invoke
- ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke.358
- ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke_2
- ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke_3
- ___65-[UAFAutoAssetSet loadAutoAssets:experiment:experimentActivated:]_block_invoke_4
- ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke
- ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke.380
- ___66-[UAFAssetUtilitiesService updateSiriAssetAvailabilityForObserver]_block_invoke
- ___67-[UAFAssetUtilitiesService updateSiriAssetAvailabilityForLanguage:]_block_invoke
- ___67-[UAFXPCService setSystemConfigurationForKey:withValue:completion:]_block_invoke
- ___68-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke.466
- ___68-[UAFAssetUtilities getDiskSpaceNeededInBytesForLanguage:forClient:]_block_invoke
- ___68-[UAFXPCService lockLatestAtomicInstance:atomicInstance:completion:]_block_invoke.462
- ___69-[UAFAssetUtilities refreshUnderstandingOnDeviceAssetsAvailableAsync]_block_invoke
- ___70-[UAFXPCConnection setSystemConfigurationForKey:withValue:completion:]_block_invoke.345
- ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke.348
- ___71+[UAFAssetSetSubscriptionManager migrateSubscriptions:user:completion:]_block_invoke_2.349
- ___71-[UAFAssetUtilitiesService updateSiriAssetAvailabilityForLanguageSync:]_block_invoke
- ___71-[UAFAssetUtilitiesService updateSiriAssetAvailabilityForLanguageSync:]_block_invoke_2
- ___71-[UAFXPCConnection lockLatestAtomicInstance:atomicInstance:completion:]_block_invoke.343
- ___72+[UAFAssetSetManager isSubscriptionExpirationIgnorable:subscriber:user:]_block_invoke
- ___75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke
- ___75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke.359
- ___75-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke_2
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.365
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.376
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.378
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke_2
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke_2.379
- ___77+[UAFStagingLogManager logTargets:withAssetSetName:withPlatformAssetVersion:]_block_invoke
- ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke
- ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke.348
- ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke_2
- ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke_3
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.451
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.458
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.459
- ___82-[UAFAssetSetManager subscribe:subscriptions:user:userInitiated:queue:completion:]_block_invoke.460
- ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.484
- ___88-[UAFAssetSetManager unsubscribe:subscriptionNames:user:userInitiated:queue:completion:]_block_invoke.461
- ___90+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke.486
- ___97+[UAFAutoAssetManager getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:]_block_invoke.518
- ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.366
- ___99+[UAFAssetSetManager subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:]_block_invoke.370
- ___AssistantServicesLibraryCore_block_invoke
- ___GenerativeModelsLibraryCore_block_invoke
- ___MorphunAssetsLibraryCore_block_invoke
- ____RegisterPeriodicUAFSubscriptionActivity_block_invoke.367
- ____RegisterXPCActivity_block_invoke.348
- ___block_descriptor_32_e17_v16?0"NSError"8l
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32bs_e36_v24?0"UAFAssetStatus"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_40_e8_32w_e30_v16?0"NSObject<OS_nw_path>"8lw32l8
- ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
- ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSNumber"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40r_e25_v32?0"NSString"8Q16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e41_v32?0"NSString"8"NSMutableArray"16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s40w_e11_v24?0d8Q16lw40l8s32l8
- ___block_descriptor_48_e8_32s40w_e36_v24?0"UAFAssetStatus"8"NSError"16lw40l8s32l8
- ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_56_e8_32r40w_e5_v8?0lw40l8r32l8
- ___block_descriptor_56_e8_32s40r48r_e30_v24?0"NSNumber"8"NSError"16lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40s48r_e40_v32?0"UAFAssetSetSubscription"8Q16^B24ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56w_e22_v16?0"NSDictionary"8ls32l8w56l8s40l8s48l8
- ___block_descriptor_73_e8_32s40s48s56bs64w_e22_v16?0"NSDictionary"8ls32l8w64l8s56l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.337
- ___block_literal_global.350
- ___block_literal_global.352
- ___block_literal_global.354
- ___block_literal_global.356
- ___block_literal_global.357
- ___block_literal_global.366
- ___block_literal_global.368
- ___block_literal_global.371
- ___block_literal_global.373
- ___block_literal_global.385
- ___block_literal_global.416
- ___block_literal_global.418
- ___block_literal_global.421
- ___block_literal_global.429
- ___block_literal_global.433
- ___block_literal_global.447
- ___block_literal_global.469
- ___block_literal_global.472
- ___block_literal_global.490
- ___block_literal_global.494
- ___block_literal_global.534
- ___block_literal_global.537
- ___getAFDeviceSupportsSiriUODSymbolLoc_block_invoke
- ___getAFLanguageCodeDidChangeDarwinNotificationSymbolLoc_block_invoke
- ___getAFOfflineDictationStatusHighQualityKeySymbolLoc_block_invoke
- ___getAFOfflineDictationStatusInstalledKeySymbolLoc_block_invoke
- ___getAFPreferencesClass_block_invoke
- ___getAFSettingsConnectionClass_block_invoke
- ___getAFShouldRunAsrOnServerForUODSymbolLoc_block_invoke
- ___getAFSiriAvailabilityClass_block_invoke
- ___getAFSiriXAssetDidChangeDarwinNotificationSymbolLoc_block_invoke
- ___getAFUODStatusSupportedFullSymbolLoc_block_invoke
- ___getAFUODStatusSupportedHybridSymbolLoc_block_invoke
- ___getGMAvailabilityWrapperClass_block_invoke
- ___getMorphunAssetsClass_block_invoke
- ___getNSStringFromAFSiriOrchestrationModeSymbolLoc_block_invoke
- ___getkAFPreferencesDidChangeDarwinNotificationSymbolLoc_block_invoke
- ___getkAFSiriCapabilitiesDidChangeNotificationSymbolLoc_block_invoke
- __sl_dlopen
- _abort_report_np
- _audit_stringAssistantServices
- _audit_stringGenerativeModels
- _audit_stringMorphunAssets
- _dispatch_after
- _dispatch_assert_queue_not$V2
- _dispatch_group_async
- _dispatch_resume
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dispatch_suspend
- _dispatch_time
- _dlerror
- _dlsym
- _getAFDeviceSupportsSiriUODSymbolLoc.ptr
- _getAFLanguageCodeDidChangeDarwinNotification
- _getAFLanguageCodeDidChangeDarwinNotificationSymbolLoc.ptr
- _getAFPreferencesClass
- _getAFPreferencesClass.softClass
- _getAFSettingsConnectionClass.softClass
- _getAFShouldRunAsrOnServerForUODSymbolLoc.ptr
- _getAFSiriAvailabilityClass.softClass
- _getAFSiriXAssetDidChangeDarwinNotification
- _getAFSiriXAssetDidChangeDarwinNotificationSymbolLoc.ptr
- _getAFUODStatusSupportedFullSymbolLoc.ptr
- _getAFUODStatusSupportedHybridSymbolLoc.ptr
- _getMorphunAssetsClass
- _getNSStringFromAFSiriOrchestrationModeSymbolLoc.ptr
- _getkAFPreferencesDidChangeDarwinNotification
- _getkAFPreferencesDidChangeDarwinNotificationSymbolLoc.ptr
- _kUAFAssistantAssistantEngineLanguageUsageAlias
- _kUAFAssistantHybridLanguageUsageAlias
- _kUAFAssistantLanguageUsageAlias
- _kUAFAssistantLegacyLanguageUsageAlias
- _kUAFBuildVersion
- _kUAFConfNoRemove
- _kUAFGMSSiriSubscriber
- _kUAFGMSSiriSubscription
- _kUAFInstanceExtension
- _kUAFJSONExtension
- _kUAFLastBuildVersionFilename
- _kUAFLastStagingLogsFromLastBuild
- _kUAFLatestStagingLogs
- _kUAFMaxUsageValues
- _kUAFMorphunAssetSet
- _kUAFMorphunFactorPrefix
- _kUAFMorphunLanguageUsageType
- _kUAFMorphunSubscriber
- _kUAFMorphunSystemLocaleSubscription
- _kUAFNLSubscriber
- _kUAFNLSystemLanguageSubscription
- _kUAFNLSystemLanguageUsageAlias
- _kUAFRootStagingLogsDir
- _kUAFSummarizationKitAssetSet
- _kUAFSummarizationKitSubscriber
- _kUAFSummarizationKitSubscription
- _kUAFUsageLimits
- _kUAFValidationAssetSet
- _kUAFValidationSubscriber
- _kUAFValidationSubscription
- _nw_path_create_default_evaluator
- _nw_path_evaluator_cancel
- _nw_path_evaluator_copy_path
- _nw_path_evaluator_set_update_handler
- _nw_path_get_status
- _nw_path_is_expensive
- _objc_getClass
- _objc_msgSend$_assistantCapabilitiesUpdate
- _objc_msgSend$_assistantEnabledChanged
- _objc_msgSend$_assistantGMSAvailabilityUpdate
- _objc_msgSend$_assistantLanguageChanged
- _objc_msgSend$_assistantLanguageUpdate
- _objc_msgSend$_assistantModeChanged
- _objc_msgSend$_assistantPreferencesUpdate
- _objc_msgSend$_assistantUpdate
- _objc_msgSend$_assistantUsageAliasForMode:
- _objc_msgSend$_checkFreeSpaceNeededForLanguage:forClient:
- _objc_msgSend$_checkFreeSpaceNeededForLanguage:isDictation:
- _objc_msgSend$_createConnection
- _objc_msgSend$_deviceSupportsGenerativeModelSystems
- _objc_msgSend$_dictationEnabledChanged
- _objc_msgSend$_downloadDictationAssetsForLanguage:useCellular:
- _objc_msgSend$_downloadSiriAssetsOverCellular:
- _objc_msgSend$_downloadSiriAssetsRetry
- _objc_msgSend$_downloadSiriAssetsWithCellular:
- _objc_msgSend$_downloadSiriAssetsWithDelay:
- _objc_msgSend$_downloadUnderstandingAssetsForLanguage:useCellular:
- _objc_msgSend$_getBiomeAssetSetStatus:atomicInstanceMetadata:entries:errorCodes:
- _objc_msgSend$_getBiomeStreamForAssetSetStatus:atomicInstanceMetadata:entries:errorCodes:assetSetDailyStatusEventType:
- _objc_msgSend$_getBiomeUAFAssetSet:atomicInstanceMetadata:entries:errorCodes:
- _objc_msgSend$_getDiskSpaceNeededInBytesForLanguage:isDictation:error:
- _objc_msgSend$_getMADownloadErrors:newerVersionError:assetSetName:assetSetID:
- _objc_msgSend$_gmsEnabledChanged
- _objc_msgSend$_handleDictationCompletionForLanguage:
- _objc_msgSend$_handleDictationProgress:status:language:
- _objc_msgSend$_handleNetworkPathUpdate:
- _objc_msgSend$_handleUpdateProgress:status:language:
- _objc_msgSend$_isLegacySiriDevice
- _objc_msgSend$_isUsageLimitExceeded:
- _objc_msgSend$_networkIsExpensiveForPath:
- _objc_msgSend$_networkIsSatisfiedForPath:
- _objc_msgSend$_postAssetStateChangedNotification
- _objc_msgSend$_siriDownloadCompleteForLanguage:
- _objc_msgSend$_stageAssetsUponPlatformAssetSetUpdate
- _objc_msgSend$_startObservers
- _objc_msgSend$_stopObserver
- _objc_msgSend$_stopObservers
- _objc_msgSend$_subscriptionDiffersFromDB:subscriber:user:expirationOnlyCount:error:
- _objc_msgSend$_systemLanguageChanged
- _objc_msgSend$_systemLanguageUpdate
- _objc_msgSend$_triggerCompletionTimerForLanguage:
- _objc_msgSend$_triggerDelegateAssetStatusUpdated
- _objc_msgSend$_updateAssetState:value:forLanguage:
- _objc_msgSend$_updateAssetUtilitiesLanguage
- _objc_msgSend$_updateAssistantSubscription
- _objc_msgSend$_updateDelegateForUODAvailable:uodStatus:
- _objc_msgSend$_updateDictationAvailabilityForLanguage:
- _objc_msgSend$_updateDictationProgress:language:
- _objc_msgSend$_updateDictationState:value:forLanguage:
- _objc_msgSend$_updateGMSSiriLanguageSubscription
- _objc_msgSend$_updateMorphunSystemLanguageSubscription
- _objc_msgSend$_updateNLSystemLanguageSubscription
- _objc_msgSend$_updateProgress:forLanguage:
- _objc_msgSend$_updateShadowSiriLocale:
- _objc_msgSend$_updateShadowSiriLocaleIfNeeded
- _objc_msgSend$_updateSiriAssetAvailability:forLanguage:
- _objc_msgSend$_usageCountForUsageType:usingUsages:
- _objc_msgSend$assetAvailableCheckTimeout
- _objc_msgSend$assetNamed:
- _objc_msgSend$assetSetIdForSELF:assetSetOrigin:
- _objc_msgSend$assetStatus
- _objc_msgSend$assetsAreAvailableForLanguage:completion:
- _objc_msgSend$assistantEnabledDidChange:
- _objc_msgSend$assistantGroup
- _objc_msgSend$assistantIsEnabled
- _objc_msgSend$assistantLanguageDidChange:
- _objc_msgSend$assistantModeDescription:
- _objc_msgSend$assistantQueue
- _objc_msgSend$attributesOfFileSystemForPath:error:
- _objc_msgSend$autoRetryDelayOnFailure
- _objc_msgSend$autoRetryDelayOnFailureIncrement
- _objc_msgSend$autoRetryDelayOnSettingsChanged
- _objc_msgSend$autoRetryEnabled
- _objc_msgSend$autoRetryLimit
- _objc_msgSend$bestSupportedLanguageCodeForLanguageCode:
- _objc_msgSend$bestSupportedSiriLanguage
- _objc_msgSend$cancelled
- _objc_msgSend$checkAssetStatus:
- _objc_msgSend$clear:path:
- _objc_msgSend$clientWithIdentifier:
- _objc_msgSend$configurationManagers:
- _objc_msgSend$countryCode
- _objc_msgSend$createBuildVersionFile
- _objc_msgSend$createLogEntryWithInfo:
- _objc_msgSend$currentAssistantLanguage
- _objc_msgSend$currentAssistantMode
- _objc_msgSend$decomposeSaveFileURL:assetSetName:atomicInstance:
- _objc_msgSend$delegate
- _objc_msgSend$delegateQueue
- _objc_msgSend$deleteItemAtURL:error:
- _objc_msgSend$deleteLoggedTargetsForEliminatedAssetSet:
- _objc_msgSend$desiredOrchestrationMode
- _objc_msgSend$deviceSupportAndUseHybridASR
- _objc_msgSend$deviceSupportFullUOD
- _objc_msgSend$dictationAvailableForLanguage:
- _objc_msgSend$dictationIsEnabled
- _objc_msgSend$dictationStatus
- _objc_msgSend$diskSpaceNeededForSubscriber:subscriptionName:error:
- _objc_msgSend$diskSpaceNeededInBytesForLanguage:forClient:completion:
- _objc_msgSend$downloadDictationAssetsForLanguage:
- _objc_msgSend$downloadQueue
- _objc_msgSend$downloadSiriAssets
- _objc_msgSend$downloadSiriAssetsOverCellular
- _objc_msgSend$experimentIdentifiersTrialClient:trialNamespace:
- _objc_msgSend$findDiffBetweenOldAssetSetUsages:newAssetSetUsages:knownAssetSets:usedAssetSets:configurationManager:
- _objc_msgSend$findOrCreateDir:
- _objc_msgSend$fromPreferences
- _objc_msgSend$getAssetStatusForLanguage:completionHandler:
- _objc_msgSend$getAssistantLanguageIfAvailableSync
- _objc_msgSend$getBuildVersionFromStagingLogsDir
- _objc_msgSend$getDiskSpaceNeededInBytesForLanguage:forClient:
- _objc_msgSend$getFactorNameForLocale:
- _objc_msgSend$getFreeDiskSpaceInBytes
- _objc_msgSend$getFreeDiskSpaceNeededInBytes:
- _objc_msgSend$getLanguage
- _objc_msgSend$getLastBuildStagingLogsDir
- _objc_msgSend$getLatestStagingLogsDir
- _objc_msgSend$getLogFileForTarget:andAssetSetName:
- _objc_msgSend$getRootStagingLogsDir
- _objc_msgSend$getSubscriptions:storeManager:
- _objc_msgSend$gmsWantsAssets
- _objc_msgSend$handleAssetStatusUpdated
- _objc_msgSend$initWithCapacity:
- _objc_msgSend$initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:
- _objc_msgSend$initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:bootUUID:experimentActivated:
- _objc_msgSend$initWithUserService
- _objc_msgSend$instanceDirURL
- _objc_msgSend$isAssistantEnabled
- _objc_msgSend$isDictationEnabled
- _objc_msgSend$isEqualToNumber:
- _objc_msgSend$isFullUODSupportedForStatus:language:
- _objc_msgSend$isHybridUODSupportedForStatus:language:
- _objc_msgSend$isLocaleDownloadSupported:
- _objc_msgSend$isLocaleEmbedded:
- _objc_msgSend$isOkayToHaveAsset
- _objc_msgSend$isOnDemandAssetSubscriptionAllowed
- _objc_msgSend$isSubscriptionExpirationIgnorable:subscriber:user:
- _objc_msgSend$isUsageLimitExceeded:
- _objc_msgSend$localeWithLocaleIdentifier:
- _objc_msgSend$logAlterFromAtomicInstance:sourceType:alterSetData:
- _objc_msgSend$logDownloadTriggerEventWithLanguage:hasExistingAssets:retryCount:
- _objc_msgSend$logSiriSubscription:subscriber:subscription:userId:locale:mode:unsubscribed:
- _objc_msgSend$logTargetSync:withAssetSetName:withPlatformAssetVersion:
- _objc_msgSend$logTargets:withAssetSetName:withPlatformAssetVersion:
- _objc_msgSend$manageAssistantSubscription:withMode:
- _objc_msgSend$manageAssistantSubscription:withMode:subscriber:subscriptionName:shouldReport:
- _objc_msgSend$manageGMSSiriLanguageSubscription:language:mode:
- _objc_msgSend$manageMorphunSystemLocaleSubscription:
- _objc_msgSend$manageNLSystemLanguageSubscription:
- _objc_msgSend$manageNLSystemLanguageSubscription:subscriber:subscriptionName:
- _objc_msgSend$managePlatformSubscription
- _objc_msgSend$manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:
- _objc_msgSend$manageSummarizationKitSubscription
- _objc_msgSend$mockAssetStatus
- _objc_msgSend$morphunUsagesForLocale:
- _objc_msgSend$moveItemAtURL:toURL:
- _objc_msgSend$moveItemAtURL:toURL:error:
- _objc_msgSend$networkPathChangeSatisfied:isExpensive:
- _objc_msgSend$observeAllAssetSets
- _objc_msgSend$observeAssetSet:queue:handler:
- _objc_msgSend$offlineDictationStatus
- _objc_msgSend$pending
- _objc_msgSend$platformAssetVersion:
- _objc_msgSend$postAssetNotificationIfNeeded
- _objc_msgSend$postDictationAssetNotificationForLanguage:
- _objc_msgSend$preferredLanguages
- _objc_msgSend$projectIdFromName:
- _objc_msgSend$rangeOfString:options:
- _objc_msgSend$refreshUAFAssetStatusAsync
- _objc_msgSend$refreshUnderstandingOnDeviceAssetsAvailableAsync
- _objc_msgSend$removeObserver:
- _objc_msgSend$removeUnusedAutoAssetSets:usedAutoAssetSets:
- _objc_msgSend$retryCount
- _objc_msgSend$retryState
- _objc_msgSend$rollStagingLogsUponNewBuildVersion
- _objc_msgSend$serializeJSONObjectToData:
- _objc_msgSend$setAssetStatus:
- _objc_msgSend$setAssistantEnabled:
- _objc_msgSend$setAssistantUODStatus:
- _objc_msgSend$setCancelled:
- _objc_msgSend$setPending:
- _objc_msgSend$setRetryState:
- _objc_msgSend$setSiriLanguage:
- _objc_msgSend$setUnderstandingOnDeviceAssetsAvailable:
- _objc_msgSend$setUodAvailable:
- _objc_msgSend$setWithObject:
- _objc_msgSend$sharedPreferences
- _objc_msgSend$showHybridAsUnsupported
- _objc_msgSend$siriUODAvailabilityDidChange:
- _objc_msgSend$siriUODStatusDidChange
- _objc_msgSend$stageAssetSet:targets:platformAssetVersion:
- _objc_msgSend$stageAssetsWithNewSubscriptions:oldSubscriptions:autoAssetSets:
- _objc_msgSend$startObserver
- _objc_msgSend$startObserversWithOptions:
- _objc_msgSend$state
- _objc_msgSend$statusGroup
- _objc_msgSend$statusQueue
- _objc_msgSend$stringFromUAFAssetState:
- _objc_msgSend$subscribe:subscriptions:queue:completion:
- _objc_msgSend$switchLanguage:
- _objc_msgSend$systemLanguage
- _objc_msgSend$targetForAssetSet:specifiers:version:autoAssetSets:
- _objc_msgSend$trialClientWithProject:
- _objc_msgSend$understandingOnDeviceAssetsAvailable
- _objc_msgSend$uodAvailable
- _objc_msgSend$updateAssetState:value:forLanguage:
- _objc_msgSend$updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:
- _objc_msgSend$updateLastSeenForCurrentUserOnQueue:completion:
- _objc_msgSend$updateSiriAssetAvailabilityForLanguage:
- _objc_msgSend$updateSiriAssetAvailabilityForLanguageSync:
- _objc_msgSend$updateSiriAssetAvailabilityForObserver
- _objc_msgSend$validateUsageAlias:usageAliasValue:
- _objc_msgSend$value
- _objc_msgSend$writeToFile:content:
- _objc_opt_respondsToSelector
- _swift_retain
CStrings:
+ "%02x"
+ "%@/%@/%@/%@.metadata.plist"
+ "%@|%@"
+ "%s %lu entries after filtering"
+ "%s %lu metadata keys, %lu specifiers, %lu onDiskKeys"
+ "%s %{public}@ Failed to unlock %{public}@ atomic instance %{public}@: %{public}@"
+ "%s %{public}@: Asset set initialized from Roots V2 for %{public}@ with %lu assets"
+ "%s %{public}@: Could not load asset set %{public}@ from Roots V2 as autoAssets is unexpectedly nil"
+ "%s %{public}@: Detected Roots V2 present for %{public}@, instance: %{public}@"
+ "%s %{public}@: Failed to initialize Roots V2 asset set for %{public}@: %{public}@"
+ "%s %{public}@: Failed to unlock %{public}@ atomic instance %{public}@ rapid lock while exiting asset info cache init: %{public}@"
+ "%s %{public}@: MA atomic instance %{public}@ for %{public}@ has been disabled by roots V2 transition"
+ "%s %{public}@: Unable to read atomic instance metadata for asset set: %{public}@ atomic instance %{public}@: %{public}@"
+ "%s %{public}@: Using Roots V2 instance %{public}@ from consistency token"
+ "%s %{public}@: asset set %{public}@, atomic instance %{public}@: failed to get cached atomic instance info, error: %{public}@"
+ "%s %{public}@: asset set %{public}@: failed to get latest atomic instance"
+ "%s %{public}@: created asset set %{public}@ atomic instance %{public}@ from asset info cache"
+ "%s %{public}@: failed to acquire a short term lock from the rapid lock for asset set %{public}@ atomic instance %{public}@, error: %{public}@"
+ "%s %{public}@: failed to get assets from asset info cache, skipping cache usage, error = %@"
+ "%s %{public}@: failed to get rapid lock on asset set name %{public}@, atomic instance %{public}@"
+ "%s %{public}@: skipping cache usage as we failed to initialize from the cache"
+ "%s Activating experiment %{public}@ with namespace %{public}@ asset set %{public}@"
+ "%s Activation of experiment %{public}@ in Namespace %{public}@ complete"
+ "%s Activation of experiment %{public}@ in Namespace %{public}@ failed: %{public}@"
+ "%s Asset %{public}@ (%{public}@) does not exist at %{public}@"
+ "%s Asset %{public}@ (%{public}@) is missing .metadata.plist at %{public}@: %{public}@"
+ "%s Asset location for %{public}@ (%{public}@): %{public}@"
+ "%s Asset set %{public}@ has no config, skipping"
+ "%s Auto asset set %{public}@ is not needed by current config and does not already exist.  Skipping."
+ "%s Biome unavailable for %{public}@, aborting"
+ "%s Cache management: cache expired for %{public}@, refreshing"
+ "%s Cache management: cache fresh for %{public}@, skipping refresh"
+ "%s Cache management: checkLocalDownloadSize error for %{public}@: %{public}@"
+ "%s Cache management: failed to init MAAutoAssetSet for %{public}@: %{public}@"
+ "%s Cache management: no cache for %{public}@, skipping refresh"
+ "%s Cache management: refresh failed for %{public}@: %{public}@"
+ "%s Cache management: refresh succeeded for %{public}@"
+ "%s Cache management: unknown MACacheTTL value %ld for %{public}@, skipping refresh"
+ "%s Calling completion with %lu entries"
+ "%s Calling completion with error: %{public}@"
+ "%s Calling subscription database access completion - granted=%d, error=%{public}@"
+ "%s Cannot empty legacy StagingLogs directory: empty storagePath"
+ "%s Cannot enumerate legacy StagingLogs directory at %{public}@"
+ "%s Cannot invalidate current Roots V2 instance %{public}@ for %{public}@"
+ "%s Closed Roots V2 lock file descriptor for %{public}@"
+ "%s Could not create asset set %{public}@ for staging: %{public}@"
+ "%s Could not create autoasset set for '%{public}@': %{public}@"
+ "%s Could not create os_transaction"
+ "%s Could not create trial client"
+ "%s Could not create url by appending '%{public}@' with '%{public}@'"
+ "%s Could not get configuration for asset set %{public}@"
+ "%s Could not get status for asset info cache of auto asset set %{public}@ atomic instance %{public}@, not writing cache entry: %{public}@"
+ "%s Could not get the status of auto asset set %{public}@ : %{public}@"
+ "%s Could not obtain sandbox extension for subscription database: %{public}@"
+ "%s Could not retrieve subscriptions for user '%@', subscriber '%{public}@': %{public}@"
+ "%s Could not update digest for asset set %{public}@ target '%{public}@'"
+ "%s Downloaded asset entry %{public}@ missing size metadata for key %{public}@, using full newer size"
+ "%s Emitted the Scheduled daily status"
+ "%s Emitting daily status scheduled event for asset set %{public}@"
+ "%s Emptied legacy StagingLogs directory at %{public}@ (removed %lu of %lu entries)"
+ "%s Experiment mismatch in Namespace %{public}@: %{public}@ != %{public}@"
+ "%s Extracted roots V2 instance ID %{public}@ from current symlink for %{public}@"
+ "%s Failed consuming subscription database sandbox extension"
+ "%s Failed to acquire exclusive lock on %{public}@: errno %d (%s)"
+ "%s Failed to create disabledByRootsV2 marker at %{public}@"
+ "%s Failed to delete Roots V2 lock file %{public}@: %{public}@"
+ "%s Failed to enumerate legacy StagingLogs directory at %{public}@: %{public}@"
+ "%s Failed to get current roots V2 instance ID for %{public}@"
+ "%s Failed to init MAAutoAssetSet for %{public}@: %{public}@"
+ "%s Failed to open and lock %{public}@: errno %d (%s)"
+ "%s Failed to remove disabledByRootsV2 marker %{public}@: %{public}@"
+ "%s Failed to remove disabledByRootsV2 marker for atomic instance %{public}@ in %{public}@: %{public}@"
+ "%s Failed to remove legacy StagingLogs entry %{public}@: %{public}@"
+ "%s Failed to write cache for asset set %{public}@ atomic instance %{public}@: %{public}@"
+ "%s Failing with error: %{public}@"
+ "%s Invalid token %{public}@"
+ "%s Keeping cache for rapid-locked atomic instance %{public}@ for asset set %{public}@"
+ "%s Keeping disabledByRootsV2 marker for %{public}@ in %{public}@ (locker exists and root installed)"
+ "%s Legacy StagingLogs directory already absent at %{public}@"
+ "%s Legacy StagingLogs directory already empty at %{public}@"
+ "%s Loaded %lu assets for asset set %{public}@ from roots V2"
+ "%s Loaded %lu assets for asset set %{public}@ from roots V2 (experiment activated: %{public}@)"
+ "%s MA Asset Origin Report asset source is unknown"
+ "%s MA Asset Origin Report missing Available OS Build"
+ "%s MA Asset Origin Report missing Downloaded OS Build"
+ "%s MA atomic instance %{public}@ for %{public}@ is still in use"
+ "%s MA locker file does not exist for %{public}@ %{public}@, no marker needed"
+ "%s Newer asset entry %{public}@ already downloaded, skipping for key %{public}@"
+ "%s Newer asset entry %{public}@ has diff size %llu for key %{public}@ (newer: %llu, downloaded: %llu)"
+ "%s Newer asset entry %{public}@ missing size metadata for key %{public}@"
+ "%s Newer asset entry %{public}@ needs no additional space for key %{public}@ (newer: %llu, downloaded: %llu)"
+ "%s No affected asset set usages after scoping"
+ "%s No asset set usages resolved"
+ "%s No config for asset set %{public}@ to manage experiment for"
+ "%s No experiment for asset set %{public}@"
+ "%s No experiment staged in trial Namespace %{public}@"
+ "%s No prestage subscriptions found at URL: %{public}@"
+ "%s No roots visible for %{public}@, but proceeding with disabledByRootsV2 marker"
+ "%s No staged level for factor %@"
+ "%s No valid cache for %{public}@ (TTL: %ld) and localOnly=YES, failing"
+ "%s No valid cache for %{public}@ (TTL: %ld), fetching from Pallas"
+ "%s Not aware of asset set and could not get auto asset set %{public}@ : %{public}@"
+ "%s Partially emptied legacy StagingLogs directory at %{public}@ (removed %lu of %lu visited entries before enumeration error)"
+ "%s Received request to disable MA atomic instance %{public}@ for roots V2 transition for %{public}@"
+ "%s Received request to invalidate Roots V2 instance %{public}@ for %{public}@"
+ "%s Released asset roots V2 lock for %{public}@"
+ "%s Removed disabledByRootsV2 marker for atomic instance %{public}@ in %{public}@"
+ "%s Removed incomplete cache entry %{public}@ for asset set %{public}@"
+ "%s Removed stale cache entry %{public}@ for asset set %{public}@"
+ "%s Removed stale disabledByRootsV2 marker %{public}@"
+ "%s Requesting MA atomic instance disable for roots V2 %{public}@ for %{public}@ via XPC"
+ "%s Requesting invalidation of Roots V2 instance %{public}@ for %{public}@ via XPC"
+ "%s Requesting subscription database access via XPC"
+ "%s Requesting subscription database access via XPC (sync)"
+ "%s Roots V2 instance %{public}@ for %{public}@ is still in use"
+ "%s Roots V2 lock file already deleted for %{public}@ %{public}@"
+ "%s Roots V2 present for %{public}@, skipping MA lock latest XPC"
+ "%s Sending Biome event for %{public}@ assetSet=%{public}@"
+ "%s Sending Biome event for assetSet=%{public}@"
+ "%s Sending first unlock notifications for asset set %{public}@ (root %{public}@)"
+ "%s Sending scheduled daily status Biome event"
+ "%s Set '%{public}@' is not configured and does not need staging"
+ "%s Skipped %lu entries missing numeric value for key %{public}@"
+ "%s Skipping %{public}@ (no config or autoAssetType)"
+ "%s Skipping %{public}@ (no specifiers)"
+ "%s Staging encountered an error: %{public}@"
+ "%s Subscription database access already allowed"
+ "%s Subscription database access already granted"
+ "%s Subscription database access request failed - %{public}@"
+ "%s Successfully consumed subscription database sandbox extension"
+ "%s Successfully disabled MA atomic instance %{public}@ for roots V2 transition for %{public}@"
+ "%s Successfully invalidated Roots V2 instance %{public}@ for %{public}@"
+ "%s Successfully locked Roots V2 %{public}@ for %{public}@"
+ "%s Token '%{public}@' Roots V2 invalidated successfully"
+ "%s Token '%{public}@' Roots V2 invalidation failed: %{public}@"
+ "%s Tokens equivalent, skipping set-targets"
+ "%s Unexpectedly couldn't retrieve subscription user '%@' subscriber '%{public}@' subscription: '%{public}@'"
+ "%s Using cached metadata for %{public}@ (TTL: %ld)"
+ "%s V1 versions of UAF Biome schemas unavailable, aborting"
+ "%s V2 versions of UAF Biome schemas unavailable, aborting "
+ "%s XPC disable of MA atomic instance %{public}@ for roots V2 %{public}@ failed: %{public}@"
+ "%s XPC disable of MA atomic instance %{public}@ for roots V2 %{public}@ succeeded"
+ "%s XPC invalidation of Roots V2 instance %{public}@ for %{public}@ failed: %{public}@"
+ "%s XPC invalidation of Roots V2 instance %{public}@ for %{public}@ succeeded"
+ "%s XPC: Unsubscribed platform asset: %{public}@"
+ "%s XPC: Unsubscribing platform asset"
+ "%s _getSubscriptionsAsDictionary requires both subscriber and user to be non-nil"
+ "%s assetSet=%{public}@ entryCount=%lu"
+ "%s assetSet=%{public}@ errorCodesCount=%lu"
+ "%s assetSet=%{public}@ eventType=%lu entryCount=%lu errorCount=%lu"
+ "%s assetSet=%{public}@ subscription=%{public}@ addedCount=%lu removedCount=%lu"
+ "%s checkDownloadSize failed for %{public}@: %{public}@"
+ "%s checkDownloadSize returned no metadata for %{public}@"
+ "%s checkLocalDownloadSize error for %{public}@ (falling back to Pallas): %{public}@"
+ "%s disableMAAtomicInstanceForRootsV2 %{public}@ for %{public}@ complete"
+ "%s disableMAAtomicInstanceForRootsV2 %{public}@ for %{public}@ failed with: %@"
+ "%s failed to archive atomic instance metadata for asset set %{public}@ atomic instance %{public}@: %{public}@"
+ "%s failed to archive metadata for asset set %{public}@ atomic instance %{public}@ specifier %{public}@: %{public}@"
+ "%s failed to create asset data symlink for asset set %{public}@ atomic instance %{public}@ specifier %{public}@: %{public}@"
+ "%s failed to create notReadyDir for asset set %{public}@ atomic instance %{public}@: %{public}@"
+ "%s failed to get metadata for asset set %{public}@ atomic instance %{public}@"
+ "%s failed to get metadata path for asset set %{public}@, atomic instance %{public}@, not removing it"
+ "%s failed to get metadata path for asset set %{public}@, atomic instance %{public}@, skipping removal"
+ "%s failed to get path for atomic instance metadata for asset set %{public}@ atomic instance %{public}@: %{public}@"
+ "%s failed to rename asset info cache dir for asset set %{public}@ atomic instance %{public}@ from %{public}@ to path %{public}@: %{public}@"
+ "%s failed to write atomic instance metadata for asset set %{public}@ atomic instance %{public}@ to path %{public}@: %{public}@"
+ "%s failed to write metadata plist for asset set %{public}@ atomic instance %{public}@ specifier %{public}@"
+ "%s filterMetadata for %{public}@: raw=%lu entries, filtered=%lu entries"
+ "%s getDefaultStoragePath returned nil, falling back to /private/var/db/assetsubscriptiond"
+ "%s including %{public}@|%{public}@ (newer than on-disk %{public}@)"
+ "%s including %{public}@|%{public}@ (not on disk)"
+ "%s invalidateRootsV2Instance %{public}@ for %{public}@ complete"
+ "%s invalidateRootsV2Instance %{public}@ for %{public}@ failed with: %@"
+ "%s issued extension"
+ "%s latestStatusForClients failed for %{public}@: %{public}@, assuming nothing on disk"
+ "%s nil assetSetName for %{public}@, aborting"
+ "%s no XPC connection"
+ "%s on-disk %{public}@|%{public}@"
+ "%s raw metadata keys: %{public}@"
+ "%s resolvedSpecifiers=%{public}@"
+ "%s sandbox extension failed"
+ "%s sandbox extension request for '%{public}@' completed with: %{public}@"
+ "%s sending Biome event for assetSet=%{public}@"
+ "%s sending Biome event for assetType=%{public}@"
+ "%s signature check failed"
+ "%s signature verification succeeded for: %{public}@"
+ "%s skipping %{public}@ (no separator)"
+ "%s skipping %{public}@ (not a dictionary)"
+ "%s skipping %{public}@|%{public}@ (older than on-disk %{public}@)"
+ "%s skipping %{public}@|%{public}@ (same version on disk)"
+ "%s skipping %{public}@|%{public}@ (specifier not resolved)"
+ "%s skipping specifier %{public}@ as no cache entry was found, error: %{public}@"
+ "%s starting scheduled daily status logging"
+ "%s unauthorized client: %{public}@"
+ "%s wrote asset info cache entry for asset set %{public}@ atomic instance %{public}@, cache entry dir is %{public}@"
+ ")"
+ "+[UAFAssetInfoCache getCachedAsset:specifier:atomicInstanceCachePath:experimentationEnabled:experimentId:error:]"
+ "+[UAFAssetInfoCache maintainCacheForAssetSet:latestAtomicInstance:]"
+ "+[UAFAssetInfoCache maintainCacheForAssetSet:latestAtomicInstance:]_block_invoke"
+ "+[UAFAssetInfoCache updateCacheIfNeeded:atomicEntries:atomicInstance:]"
+ "+[UAFAssetInfoCache writeCacheForAssetSet:atomicInstance:atomicEntries:atomicInstanceMetadata:error:]"
+ "+[UAFAssetSetManager _subscriptionDiffersFromDB:subscriber:user:expirationOnlyCount:storeSubscriptions:error:]"
+ "+[UAFAssetSetManager isSubscriptionExpirationIgnorable:subscriber:user:storeSubscriptions:]_block_invoke"
+ "+[UAFAssetSetSubscriptionManager getSubscriptionsAsDictionary:storeManager:]"
+ "+[UAFAssetSetSubscriptionManager subscriptions:subscriber:user:completion:]"
+ "+[UAFAutoAssetManager filterMetadata:specifiers:onDiskKeys:includeSpecifierKeys:]"
+ "+[UAFAutoAssetManager findDiffBetweenOldAssetSetUsages:newAssetSetUsages:configurationManager:]"
+ "+[UAFAutoAssetManager manageExperiment:config:consistencyToken:]"
+ "+[UAFAutoAssetManager manageExperimentFor:consistencyToken:]"
+ "+[UAFAutoAssetManager manageMetadataCacheForConfig:autoAssetSet:]"
+ "+[UAFAutoAssetManager manageMetadataCacheForConfig:autoAssetSet:]_block_invoke"
+ "+[UAFAutoAssetManager metadataForAssetSetUsages:configurationManager:expensiveNetworking:localOnly:includeSpecifierKeys:queue:completion:]"
+ "+[UAFAutoAssetManager metadataForAssetSetUsages:configurationManager:expensiveNetworking:localOnly:includeSpecifierKeys:queue:completion:]_block_invoke"
+ "+[UAFAutoAssetManager metadataForAssetSetUsages:configurationManager:expensiveNetworking:localOnly:includeSpecifierKeys:queue:completion:]_block_invoke_3"
+ "+[UAFAutoAssetManager requestSandboxExtension:queue:completion:]"
+ "+[UAFAutoAssetManager requestSandboxExtension:queue:completion:]_block_invoke_2"
+ "+[UAFAutoAssetManager stageAssetSet:targets:]"
+ "+[UAFAutoAssetManager stageAssetsWithConfigurationManager:version:token:]"
+ "+[UAFAutoAssetManager targetForAssetSet:specifiers:version:]"
+ "+[UAFBiomeInstrumenter _getBiomeUAFAssetSet:atomicInstanceMetadata:assetSetOriginReport:entries:errorCodes:]"
+ "+[UAFBiomeStreamWriter _constructBiomeAssetSet:storeManager:]"
+ "+[UAFBiomeStreamWriter _getAllAssetSets]_block_invoke"
+ "+[UAFBiomeStreamWriter _getBiomeUAFAssetSet:atomicInstanceMetadata:assetSetOriginReport:entries:errorCodes:]"
+ "+[UAFBiomeStreamWriter logAlterFromAtomicInstance:sourceType:configuredSpecifiers:addedAssets:removedAssets:]"
+ "+[UAFBiomeStreamWriter logAssetSetArrivedEvent:atomicInstanceMetadata:assetSetOriginReport:entries:]"
+ "+[UAFBiomeStreamWriter logAssetSetDownloadErrorEvent:atomicInstanceMetadata:errorCodes:]"
+ "+[UAFBiomeStreamWriter logScheduledDailyAssetStatus]"
+ "+[UAFCommonUtilities activateExperimentId:trialNamespace:]"
+ "+[UAFCommonUtilities activateExperimentId:trialNamespace:]_block_invoke"
+ "+[UAFCommonUtilities emptyLegacyStagingLogsDirectoryUnderStoragePath:]"
+ "+[UAFCommonUtilities experimentIdentifiersTrialClient:trialNamespace:staged:]"
+ "+[UAFCommonUtilities getMADownloadErrors:newerVersionError:assetSetName:assetSetID:]"
+ "+[UAFCommonUtilities trialClient]"
+ "+[UAFInstrumentationProvider logAlterFromAtomicInstance:assetType:configuredSpecifiers:sourceType:alterSetData:]"
+ "+[UAFRootsV2AssetSet disableMAAtomicInstanceForRootsV2:assetSetName:completion:]"
+ "+[UAFRootsV2AssetSet invalidateRootsV2Instance:assetSetName:completion:]"
+ "+[UAFRootsV2AssetSet lockRootsV2InstanceId:assetSetName:error:]"
+ "+[UAFRootsV2AssetSet removeDisabledByRootsV2MarkerForAtomicInstance:assetSetName:]"
+ "+[UAFRootsV2AssetSet removeDisabledByRootsV2MarkersForAssetSet:]"
+ "+[UAFRootsV2AssetSet requestDisableMAAtomicInstanceForRootsV2:assetSetName:queue:completion:]"
+ "+[UAFRootsV2AssetSet requestDisableMAAtomicInstanceForRootsV2:assetSetName:queue:completion:]_block_invoke"
+ "+[UAFRootsV2AssetSet requestDisableMAAtomicInstanceForRootsV2:assetSetName:queue:completion:]_block_invoke_2"
+ "+[UAFRootsV2AssetSet requestInvalidateRootsV2Instance:assetSetName:queue:completion:]"
+ "+[UAFRootsV2AssetSet requestInvalidateRootsV2Instance:assetSetName:queue:completion:]_block_invoke"
+ "+[UAFRootsV2AssetSet requestInvalidateRootsV2Instance:assetSetName:queue:completion:]_block_invoke_2"
+ "+[UAFRootsV2AssetSet rootsV2Directory]"
+ "+[UAFRootsV2AssetSet sendNotificationsForInstalledRoots]"
+ ","
+ "-[UAFAssetSet assetSetIdForSELF:atomicInstanceMetadata:]"
+ "-[UAFAssetSet initializeRootsV2WithInstanceId:assetSet:consistencyToken:]"
+ "-[UAFAssetSet resolveConsistencyToken:]"
+ "-[UAFAssetSet setupExperiment:disableExperimentation:]"
+ "-[UAFAssetSetConsistencyToken initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:rootsV2InstanceId:bootUUID:experimentActivated:]"
+ "-[UAFAssetSetManager _processSubscriptionDatabaseExtensionToken:xpcError:error:]"
+ "-[UAFAssetSetManager _subscriptionDatabaseAccessIsGranted]"
+ "-[UAFAssetSetManager ensureSubscriptionDatabaseAccessSync]"
+ "-[UAFAssetSetManager ensureSubscriptionDatabaseAccessWithQueue:completion:]"
+ "-[UAFAssetSetManager ensureSubscriptionDatabaseAccessWithQueue:completion:]_block_invoke_2"
+ "-[UAFAssetSetManager metadataForSubscriptions:policies:includeSpecifierKeys:queue:completion:]_block_invoke"
+ "-[UAFAssetSetManager metadataForSubscriptions:policies:includeSpecifierKeys:queue:completion:]_block_invoke_2"
+ "-[UAFAssetSetManager sumMetadataEntries:forKey:]"
+ "-[UAFAutoAssetSet initFromAssetInfoCache:autoAssets:experiment:atomicInstance:]"
+ "-[UAFAutoAssetSet invalidateWithQueue:completion:]"
+ "-[UAFAutoAssetSet readAtomicInstanceInfoFromAssetInfoCache:autoAssets:experiment:atomicInstance:]"
+ "-[UAFRootsV2AssetSet dealloc]"
+ "-[UAFRootsV2AssetSet getAssetWithName:andSpecifier:experimentationEnabled:experimentId:]"
+ "-[UAFRootsV2AssetSet loadAssets:experiment:]"
+ "-[UAFRootsV2AssetSet lockAssets:error:]"
+ "-[UAFSubscriptionStoreManager _getSubscriptionsAsDictionary:subscriptionsFor:]"
+ "-[UAFSubscriptionStoreManager _getSubscriptionsAsDictionary:user:]"
+ "-[UAFSubscriptionStoreManager _prepareGetSubscriptionsStatement:user:]"
+ "-[UAFXPCConnection disableMAAtomicInstanceForRootsV2:assetSetName:completion:]_block_invoke"
+ "-[UAFXPCConnection disableMAAtomicInstanceForRootsV2:assetSetName:completion:]_block_invoke_2"
+ "-[UAFXPCConnection invalidateRootsV2Instance:assetSetName:completion:]_block_invoke"
+ "-[UAFXPCConnection invalidateRootsV2Instance:assetSetName:completion:]_block_invoke_2"
+ "-[UAFXPCConnection lockLatestAtomicInstance:atomicInstance:completion:]"
+ "-[UAFXPCConnection requestSubscriptionDatabaseAccess:]_block_invoke"
+ "-[UAFXPCConnection requestSubscriptionDatabaseAccess:]_block_invoke_2"
+ "-[UAFXPCConnection requestSubscriptionDatabaseAccessSync:]_block_invoke"
+ "-[UAFXPCConnection requestSubscriptionDatabaseAccessSync:]_block_invoke_2"
+ "-[UAFXPCService isConnectionAppleSigned:error:]"
+ "-[UAFXPCService requestSubscriptionDatabaseAccess:]"
+ ".%@"
+ ".disabledByRootsV2"
+ ".lock"
+ ".notReady"
+ "/private/"
+ "/private/var/db/assetsubscriptiond/RootsV2"
+ "/private/var/db/assetsubscriptiond/assetInfoCache"
+ "@\"UAFAsset\"24@?0@\"NSString\"8@\"NSString\"16"
+ "AdopterExperimentActivation"
+ "Asset Set Consistency Token %@ for assetSet %@ with atomic instance %@ rootsV2InstanceId %@ (%@ with ref count %lld) experimentActivated %@ bootUUID %@ isBootUUIDCurrent %d object instance %@ experiment %@ preinstalledAssetsSummary %@"
+ "AssetRootsV2"
+ "AssetSource is reported Unknown by MA"
+ "B16@?0@\"NSError\"8"
+ "Cannot invalidate the current Roots V2 instance"
+ "Could not acquire exclusive lock on %@"
+ "Could not determine console user"
+ "Could not determine current user"
+ "Error with set-targets, see the 'assetSetErrors' key for a per-set breakdown: %@"
+ "Failed to acquire exclusive lock on MA locker: %s"
+ "Failed to acquire exclusive lock: %s"
+ "Failed to consume sandbox extension"
+ "Failed to create SecTask"
+ "Failed to create disabledByRootsV2 marker file"
+ "Failed to delete Roots V2 lock file"
+ "Failed to init MAAutoAssetSet for %@"
+ "Failed to issue sandbox extension"
+ "Failed to lock Roots V2 instance: %s"
+ "Failed to read subscriptions from DB"
+ "Failed to verify signing identity"
+ "Failed to write metadata plist"
+ "Instrumentation Failure"
+ "Invalid token"
+ "KEY_NOT_FOUND_IN_RESPONSE"
+ "LocalOnly"
+ "Lock file does not exist: %@"
+ "MA atomic instance %@ has been disabled by roots V2 transition for asset set %@"
+ "MA atomic instance is still in use by another process"
+ "Missing Available OS Build in Asset Origin Report"
+ "Missing Downloaded OS Build in Asset Origin Report"
+ "No XPC connection"
+ "No current root exists"
+ "No extension token received"
+ "No local cache available for %@ and localOnly policy is set"
+ "No signing identifier found"
+ "Roots V2 instance is still in use by another process"
+ "Roots V2 instance lock file already deleted"
+ "RootsV2"
+ "Sandbox Extension Failure"
+ "Sandbox consuming failed"
+ "Sandbox issuing failed"
+ "Staging"
+ "TIMESTAMP"
+ "UAFRootsV2AssetSet.Concurrent"
+ "Unauthorized client"
+ "_Specifier"
+ "_Version"
+ "_uafCacheCheck"
+ "asset_info_cache_support"
+ "atomic instance cache path does not exist at %@"
+ "checkLocalDownloadSize"
+ "com.apple."
+ "current"
+ "demo-external"
+ "demo-internal"
+ "failed to get atomic instance metadata path for asset set %@, atomic instance %@"
+ "file-read-data"
+ "get subscriptions as dictionary"
+ "metadataForSubscriptions"
+ "nil extension"
+ "notReady"
+ "resolvedLocation"
+ "rootsV2InstanceId"
+ "v16@?0@\"NSArray\"8"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v32@?0@\"NSDictionary\"8q16@\"NSError\"24"
+ "|"
- "#16@0:8"
- "%s #settings Already in progress download for dictation assets language %{public}@... Skipping..."
- "%s #settings Assets not available due to no UOD support. Return NO."
- "%s #settings Assistant preferences changed to : %s"
- "%s #settings Auto retry download on enablement change"
- "%s #settings Auto retry download on language change, language = %{public}@"
- "%s #settings Auto retry download on network change"
- "%s #settings Auto retry is disabled"
- "%s #settings Auto retry skipped due to need for inexpensive network"
- "%s #settings Calling delegate assistantEnabledDidChange : %s"
- "%s #settings Calling delegate assistantLanguageDidChange : %{public}@"
- "%s #settings Cannot download Dictation assets due to nil language"
- "%s #settings Cannot download Dictation assets for %{public}@ due to network connectivity..."
- "%s #settings Cannot download Siri assets for language %{public}@ due to network connectivity..."
- "%s #settings Checking to see if on-device dictation assets are available for %{public}@"
- "%s #settings Current asset state %@ with value %d"
- "%s #settings Dictation available for %{public}@"
- "%s #settings Dictation download complete for %{public}@"
- "%s #settings Dictation download percent %d for language %{public}@"
- "%s #settings Dictation still not available after download completed for language %{public}@"
- "%s #settings Dictation still not available after retrying availability check for language %{public}@"
- "%s #settings Dictation still not available after successful download for language %{public}@"
- "%s #settings Download API call"
- "%s #settings Download Siri assets for language:%{public}@ cellular:%d"
- "%s #settings Download complete for language %{public}@"
- "%s #settings Download legacy Siri assets for language:%{public}@ cellular:%d"
- "%s #settings Download progress %d%% for language %{public}@"
- "%s #settings Download progress clamped to %d%% for language %{public}@"
- "%s #settings Download requested for Dictation assets (%{public}@) but hit out of space... %llu bytes needed"
- "%s #settings Download requested for Siri assets (%{public}@) but hit out of space... %llu bytes needed"
- "%s #settings Download requested for Siri assets skipped due to existing download in progress (%{public}@)..."
- "%s #settings Download requested for language (%{public}@) (cellular:%d)"
- "%s #settings Downloading dictation assets for language %{public}@..."
- "%s #settings Error getting free disk space: %@"
- "%s #settings Error getting free size"
- "%s #settings Failed to check UAF asset status due to timeout"
- "%s #settings Failed to check assets availability due to nil language. Return NO"
- "%s #settings Failed to check assets availability due to timeout, language = %{public}@"
- "%s #settings Failed to check assets download size due to error %@, language = %{public}@"
- "%s #settings Failed to check assistant UOD availability due to timeout"
- "%s #settings Failed to check assistant UOD status due to timeout"
- "%s #settings Failed to check size due to error %@"
- "%s #settings Failed to check size due to timeout"
- "%s #settings Failed to subscribe to dictation language %{public}@ due to error %@"
- "%s #settings Failed to subscribe to dictation language %{public}@ due to timeout"
- "%s #settings Forcing display state to %@ (enabled:%d, hybridUOD:%d, fullUOD:%d)"
- "%s #settings Forcing display state to %@ due to UOD available"
- "%s #settings Forcing downloading state to failed"
- "%s #settings Forcing unknown server state to not started until WiFi gets enabled"
- "%s #settings Free space %llu / Download size %llu"
- "%s #settings NO returned for UOD"
- "%s #settings Network path nothing changed"
- "%s #settings Primary network (satisfied:%d, expensive: %d)"
- "%s #settings Refresh server side asset state %@ with value %d"
- "%s #settings Retry attempt %d"
- "%s #settings Retry attempt %d skipped"
- "%s #settings Returning enough space for assets even with an unknown size requested"
- "%s #settings Returning enough space for assets even with an unknown size requested, language = %{public}@"
- "%s #settings Returning state %@ with value %d"
- "%s #settings Siri language changed to : %{public}@"
- "%s #settings Skip download due to assets available already"
- "%s #settings Skip download due to network path"
- "%s #settings Skip download due to nil language"
- "%s #settings Skip retry after hitting limit %d"
- "%s #settings Skip retry attempt on pending execution"
- "%s #settings Skipping due to one attempt already in progress"
- "%s #settings Start UAFAssetStatus observer"
- "%s #settings Start UOD observer"
- "%s #settings Start language observer"
- "%s #settings Start network observer"
- "%s #settings Start observers"
- "%s #settings Start preferences observer"
- "%s #settings Stop observers"
- "%s #settings UOD available already for %{public}@. Skip updating download progress..."
- "%s #settings UOD check available:%d prev:%d"
- "%s #settings UOD check for language %{public}@"
- "%s #settings UOD status watchdog hit. Download failed. Language = %{public}@"
- "%s #settings UOD status watchdog hit. Fetching status again. Language = %{public}@"
- "%s #settings Updated Siri asset status for %{public}@ with state %@ and value %@"
- "%s #settings Using mock asset state %@ with value %d"
- "%s #settings Using path to check for free space: %@"
- "%s #settings asset status delegate"
- "%s #settings asset status update requested"
- "%s #settings checkAssetStatus error: %@"
- "%s #settings dictation language is nil!"
- "%s #settings diskSpaceNeededInBytesForLanguage with nil completion, language = %{public}@"
- "%s #settings download XPC"
- "%s #settings download cellular XPC"
- "%s #settings download dictation XPC"
- "%s #settings forcing state to UAFAssetStateFinished due to sudden UOD available for %{public}@..."
- "%s #settings forcing state to UAFAssetStateNotStarted due to sudden UOD unavailable for %{public}@..."
- "%s #settings isHighQualityValue is nil for %{public}@!"
- "%s #settings isInstalledValue is nil for %{public}@!"
- "%s #settings nil completion"
- "%s #settings nil language"
- "%s #settings nil language, skipping download..."
- "%s #settings offlineDictationStatus is nil!"
- "%s #settings offlineDictationStatusForLanguage is nil for %{public}@!"
- "%s #settings posting Dictation notification not supported."
- "%s #settings posting Siri notification not supported."
- "%s #settings progress status %@"
- "%s #settings return default size %llu"
- "%s #settings return size %llu"
- "%s #settings server UOD check for language %{public}@"
- "%s #settings service resumed"
- "%s #settings service suspended"
- "%s #settings siriUODAvailabilityDidChange delegate available:%d"
- "%s #settings update asset status %@ for language %{public}@"
- "%s %{public}@ does not contain a dictionary"
- "%s %{public}@ does not contain valid eventInformation"
- "%s Allowing removal of assets"
- "%s Asset set %{public}@ has no metadata asset, skipping"
- "%s Asset set %{public}@ should not have any entries"
- "%s Asset set %{public}@ should not have any entries for OS version %{public}@"
- "%s Asset set configuration error %{public}@ metadata asset defined but not found"
- "%s Assistant Subscription not allowed"
- "%s Assistant enablement changed to : %{public}@"
- "%s Assistant language changed to : %{public}@"
- "%s Assistant mode changed to : %{public}@"
- "%s Bad parameters passed: %{public}@"
- "%s Cannot delete logs for nil or empty asset set name"
- "%s Cannot find/create nil path"
- "%s Cannot log target: invalid parameters (target: %{public}@, assetSetName: %{public}@)"
- "%s Cannot log targets: invalid parameters (targets count: %lu, assetSetName: %{public}@)"
- "%s Cannot serialize nil JSON object"
- "%s Completed proxying '%{public}@' request on behalf of pid %d"
- "%s Completed proxying request on behalf of pid %d"
- "%s Could not create auto asset set %{public}@ : %{public}@"
- "%s Could not create platform asset subscription"
- "%s Could not determine status for set %{public}@ : %{public}@"
- "%s Could not determine system user, failing to create platform subscription: %{public}@"
- "%s Could not find TRIProject for %{public}@"
- "%s Could not indicate lack of need in this OS for asset set %{public}@ : %{public}@"
- "%s Could not retrieve subscription for user '%@', subscriber '%{public}@', subscription '%{public}@': %{public}@"
- "%s Could not retrieve subscriptions, device is currently locked"
- "%s Could not set potential siri locale to %{public}@: %{public}@"
- "%s Creating AutoAssetSet %{public}@ for staging."
- "%s Deleting %{public}@"
- "%s Deleting directory that was found with the path of %{public}@"
- "%s Deleting directory that was found with the path of the build version file %{public}@"
- "%s Denying removal of unused asset sets due to inhibiting asset removal"
- "%s Denying subscription due to exceeding usage limits for subscriber \"%{public}@\""
- "%s Dictation enablement changed to : %{public}@"
- "%s Did not find %{public}@. Skip removing logs for eliminated assetSet %{public}@"
- "%s Did not find %{public}@. Skipping rollover"
- "%s Disallowing removal of assets post-upgrade"
- "%s Emitting Siri subscription change AIR event"
- "%s Error updating last seen time for current user: %@"
- "%s Exception while parsing %{public}@: %{public}@"
- "%s Failed to configureAssetDelivery after updating Shadow Siri Locale: %{public}@"
- "%s Failed to create directory at %{public}@ with error %{public}@"
- "%s Failed to delete directory with the path of the build version file: %{public}@"
- "%s Failed to delete existing item at %{public}@: %{public}@"
- "%s Failed to delete item in %{public}@ with error: %{public}@"
- "%s Failed to delete the directory: %{public}@"
- "%s Failed to delete the old %{public}@: %{public}@. Skipping rollover"
- "%s Failed to delete unexpected file at %{public}@: %{public}@"
- "%s Failed to enumerate directory contents: %{public}@"
- "%s Failed to get %{public}@"
- "%s Failed to get all subscriptions due to error: %{public}@. Stopping staging"
- "%s Failed to get default storage path"
- "%s Failed to get log file for target %{public}@"
- "%s Failed to get parent directory for %{public}@"
- "%s Failed to get running build version"
- "%s Failed to get the relevant staging directory URLs for rollover"
- "%s Failed to move item from %{public}@ to %{public}@ with error %{public}@"
- "%s Failed to parse %{public}@: %{public}@"
- "%s Failed to read %{public}@: %{public}@"
- "%s Failed to remove \"%@\": %{public}@"
- "%s Failed to remove file %{public}@: %{public}@"
- "%s Failed to rollover logs from %{public}@ to %{public}@"
- "%s Failed to serialize JSON object: %{public}@"
- "%s Failed to serialize data to json"
- "%s Failed to write build version to %{public}@"
- "%s Failed to write to %{public}@ with error %{public}@"
- "%s Failed to write to log file %{public}@"
- "%s Found unexpected file where directory should exist at %{public}@. Deleting file..."
- "%s GMS enablement changed to : %{public}@"
- "%s Invalid parameters for getLogFileForTarget: %@"
- "%s Newer asset entry %{public}@ missing download size metadata for key %{public}@"
- "%s Newer asset entry %{public}@ skipped due to having a latest downloaded entry"
- "%s No platform assets available when attempting to staging assets"
- "%s No staging targets for other OS versions"
- "%s No version -> configuration managers available when attempting to staging assets"
- "%s Not emitting Siri subscription event for %{public}@ for subscriber %{public}@ as it is up to date"
- "%s Not updating Assistant enablement as it is unchanged from : %{public}@"
- "%s Not updating Assistant language as value is unchanged from : %{public}@"
- "%s Not updating Assistant mode as it is unchanged from : %{public}@"
- "%s Not updating Dictation enablement as it is unchanged from : %{public}@"
- "%s Not updating GMS enablement as it is unchanged from : %{public}@"
- "%s Not updating system language as value is unchanged from : %{public}@"
- "%s Platform asset missing from asset set id %@"
- "%s Platform asset version missing from platform's asset metadata"
- "%s Platform asset's metadata missing"
- "%s Posting notification of subscription availability"
- "%s Processing update to assistant capabilities"
- "%s Processing update to assistant language"
- "%s Processing update to assistant preferences"
- "%s Processing update to gms availability"
- "%s Processing update to system language"
- "%s Received '%{public}@' request, proxying to subscription service on behalf of pid %d"
- "%s Received request from pid %d, proxying to subscription service"
- "%s Removed \"%@\""
- "%s Set potential siri locale to %{public}@"
- "%s Siri IE is now: wants assets: %d, language: %{public}@, mode: %{public}@"
- "%s Siri configured for: language %{public}@, mode: %{public}@ (assistant enabled: %d, assistant language: %{public}@)"
- "%s Skipping platform directory: %{public}@ < %{public}@"
- "%s Skipping rollover - build version %{public}@ has not changed"
- "%s Staging assets due to receiving MA notification for platform assets"
- "%s Staging with platform asset version %{public}@"
- "%s Starting observers"
- "%s Stopping observers"
- "%s Successfully removed log file %{public}@"
- "%s Successfully rolled staging logs due to moving from build %{public}@ to %{public}@"
- "%s System language changed to : %{public}@"
- "%s Unable to determine the %{public}@ build version. Proceeding with rollover"
- "%s Unexpectedly couldn't retrieve subscription user '%@' subscriber '%{public}@' subscription: '%{public}@': %{public}@"
- "%s Usage limit exceeded for asset set %@ of usage type %@ with limit of %d"
- "%s XPC received and not subscription service"
- "%s checkAssetStatus failed with: %@"
- "%s diskSpaceInBytesForLanguage %@ failed with: %@"
- "%s logAlterFromAtomicInstance: Biome unavailable for %{public}@, aborting"
- "%s logAlterFromAtomicInstance: assetSet=%{public}@ subscription=%{public}@ addedCount=%lu removedCount=%lu"
- "%s logAlterFromAtomicInstance: nil assetSetName for %{public}@, aborting"
- "%s logAlterFromAtomicInstance: sending Biome event for %{public}@ assetSet=%{public}@"
- "%s logAssetSetDownloadEvent: Biome unavailable, aborting"
- "%s logAssetSetDownloadEvent: assetSet=%{public}@ eventType=%lu entryCount=%lu errorCount=%lu"
- "%s logAssetSetDownloadEvent: sending Biome event for assetSet=%{public}@"
- "%s logScheduledDailyAssetStatus: Biome unavailable, aborting"
- "%s logScheduledDailyAssetStatus: sending Biome event"
- "%s logScheduledDailyAssetStatus: starting"
- "("
- "+[UAFAssetSetManager _subscriptionDiffersFromDB:subscriber:user:expirationOnlyCount:error:]"
- "+[UAFAssetSetManager isSubscriptionExpirationIgnorable:subscriber:user:]_block_invoke"
- "+[UAFAssetStatus dictationAvailableForLanguage:]"
- "+[UAFAutoAssetInstance clear:path:]"
- "+[UAFAutoAssetManager findDiffBetweenOldAssetSetUsages:newAssetSetUsages:knownAssetSets:usedAssetSets:configurationManager:]"
- "+[UAFAutoAssetManager removeUnusedAutoAssetSets:usedAutoAssetSets:]"
- "+[UAFAutoAssetManager stageAssetSet:targets:platformAssetVersion:]"
- "+[UAFAutoAssetManager stageAssetsWithNewSubscriptions:oldSubscriptions:autoAssetSets:]"
- "+[UAFAutoAssetManager targetForAssetSet:specifiers:version:autoAssetSets:]"
- "+[UAFBiomeInstrumenter _getBiomeUAFAssetSet:atomicInstanceMetadata:entries:errorCodes:]"
- "+[UAFCommonUtilities experimentIdentifiersTrialClient:trialNamespace:]"
- "+[UAFCommonUtilities getFreeDiskSpaceInBytes]"
- "+[UAFCommonUtilities getFreeDiskSpaceNeededInBytes:]"
- "+[UAFCommonUtilities trialClientWithProject:]"
- "+[UAFInstrumentationProvider _getMADownloadErrors:newerVersionError:assetSetName:assetSetID:]"
- "+[UAFInstrumentationProvider logAlterFromAtomicInstance:sourceType:alterSetData:]"
- "+[UAFManagedSubscriptions _stageAssetsUponPlatformAssetSetUpdate]"
- "+[UAFManagedSubscriptions manageAssistantSubscription:withMode:subscriber:subscriptionName:shouldReport:]"
- "+[UAFManagedSubscriptions managePlatformSubscription]"
- "+[UAFPlatform configurationManagers:]"
- "+[UAFPlatform platformAssetVersion:]"
- "+[UAFStagingLogManager createBuildVersionFile]"
- "+[UAFStagingLogManager deleteItemAtURL:error:]"
- "+[UAFStagingLogManager deleteLoggedTargetsForEliminatedAssetSet:]"
- "+[UAFStagingLogManager deleteLoggedTargetsForEliminatedAssetSet:]_block_invoke"
- "+[UAFStagingLogManager findOrCreateDir:]"
- "+[UAFStagingLogManager getBuildVersionFromStagingLogsDir]"
- "+[UAFStagingLogManager getLastBuildStagingLogsDir]"
- "+[UAFStagingLogManager getLatestStagingLogsDir]"
- "+[UAFStagingLogManager getLogFileForTarget:andAssetSetName:]"
- "+[UAFStagingLogManager getRootStagingLogsDir]"
- "+[UAFStagingLogManager logTargetSync:withAssetSetName:withPlatformAssetVersion:]"
- "+[UAFStagingLogManager logTargets:withAssetSetName:withPlatformAssetVersion:]"
- "+[UAFStagingLogManager moveItemAtURL:toURL:]"
- "+[UAFStagingLogManager rollStagingLogsUponNewBuildVersion]_block_invoke"
- "+[UAFStagingLogManager serializeJSONObjectToData:]"
- "+[UAFStagingLogManager writeToFile:content:]"
- "-%@"
- "-[UAFAssetSet assetSetIdForSELF:assetSetOrigin:]"
- "-[UAFAssetSetConfiguration isUsageLimitExceeded:]"
- "-[UAFAssetSetConsistencyToken initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:bootUUID:experimentActivated:]"
- "-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke"
- "-[UAFAssetUtilities _assistantPreferencesUpdate]_block_invoke"
- "-[UAFAssetUtilities _checkFreeSpaceNeededForLanguage:forClient:]"
- "-[UAFAssetUtilities _downloadSiriAssetsOverCellular:]"
- "-[UAFAssetUtilities _downloadSiriAssetsRetry]"
- "-[UAFAssetUtilities _downloadSiriAssetsRetry]_block_invoke"
- "-[UAFAssetUtilities _downloadSiriAssetsWithDelay:]"
- "-[UAFAssetUtilities _handleNetworkPathUpdate:]"
- "-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke"
- "-[UAFAssetUtilities _stopObservers]"
- "-[UAFAssetUtilities _triggerDelegateAssetStatusUpdated]_block_invoke"
- "-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke"
- "-[UAFAssetUtilities assetStatus]"
- "-[UAFAssetUtilities assetsAreAvailableForLanguage:completion:]"
- "-[UAFAssetUtilities assistantUODStatus]"
- "-[UAFAssetUtilities currentAssetStatus]"
- "-[UAFAssetUtilities downloadSiriAssetsIfNeeded]"
- "-[UAFAssetUtilities downloadSiriAssetsIfNeeded]_block_invoke_3"
- "-[UAFAssetUtilities downloadSiriAssetsOverCellular]"
- "-[UAFAssetUtilities downloadSiriAssets]"
- "-[UAFAssetUtilities getDiskSpaceNeededInBytesForLanguage:forClient:]"
- "-[UAFAssetUtilities refreshUAFAssetStatusAsync]_block_invoke"
- "-[UAFAssetUtilities refreshUAFAssetStatusAsync]_block_invoke_3"
- "-[UAFAssetUtilities startObserversWithOptions:]_block_invoke"
- "-[UAFAssetUtilities startObserversWithOptions:]_block_invoke_2"
- "-[UAFAssetUtilities understandingOnDeviceAssetsAvailable]"
- "-[UAFAssetUtilitiesService _checkFreeSpaceNeededForLanguage:isDictation:]"
- "-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]"
- "-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke"
- "-[UAFAssetUtilitiesService _downloadSiriAssetsWithCellular:]_block_invoke"
- "-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]"
- "-[UAFAssetUtilitiesService _getDiskSpaceNeededInBytesForLanguage:isDictation:error:]"
- "-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]"
- "-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke"
- "-[UAFAssetUtilitiesService _handleUpdateProgress:status:language:]"
- "-[UAFAssetUtilitiesService _siriDownloadCompleteForLanguage:]"
- "-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]"
- "-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke"
- "-[UAFAssetUtilitiesService _updateAssetState:value:forLanguage:]"
- "-[UAFAssetUtilitiesService _updateDictationAvailabilityForLanguage:]"
- "-[UAFAssetUtilitiesService _updateDictationProgress:language:]"
- "-[UAFAssetUtilitiesService _updateProgress:forLanguage:]"
- "-[UAFAssetUtilitiesService _updateSiriAssetAvailability:forLanguage:]"
- "-[UAFAssetUtilitiesService checkAssetStatus:]"
- "-[UAFAssetUtilitiesService diskSpaceNeededInBytesForLanguage:forClient:completion:]"
- "-[UAFAssetUtilitiesService downloadDictationAssetsForLanguage:]"
- "-[UAFAssetUtilitiesService downloadSiriAssetsOverCellular]"
- "-[UAFAssetUtilitiesService downloadSiriAssets]"
- "-[UAFAssetUtilitiesService postAssetNotificationIfNeeded]"
- "-[UAFAssetUtilitiesService postDictationAssetNotificationForLanguage:]"
- "-[UAFAssetUtilitiesService resume]"
- "-[UAFAssetUtilitiesService suspend]"
- "-[UAFAssetUtilitiesService updateSiriAssetAvailabilityForLanguageSync:]"
- "-[UAFSubscriptionStoreManager _getSubscriptions:user:]"
- "-[UAFSubscriptionStoreManager _isUsageLimitExceeded:]"
- "-[UAFSubscriptionStoreManager subscribe:subscriptions:user:node:]_block_invoke"
- "-[UAFXPCConnection checkAssetStatus:]_block_invoke"
- "-[UAFXPCConnection checkAssetStatus:]_block_invoke_2"
- "-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke"
- "-[UAFXPCConnection diskSpaceNeededInBytesForLanguage:forClient:completion:]_block_invoke_2"
- "-[UAFXPCConnection downloadDictationAssetsForLanguage:]_block_invoke_2"
- "-[UAFXPCConnection downloadSiriAssetsOverCellular]_block_invoke_2"
- "-[UAFXPCConnection downloadSiriAssets]_block_invoke_2"
- "-[UAFXPCConnection postAssetNotificationIfNeeded]_block_invoke_2"
- "-[UAFXPCConnection postDictationAssetNotificationForLanguage:]_block_invoke_2"
- "-[UAFXPCService _assistantCapabilitiesUpdate]"
- "-[UAFXPCService _assistantEnabledChanged]"
- "-[UAFXPCService _assistantGMSAvailabilityUpdate]"
- "-[UAFXPCService _assistantLanguageChanged]"
- "-[UAFXPCService _assistantLanguageUpdate]"
- "-[UAFXPCService _assistantModeChanged]"
- "-[UAFXPCService _assistantPreferencesUpdate]"
- "-[UAFXPCService _dictationEnabledChanged]"
- "-[UAFXPCService _gmsEnabledChanged]"
- "-[UAFXPCService _startObservers]"
- "-[UAFXPCService _stopObservers]"
- "-[UAFXPCService _systemLanguageChanged]"
- "-[UAFXPCService _systemLanguageUpdate]"
- "-[UAFXPCService _updateAssistantSubscription]"
- "-[UAFXPCService _updateGMSSiriLanguageSubscription]"
- "-[UAFXPCService _updateShadowSiriLocale:]_block_invoke"
- "-[UAFXPCService checkAssetStatus:]"
- "-[UAFXPCService diskSpaceNeededInBytesForLanguage:forClient:completion:]"
- "-[UAFXPCService downloadDictationAssetsForLanguage:]"
- "-[UAFXPCService downloadSiriAssetsOverCellular]"
- "-[UAFXPCService downloadSiriAssets]"
- "-[UAFXPCService expireSubscriptions:]_block_invoke"
- "-[UAFXPCService lockLatestAtomicInstance:atomicInstance:completion:]_block_invoke"
- "-[UAFXPCService markAssetsExpired:completion:]"
- "-[UAFXPCService markAssetsExpired:completion:]_block_invoke"
- "-[UAFXPCService operationWithConfig:completion:]_block_invoke"
- "-[UAFXPCService postAssetNotificationIfNeeded]"
- "-[UAFXPCService postDictationAssetNotificationForLanguage:]"
- "-[UAFXPCService runUpdates]_block_invoke_2"
- "-[UAFXPCService setSystemConfigurationForKey:withValue:completion:]_block_invoke"
- "-[UAFXPCService subscriptions:subscriber:user:completion:]"
- ".cxx_destruct"
- ".json"
- "@"
- "@\"<UAFAssetUtilitiesDelegate>\""
- "@\"MAAutoAssetSet\""
- "@\"MAAutoAssetSetRapidLock\""
- "@\"MAAutoAssetSetStatus\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_group>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_nw_path_evaluator>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListener\""
- "@\"RBSAssertion\""
- "@\"UAFAssetSetConfiguration\""
- "@\"UAFAssetSetConsistencyToken\""
- "@\"UAFAssetSetExperiment\""
- "@\"UAFAssetStatus\""
- "@\"UAFAssetUtilitiesService\""
- "@\"UAFAutoAssetSet\""
- "@\"UAFConfigurationManager\""
- "@\"UAFExperimentalAssetsConfiguration\""
- "@\"UAFRetryState\""
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8I16"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8^I16"
- "@24@0:8^i16"
- "@24@0:8^{sqlite3_stmt=}16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@28@0:8B16^q20"
- "@28@0:8^{sqlite3_stmt=}16i24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@32@0:8@16^B24"
- "@32@0:8^@16@24"
- "@32@0:8^@16^@24"
- "@32@0:8^{sqlite3_stmt=}16@24"
- "@36@0:8@16@24B32"
- "@36@0:8@16B24^@28"
- "@36@0:8@16I24^@28"
- "@36@0:8^@16I24^@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16@24B32B36"
- "@40@0:8@16@24Q32"
- "@40@0:8@16@24^@32"
- "@40@0:8@16@24^B32"
- "@40@0:8@16Q24@?32"
- "@40@0:8@16^B24^@32"
- "@44@0:8@16@24B32@36"
- "@44@0:8@16@24B32^@36"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32@?40"
- "@48@0:8@16@24@32^@40"
- "@48@0:8@16@24B32B36@40"
- "@48@0:8@16@24^B32^@40"
- "@48@0:8Q16d24Q32Q40"
- "@52@0:8@16@24@32B40@44"
- "@52@0:8@16B24@28@36@?44"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24@32@40B48B52"
- "@56@0:8@16@24@32@40Q48"
- "@56@0:8@16@24@32@40^@48"
- "@56@0:8@16@24@32^B40^@48"
- "@56@0:8@16@24@32^q40^@48"
- "@56@0:8@16@24^B32^B40^@48"
- "@64@0:8@16@24@32@40@48^@56"
- "@68@0:8@16@24@32@40@48@56B64"
- "@68@0:8@16^@24B32^B36^B44^@52^@60"
- "@72@0:8@16@24@32@40@48@56^@64"
- "@?"
- "@?16@0:8"
- "AFDeviceSupportsSiriUOD"
- "AFLanguageCodeDidChangeDarwinNotification"
- "AFOfflineDictationStatusHighQualityKey"
- "AFOfflineDictationStatusInstalledKey"
- "AFPreferences"
- "AFSettingsConnection"
- "AFShouldRunAsrOnServerForUOD"
- "AFSiriAvailability"
- "AFSiriXAssetDidChangeDarwinNotification"
- "AFUODStatusSupportedFull"
- "AFUODStatusSupportedHybrid"
- "Asset Set Consistency Token %@ for assetSet %@ with atomic instance %@ (%@ with ref count %lld) experimentActivated %@ bootUUID %@ isBootUUIDCurrent %d object instance %@ experiment %@ preinstalledAssetsSummary %@"
- "AssetDelivery"
- "B"
- "B16@0:8"
- "B20@0:8I16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B24@0:8^@16"
- "B24@0:8r*16"
- "B28@0:8@16B24"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "B32@0:8@16@?24"
- "B32@0:8@16^@24"
- "B32@0:8@16^Q24"
- "B32@0:8^B16^i24"
- "B36@0:8i16^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}20^@28"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24^@32"
- "B40@0:8@16^@24^@32"
- "B48@0:8@16@24@32@40"
- "B48@0:8@16@24@32^@40"
- "B48@0:8@16^@24^B32^B40"
- "B52@0:8@16@24#32B40^@44"
- "B52@0:8@16@24B32@36^@44"
- "B56@0:8@16@24@32@40@48"
- "B60@0:8@16@24@32@40@48B56"
- "B72@0:8@16@24B32B36@40^B48^B56^B64"
- "BuildVersion.json"
- "DailyStatus"
- "GMAvailabilityWrapper"
- "I"
- "I16@0:8"
- "I32@0:8@16^@24"
- "Invalid URL path"
- "JSONObjectWithData:options:error:"
- "LastStagingLogsFromLastBuildVersion"
- "LatestStagingLogs"
- "MaxUsageValues"
- "Missing assetSetName"
- "Missing minTargetOSVersion"
- "MorphunAssets"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "NSStringFromAFSiriOrchestrationMode"
- "NSXPCListenerDelegate"
- "NoRemove"
- "OSSupported:"
- "OSThirdPartyCompatibilityVersion:"
- "OSVersion"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q24@0:8Q16"
- "Q28@0:8@16B24"
- "Q32@0:8@16@24"
- "Q32@0:8@16Q24"
- "Q32@0:8Q16Q24"
- "T#,R"
- "T@\"<UAFAssetUtilitiesDelegate>\",W,N,V_delegate"
- "T@\"MAAutoAssetSet\",&,N,V_autoAssetSet"
- "T@\"MAAutoAssetSetRapidLock\",R,N,V_rapidLock"
- "T@\"MAAutoAssetSetStatus\",&,N,V_autoAssetSetStatus"
- "T@\"NSArray\",&,N,V_assets"
- "T@\"NSArray\",&,N,V_baseURLs"
- "T@\"NSArray\",&,N,V_expansions"
- "T@\"NSArray\",&,N,V_requiredUsageTypes"
- "T@\"NSArray\",&,N,V_subscriptions"
- "T@\"NSArray\",&,N,V_usageLimits"
- "T@\"NSArray\",&,N,V_usageTypes"
- "T@\"NSArray\",R,N"
- "T@\"NSDate\",R,C,V_expiration"
- "T@\"NSDictionary\",&,N,V_assetSpecifiers"
- "T@\"NSDictionary\",&,N,V_assistantUODStatus"
- "T@\"NSDictionary\",&,N,V_minVersions"
- "T@\"NSDictionary\",&,N,V_usageValues"
- "T@\"NSDictionary\",&,N,V_values"
- "T@\"NSDictionary\",R,C,V_assetSets"
- "T@\"NSDictionary\",R,C,V_metadata"
- "T@\"NSDictionary\",R,C,V_usageAliases"
- "T@\"NSDictionary\",R,N,V_usages"
- "T@\"NSError\",&,N,V_autoAssetSetError"
- "T@\"NSError\",R,V_availableForUseError"
- "T@\"NSError\",R,V_newerVersionError"
- "T@\"NSMutableDictionary\",&,N,V_assetSetCache"
- "T@\"NSMutableDictionary\",&,N,V_assets"
- "T@\"NSMutableDictionary\",&,N,V_autoAssetSets"
- "T@\"NSMutableDictionary\",&,N,V_dictationStatus"
- "T@\"NSMutableDictionary\",&,N,V_errors"
- "T@\"NSMutableDictionary\",&,N,V_progresses"
- "T@\"NSMutableDictionary\",&,N,V_statuses"
- "T@\"NSMutableSet\",&,V_assetSetObservers"
- "T@\"NSNumber\",&,N,V_value"
- "T@\"NSObject<OS_dispatch_group>\",&,N,V_assistantGroup"
- "T@\"NSObject<OS_dispatch_group>\",&,N,V_statusGroup"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_assistantQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_delegateQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_downloadQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_statusQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSSet\",&,N,V_preinstalledAssetsSummary"
- "T@\"NSSet\",C,N,V_addedSpecifiers"
- "T@\"NSSet\",C,N,V_removedSelectors"
- "T@\"NSString\",&,N,V_assetSetName"
- "T@\"NSString\",&,N,V_atomicInstance"
- "T@\"NSString\",&,N,V_autoAssetSpecifierTemplate"
- "T@\"NSString\",&,N,V_autoAssetType"
- "T@\"NSString\",&,N,V_catalogAssetSetID"
- "T@\"NSString\",&,N,V_experimentId"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",&,N,V_maxOSVersion"
- "T@\"NSString\",&,N,V_metadataAsset"
- "T@\"NSString\",&,N,V_minOSVersion"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",&,N,V_siriLanguage"
- "T@\"NSString\",&,N,V_thirdPartyCompatibilityVersion"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_trialFactor"
- "T@\"NSString\",C,N,V_trialNamespace"
- "T@\"NSString\",C,N,V_trialProject"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,V_assistantLanguage"
- "T@\"NSString\",R,C,V_experimentId"
- "T@\"NSString\",R,C,V_name"
- "T@\"NSString\",R,C,V_systemLanguage"
- "T@\"NSString\",R,N,V_bootUUID"
- "T@\"NSString\",R,N,V_gmsLanguage"
- "T@\"NSString\",R,N,V_siriLanguage"
- "T@\"NSString\",R,V_assetSetId"
- "T@\"NSString\",R,V_databaseName"
- "T@\"NSString\",R,V_latestDownloadedAtomicInstance"
- "T@\"NSURL\",&,N,V_originatingURL"
- "T@\"NSURL\",R,C,V_location"
- "T@\"NSUUID\",&,N,V_instanceUUID"
- "T@\"NSUUID\",&,N,V_uuid"
- "T@\"NSUUID\",R,N,V_uuid"
- "T@\"UAFAssetSetConsistencyToken\",R,C,V_consistencyToken"
- "T@\"UAFAssetSetExperiment\",&,N,V_experiment"
- "T@\"UAFAssetSetManager\",R,N"
- "T@\"UAFAssetStatus\",&,N,V_assetStatus"
- "T@\"UAFAutoAssetSet\",&,N,V_autoAssetSet"
- "T@\"UAFConfigurationManager\",&,N,V_assetSetManager"
- "T@\"UAFExperimentalAssetsConfiguration\",&,N,V_experimentalAssets"
- "T@\"UAFGestalt\",R,N"
- "T@\"UAFRetryState\",&,N,V_retryState"
- "T@?,C,N,V_internalProgressCompletion"
- "T@?,C,N,V_progressWithStatus"
- "T@?,C,N,V_updateHandler"
- "TB,N,V_assistantEnabled"
- "TB,N,V_autoRetryEnabled"
- "TB,N,V_cancelled"
- "TB,N,V_disableAssetRemoval"
- "TB,N,V_enableExpensiveCellular"
- "TB,N,V_experimentActivated"
- "TB,N,V_ignoreOSCompatibility"
- "TB,N,V_networkExpensive"
- "TB,N,V_networkSatisfied"
- "TB,N,V_pending"
- "TB,N,V_showHybridAsUnsupported"
- "TB,N,V_subjectToAppleIntelligenceWaitlist"
- "TB,N,V_understandingOnDeviceAssetsAvailable"
- "TB,N,V_uodAvailable"
- "TB,N,V_updateIsFinished"
- "TB,R"
- "TB,R,N,V_assistantEnabled"
- "TB,R,N,V_dictationEnabled"
- "TB,R,N,V_experimentActivated"
- "TB,R,N,V_experimentationEnabled"
- "TB,R,N,V_gmsEnabled"
- "TB,R,N,V_isBootUUIDCurrent"
- "TB,R,N,V_locked"
- "TB,R,V_originFactory"
- "TB,R,V_originPSUS"
- "TI,N,V_autoRetryLimit"
- "TI,N,V_retryCount"
- "TQ,N,V_completed"
- "TQ,N,V_completedWork"
- "TQ,N,V_maxProgressBeforeComplete"
- "TQ,N,V_reportedComplete"
- "TQ,N,V_reportedCompletedWork"
- "TQ,N,V_reportedPercent"
- "TQ,N,V_reportedStatus"
- "TQ,N,V_reportedTotal"
- "TQ,N,V_reportedTotalWork"
- "TQ,N,V_sourceType"
- "TQ,N,V_state"
- "TQ,N,V_total"
- "TQ,N,V_totalWork"
- "TQ,R"
- "TQ,R,N,V_assistantMode"
- "TQ,R,V_completedBytes"
- "TQ,R,V_downloadStatus"
- "TQ,R,V_totalBytes"
- "TQ,R,V_updateCount"
- "Td,N,V_assetAvailableCheckTimeout"
- "Td,N,V_autoRetryDelayOnFailure"
- "Td,N,V_autoRetryDelayOnFailureIncrement"
- "Td,N,V_autoRetryDelayOnSettingsChanged"
- "Td,R,V_completedPercent"
- "Ti,N,V_fd"
- "Ti,N,V_maStartupNotifyToken"
- "Ti,N,V_refCount"
- "Ti,N,V_uafNotifyToken"
- "Tq,R,V_originType"
- "UAF"
- "UAF.stagingDueToPlatformAssetUpdate"
- "UAFAppleIntelligenceReporting"
- "UAFAsset"
- "UAFAssetConfiguration"
- "UAFAssetExpansion"
- "UAFAssetSet"
- "UAFAssetSetConfiguration"
- "UAFAssetSetConsistencyToken"
- "UAFAssetSetExperiment"
- "UAFAssetSetExperimentConfiguration"
- "UAFAssetSetManager"
- "UAFAssetSetMetadata"
- "UAFAssetSetObserver"
- "UAFAssetSetProgress"
- "UAFAssetSetStatus"
- "UAFAssetSetSubscription"
- "UAFAssetSetSubscriptionManager"
- "UAFAssetStatus"
- "UAFAssetUtilitiesService"
- "UAFAtomicInstanceMetadata"
- "UAFAutoAssetHistory"
- "UAFAutoAssetInstance"
- "UAFAutoAssetManager"
- "UAFAutoAssetProgress"
- "UAFAutoAssetSet"
- "UAFAutoBugCapture"
- "UAFBiomeInstrumenter"
- "UAFCommonUtilities"
- "UAFConfiguration"
- "UAFConfigurationManager"
- "UAFCoreAnalyticsInstrumenter"
- "UAFExperimentalAssetsConfiguration"
- "UAFExpiredAssets"
- "UAFGestalt"
- "UAFInstrumentationAlterSetData"
- "UAFInstrumentationProvider"
- "UAFManagedSubscriptions"
- "UAFMinVersionConfiguration"
- "UAFOSEligibility"
- "UAFPlatform"
- "UAFPreinstalledAssetsCache"
- "UAFPrestageConfiguration"
- "UAFRetryState"
- "UAFStagingLogManager.Serial"
- "UAFSubscriptionStoreManager"
- "UAFTrialConversions"
- "UAFUsageAliasConfiguration"
- "UAFUser"
- "UAFUserManager"
- "UAFXPCActivity"
- "UAFXPCConnection"
- "UAFXPCProxyService"
- "UAFXPCProxyServiceInterface"
- "UAFXPCService"
- "UOD not supported"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathComponent:isDirectory:"
- "URLByAppendingPathExtension:"
- "URLByDeletingLastPathComponent"
- "URLByDeletingPathExtension"
- "URLByResolvingSymlinksInPath"
- "URLForDirectory:inDomain:appropriateForURL:create:error:"
- "URLWithString:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Unable to find class %s"
- "UsageLimits"
- "Vv16@0:8"
- "Vv24@0:8@\"NSString\"16"
- "Vv24@0:8@16"
- "Vv24@0:8@?16"
- "Vv24@0:8@?<v@?@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
- "Vv24@0:8@?<v@?@\"UAFAssetStatus\"@\"NSError\">16"
- "Vv32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@\"UAFAssetSetConsistencyToken\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@16@?24"
- "Vv40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16Q24@?<v@?@\"NSNumber\"@\"NSError\">32"
- "Vv40@0:8@16@24@?32"
- "Vv40@0:8@16Q24@?32"
- "XPC sent to wrong endpoint"
- "^v16@0:8"
- "^{_NSZone=}16@0:8"
- "^{sqlite3=}"
- "^{sqlite3_stmt=}"
- "_TtC21UnifiedAssetFramework19UAFAIREventReporter"
- "_acquireAssertion"
- "_addedSpecifiers"
- "_allowCreate"
- "_assetAvailableCheckTimeout"
- "_assetNameToAutoAsset"
- "_assetSetCache"
- "_assetSetId"
- "_assetSetManager"
- "_assetSetName"
- "_assetSetObservers"
- "_assetSets"
- "_assetSetsComplete:assetSetCompleteness:"
- "_assetSpecifiers"
- "_assetStatus"
- "_assetUtilitiesService"
- "_assets"
- "_assistantCapabilitiesChangeToken"
- "_assistantCapabilitiesUpdate"
- "_assistantEnabled"
- "_assistantEnabledChanged"
- "_assistantGMSAvailabilityUpdate"
- "_assistantGroup"
- "_assistantLangChangeToken"
- "_assistantLanguage"
- "_assistantLanguageChanged"
- "_assistantLanguageUpdate"
- "_assistantMode"
- "_assistantModeChanged"
- "_assistantPrefChangeToken"
- "_assistantPreferencesUpdate"
- "_assistantQueue"
- "_assistantUODStatus"
- "_assistantUpdate"
- "_assistantUsageAliasForMode:"
- "_atomicInstance"
- "_autoAssetSet"
- "_autoAssetSetError"
- "_autoAssetSetStatus"
- "_autoAssetSets"
- "_autoAssetSpecifierTemplate"
- "_autoAssetType"
- "_autoRetryDelayOnFailure"
- "_autoRetryDelayOnFailureIncrement"
- "_autoRetryDelayOnSettingsChanged"
- "_autoRetryEnabled"
- "_autoRetryLimit"
- "_availableForUseError"
- "_baseURLs"
- "_beginDatabaseTransaction"
- "_bootUUID"
- "_cachingAutoAssetSet"
- "_cancelled"
- "_catalogAssetSetID"
- "_cfg"
- "_checkDbVersion:storedVersion:"
- "_checkFreeSpaceNeededForLanguage:forClient:"
- "_checkFreeSpaceNeededForLanguage:isDictation:"
- "_clearSystemAssetSetUsages"
- "_closeDatabase"
- "_collectAssetOriginMetadata:atomicInstanceOriginMetadata:entries:"
- "_completed"
- "_completedBytes"
- "_completedPercent"
- "_completedWork"
- "_completionWatchdogInProgress"
- "_connection"
- "_connectionInterrupted"
- "_connectionInvalidated"
- "_consistencyToken"
- "_constructBiomeAssetSet:storeManager:"
- "_createBiomeAssetSet:withAssets:sourceType:"
- "_createConnection"
- "_createHistoryDirIfNeeded:error:"
- "_createXPCConnection"
- "_currentOSVersion"
- "_dataFromSystemAssetSetUsages:"
- "_dataFromUAFAssetSubscription:"
- "_databaseName"
- "_dbUpToDate"
- "_deepestUnderlyingError:"
- "_delegate"
- "_delegateQueue"
- "_deleteDbVersion"
- "_deviceSupportsGenerativeModelSystems"
- "_dictationEnabled"
- "_dictationEnabledChanged"
- "_dictationStatus"
- "_directoryContainsPlist:"
- "_disableAssetRemoval"
- "_downloadDictationAssetsForLanguage:useCellular:"
- "_downloadQueue"
- "_downloadSiriAssetsOverCellular:"
- "_downloadSiriAssetsRetry"
- "_downloadSiriAssetsWithCellular:"
- "_downloadSiriAssetsWithDelay:"
- "_downloadStatus"
- "_downloadUnderstandingAssetsForLanguage:useCellular:"
- "_dropTable:"
- "_eligibilityCountryPolicyStringIsChina:"
- "_emitAssetDailyStatusEvent:atomicInstanceMetadata:entries:assetSetDailyStatusEventType:"
- "_emitSubscriptionComplete:subscriber:user:assetSets:"
- "_emitSubscriptionCompleteForAssetSet:"
- "_enableExpensiveCellular"
- "_endDatabaseTransaction"
- "_errors"
- "_expansions"
- "_experiment"
- "_experimentActivated"
- "_experimentId"
- "_experimentalAssets"
- "_experimentationEnabled"
- "_expiration"
- "_factoryAssetsPresent"
- "_fd"
- "_fetchAllConfiguration"
- "_fetchAllSystemAssetSetUsages"
- "_fetchExpiredSubscriptions"
- "_fetchSystemAssetSetUsages"
- "_finalizeStatements"
- "_generateHash"
- "_getAllSubscriptions:"
- "_getAssetOriginType:"
- "_getAssetSource:"
- "_getAssetSpecifiersForSubscription:assetSetUsages:"
- "_getAssetTypeFromConfig"
- "_getAutoAssetSetInfo:entries:includeAssetVersion:"
- "_getBiomeAssetSetStatus:atomicInstanceMetadata:entries:errorCodes:"
- "_getBiomeEventDeviceMetadata"
- "_getBiomeStreamForAssetSetStatus:atomicInstanceMetadata:entries:errorCodes:assetSetDailyStatusEventType:"
- "_getBiomeStreamForScheduledDailyAssetStatus"
- "_getBiomeUAFAssetSet:atomicInstanceMetadata:entries:errorCodes:"
- "_getDeprecatedDirectoriesForUsageAlias:baseURL:"
- "_getDeprecatedFilesForUsageAlias:baseURL:"
- "_getDeprecatedUsageAlias:usageAliasValue:"
- "_getDiskSpaceNeededInBytesForLanguage:isDictation:error:"
- "_getMADownloadErrors:newerVersionError:assetSetName:assetSetID:"
- "_getManagerReadOnly:"
- "_getPallasAudienceForType:"
- "_getPallasURLForType:"
- "_getPersistAssetInfoPath"
- "_getSubscribers:subscribers:"
- "_getSubscription:"
- "_getSubscription:subscription:user:"
- "_getSubscriptions:subscriptionsFor:"
- "_getSubscriptions:user:"
- "_getSubscriptionsStatus"
- "_getURLForDeprecatedUsageAlias:usageAliasValue:"
- "_getURLForUsageAlias:usageAliasName:usageAliasValue:"
- "_getUsageAlias:usageAliasValue:"
- "_getUser:lastSeen:nodeName:"
- "_gmsAvailabilityToken"
- "_gmsEnabled"
- "_gmsEnabledChanged"
- "_gmsLanguage"
- "_handleDictationCompletionForLanguage:"
- "_handleDictationProgress:status:language:"
- "_handleNetworkPathUpdate:"
- "_handleUpdateProgress:status:language:"
- "_hash"
- "_identifier"
- "_ignoreOSCompatibility"
- "_instanceUUID"
- "_internalProgressCompletion"
- "_invalidate"
- "_isBootUUIDCurrent"
- "_isLegacySiriDevice"
- "_isUsageLimitExceeded:"
- "_latestDownloadedAtomicInstance"
- "_location"
- "_locked"
- "_maStartupNotifyToken"
- "_maxOSVersion"
- "_maxProgressBeforeComplete"
- "_metadata"
- "_metadataAsset"
- "_minOSVersion"
- "_minVersions"
- "_moveDatabase"
- "_name"
- "_networkExpensive"
- "_networkIsExpensiveForPath:"
- "_networkIsSatisfiedForPath:"
- "_networkSatisfied"
- "_newerVersionError"
- "_observerEnabled"
- "_observerOptions"
- "_oldDatabaseName"
- "_openDatabase:"
- "_openDatabaseFile:existed:"
- "_originFactory"
- "_originPSUS"
- "_originType"
- "_originatingURL"
- "_pathEvaluator"
- "_pending"
- "_performDbUpgrade:"
- "_persistAssetSetInfo:assetSetIdentifier:isEliminating:jsonData:error:"
- "_platformAssetSetObserver"
- "_postAssetStateChangedNotification"
- "_predicateKeys"
- "_preinstalledAssetsSummary"
- "_prepareStatements"
- "_progressWithStatus"
- "_progresses"
- "_queue"
- "_queuesArePaused"
- "_rapidLock"
- "_rbassertion"
- "_readAllSubscribers"
- "_readAllSubscriptions"
- "_readAllSubscriptionsAndSubscribers"
- "_readAllUsers"
- "_readConfigurationKey"
- "_readDbVersion"
- "_readOnly"
- "_readSubscription"
- "_readSubscriptionsForSubscriber"
- "_readSubscriptionsForUser"
- "_readUser"
- "_readUsersOlderThan"
- "_refCount"
- "_releaseAssertion"
- "_removeAllSubscriptions"
- "_removeAllSystemAssetSetUsages"
- "_removeAllUsers"
- "_removeSubscription"
- "_removeUser"
- "_removeUser:"
- "_removedSelectors"
- "_reportedComplete"
- "_reportedCompletedWork"
- "_reportedPercent"
- "_reportedStatus"
- "_reportedTotal"
- "_reportedTotalWork"
- "_requiredUsageTypes"
- "_retryCount"
- "_retryState"
- "_rollbackDatabaseTransaction"
- "_rootsPresent"
- "_serviceName"
- "_setDbVersion"
- "_setDbVersion:"
- "_setPallasAudience:forType:"
- "_setPallasURL:forType:"
- "_setQueue:"
- "_setSystemAssetSetUsages"
- "_setSystemAssetSetUsages:"
- "_setSystemAssetSetUsages:usages:"
- "_setUserLastSeenTime:node:time:"
- "_showHybridAsUnsupported"
- "_siriDownloadCompleteForLanguage:"
- "_siriLanguage"
- "_sourceType"
- "_stageAssetsUponPlatformAssetSetUpdate"
- "_startObservers"
- "_state"
- "_statusGroup"
- "_statusQueue"
- "_statuses"
- "_stopObserver"
- "_stopObservers"
- "_store"
- "_subjectToAppleIntelligenceWaitlist"
- "_subscribeSubscription:subscriptionName:assetSetSubscription:expires:user:"
- "_subscriptionDiffersFromDB:subscriber:user:expirationOnlyCount:error:"
- "_subscriptionService"
- "_subscriptionTime:"
- "_subscriptions"
- "_systemAssetSetUsagesFromData:"
- "_systemLangChangeToken"
- "_systemLanguage"
- "_systemLanguageChanged"
- "_systemLanguageUpdate"
- "_thirdPartyCompatibilityVersion"
- "_total"
- "_totalBytes"
- "_totalWork"
- "_trialFactor"
- "_trialNamespace"
- "_trialProject"
- "_triggerCompletionTimerForLanguage:"
- "_triggerDelegateAssetStatusUpdated"
- "_uafAssetSetSubscriptionFromData:"
- "_uafNotifyToken"
- "_understandingOnDeviceAssetsAvailable"
- "_unsubscribeSubscription:subscription:user:"
- "_uodAvailable"
- "_updateAssetState:value:forLanguage:"
- "_updateAssetUtilitiesLanguage"
- "_updateAssistantSubscription"
- "_updateCount"
- "_updateCountryPolicy:"
- "_updateDelegateForUODAvailable:uodStatus:"
- "_updateDeviceLanguage:"
- "_updateDictationAvailabilityForLanguage:"
- "_updateDictationProgress:language:"
- "_updateDictationState:value:forLanguage:"
- "_updateEligibilityData"
- "_updateGMSSiriLanguageSubscription"
- "_updateHandler"
- "_updateIsFinished"
- "_updateMorphunSystemLanguageSubscription"
- "_updateNLSystemLanguageSubscription"
- "_updateProgress:forLanguage:"
- "_updateShadowSiriLocale:"
- "_updateShadowSiriLocaleIfNeeded"
- "_updateSiriAssetAvailability:forLanguage:"
- "_updateSiriLanguage:"
- "_updateSystemAssetSetUsages:assetSetUsages:configurationManager:"
- "_usageAliases"
- "_usageCountForUsageType:usingUsages:"
- "_usageLimits"
- "_usageTypes"
- "_usageValues"
- "_usages"
- "_uuid"
- "_value"
- "_values"
- "_writeAssetInfoToFile:data:filePath:error:"
- "_writeConfigurationKey"
- "_writeSubscription"
- "_writeUserLastSeen"
- "_xpcConnection"
- "_xpcListener"
- "absoluteString"
- "absoluteURL"
- "acquireClassAAssertion"
- "acquireShortTermLockSync"
- "acquireWithError:"
- "addDeprecatedValues:"
- "addEntriesFromDictionary:"
- "addKeyValuePair:with:"
- "addObject:"
- "addObjectsFromArray:"
- "addedSpecifiers"
- "allKeys"
- "allObjects"
- "allUsers"
- "allValues"
- "allowCheckDownloadOverExpensive"
- "allowRemoves"
- "alterEntriesRepresentingAtomicSync:toBeComprisedOfEntries:withNeedPolicy:"
- "alternateDSID"
- "applyAssetTransformations:"
- "applyMinVersions:"
- "applyOSCompatibility:"
- "applySubscriptions:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayByAddingObjectsFromArray:"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "asr.language"
- "assetAttributes"
- "assetAvailableCheckTimeout"
- "assetAvailableOSBuild"
- "assetDeliveryReady"
- "assetDownloadedOSBuild"
- "assetId"
- "assetNamed:"
- "assetNamed:withUsage:"
- "assetNamed:withUsage:disableExperimentation:"
- "assetNamesForAssetSet:usages:"
- "assetOriginEntries"
- "assetOriginType"
- "assetProperty:"
- "assetRootSupported"
- "assetSetCache"
- "assetSetCacheMiss:"
- "assetSetComplete:"
- "assetSetEmpty:"
- "assetSetForStagingSync:asEntriesWhenTargeting:"
- "assetSetIdForSELF:assetSetOrigin:"
- "assetSetInfo:"
- "assetSetManager"
- "assetSetNamesFromUsages:configurationManager:"
- "assetSetObservers"
- "assetSetUsagesForSubscribers:storeManager:configurationManager:anyUnknown:error:"
- "assetSpecifier:assetSetConfiguration:"
- "assetSpecifiersFromRoots:"
- "assetStatus"
- "assetType"
- "assetWithName:autoAssets:experiment:"
- "assetdelivery-validation"
- "assets"
- "assetsAreAvailableForLanguage:completion:"
- "assetsExpired:error:"
- "assistantEnabled"
- "assistantEnabledDidChange:"
- "assistantGroup"
- "assistantIsEnabled"
- "assistantLanguage"
- "assistantLanguageDidChange:"
- "assistantMode"
- "assistantModeDescription:"
- "assistantModeFromDescription:mode:"
- "assistantQueue"
- "assistantUODStatus"
- "atomicInstanceFromLockPath:"
- "attributeWithDomain:name:"
- "attributes"
- "attributesOfFileSystemForPath:error:"
- "autoAssetDetailsForAssetNamed:assetSet:usages:autoAssetType:autoAssetSpecifier:"
- "autoAssetEntryToAsset:withAssetName:experimentationEnabled:experimentId:"
- "autoAssetExistsWithEntries:"
- "autoAssetSet:usages:uuid:autoAssets:experiment:atomicInstance:error:"
- "autoAssetSetClientName"
- "autoAssetSetError"
- "autoAssetSetForStatus:"
- "autoAssetSetStatus"
- "autoAssetSetStatus:"
- "autoAssetSpecifierTemplate"
- "autoAssetType"
- "autoAssets:usages:"
- "autoRetryDelayOnFailure"
- "autoRetryDelayOnFailureIncrement"
- "autoRetryDelayOnSettingsChanged"
- "autoRetryEnabled"
- "autoRetryLimit"
- "autorelease"
- "backgroundNeedPolicy"
- "baseURLs"
- "basicOriginType:"
- "bestEffortSerializeDictToJSONStr:error:"
- "bestSupportedLanguageCodeForLanguageCode:"
- "bestSupportedSiriLanguage"
- "bindData:col:data:"
- "bindDate:col:date:"
- "bindString:col:string:"
- "blockCheckDownload"
- "boolForKey:"
- "boolValue"
- "bootUUIDError"
- "bundle"
- "bundleForClass:"
- "bundleIdentifier"
- "bytes"
- "cStringUsingEncoding:"
- "cacheAssetSetCompleteness:autoAssetSetStatus:"
- "cacheAssetSetCompleteness:complete:"
- "cacheDeleteDefaultsKeyForAutoAssetType:autoAssetSpecifier:"
- "cacheDeleteDisabledForAssetNamed:assetSet:usages:"
- "cacheDeleteDisabledForAutoAssetType:autoAssetSpecifier:"
- "cacheDeleteStatusChange:"
- "cancelled"
- "captureWithType:subType:context:logCategory:"
- "captureWithType:subType:context:logCategory:withSDRDiagnosticReporter:"
- "catalogAssetSetID"
- "catalogCachedAssetSetID"
- "checkAssetStatus:"
- "checkAtomic:forAtomicInstance:awaitingDownload:withNeedPolicy:withTimeout:completion:"
- "checkAtomic:forAtomicInstance:awaitingDownload:withNeedPolicy:withTimeout:reportingProgress:completion:"
- "checkAtomicSync:forAtomicInstance:withTimeout:discoveredAtomicEntries:error:"
- "checkForAssetTypePath:"
- "class"
- "clear:path:"
- "clearSystemAssetSetUsages:"
- "clientDomainName"
- "clientWithIdentifier:"
- "coalesceDownloadStatus:"
- "coalesceDownloadStatus:withDownloadStatus:"
- "code"
- "com.apple.UAF.Asset.download"
- "com.apple.UAF.Asset.status"
- "com.apple.UAF.AssetUtilities.AssistantQueue"
- "com.apple.UAF.AssetUtilities.DelegateQueue"
- "com.apple.UAF.AssetUtilities.DownloadQueue"
- "com.apple.UAF.AssetUtilities.StatusQueue"
- "com.apple.gms.availability.notification"
- "com.apple.language.changed"
- "com.apple.siri.assistant.assistantengine.language"
- "com.apple.siri.assistant.hybrid.language"
- "com.apple.siri.assistant.language"
- "com.apple.siri.assistant.legacy.language"
- "com.apple.siri.intelligenceengine"
- "com.apple.siri.morphun"
- "com.apple.siri.nl"
- "com.apple.siri.nl.morphun."
- "com.apple.siri.nl.system.language"
- "com.apple.siri.uaf.validation.general"
- "com.apple.siri.understanding"
- "com.apple.summarizationkit"
- "com.apple.uaf.assetutil"
- "compareVersion:with:"
- "compatibilityVersionStringForAssetType:"
- "completed"
- "completedAtomicInstance:"
- "completedAtomicInstances"
- "completedBytes"
- "completedPercent"
- "completedWork"
- "componentsSeparatedByString:"
- "computePredicateKeys"
- "conditionallyLockLatestAssetSet:newestInstance:checkAtomicError:completion:"
- "configurationManagers:"
- "configureAssetDelivery:configurationManager:"
- "configureAssetDelivery:configurationManager:lockIfUnchanged:"
- "configureAssetDelivery:configurationManager:lockIfUnchanged:oldSubscriptions:newSubscriptions:userInitiated:"
- "configureAssetSet:specifiers:changed:downloaded:currentPolicy:"
- "configureAutoAssetsFromNewSubscriptions:oldSubscriptions:configurationManager:lockIfUnchanged:userInitiated:"
- "configureCacheDeleteWithConfig:completion:"
- "configuredAssetEntries"
- "conformsToProtocol:"
- "consistencyToken"
- "consistencyTokenFromConfig:atomicInstance:experiment:"
- "containsObject:"
- "containsString:"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "copy"
- "copyBootSessionUUID"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countForObject:"
- "countryCode"
- "createAssetFromMAAsset:assetName:experimentationEnabled:experimentId:"
- "createAssetFromPreinstalledWithAutoAssetInfo:assetName:experimentationEnabled:experimentId:"
- "createBuildVersionFile"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "createHoldSubscription:"
- "createLogEntryWithInfo:"
- "createProxyXPCConnection"
- "createSubscriptionXPCConnection"
- "createXPCConnection"
- "currentAssetStatus"
- "currentAssistantLanguage"
- "currentAssistantMode"
- "currentConnection"
- "currentConsoleUserWithUID:"
- "currentLocale"
- "currentLockURLForAssetSet:"
- "currentProcess"
- "currentSetStatus:"
- "currentSetStatusSync:"
- "currentUser"
- "currentUserWithNode:error:"
- "d"
- "d16@0:8"
- "daemonLaunchTasks"
- "daemonSubscriptionMigration"
- "data"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithContentsOfURL:options:error:"
- "dataWithJSONObject:options:error:"
- "databaseName"
- "date"
- "dateWithTimeIntervalSince1970:"
- "dateWithTimeIntervalSinceNow:"
- "dealloc"
- "debugDescription"
- "decimalDigitCharacterSet"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decomposeSaveFileURL:assetSetName:atomicInstance:"
- "defaultCheckPolicy"
- "defaultDeviceId"
- "defaultInterface"
- "defaultManager"
- "defaults"
- "delegate"
- "delegateQueue"
- "deleteItemAtURL:error:"
- "deleteLoggedTargetsForEliminatedAssetSet:"
- "description"
- "desiredOrchestrationMode"
- "destinationOfSymbolicLinkAtPath:error:"
- "deviceIsAudioAccessory"
- "deviceMatch:onMatch:"
- "deviceSupportAndUseHybridASR"
- "deviceSupportFullUOD"
- "diagnosticInformation:"
- "dictation."
- "dictationAvailableForLanguage:"
- "dictationEnabled"
- "dictationIsEnabled"
- "dictationStatus"
- "dictionary"
- "dictionaryForGestalt:"
- "dictionaryIsValid:"
- "dictionaryRepresentation"
- "dictionaryWithCapacity:"
- "dictionaryWithContentsOfURL:error:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "directoryValue"
- "disableAssetRemoval"
- "disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:"
- "disableCacheDelete:forAutoAssetType:autoAssetSpecifier:"
- "disabled"
- "diskSpaceNeededForSubscriber:subscriptionName:error:"
- "diskSpaceNeededForSubscribers:error:"
- "diskSpaceNeededForSubscribers:storeManager:configurationManager:error:"
- "diskSpaceNeededInBytesForLanguage:forClient:completion:"
- "distantFuture"
- "doDatabaseOperation:useTransaction:logDescription:error:"
- "domain"
- "downloadDictationAssetsForLanguage:"
- "downloadProgress"
- "downloadQueue"
- "downloadSiriAssets"
- "downloadSiriAssetsIfNeeded"
- "downloadSiriAssetsOverCellular"
- "downloadStatusForSubscriber:subscriptionName:"
- "downloadStatusForSubscriber:subscriptionName:queue:completion:"
- "downloadStatusForSubscribers:"
- "downloadStatusForSubscribers:queue:completion:"
- "downloadStatusPrecedence"
- "downloadedCatalogCachedAssetSetID"
- "effectiveUserIdentifier"
- "eliminateAllForAssetTypeSync:"
- "eliminateAssetType:"
- "eliminateAtomicSync:usingClientDomain:forAssetSetIdentifier:awaitingUnlocked:"
- "emitMessage:"
- "empty content"
- "enableExpensiveCellular"
- "enabled"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endAtomicLock:ofAtomicInstance:completion:"
- "endAtomicLockSync:ofAtomicInstance:"
- "endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:completion:"
- "endAtomicLocksSync:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:"
- "endShortTermLockSync"
- "entitledTrialNamespaceNames"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "errorForSQLite:"
- "errorWithDomain:code:userInfo:"
- "evaluateWithObject:"
- "eventInformation"
- "executablePath"
- "executeSQL:"
- "exlock:"
- "expansions"
- "experimentIdentifiersTrialClient:trialNamespace:"
- "experimentIdentifiersWithNamespaceName:"
- "experimentalAssets"
- "experimentationEnabled"
- "expirationAsString"
- "expireSubscriptions"
- "expireSubscriptions:"
- "expiredTokens:"
- "fd"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "fileLockPolicy"
- "fileSystemRepresentation"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "fileURLWithPath:isDirectory:relativeToURL:"
- "findDiffBetweenOldAssetSetUsages:newAssetSetUsages:knownAssetSets:usedAssetSets:configurationManager:"
- "findOrCreateDir:"
- "finished:withStatus:withError:"
- "finishedOutOfSpace:"
- "firstObject"
- "flattenSubscriptions:"
- "forceRemoveAutoAssetSet:"
- "fromAssetDir:error:"
- "fromContentsOfURL:assetSetManager:error:"
- "fromContentsOfURL:error:"
- "fromPreferences"
- "generateEntitledTrialNamespaces"
- "generateInformationWithError:"
- "getAllAssetSets"
- "getAllAssetSetsWithDeprecated:"
- "getAllDeprecatedAssetSets"
- "getAllSubscriptions:"
- "getAllSystemAssetSetUsages:"
- "getAllSystemConfiguration:"
- "getAssetNameFromPath:"
- "getAssetSelectorsFromSpecifiers:status:"
- "getAssetSet:"
- "getAssetSetAssets:usageValue:withSource:"
- "getAssetSetNoCache:deprecated:"
- "getAssetSetUsages:storeManager:"
- "getAssetSetUsagesForUsageAlias:usageAliasValue:"
- "getAssetStatusForLanguage:completionHandler:"
- "getAssets:"
- "getAssets:withSource:"
- "getAssistantLanguageIfAvailableSync"
- "getAutoAssetPreinstalled"
- "getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:telemetryInfo:"
- "getAutoAssetSpecifier:"
- "getAutoAssetType:"
- "getAutoAssets:"
- "getAutoSetEntries:specifiers:"
- "getBuildVersionFromStagingLogsDir"
- "getClientName"
- "getComparableUsages:"
- "getConcurrentQueue"
- "getConfigurationDirURL:"
- "getCurrentSpecifiers:expectedAutoAssetType:"
- "getDefaultStoragePath"
- "getDeprecatedUsageAliasNameFromPath:"
- "getDirectoryPath:trialNamespace:trialFactor:"
- "getDiskSpaceNeededInBytesForLanguage:forClient:"
- "getDownloadStatusForAssetSet:configurationManager:"
- "getDownloadStatusFromAssetSetUsages:configurationManager:"
- "getDownloadStatusFromAssetSetUsages:configurationManager:queue:completion:"
- "getDownloadStatusFromMAAutoAssetSetStatus:config:"
- "getExistingSubscription:subscriber:"
- "getFactorNameForLocale:"
- "getFilteredUsages:"
- "getFreeDiskSpaceInBytes"
- "getFreeDiskSpaceNeededInBytes:"
- "getISO8601Timestamp:withFractionalSeconds:"
- "getLanguage"
- "getLastBuildStagingLogsDir"
- "getLatestStagingLogsDir"
- "getLocalFileUrl"
- "getLockReason:"
- "getLogFileForTarget:andAssetSetName:"
- "getMAAutoAssetDownloadErrorsSync"
- "getMAPath:"
- "getMapReason:"
- "getMinVersion:provider:"
- "getPWUID:error:"
- "getPersistedAssetInfo"
- "getPrestageSubscriptions"
- "getReason:operation:"
- "getResourceValue:forKey:error:"
- "getRootStagingLogsDir"
- "getSerialQueue"
- "getSpecifiers:assetSetUsages:experiment:"
- "getSubscribers:error:"
- "getSubscribers:storeManager:error:"
- "getSubscription:subscriber:user:error:"
- "getSubscription:subscriber:user:storeManager:error:"
- "getSubscriptions:storeManager:"
- "getSubscriptions:user:error:"
- "getSubscriptions:user:storeManager:error:"
- "getSystemAssetSetUsages:"
- "getSystemConfigurationForKey:"
- "getSystemUsageAssets:"
- "getTemplatePart:"
- "getUAFPallasURLForAssetSet:"
- "getUAFPallasURLForAssetType:"
- "getUAFPopulationForAssetSet:"
- "getUAFPopulationForAssetType:"
- "getUID:andEUID:"
- "getUUIDBytes:"
- "getUsageAlias:usageAliasValue:"
- "getUserDefaultStoragePath"
- "getUserLastSeenTime:error:"
- "getUserNodeName:error:"
- "getUserServiceXPCEndpoint"
- "getUsers:"
- "getUsersOlderThanDate:error:"
- "getenv:"
- "geteuid"
- "gmsEnabled"
- "gmsLanguage"
- "gmsWantsAssets"
- "handleAssetStatusUpdated"
- "hasIdenticalAssets:"
- "hasIdenticalAssets:includeBootUUID:"
- "hasPath"
- "hasPrefix:"
- "hasStartupActivatedCompletedOnce"
- "hasSufficientDiskSpaceForClient:"
- "hasSufficientDiskSpaceForDownload"
- "hasSuffix:"
- "hash"
- "i16@0:8"
- "i20@0:8i16"
- "i24@0:8@16"
- "i24@0:8q16"
- "i24@0:8r*16"
- "i32@0:8@16@24"
- "i32@0:8@16@?24"
- "i32@0:8@16^@24"
- "i36@0:8^{sqlite3_stmt=}16i24@28"
- "i40@0:8@16@24@32"
- "i40@0:8@16@24@?32"
- "i40@0:8@16@24^@32"
- "i40@0:8@16^@24^@32"
- "i40@0:8@16^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}24^@32"
- "i40@0:8@16i24i28^@32"
- "i40@0:8^@16^@24@32"
- "i44@0:8@16B24@28@?36"
- "i44@0:8@?16B24@28^@36"
- "identifier"
- "ignoreOSCompatibility"
- "immediateNeedPolicy"
- "indexOfObject:"
- "init"
- "init:assetSetIdentifier:assetSetAtomicInstance:"
- "init:assetSets:usageAliases:"
- "init:assetSets:usageAliases:expires:"
- "initCache:"
- "initForAssetType:withAssetSpecifier:"
- "initForAssetType:withAssetSpecifier:assetLockedInhibitsRemoval:"
- "initForMinTargetOSVersion:toMaxTargetOSVersion:asEntriesWhenTargeting:"
- "initLockerUsingClientDomain:forAssetSetIdentifier:error:"
- "initLockerUsingClientDomain:forAssetSetIdentifier:usingDesiredPolicyCategory:completingFromQueue:error:"
- "initSubscriptionService"
- "initUsingClientDomain:forClientName:forAssetSetIdentifier:comprisedOfEntries:completingFromQueue:error:"
- "initUsingClientDomain:forClientName:forAssetSetIdentifier:comprisedOfEntries:error:"
- "initWithAliasName:aliasValue:"
- "initWithAssetName:assetSpecifier:assetVersion:assetLocale:assetSource:isAssetPathValid:assetPath:assetDownloadSizeInBytes:assetUnarchivedSizeInBytes:sourceOSBuild:promotedOSBuild:"
- "initWithAssetSet:configurationDirURLs:queue:updateHandler:"
- "initWithAssetSet:ignoreMobileAssetStartup:configurationDirURLs:queue:updateHandler:"
- "initWithAssetSet:queue:updateHandler:"
- "initWithAssetSet:usages:"
- "initWithAssetSet:usages:configurationDirURLs:"
- "initWithAssetSet:usages:configurationDirURLs:disableExperimentation:consistencyToken:"
- "initWithAssetSet:usages:disableExperimentation:"
- "initWithAssetSetName:assets:assetType:assetSetId:audienceId:mobileAssetDownloadErrorCodeFrequency:fromPreSoftwareUpdateStaging:expensiveCellularDownloadRequested:fromFactory:"
- "initWithAssetSetName:autoAssets:uuid:experiment:atomicInstance:error:"
- "initWithAssetSetStatus:statusReason:"
- "initWithAssetSetUsages:configurationManager:internalProgressWithStatus:"
- "initWithBytes:length:encoding:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithConfiguration:uuid:"
- "initWithDbDirPath:dbName:"
- "initWithDbDirPath:dbName:readOnly:allowCreate:"
- "initWithDefaultService"
- "initWithDeviceId:deviceType:programCode:systemBuild:inputLocale:nanoSecondsSinceLastBoot:"
- "initWithDeviceMetadata:availableAssetDailyStatus:"
- "initWithDictionary:"
- "initWithDictionary:assetSetManager:"
- "initWithExperimentId:assetSpecifiers:"
- "initWithExplanation:target:attributes:"
- "initWithFileDescriptor:closeOnDealloc:"
- "initWithLanguageCode:countryCode:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithMachServiceName:subscriptionService:"
- "initWithMobileAssetDownloadErrorCode:timesOccurred:"
- "initWithName:assetSets:usageAliases:"
- "initWithName:assetSets:usageAliases:expires:"
- "initWithName:location:metadata:"
- "initWithName:maxProgressBeforeComplete:progressWithStatus:"
- "initWithQueue:"
- "initWithStatus:"
- "initWithStatus:percent:completedBytes:totalBytes:"
- "initWithSubscriberName:subscriptions:"
- "initWithSubscriptionName:assetSetIndices:assetSetUsages:usageAliases:alteredAssetSets:eliminatedAssetSets:"
- "initWithSubscriptionServiceName"
- "initWithSuiteName:"
- "initWithType:"
- "initWithURLs:"
- "initWithUTF8String:"
- "initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:"
- "initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:bootUUID:experimentActivated:"
- "initWithUUIDString:"
- "initWithUafAssetSets:uafAssetSubscriptions:allAssets:"
- "initWithUsageName:usageValue:"
- "initWithUserService"
- "initWithXPCListener:subscriptionService:"
- "instance"
- "instanceDirURL"
- "instanceUUID"
- "intValue"
- "integerValue"
- "interfaceWithProtocol:"
- "internalProgressCompletion"
- "invalidate"
- "invalidate:completion:"
- "invalidateAtomicInstance:assetSetName:queue:completion:"
- "invalidateCache"
- "invalidateSyncWithError:"
- "invalidateWithQueue:completion:"
- "invertedSet"
- "isAssistantEnabled"
- "isBiomeAvailable"
- "isBootUUIDCurrent"
- "isDictationEnabled"
- "isEnabled"
- "isEqual:"
- "isEqualToNumber:"
- "isEqualToSet:"
- "isEqualToString:"
- "isEqualWithoutExpiration:"
- "isExpensive"
- "isFullUODSupportedForStatus:language:"
- "isGameModeEnabled"
- "isHybridUODSupportedForStatus:language:"
- "isInexpensiveNetworkAvailable"
- "isInternalInstall"
- "isKeySupported:key:"
- "isKindOfClass:"
- "isLatestConsistencyToken:"
- "isLocaleDownloadSupported:"
- "isLocaleEmbedded:"
- "isManaged"
- "isMemberOfClass:"
- "isMultiUser"
- "isOkayToHaveAsset"
- "isOnDemandAssetSubscriptionAllowed"
- "isProxy"
- "isSharedIPad"
- "isSiriAnalyticsAvailable"
- "isSiriknowledgedSupported"
- "isStalled"
- "isSubscriptionExpirationIgnorable:subscriber:user:"
- "isSymptomDiagnosticReporterAvailable"
- "isSystemUser:error:"
- "isSystemUserUsingUID:"
- "isTrialAvailable"
- "isUsageLimitExceeded:"
- "isValid:assetSetManager:error:"
- "isValid:error:"
- "isValid:fileType:fileVersions:error:"
- "isValid:fileURL:error:"
- "isValid:validUsageTypes:error:"
- "isValidJSONObject:"
- "isValidTemplate:requiredUsageTypes:error:"
- "isValidUsages:"
- "isValidValue:key:kind:required:error:"
- "jsonDictionary"
- "kAFPreferencesDidChangeDarwinNotification"
- "kAFSiriCapabilitiesDidChangeNotification"
- "knownUsagesForAssetSet:usageType:"
- "languageCode"
- "lastPathComponent"
- "latestAtomicInstanceForClients:"
- "latestAtomicInstanceForClients:OSSupported:error:"
- "latestAtomicInstanceFromMA:error:"
- "latestDowloadedAtomicInstanceEntries"
- "latestDownloadedAtomicInstanceFromFactoryPreinstalled"
- "latestDownloadedAtomicInstanceFromPreSUStaging"
- "latestStatusForClients:error:"
- "length"
- "levelForFactor:withNamespaceName:"
- "levelOneOfCase"
- "listenForMAStartupNotification:updateHandler:"
- "listenForNotification:queue:updateHandler:"
- "listenForUAFNotificationsForAssetSet:forRoot:queue:updateHandler:"
- "listenForUpdates:updateHandler:"
- "listener:shouldAcceptNewConnection:"
- "loadAutoAssets:experiment:experimentActivated:"
- "loadToken:error:"
- "localTimeZone"
- "localeWithLocaleIdentifier:"
- "localizedDescription"
- "lock:"
- "lockAtomicSync:forAtomicInstance:error:"
- "lockAtomicSync:forAtomicInstance:withNeedPolicy:withTimeout:lockedAtomicEntries:error:"
- "lockAutoAssets:error:"
- "lockLatestAssetSet:atomicInstance:"
- "lockLatestAssetSet:atomicInstance:completion:"
- "lockLatestAtomicInstance:atomicInstance:completion:"
- "lockURL"
- "lockedAtomicEntriesOriginReportSync:forLockedAtomicInstance:oflockedAtomicEntries:error:"
- "logAlterFromAtomicInstance:sourceType:addedAssets:removedAssets:"
- "logAlterFromAtomicInstance:sourceType:alterSetData:"
- "logAssetSetDownloadEvent:atomicInstanceMetadata:entries:errorCodes:assetSetDailyStatusEventType:"
- "logAtomicInstance:name:entries:"
- "logAvailableAssetDailyStatus"
- "logDownloadTriggerEventWithLanguage:hasExistingAssets:retryCount:"
- "logScheduledDailyAssetStatus"
- "logSiriSubscription:subscriber:subscription:userId:locale:mode:unsubscribed:"
- "logSubscriptionCompleteForSubscriptions:subscriber:user:"
- "logTargetSync:withAssetSetName:withPlatformAssetVersion:"
- "logTargets:withAssetSetName:withPlatformAssetVersion:"
- "logUAFAssetSetDailyStatus:atomicInstanceMetadata:entries:assetSetDailyStatusEventType:"
- "logUAFAssetSetState:assetSpecifiersAndVersions:"
- "loginUser"
- "longLongValue"
- "lowercaseString"
- "maStartupNotifyToken"
- "mainBundle"
- "maintenanceTaskWithCompletion:"
- "manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:"
- "manageAssistantSubscription:withMode:"
- "manageAssistantSubscription:withMode:subscriber:subscriptionName:shouldReport:"
- "manageGMSSiriLanguageSubscription:language:mode:"
- "manageMorphunSystemLocaleSubscription:"
- "manageNLSystemLanguageSubscription:"
- "manageNLSystemLanguageSubscription:subscriber:subscriptionName:"
- "managePlatformSubscription"
- "manageSubscription:subscriber:assetSets:usageAliases:useHold:userInitiated:"
- "manageSummarizationKitSubscription"
- "mapAsset:queue:completion:"
- "mapLockedAtomicEntry:forAtomicInstance:mappingSelector:completion:"
- "markAssetsExpired:completion:"
- "markAssetsExpired:error:"
- "maxOSVersion"
- "maxProgressBeforeComplete"
- "maxTargetOSVersion"
- "maxVersionFromVersionString:"
- "metadataAsset"
- "migrateMBSetupUserSubscriptions:user:node:"
- "migrateSubscriptions:user:completion:"
- "minOSVersion"
- "minTargetOSVersion"
- "minVersions"
- "minVersions:"
- "mobileGestaltQuery:"
- "mockAssetStatus"
- "morphun.language"
- "morphunUsagesForLocale:"
- "moveItemAtPath:toPath:error:"
- "moveItemAtURL:toURL:"
- "moveItemAtURL:toURL:error:"
- "mutableCopy"
- "nameForUser:error:"
- "namespaceNameFromId:"
- "nanoHasGreymatterCompanion"
- "needForAtomicSync:withNeedPolicy:"
- "networkExpensive"
- "networkPathChangeSatisfied:isExpensive:"
- "networkSatisfied"
- "newerAtomicInstanceDiscovered"
- "newerDiscoveredAtomicEntries"
- "nil"
- "nil filePath"
- "nil language"
- "nodeForUser:error:"
- "nolock:"
- "notificationForAssetSet:forRoot:"
- "notifyRegistrationName:forAssetSetIdentifier:"
- "notifyRegistrationName:forAssetType:"
- "now"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLong:"
- "numberWithLongLong:"
- "numberWithShort:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeAllAssetSets"
- "observeAssetSet:"
- "observeAssetSet:policies:queue:handler:"
- "observeAssetSet:queue:handler:"
- "observeAssetSetExperimentalNamespace:"
- "offlineDictationStatus"
- "openFD:oflags:mode:error:"
- "operationWithConfig:completion:"
- "originatingURL"
- "osVersionConfigMatch:"
- "overlayRoots:"
- "path"
- "pathExtension"
- "pathWithComponents:"
- "pending"
- "performDbUpgrade"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performUserCleanup"
- "performUserCleanupOnQueue:completion:"
- "persistAssetSetInfoConfiguring:entries:isEliminating:reason:"
- "persistAssetSetInfoLocked:atomicEntries:autoAssetSet:isEliminating:reason:"
- "persistentDomainForName:"
- "platformAssetVersion"
- "platformAssetVersion:"
- "populateCache:"
- "postAssetNotificationIfNeeded"
- "postDictationAssetNotificationForLanguage:"
- "precedenceOfStatus:"
- "predicateMatch:"
- "predicateMatch:predicateKeys:"
- "predicateWithFormat:"
- "preferredLanguages"
- "processAssetSet:allAssets:"
- "processIdIsLockingToken:statBuffer:error:"
- "processIdentifier"
- "processIdsLockingToken:"
- "processInfo"
- "processName"
- "progress:"
- "progress:completed:total:status:context:"
- "progressWithStatus"
- "progresses"
- "projectIdFromName:"
- "propertiesAsDictionary"
- "propertiesAsDictionary:"
- "pwdNameForUser:error:"
- "pwdNodeForUser:error:"
- "pwdUIDToUserID:"
- "pwdUserIDToUID:withError:"
- "pwdUserWithNodeForUID:uid:error:"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "q32@0:8@16@24"
- "query:forKey:"
- "queryAllSupportedKeys:"
- "queryAssetType:"
- "queryMetaDataSync"
- "queue"
- "rangeOfCharacterFromSet:"
- "rangeOfString:"
- "rangeOfString:options:"
- "rapidLock"
- "readData:col:"
- "readDate:col:"
- "readString:col:"
- "recordEvent:::"
- "refCount"
- "refreshUAFAssetStatusAsync"
- "refreshUnderstandingOnDeviceAssetsAvailableAsync"
- "regionCode"
- "registerOnBootUAFActivityWithLockAssertion:"
- "registerUpdateForNamespaceName:queue:usingBlock:"
- "release"
- "releaseClassAAssertion:"
- "releaseIncompatibleAssetSet:specifiers:configuration:"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllSubscriptions"
- "removeAllSystemAssetSetUsages"
- "removeAllUsers"
- "removeAutoAssetSet:fallbackAlter:"
- "removeDeprecatedAssetSets"
- "removeDeprecatedAutoAssetSets"
- "removeItemAtPath:error:"
- "removeItemAtURL:error:"
- "removeObject:"
- "removeObjectForKey:"
- "removeObjectsInArray:"
- "removeObserver:"
- "removeToken:"
- "removeUnusedAutoAssetSets:usedAutoAssetSets:"
- "removeUser:"
- "removeUser:queue:completion:"
- "removedSelectors"
- "rename:toPath:error:"
- "reportPercent:status:totalKnown:"
- "reportStatus:"
- "reportedComplete"
- "reportedCompletedWork"
- "reportedPercent"
- "reportedStatus"
- "reportedTotal"
- "reportedTotalWork"
- "reporter"
- "requiredUsageTypes"
- "resetAssetSets:"
- "resetAssetSets:queue:completion:"
- "resetAutoAsset:"
- "resetAutoAsset:userInfo:"
- "resetAutoAssets"
- "resetAutoAssets:"
- "respondsToSelector:"
- "results"
- "resume"
- "retain"
- "retainCount"
- "retrieveAssetSet:usages:"
- "retrieveAssetSet:usages:consistencyToken:"
- "retrieveAssetSet:usages:consistencyToken:queue:completion:"
- "retrieveAssetSet:usages:disableExperimentation:"
- "retrieveAssetSet:usages:queue:completion:"
- "retryCount"
- "retryState"
- "returnTypes:"
- "rollStagingLogsUponNewBuildVersion"
- "rootDirectory"
- "runUpdates"
- "running"
- "sandboxCheckMachEndpoint:"
- "saveFileURL:"
- "schedulerPolicy"
- "scheme"
- "selectXPCEndpoint"
- "self"
- "self is nil"
- "sendCAEvent:assetSpecifier:assetVersion:"
- "sendEvent:"
- "sendNotificationDBReset"
- "sendNotificationForAssetSet:"
- "sendUAFNotificationForAssetSet:forRoot:"
- "serializeDictToJSONData:error:"
- "serializeDictToJSONStr:error:"
- "serializeJSONObjectToData:"
- "serviceName"
- "set"
- "setAddedSpecifiers:"
- "setAllowCheckDownloadOnBattery:"
- "setAllowCheckDownloadOverCellular:"
- "setAllowCheckDownloadOverExpensive:"
- "setAssetAvailableCheckTimeout:"
- "setAssetSetCache:"
- "setAssetSetManager:"
- "setAssetSetName:"
- "setAssetSetObservers:"
- "setAssetSpecifiers:"
- "setAssetStatus:"
- "setAssets:"
- "setAssistantEnabled:"
- "setAssistantGroup:"
- "setAssistantQueue:"
- "setAssistantUODStatus:"
- "setAtomicInstance:"
- "setAutoAssetSet:"
- "setAutoAssetSetError:"
- "setAutoAssetSetStatus:"
- "setAutoAssetSets:"
- "setAutoAssetSpecifierTemplate:"
- "setAutoAssetType:"
- "setAutoRetryDelayOnFailure:"
- "setAutoRetryDelayOnFailureIncrement:"
- "setAutoRetryDelayOnSettingsChanged:"
- "setAutoRetryEnabled:"
- "setAutoRetryLimit:"
- "setBackgroundNeedPolicy:configuration:"
- "setBaseURLs:"
- "setBlockCheckDownload:"
- "setBool:forKey:"
- "setCancelled:"
- "setCatalogAssetSetID:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCompleted:"
- "setCompletedWork:"
- "setDateFormat:"
- "setDelegate:"
- "setDelegateQueue:"
- "setDictationStatus:"
- "setDisableAssetRemoval:"
- "setDoNotBlockBeforeFirstUnlock:"
- "setDoNotBlockOnNetworkStatus:"
- "setDownloadQueue:"
- "setEnableExpensiveCellular:"
- "setErrors:"
- "setExistingAssets:"
- "setExpansions:"
- "setExperiment:"
- "setExperimentActivated:"
- "setExperimentId:"
- "setExperimentalAssets:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFd:"
- "setIdentifier:"
- "setIgnoreOSCompatibility:"
- "setImmediateDownloadTriggered:"
- "setInstanceUUID:"
- "setInternalProgressCompletion:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setLatestAtomicInstance:autoAssetSet:fallbackAlter:atomicInstanceMetadata:"
- "setLocale:"
- "setMaStartupNotifyToken:"
- "setMaxOSVersion:"
- "setMaxProgressBeforeComplete:"
- "setMetadataAsset:"
- "setMinOSVersion:"
- "setMinVersions:"
- "setMinimalSpecifiers:"
- "setName:"
- "setNetworkExpensive:"
- "setNetworkSatisfied:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOriginatingURL:"
- "setPending:"
- "setPreinstalledAssetsSummary:"
- "setProgressWithStatus:"
- "setProgresses:"
- "setRefCount:"
- "setRemoteObjectInterface:"
- "setRemovedSelectors:"
- "setReportedComplete:"
- "setReportedCompletedWork:"
- "setReportedPercent:"
- "setReportedStatus:"
- "setReportedTotal:"
- "setReportedTotalWork:"
- "setRequiredUsageTypes:"
- "setRetryCount:"
- "setRetryState:"
- "setShowHybridAsUnsupported:"
- "setSiriLanguage:"
- "setSourceType:"
- "setState:"
- "setStatusGroup:"
- "setStatusQueue:"
- "setStatuses:"
- "setSubjectToAppleIntelligenceWaitlist:"
- "setSubscriptions:"
- "setSupportingShortTermLocks:"
- "setSystemConfigurationForKey:withValue:"
- "setSystemConfigurationForKey:withValue:completion:"
- "setThirdPartyCompatibilityVersion:"
- "setTimeZone:"
- "setTotal:"
- "setTotalWork:"
- "setTrialFactor:"
- "setTrialNamespace:"
- "setTrialProject:"
- "setUAFPallasURL:assetSet:"
- "setUAFPopulation:"
- "setUAFPopulation:assetSet:"
- "setUAFPopulation:url:"
- "setUAFPopulation:url:assetSet:"
- "setUAFPopulationForAssetType:forType:withURL:"
- "setUafNotifyToken:"
- "setUnderstandingOnDeviceAssetsAvailable:"
- "setUodAvailable:"
- "setUpdateHandler:"
- "setUpdateIsFinished:"
- "setUsageLimits:"
- "setUsageTypes:"
- "setUsageValues:"
- "setUserInitiated:"
- "setUserLastSeenTime:node:time:"
- "setUuid:"
- "setValue:"
- "setValue:forKey:"
- "setValues:"
- "setWithArray:"
- "setWithObject:"
- "setWithObjects:"
- "setWithSet:"
- "sharedDefaultEvaluator"
- "sharedManager"
- "sharedPreferences"
- "sharedStream"
- "shortTermLockFileName"
- "shouldCheckAssetSet:autoAssetSet:changed:downloaded:experiment:locked:userInitiated:removalNeeded:"
- "shouldWaitForMobileAssetStart:"
- "showHybridAsUnsupported"
- "signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:"
- "simulatorResourcesDirectory"
- "siriLanguage"
- "siriUODAvailabilityDidChange:"
- "siriUODStatusDidChange"
- "sizeInBytesForConfig:key:error:"
- "snapshotWithSignature:delay:events:payload:actions:reply:"
- "softlink:o:path:/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels"
- "softlink:r:path:/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices"
- "softlink:r:path:/System/Library/PrivateFrameworks/MorphunAssets.framework/MorphunAssets"
- "source"
- "sourceType"
- "spaceNeededForAssetSetUsages:key:configurationManager:error:"
- "specializeTemplate:usages:"
- "specializeTemplate:usages:invalid:error:"
- "stageAssetSet:targets:platformAssetVersion:"
- "stageAssetsWithNewSubscriptions:oldSubscriptions:autoAssetSets:"
- "standardUserDefaults"
- "start"
- "startAsync"
- "startObserver"
- "startObservers"
- "startObserversWithOptions:"
- "started:"
- "stat:withBuf:error:"
- "status"
- "statusGroup"
- "statusQueue"
- "stop"
- "stopAsync"
- "stored"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringByDeletingLastPathComponent"
- "stringByDeletingPathExtension"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringForKey:"
- "stringFromDate:"
- "stringFromDate:timeZone:formatOptions:"
- "stringFromUAFAssetState:"
- "stringValue"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "subjectToAppleIntelligenceWaitlist"
- "subscribe:subscriptions:queue:completion:"
- "subscribe:subscriptions:user:node:"
- "subscribe:subscriptions:user:storeManager:configurationManager:userInitiated:"
- "subscribe:subscriptions:user:userInitiated:queue:completion:"
- "subscribeWithConfig:userInitiated:completion:"
- "subscribedUsagesForAssetSet:"
- "subscriptions"
- "subscriptions:"
- "subscriptions:subscriber:user:completion:"
- "subscriptions:subscriber:user:storeManager:error:"
- "subscriptionsForSubscriber:"
- "substringFromIndex:"
- "substringToIndex:"
- "substringWithRange:"
- "summarize"
- "summary"
- "summary:"
- "superclass"
- "supportedFileVersions"
- "supportsSecureCoding"
- "suspend"
- "switchLanguage:"
- "synchronize"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "sysdiagnoseInformationWithError:"
- "system.language"
- "system.locale"
- "systemLanguage"
- "systemTimeZone"
- "systemUserWithNode:error:"
- "targetForAssetSet:specifiers:version:autoAssetSets:"
- "thirdPartyCompatibilityVersion"
- "timeIntervalSince1970"
- "timeIntervalSinceDate:"
- "timeZoneWithAbbreviation:"
- "tokenDir:"
- "tokenFilename:"
- "total"
- "totalBytes"
- "totalExpectedBytes"
- "totalWork"
- "totalWrittenBytes"
- "trialClientWithProject:"
- "trialFactor"
- "trialNamespace"
- "trialProject"
- "uafNotifyToken"
- "uid"
- "uidForUser:error:"
- "umCurrentUMUserWithNode:error:"
- "umEntitlementPresent"
- "umNameForUser:error:"
- "umNodeForUser:error:"
- "umUserWithDSID:withUid:withError:"
- "umUserWithNodeForUID:uid:error:"
- "unarchiveToken:error:"
- "unarchivedObjectOfClass:fromData:error:"
- "unarchivedObjectOfClasses:fromData:error:"
- "understandingOnDeviceAssetsAvailable"
- "unlock:"
- "unlockableTokenError"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "unsubscribe:subscriptionNames:queue:completion:"
- "unsubscribe:subscriptionNames:user:userInitiated:queue:completion:"
- "unsubscribe:subscriptions:user:node:"
- "unsubscribe:subscriptions:user:storeManager:configurationManager:userInitiated:"
- "unsubscribeWithConfig:userInitiated:completion:"
- "uodAvailable"
- "updateAssetState:value:forLanguage:"
- "updateAssetsForSubscriber:subscriptionName:policies:queue:detailedProgress:completion:"
- "updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:"
- "updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:"
- "updateAssetsForSubscribers:policies:queue:detailedProgress:completion:"
- "updateAssetsForSubscribers:policies:queue:progress:detailedProgress:internalProgress:completion:storeManager:configurationManager:"
- "updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:requestId:completion:"
- "updateCount"
- "updateFinished:"
- "updateHandler"
- "updateIsFinished"
- "updateLastSeenForCurrentUserOnQueue:completion:"
- "updateLastSeenForUser:queue:completion:"
- "updateSiriAssetAvailabilityForLanguage:"
- "updateSiriAssetAvailabilityForLanguageSync:"
- "updateSiriAssetAvailabilityForObserver"
- "updateSystemAssetSetUsages:"
- "updateSystemAssetSetUsages:configurationManager:"
- "uppercaseString"
- "urlForGestalt:"
- "usageLimits"
- "usageTypes"
- "usageValues"
- "usages"
- "userInfo"
- "userInitiated"
- "userIsValidForAssetSetManagement:"
- "userWithNodeForUID:uid:error:"
- "username"
- "v16@0:8"
- "v16@?0@\"NSObject<OS_nw_path>\"8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8^v16"
- "v24@0:8d16"
- "v24@?0@\"NSNumber\"8@\"NSError\"16"
- "v24@?0@\"UAFAssetStatus\"8@\"NSError\"16"
- "v24@?0d8Q16"
- "v28@0:8@16B24"
- "v28@0:8B16@20"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16B24I28"
- "v32@0:8@16Q24"
- "v32@0:8Q16@24"
- "v32@0:8^I16^I24"
- "v36@0:8@16@24B32"
- "v36@0:8@16B24@?28"
- "v36@0:8B16@20@28"
- "v36@0:8B16@20Q28"
- "v36@0:8Q16Q24B32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24q32"
- "v40@0:8@16Q24@32"
- "v40@0:8@16Q24@?32"
- "v40@0:8Q16@24@32"
- "v40@0:8Q16Q24@32"
- "v44@0:8@16@24B32@36"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSError\">40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24@32B40B44"
- "v48@0:8@16@24@32Q40"
- "v48@0:8@16Q24@32@40"
- "v52@0:8@16@24@32B40@44"
- "v52@0:8@16Q24@32@40B48"
- "v56@0:8@16@24@32@40@48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24@32@40Q48"
- "v56@0:8@16@24@32@?40@?48"
- "v56@0:8@16@24@32^@40^@48"
- "v56@0:8@16@24B32@36@44B52"
- "v56@0:8@16Q24Q32Q40@48"
- "v60@0:8@16@24@32B40@44@?52"
- "v60@0:8@16@24B32@?36@44@?52"
- "v60@0:8B16@20@28@36@44@?52"
- "v64@0:8@16@24@32@40@?48@?56"
- "v64@0:8@16@24@32I40@44Q52B60"
- "v88@0:8@16@24@32@40@?48@?56@?64@72@80"
- "v88@0:8@16@24@32@?40@?48@?56@?64@72@80"
- "valid"
- "validLocalNode"
- "validLocalUsers:error:"
- "validNodesWithError:"
- "validProgressTypes"
- "validatePopulation:resolvedPopulation:isNamedString:isDefault:"
- "validateUsageAlias:usageAliasValue:"
- "validation-assets"
- "valueForEntitlement:"
- "values"
- "versionComponentFromString:"
- "versionComponentsFromString:"
- "waitForMobileAssetStart:queue:completion:"
- "wasPreinstalled"
- "writeData:error:"
- "writeManager"
- "writeToFile:content:"
- "writeToURL:options:error:"
- "zone"

```
