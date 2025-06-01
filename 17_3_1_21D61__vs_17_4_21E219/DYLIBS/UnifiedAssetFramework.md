## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3302.4.1.0.0
-  __TEXT.__text: 0x4b43c
-  __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x25a8
-  __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x63c
-  __TEXT.__cstring: 0x70ec
-  __TEXT.__oslogstring: 0x88b5
-  __TEXT.__dlopen_cstrs: 0x290
-  __TEXT.__unwind_info: 0xc40
-  __TEXT.__objc_classname: 0x324
-  __TEXT.__objc_methname: 0x78d1
-  __TEXT.__objc_methtype: 0xbb1
-  __TEXT.__objc_stubs: 0x6460
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x13c0
-  __DATA_CONST.__objc_classlist: 0x108
+3304.77.1.1.1
+  __TEXT.__text: 0x5483c
+  __TEXT.__auth_stubs: 0xa30
+  __TEXT.__objc_methlist: 0x29d0
+  __TEXT.__const: 0xc0
+  __TEXT.__gcc_except_tab: 0x824
+  __TEXT.__cstring: 0x7e64
+  __TEXT.__oslogstring: 0x915d
+  __TEXT.__dlopen_cstrs: 0x238
+  __TEXT.__unwind_info: 0xe10
+  __TEXT.__objc_classname: 0x38b
+  __TEXT.__objc_methname: 0x8331
+  __TEXT.__objc_methtype: 0xc45
+  __TEXT.__objc_stubs: 0x6c00
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__const: 0x16b0
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2730
-  __DATA_CONST.__objc_selrefs: 0x1df0
-  __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__cfstring: 0x2e40
+  __DATA_CONST.__objc_const: 0x2b08
+  __DATA_CONST.__objc_selrefs: 0x2028
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x340
+  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__objc_arraydata: 0xc8
+  __AUTH_CONST.__cfstring: 0x3380
   __AUTH_CONST.__objc_intobj: 0x228
-  __AUTH_CONST.__objc_const: 0x240
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x500
+  __AUTH_CONST.__objc_const: 0x4c8
+  __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__auth_got: 0x528
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x318
-  __DATA.__objc_superrefs: 0xb0
-  __DATA.__objc_ivar: 0x28c
-  __DATA.__data: 0x208
+  __DATA.__objc_ivar: 0x2cc
+  __DATA.__data: 0x210
+  __DATA.__common: 0x18
   __DATA.__bss: 0x8
-  __DATA_DIRTY.__const: 0x420
-  __DATA_DIRTY.__objc_const: 0xc58
-  __DATA_DIRTY.__objc_data: 0x910
+  __DATA_DIRTY.__const: 0x280
+  __DATA_DIRTY.__objc_const: 0xc10
+  __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__common: 0x48
-  __DATA_DIRTY.__bss: 0x290
+  __DATA_DIRTY.__bss: 0x2a8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: FD6B6729-AD57-365C-B975-D1334D28658C
-  Functions: 1055
-  Symbols:   3968
-  CStrings:  3065
+  UUID: 6A07A6D2-178F-3BA5-AC68-9D757782D90F
+  Functions: 1173
+  Symbols:   4391
+  CStrings:  3371
 
Symbols:
+ +[UAFAssetSet autoAssetSet:usages:uuid:]
+ +[UAFAssetSetManager autoAssetDetailsForAssetNamed:assetSet:usages:autoAssetType:autoAssetSpecifier:]
+ +[UAFAssetSetManager cacheDeleteDefaultsKeyForAutoAssetType:autoAssetSpecifier:]
+ +[UAFAssetSetManager cacheDeleteDisabledForAutoAssetType:autoAssetSpecifier:]
+ +[UAFAssetSetManager defaults]
+ +[UAFAssetSetManager disableCacheDelete:forAutoAssetType:autoAssetSpecifier:]
+ +[UAFAssetSetMetadata OSVersion]
+ +[UAFAssetSetMetadata fromAssetDir:error:]
+ +[UAFAssetSetMetadata fromContentsOfURL:error:]
+ +[UAFAssetSetMetadata isValid:error:]
+ +[UAFAssetSetMetadata supportedFileVersions]
+ +[UAFAutoAssetManager _createXPCConnection]
+ +[UAFAutoAssetManager _logDailyStatusEventForAssetSetArrived:entries:]
+ +[UAFAutoAssetManager conditionallyLockLatestAssetSet:newestInstance:checkAtomicError:completion:]
+ +[UAFAutoAssetManager forceRemoveAutoAssetSet:]
+ +[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:noAllowed:]
+ +[UAFAutoAssetManager latestAtomicInstanceForClients:OSSupported:error:]
+ +[UAFAutoAssetManager latestAtomicInstanceFromMA:error:]
+ +[UAFAutoAssetManager lockLatestAssetSet:completion:]
+ +[UAFAutoAssetManager logAtomicInstance:name:entries:]
+ +[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:]
+ +[UAFAutoAssetManager removeAutoAssetSet:completion:]
+ +[UAFAutoAssetManager shouldCheckAssetSet:autoAssetSet:changed:locked:]
+ +[UAFAutoAssetSet autoAssetEntryToAsset:withAssetName:]
+ +[UAFAutoAssetSet catalogAssetSetID:]
+ +[UAFAutoAssetSet latestAtomicInstance:completion:]
+ +[UAFCommonUtilities getMAPath:]
+ +[UAFCommonUtilities isAssistantEnabled]
+ +[UAFCommonUtilities isDictationEnabled]
+ +[UAFCommonUtilities mobileGestaltQuery:]
+ +[UAFCommonUtilities systemLanguageLocale]
+ +[UAFConfiguration trialFeatureEnabled:]
+ +[UAFGestalt deviceMatch:onMatch:]
+ +[UAFGestalt dictionaryForGestalt:]
+ +[UAFGestalt dictionaryIsValid:]
+ +[UAFGestalt isKeySupported:key:]
+ +[UAFGestalt predicateMatch:]
+ +[UAFGestalt sharedManager]
+ +[UAFGestalt urlForGestalt:]
+ +[UAFInstrumentationProvider logDownloadTriggerEventWithLanguage:hasExistingAssets:retryCount:]
+ +[UAFMinVersionConfiguration fromContentsOfURL:error:]
+ +[UAFMinVersionConfiguration isValid:error:]
+ +[UAFMinVersionConfiguration supportedFileVersions]
+ +[UAFPlatform compareVersion:with:]
+ +[UAFPreinstalledAssetsCache assetNamed:assetType:attributes:]
+ +[UAFPreinstalledAssetsCache checkForAssetTypePath:]
+ +[UAFPreinstalledAssetsCache initCache]
+ +[UAFPreinstalledAssetsCache invalidateCache]
+ +[UAFPreinstalledAssetsCache lookupStringForAsset:withAttributes:]
+ +[UAFPreinstalledAssetsCache queryAssetType:attributes:]
+ +[UAFPrestageConfiguration fromContentsOfURL:error:]
+ +[UAFPrestageConfiguration isValid:error:]
+ +[UAFPrestageConfiguration predicateMatch:]
+ +[UAFPrestageConfiguration supportedFileVersions]
+ -[UAFAssetConfiguration ignoreOSCompatibility]
+ -[UAFAssetConfiguration setIgnoreOSCompatibility:]
+ -[UAFAssetSet applyAssetTransformations:]
+ -[UAFAssetSet applyMinVersions:]
+ -[UAFAssetSet applyOSCompatibility:]
+ -[UAFAssetSet createAssetFromPreinstalledWithAutoAssetInfo:assetName:fromRoot:]
+ -[UAFAssetSet dealloc]
+ -[UAFAssetSet getAutoAssetPreinstalledForRoots:]
+ -[UAFAssetSet setAssetsPromoted:purgeabilityLevel:error:]
+ -[UAFAssetSet setAssetsProvisional:purgeabilityLevel:error:]
+ -[UAFAssetSetConfiguration metadataAsset]
+ -[UAFAssetSetConfiguration setMetadataAsset:]
+ -[UAFAssetSetManager assetNamesForAssetSet:usages:]
+ -[UAFAssetSetManager cacheDeleteDisabledForAssetNamed:assetSet:usages:]
+ -[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]
+ -[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:storeManager:configurationManager:]
+ -[UAFAssetSetMetadata .cxx_destruct]
+ -[UAFAssetSetMetadata OSSupported]
+ -[UAFAssetSetMetadata initWithDictionary:]
+ -[UAFAssetSetMetadata maxOSVersion]
+ -[UAFAssetSetMetadata minOSVersion]
+ -[UAFAssetSetMetadata setMaxOSVersion:]
+ -[UAFAssetSetMetadata setMinOSVersion:]
+ -[UAFAssetUtilities _assetsAreAvailableForLanguageSync:delegateEnabled:]
+ -[UAFAssetUtilities _downloadSiriAssetsRetry]
+ -[UAFAssetUtilities _downloadSiriAssetsWithDelay:]
+ -[UAFAssetUtilities _handleNetworkPathUpdate:]
+ -[UAFAssetUtilities _networkIsExpensiveForPath:]
+ -[UAFAssetUtilities _networkIsSatisfiedForPath:]
+ -[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:delegateEnabled:]
+ -[UAFAssetUtilities assetAvailableCheckTimeout]
+ -[UAFAssetUtilities assistantQueue]
+ -[UAFAssetUtilities autoRetryDelayOnFailureIncrement]
+ -[UAFAssetUtilities autoRetryDelayOnFailure]
+ -[UAFAssetUtilities autoRetryDelayOnSettingsChanged]
+ -[UAFAssetUtilities autoRetryEnabled]
+ -[UAFAssetUtilities autoRetryLimit]
+ -[UAFAssetUtilities currentAssetStatus]
+ -[UAFAssetUtilities downloadQueue]
+ -[UAFAssetUtilities retryState]
+ -[UAFAssetUtilities setAssetAvailableCheckTimeout:]
+ -[UAFAssetUtilities setAssistantQueue:]
+ -[UAFAssetUtilities setAutoRetryDelayOnFailure:]
+ -[UAFAssetUtilities setAutoRetryDelayOnFailureIncrement:]
+ -[UAFAssetUtilities setAutoRetryDelayOnSettingsChanged:]
+ -[UAFAssetUtilities setAutoRetryEnabled:]
+ -[UAFAssetUtilities setAutoRetryLimit:]
+ -[UAFAssetUtilities setDownloadQueue:]
+ -[UAFAssetUtilities setRetryState:]
+ -[UAFAssetUtilities setStatusQueue:]
+ -[UAFAssetUtilities startObserversWithOptions:]
+ -[UAFAssetUtilities statusQueue]
+ -[UAFAssetUtilitiesService _handleDictationProgress:status:language:]
+ -[UAFAssetUtilitiesService _siriDownloadCompleteForLanguage:]
+ -[UAFAssetUtilitiesService _stopObserver]
+ -[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]
+ -[UAFAssetUtilitiesService _updateDictationAvailabilityForLanguage:]
+ -[UAFAssetUtilitiesService _updateDictationProgress:language:]
+ -[UAFAssetUtilitiesService _updateDictationState:value:forLanguage:]
+ -[UAFAssetUtilitiesService updateSiriAssetAvailabilityForLanguageSync:]
+ -[UAFAssetUtilitiesService updateSiriAssetAvailabilityForObserver]
+ -[UAFAutoAssetSet initWithAssetSetName:autoAssets:uuid:]
+ -[UAFAutoAssetSet setUuid:]
+ -[UAFAutoAssetSet uuid]
+ -[UAFConfigurationManager getMinVersion:provider:]
+ -[UAFConfigurationManager getPrestage:]
+ -[UAFConfigurationManager minVersions:]
+ -[UAFGestalt init]
+ -[UAFGestalt query:forKey:]
+ -[UAFGestalt queryAllSupportedKeys:]
+ -[UAFMinVersionConfiguration .cxx_destruct]
+ -[UAFMinVersionConfiguration assetSetName]
+ -[UAFMinVersionConfiguration initWithDictionary:]
+ -[UAFMinVersionConfiguration minVersions]
+ -[UAFMinVersionConfiguration setAssetSetName:]
+ -[UAFMinVersionConfiguration setMinVersions:]
+ -[UAFPrestageConfiguration .cxx_destruct]
+ -[UAFPrestageConfiguration initWithDictionary:]
+ -[UAFPrestageConfiguration mergeAssetSetUsages:]
+ -[UAFPrestageConfiguration name]
+ -[UAFPrestageConfiguration setName:]
+ -[UAFPrestageConfiguration setUsages:]
+ -[UAFPrestageConfiguration usages:]
+ -[UAFPrestageConfiguration usages]
+ -[UAFRetryState cancelled]
+ -[UAFRetryState pending]
+ -[UAFRetryState retryCount]
+ -[UAFRetryState setCancelled:]
+ -[UAFRetryState setPending:]
+ -[UAFRetryState setRetryCount:]
+ -[UAFXPCConnection lockLatestAtomicInstance:completion:]
+ -[UAFXPCService configureCacheDeleteWithConfig:completion:]
+ -[UAFXPCService lockLatestAtomicInstance:completion:]
+ -[UAFXPCService runUpdates]
+ GCC_except_table11
+ GCC_except_table18
+ GCC_except_table19
+ GCC_except_table22
+ GCC_except_table25
+ GCC_except_table26
+ GCC_except_table36
+ GCC_except_table39
+ GCC_except_table40
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table64
+ GCC_except_table66
+ _NSFileType
+ _NSFileTypeRegular
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_UAFAssetSetMetadata
+ _OBJC_CLASS_$_UAFGestalt
+ _OBJC_CLASS_$_UAFMinVersionConfiguration
+ _OBJC_CLASS_$_UAFPreinstalledAssetsCache
+ _OBJC_CLASS_$_UAFPrestageConfiguration
+ _OBJC_CLASS_$_UAFRetryState
+ _OBJC_IVAR_$_UAFAssetConfiguration._ignoreOSCompatibility
+ _OBJC_IVAR_$_UAFAssetSet._assetNameToAutoAsset
+ _OBJC_IVAR_$_UAFAssetSet._minVersions
+ _OBJC_IVAR_$_UAFAssetSetConfiguration._metadataAsset
+ _OBJC_IVAR_$_UAFAssetSetMetadata._maxOSVersion
+ _OBJC_IVAR_$_UAFAssetSetMetadata._minOSVersion
+ _OBJC_IVAR_$_UAFAssetUtilities._assetAvailableCheckTimeout
+ _OBJC_IVAR_$_UAFAssetUtilities._autoRetryDelayOnFailure
+ _OBJC_IVAR_$_UAFAssetUtilities._autoRetryDelayOnFailureIncrement
+ _OBJC_IVAR_$_UAFAssetUtilities._autoRetryDelayOnSettingsChanged
+ _OBJC_IVAR_$_UAFAssetUtilities._autoRetryEnabled
+ _OBJC_IVAR_$_UAFAssetUtilities._autoRetryLimit
+ _OBJC_IVAR_$_UAFAssetUtilities._downloadQueue
+ _OBJC_IVAR_$_UAFAssetUtilities._networkExpensive
+ _OBJC_IVAR_$_UAFAssetUtilities._networkSatisfied
+ _OBJC_IVAR_$_UAFAssetUtilities._observerOptions
+ _OBJC_IVAR_$_UAFAssetUtilities._pathEvaluator
+ _OBJC_IVAR_$_UAFAssetUtilities._retryState
+ _OBJC_IVAR_$_UAFAssetUtilitiesService._retryCount
+ _OBJC_IVAR_$_UAFAutoAssetSet._uuid
+ _OBJC_IVAR_$_UAFMinVersionConfiguration._assetSetName
+ _OBJC_IVAR_$_UAFMinVersionConfiguration._minVersions
+ _OBJC_IVAR_$_UAFPrestageConfiguration._name
+ _OBJC_IVAR_$_UAFPrestageConfiguration._usages
+ _OBJC_IVAR_$_UAFRetryState._cancelled
+ _OBJC_IVAR_$_UAFRetryState._pending
+ _OBJC_IVAR_$_UAFRetryState._retryCount
+ _OBJC_METACLASS_$_UAFAssetSetMetadata
+ _OBJC_METACLASS_$_UAFGestalt
+ _OBJC_METACLASS_$_UAFMinVersionConfiguration
+ _OBJC_METACLASS_$_UAFPreinstalledAssetsCache
+ _OBJC_METACLASS_$_UAFPrestageConfiguration
+ _OBJC_METACLASS_$_UAFRetryState
+ _UAFLogContextLargeMessage
+ _UAFLogContextMAConfig
+ _UAFLogContextUAFTool
+ __MapTrialProjectsToNamespacesFromConfig
+ __OBJC_$_CLASS_METHODS_UAFAssetSetMetadata
+ __OBJC_$_CLASS_METHODS_UAFGestalt
+ __OBJC_$_CLASS_METHODS_UAFMinVersionConfiguration
+ __OBJC_$_CLASS_METHODS_UAFPreinstalledAssetsCache
+ __OBJC_$_CLASS_METHODS_UAFPrestageConfiguration
+ __OBJC_$_CLASS_PROP_LIST_UAFGestalt
+ __OBJC_$_INSTANCE_METHODS_UAFAssetSetMetadata
+ __OBJC_$_INSTANCE_METHODS_UAFGestalt
+ __OBJC_$_INSTANCE_METHODS_UAFMinVersionConfiguration
+ __OBJC_$_INSTANCE_METHODS_UAFPrestageConfiguration
+ __OBJC_$_INSTANCE_METHODS_UAFRetryState
+ __OBJC_$_INSTANCE_VARIABLES_UAFAssetSetMetadata
+ __OBJC_$_INSTANCE_VARIABLES_UAFMinVersionConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_UAFPrestageConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_UAFRetryState
+ __OBJC_$_PROP_LIST_UAFAssetSetMetadata
+ __OBJC_$_PROP_LIST_UAFMinVersionConfiguration
+ __OBJC_$_PROP_LIST_UAFPrestageConfiguration
+ __OBJC_$_PROP_LIST_UAFRetryState
+ __OBJC_CLASS_RO_$_UAFAssetSetMetadata
+ __OBJC_CLASS_RO_$_UAFGestalt
+ __OBJC_CLASS_RO_$_UAFMinVersionConfiguration
+ __OBJC_CLASS_RO_$_UAFPreinstalledAssetsCache
+ __OBJC_CLASS_RO_$_UAFPrestageConfiguration
+ __OBJC_CLASS_RO_$_UAFRetryState
+ __OBJC_METACLASS_RO_$_UAFAssetSetMetadata
+ __OBJC_METACLASS_RO_$_UAFGestalt
+ __OBJC_METACLASS_RO_$_UAFMinVersionConfiguration
+ __OBJC_METACLASS_RO_$_UAFPreinstalledAssetsCache
+ __OBJC_METACLASS_RO_$_UAFPrestageConfiguration
+ __OBJC_METACLASS_RO_$_UAFRetryState
+ ___112+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:]_block_invoke.333
+ ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.341
+ ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.342
+ ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.343
+ ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.344
+ ___134-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:storeManager:configurationManager:]_block_invoke
+ ___134-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:storeManager:configurationManager:]_block_invoke_2
+ ___134-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:storeManager:configurationManager:]_block_invoke_3
+ ___134-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:storeManager:configurationManager:]_block_invoke_4
+ ___134-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:storeManager:configurationManager:]_block_invoke_5
+ ___134-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:storeManager:configurationManager:]_block_invoke_6
+ ___134-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:storeManager:configurationManager:]_block_invoke_7
+ ___173+[UAFTrialUpdateManager updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]_block_invoke.254
+ ___173+[UAFTrialUpdateManager updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]_block_invoke.256
+ ___173+[UAFTrialUpdateManager updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]_block_invoke.257
+ ___173+[UAFTrialUpdateManager updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]_block_invoke.258
+ ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke.272
+ ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_2.273
+ ___27+[UAFGestalt sharedManager]_block_invoke
+ ___27-[UAFGestalt query:forKey:]_block_invoke
+ ___27-[UAFXPCService runUpdates]_block_invoke
+ ___27-[UAFXPCService runUpdates]_block_invoke.270
+ ___28-[UAFAssetSet overlayRoots:]_block_invoke.302
+ ___30+[UAFAssetSetManager defaults]_block_invoke
+ ___31-[UAFXPCConnection _connection]_block_invoke.239
+ ___32+[UAFAssetSetMetadata OSVersion]_block_invoke
+ ___36-[UAFGestalt queryAllSupportedKeys:]_block_invoke
+ ___37+[UAFCommonUtilities resetAutoAssets]_block_invoke
+ ___37+[UAFCommonUtilities resetAutoAssets]_block_invoke_2
+ ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke.255
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.324
+ ___39+[UAFPreinstalledAssetsCache initCache]_block_invoke
+ ___39+[UAFPreinstalledAssetsCache initCache]_block_invoke_2
+ ___39+[UAFPreinstalledAssetsCache initCache]_block_invoke_3
+ ___39-[UAFAssetUtilities currentAssetStatus]_block_invoke
+ ___39-[UAFAssetUtilities downloadSiriAssets]_block_invoke
+ ___42-[UAFXPCConnection diagnosticInformation:]_block_invoke.242
+ ___45-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke.273
+ ___45-[UAFAssetUtilities _downloadSiriAssetsRetry]_block_invoke
+ ___46-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke
+ ___46-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke.267
+ ___47-[UAFAssetUtilities _refreshUAFAssetStatusSync]_block_invoke_2
+ ___47-[UAFAssetUtilities downloadSiriAssetsIfNeeded]_block_invoke
+ ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke
+ ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke.241
+ ___47-[UAFAssetUtilities startObserversWithOptions:]_block_invoke.244
+ ___48-[UAFAssetSet getAutoAssetPreinstalledForRoots:]_block_invoke
+ ___50-[UAFAssetUtilities _downloadSiriAssetsWithDelay:]_block_invoke
+ ___51+[UAFAutoAssetSet latestAtomicInstance:completion:]_block_invoke
+ ___51+[UAFAutoAssetSet latestAtomicInstance:completion:]_block_invoke.247
+ ___51-[UAFAssetUtilities downloadSiriAssetsOverCellular]_block_invoke
+ ___51-[UAFXPCConnection operationWithConfig:completion:]_block_invoke.241
+ ___53+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke
+ ___53+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke.308
+ ___53+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke_2
+ ___53+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke_2.309
+ ___53+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke_3
+ ___53+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke_4
+ ___53+[UAFAutoAssetManager removeAutoAssetSet:completion:]_block_invoke
+ ___53-[UAFAssetUtilities _downloadSiriAssetsOverCellular:]_block_invoke.269
+ ___53-[UAFXPCService lockLatestAtomicInstance:completion:]_block_invoke
+ ___54+[UAFAutoAssetManager logAtomicInstance:name:entries:]_block_invoke
+ ___56+[UAFPreinstalledAssetsCache queryAssetType:attributes:]_block_invoke
+ ___56-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke
+ ___56-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke.244
+ ___56-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke_2
+ ___59-[UAFAssetUtilities _assistantPreferencesAndLanguageUpdate]_block_invoke.278
+ ___60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke.288
+ ___62+[UAFPreinstalledAssetsCache assetNamed:assetType:attributes:]_block_invoke
+ ___62-[UAFXPCConnection downloadSizeInBytesForLanguage:completion:]_block_invoke.257
+ ___63+[UAFAssetSetManager subscribe:subscriptions:queue:completion:]_block_invoke.254
+ ___63+[UAFAssetSetManager subscribe:subscriptions:queue:completion:]_block_invoke.257
+ ___63-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke
+ ___63-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke.261
+ ___65+[UAFAssetSetManager unsubscribe:subscriptions:queue:completion:]_block_invoke.259
+ ___65+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:]_block_invoke
+ ___65+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:]_block_invoke.328
+ ___66+[UAFPreinstalledAssetsCache lookupStringForAsset:withAttributes:]_block_invoke
+ ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke.281
+ ___66-[UAFAssetUtilitiesService updateSiriAssetAvailabilityForObserver]_block_invoke
+ ___71+[UAFAutoAssetManager shouldCheckAssetSet:autoAssetSet:changed:locked:]_block_invoke
+ ___71-[UAFAssetUtilitiesService updateSiriAssetAvailabilityForLanguageSync:]_block_invoke
+ ___71-[UAFAssetUtilitiesService updateSiriAssetAvailabilityForLanguageSync:]_block_invoke_2
+ ___72-[UAFAssetUtilities _assetsAreAvailableForLanguageSync:delegateEnabled:]_block_invoke
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.266
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.277
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.279
+ ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke_2.280
+ ___77+[UAFAssetSetManager disableCacheDelete:forAutoAssetType:autoAssetSpecifier:]_block_invoke
+ ___78-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:delegateEnabled:]_block_invoke
+ ___78-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:delegateEnabled:]_block_invoke.256
+ ___78-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:delegateEnabled:]_block_invoke_2
+ ___80+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:noAllowed:]_block_invoke
+ ___80+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:noAllowed:]_block_invoke.286
+ ___80+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:noAllowed:]_block_invoke_2
+ ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke.248
+ ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke_3
+ ___83+[UAFAssetSetManager updateAssets:subscription:policies:queue:progress:completion:]_block_invoke
+ ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke
+ ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke.356
+ ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke_2
+ ___88-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]_block_invoke_3
+ ___90-[UAFAssetSetObserver initWithAssetSet:configurationDirURLs:queue:updateHandler:delegate:]_block_invoke.252
+ ___93+[UAFAssetSetManager updateAssets:subscription:policies:queue:progressWithStatus:completion:]_block_invoke
+ ___98+[UAFAutoAssetManager conditionallyLockLatestAssetSet:newestInstance:checkAtomicError:completion:]_block_invoke
+ ___98+[UAFAutoAssetManager conditionallyLockLatestAssetSet:newestInstance:checkAtomicError:completion:]_block_invoke.338
+ ____RegisterXPCActivity_block_invoke.245
+ ___block_descriptor_40_e8_32bs_e11_v24?0d8Q16ls32l8
+ ___block_descriptor_40_e8_32r_e22_v16?0"NSDictionary"8lr32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSString"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8
+ ___block_descriptor_40_e8_32w_e30_v16?0"NSObject<OS_nw_path>"8lw32l8
+ ___block_descriptor_48_e8_32s40bs_e11_v24?0d8Q16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e22_v16?0"NSDictionary"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e30_v24?0"NSString"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e11_v24?0d8Q16lw40l8s32l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_50_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32r40w_e5_v8?0lw40l8r32l8
+ ___block_descriptor_56_e8_32s40r48r_e30_v24?0"NSNumber"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48w_e22_v16?0"NSDictionary"8lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e42_v32?0"NSString"8"NSArray"16"NSError"24ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e42_v24?0"MAAutoAssetSetStatus"8"NSError"16ls32l8s56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
+ ___block_descriptor_66_e8_32s40s48r56w_e22_v16?0"NSDictionary"8lw56l8s32l8r48l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs72r80r_e42_v32?0"NSString"8"NSArray"16"NSError"24ls32l8r72l8s40l8s48l8r80l8s56l8s64l8
+ ___block_literal_global.240
+ ___block_literal_global.241
+ ___block_literal_global.243
+ ___block_literal_global.246
+ ___block_literal_global.247
+ ___block_literal_global.248
+ ___block_literal_global.250
+ ___block_literal_global.252
+ ___block_literal_global.253
+ ___block_literal_global.254
+ ___block_literal_global.255
+ ___block_literal_global.258
+ ___block_literal_global.259
+ ___block_literal_global.261
+ ___block_literal_global.262
+ ___block_literal_global.322
+ ___block_literal_global.337
+ ___block_literal_global.341
+ __unnamed_array_storage.267
+ __unnamed_array_storage.274
+ __unnamed_array_storage.281
+ _kUAFABCInstanceFailure
+ _kUAFAllDevices
+ _kUAFAssetMetadataUnarchivedSizeKey
+ _kUAFAssetSetMetadataFileType
+ _kUAFAssetSetMetadataFileVersion_1_0_0
+ _kUAFAutoAssetFileLockReason
+ _kUAFDefaultInternalBaseDir
+ _kUAFDisableCacheDeleteKeyPrefix
+ _kUAFGestaltAllDevices
+ _kUAFGestaltGestaltPredicate
+ _kUAFGestaltSupportedKeys
+ _kUAFGestaltTargetingKey
+ _kUAFGestaltTargetingPredicate
+ _kUAFGestaltTargetingType
+ _kUAFGestaltType
+ _kUAFGestaltValues
+ _kUAFGestaltVersion_1_0_0
+ _kUAFIgnoreOSCompatibility
+ _kUAFMaxOSVersion
+ _kUAFMetadataAsset
+ _kUAFMetadataFileName
+ _kUAFMinOSVersion
+ _kUAFMinVersion
+ _kUAFMinVersionConfigurationDir
+ _kUAFMinVersionFileNameSeperator
+ _kUAFMinVersionFileType
+ _kUAFMinVersionFileVersion_1_0_0
+ _kUAFPrestageConfigurationDir
+ _kUAFPrestageFileType
+ _kUAFPrestageFileVersion_1_0_0
+ _kUAFPrestagePredicate
+ _kUAFSuiteName
+ _kUAFTargetingPredicate
+ _kUAFTargetingType
+ _kUAFUsageValue
+ _kUAFUsages
+ _kUAFValidConfigs
+ _kUAFXPCCacheDeleteDisabled
+ _kUAFXPCConfigureCacheDelete
+ _nw_path_create_default_evaluator
+ _nw_path_evaluator_cancel
+ _nw_path_evaluator_copy_path
+ _nw_path_evaluator_set_update_handler
+ _nw_path_get_status
+ _nw_path_is_expensive
+ _objc_moveWeak
+ _objc_msgSend$OSSupported
+ _objc_msgSend$OSVersion
+ _objc_msgSend$_assetsAreAvailableForLanguageSync:delegateEnabled:
+ _objc_msgSend$_createXPCConnection
+ _objc_msgSend$_downloadSiriAssetsRetry
+ _objc_msgSend$_downloadSiriAssetsWithDelay:
+ _objc_msgSend$_handleDictationProgress:status:language:
+ _objc_msgSend$_handleNetworkPathUpdate:
+ _objc_msgSend$_logDailyStatusEventForAssetSetArrived:entries:
+ _objc_msgSend$_networkIsExpensiveForPath:
+ _objc_msgSend$_networkIsSatisfiedForPath:
+ _objc_msgSend$_siriDownloadCompleteForLanguage:
+ _objc_msgSend$_stopObserver
+ _objc_msgSend$_triggerCompletionTimerForLanguage:
+ _objc_msgSend$_updateDelegateForUODAvailable:uodStatus:delegateEnabled:
+ _objc_msgSend$_updateDictationAvailabilityForLanguage:
+ _objc_msgSend$_updateDictationProgress:language:
+ _objc_msgSend$_updateDictationState:value:forLanguage:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$applyAssetTransformations:
+ _objc_msgSend$applyMinVersions:
+ _objc_msgSend$applyOSCompatibility:
+ _objc_msgSend$assetAvailableCheckTimeout
+ _objc_msgSend$assetLockedInhibitsRemoval
+ _objc_msgSend$assetNamed:assetType:attributes:
+ _objc_msgSend$assetVersion
+ _objc_msgSend$assistantGroup
+ _objc_msgSend$assistantQueue
+ _objc_msgSend$attributesOfItemAtPath:error:
+ _objc_msgSend$autoAssetDetailsForAssetNamed:assetSet:usages:autoAssetType:autoAssetSpecifier:
+ _objc_msgSend$autoAssetSet:usages:uuid:
+ _objc_msgSend$autoRetryDelayOnFailure
+ _objc_msgSend$autoRetryDelayOnFailureIncrement
+ _objc_msgSend$autoRetryDelayOnSettingsChanged
+ _objc_msgSend$autoRetryEnabled
+ _objc_msgSend$autoRetryLimit
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$cacheDeleteDefaultsKeyForAutoAssetType:autoAssetSpecifier:
+ _objc_msgSend$cacheDeleteDisabledForAutoAssetType:autoAssetSpecifier:
+ _objc_msgSend$cancelled
+ _objc_msgSend$catalogAssetSetID:
+ _objc_msgSend$catalogCachedAssetSetID
+ _objc_msgSend$compareVersion:with:
+ _objc_msgSend$conditionallyLockLatestAssetSet:newestInstance:checkAtomicError:completion:
+ _objc_msgSend$configureCacheDeleteWithConfig:completion:
+ _objc_msgSend$containsString:
+ _objc_msgSend$createAssetFromPreinstalledWithAutoAssetInfo:assetName:fromRoot:
+ _objc_msgSend$defaults
+ _objc_msgSend$deviceMatch:onMatch:
+ _objc_msgSend$dictionaryForGestalt:
+ _objc_msgSend$dictionaryIsValid:
+ _objc_msgSend$disableCacheDelete:forAutoAssetType:autoAssetSpecifier:
+ _objc_msgSend$eliminateAtomicSync:usingClientDomain:forAssetSetIdentifier:awaitingUnlocked:
+ _objc_msgSend$evaluateWithObject:
+ _objc_msgSend$forceRemoveAutoAssetSet:
+ _objc_msgSend$fromAssetDir:error:
+ _objc_msgSend$fromContentsOfURL:error:
+ _objc_msgSend$getAutoAssetPreinstalledForRoots:
+ _objc_msgSend$getMAPath:
+ _objc_msgSend$getPrestage:
+ _objc_msgSend$ignoreOSCompatibility
+ _objc_msgSend$initForAssetType:withAssetSpecifier:assetLockedInhibitsRemoval:
+ _objc_msgSend$initLockerUsingClientDomain:forAssetSetIdentifier:error:
+ _objc_msgSend$initLockerUsingClientDomain:forAssetSetIdentifier:usingDesiredPolicyCategory:completingFromQueue:error:
+ _objc_msgSend$initWithAssetSetName:autoAssets:uuid:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$invalidatePromotedInstances:autoAssetSet:group:noAllowed:
+ _objc_msgSend$isAssistantEnabled
+ _objc_msgSend$isDictationEnabled
+ _objc_msgSend$isKeySupported:key:
+ _objc_msgSend$latestAtomicInstance:completion:
+ _objc_msgSend$latestAtomicInstanceForClients:OSSupported:error:
+ _objc_msgSend$latestAtomicInstanceFromMA:error:
+ _objc_msgSend$latestDownloadedAtomicInstance
+ _objc_msgSend$lockAtomic:forAtomicInstance:completion:
+ _objc_msgSend$lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:completion:
+ _objc_msgSend$lockAtomicSync:forAtomicInstance:error:
+ _objc_msgSend$lockLatestAssetSet:completion:
+ _objc_msgSend$lockLatestAtomicInstance:completion:
+ _objc_msgSend$logAtomicInstance:name:entries:
+ _objc_msgSend$logDownloadTriggerEventWithLanguage:hasExistingAssets:retryCount:
+ _objc_msgSend$lookupStringForAsset:withAttributes:
+ _objc_msgSend$manageAssetSet:specifiers:lockIfUnchanged:
+ _objc_msgSend$maxOSVersion
+ _objc_msgSend$mergeAssetSetUsages:
+ _objc_msgSend$metadataAsset
+ _objc_msgSend$minOSVersion
+ _objc_msgSend$minVersions
+ _objc_msgSend$minVersions:
+ _objc_msgSend$mobileGestaltQuery:
+ _objc_msgSend$mockAssetStatus
+ _objc_msgSend$newerAtomicInstanceDiscovered
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$pending
+ _objc_msgSend$predicateMatch:
+ _objc_msgSend$predicateWithFormat:
+ _objc_msgSend$queryAssetType:attributes:
+ _objc_msgSend$removeAutoAssetSet:completion:
+ _objc_msgSend$retryCount
+ _objc_msgSend$retryState
+ _objc_msgSend$runUpdates
+ _objc_msgSend$setAssetDownloadSizeInBytes:
+ _objc_msgSend$setAssetUnarchivedSizeInBytes:
+ _objc_msgSend$setAssetsPromoted:purgeabilityLevel:error:
+ _objc_msgSend$setAssetsProvisional:purgeabilityLevel:error:
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setCancelled:
+ _objc_msgSend$setPending:
+ _objc_msgSend$setRetryState:
+ _objc_msgSend$setSupportingShortTermLocks:
+ _objc_msgSend$shouldCheckAssetSet:autoAssetSet:changed:locked:
+ _objc_msgSend$startObserversWithOptions:
+ _objc_msgSend$subscriptionsForSubscriber:
+ _objc_msgSend$systemLanguageLocale
+ _objc_msgSend$trialFeatureEnabled:
+ _objc_msgSend$understandingOnDeviceAssetsAvailable
+ _objc_msgSend$updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:
+ _objc_msgSend$updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:storeManager:configurationManager:
+ _objc_msgSend$updateSiriAssetAvailabilityForLanguageSync:
+ _objc_msgSend$updateSiriAssetAvailabilityForObserver
+ _objc_msgSend$urlForGestalt:
+ _objc_msgSend$usages:
+ _objc_msgSend$value
+ _os_variant_has_internal_content
- +[UAFAssetSet autoAssetSet:usages:]
- +[UAFAssetSetManager updateAssets:subscription:policies:queue:progressWithStatus:completion:storeManager:configurationManager:]
- +[UAFAutoAssetInstance autoAssetEntryToAsset:withAssetName:]
- +[UAFAutoAssetInstance instanceFileURL:atomicInstance:]
- +[UAFAutoAssetInstance loadInstanceWithAssetSetName:]
- +[UAFAutoAssetInstance loadInstanceWithURL:]
- +[UAFAutoAssetInstance removeInstanceWithAssetSetName:atomicInstance:]
- +[UAFAutoAssetInstance setFileURL:]
- +[UAFAutoAssetInstance validateAllInstances]
- +[UAFAutoAssetManager assetSetAvailable:error:]
- +[UAFAutoAssetManager handleDownloadedAndUnavailable:specifiers:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:]
- +[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:]
- +[UAFAutoAssetManager lockLatestAssetSet:]
- +[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:eliminateAndRetry:]
- +[UAFAutoAssetManager removeAutoAssetSet:]
- +[UAFCommonUtilities _eliminateAutoAssetSet:]
- +[UAFCommonUtilities _resetAutoAssetSets:]
- +[UAFCommonUtilities setEPRIfNeeded]
- +[UAFTrialMAAssetsCache checkForAssetTypePath:]
- +[UAFTrialMAAssetsCache getFactor:asRoot:assetType:matchingAttribute:attributeValue:]
- +[UAFTrialMAAssetsCache initCache]
- +[UAFTrialMAAssetsCache invalidateCache]
- +[UAFTrialMAAssetsCache lookupStringForFactor:asRoot:matchingAttribute:attributeValue:]
- +[UAFTrialMAAssetsCache queryFactor:asRoot:assetType:matchingAttribute:attributeValue:]
- +[UAFXPCService _isAssistantEnabled]
- +[UAFXPCService _isDictationEnabled]
- +[UAFXPCService _systemLanguageLocale]
- -[UAFAssetSetObserver rootNotifyToken]
- -[UAFAssetSetObserver setRootNotifyToken:]
- -[UAFAssetUtilities _emitDownloadTriggerEventWithLanguage:hasExistingAssets:]
- -[UAFAssetUtilities _handleNetworkPathUpdate]
- -[UAFAssetUtilities _hasInexpensiveNetwork]
- -[UAFAssetUtilities _networkIsSatisfied]
- -[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]
- -[UAFAssetUtilities observeValueForKeyPath:ofObject:change:context:]
- -[UAFAssetUtilities setUtilityQueue:]
- -[UAFAssetUtilities utilityQueue]
- -[UAFAssetUtilitiesService _handleDictationProgress:language:]
- -[UAFAssetUtilitiesService setSettingsConnection:]
- -[UAFAssetUtilitiesService settingsConnection]
- -[UAFAssetUtilitiesService stopObserver]
- -[UAFAssetUtilitiesService updateDictationState:withValue:forLanguage:]
- -[UAFAutoAssetInstance .cxx_destruct]
- -[UAFAutoAssetInstance assetSetName]
- -[UAFAutoAssetInstance assetsFromSpecifiers:]
- -[UAFAutoAssetInstance assets]
- -[UAFAutoAssetInstance atomicInstance]
- -[UAFAutoAssetInstance dealloc]
- -[UAFAutoAssetInstance encodeToDictionary]
- -[UAFAutoAssetInstance initWithAssetSetName:atomicInstance:entries:]
- -[UAFAutoAssetInstance initWithDictionary:]
- -[UAFAutoAssetInstance isValid]
- -[UAFAutoAssetInstance lockFileFD]
- -[UAFAutoAssetInstance lockForLoading]
- -[UAFAutoAssetInstance lockForRemoval]
- -[UAFAutoAssetInstance setAssetSetName:]
- -[UAFAutoAssetInstance setAssets:]
- -[UAFAutoAssetInstance setAtomicInstance:]
- -[UAFAutoAssetInstance setLatest:]
- -[UAFAutoAssetInstance setLockFileFD:]
- -[UAFAutoAssetInstance unlock]
- -[UAFAutoAssetSet catalogAssetSetID]
- -[UAFAutoAssetSet initWithAssetSetName:autoAssets:]
- -[UAFAutoAssetSet instance]
- -[UAFAutoAssetSet setInstance:]
- GCC_except_table0
- GCC_except_table15
- GCC_except_table17
- GCC_except_table2
- GCC_except_table21
- GCC_except_table3
- GCC_except_table30
- GCC_except_table34
- GCC_except_table56
- _OBJC_CLASS_$_UAFTrialMAAssetsCache
- _OBJC_IVAR_$_UAFAssetSetObserver._rootNotifyToken
- _OBJC_IVAR_$_UAFAssetUtilities._observerEnabled
- _OBJC_IVAR_$_UAFAssetUtilities._retryCount
- _OBJC_IVAR_$_UAFAssetUtilities._utilityQueue
- _OBJC_IVAR_$_UAFAssetUtilitiesService._settingsConnection
- _OBJC_IVAR_$_UAFAutoAssetInstance._assetSetName
- _OBJC_IVAR_$_UAFAutoAssetInstance._assets
- _OBJC_IVAR_$_UAFAutoAssetInstance._atomicInstance
- _OBJC_IVAR_$_UAFAutoAssetInstance._lockFileFD
- _OBJC_IVAR_$_UAFAutoAssetSet._instance
- _OBJC_IVAR_$_UAFXPCService._subscriptions
- _OBJC_METACLASS_$_UAFTrialMAAssetsCache
- __OBJC_$_CLASS_METHODS_UAFTrialMAAssetsCache
- __OBJC_$_CLASS_METHODS_UAFXPCService
- __OBJC_$_INSTANCE_METHODS_UAFAutoAssetInstance
- __OBJC_$_INSTANCE_VARIABLES_UAFAutoAssetInstance
- __OBJC_$_PROP_LIST_UAFAutoAssetInstance
- __OBJC_CLASS_RO_$_UAFTrialMAAssetsCache
- __OBJC_METACLASS_RO_$_UAFTrialMAAssetsCache
- ___100-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:]_block_invoke
- ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.286
- ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.287
- ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.288
- ___127+[UAFAssetSetManager updateAssets:subscription:policies:queue:progressWithStatus:completion:storeManager:configurationManager:]_block_invoke
- ___127+[UAFAssetSetManager updateAssets:subscription:policies:queue:progressWithStatus:completion:storeManager:configurationManager:]_block_invoke_2
- ___127+[UAFAssetSetManager updateAssets:subscription:policies:queue:progressWithStatus:completion:storeManager:configurationManager:]_block_invoke_3
- ___127+[UAFAssetSetManager updateAssets:subscription:policies:queue:progressWithStatus:completion:storeManager:configurationManager:]_block_invoke_4
- ___127+[UAFAssetSetManager updateAssets:subscription:policies:queue:progressWithStatus:completion:storeManager:configurationManager:]_block_invoke_5
- ___127+[UAFAssetSetManager updateAssets:subscription:policies:queue:progressWithStatus:completion:storeManager:configurationManager:]_block_invoke_6
- ___127+[UAFAssetSetManager updateAssets:subscription:policies:queue:progressWithStatus:completion:storeManager:configurationManager:]_block_invoke_7
- ___134+[UAFAutoAssetManager handleDownloadedAndUnavailable:specifiers:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:]_block_invoke
- ___173+[UAFTrialUpdateManager updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]_block_invoke.230
- ___173+[UAFTrialUpdateManager updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]_block_invoke.233
- ___173+[UAFTrialUpdateManager updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]_block_invoke.234
- ___173+[UAFTrialUpdateManager updateOnDemandFactors:trialFactors:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:updateProgress:completion:]_block_invoke.235
- ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke.249
- ___188+[UAFTrialUpdateManager updateTrialFactors:rolloutUpdateMode:removeUnneededFactors:expensiveNetworking:updateCount:storeManager:noRemovalNamespaces:assetSetNamespaces:progress:completion:]_block_invoke_2.250
- ___31-[UAFAutoAssetInstance isValid]_block_invoke
- ___31-[UAFXPCConnection _connection]_block_invoke.215
- ___34+[UAFTrialMAAssetsCache initCache]_block_invoke
- ___34+[UAFTrialMAAssetsCache initCache]_block_invoke_2
- ___34+[UAFTrialMAAssetsCache initCache]_block_invoke_3
- ___35-[UAFAssetUtilities startObservers]_block_invoke
- ___37-[UAFXPCConnection checkAssetStatus:]_block_invoke.228
- ___37-[UAFXPCService initWithXPCListener:]_block_invoke
- ___37-[UAFXPCService initWithXPCListener:]_block_invoke.238
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.271
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.272
- ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke
- ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.261
- ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke.262
- ___42-[UAFXPCConnection diagnosticInformation:]_block_invoke.218
- ___44-[UAFAutoAssetSet lockLatestAtomicInstance:]_block_invoke
- ___44-[UAFAutoAssetSet lockLatestAtomicInstance:]_block_invoke_2
- ___45-[UAFAssetUtilities _assistantLanguageUpdate]_block_invoke.253
- ___45-[UAFAssetUtilities _handleNetworkPathUpdate]_block_invoke
- ___45-[UAFAssetUtilities _handleNetworkPathUpdate]_block_invoke.243
- ___47-[UAFAssetUtilities _refreshUAFAssetStatusSync]_block_invoke.233
- ___51-[UAFXPCConnection operationWithConfig:completion:]_block_invoke.217
- ___53+[UAFManagedSubscriptions managePlatformSubscription]_block_invoke
- ___55-[UAFAssetUtilities assetsAreAvailableForLanguageSync:]_block_invoke
- ___59-[UAFAssetUtilities _assistantPreferencesAndLanguageUpdate]_block_invoke.258
- ___60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke.254
- ___60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke.258
- ___60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke.259
- ___60+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke_2
- ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke
- ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke.229
- ___62-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke_2
- ___62-[UAFAssetUtilitiesService _handleDictationProgress:language:]_block_invoke
- ___62-[UAFXPCConnection downloadSizeInBytesForLanguage:completion:]_block_invoke.230
- ___63+[UAFAssetSetManager subscribe:subscriptions:queue:completion:]_block_invoke.224
- ___63+[UAFAssetSetManager subscribe:subscriptions:queue:completion:]_block_invoke.227
- ___64-[UAFAssetUtilitiesService _updateAssetState:value:forLanguage:]_block_invoke
- ___64-[UAFAssetUtilitiesService _updateAssetState:value:forLanguage:]_block_invoke.257
- ___65+[UAFAssetSetManager unsubscribe:subscriptions:queue:completion:]_block_invoke.229
- ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke.255
- ___66-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke_2
- ___67-[UAFAssetUtilitiesService updateSiriAssetAvailabilityForLanguage:]_block_invoke_2
- ___70+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:]_block_invoke
- ___70+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:]_block_invoke.252
- ___70+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:]_block_invoke_2
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.233
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.250
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke.252
- ___76-[UAFAssetUtilitiesService _downloadDictationAssetsForLanguage:useCellular:]_block_invoke_2.253
- ___80-[UAFAssetUtilitiesService _downloadUnderstandingAssetsForLanguage:useCellular:]_block_invoke.224
- ___83+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:eliminateAndRetry:]_block_invoke
- ___85+[UAFTrialMAAssetsCache getFactor:asRoot:assetType:matchingAttribute:attributeValue:]_block_invoke
- ___87+[UAFTrialMAAssetsCache queryFactor:asRoot:assetType:matchingAttribute:attributeValue:]_block_invoke
- ___90-[UAFAssetSetObserver initWithAssetSet:configurationDirURLs:queue:updateHandler:delegate:]_block_invoke.228
- ___SiriAnalyticsLibraryCore_block_invoke
- ____RegisterXPCActivity_block_invoke.222
- ___block_descriptor_32_e30_v24?0"NSString"8"NSError"16l
- ___block_descriptor_40_e8_32bs_e11_v24?0Q8Q16ls32l8
- ___block_descriptor_40_e8_32bs_e8_v12?0i8ls32l8
- ___block_descriptor_41_e8_32s_e24_v32?0"MAAsset"8Q16^B24ls32l8
- ___block_descriptor_42_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32s40bs_e11_v24?0Q8Q16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e22_v16?0"NSDictionary"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e11_v24?0Q8Q16lw40l8s32l8
- ___block_descriptor_56_e8_32s40s48s_e42_v24?0"MAAutoAssetSetStatus"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e42_v32?0"NSString"8"NSArray"16"NSError"24ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40r48r56w_e30_v24?0"NSNumber"8"NSError"16lw56l8r40l8r48l8s32l8
- ___block_descriptor_65_e8_32s40s48r56w_e22_v16?0"NSDictionary"8lw56l8s32l8r48l8s40l8
- ___block_descriptor_66_e8_32s40s48s56s_e42_v32?0"NSString"8"NSArray"16"NSError"24ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
- ___block_descriptor_73_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8s48l8r64l8s56l8
- ___block_literal_global.211
- ___block_literal_global.217
- ___block_literal_global.220
- ___block_literal_global.221
- ___block_literal_global.222
- ___block_literal_global.223
- ___block_literal_global.224
- ___block_literal_global.225
- ___block_literal_global.227
- ___block_literal_global.229
- ___block_literal_global.231
- ___block_literal_global.233
- ___block_literal_global.234
- ___block_literal_global.236
- ___block_literal_global.238
- ___block_literal_global.269
- ___block_literal_global.270
- ___block_literal_global.307
- ___getAssistantSiriAnalyticsClass_block_invoke
- __unnamed_array_storage.243
- __unnamed_array_storage.250
- __unnamed_array_storage.257
- _audit_stringSiriAnalytics
- _close
- _objc_msgSend$_eliminateAutoAssetSet:
- _objc_msgSend$_emitDownloadTriggerEventWithLanguage:hasExistingAssets:
- _objc_msgSend$_handleDictationProgress:language:
- _objc_msgSend$_handleNetworkPathUpdate
- _objc_msgSend$_isAssistantEnabled
- _objc_msgSend$_isDictationEnabled
- _objc_msgSend$_networkIsSatisfied
- _objc_msgSend$_resetAutoAssetSets:
- _objc_msgSend$_systemLanguageLocale
- _objc_msgSend$_updateDelegateForUODAvailable:uodStatus:
- _objc_msgSend$addObserver:forKeyPath:options:context:
- _objc_msgSend$allValues
- _objc_msgSend$assetSetAvailable:error:
- _objc_msgSend$assetsFromSpecifiers:
- _objc_msgSend$atomicInstance
- _objc_msgSend$autoAssetSet:usages:
- _objc_msgSend$catalogAssetSetID
- _objc_msgSend$currentSetStatus:
- _objc_msgSend$eliminateAllForAssetTypeSync:
- _objc_msgSend$eliminateAllForSelectorSync:
- _objc_msgSend$eliminateAtomicSync:usingClientDomain:forAssetSetIdentifier:
- _objc_msgSend$fileSystemRepresentation
- _objc_msgSend$formSubAtomicInstanceSync:fromAtomicInstance:toBeComprisedOfEntries:error:
- _objc_msgSend$getFactor:asRoot:assetType:matchingAttribute:attributeValue:
- _objc_msgSend$getFormReason:atomicInstance:
- _objc_msgSend$handleDownloadedAndUnavailable:specifiers:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:
- _objc_msgSend$initForAssetType:withAssetSpecifier:
- _objc_msgSend$initWithAssetSetName:atomicInstance:entries:
- _objc_msgSend$initWithAssetSetName:autoAssets:
- _objc_msgSend$instance
- _objc_msgSend$instanceFileURL:atomicInstance:
- _objc_msgSend$invalidatePromotedInstances:autoAssetSet:group:
- _objc_msgSend$isEqualToDictionary:
- _objc_msgSend$isValid
- _objc_msgSend$linkItemAtURL:toURL:error:
- _objc_msgSend$loadInstanceWithAssetSetName:
- _objc_msgSend$loadInstanceWithURL:
- _objc_msgSend$lockAtomic:forAtomicInstance:withTimeout:completion:
- _objc_msgSend$lockAtomicSync:forAtomicInstance:withTimeout:lockedAtomicEntries:error:
- _objc_msgSend$lockForLoading
- _objc_msgSend$lockForRemoval
- _objc_msgSend$lockLatestAssetSet:
- _objc_msgSend$lookupStringForFactor:asRoot:matchingAttribute:attributeValue:
- _objc_msgSend$manageAssetSet:specifiers:lockIfUnchanged:eliminateAndRetry:
- _objc_msgSend$observeAssetSet:queue:handler:
- _objc_msgSend$queryFactor:asRoot:assetType:matchingAttribute:attributeValue:
- _objc_msgSend$removeAutoAssetSet:
- _objc_msgSend$removeInstanceWithAssetSetName:atomicInstance:
- _objc_msgSend$removeObserver:forKeyPath:
- _objc_msgSend$setAssetSizeOnDisk:
- _objc_msgSend$setEPRIfNeeded
- _objc_msgSend$setFileURL:
- _objc_msgSend$setInstance:
- _objc_msgSend$setLatest:
- _objc_msgSend$settingsConnection
- _objc_msgSend$stopObserver
- _objc_msgSend$unlock
- _objc_msgSend$updateAssets:subscription:policies:queue:progressWithStatus:completion:
- _objc_msgSend$updateAssets:subscription:policies:queue:progressWithStatus:completion:storeManager:configurationManager:
- _objc_msgSend$updateDictationState:withValue:forLanguage:
- _objc_msgSend$utilityQueue
- _objc_msgSend$validateAllInstances
- _open
- _os_variant_has_internal_diagnostics
CStrings:
+ "\x01\x14"
+ "\x011X"
+ "\x02"
+ "\x02\x13"
+ "\a\x15"
+ "\x15"
+ "%@%@"
+ "%@-%@-%@"
+ "%s #settings Auto retry download on enablement change"
+ "%s #settings Auto retry download on language change"
+ "%s #settings Auto retry download on network change"
+ "%s #settings Auto retry is disabled"
+ "%s #settings Current asset state %@ with value %d"
+ "%s #settings Dictation still not available after download completed"
+ "%s #settings Dictation still not available after retrying availability check"
+ "%s #settings Dictation still not available after successful download"
+ "%s #settings Download complete for language %@"
+ "%s #settings Download progress clamped to %d%%"
+ "%s #settings Failed to check UAF asset status due to timeout"
+ "%s #settings Forcing display state to %@ (enabled:%d, hybridUOD:%d, fullUOD:%d)"
+ "%s #settings Forcing display state to %@ due to UOD available"
+ "%s #settings Forcing unknown server state to not started until WiFi gets enabled"
+ "%s #settings Refresh server side asset state %@ with value %d"
+ "%s #settings Retry attempt %d"
+ "%s #settings Retry attempt %d skipped"
+ "%s #settings Returning state %@ with value %d"
+ "%s #settings Skip retry after hitting limit %d"
+ "%s #settings Skip retry attempt on pending execution"
+ "%s #settings Start UAFAssetStatus observer"
+ "%s #settings Start UOD observer"
+ "%s #settings Start language observer"
+ "%s #settings Start network observer"
+ "%s #settings Start observers"
+ "%s #settings Start preferences observer"
+ "%s #settings Stop observers"
+ "%s #settings Using mock asset state %@ with value %d"
+ "%s #settings asset status delegate"
+ "%s #settings asset status update requested"
+ "%s #settings nil completion"
+ "%s #settings server UOD check for language %@"
+ "%s %@ Lock reason: %@, locks: %@"
+ "%s %@ is an allowed specifier for %@, skipping"
+ "%s %{public}@ Failed to unlock asset set %{public}@ instance %{public}@"
+ "%s %{public}@ Unlocked asset set %{public}@ atomic instance %{public}@"
+ "%s %{public}@: Asset %{public}@ in asset set %{public}@ included as it ignores OS compatibility"
+ "%s %{public}@: Asset set %{public}@ with minOSVersion %{public}@ and maxOSVersion %{public}@ incompatible with current OS Version %{public}@"
+ "%s %{public}@: Asset set dealloc'd"
+ "%s %{public}@: Asset set initialized for %{public}@"
+ "%s %{public}@: Cannot load promotion state for asset set %{public}@"
+ "%s %{public}@: Cannot promote nonexistent asset %{public}@ in asset set %{public}@"
+ "%s %{public}@: Cannot promote unpromotable asset %{public}@ in asset set %{public}@"
+ "%s %{public}@: Cannot set provisional nonexistent asset %{public}@ in asset set %{public}@"
+ "%s %{public}@: Cannot set provisional unpromotable asset %{public}@ in asset set %{public}@"
+ "%s %{public}@: Could not get status of auto asset  %{public}@ : %{public}@"
+ "%s %{public}@: Could not get status of auto asset set %{public}@ : %{public}@"
+ "%s %{public}@: Could not get the current status of auto asset  %{public}@ : %{public}@"
+ "%s %{public}@: Could not initialize auto asset set %{public}@ : %{public}@"
+ "%s %{public}@: Could not lock asset set %{public}@: %{public}@"
+ "%s %{public}@: Did not have auto asset set object for set %{public}@ when attempting to gather errors"
+ "%s %{public}@: Failed to load asset set metadata from asset %{public}@ in asset set %{public}@ at location %@: %{public}@"
+ "%s %{public}@: Locked asset set %{public}@ atomic instance %{public}@"
+ "%s %{public}@: Not included %@ as it's version %@ is less than the required minimum %@"
+ "%s %{public}@: Returning %d transformed asset(s)"
+ "%s %{public}@: Returning %{public}@ from MA Root"
+ "%s %{public}@: setAssetsPromoted:purgeabilityLevel: promoteFactorsForNamespace failed for namespace %@: %ld %@"
+ "%s %{public}@: setAssetsProvisional:purgeabilityLevel: setFactorsProvisionalForNamespace failed for namespace %@: %ld %@"
+ "%s %{public}@: using autoasset root for %@"
+ "%s %{public}@: using trial root for %@"
+ "%s Asset promotion disabled in this build."
+ "%s Asset set %{public}@ atomic instance %{public}@ contains:\n%{public}@"
+ "%s AssetSet Identifier: %{public}@: %{public}@"
+ "%s Attempting force removing asset set %{public}@"
+ "%s Auto asset set %{public}@ does not have expected specifiers %{public}@, has %{public}@"
+ "%s Auto asset set %{public}@ extra specifiers: %{public}@"
+ "%s Auto asset set %{public}@ has atomic instance %{public}@, but is not available to clients, locking latest instance"
+ "%s Auto asset set %{public}@ has had its configuration changed"
+ "%s Auto asset set %{public}@ is available and has atomic instance %{public}@"
+ "%s Auto asset set %{public}@ is configured, has atomic instance %{public}@, and is available to clients, no further management needed"
+ "%s Auto asset set %{public}@ is desired but newest published atomic instance %{public}@ from catalog %{public}@ contains no assets"
+ "%s Auto asset set %{public}@ is desired but no atomic instance is available"
+ "%s Auto asset set %{public}@ locking complete with error: %{public}@"
+ "%s Auto asset set %{public}@ missing specifiers: %{public}@"
+ "%s Cache delete disabled for type %{public}@ specifier %{public}@"
+ "%s Cache delete enabled for type %{public}@ specifier %{public}@"
+ "%s Checking %{public}@ was cancelled, retrying"
+ "%s Configuration key %@ is not an %@"
+ "%s Could not end lock of auto asset set %{public}@ atomic instance %{public}@ : %{public}@"
+ "%s Could not find config file for %@"
+ "%s Could not lock auto asset set %{public}@ : %{public}@"
+ "%s Could not lock latest instance of %{public}@: %{public}@"
+ "%s Current OS Version \"%@\" is not a valid version"
+ "%s Decrement locks for atomic instance %{public}@ in auto asset set %{public}@ with reason %{public}@ lockCount: %ld"
+ "%s Dictionary is not valid"
+ "%s Discovered newer instance of %{public}@: %{public}@ vs %{public}@, XPC'ing to siriknowledged to lock"
+ "%s Emitted SADAvailableAssetDailyStatus message for asset sets"
+ "%s Emitting asset set arrived daily status event for auto asset set %{public}@:"
+ "%s Error reading %@: %@"
+ "%s Error retrieving assets for %{public}@ with usages: %{public}@"
+ "%s Evaluating predicate string: '%{public}@'"
+ "%s Failed to find auto asset specifier for asset %{public}@ in asset set %{public}@'"
+ "%s Failed to find auto asset type for asset set %{public}@'"
+ "%s Failed to find configuration for asset set %{public}@'"
+ "%s Failed to get a valid URL for metadata asset %{public}@ in asset set %{public}@ at location %@"
+ "%s Failed to load %@:%@"
+ "%s Failed to load UAFAssetSetMetadata dictionary from \"%@\": %@"
+ "%s Failed to load UAFMinVersionConfiguration dictionary from \"%@\": %@"
+ "%s Failed to load asset set metadata from asset %{public}@ in asset set %{public}@ at location %@: %{public}@"
+ "%s Failed to validate UAFAssetSetMetadata dictionary from \"%@\""
+ "%s Failed to validate UAFMinVersionConfiguration dictionary from \"%@\""
+ "%s Force remove of %{public}@ failed: %@"
+ "%s Forcibly eliminating auto asset %{public}@ using awaitingUnlocked:NO"
+ "%s Generating asset usages log"
+ "%s Generating subscription log"
+ "%s Generating system asset log"
+ "%s Generating system configuration log"
+ "%s Ignoring notification Siri language unchanged from : %{public}@"
+ "%s Invalid %@ value: %@"
+ "%s Locking latest instance of auto asset set %{public}@ although it is unchanged"
+ "%s MA AutoAssetSet's assetSetID is same as assetSetName"
+ "%s MA AutoAssetSet's downloadedCatalogCachedAssetSetID is nil for asset set - %{public}@"
+ "%s MaxOSVersion \"%@\" is not a valid version"
+ "%s MinOSVersion \"%@\" is not a valid version"
+ "%s MinVersion \"%@\" is not a valid version"
+ "%s Mismatched file type %@ vs %@"
+ "%s Mismatched file version %@ vs %@"
+ "%s Missing predicate string"
+ "%s No AutoAssetSpecifier for \"%{public}@\" asset in \"%{public}@\" asset set, skipping"
+ "%s No configuration for asset set: %{public}@"
+ "%s No matching configs for %{public}@"
+ "%s No mobile gestalt answer for %@"
+ "%s No strong completion routine, exiting retry cycle"
+ "%s Not changing cache delete disabled for asset %{public}@ in asset set %{public}@ as it is already %{public}@"
+ "%s Not unlocking %{public}@ as all specifiers allowed"
+ "%s Query returned %d assets"
+ "%s Received notification for %{public}@"
+ "%s Removing autoassetset %{public}@"
+ "%s Sending notification %{public}@"
+ "%s Subscriptions for subscriber: %{public}@: %{public}@"
+ "%s System AssetSetUsages: %{public}@"
+ "%s System Configuration: %{public}@"
+ "%s Unknown targeting type: %@"
+ "%s Unknown targeting type: %{public}@"
+ "%s Usage is not expected kind \"%@\""
+ "%s ValidConfig is not expected kind \"%@\""
+ "%s assetLockedInhibitsRemoval value %{public}@ doesn't match desired value %{public}@ for asset type %{public}@ and specifier %{public}@ in asset set %{public}@"
+ "%s dictionary is null"
+ "%s setAssetsPromoted:purgeabilityLevel: setPurgeabilityLevelsForFactors failed for namespace %@"
+ "%s setAssetsProvisional:purgeabilityLevel: setPurgeabilityLevelsForFactors failed for namespace %@"
+ "%s updateAutoAssetsFromAssetSetUsages complete"
+ "'%@'"
+ "+[UAFAssetSet autoAssetSet:usages:uuid:]"
+ "+[UAFAssetSetManager autoAssetDetailsForAssetNamed:assetSet:usages:autoAssetType:autoAssetSpecifier:]"
+ "+[UAFAssetSetManager disableCacheDelete:forAutoAssetType:autoAssetSpecifier:]_block_invoke"
+ "+[UAFAssetSetManager generateInformationWithError:]"
+ "+[UAFAssetSetMetadata fromContentsOfURL:error:]"
+ "+[UAFAssetSetMetadata isValid:error:]"
+ "+[UAFAutoAssetManager _logDailyStatusEventForAssetSetArrived:entries:]"
+ "+[UAFAutoAssetManager conditionallyLockLatestAssetSet:newestInstance:checkAtomicError:completion:]_block_invoke"
+ "+[UAFAutoAssetManager forceRemoveAutoAssetSet:]"
+ "+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:noAllowed:]"
+ "+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:noAllowed:]_block_invoke"
+ "+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:noAllowed:]_block_invoke_2"
+ "+[UAFAutoAssetManager latestAtomicInstanceForClients:OSSupported:error:]"
+ "+[UAFAutoAssetManager latestAtomicInstanceFromMA:error:]"
+ "+[UAFAutoAssetManager listenForUpdates:updateHandler:]_block_invoke"
+ "+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke"
+ "+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke_4"
+ "+[UAFAutoAssetManager logAtomicInstance:name:entries:]_block_invoke"
+ "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:]"
+ "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:]_block_invoke"
+ "+[UAFAutoAssetManager removeAutoAssetSet:completion:]"
+ "+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]"
+ "+[UAFAutoAssetManager shouldCheckAssetSet:autoAssetSet:changed:locked:]"
+ "+[UAFAutoAssetManager shouldCheckAssetSet:autoAssetSet:changed:locked:]_block_invoke"
+ "+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke_2"
+ "+[UAFAutoAssetSet catalogAssetSetID:]"
+ "+[UAFAutoAssetSet latestAtomicInstance:completion:]"
+ "+[UAFAutoAssetSet latestAtomicInstance:completion:]_block_invoke"
+ "+[UAFCommonUtilities resetAutoAssets]"
+ "+[UAFCommonUtilities resetAutoAssets]_block_invoke"
+ "+[UAFCommonUtilities resetAutoAssets]_block_invoke_2"
+ "+[UAFConfiguration trialFeatureEnabled:]"
+ "+[UAFGestalt deviceMatch:onMatch:]"
+ "+[UAFGestalt dictionaryForGestalt:]"
+ "+[UAFGestalt dictionaryIsValid:]"
+ "+[UAFGestalt predicateMatch:]"
+ "+[UAFInstrumentationProvider logDownloadTriggerEventWithLanguage:hasExistingAssets:retryCount:]"
+ "+[UAFMinVersionConfiguration fromContentsOfURL:error:]"
+ "+[UAFMinVersionConfiguration isValid:error:]"
+ "+[UAFPreinstalledAssetsCache assetNamed:assetType:attributes:]_block_invoke"
+ "+[UAFPreinstalledAssetsCache checkForAssetTypePath:]"
+ "+[UAFPreinstalledAssetsCache queryAssetType:attributes:]"
+ "+[UAFPrestageConfiguration fromContentsOfURL:error:]"
+ "+[UAFPrestageConfiguration isValid:error:]"
+ "+[UAFPrestageConfiguration predicateMatch:]"
+ "-%@=%@"
+ "-[UAFAssetSet applyMinVersions:]"
+ "-[UAFAssetSet applyOSCompatibility:]"
+ "-[UAFAssetSet createAssetFromPreinstalledWithAutoAssetInfo:assetName:fromRoot:]"
+ "-[UAFAssetSet dealloc]"
+ "-[UAFAssetSet setAssetsPromoted:purgeabilityLevel:error:]"
+ "-[UAFAssetSet setAssetsProvisional:purgeabilityLevel:error:]"
+ "-[UAFAssetSetManager assetNamesForAssetSet:usages:]"
+ "-[UAFAssetSetManager disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:]"
+ "-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:storeManager:configurationManager:]"
+ "-[UAFAssetSetMetadata OSSupported]"
+ "-[UAFAssetUtilities _assetsAreAvailableForLanguageSync:delegateEnabled:]"
+ "-[UAFAssetUtilities _downloadSiriAssetsRetry]"
+ "-[UAFAssetUtilities _downloadSiriAssetsRetry]_block_invoke"
+ "-[UAFAssetUtilities _handleNetworkPathUpdate:]"
+ "-[UAFAssetUtilities _handleNetworkPathUpdate:]_block_invoke"
+ "-[UAFAssetUtilities _stopObservers]"
+ "-[UAFAssetUtilities _triggerDelegateAssetStatusUpdated]_block_invoke"
+ "-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:delegateEnabled:]_block_invoke"
+ "-[UAFAssetUtilities assetStatus]"
+ "-[UAFAssetUtilities currentAssetStatus]"
+ "-[UAFAssetUtilities downloadSiriAssetsIfNeeded]_block_invoke"
+ "-[UAFAssetUtilities startObserversWithOptions:]_block_invoke"
+ "-[UAFAssetUtilities startObserversWithOptions:]_block_invoke_2"
+ "-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke"
+ "-[UAFAssetUtilitiesService _siriDownloadCompleteForLanguage:]"
+ "-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]_block_invoke"
+ "-[UAFAssetUtilitiesService _updateDictationAvailabilityForLanguage:]"
+ "-[UAFAssetUtilitiesService _updateDictationProgress:language:]"
+ "-[UAFAssetUtilitiesService updateSiriAssetAvailabilityForLanguageSync:]"
+ "-[UAFAutoAssetSet initWithAssetSetName:autoAssets:uuid:]"
+ "-[UAFConfigurationManager getMinVersion:provider:]"
+ "-[UAFConfigurationManager getPrestage:]"
+ "-[UAFConfigurationManager minVersions:]"
+ "-[UAFGestalt query:forKey:]"
+ "-[UAFGestalt queryAllSupportedKeys:]"
+ "-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke"
+ "-[UAFXPCConnection lockLatestAtomicInstance:completion:]_block_invoke_2"
+ "-[UAFXPCService configureCacheDeleteWithConfig:completion:]"
+ "-[UAFXPCService lockLatestAtomicInstance:completion:]"
+ "-[UAFXPCService runUpdates]"
+ "-[UAFXPCService runUpdates]_block_invoke"
+ ".minversion."
+ "@\"NSObject<OS_nw_path_evaluator>\""
+ "@\"UAFRetryState\""
+ "@24@0:8q16"
+ "@36@0:8@16@24B32"
+ "@40@0:8@16^B24^@32"
+ "ATOMIC_INSTANCE_ELIMINATED"
+ "ATOMIC_INSTANCE_NO_ENTRIES"
+ "AllDevices"
+ "AppleNeuralEngineSubtype"
+ "Asset is not expected kind \"%@\""
+ "AssetSetMetadata"
+ "AutoAsset Instance Missing Asset"
+ "B32@0:8@16@?24"
+ "B44@0:8@16@24B32^B36"
+ "CacheDeleteDisabled"
+ "Configuration key %@ is not an %@"
+ "ConfigureCacheDelete"
+ "Could not eliminate as there are current locks"
+ "DeviceClass"
+ "DisableCacheDelete"
+ "Failed to get auto asset configuration for asset %@ in asset set %@ with usages %@"
+ "GestaltConfiguration"
+ "GestaltPredicate"
+ "HardwarePlatform"
+ "HasAppleNeuralEngine"
+ "I"
+ "I16@0:8"
+ "IgnoreOSCompatibility"
+ "LargeMessage"
+ "MAConfig"
+ "MaxOSVersion"
+ "MaxOSVersion \"%@\" is not a valid version"
+ "MetadataAsset"
+ "Min Versions"
+ "MinOSVersion"
+ "MinOSVersion \"%@\" is not a valid version"
+ "MinVersion"
+ "MinVersion \"%@\" is not a valid version"
+ "MinVersion Configuration"
+ "MinVersions"
+ "OSSupported"
+ "OSVersion"
+ "Prestage"
+ "Prestage Configuration"
+ "PrestageConfiguration"
+ "PrestagePredicate"
+ "ProductType"
+ "ProductVersion"
+ "SupportedKeys"
+ "SystemLanguage"
+ "T@\"NSArray\",&,N,V_usages"
+ "T@\"NSDictionary\",&,N,V_minVersions"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_assistantQueue"
+ "T@\"NSString\",&,N,V_maxOSVersion"
+ "T@\"NSString\",&,N,V_metadataAsset"
+ "T@\"NSString\",&,N,V_minOSVersion"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSUUID\",&,N,V_uuid"
+ "T@\"UAFGestalt\",R,N"
+ "T@\"UAFRetryState\",&,N,V_retryState"
+ "TB,N,V_autoRetryEnabled"
+ "TB,N,V_cancelled"
+ "TB,N,V_ignoreOSCompatibility"
+ "TB,N,V_pending"
+ "TI,N,V_autoRetryLimit"
+ "TI,N,V_retryCount"
+ "TargetingKey"
+ "TargetingPredicate"
+ "TargetingType"
+ "Td,N,V_assetAvailableCheckTimeout"
+ "Td,N,V_autoRetryDelayOnFailure"
+ "Td,N,V_autoRetryDelayOnFailureIncrement"
+ "Td,N,V_autoRetryDelayOnSettingsChanged"
+ "UAFAssetSetMetadata"
+ "UAFGestalt"
+ "UAFMinVersionConfiguration"
+ "UAFPreinstalledAssetsCache"
+ "UAFPrestageConfiguration"
+ "UAFRetryState"
+ "UAFTool"
+ "UsageValue"
+ "Usages"
+ "ValidConfigs"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "_assetAvailableCheckTimeout"
+ "_assetNameToAutoAsset"
+ "_assetsAreAvailableForLanguageSync:delegateEnabled:"
+ "_autoRetryDelayOnFailure"
+ "_autoRetryDelayOnFailureIncrement"
+ "_autoRetryDelayOnSettingsChanged"
+ "_autoRetryEnabled"
+ "_autoRetryLimit"
+ "_cancelled"
+ "_createXPCConnection"
+ "_downloadSiriAssetsRetry"
+ "_downloadSiriAssetsWithDelay:"
+ "_handleDictationProgress:status:language:"
+ "_handleNetworkPathUpdate:"
+ "_ignoreOSCompatibility"
+ "_logDailyStatusEventForAssetSetArrived:entries:"
+ "_maxOSVersion"
+ "_metadataAsset"
+ "_minOSVersion"
+ "_minVersions"
+ "_networkExpensive"
+ "_networkIsExpensiveForPath:"
+ "_networkIsSatisfiedForPath:"
+ "_networkSatisfied"
+ "_observerOptions"
+ "_pathEvaluator"
+ "_pending"
+ "_retryState"
+ "_siriDownloadCompleteForLanguage:"
+ "_stopObserver"
+ "_triggerCompletionTimerForLanguage:"
+ "_updateDelegateForUODAvailable:uodStatus:delegateEnabled:"
+ "_updateDictationAvailabilityForLanguage:"
+ "_updateDictationProgress:language:"
+ "_updateDictationState:value:forLanguage:"
+ "appendFormat:"
+ "applyAssetTransformations:"
+ "applyMinVersions:"
+ "applyOSCompatibility:"
+ "assetAvailableCheckTimeout"
+ "assetLockedInhibitsRemoval"
+ "assetNamed:assetType:attributes:"
+ "assetNamesForAssetSet:usages:"
+ "assetVersion"
+ "assistantQueue"
+ "attributesOfItemAtPath:error:"
+ "autoAssetDetailsForAssetNamed:assetSet:usages:autoAssetType:autoAssetSpecifier:"
+ "autoAssetSet:usages:uuid:"
+ "autoRetryDelayOnFailure"
+ "autoRetryDelayOnFailureIncrement"
+ "autoRetryDelayOnSettingsChanged"
+ "autoRetryEnabled"
+ "autoRetryLimit"
+ "boolForKey:"
+ "cacheDeleteDefaultsKeyForAutoAssetType:autoAssetSpecifier:"
+ "cacheDeleteDisabledForAssetNamed:assetSet:usages:"
+ "cacheDeleteDisabledForAutoAssetType:autoAssetSpecifier:"
+ "cancelled"
+ "catalogAssetSetID:"
+ "catalogCachedAssetSetID"
+ "com.apple.UAF.AssetUtilities.DownloadQueue"
+ "com.apple.UnifiedAssetFramework.UnarchivedSize"
+ "com.apple.siri.tts"
+ "compareVersion:with:"
+ "conditionallyLockLatestAssetSet:newestInstance:checkAtomicError:completion:"
+ "configureCacheDeleteWithConfig:completion:"
+ "containsString:"
+ "createAssetFromPreinstalledWithAutoAssetInfo:assetName:fromRoot:"
+ "currentAssetStatus"
+ "d"
+ "d16@0:8"
+ "defaults"
+ "deviceMatch:onMatch:"
+ "dictionaryForGestalt:"
+ "dictionaryIsValid:"
+ "disableCacheDelete:forAssetNamed:assetSet:usages:queue:completion:"
+ "disableCacheDelete:forAutoAssetType:autoAssetSpecifier:"
+ "disable_trial_com_apple_siri_asr_hammer"
+ "disable_trial_com_apple_siri_dialog"
+ "disable_trial_com_apple_siri_findmy"
+ "disable_trial_com_apple_siri_tts"
+ "disable_trial_com_apple_siri_understanding"
+ "disable_trial_com_apple_siri_understanding_nl_overrides"
+ "dtma"
+ "eliminateAtomicSync:usingClientDomain:forAssetSetIdentifier:awaitingUnlocked:"
+ "evaluateWithObject:"
+ "file locking latest version of"
+ "file://%@%@/Gestalt/%@.plist"
+ "force-"
+ "forceRemoveAutoAssetSet:"
+ "fromAssetDir:error:"
+ "getAutoAssetPreinstalledForRoots:"
+ "getMAPath:"
+ "getMinVersion:provider:"
+ "getPrestage:"
+ "ignoreOSCompatibility"
+ "initForAssetType:withAssetSpecifier:assetLockedInhibitsRemoval:"
+ "initLockerUsingClientDomain:forAssetSetIdentifier:error:"
+ "initLockerUsingClientDomain:forAssetSetIdentifier:usingDesiredPolicyCategory:completingFromQueue:error:"
+ "initWithAssetSetName:autoAssets:uuid:"
+ "initWithSuiteName:"
+ "invalidatePromotedInstances:autoAssetSet:group:noAllowed:"
+ "isAssistantEnabled"
+ "isDictationEnabled"
+ "isKeySupported:key:"
+ "latestAtomicInstance:completion:"
+ "latestAtomicInstanceForClients:OSSupported:error:"
+ "latestAtomicInstanceFromMA:error:"
+ "latestDownloadedAtomicInstance"
+ "lockAtomic:forAtomicInstance:completion:"
+ "lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:completion:"
+ "lockAtomicSync:forAtomicInstance:error:"
+ "lockLatestAssetSet:completion:"
+ "lockLatestAtomicInstance:completion:"
+ "logAtomicInstance:name:entries:"
+ "logDownloadTriggerEventWithLanguage:hasExistingAssets:retryCount:"
+ "lookupStringForAsset:withAttributes:"
+ "manageAssetSet:specifiers:lockIfUnchanged:"
+ "maxOSVersion"
+ "mergeAssetSetUsages:"
+ "metadata.plist"
+ "metadataAsset"
+ "minOSVersion"
+ "minVersions"
+ "minVersions:"
+ "mobileGestaltQuery:"
+ "mobileasset_com_apple_siri_tts"
+ "newerAtomicInstanceDiscovered"
+ "numberWithBool:"
+ "pending"
+ "predicateMatch:"
+ "predicateWithFormat:"
+ "query:forKey:"
+ "queryAllSupportedKeys:"
+ "queryAssetType:attributes:"
+ "removeAutoAssetSet:completion:"
+ "retryCount"
+ "retryState"
+ "runUpdates"
+ "setAssetAvailableCheckTimeout:"
+ "setAssetDownloadSizeInBytes:"
+ "setAssetUnarchivedSizeInBytes:"
+ "setAssetsPromoted:purgeabilityLevel:error:"
+ "setAssetsProvisional:purgeabilityLevel:error:"
+ "setAssistantQueue:"
+ "setAutoRetryDelayOnFailure:"
+ "setAutoRetryDelayOnFailureIncrement:"
+ "setAutoRetryDelayOnSettingsChanged:"
+ "setAutoRetryEnabled:"
+ "setAutoRetryLimit:"
+ "setBool:forKey:"
+ "setCancelled:"
+ "setIgnoreOSCompatibility:"
+ "setMaxOSVersion:"
+ "setMetadataAsset:"
+ "setMinOSVersion:"
+ "setMinVersions:"
+ "setPending:"
+ "setRetryState:"
+ "setSupportingShortTermLocks:"
+ "setUsages:"
+ "setUuid:"
+ "shouldCheckAssetSet:autoAssetSet:changed:locked:"
+ "startObserversWithOptions:"
+ "systemLanguageLocale"
+ "trialFeatureEnabled:"
+ "updateAssetsForSubscriber:subscriptionName:policies:queue:progress:completion:storeManager:configurationManager:"
+ "updateSiriAssetAvailabilityForLanguageSync:"
+ "updateSiriAssetAvailabilityForObserver"
+ "urlForGestalt:"
+ "usages:"
+ "uuid"
+ "v16@?0@\"NSObject<OS_nw_path>\"8"
+ "v20@0:8I16"
+ "v24@0:8d16"
+ "v32@0:8@16B24I28"
+ "v32@0:8B16@20B28"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
+ "v36@0:8B16@20@28"
+ "v56@0:8@16@24@32^@40^@48"
+ "v60@0:8B16@20@28@36@44@?52"
- "\x01\x15"
- "\x026"
- "\x03\x13"
- "\x05\x15"
- "\x13"
- "\x17"
- "%@-%d-%@-%@"
- "%s #settings Forcing unknown server state to not started when network is unavailable."
- "%s #settings Refreshing asset status"
- "%s #settings _updateProgress nil language"
- "%s #settings checkAssetStatus with nil completion"
- "%s %@ invalid: %{public}@ != %{public}@"
- "%s %{public}@: Asset set initialized"
- "%s %{public}@: Returning %d factory assets"
- "%s %{public}@: setAssetsPromoted:purgabilityLevel: promoteFactorsForNamespace failed for namespace %@: %ld %@"
- "%s %{public}@: setAssetsProvisional:purgabilityLevel: setFactorsProvisionalForNamespace failed for namespace %@: %ld %@"
- "%s %{public}@: using root for %@"
- "%s Acquired exclusive lock on %@"
- "%s Acquired shared lock on %@"
- "%s Archived auto asset instance state for asset set %{public}@ to %@ and linked to %@"
- "%s Attempting to eliminate, recreate, and check auto asset set %{public}@ as it has both MAAutoAssetErrorCheckNoWaitNoDownloadedInstance (no assets) and MAAutoAssetErrorSameVersionFound (assets already downloaded)"
- "%s Auto asset instance state at %@ doesn't exist: %{public}@"
- "%s Auto asset instance state for asset set %{public}@ already written to %@ and linked to %@"
- "%s Auto asset set %{public}@ are already available and reflects the current configuration, no further management needed"
- "%s Auto asset set %{public}@ doest not have expected specifiers %{public}@, has %{public}@"
- "%s Auto asset set %{public}@ is available has has atomic instance %{public}@"
- "%s Cannot load promotion state for asset set %{public}@"
- "%s Cannot promote nonexistant asset %{public}@ in asset set %{public}@"
- "%s Cannot promote unpromotable asset %{public}@ in asset set %{public}@"
- "%s Cannot remove \"%@\" yet as it cannot be locked for removal"
- "%s Cannot set provisional nonexistant asset %{public}@ in asset set %{public}@"
- "%s Cannot set provisional unpromotable asset %{public}@ in asset set %{public}@"
- "%s Could not eliminate broken auto asset %{public}@ in %{public}@ : %{public}@"
- "%s Could not eliminate broken auto asset set %{public}@ : %{public}@"
- "%s Could not eliminate serialize version of auto asset %{public}@"
- "%s Could not get status of auto asset  %{public}@ : %{public}@"
- "%s Could not get the current status of auto asset  %{public}@ : %{public}@"
- "%s Could not lock asset set %{public}@: %{public}@"
- "%s Could not remove serialized version of atomic instance %{public}@ in auto asset set %{public}@ with reason %{public}@, and so cannot decrement locks for it"
- "%s Could not unlock atomic instance of auto asset set %{public}@: %{public}@"
- "%s Decrement locks for atomic instance %{public}@ in auto asset set %{public}@ with reason %{public}@"
- "%s Did not have auto asset set object for set %{public}@ when attempting to gather errors"
- "%s Eliminated broken auto asset %{public}@ in %{public}@"
- "%s Eliminated broken auto asset set %{public}@"
- "%s Emitted SADAvailableAssetDailyStatus message for asset sets %{public}@"
- "%s Failed load auto set instance from dictionary as at least one of required fields \"%@\" and %{public}@ weren't present in %{public}@"
- "%s Failed to acquire exclusive lock on %@ as there are existing shared locks: %s"
- "%s Failed to acquire exclusive lock on %@: %s"
- "%s Failed to acquire shared lock on %@: %s"
- "%s Failed to check auto asset set to validate asset set %{public}@ with instance %{public}@: %{public}@"
- "%s Failed to clear stored state of asset set %{public}@ after update error"
- "%s Failed to create auto asset set to validate asset set %{public}@ with instance %{public}@: %{public}@"
- "%s Failed to create dir for auto asset instance state for asset set %{public}@ at %@: %{public}@"
- "%s Failed to create subatomic instance from atomic instance %{public}@ to promoted assets in asset set %{public}@: %{public}@"
- "%s Failed to eliminate %{public}@ due to error %{public}@"
- "%s Failed to generate MAAutoAssetSetEntry for %{public}@ : %{public}@"
- "%s Failed to link auto asset instance state for asset set %{public}@ from %@ to %@: %{public}@"
- "%s Failed to lock asset set %{public}@ with atomic instance %{public}@ after loading instance from storage: %{public}@"
- "%s Failed to lock subatomic instance %{public}@ to promoted assets in asset set %{public}@: %{public}@"
- "%s Failed to notify about removal of asset set %{public}@"
- "%s Failed to notify about update of instance state for asset set %{public}@ from %@ to %@"
- "%s Failed to parse auto asset promotion state from %@"
- "%s Failed to read auto asset instance state from %@ : %{public}@"
- "%s Failed to release lock on %@: %s"
- "%s Failed to remove auto asset instance state for asset set %{public}@ from %@: %{public}@"
- "%s Failed to remove invalid instance at \"%@\": %{public}@"
- "%s Failed to set %{public}@ instance of asset set %{public}@ as latest: %{public}@"
- "%s Failed to unlock asset set %{public}@"
- "%s Failed to write auto asset instance state for asset set %{public}@ to %@: %{public}@"
- "%s Found no locks for %{public}@ with reason \"%{public}@\""
- "%s Instance at \"%@\" is valid"
- "%s Internal build setting EPR audience at boot"
- "%s Loading asset set %{public}@ with atomic instance %{public}@ from storage"
- "%s Locked asset set %{public}@ with atomic instance %{public}@ with MobileAsset after loading from storage"
- "%s MA AutoAssetSet's downloadedCatalogCachedAssetSetID is nil"
- "%s MAAutoAsset eliminateAllForAssetTypeSync returned: %@"
- "%s Not attempting to eliminate, recreate, and check auto asset set %{public}@ as it has assetSetAvailableError %{public}@ and checkAtomicError %{public}@"
- "%s Not marking assets in atomic instance %{public}@ promoted for auto asset %{public}@ in asset set %{public}@ as that instance is already promoted"
- "%s Not marking assets in atomic instance %{public}@ provisional for auto asset %{public}@ in asset set %{public}@ as that instance has already reached max provisional count"
- "%s Not marking assets in atomic instance %{public}@ provisional for auto asset %{public}@ in asset set %{public}@ as that instance is already promoted"
- "%s Parsed auto asset instance state from \"%@\" with:\nasset set name: %{public}@\ninstance: %{public}@\nassets: %{public}@"
- "%s Released lock on %@"
- "%s Removed invalid instance at \"%@\""
- "%s Returning %@"
- "%s Setting provisional count for %{public}@ to %llu in atomic instance %{public}@ of auto asset %{public}@"
- "%s Skipping %@ due to no assetType defined"
- "%s Skipping resetAutoAssets due to nil UAFAssetSetConfiguration"
- "%s setAssetsPromoted:purgabilityLevel: setPurgeabilityLevelsForFactors failed for namespace %@"
- "%s setAssetsProvisional:purgabilityLevel: setPurgeabilityLevelsForFactors failed for namespace %@"
- "+[UAFAssetSet autoAssetSet:usages:]"
- "+[UAFAssetSetManager updateAssets:subscription:policies:queue:progressWithStatus:completion:storeManager:configurationManager:]"
- "+[UAFAutoAssetInstance loadInstanceWithURL:]"
- "+[UAFAutoAssetInstance removeInstanceWithAssetSetName:atomicInstance:]"
- "+[UAFAutoAssetInstance validateAllInstances]"
- "+[UAFAutoAssetManager assetSetAvailable:error:]"
- "+[UAFAutoAssetManager handleDownloadedAndUnavailable:specifiers:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:]"
- "+[UAFAutoAssetManager handleDownloadedAndUnavailable:specifiers:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:]_block_invoke"
- "+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:]"
- "+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:]_block_invoke"
- "+[UAFAutoAssetManager invalidatePromotedInstances:autoAssetSet:group:]_block_invoke_2"
- "+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke"
- "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:eliminateAndRetry:]"
- "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:eliminateAndRetry:]_block_invoke"
- "+[UAFAutoAssetManager removeAutoAssetSet:]"
- "+[UAFAutoAssetManager setLatestAtomicInstance:autoAssetSet:]_block_invoke_2"
- "+[UAFCommonUtilities _eliminateAutoAssetSet:]"
- "+[UAFCommonUtilities _resetAutoAssetSets:]"
- "+[UAFCommonUtilities setEPRIfNeeded]"
- "+[UAFTrialMAAssetsCache checkForAssetTypePath:]"
- "+[UAFTrialMAAssetsCache getFactor:asRoot:assetType:matchingAttribute:attributeValue:]_block_invoke"
- "+[UAFTrialMAAssetsCache queryFactor:asRoot:assetType:matchingAttribute:attributeValue:]"
- "-[UAFAssetSet setAssetsPromoted:purgabilityLevel:error:]"
- "-[UAFAssetSet setAssetsProvisional:purgabilityLevel:error:]"
- "-[UAFAssetSetConfiguration getAssets:]"
- "-[UAFAssetUtilities _emitDownloadTriggerEventWithLanguage:hasExistingAssets:]"
- "-[UAFAssetUtilities _handleNetworkPathUpdate]"
- "-[UAFAssetUtilities _handleNetworkPathUpdate]_block_invoke"
- "-[UAFAssetUtilities _updateDelegateForUODAvailable:uodStatus:]_block_invoke"
- "-[UAFAssetUtilities assetsAreAvailableForLanguageSync:]"
- "-[UAFAssetUtilities downloadSiriAssetsIfNeeded]"
- "-[UAFAssetUtilitiesService _handleDictationCompletionForLanguage:]_block_invoke_2"
- "-[UAFAssetUtilitiesService _handleDictationProgress:language:]"
- "-[UAFAssetUtilitiesService _updateAssetState:value:forLanguage:]_block_invoke"
- "-[UAFAutoAssetInstance initWithDictionary:]"
- "-[UAFAutoAssetInstance isValid]"
- "-[UAFAutoAssetInstance isValid]_block_invoke"
- "-[UAFAutoAssetInstance lockForLoading]"
- "-[UAFAutoAssetInstance lockForRemoval]"
- "-[UAFAutoAssetInstance setLatest:]"
- "-[UAFAutoAssetInstance unlock]"
- "-[UAFAutoAssetSet catalogAssetSetID]"
- "-[UAFAutoAssetSet initWithAssetSetName:autoAssets:]"
- "-[UAFAutoAssetSet lockLatestAtomicInstance:]"
- "-[UAFAutoAssetSet lockLatestAtomicInstance:]_block_invoke"
- "-[UAFAutoAssetSet lockLatestAtomicInstance:]_block_invoke_2"
- "-[UAFXPCService initWithXPCListener:]"
- "-[UAFXPCService initWithXPCListener:]_block_invoke"
- "@\"AFSettingsConnection\""
- "@\"UAFAutoAssetInstance\""
- "@44@0:8@16B24@28@36"
- "@52@0:8@16B24@28@36@44"
- "A"
- "AssistantSiriAnalytics"
- "Locking to see if %@ defined at all"
- "T@\"AFSettingsConnection\",&,N,V_settingsConnection"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_utilityQueue"
- "T@\"NSString\",&,N,V_atomicInstance"
- "T@\"UAFAutoAssetInstance\",&,N,V_instance"
- "Ti,N,V_lockFileFD"
- "Ti,N,V_rootNotifyToken"
- "UAFTrialMAAssetsCache"
- "_atomicInstance"
- "_eliminateAutoAssetSet:"
- "_emitDownloadTriggerEventWithLanguage:hasExistingAssets:"
- "_handleDictationProgress:language:"
- "_handleNetworkPathUpdate"
- "_instance"
- "_isAssistantEnabled"
- "_isDictationEnabled"
- "_lockFileFD"
- "_networkIsSatisfied"
- "_resetAutoAssetSets:"
- "_rootNotifyToken"
- "_settingsConnection"
- "_subscriptions"
- "_systemLanguageLocale"
- "_updateDelegateForUODAvailable:uodStatus:"
- "_utilityQueue"
- "addObserver:forKeyPath:options:context:"
- "allValues"
- "assetSetAvailable:error:"
- "assetsFromSpecifiers:"
- "atomicInstance"
- "autoAssetSet:usages:"
- "catalogAssetSetID"
- "com.apple.UAF.AssetUtilities.UtilityQueue"
- "currentSetStatus:"
- "eliminateAllForAssetTypeSync:"
- "eliminateAllForSelectorSync:"
- "eliminateAtomicSync:usingClientDomain:forAssetSetIdentifier:"
- "fileSystemRepresentation"
- "formSubAtomicInstanceSync:fromAtomicInstance:toBeComprisedOfEntries:error:"
- "getFactor:asRoot:assetType:matchingAttribute:attributeValue:"
- "handleDownloadedAndUnavailable:specifiers:lockIfUnchanged:autoAssetSet:assetSetAvailableError:checkAtomicError:"
- "initForAssetType:withAssetSpecifier:"
- "initWithAssetSetName:atomicInstance:entries:"
- "initWithAssetSetName:autoAssets:"
- "instanceFileURL:atomicInstance:"
- "invalidatePromotedInstances:autoAssetSet:group:"
- "isEqualToDictionary:"
- "isValid"
- "linkItemAtURL:toURL:error:"
- "loadInstanceWithAssetSetName:"
- "loadInstanceWithURL:"
- "lockAtomic:forAtomicInstance:withTimeout:completion:"
- "lockAtomicSync:forAtomicInstance:withTimeout:lockedAtomicEntries:error:"
- "lockFileFD"
- "lockForLoading"
- "lockForRemoval"
- "lockLatestAssetSet:"
- "lookupStringForFactor:asRoot:matchingAttribute:attributeValue:"
- "manageAssetSet:specifiers:lockIfUnchanged:eliminateAndRetry:"
- "observeValueForKeyPath:ofObject:change:context:"
- "placeholder"
- "queryFactor:asRoot:assetType:matchingAttribute:attributeValue:"
- "removeAutoAssetSet:"
- "removeInstanceWithAssetSetName:atomicInstance:"
- "removeObserver:forKeyPath:"
- "rootNotifyToken"
- "setAssetSizeOnDisk:"
- "setAtomicInstance:"
- "setEPRIfNeeded"
- "setFileURL:"
- "setInstance:"
- "setLatest:"
- "setLockFileFD:"
- "setRootNotifyToken:"
- "setSettingsConnection:"
- "setUtilityQueue:"
- "settingsConnection"
- "siriknowledged"
- "softlink:o:path:/System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics"
- "stopObserver"
- "uaftool reset"
- "unlock"
- "updateAssets:subscription:policies:queue:progressWithStatus:completion:storeManager:configurationManager:"
- "updateDictationState:withValue:forLanguage:"
- "utilityQueue"
- "v24@?0Q8Q16"
- "v28@0:8B16@20"
- "v32@?0@\"MAAsset\"8Q16^B24"
- "v40@0:8@16@24B32B36"
- "v48@0:8@16@24@32^v40"
- "v60@0:8@16@24B32@36@44@52"
- "validateAllInstances"
- "validating instance"

```
