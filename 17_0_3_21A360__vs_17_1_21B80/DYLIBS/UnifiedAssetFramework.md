## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3300.113.2.0.0
-  __TEXT.__text: 0x3feec
-  __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x1e8c
-  __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x5d8
-  __TEXT.__cstring: 0x65ab
-  __TEXT.__oslogstring: 0x6d77
+3301.9.1.0.0
+  __TEXT.__text: 0x4b440
+  __TEXT.__auth_stubs: 0x9e0
+  __TEXT.__objc_methlist: 0x25a8
+  __TEXT.__const: 0x90
+  __TEXT.__gcc_except_tab: 0x63c
+  __TEXT.__cstring: 0x70d8
+  __TEXT.__oslogstring: 0x88b5
   __TEXT.__dlopen_cstrs: 0x290
-  __TEXT.__unwind_info: 0xaac
-  __TEXT.__objc_classname: 0x2d7
-  __TEXT.__objc_methname: 0x66e0
-  __TEXT.__objc_methtype: 0xaf2
-  __TEXT.__objc_stubs: 0x56c0
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x12d8
-  __DATA_CONST.__objc_classlist: 0xe8
+  __TEXT.__unwind_info: 0xc40
+  __TEXT.__objc_classname: 0x324
+  __TEXT.__objc_methname: 0x78d1
+  __TEXT.__objc_methtype: 0xbb1
+  __TEXT.__objc_stubs: 0x6460
+  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__const: 0x13c0
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2318
-  __DATA_CONST.__objc_selrefs: 0x1998
+  __DATA_CONST.__objc_const: 0x2730
+  __DATA_CONST.__objc_selrefs: 0x1df0
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__cfstring: 0x28e0
+  __AUTH_CONST.__cfstring: 0x2e20
   __AUTH_CONST.__objc_intobj: 0x228
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__objc_const: 0x240
+  __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x4d0
+  __AUTH_CONST.__auth_got: 0x500
+  __AUTH.__objc_data: 0x140
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x2f0
-  __DATA.__objc_superrefs: 0x90
-  __DATA.__objc_ivar: 0x240
+  __DATA.__objc_classrefs: 0x318
+  __DATA.__objc_superrefs: 0xb0
+  __DATA.__objc_ivar: 0x28c
   __DATA.__data: 0x208
   __DATA.__bss: 0x8
   __DATA_DIRTY.__const: 0x420
   __DATA_DIRTY.__objc_const: 0xc58
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__common: 0x48
-  __DATA_DIRTY.__bss: 0x250
+  __DATA_DIRTY.__bss: 0x290
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 900
-  Symbols:   3458
-  CStrings:  2336
+  Functions: 1055
+  Symbols:   3968
+  CStrings:  2694
 
Symbols:
+ +[UAFAssetSet autoAssetSet:usages:]
+ +[UAFAssetSetConfiguration fromContentsOfURL:applyFeatureFlags:error:]
+ +[UAFAssetSetManager sharedManager]
+ +[UAFAssetSetObserver listenForUAFNotificationsForAssetSet:forRoot:queue:updateHandler:]
+ +[UAFAssetSetObserver notificationForAssetSet:forRoot:]
+ +[UAFAssetSetObserver sendUAFNotificationForAssetSet:forRoot:]
+ +[UAFAutoAssetInstance autoAssetEntryToAsset:withAssetName:]
+ +[UAFAutoAssetInstance clear:path:]
+ +[UAFAutoAssetInstance decomposeSaveFileURL:assetSetName:atomicInstance:]
+ +[UAFAutoAssetInstance instanceDirURL]
+ +[UAFAutoAssetInstance instanceFileURL:atomicInstance:]
+ +[UAFAutoAssetInstance loadInstanceWithAssetSetName:]
+ +[UAFAutoAssetInstance loadInstanceWithURL:]
+ +[UAFAutoAssetInstance removeInstanceWithAssetSetName:atomicInstance:]
+ +[UAFAutoAssetInstance saveFileURL:]
+ +[UAFAutoAssetInstance setFileURL:]
+ +[UAFAutoAssetInstance validateAllInstances]
+ +[UAFAutoAssetManager configureAssetSet:specifiers:changed:]
+ +[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:]
+ +[UAFAutoAssetManager handleDownloadedAndUnavailable:specifiers:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:]
+ +[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:]
+ +[UAFAutoAssetManager listenForUpdates:updateHandler:]
+ +[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:eliminateAndRetry:]
+ +[UAFAutoAssetManager removeUnusedAutoAssetSets:usedAutoAssetSets:]
+ +[UAFAutoAssetManager sendNotificationForAssetSet:]
+ +[UAFAutoAssetManager stageAssetSet:targets:]
+ +[UAFAutoAssetManager stageAssetsWithSubscriptions:knownAutoAssetSets:usedAutoAssetSets:]
+ +[UAFAutoAssetManager targetForAssetSet:specifiers:version:]
+ +[UAFAutoAssetPromotion _loadPromotionWithAssetSetName:]
+ +[UAFAutoAssetPromotion buildVersionFromLockReason:]
+ +[UAFAutoAssetPromotion buildVersion]
+ +[UAFAutoAssetPromotion cacheDirURL]
+ +[UAFAutoAssetPromotion clear]
+ +[UAFAutoAssetPromotion getFormReason:atomicInstance:]
+ +[UAFAutoAssetPromotion getLockReason:]
+ +[UAFAutoAssetPromotion loadPromotionWithAssetSetName:]
+ +[UAFAutoAssetPromotion loadPromotionWithAssetSetName:latestAtomicInstance:]
+ +[UAFAutoAssetPromotion lockPrefix]
+ +[UAFAutoAssetPromotion lockReasonFromPromotion:]
+ +[UAFAutoAssetPromotion lockReasonValid:]
+ +[UAFAutoAssetPromotion saveFileURL:]
+ +[UAFAutoAssetSet getClientName]
+ +[UAFAutoAssetSet getConcurrentQueue]
+ +[UAFAutoAssetSet getLockReason:]
+ +[UAFCommonUtilities _eliminateAutoAssetSet:]
+ +[UAFCommonUtilities _getPopulationMapping:toAudience:toServer:]
+ +[UAFCommonUtilities _resetAutoAssetSets:]
+ +[UAFCommonUtilities getUAFPallasURLForAssetSet:]
+ +[UAFCommonUtilities getUAFPallasURLForAssetType:]
+ +[UAFCommonUtilities getUAFPopulationForAssetSet:]
+ +[UAFCommonUtilities getUAFPopulationForAssetType:]
+ +[UAFCommonUtilities setUAFPallasURL:assetSet:]
+ +[UAFCommonUtilities setUAFPopulation:assetSet:]
+ +[UAFInstrumentationProvider logUAFAssetSetDailyStatus:]
+ +[UAFManagedSubscriptions getConcurrentQueue]
+ +[UAFManagedSubscriptions managePlatformSubscription]
+ +[UAFPlatform configurationManagers:]
+ +[UAFPlatform maxVersionFromVersionString:]
+ +[UAFPlatform versionComponentFromString:]
+ +[UAFPlatform versionComponentsFromString:]
+ +[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]
+ +[UAFTrialUpdateManager updateTrialFromAssetSetUsages:rolloutUpdateMode:expensiveNetworking:storeManager:configurationManager:progress:completion:]
+ -[UAFAssetSet assetNamed:]
+ -[UAFAssetSet assetNamed:withUsage:]
+ -[UAFAssetSet assets]
+ -[UAFAssetSet autoAssetSet]
+ -[UAFAssetSet markAssetsPromoted:error:]
+ -[UAFAssetSet markAssetsProvisional:error:]
+ -[UAFAssetSet setAutoAssetSet:]
+ -[UAFAssetSetConfiguration applyFeatureFlags]
+ -[UAFAssetSetConfiguration getAssets:]
+ -[UAFAssetSetConfiguration isTrialAvailable]
+ -[UAFAssetSetConfiguration setIsTrialAvailable:]
+ -[UAFAssetSetManager .cxx_destruct]
+ -[UAFAssetSetManager assetSetObservers]
+ -[UAFAssetSetManager configurationManager]
+ -[UAFAssetSetManager downloadStatusForSubscriber:subscriptionName:]
+ -[UAFAssetSetManager init]
+ -[UAFAssetSetManager knownUsagesForAssetSet:usageType:]
+ -[UAFAssetSetManager observeAssetSet:queue:handler:]
+ -[UAFAssetSetManager removeObserver:]
+ -[UAFAssetSetManager retrieveAssetSet:usages:]
+ -[UAFAssetSetManager setAssetSetObservers:]
+ -[UAFAssetSetManager setConfigurationManager:]
+ -[UAFAssetSetManager setSubscriptionStoreManager:]
+ -[UAFAssetSetManager subscribe:subscriptions:queue:completion:]
+ -[UAFAssetSetManager subscribedUsagesForAssetSet:]
+ -[UAFAssetSetManager subscriptionStoreManager]
+ -[UAFAssetSetManager subscriptionsForSubscriber:]
+ -[UAFAssetSetManager unsubscribe:subscriptionNames:queue:completion:]
+ -[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:]
+ -[UAFAssetSetObserver rootNotifyToken]
+ -[UAFAssetSetObserver setRootNotifyToken:]
+ -[UAFAssetSetSubscription initWithName:assetSets:usageAliases:]
+ -[UAFAssetSetSubscription initWithName:assetSets:usageAliases:expires:]
+ -[UAFAssetUtilitiesService _downloadSiriAssetsWithCellular:]
+ -[UAFAutoAssetInstance .cxx_destruct]
+ -[UAFAutoAssetInstance assetSetName]
+ -[UAFAutoAssetInstance assetsFromSpecifiers:]
+ -[UAFAutoAssetInstance assets]
+ -[UAFAutoAssetInstance atomicInstance]
+ -[UAFAutoAssetInstance dealloc]
+ -[UAFAutoAssetInstance encodeToDictionary]
+ -[UAFAutoAssetInstance initWithAssetSetName:atomicInstance:entries:]
+ -[UAFAutoAssetInstance initWithDictionary:]
+ -[UAFAutoAssetInstance isValid]
+ -[UAFAutoAssetInstance lockFileFD]
+ -[UAFAutoAssetInstance lockForLoading]
+ -[UAFAutoAssetInstance lockForRemoval]
+ -[UAFAutoAssetInstance setAssetSetName:]
+ -[UAFAutoAssetInstance setAssets:]
+ -[UAFAutoAssetInstance setAtomicInstance:]
+ -[UAFAutoAssetInstance setLatest:]
+ -[UAFAutoAssetInstance setLockFileFD:]
+ -[UAFAutoAssetInstance unlock]
+ -[UAFAutoAssetPromotion .cxx_destruct]
+ -[UAFAutoAssetPromotion assetSetName]
+ -[UAFAutoAssetPromotion buildVersion]
+ -[UAFAutoAssetPromotion clear]
+ -[UAFAutoAssetPromotion encodeToDictionary]
+ -[UAFAutoAssetPromotion initWithAssetSetName:]
+ -[UAFAutoAssetPromotion initWithDictionary:]
+ -[UAFAutoAssetPromotion instanceForSpecifier:]
+ -[UAFAutoAssetPromotion latestAtomicInstance]
+ -[UAFAutoAssetPromotion latestPromotedSpecifiers]
+ -[UAFAutoAssetPromotion latestProvisionalSpecifiers]
+ -[UAFAutoAssetPromotion markSpecifiersPromoted:assetType:autoAssetSet:atomicInstance:error:]
+ -[UAFAutoAssetPromotion markSpecifiersProvisional:atomicInstance:error:]
+ -[UAFAutoAssetPromotion promotedSpecifiers]
+ -[UAFAutoAssetPromotion save:]
+ -[UAFAutoAssetPromotion setAssetSetName:]
+ -[UAFAutoAssetPromotion setBuildVersion:]
+ -[UAFAutoAssetPromotion setLatestAtomicInstance:]
+ -[UAFAutoAssetPromotion setLatestPromotedSpecifiers:]
+ -[UAFAutoAssetPromotion setLatestProvisionalSpecifiers:]
+ -[UAFAutoAssetPromotion setPromotedSpecifiers:]
+ -[UAFAutoAssetSet .cxx_destruct]
+ -[UAFAutoAssetSet addAtomicInstance:]
+ -[UAFAutoAssetSet assetSetName]
+ -[UAFAutoAssetSet assetWithName:]
+ -[UAFAutoAssetSet assets]
+ -[UAFAutoAssetSet atomicInstances]
+ -[UAFAutoAssetSet autoAssetSet]
+ -[UAFAutoAssetSet availableForUseError:newerVersionError:]
+ -[UAFAutoAssetSet catalogAssetSetID]
+ -[UAFAutoAssetSet dealloc]
+ -[UAFAutoAssetSet getMAAutoAssetDownloadErrorsSync]
+ -[UAFAutoAssetSet initWithAssetSetName:autoAssets:]
+ -[UAFAutoAssetSet instance]
+ -[UAFAutoAssetSet latestAtomicInstance]
+ -[UAFAutoAssetSet lockAtomicInstance:specifierToAssetName:]
+ -[UAFAutoAssetSet lockAutoAssets:]
+ -[UAFAutoAssetSet lockLatestAtomicInstance:]
+ -[UAFAutoAssetSet markAssetsPromoted:error:]
+ -[UAFAutoAssetSet markAssetsProvisional:error:]
+ -[UAFAutoAssetSet setAssetSetName:]
+ -[UAFAutoAssetSet setAssets:]
+ -[UAFAutoAssetSet setAtomicInstances:]
+ -[UAFAutoAssetSet setAutoAssetSet:]
+ -[UAFAutoAssetSet setInstance:]
+ -[UAFAutoAssetSet setLatestAtomicInstance:]
+ -[UAFAutoAssetSet setUnpromotableAssets:]
+ -[UAFAutoAssetSet unpromotableAssets]
+ -[UAFConfigurationManager shouldApplyFeatureFlags]
+ -[UAFSubscriptionStoreManager updateSystemAssetSetUsages:configurationManager:]
+ -[UAFUsageAliasConfiguration getAssetSetAssets:usageValue:withSource:]
+ -[UAFUsageAliasConfiguration getAssets:]
+ -[UAFUsageAliasConfiguration getAssets:withSource:]
+ -[UAFUsageAliasConfiguration getAutoAssets:]
+ GCC_except_table12
+ GCC_except_table13
+ GCC_except_table34
+ GCC_except_table56
+ _MGCopyAnswer
+ _NSCocoaErrorDomain
+ _NSURLIsDirectoryKey
+ _OBJC_CLASS_$_MAAutoAssetSetTarget
+ _OBJC_CLASS_$_UAFAutoAssetInstance
+ _OBJC_CLASS_$_UAFAutoAssetPromotion
+ _OBJC_CLASS_$_UAFAutoAssetSet
+ _OBJC_CLASS_$_UAFPlatform
+ _OBJC_IVAR_$_UAFAssetSetConfiguration._isTrialAvailable
+ _OBJC_IVAR_$_UAFAssetSetManager._assetSetObservers
+ _OBJC_IVAR_$_UAFAssetSetManager._configurationManager
+ _OBJC_IVAR_$_UAFAssetSetManager._subscriptionStoreManager
+ _OBJC_IVAR_$_UAFAssetSetObserver._rootNotifyToken
+ _OBJC_IVAR_$_UAFAutoAssetInstance._assetSetName
+ _OBJC_IVAR_$_UAFAutoAssetInstance._assets
+ _OBJC_IVAR_$_UAFAutoAssetInstance._atomicInstance
+ _OBJC_IVAR_$_UAFAutoAssetInstance._lockFileFD
+ _OBJC_IVAR_$_UAFAutoAssetPromotion._assetSetName
+ _OBJC_IVAR_$_UAFAutoAssetPromotion._buildVersion
+ _OBJC_IVAR_$_UAFAutoAssetPromotion._latestAtomicInstance
+ _OBJC_IVAR_$_UAFAutoAssetPromotion._latestPromotedSpecifiers
+ _OBJC_IVAR_$_UAFAutoAssetPromotion._latestProvisionalSpecifiers
+ _OBJC_IVAR_$_UAFAutoAssetPromotion._promotedSpecifiers
+ _OBJC_IVAR_$_UAFAutoAssetSet._assetSetName
+ _OBJC_IVAR_$_UAFAutoAssetSet._assets
+ _OBJC_IVAR_$_UAFAutoAssetSet._atomicInstances
+ _OBJC_IVAR_$_UAFAutoAssetSet._autoAssetSet
+ _OBJC_IVAR_$_UAFAutoAssetSet._instance
+ _OBJC_IVAR_$_UAFAutoAssetSet._latestAtomicInstance
+ _OBJC_IVAR_$_UAFAutoAssetSet._unpromotableAssets
+ _OBJC_METACLASS_$_UAFAutoAssetInstance
+ _OBJC_METACLASS_$_UAFAutoAssetPromotion
+ _OBJC_METACLASS_$_UAFAutoAssetSet
+ _OBJC_METACLASS_$_UAFPlatform
+ _UAFSubscriptionDownloadStatusDescription
+ __OBJC_$_CLASS_METHODS_UAFAutoAssetInstance
+ __OBJC_$_CLASS_METHODS_UAFAutoAssetPromotion
+ __OBJC_$_CLASS_METHODS_UAFAutoAssetSet
+ __OBJC_$_CLASS_METHODS_UAFPlatform
+ __OBJC_$_CLASS_PROP_LIST_UAFAssetSetManager
+ __OBJC_$_INSTANCE_METHODS_UAFAssetSetManager
+ __OBJC_$_INSTANCE_METHODS_UAFAutoAssetInstance
+ __OBJC_$_INSTANCE_METHODS_UAFAutoAssetPromotion
+ __OBJC_$_INSTANCE_METHODS_UAFAutoAssetSet
+ __OBJC_$_INSTANCE_VARIABLES_UAFAssetSetManager
+ __OBJC_$_INSTANCE_VARIABLES_UAFAutoAssetInstance
+ __OBJC_$_INSTANCE_VARIABLES_UAFAutoAssetPromotion
+ __OBJC_$_INSTANCE_VARIABLES_UAFAutoAssetSet
+ __OBJC_$_PROP_LIST_UAFAssetSetManager
+ __OBJC_$_PROP_LIST_UAFAutoAssetInstance
+ __OBJC_$_PROP_LIST_UAFAutoAssetPromotion
+ __OBJC_$_PROP_LIST_UAFAutoAssetSet
+ __OBJC_CLASS_RO_$_UAFAutoAssetInstance
+ __OBJC_CLASS_RO_$_UAFAutoAssetPromotion
+ __OBJC_CLASS_RO_$_UAFAutoAssetSet
+ __OBJC_CLASS_RO_$_UAFPlatform
+ __OBJC_METACLASS_RO_$_UAFAutoAssetInstance
+ __OBJC_METACLASS_RO_$_UAFAutoAssetPromotion
+ __OBJC_METACLASS_RO_$_UAFAutoAssetSet
+ __OBJC_METACLASS_RO_$_UAFPlatform
+ ___100-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:]_block_invoke
+ ___112+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:]_block_invoke
+ ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.286
+ ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.287
+ ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.288
+ ___134+[UAFAutoAssetManager handleDownloadedAndUnavailable:specifiers:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:]_block_invoke
+ ___147+[UAFTrialUpdateManager updateTrialFromAssetSetUsages:rolloutUpdateMode:expensiveNetworking:storeManager:configurationManager:progress:completion:]_block_invoke
+ ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke
+ ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke.249
+ ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_2
+ ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_2.250
+ ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_3
+ ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_4
+ ___21-[UAFAssetSet assets]_block_invoke
+ ___26-[UAFAssetSet assetNamed:]_block_invoke
+ ___26-[UAFAutoAssetSet dealloc]_block_invoke
+ ___31-[UAFAutoAssetInstance isValid]_block_invoke
+ ___35+[UAFAssetSetManager sharedManager]_block_invoke
+ ___37+[UAFAutoAssetPromotion buildVersion]_block_invoke
+ ___37+[UAFAutoAssetSet getConcurrentQueue]_block_invoke
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.271
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.272
+ ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.261
+ ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.262
+ ___44-[UAFAutoAssetSet lockLatestAtomicInstance:]_block_invoke
+ ___44-[UAFAutoAssetSet lockLatestAtomicInstance:]_block_invoke_2
+ ___45+[UAFManagedSubscriptions getConcurrentQueue]_block_invoke
+ ___53+[UAFManagedSubscriptions managePlatformSubscription]_block_invoke
+ ___54+[UAFAutoAssetManager listenForUpdates:updateHandler:]_block_invoke
+ ___60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke.254
+ ___60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke.258
+ ___60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke.259
+ ___60-[UAFAssetUtilitiesService _downloadSiriAssetsWithCellular:]_block_invoke
+ ___63+[UAFAssetSetManager subscribe:subscriptions:queue:completion:]_block_invoke.227
+ ___65+[UAFAssetSetManager unsubscribe:subscriptions:queue:completion:]_block_invoke.229
+ ___70+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:]_block_invoke
+ ___70+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:]_block_invoke.252
+ ___70+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:]_block_invoke_2
+ ___79-[UAFSubscriptionStoreManager updateSystemAssetSetUsages:configurationManager:]_block_invoke
+ ___83+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:eliminateAndRetry:]_block_invoke
+ ___88+[UAFAssetSetObserver listenForUAFNotificationsForAssetSet:forRoot:queue:updateHandler:]_block_invoke
+ ___90-[UAFAssetSetObserver initWithAssetSet:configurationDirURLs:queue:updateHandler:delegate:]_block_invoke.228
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0i8ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_i8?0lr48l8s32l8r56l8s40l8
+ ___block_descriptor_66_e8_32s40s48s56s_e42_v32?0"NSString"8"NSArray"16"NSError"24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_73_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e42_v32?0"NSString"8"NSArray"16"NSError"24ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_81_e8_32s40s48s56bs64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.220
+ ___block_literal_global.224
+ ___block_literal_global.235
+ ___block_literal_global.256
+ ___block_literal_global.269
+ ___block_literal_global.270
+ ___block_literal_global.307
+ _close
+ _kUAFAssetMetadataAssetSpecifierKey
+ _kUAFAssetSetNotificationRootSuffix
+ _kUAFAutoAssetSpecifier
+ _kUAFAutoAssetStageReason
+ _kUAFAutoAssetUnblockReason
+ _kUAFDir
+ _kUAFExtension
+ _kUAFInstanceExtension
+ _kUAFPlatformAssetSet
+ _kUAFPlatformOSUpdates
+ _kUAFPlatformSubscriber
+ _kUAFPlatformSubscription
+ _kUAFPolicyForceUpdateNamespaces
+ _kUAFPromotionDir
+ _kUAFPromotionMaxProvisionalCount
+ _kUAFPromotionReasonPrefix
+ _kUAFPromotionReasonSeparator
+ _objc_msgSend$URLByAppendingPathComponent:isDirectory:
+ _objc_msgSend$URLByStandardizingPath
+ _objc_msgSend$URLForDirectory:inDomain:appropriateForURL:create:error:
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$_downloadSiriAssetsWithCellular:
+ _objc_msgSend$_eliminateAutoAssetSet:
+ _objc_msgSend$_getPopulationMapping:toAudience:toServer:
+ _objc_msgSend$_loadPromotionWithAssetSetName:
+ _objc_msgSend$_resetAutoAssetSets:
+ _objc_msgSend$addAtomicInstance:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$alterEntriesRepresentingAtomicSync:toBeComprisedOfEntries:withNeedPolicy:
+ _objc_msgSend$applyFeatureFlags
+ _objc_msgSend$assetNamed:
+ _objc_msgSend$assetNamed:withUsage:
+ _objc_msgSend$assetSetForStagingSync:asEntriesWhenTargeting:
+ _objc_msgSend$assetSetName
+ _objc_msgSend$assetWithName:
+ _objc_msgSend$assetsFromSpecifiers:
+ _objc_msgSend$atomicInstance
+ _objc_msgSend$autoAssetEntryToAsset:withAssetName:
+ _objc_msgSend$autoAssetSet
+ _objc_msgSend$autoAssetSet:usages:
+ _objc_msgSend$blockCheckDownload
+ _objc_msgSend$buildVersion
+ _objc_msgSend$buildVersionFromLockReason:
+ _objc_msgSend$cacheDirURL
+ _objc_msgSend$catalogAssetSetID
+ _objc_msgSend$checkAtomic:forAtomicInstance:withTimeout:completion:
+ _objc_msgSend$clear
+ _objc_msgSend$clear:path:
+ _objc_msgSend$configurationManagers:
+ _objc_msgSend$configureAssetSet:specifiers:changed:
+ _objc_msgSend$configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$decimalDigitCharacterSet
+ _objc_msgSend$decomposeSaveFileURL:assetSetName:atomicInstance:
+ _objc_msgSend$downloadStatus:subscription:
+ _objc_msgSend$encodeToDictionary
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$formSubAtomicInstanceSync:fromAtomicInstance:toBeComprisedOfEntries:error:
+ _objc_msgSend$fromContentsOfURL:applyFeatureFlags:error:
+ _objc_msgSend$getAssetSetAssets:usageValue:withSource:
+ _objc_msgSend$getAssetSetUsages:
+ _objc_msgSend$getAssets:
+ _objc_msgSend$getAssets:withSource:
+ _objc_msgSend$getClientName
+ _objc_msgSend$getFormReason:atomicInstance:
+ _objc_msgSend$getKnownUsagesForAssetSet:usageType:
+ _objc_msgSend$getLockReason:
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$getUAFPallasURLForAssetType:
+ _objc_msgSend$getUAFPopulationForAssetType:
+ _objc_msgSend$handleDownloadedAndUnavailable:specifiers:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:
+ _objc_msgSend$initForMinTargetOSVersion:toMaxTargetOSVersion:asEntriesWhenTargeting:
+ _objc_msgSend$initWithAssetSetName:
+ _objc_msgSend$initWithAssetSetName:atomicInstance:entries:
+ _objc_msgSend$initWithAssetSetName:autoAssets:
+ _objc_msgSend$initWithName:assetSets:usageAliases:
+ _objc_msgSend$initWithName:assetSets:usageAliases:expires:
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$instance
+ _objc_msgSend$instanceDirURL
+ _objc_msgSend$instanceFileURL:atomicInstance:
+ _objc_msgSend$instanceForSpecifier:
+ _objc_msgSend$invalidatePromotedInstances:autoAssetSet:group:
+ _objc_msgSend$invertedSet
+ _objc_msgSend$isEqualToDictionary:
+ _objc_msgSend$isTrialAvailable
+ _objc_msgSend$isValid
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$latestAtomicInstance
+ _objc_msgSend$latestDowloadedAtomicInstanceEntries
+ _objc_msgSend$latestPromotedSpecifiers
+ _objc_msgSend$latestProvisionalSpecifiers
+ _objc_msgSend$linkItemAtURL:toURL:error:
+ _objc_msgSend$listenForUAFNotificationsForAssetSet:forRoot:queue:updateHandler:
+ _objc_msgSend$listenForUpdates:updateHandler:
+ _objc_msgSend$loadInstanceWithAssetSetName:
+ _objc_msgSend$loadInstanceWithURL:
+ _objc_msgSend$loadPromotionWithAssetSetName:
+ _objc_msgSend$loadPromotionWithAssetSetName:latestAtomicInstance:
+ _objc_msgSend$lockAtomicInstance:specifierToAssetName:
+ _objc_msgSend$lockAutoAssets:
+ _objc_msgSend$lockForLoading
+ _objc_msgSend$lockForRemoval
+ _objc_msgSend$lockLatestAtomicInstance:
+ _objc_msgSend$lockPrefix
+ _objc_msgSend$lockReasonFromPromotion:
+ _objc_msgSend$lockReasonValid:
+ _objc_msgSend$logUAFAssetSetDailyStatus:
+ _objc_msgSend$manageAssetSet:specifiers:lockIfUnchanged:eliminateAndRetry:
+ _objc_msgSend$managePlatformSubscription
+ _objc_msgSend$markAssetsPromoted:error:
+ _objc_msgSend$markAssetsProvisional:error:
+ _objc_msgSend$markSpecifiersPromoted:assetType:autoAssetSet:atomicInstance:error:
+ _objc_msgSend$markSpecifiersProvisional:atomicInstance:error:
+ _objc_msgSend$maxTargetOSVersion
+ _objc_msgSend$maxVersionFromVersionString:
+ _objc_msgSend$minTargetOSVersion
+ _objc_msgSend$needForAtomicSync:
+ _objc_msgSend$notificationForAssetSet:forRoot:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$observeAssetSet:queue:handler:
+ _objc_msgSend$promotedSpecifiers
+ _objc_msgSend$rangeOfString:options:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeInstanceWithAssetSetName:atomicInstance:
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$removeUnusedAutoAssetSets:usedAutoAssetSets:
+ _objc_msgSend$retrieveAssetSet:usages:
+ _objc_msgSend$save:
+ _objc_msgSend$saveFileURL:
+ _objc_msgSend$schedulerPolicy
+ _objc_msgSend$sendUAFNotificationForAssetSet:forRoot:
+ _objc_msgSend$setFileURL:
+ _objc_msgSend$setInstance:
+ _objc_msgSend$setLatest:
+ _objc_msgSend$sharedManager
+ _objc_msgSend$shouldApplyFeatureFlags
+ _objc_msgSend$stageAssetSet:targets:
+ _objc_msgSend$stageAssetsWithSubscriptions:knownAutoAssetSets:usedAutoAssetSets:
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$targetForAssetSet:specifiers:version:
+ _objc_msgSend$unlock
+ _objc_msgSend$unsubscribe:subscriptions:queue:completion:
+ _objc_msgSend$updateSystemAssetSetUsages:configurationManager:
+ _objc_msgSend$updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:
+ _objc_msgSend$updateTrialFromAssetSetUsages:rolloutUpdateMode:expensiveNetworking:storeManager:configurationManager:progress:completion:
+ _objc_msgSend$validateAllInstances
+ _objc_msgSend$versionComponentFromString:
+ _objc_msgSend$versionComponentsFromString:
+ _objc_msgSend$writeToURL:error:
+ _objc_setProperty_atomic
+ _objc_sync_enter
+ _objc_sync_exit
+ _open
- +[UAFAssetSet getAutoAssetClientName]
- +[UAFAssetSet getAutoAssetLockReason:]
- +[UAFAssetSet getLockedAutoAssets:usages:autoAssetSet:atomicInstance:assetNameToAutoAsset:]
- +[UAFAssetSet getMAAssetSetID:]
- +[UAFAssetSetObserver listenForAutoAssetNotificationsForAssetSet:queue:updateHandler:]
- +[UAFAssetSetObserver listenForUAFNotificationsForAssetSet:queue:updateHandler:]
- +[UAFAssetSetObserver notificationForAssetSet:]
- +[UAFAssetSetObserver sendUAFNotificationForAssetSet:]
- +[UAFAutoAssetManager configureAssetSet:assetSetUsages:configurationManager:changed:]
- +[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:configurationManager:lockIfUnchanged:]
- +[UAFAutoAssetManager handleDownloadedAndUnavailable:assetSetUsages:configurationManager:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:]
- +[UAFAutoAssetManager manageAssetSet:assetSetUsages:configurationManager:lockIfUnchanged:eliminateAndRetry:]
- +[UAFCommonUtilities _eliminateAutoAssetType:]
- +[UAFCommonUtilities _resetAutoAssetTypes:]
- +[UAFInstrumentationProvider logUAFAssetSetDailyStatus:assetSetID:]
- +[UAFTrialUpdateManager updateTrialFactors:missingRolloutsOnly:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]
- +[UAFTrialUpdateManager updateTrialFromAssetSetUsages:missingRolloutsOnly:expensiveNetworking:storeManager:configurationManager:progress:completion:]
- -[UAFAssetSet createAssetFromAutoAsset:assetName:]
- -[UAFAssetSet dealloc]
- -[UAFAssetSet getAutoAssets]
- -[UAFAssetSet getMAAutoAssetDownloadErrorsSync]
- -[UAFAssetSetObserver autoAssetNotifyToken]
- -[UAFAssetSetObserver setAutoAssetNotifyToken:]
- -[UAFSubscriptionStoreManager updateSystemAssetSetUsages]
- -[UAFUsageAliasConfiguration getAssetSetTrialAssets:usageValue:]
- GCC_except_table23
- _OBJC_IVAR_$_UAFAssetSet._assetNameToAutoAsset
- _OBJC_IVAR_$_UAFAssetSet._autoAssetAtomicInstance
- _OBJC_IVAR_$_UAFAssetSetObserver._autoAssetNotifyToken
- ___108+[UAFAutoAssetManager manageAssetSet:assetSetUsages:configurationManager:lockIfUnchanged:eliminateAndRetry:]_block_invoke
- ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.264
- ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.265
- ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.266
- ___149+[UAFTrialUpdateManager updateTrialFromAssetSetUsages:missingRolloutsOnly:expensiveNetworking:storeManager:configurationManager:progress:completion:]_block_invoke
- ___159+[UAFAutoAssetManager handleDownloadedAndUnavailable:assetSetUsages:configurationManager:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:]_block_invoke
- ___190+[UAFTrialUpdateManager updateTrialFactors:missingRolloutsOnly:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke
- ___190+[UAFTrialUpdateManager updateTrialFactors:missingRolloutsOnly:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke.248
- ___190+[UAFTrialUpdateManager updateTrialFactors:missingRolloutsOnly:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_2
- ___190+[UAFTrialUpdateManager updateTrialFactors:missingRolloutsOnly:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_2.249
- ___190+[UAFTrialUpdateManager updateTrialFactors:missingRolloutsOnly:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_3
- ___190+[UAFTrialUpdateManager updateTrialFactors:missingRolloutsOnly:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_4
- ___22-[UAFAssetSet dealloc]_block_invoke
- ___22-[UAFAssetSet refresh]_block_invoke.270
- ___24-[UAFAssetSet getAsset:]_block_invoke
- ___24-[UAFAssetSet getAssets]_block_invoke
- ___34-[UAFAssetSet getAsset:withUsage:]_block_invoke
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.255
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.256
- ___46-[UAFAssetUtilitiesService downloadSiriAssets]_block_invoke
- ___47-[UAFAssetSet getMAAutoAssetDownloadErrorsSync]_block_invoke
- ___58-[UAFAssetUtilitiesService downloadSiriAssetsOverCellular]_block_invoke
- ___58-[UAFSubscriptionStoreManager updateSystemAssetSetUsages:]_block_invoke
- ___60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke.243
- ___60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke.246
- ___60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke.247
- ___63+[UAFAssetSetManager subscribe:subscriptions:queue:completion:]_block_invoke.221
- ___65+[UAFAssetSetManager unsubscribe:subscriptions:queue:completion:]_block_invoke.226
- ___80+[UAFAssetSetObserver listenForUAFNotificationsForAssetSet:queue:updateHandler:]_block_invoke
- ___86+[UAFAssetSetObserver listenForAutoAssetNotificationsForAssetSet:queue:updateHandler:]_block_invoke
- ___90-[UAFAssetSetObserver initWithAssetSet:configurationDirURLs:queue:updateHandler:delegate:]_block_invoke.229
- ___98+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:configurationManager:lockIfUnchanged:]_block_invoke
- ___block_descriptor_40_e8_32s_e30_v24?0"NSString"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32s40s_e52_v32?0"NSString"8"MAAutoAssetSetAtomicEntry"16^B24ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e5_i8?0ls32l8r48l8s40l8
- ___block_descriptor_66_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_74_e8_32s40s48s56bs64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_74_e8_32s40s48s56s64s_e42_v32?0"NSString"8"NSArray"16"NSError"24ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.214
- ___block_literal_global.245
- ___block_literal_global.252
- _objc_msgSend$_eliminateAutoAssetType:
- _objc_msgSend$_resetAutoAssetTypes:
- _objc_msgSend$alterEntriesRepresentingAtomicSync:toBeComprisedOfEntries:
- _objc_msgSend$configureAssetSet:assetSetUsages:configurationManager:changed:
- _objc_msgSend$configureAutoAssetsFromAssetSetUsages:configurationManager:lockIfUnchanged:
- _objc_msgSend$createAssetFromAutoAsset:assetName:
- _objc_msgSend$fromContentsOfURL:error:
- _objc_msgSend$getAssetSetTrialAssets:usageValue:
- _objc_msgSend$getAssets
- _objc_msgSend$getAutoAssetClientName
- _objc_msgSend$getAutoAssetLockReason:
- _objc_msgSend$getAutoAssets
- _objc_msgSend$getLockedAutoAssets:usages:autoAssetSet:atomicInstance:assetNameToAutoAsset:
- _objc_msgSend$getMAAssetSetID:
- _objc_msgSend$handleDownloadedAndUnavailable:assetSetUsages:configurationManager:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:
- _objc_msgSend$init:assetSets:usageAliases:
- _objc_msgSend$listenForAutoAssetNotificationsForAssetSet:queue:updateHandler:
- _objc_msgSend$listenForUAFNotificationsForAssetSet:queue:updateHandler:
- _objc_msgSend$logUAFAssetSetDailyStatus:assetSetID:
- _objc_msgSend$manageAssetSet:assetSetUsages:configurationManager:lockIfUnchanged:eliminateAndRetry:
- _objc_msgSend$mutableCopy
- _objc_msgSend$notificationForAssetSet:
- _objc_msgSend$updateSystemAssetSetUsages
- _objc_msgSend$updateTrialFactors:missingRolloutsOnly:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:
- _objc_msgSend$updateTrialFromAssetSetUsages:missingRolloutsOnly:expensiveNetworking:storeManager:configurationManager:progress:completion:
CStrings:
+ "\x05\x15"
+ "\x06"
+ "\a"
+ "\x13"
+ "%@ lock of %@ for %@ to establish some assets as promoted"
+ "%@ promoting assets in asset set %@ from atomic instance %@"
+ "%@%@%@"
+ "%@.9999"
+ "%s #settings Cannot download Siri assets due to network connectivity..."
+ "%s %@ invalid: %{public}@ != %{public}@"
+ "%s Acquired exclusive lock on %@"
+ "%s Acquired shared lock on %@"
+ "%s Archived auto asset instance state for asset set %{public}@ to %@ and linked to %@"
+ "%s Archived auto asset promotion state for asset set %{public}@ to %@"
+ "%s Asset set %{public}@ should not have any entries for OS version %{public}@"
+ "%s Auto asset instance state at %@ doesn't exist: %{public}@"
+ "%s Auto asset instance state for asset set %{public}@ already written to %@ and linked to %@"
+ "%s Auto asset promotion state for asset set %{public}@ doesn't exist: %{public}@"
+ "%s Auto asset set %{public}@ currently has downloads blocked"
+ "%s Auto asset set %{public}@ doest not have expected specifiers %{public}@, has %{public}@"
+ "%s Auto asset set %{public}@ has expected specifiers %{public}@"
+ "%s Auto asset set %{public}@ is available has has atomic instance %{public}@"
+ "%s Can't get %@ assets for usage value \"%@\" in usage alias \"%@\": Unable to get asset config for asset set \"%@\""
+ "%s Can't get %@ assets: No asset manager present usage alias \"%@\""
+ "%s Can't get %@ assets: Unknown usage value \"%@\" in usage alias \"%@\""
+ "%s Cannot load promotion state for asset set %{public}@"
+ "%s Cannot promote nonexistant asset %{public}@ in asset set %{public}@"
+ "%s Cannot promote unpromotable asset %{public}@ in asset set %{public}@"
+ "%s Cannot remove \"%@\" yet as it cannot be locked for removal"
+ "%s Cannot set provisional nonexistant asset %{public}@ in asset set %{public}@"
+ "%s Cannot set provisional unpromotable asset %{public}@ in asset set %{public}@"
+ "%s Could get not stage asset set %{public}@ for other OS versions: %{public}@"
+ "%s Could initialize auto asset set %{public}@ : %{public}@"
+ "%s Could not check entries in atomic instance %{public}@ in auto asset set %{public}@ with reason %{public}@: %{public}@"
+ "%s Could not create auto asset set %{public}@ : %{public}@"
+ "%s Could not eliminate serialize version of auto asset %{public}@"
+ "%s Could not get auto asset set %{public}@ : %{public}@"
+ "%s Could not indicate lack of need in this OS for asset set %{public}@ : %{public}@"
+ "%s Could not indicate need for asset set %{public}@ : %{public}@"
+ "%s Could not remove serialized version of atomic instance %{public}@ in auto asset set %{public}@ with reason %{public}@, and so cannot decrement locks for it"
+ "%s Decoding of the auto asset promotion asset set name failed"
+ "%s Decrement locks for invalid promoted atomic instance %{public}@ in auto asset set %{public}@ with reason %{public}@"
+ "%s Did not have auto asset set object for set %{public}@ when attempting to gather errors"
+ "%s Emitted SADAvailableAssetDailyStatus message for asset sets %{public}@"
+ "%s Failed find cache dir for bundleIdentifier %{public}@: %{public}@"
+ "%s Failed load auto set instance from dictionary as at least one of required fields \"%@\" and %{public}@ weren't present in %{public}@"
+ "%s Failed to acquire exclusive lock on %@ as there are existing shared locks: %s"
+ "%s Failed to acquire exclusive lock on %@: %s"
+ "%s Failed to acquire shared lock on %@: %s"
+ "%s Failed to archive auto asset promotion state for asset set %{public}@ to %@: %{public}@"
+ "%s Failed to check auto asset set to validate asset set %{public}@ with instance %{public}@: %{public}@"
+ "%s Failed to clear stored state of asset set %{public}@ after update error"
+ "%s Failed to create UAFAssetSetObserver for %{public}@'"
+ "%s Failed to create auto asset set to validate asset set %{public}@ with instance %{public}@: %{public}@"
+ "%s Failed to create dir for auto asset instance state for asset set %{public}@ at %@: %{public}@"
+ "%s Failed to create dirs for \"%@\": %{public}@"
+ "%s Failed to create subatomic instance from atomic instance %{public}@ to promoted assets in asset set %{public}@: %{public}@"
+ "%s Failed to generate MAAutoAssetSetEntry for %{public}@ : %{public}@"
+ "%s Failed to generate target for Asset set %{public}@ for OS version %{public}@"
+ "%s Failed to link auto asset instance state for asset set %{public}@ from %@ to %@: %{public}@"
+ "%s Failed to lock asset set %{public}@ with atomic instance %{public}@ after loading instance from storage: %{public}@"
+ "%s Failed to lock subatomic instance %{public}@ to promoted assets in asset set %{public}@: %{public}@"
+ "%s Failed to notify about removal of asset set %{public}@"
+ "%s Failed to notify about update of instance state for asset set %{public}@ from %@ to %@"
+ "%s Failed to parse auto asset promotion state from \"%@\" for asset set %{public}@"
+ "%s Failed to parse auto asset promotion state from %@"
+ "%s Failed to read auto asset instance state from %@ : %{public}@"
+ "%s Failed to read auto asset promotion state from \"%@\" for asset set %{public}@: %{public}@"
+ "%s Failed to release lock on %@: %s"
+ "%s Failed to remove \"%@\": %{public}@"
+ "%s Failed to remove auto asset instance state for asset set %{public}@ from %@: %{public}@"
+ "%s Failed to remove invalid instance at \"%@\": %{public}@"
+ "%s Failed to set %{public}@ instance of asset set %{public}@ as latest: %{public}@"
+ "%s Failed to unlock subatomic instance %{public}@ from promoted assets in asset set %{public}@: %{public}@"
+ "%s Failed to write auto asset instance state for asset set %{public}@ to %@: %{public}@"
+ "%s Instance at \"%@\" is valid"
+ "%s Loading asset set %{public}@ with atomic instance %{public}@ from storage"
+ "%s Locked asset set %{public}@ with atomic instance %{public}@ with MobileAsset after loading from storage"
+ "%s MAAutoAsset eliminateAllForAssetTypeSync returned: %@"
+ "%s No auto asset type defined for %{public}@ for OS version %{public}@"
+ "%s No platform assets available when attempting to staging assets"
+ "%s No staging targets for other OS versions"
+ "%s No trial assets for asset set %{public}@ for observer"
+ "%s No version -> configuration managers available when attempting to staging assets"
+ "%s Not marking assets in atomic instance %{public}@ promoted for auto asset %{public}@ in asset set %{public}@ as that instance is already promoted"
+ "%s Not marking assets in atomic instance %{public}@ provisional for auto asset %{public}@ in asset set %{public}@ as that instance has already reached max provisional count"
+ "%s Not marking assets in atomic instance %{public}@ provisional for auto asset %{public}@ in asset set %{public}@ as that instance is already promoted"
+ "%s Parsed auto asset instance state from \"%@\" with:\nasset set name: %{public}@\ninstance: %{public}@\nassets: %{public}@"
+ "%s Parsed auto asset promotion state from \"%@\" for asset set %{public}@ has atomic instance %{public}@, not desired atomic instance %{public}@"
+ "%s Parsed auto asset promotion state from \"%@\" for asset set %{public}@ with:\nasset set name: %{public}@\nbuild version: %{public}@\nlatest atomic instance: %{public}@\nlatest promoted specifiers: %{public}@\nlatest provisional specifiers: %{public}@\npromoted specifiers: %{public}@"
+ "%s Released lock on %@"
+ "%s Removed \"%@\""
+ "%s Removed invalid instance at \"%@\""
+ "%s Resetting asset promotion state from \"%@\" for asset set %{public}@ as current build version %{public}@ does not match saved build version %{public}@"
+ "%s Returning %@"
+ "%s Setting provisional count for %{public}@ to %llu in atomic instance %{public}@ of auto asset %{public}@"
+ "%s Skipping %@ due to no assetType defined"
+ "%s Skipping resetAutoAssets due to nil UAFAssetSetConfiguration"
+ "%s Staging asset set %{public}@ for OS versions %{public}@ through %{public}@ with type %{public}@ and entries %{public}@"
+ "%s Unexpected token is not of kind UAFAssetSetObserver'"
+ "%s Unknown asset source %@ for %@"
+ "%s Updated locks to remove invalid promoted atomic instances of auto asset set %{public}@"
+ "%s Updating namespaces for %{public}@ prior to on-demand factor downloading"
+ "%s notification \"%@\" received"
+ "+[UAFAssetSet autoAssetSet:usages:]"
+ "+[UAFAssetSetConfiguration fromContentsOfURL:applyFeatureFlags:error:]"
+ "+[UAFAssetSetObserver listenForUAFNotificationsForAssetSet:forRoot:queue:updateHandler:]"
+ "+[UAFAssetSetObserver listenForUAFNotificationsForAssetSet:forRoot:queue:updateHandler:]_block_invoke"
+ "+[UAFAssetSetObserver sendUAFNotificationForAssetSet:forRoot:]"
+ "+[UAFAutoAssetInstance clear:path:]"
+ "+[UAFAutoAssetInstance loadInstanceWithURL:]"
+ "+[UAFAutoAssetInstance removeInstanceWithAssetSetName:atomicInstance:]"
+ "+[UAFAutoAssetInstance validateAllInstances]"
+ "+[UAFAutoAssetManager configureAssetSet:specifiers:changed:]"
+ "+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:]"
+ "+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:]_block_invoke"
+ "+[UAFAutoAssetManager handleDownloadedAndUnavailable:specifiers:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:]"
+ "+[UAFAutoAssetManager handleDownloadedAndUnavailable:specifiers:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:]_block_invoke"
+ "+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:]"
+ "+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:]_block_invoke"
+ "+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:]_block_invoke_2"
+ "+[UAFAutoAssetManager listenForUpdates:updateHandler:]"
+ "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:eliminateAndRetry:]"
+ "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:eliminateAndRetry:]_block_invoke"
+ "+[UAFAutoAssetManager sendNotificationForAssetSet:]"
+ "+[UAFAutoAssetManager stageAssetSet:targets:]"
+ "+[UAFAutoAssetManager stageAssetsWithSubscriptions:knownAutoAssetSets:usedAutoAssetSets:]"
+ "+[UAFAutoAssetManager targetForAssetSet:specifiers:version:]"
+ "+[UAFAutoAssetPromotion _loadPromotionWithAssetSetName:]"
+ "+[UAFAutoAssetPromotion cacheDirURL]"
+ "+[UAFAutoAssetPromotion clear]"
+ "+[UAFAutoAssetPromotion loadPromotionWithAssetSetName:latestAtomicInstance:]"
+ "+[UAFCommonUtilities _eliminateAutoAssetSet:]"
+ "+[UAFCommonUtilities _getPopulationMapping:toAudience:toServer:]"
+ "+[UAFCommonUtilities _resetAutoAssetSets:]"
+ "+[UAFInstrumentationProvider logUAFAssetSetDailyStatus:]"
+ "+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]"
+ "+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke"
+ "+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_2"
+ "+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_4"
+ "+[UAFTrialUpdateManager updateTrialFromAssetSetUsages:rolloutUpdateMode:expensiveNetworking:storeManager:configurationManager:progress:completion:]"
+ "+[UAFTrialUpdateManager updateTrialFromAssetSetUsages:rolloutUpdateMode:expensiveNetworking:storeManager:configurationManager:progress:completion:]_block_invoke"
+ "-[UAFAssetSet assetNamed:]"
+ "-[UAFAssetSet assetNamed:]_block_invoke"
+ "-[UAFAssetSet assetNamed:withUsage:]"
+ "-[UAFAssetSet markAssetsPromoted:error:]"
+ "-[UAFAssetSet markAssetsProvisional:error:]"
+ "-[UAFAssetSetConfiguration getAssets:]"
+ "-[UAFAssetSetManager observeAssetSet:queue:handler:]"
+ "-[UAFAssetSetManager removeObserver:]"
+ "-[UAFAssetUtilitiesService _downloadSiriAssetsWithCellular:]"
+ "-[UAFAutoAssetInstance initWithDictionary:]"
+ "-[UAFAutoAssetInstance isValid]"
+ "-[UAFAutoAssetInstance isValid]_block_invoke"
+ "-[UAFAutoAssetInstance lockForLoading]"
+ "-[UAFAutoAssetInstance lockForRemoval]"
+ "-[UAFAutoAssetInstance setLatest:]"
+ "-[UAFAutoAssetInstance unlock]"
+ "-[UAFAutoAssetPromotion clear]"
+ "-[UAFAutoAssetPromotion initWithDictionary:]"
+ "-[UAFAutoAssetPromotion markSpecifiersPromoted:assetType:autoAssetSet:atomicInstance:error:]"
+ "-[UAFAutoAssetPromotion markSpecifiersProvisional:atomicInstance:error:]"
+ "-[UAFAutoAssetPromotion save:]"
+ "-[UAFAutoAssetSet availableForUseError:newerVersionError:]"
+ "-[UAFAutoAssetSet catalogAssetSetID]"
+ "-[UAFAutoAssetSet dealloc]_block_invoke"
+ "-[UAFAutoAssetSet getMAAutoAssetDownloadErrorsSync]"
+ "-[UAFAutoAssetSet initWithAssetSetName:autoAssets:]"
+ "-[UAFAutoAssetSet lockAtomicInstance:specifierToAssetName:]"
+ "-[UAFAutoAssetSet lockLatestAtomicInstance:]"
+ "-[UAFAutoAssetSet lockLatestAtomicInstance:]_block_invoke"
+ "-[UAFAutoAssetSet lockLatestAtomicInstance:]_block_invoke_2"
+ "-[UAFAutoAssetSet markAssetsPromoted:error:]"
+ "-[UAFAutoAssetSet markAssetsProvisional:error:]"
+ "-[UAFSubscriptionStoreManager updateSystemAssetSetUsages:configurationManager:]_block_invoke"
+ "-[UAFUsageAliasConfiguration getAssetSetAssets:usageValue:withSource:]"
+ ":"
+ "<unset>"
+ "@"
+ "@\"UAFAutoAssetInstance\""
+ "@\"UAFAutoAssetSet\""
+ "@\"UAFSubscriptionStoreManager\""
+ "@28@0:8@16B24"
+ "@32@0:8^@16@24"
+ "@40@0:8@16@24^B32"
+ "All"
+ "AssetSpecifier"
+ "B24@0:8^@16"
+ "B28@0:8@16B24"
+ "B40@0:8@16^@24^@32"
+ "B56@0:8@16@24@32@40^@48"
+ "BuildVersion"
+ "ForceUpdateNamespaces"
+ "MobileAssetAssetAudience-%@"
+ "PallasUrlOverrideV2-%@"
+ "T@\"MAAutoAssetSet\",&,N,V_autoAssetSet"
+ "T@\"NSMutableDictionary\",&,N,V_assets"
+ "T@\"NSMutableDictionary\",&,N,V_latestProvisionalSpecifiers"
+ "T@\"NSMutableDictionary\",&,N,V_promotedSpecifiers"
+ "T@\"NSMutableSet\",&,N,V_atomicInstances"
+ "T@\"NSMutableSet\",&,N,V_latestPromotedSpecifiers"
+ "T@\"NSMutableSet\",&,N,V_unpromotableAssets"
+ "T@\"NSMutableSet\",&,V_assetSetObservers"
+ "T@\"NSString\",&,N,V_atomicInstance"
+ "T@\"NSString\",&,N,V_buildVersion"
+ "T@\"NSString\",&,N,V_latestAtomicInstance"
+ "T@\"UAFAssetSetManager\",R,N"
+ "T@\"UAFAutoAssetInstance\",&,N,V_instance"
+ "T@\"UAFAutoAssetSet\",&,N,V_autoAssetSet"
+ "T@\"UAFConfigurationManager\",&,V_configurationManager"
+ "T@\"UAFSubscriptionStoreManager\",&,V_subscriptionStoreManager"
+ "TB,N,V_isTrialAvailable"
+ "Ti,N,V_lockFileFD"
+ "Ti,N,V_rootNotifyToken"
+ "UAF Promotion"
+ "UAFAutoAssetInstance"
+ "UAFAutoAssetPromotion"
+ "UAFAutoAssetSet"
+ "UAFAutoAssetSet.Concurrent"
+ "UAFManagedSubscriptions.Concurrent"
+ "UAFPlatform"
+ "URLByAppendingPathComponent:isDirectory:"
+ "URLByStandardizingPath"
+ "URLForDirectory:inDomain:appropriateForURL:create:error:"
+ "URLWithString:"
+ "_assetSetObservers"
+ "_atomicInstance"
+ "_atomicInstances"
+ "_buildVersion"
+ "_configurationManager"
+ "_downloadSiriAssetsWithCellular:"
+ "_eliminateAutoAssetSet:"
+ "_getPopulationMapping:toAudience:toServer:"
+ "_instance"
+ "_isTrialAvailable"
+ "_latestAtomicInstance"
+ "_latestPromotedSpecifiers"
+ "_latestProvisionalSpecifiers"
+ "_loadPromotionWithAssetSetName:"
+ "_lockFileFD"
+ "_promotedSpecifiers"
+ "_resetAutoAssetSets:"
+ "_rootNotifyToken"
+ "_subscriptionStoreManager"
+ "_unpromotableAssets"
+ "addAtomicInstance:"
+ "addEntriesFromDictionary:"
+ "alterEntriesRepresentingAtomicSync:toBeComprisedOfEntries:withNeedPolicy:"
+ "applyFeatureFlags"
+ "assetNamed"
+ "assetNamed:"
+ "assetNamed:withUsage:"
+ "assetSetForStagingSync:asEntriesWhenTargeting:"
+ "assetSetObservers"
+ "assetWithName:"
+ "assetsFromSpecifiers:"
+ "atomicInstance"
+ "atomicInstances"
+ "autoAssetEntryToAsset:withAssetName:"
+ "autoAssetSet"
+ "autoAssetSet:usages:"
+ "availableForUseError:newerVersionError:"
+ "blockCheckDownload"
+ "buildVersion"
+ "buildVersionFromLockReason:"
+ "cacheDirURL"
+ "catalogAssetSetID"
+ "checkAtomic:forAtomicInstance:withTimeout:completion:"
+ "clear"
+ "clear:path:"
+ "com.apple.MobileAsset"
+ "com.apple.UnifiedAssetFramework.AssetSpecifier"
+ "com.apple.siri.UnifiedAssetFramework"
+ "com.apple.siri.asr.hammer"
+ "com.apple.siri.findmy"
+ "com.apple.siri.uaf.osupdates"
+ "com.apple.siri.uaf.platform"
+ "com.apple.siri.understanding.nl.overrides"
+ "configurationManager"
+ "configurationManagers:"
+ "configureAssetSet:specifiers:changed:"
+ "configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "decimalDigitCharacterSet"
+ "decomposeSaveFileURL:assetSetName:atomicInstance:"
+ "does need"
+ "downloadStatusForSubscriber:subscriptionName:"
+ "encodeToDictionary"
+ "fileSystemRepresentation"
+ "force all rollouts"
+ "formSubAtomicInstanceSync:fromAtomicInstance:toBeComprisedOfEntries:error:"
+ "fromContentsOfURL:applyFeatureFlags:error:"
+ "getAssetSetAssets:usageValue:withSource:"
+ "getAssets:"
+ "getAssets:withSource:"
+ "getClientName"
+ "getFormReason:atomicInstance:"
+ "getLockReason:"
+ "getResourceValue:forKey:error:"
+ "getUAFPallasURLForAssetSet:"
+ "getUAFPallasURLForAssetType:"
+ "getUAFPopulationForAssetSet:"
+ "getUAFPopulationForAssetType:"
+ "handleDownloadedAndUnavailable:specifiers:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:"
+ "i32@0:8@16@?24"
+ "i44@0:8@16B24@28@?36"
+ "initForMinTargetOSVersion:toMaxTargetOSVersion:asEntriesWhenTargeting:"
+ "initWithAssetSetName:"
+ "initWithAssetSetName:atomicInstance:entries:"
+ "initWithAssetSetName:autoAssets:"
+ "initWithName:assetSets:usageAliases:"
+ "initWithName:assetSets:usageAliases:expires:"
+ "initWithUUIDString:"
+ "instance"
+ "instanceDirURL"
+ "instanceFileURL:atomicInstance:"
+ "instanceForSpecifier:"
+ "invalidatePromotedInstances:autoAssetSet:group:"
+ "invertedSet"
+ "isEqualToDictionary:"
+ "isTrialAvailable"
+ "isValid"
+ "knownUsagesForAssetSet:usageType:"
+ "lastPathComponent"
+ "latestAtomicInstance"
+ "latestDowloadedAtomicInstanceEntries"
+ "latestPromotedSpecifiers"
+ "latestProvisionalSpecifiers"
+ "linkItemAtURL:toURL:error:"
+ "listenForUAFNotificationsForAssetSet:forRoot:queue:updateHandler:"
+ "listenForUpdates:updateHandler:"
+ "loadInstanceWithAssetSetName:"
+ "loadInstanceWithURL:"
+ "loadPromotionWithAssetSetName:"
+ "loadPromotionWithAssetSetName:latestAtomicInstance:"
+ "lockAtomicInstance:specifierToAssetName:"
+ "lockAutoAssets:"
+ "lockFileFD"
+ "lockForLoading"
+ "lockForRemoval"
+ "lockLatestAtomicInstance:"
+ "lockPrefix"
+ "lockReasonFromPromotion:"
+ "lockReasonValid:"
+ "logUAFAssetSetDailyStatus:"
+ "manageAssetSet:specifiers:lockIfUnchanged:eliminateAndRetry:"
+ "managePlatformSubscription"
+ "markAssetsPromoted:error:"
+ "markAssetsProvisional:error:"
+ "markSpecifiersPromoted:assetType:autoAssetSet:atomicInstance:error:"
+ "markSpecifiersProvisional:atomicInstance:error:"
+ "maxTargetOSVersion"
+ "maxVersionFromVersionString:"
+ "minTargetOSVersion"
+ "mobileasset_com_apple_siri_asr_hammer"
+ "mobileasset_com_apple_siri_findmy"
+ "mobileasset_com_apple_siri_understanding"
+ "mobileasset_com_apple_siri_understanding_nl_overrides"
+ "needForAtomicSync:"
+ "notificationForAssetSet:forRoot:"
+ "numberWithInteger:"
+ "observeAssetSet:queue:handler:"
+ "placeholder"
+ "platform"
+ "promotedSpecifiers"
+ "promotion"
+ "rangeOfString:options:"
+ "removeAllObjects"
+ "removeInstanceWithAssetSetName:atomicInstance:"
+ "removeItemAtURL:error:"
+ "removeObjectForKey:"
+ "removeObserver:"
+ "removeUnusedAutoAssetSets:usedAutoAssetSets:"
+ "retrieveAssetSet:usages:"
+ "root"
+ "rootNotifyToken"
+ "save:"
+ "saveFileURL:"
+ "schedulerPolicy"
+ "sendNotificationForAssetSet:"
+ "sendUAFNotificationForAssetSet:forRoot:"
+ "setAssetSetObservers:"
+ "setAtomicInstance:"
+ "setAtomicInstances:"
+ "setAutoAssetSet:"
+ "setBuildVersion:"
+ "setConfigurationManager:"
+ "setFileURL:"
+ "setInstance:"
+ "setIsTrialAvailable:"
+ "setLatest:"
+ "setLatestAtomicInstance:"
+ "setLatestPromotedSpecifiers:"
+ "setLatestProvisionalSpecifiers:"
+ "setLockFileFD:"
+ "setPromotedSpecifiers:"
+ "setRootNotifyToken:"
+ "setSubscriptionStoreManager:"
+ "setUAFPallasURL:assetSet:"
+ "setUAFPopulation:assetSet:"
+ "setUnpromotableAssets:"
+ "sharedManager"
+ "shouldApplyFeatureFlags"
+ "siriknowledged"
+ "stageAssetSet:targets:"
+ "stageAssetsWithSubscriptions:knownAutoAssetSets:usedAutoAssetSets:"
+ "stringByDeletingPathExtension"
+ "subscribedUsagesForAssetSet:"
+ "subscriptionStoreManager"
+ "subscriptionsForSubscriber:"
+ "targetForAssetSet:specifiers:version:"
+ "uaftool reset"
+ "unlock"
+ "unpromotableAssets"
+ "unsubscribe:subscriptionNames:queue:completion:"
+ "updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:"
+ "updateSystemAssetSetUsages:configurationManager:"
+ "updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:"
+ "updateTrialFromAssetSetUsages:rolloutUpdateMode:expensiveNetworking:storeManager:configurationManager:progress:completion:"
+ "v32@0:8^@16^@24"
+ "v40@0:8@16@24B32B36"
+ "v44@0:8@16@24@32B40"
+ "v60@0:8@16@24B32@36@44@52"
+ "v68@0:8@16q24B32@36@44@?52@?60"
+ "v88@0:8@16q24B32B36Q40@48@56@64@?72@?80"
+ "validateAllInstances"
+ "versionComponentFromString:"
+ "versionComponentsFromString:"
+ "will in another OS need"
+ "writeToURL:error:"
- "\b\x14"
- "%s #settings Cannot downloading Siri assets due to network connectivity..."
- "%s %{public}@: Failed to unlock asset set %{public}@"
- "%s Can't get Trial factors for usage value \"%@\" in usage alias \"%@\": Unable to get asset config for asset set \"%@\""
- "%s Can't get Trial factors: No asset manager present usage alias \"%@\""
- "%s Can't get Trial factors: Unknown usage value \"%@\" in usage alias \"%@\""
- "%s Could not get trial assets for asset set %{public}@ for observer"
- "%s Emitted SADAvailableAssetDailyStatus message for asset set name %{public}@ with ID %{public}@"
- "%s Skipping resetAutoAssets due to nil AssetTypes"
- "%s Updating namespaces for %@ prior to on-demand factor downloading"
- "+[UAFAssetSet getLockedAutoAssets:usages:autoAssetSet:atomicInstance:assetNameToAutoAsset:]"
- "+[UAFAssetSet getMAAssetSetID:]"
- "+[UAFAssetSetConfiguration fromContentsOfURL:error:]"
- "+[UAFAssetSetObserver listenForAutoAssetNotificationsForAssetSet:queue:updateHandler:]"
- "+[UAFAssetSetObserver listenForUAFNotificationsForAssetSet:queue:updateHandler:]"
- "+[UAFAssetSetObserver sendUAFNotificationForAssetSet:]"
- "+[UAFAutoAssetManager configureAssetSet:assetSetUsages:configurationManager:changed:]"
- "+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:configurationManager:lockIfUnchanged:]"
- "+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:configurationManager:lockIfUnchanged:]_block_invoke"
- "+[UAFAutoAssetManager handleDownloadedAndUnavailable:assetSetUsages:configurationManager:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:]"
- "+[UAFAutoAssetManager handleDownloadedAndUnavailable:assetSetUsages:configurationManager:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:]_block_invoke"
- "+[UAFAutoAssetManager manageAssetSet:assetSetUsages:configurationManager:lockIfUnchanged:eliminateAndRetry:]"
- "+[UAFAutoAssetManager manageAssetSet:assetSetUsages:configurationManager:lockIfUnchanged:eliminateAndRetry:]_block_invoke"
- "+[UAFCommonUtilities _resetAutoAssetTypes:]"
- "+[UAFInstrumentationProvider logUAFAssetSetDailyStatus:assetSetID:]"
- "+[UAFTrialUpdateManager updateTrialFactors:missingRolloutsOnly:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]"
- "+[UAFTrialUpdateManager updateTrialFactors:missingRolloutsOnly:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke"
- "+[UAFTrialUpdateManager updateTrialFactors:missingRolloutsOnly:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_2"
- "+[UAFTrialUpdateManager updateTrialFactors:missingRolloutsOnly:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_4"
- "+[UAFTrialUpdateManager updateTrialFromAssetSetUsages:missingRolloutsOnly:expensiveNetworking:storeManager:configurationManager:progress:completion:]"
- "+[UAFTrialUpdateManager updateTrialFromAssetSetUsages:missingRolloutsOnly:expensiveNetworking:storeManager:configurationManager:progress:completion:]_block_invoke"
- "-[UAFAssetSet dealloc]_block_invoke"
- "-[UAFAssetSet getAsset:]"
- "-[UAFAssetSet getAsset:]_block_invoke"
- "-[UAFAssetSet getAsset:withUsage:]"
- "-[UAFAssetSet getAsset:withUsage:]_block_invoke"
- "-[UAFAssetSet getMAAutoAssetDownloadErrorsSync]"
- "-[UAFAssetSet getMAAutoAssetDownloadErrorsSync]_block_invoke"
- "-[UAFAssetSet refresh]_block_invoke"
- "-[UAFAssetSet setAssetsPromoted:error:]"
- "-[UAFAssetSet setAssetsProvisional:error:]"
- "-[UAFAssetUtilitiesService downloadSiriAssetsOverCellular]"
- "-[UAFAssetUtilitiesService downloadSiriAssets]"
- "-[UAFSubscriptionStoreManager updateSystemAssetSetUsages:]_block_invoke"
- "-[UAFUsageAliasConfiguration getAssetSetTrialAssets:usageValue:]"
- "@48@0:8@16@24@32^B40"
- "B56@0:8@16@24^@32^@40^@48"
- "Ti,N,V_autoAssetNotifyToken"
- "_assetNameToAutoAsset"
- "_autoAssetAtomicInstance"
- "_autoAssetNotifyToken"
- "_eliminateAutoAssetType:"
- "_resetAutoAssetTypes:"
- "alterEntriesRepresentingAtomicSync:toBeComprisedOfEntries:"
- "autoAssetNotifyToken"
- "configureAssetSet:assetSetUsages:configurationManager:changed:"
- "configureAutoAssetsFromAssetSetUsages:configurationManager:lockIfUnchanged:"
- "createAssetFromAutoAsset:assetName:"
- "getAsset"
- "getAssetSetTrialAssets:usageValue:"
- "getAutoAssetClientName"
- "getAutoAssetLockReason:"
- "getAutoAssets"
- "getLockedAutoAssets:usages:autoAssetSet:atomicInstance:assetNameToAutoAsset:"
- "getMAAssetSetID:"
- "handleDownloadedAndUnavailable:assetSetUsages:configurationManager:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:"
- "i40@0:8@16@24@?32"
- "listenForAutoAssetNotificationsForAssetSet:queue:updateHandler:"
- "listenForUAFNotificationsForAssetSet:queue:updateHandler:"
- "logUAFAssetSetDailyStatus:assetSetID:"
- "manageAssetSet:assetSetUsages:configurationManager:lockIfUnchanged:eliminateAndRetry:"
- "mutableCopy"
- "notificationForAssetSet:"
- "sendUAFNotificationForAssetSet:"
- "setAutoAssetNotifyToken:"
- "updateSystemAssetSetUsages"
- "updateTrialFactors:missingRolloutsOnly:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:"
- "updateTrialFromAssetSetUsages:missingRolloutsOnly:expensiveNetworking:storeManager:configurationManager:progress:completion:"
- "v32@?0@\"NSString\"8@\"MAAutoAssetSetAtomicEntry\"16^B24"
- "v48@0:8@16@24@32B40B44"
- "v64@0:8@16B24B28@32@40@?48@?56"
- "v68@0:8@16@24@32B40@44@52@60"
- "v84@0:8@16B24B28B32Q36@44@52@60@?68@?76"

```
