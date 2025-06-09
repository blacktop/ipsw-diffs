## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

-300.15.0.0.0
-  __TEXT.__text: 0x183104
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_methlist: 0x18e98
-  __TEXT.__const: 0x3a0
-  __TEXT.__gcc_except_tab: 0x1ad78
-  __TEXT.__cstring: 0x53f5
-  __TEXT.__oslogstring: 0xa618
+336.4.0.0.0
+  __TEXT.__text: 0x18f344
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__objc_methlist: 0x199b0
+  __TEXT.__const: 0x440
+  __TEXT.__gcc_except_tab: 0x1b294
+  __TEXT.__cstring: 0x5a97
+  __TEXT.__oslogstring: 0xb25b
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__unwind_info: 0xf028
-  __TEXT.__objc_classname: 0x4691
-  __TEXT.__objc_methname: 0x199b6
-  __TEXT.__objc_methtype: 0xddd3
-  __TEXT.__objc_stubs: 0x11680
-  __DATA_CONST.__got: 0xc20
-  __DATA_CONST.__const: 0x3ab8
-  __DATA_CONST.__objc_classlist: 0x1168
-  __DATA_CONST.__objc_catlist: 0x130
-  __DATA_CONST.__objc_protolist: 0xd0
+  __TEXT.__unwind_info: 0xf400
+  __TEXT.__objc_classname: 0x470b
+  __TEXT.__objc_methname: 0x1ae5c
+  __TEXT.__objc_methtype: 0xdf5d
+  __TEXT.__objc_stubs: 0x12720
+  __DATA_CONST.__got: 0xc88
+  __DATA_CONST.__const: 0x40c0
+  __DATA_CONST.__objc_classlist: 0x1188
+  __DATA_CONST.__objc_catlist: 0x138
+  __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6250
-  __DATA_CONST.__objc_superrefs: 0x10e8
-  __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x6a0
-  __AUTH_CONST.__const: 0x8a0
-  __AUTH_CONST.__cfstring: 0x6e60
-  __AUTH_CONST.__objc_const: 0x2b3a8
-  __AUTH_CONST.__objc_dictobj: 0x78
+  __DATA_CONST.__objc_selrefs: 0x66d0
+  __DATA_CONST.__objc_superrefs: 0x10f8
+  __DATA_CONST.__objc_arraydata: 0x150
+  __AUTH_CONST.__auth_got: 0x698
+  __AUTH_CONST.__const: 0x9a0
+  __AUTH_CONST.__cfstring: 0x7580
+  __AUTH_CONST.__objc_const: 0x2c170
+  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__objc_intobj: 0x120
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xa410
-  __DATA.__objc_ivar: 0x10d0
-  __DATA.__data: 0xa10
-  __DATA.__bss: 0xe0
-  __DATA_DIRTY.__objc_data: 0xa00
-  __DATA_DIRTY.__bss: 0x198
+  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH.__objc_data: 0xa2f8
+  __DATA.__objc_ivar: 0x1154
+  __DATA.__data: 0xa70
+  __DATA.__bss: 0xf8
+  __DATA_DIRTY.__objc_data: 0xc58
+  __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__bss: 0x1c0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage
   - /System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis
+  - /System/Library/Frameworks/Speech.framework/Speech
   - /System/Library/Frameworks/Translation.framework/Translation
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 91639137-2B70-313D-91AD-0455D0CCE6C6
-  Functions: 9587
-  Symbols:   32690
-  CStrings:  8557
+  UUID: F6FB5146-266C-3A67-B4C5-8F236B941EF0
+  Functions: 9891
+  Symbols:   33610
+  CStrings:  8938
 
Symbols:
+ +[NSError(LTTranslationInternalError) ltd_invalidResultError]
+ +[_LTDASRAssetModel modelFromAsset:]
+ +[_LTDASRAssetService _assetTypesFoDevice]
+ +[_LTDASRAssetService _downloadAsset:progress:completion:]
+ +[_LTDASRAssetService _purgeAsset:completion:]
+ +[_LTDASRAssetService _sfInstalledLTIdentifiersForTaskHint:filter:completion:]
+ +[_LTDASRAssetService _sfSupportedLTIdentifiersForTaskHint:filter:completion:]
+ +[_LTDASRAssetService _sfTaskHintForLTTaskHint:]
+ +[_LTDASRAssetService _supportedIdentifiersWithCommpletion:]
+ +[_LTDASRAssetService _taskHintForLTAssetType:]
+ +[_LTDASRAssetService asrAssetWithIdentifier:taskHint:]
+ +[_LTDASRAssetService availableAssetsWithCompletion:]
+ +[_LTDASRAssetService downloadAsset:options:progress:completion:]
+ +[_LTDASRAssetService downloadAsset:options:progress:completion:].cold.1
+ +[_LTDASRAssetService installedAssetsWithCompletion:]
+ +[_LTDASRAssetService isSupportedTaskHint:]
+ +[_LTDASRAssetService purgeAsset:completion:]
+ +[_LTDASRAssetService purgeAsset:completion:].cold.1
+ +[_LTDASRAssetService queryAssetType:filter:completion:]
+ +[_LTDASRAssetService queue]
+ +[_LTDASRAssetService queue].cold.1
+ +[_LTDASRAssetService supportedLanguagesForTaskHint:]
+ +[_LTDAssetModel _assetStateForOfflineState:]
+ +[_LTDAssetModel _offlineStateForAssetState:]
+ +[_LTDAssetService _addSyntheticASREntriesToAssets:]
+ +[_LTDAssetService _assetProviderForAssetType:]
+ +[_LTDAssetService _assetProviderForAssetType:].cold.1
+ +[_LTDAssetService _awaitDownloadForAsset:]
+ +[_LTDAssetService _errorForAssetProviderResolutionForAssetType:]
+ +[_LTDAssetService _isObsoleteCatalogType:].cold.2
+ +[_LTDConfigurationService supportedIdentifiersForTask:completion:]
+ +[_LTDLanguageAssetService _localeRanks]
+ +[_LTDLanguageAssetService _localeRanks].cold.1
+ +[_LTDLanguageAssetService _localeRanks].cold.2
+ +[_LTDLanguageAssetService _localeRanks].cold.3
+ +[_LTDLanguageAssetService _localeRanks].cold.4
+ +[_LTDLanguageAssetService availableIdentifiers]
+ +[_LTDLanguageAssetService startLanguageStatusSession:taskHint:progress:observations:completion:]
+ +[_LTDMAAssetService purgeAsset:completion:].cold.1
+ +[_LTDTTSAssetService _allTTSAssets]
+ +[_LTDTTSAssetService _mapIdentifierForSiriTTS:]
+ +[_LTDTTSAssetService _subscribeToVoice:]
+ +[_LTDTTSAssetService _subscribeToVoice:].cold.1
+ +[_LTDTTSAssetService downloadAsset:options:progress:completion:].cold.1
+ +[_LTDUAFAssetService _allAssetLocales]
+ +[_LTDUAFAssetService _allAssetLocales].cold.1
+ +[_LTDUAFAssetService _allAssetSpecifiersByLocaleId]
+ +[_LTDUAFAssetService _allAssetSpecifiers]
+ +[_LTDUAFAssetService _catalog]
+ +[_LTDUAFAssetService _catalog].cold.1
+ +[_LTDUAFAssetService _configBundleURL]
+ +[_LTDUAFAssetService _errorFor:message:]
+ +[_LTDUAFAssetService _queue]
+ +[_LTDUAFAssetService _queue].cold.1
+ +[_LTDUAFAssetService _registerChangeHandler:]
+ +[_LTDUAFAssetService _registerForAsset:progress:completion:]
+ +[_LTDUAFAssetService _requiredAssetSpecifiers]
+ +[_LTDUAFAssetService _selectedLocales]
+ +[_LTDUAFAssetService _subscribe:completion:]
+ +[_LTDUAFAssetService _subscribe:completion:].cold.1
+ +[_LTDUAFAssetService _subscribedAssetSpecifiers]
+ +[_LTDUAFAssetService _subscriptions]
+ +[_LTDUAFAssetService _unsubscribe:completion:]
+ +[_LTDUAFAssetService assetUsageValuesForAssetType:]
+ +[_LTDUAFAssetService downloadAsset:options:progress:completion:].cold.1
+ +[_LTDUAFAssetService downloadCatalogForAssetType:completion:]
+ +[_LTDUAFAssetService purgeAsset:completion:].cold.1
+ +[_LTDUAFAssetService queryAssetType:filter:completion:]
+ +[_LTDUAFAssetService queryAssetType:filter:error:]
+ +[_LTDUAFAssetService stateForAsset:]
+ +[_LTDUAFBridge assetIdentifierForAssetSpecifier:]
+ +[_LTDUAFBridge assetSpecifierForAssetIdentifier:]
+ +[_LTDUAFBridge assetSpecifierForAssetUsages:]
+ +[_LTDUAFBridge assetSpecifiersForAssetType:locale:]
+ +[_LTDUAFBridge assetTypeForAssetSpecifier:]
+ +[_LTDUAFBridge assetTypeForAssetUsage:]
+ +[_LTDUAFBridge assetUsagesForAssetSpecifier:]
+ +[_LTDUAFBridge assetUsagesForAssetType:]
+ +[_LTDUAFBridge assetUsagesForAssetType:locale:]
+ +[_LTSpeechRecognitionResult(Daemon) resultWithPackage:locale:modelVersion:taskHint:isFinal:]
+ +[_LTSpeechRecognitionResult(Daemon) resultWithPackage:locale:modelVersion:taskHint:isFinal:endOfUtterance:]
+ +[_LTSpeechRecognitionResult(Daemon) resultWithResult:locale:modelVersion:taskHint:isFinal:]
+ +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:configAsset:validateIfNeeded:]
+ +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:configAsset:validateIfNeeded:].cold.1
+ +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:configAsset:validateIfNeeded:].cold.10
+ +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:configAsset:validateIfNeeded:].cold.2
+ +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:configAsset:validateIfNeeded:].cold.3
+ +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:configAsset:validateIfNeeded:].cold.4
+ +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:configAsset:validateIfNeeded:].cold.5
+ +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:configAsset:validateIfNeeded:].cold.6
+ +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:configAsset:validateIfNeeded:].cold.7
+ +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:configAsset:validateIfNeeded:].cold.8
+ +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:configAsset:validateIfNeeded:].cold.9
+ +[_LTSpeechTranslationAssetInfo _validTopLevelSymlinkDirectory:configAssetURL:assets:]
+ +[_LTSpeechTranslationAssetInfo _validTopLevelSymlinkDirectory:configAssetURL:assets:].cold.1
+ +[_LTSpeechTranslationAssetInfo _validTopLevelSymlinkDirectory:configAssetURL:assets:].cold.2
+ +[_LTSpeechTranslationAssetInfo _validTopLevelSymlinkDirectory:configAssetURL:assets:].cold.3
+ -[NSUserDefaults(TranslationDaemonAdditions) lt_asrModels]
+ -[NSUserDefaults(TranslationDaemonAdditions) lt_asrTask]
+ -[NSUserDefaults(TranslationDaemonAdditions) lt_asrTasks]
+ -[NSUserDefaults(TranslationDaemonAdditions) lt_mtCustomModel]
+ -[NSUserDefaults(TranslationDaemonAdditions) lt_ovadEnabled]
+ -[NSUserDefaults(TranslationDaemonAdditions) lt_overrides]
+ -[TTSAsset(TranslationDaemonAdditions) weight]
+ -[_LTClientConnection startLanguageStatusChangeObservation:taskHint:completion:]
+ -[_LTClientConnection translateStreamingInput:withContext:completion:]
+ -[_LTClientConnection updateOVADStreamingState:]
+ -[_LTCombinedEngine translateStreamingInput:context:stabilizer:completion:]
+ -[_LTDASRAssetModel .cxx_destruct]
+ -[_LTDASRAssetModel assetBuild]
+ -[_LTDASRAssetModel assetId]
+ -[_LTDASRAssetModel assetLanguage]
+ -[_LTDASRAssetModel assetName]
+ -[_LTDASRAssetModel assetSubtype]
+ -[_LTDASRAssetModel assetTypeName]
+ -[_LTDASRAssetModel assetType]
+ -[_LTDASRAssetModel assetVersion]
+ -[_LTDASRAssetModel canBePurged]
+ -[_LTDASRAssetModel contentVersion]
+ -[_LTDASRAssetModel coreAssetName]
+ -[_LTDASRAssetModel debugDescription]
+ -[_LTDASRAssetModel description]
+ -[_LTDASRAssetModel downloadSize]
+ -[_LTDASRAssetModel formatVersion]
+ -[_LTDASRAssetModel getLocalFileUrl]
+ -[_LTDASRAssetModel hash]
+ -[_LTDASRAssetModel identifier]
+ -[_LTDASRAssetModel initWithAssetIdentifier:]
+ -[_LTDASRAssetModel initWithAssetIdentifier:].cold.1
+ -[_LTDASRAssetModel initWithProvider:]
+ -[_LTDASRAssetModel isAvailable]
+ -[_LTDASRAssetModel isDownloading]
+ -[_LTDASRAssetModel isEqual:]
+ -[_LTDASRAssetModel isInstalled]
+ -[_LTDASRAssetModel isMultiLocaleAsset]
+ -[_LTDASRAssetModel isPremiumTextLID]
+ -[_LTDASRAssetModel localeIdentifiers]
+ -[_LTDASRAssetModel managedAssetProvider]
+ -[_LTDASRAssetModel managedAssetType]
+ -[_LTDASRAssetModel progress]
+ -[_LTDASRAssetModel provider]
+ -[_LTDASRAssetModel requiredCapabilityIdentifier]
+ -[_LTDASRAssetModel setAssetPath:]
+ -[_LTDASRAssetModel setAssetSubtype:]
+ -[_LTDASRAssetModel setProvider:]
+ -[_LTDASRAssetModel shouldPurgeWithLocale]
+ -[_LTDASRAssetModel state]
+ -[_LTDASRAssetModel supportedLanguages]
+ -[_LTDASRAssetModel supportsLocale:]
+ -[_LTDASRAssetModel supportsTaskHint:]
+ -[_LTDASRAssetModel unarchivedSize]
+ -[_LTDASRConfigurationModel _defaultAssetType]
+ -[_LTDASRConfigurationModel _taskHintMap]
+ -[_LTDASRConfigurationModel assetTypeForTaskHint:localeIdentifier:]
+ -[_LTDASRConfigurationModel assetTypesForLocaleIdentifier:]
+ -[_LTDASRConfigurationModel supportedLocaleIdentifiersForTaskHint:]
+ -[_LTDAssetModel _addComponentAsset:]
+ -[_LTDAssetModel addComponentAsset:]
+ -[_LTDAssetModel addComponentAsset:].cold.1
+ -[_LTDAssetModel addComponentAsset:].cold.2
+ -[_LTDAssetModel addComponentAsset:].cold.3
+ -[_LTDAssetModel assetSubtype]
+ -[_LTDAssetModel components]
+ -[_LTDAssetModel getLocalFileUrlForTaskHint:]
+ -[_LTDAssetModel hash]
+ -[_LTDAssetModel initWithAssetIdentifier:]
+ -[_LTDAssetModel isASRModelSupportingTaskHint:]
+ -[_LTDAssetModel managedAssetProvider]
+ -[_LTDAssetModel setAssetSubtype:]
+ -[_LTDAssetModel supportsTaskHint:]
+ -[_LTDLanguageAssetCache notify:ofObservations:]
+ -[_LTDLanguageAssetCache observationFilterConditions]
+ -[_LTDLanguageAssetCache setInitialObservationsForIdentifiers:]
+ -[_LTDLanguageAssetCache setObservationFilterConditions:]
+ -[_LTDLanguageAssetCache setRequiredAssets:localeRanks:]
+ -[_LTDLanguageAssetCache supportedLocalesSubsetForTask:]
+ -[_LTDLanguageAssetCacheObserver initWithID:taskHint:progress:observations:completion:]
+ -[_LTDLanguageAssetCacheObserver taskHint]
+ -[_LTDMAAssetModel assetName].cold.1
+ -[_LTDMAAssetModel assetSubtype]
+ -[_LTDMAAssetModel hash]
+ -[_LTDMAAssetModel initWithAssetIdentifier:]
+ -[_LTDMAAssetModel initWithProvider:]
+ -[_LTDMAAssetModel initWithProvider:].cold.1
+ -[_LTDMAAssetModel isEqual:]
+ -[_LTDMAAssetModel isMultiLocaleAsset]
+ -[_LTDMAAssetModel localeIdentifiers]
+ -[_LTDMAAssetModel managedAssetProvider]
+ -[_LTDMAAssetModel provider]
+ -[_LTDMAAssetModel setAssetSubtype:]
+ -[_LTDMAAssetModel setProvider:]
+ -[_LTDMAAssetModel shouldPurgeWithLocale]
+ -[_LTDMAAssetModel supportsLocale:]
+ -[_LTDMAAssetModel supportsTaskHint:]
+ -[_LTDStreamStabilizer .cxx_destruct]
+ -[_LTDStreamStabilizer init]
+ -[_LTDStreamStabilizer init].cold.1
+ -[_LTDStreamStabilizer reset]
+ -[_LTDStreamStabilizer setStableSegments:]
+ -[_LTDStreamStabilizer stabilizationState]
+ -[_LTDStreamStabilizer stableSegments]
+ -[_LTDTTSAssetModel assetSubtype]
+ -[_LTDTTSAssetModel debugDescription]
+ -[_LTDTTSAssetModel description]
+ -[_LTDTTSAssetModel hash]
+ -[_LTDTTSAssetModel initWithProvider:]
+ -[_LTDTTSAssetModel isEqual:]
+ -[_LTDTTSAssetModel isMultiLocaleAsset]
+ -[_LTDTTSAssetModel localeIdentifiers]
+ -[_LTDTTSAssetModel managedAssetProvider]
+ -[_LTDTTSAssetModel provider]
+ -[_LTDTTSAssetModel setAssetName:]
+ -[_LTDTTSAssetModel setAssetSubtype:]
+ -[_LTDTTSAssetModel setProvider:]
+ -[_LTDTTSAssetModel shouldPurgeWithLocale]
+ -[_LTDTTSAssetModel supportsLocale:]
+ -[_LTDTTSAssetModel supportsTaskHint:]
+ -[_LTDUAFAssetModel .cxx_destruct]
+ -[_LTDUAFAssetModel assetBuild]
+ -[_LTDUAFAssetModel assetId]
+ -[_LTDUAFAssetModel assetLanguage]
+ -[_LTDUAFAssetModel assetName]
+ -[_LTDUAFAssetModel assetSubtype]
+ -[_LTDUAFAssetModel assetTypeName]
+ -[_LTDUAFAssetModel assetType]
+ -[_LTDUAFAssetModel assetUsages]
+ -[_LTDUAFAssetModel assetVersion]
+ -[_LTDUAFAssetModel canBePurged]
+ -[_LTDUAFAssetModel compare:]
+ -[_LTDUAFAssetModel contentVersion]
+ -[_LTDUAFAssetModel coreAssetName]
+ -[_LTDUAFAssetModel debugDescription]
+ -[_LTDUAFAssetModel description]
+ -[_LTDUAFAssetModel downloadSize]
+ -[_LTDUAFAssetModel formatVersion]
+ -[_LTDUAFAssetModel getLocalFileUrl]
+ -[_LTDUAFAssetModel hash]
+ -[_LTDUAFAssetModel identifier]
+ -[_LTDUAFAssetModel initWithAssetIdentifier:]
+ -[_LTDUAFAssetModel initWithAssetSpecifier:]
+ -[_LTDUAFAssetModel initWithProvider:]
+ -[_LTDUAFAssetModel isAvailable]
+ -[_LTDUAFAssetModel isDownloading]
+ -[_LTDUAFAssetModel isEqual:]
+ -[_LTDUAFAssetModel isInstalled]
+ -[_LTDUAFAssetModel isMultiLocaleAsset]
+ -[_LTDUAFAssetModel isPremiumTextLID]
+ -[_LTDUAFAssetModel localeIdentifiers]
+ -[_LTDUAFAssetModel managedAssetProvider]
+ -[_LTDUAFAssetModel managedAssetType]
+ -[_LTDUAFAssetModel progress]
+ -[_LTDUAFAssetModel provider]
+ -[_LTDUAFAssetModel requiredCapabilityIdentifier]
+ -[_LTDUAFAssetModel setAssetSubtype:]
+ -[_LTDUAFAssetModel setProvider:]
+ -[_LTDUAFAssetModel shouldPurgeWithLocale]
+ -[_LTDUAFAssetModel state]
+ -[_LTDUAFAssetModel supportedLanguages]
+ -[_LTDUAFAssetModel supportsLocale:]
+ -[_LTDUAFAssetModel supportsTaskHint:]
+ -[_LTDUAFAssetModel unarchivedSize]
+ -[_LTHotfixManager setHotfixURL:]
+ -[_LTHotfixManager setHotfixURL:].cold.1
+ -[_LTMultilingualSpeechRecognizer currentLocale]
+ -[_LTMultilingualSpeechRecognizer enableMultiFieldInput]
+ -[_LTMultilingualSpeechRecognizer initWithModelURLs:modelVersions:taskHint:]
+ -[_LTMultilingualSpeechRecognizer setCurrentLocale:]
+ -[_LTMultilingualSpeechRecognizer setEnableMultiFieldInput:]
+ -[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:enableStreamingSpeechTranslation:enableMultiFieldInput:resultHandler:]
+ -[_LTOfflineAssetManager speechTranslationAssetInfoForLocalePair:taskHint:error:]
+ -[_LTOfflineAssetManager speechTranslationAssetInfoForLocalePair:taskHint:error:].cold.1
+ -[_LTOfflineTranslationEngine _concatenatedAlignmentsFromSentences:]
+ -[_LTOfflineTranslationEngine _handleTranslationResults:withContext:sourceString:sourceSpans:stabilizer:]
+ -[_LTOfflineTranslationEngine _handleTranslationResults:withContext:sourceString:sourceSpans:stabilizer:].cold.1
+ -[_LTOfflineTranslationEngine _loadEtiquetteSanitizersForTaskHint:]
+ -[_LTOfflineTranslationEngine _loadEtiquetteSanitizersForTaskHint:].cold.1
+ -[_LTOfflineTranslationEngine _loadEtiquetteSanitizersForTaskHint:].cold.2
+ -[_LTOfflineTranslationEngine _translateString:isFinal:withContext:toLocale:withSpans:stabilizer:completion:]
+ -[_LTOfflineTranslationEngine initWithLocalePair:taskHint:assetInfo:selfLoggingManager:]
+ -[_LTOfflineTranslationEngine taskHint]
+ -[_LTOfflineTranslationEngine translateStreamingInput:context:stabilizer:completion:]
+ -[_LTOnlineTranslationEngine translateStreamingInput:context:stabilizer:completion:]
+ -[_LTServerSpeechSession _updateOVADStreamingState_onQueue:]
+ -[_LTServerSpeechSession _updateOVADStreamingState_onQueue:].cold.1
+ -[_LTServerSpeechSession cancelOwnVoicePendingSwapAndRestartTimer]
+ -[_LTServerSpeechSession forcePendingSwapAndRestart]
+ -[_LTServerSpeechSession ownVoicePendingSwapAndRestartTimer]
+ -[_LTServerSpeechSession setOwnVoicePendingSwapAndRestartTimer:]
+ -[_LTServerSpeechSession swapLocalesAndRestartWithStateResetAndLogMessage:]
+ -[_LTServerSpeechSession swapLocalesAndRestart]
+ -[_LTServerSpeechSession swapLocalesAndRestart].cold.1
+ -[_LTServerSpeechSession updateOVADStreamingState:]
+ -[_LTServerSpeechSession updateOwnVoicePendingSwapAndRestartTimer]
+ -[_LTSpeechRecognitionResult(Daemon) initWithPackage:locale:modelVersion:taskHint:isFinal:endOfUtterance:]
+ -[_LTSpeechRecognitionResult(Daemon) initWithPackage:locale:modelVersion:taskHint:isFinal:endOfUtterance:].cold.1
+ -[_LTSpeechRecognitionResult(Daemon) initWithResult:locale:modelVersion:taskHint:isFinal:]
+ -[_LTSpeechRecognizer initWithModelURL:language:modelVersion:taskHint:]
+ -[_LTSpeechRecognizer initWithModelURL:language:modelVersion:taskHint:].cold.1
+ -[_LTSpeechRecognizer initWithModelURL:language:modelVersion:taskHint:].cold.2
+ -[_LTSpeechRecognizer startRecognitionWithAutoStop:enableStreamingSpeechTranslation:resultHandler:]
+ -[_LTSpeechTranslationAssetInfo isCompleteBidirectionalModelForTaskHint:]
+ -[_LTSpeechTranslationAssetInfo isCompletePassthroughModelForTaskHint:]
+ -[_LTSpeechTranslationAssetInfo speechModelURLForLocale:taskHint:]
+ -[_LTTextLanguageDetectionResult(Daemon) initWithScorer:lowConfidenceLocales:strategy:]
+ -[_LTTextLanguageDetectorScorer append:]
+ -[_LTTextLanguageDetectorScorer weightedLocaleWithStrategy:]
+ -[_LTTextLanguageDetectorScorer weightedLocaleWithStrategy:].cold.1
+ -[_LTTranslationCandidate(Daemon) initWithFormattedString:sanitizedFormattedString:confidence:lowConfidence:romanization:tokens:preToPostITN:stableString:]
+ -[_LTTranslationResult(Daemon) updateAlignmentWithSourceSpans:offlineTargetSpans:]
+ -[_LTTranslationServer _prepareStabilizerForContext:]
+ -[_LTTranslationServer _prepareStabilizerForContext:].cold.1
+ -[_LTTranslationServer translateStreamingInput:withContext:completion:]
+ -[_LTTranslationServer updateOVADStreamingState:]
+ GCC_except_table1007
+ GCC_except_table1013
+ GCC_except_table1029
+ GCC_except_table1039
+ GCC_except_table1053
+ GCC_except_table1059
+ GCC_except_table1067
+ GCC_except_table1087
+ GCC_except_table1111
+ GCC_except_table1113
+ GCC_except_table1125
+ GCC_except_table1127
+ GCC_except_table1160
+ GCC_except_table1190
+ GCC_except_table1195
+ GCC_except_table1211
+ GCC_except_table1243
+ GCC_except_table1249
+ GCC_except_table1275
+ GCC_except_table1277
+ GCC_except_table1305
+ GCC_except_table1356
+ GCC_except_table1358
+ GCC_except_table1360
+ GCC_except_table1362
+ GCC_except_table1364
+ GCC_except_table1366
+ GCC_except_table1402
+ GCC_except_table1414
+ GCC_except_table1420
+ GCC_except_table1424
+ GCC_except_table1483
+ GCC_except_table1520
+ GCC_except_table1522
+ GCC_except_table1524
+ GCC_except_table1550
+ GCC_except_table1581
+ GCC_except_table1585
+ GCC_except_table1589
+ GCC_except_table160
+ GCC_except_table1617
+ GCC_except_table1637
+ GCC_except_table1641
+ GCC_except_table1650
+ GCC_except_table1656
+ GCC_except_table1658
+ GCC_except_table1676
+ GCC_except_table1680
+ GCC_except_table1686
+ GCC_except_table1704
+ GCC_except_table1706
+ GCC_except_table1708
+ GCC_except_table1740
+ GCC_except_table1776
+ GCC_except_table182
+ GCC_except_table1826
+ GCC_except_table1828
+ GCC_except_table1834
+ GCC_except_table1872
+ GCC_except_table1874
+ GCC_except_table1884
+ GCC_except_table1908
+ GCC_except_table1916
+ GCC_except_table1926
+ GCC_except_table1934
+ GCC_except_table1956
+ GCC_except_table1964
+ GCC_except_table1966
+ GCC_except_table1968
+ GCC_except_table1992
+ GCC_except_table2000
+ GCC_except_table2036
+ GCC_except_table2038
+ GCC_except_table2040
+ GCC_except_table2042
+ GCC_except_table2044
+ GCC_except_table2047
+ GCC_except_table2048
+ GCC_except_table2049
+ GCC_except_table2051
+ GCC_except_table2057
+ GCC_except_table2062
+ GCC_except_table2068
+ GCC_except_table2077
+ GCC_except_table2083
+ GCC_except_table2085
+ GCC_except_table2086
+ GCC_except_table2088
+ GCC_except_table2089
+ GCC_except_table2095
+ GCC_except_table2107
+ GCC_except_table2113
+ GCC_except_table2136
+ GCC_except_table2137
+ GCC_except_table2138
+ GCC_except_table2139
+ GCC_except_table2141
+ GCC_except_table2142
+ GCC_except_table2143
+ GCC_except_table2144
+ GCC_except_table2145
+ GCC_except_table2146
+ GCC_except_table2147
+ GCC_except_table2170
+ GCC_except_table2171
+ GCC_except_table2172
+ GCC_except_table2175
+ GCC_except_table2176
+ GCC_except_table2177
+ GCC_except_table2180
+ GCC_except_table2181
+ GCC_except_table2182
+ GCC_except_table2183
+ GCC_except_table2191
+ GCC_except_table2196
+ GCC_except_table2202
+ GCC_except_table2210
+ GCC_except_table2211
+ GCC_except_table2212
+ GCC_except_table2215
+ GCC_except_table2221
+ GCC_except_table2230
+ GCC_except_table2231
+ GCC_except_table2233
+ GCC_except_table2234
+ GCC_except_table2235
+ GCC_except_table2239
+ GCC_except_table2245
+ GCC_except_table2253
+ GCC_except_table2263
+ GCC_except_table2266
+ GCC_except_table2271
+ GCC_except_table2282
+ GCC_except_table2287
+ GCC_except_table2289
+ GCC_except_table2295
+ GCC_except_table2301
+ GCC_except_table2302
+ GCC_except_table2303
+ GCC_except_table2305
+ GCC_except_table2323
+ GCC_except_table2326
+ GCC_except_table2327
+ GCC_except_table2330
+ GCC_except_table2331
+ GCC_except_table2332
+ GCC_except_table2333
+ GCC_except_table2336
+ GCC_except_table2342
+ GCC_except_table2345
+ GCC_except_table2356
+ GCC_except_table2357
+ GCC_except_table2369
+ GCC_except_table2371
+ GCC_except_table2372
+ GCC_except_table2378
+ GCC_except_table2382
+ GCC_except_table2384
+ GCC_except_table2385
+ GCC_except_table2387
+ GCC_except_table2393
+ GCC_except_table2397
+ GCC_except_table2400
+ GCC_except_table2406
+ GCC_except_table2415
+ GCC_except_table2416
+ GCC_except_table2422
+ GCC_except_table2427
+ GCC_except_table2429
+ GCC_except_table2430
+ GCC_except_table2436
+ GCC_except_table2442
+ GCC_except_table2451
+ GCC_except_table2456
+ GCC_except_table2457
+ GCC_except_table2461
+ GCC_except_table2462
+ GCC_except_table2464
+ GCC_except_table2483
+ GCC_except_table2489
+ GCC_except_table2492
+ GCC_except_table2493
+ GCC_except_table2494
+ GCC_except_table2496
+ GCC_except_table2502
+ GCC_except_table2507
+ GCC_except_table2508
+ GCC_except_table2514
+ GCC_except_table2517
+ GCC_except_table2540
+ GCC_except_table2542
+ GCC_except_table2543
+ GCC_except_table2544
+ GCC_except_table2545
+ GCC_except_table2546
+ GCC_except_table2555
+ GCC_except_table2558
+ GCC_except_table2564
+ GCC_except_table2568
+ GCC_except_table2569
+ GCC_except_table2570
+ GCC_except_table2571
+ GCC_except_table2590
+ GCC_except_table2596
+ GCC_except_table2598
+ GCC_except_table2599
+ GCC_except_table2600
+ GCC_except_table2601
+ GCC_except_table2604
+ GCC_except_table2605
+ GCC_except_table2611
+ GCC_except_table2624
+ GCC_except_table2625
+ GCC_except_table2627
+ GCC_except_table2629
+ GCC_except_table2630
+ GCC_except_table2631
+ GCC_except_table2633
+ GCC_except_table2635
+ GCC_except_table2636
+ GCC_except_table2637
+ GCC_except_table2656
+ GCC_except_table2662
+ GCC_except_table2684
+ GCC_except_table2685
+ GCC_except_table2687
+ GCC_except_table2689
+ GCC_except_table2691
+ GCC_except_table2693
+ GCC_except_table2695
+ GCC_except_table2699
+ GCC_except_table2705
+ GCC_except_table2711
+ GCC_except_table2713
+ GCC_except_table2714
+ GCC_except_table2720
+ GCC_except_table2725
+ GCC_except_table2726
+ GCC_except_table2727
+ GCC_except_table2733
+ GCC_except_table2738
+ GCC_except_table2739
+ GCC_except_table2740
+ GCC_except_table2746
+ GCC_except_table2748
+ GCC_except_table2749
+ GCC_except_table2752
+ GCC_except_table2753
+ GCC_except_table2762
+ GCC_except_table2768
+ GCC_except_table2774
+ GCC_except_table2776
+ GCC_except_table2786
+ GCC_except_table2789
+ GCC_except_table2790
+ GCC_except_table2792
+ GCC_except_table2804
+ GCC_except_table2805
+ GCC_except_table2817
+ GCC_except_table2823
+ GCC_except_table2825
+ GCC_except_table2826
+ GCC_except_table2830
+ GCC_except_table2831
+ GCC_except_table2833
+ GCC_except_table2839
+ GCC_except_table2846
+ GCC_except_table2852
+ GCC_except_table2857
+ GCC_except_table2858
+ GCC_except_table2859
+ GCC_except_table2860
+ GCC_except_table2863
+ GCC_except_table2869
+ GCC_except_table2873
+ GCC_except_table2874
+ GCC_except_table2880
+ GCC_except_table2886
+ GCC_except_table2888
+ GCC_except_table2889
+ GCC_except_table2890
+ GCC_except_table2899
+ GCC_except_table2905
+ GCC_except_table2909
+ GCC_except_table2911
+ GCC_except_table2912
+ GCC_except_table2913
+ GCC_except_table2914
+ GCC_except_table2915
+ GCC_except_table2921
+ GCC_except_table2934
+ GCC_except_table2935
+ GCC_except_table2941
+ GCC_except_table2954
+ GCC_except_table2961
+ GCC_except_table2964
+ GCC_except_table2965
+ GCC_except_table2966
+ GCC_except_table2968
+ GCC_except_table2970
+ GCC_except_table2975
+ GCC_except_table2981
+ GCC_except_table2989
+ GCC_except_table2994
+ GCC_except_table3003
+ GCC_except_table3005
+ GCC_except_table3006
+ GCC_except_table3008
+ GCC_except_table3009
+ GCC_except_table3010
+ GCC_except_table3017
+ GCC_except_table3025
+ GCC_except_table3029
+ GCC_except_table3032
+ GCC_except_table3033
+ GCC_except_table3038
+ GCC_except_table3048
+ GCC_except_table3062
+ GCC_except_table3063
+ GCC_except_table3064
+ GCC_except_table3065
+ GCC_except_table3067
+ GCC_except_table3078
+ GCC_except_table3084
+ GCC_except_table3088
+ GCC_except_table3091
+ GCC_except_table3101
+ GCC_except_table3110
+ GCC_except_table3111
+ GCC_except_table3112
+ GCC_except_table3113
+ GCC_except_table3114
+ GCC_except_table3120
+ GCC_except_table3126
+ GCC_except_table3127
+ GCC_except_table378
+ GCC_except_table432
+ GCC_except_table463
+ GCC_except_table549
+ GCC_except_table569
+ GCC_except_table573
+ GCC_except_table589
+ GCC_except_table595
+ GCC_except_table609
+ GCC_except_table613
+ GCC_except_table631
+ GCC_except_table649
+ GCC_except_table663
+ GCC_except_table665
+ GCC_except_table683
+ GCC_except_table697
+ GCC_except_table731
+ GCC_except_table733
+ GCC_except_table773
+ GCC_except_table791
+ GCC_except_table795
+ GCC_except_table811
+ GCC_except_table815
+ GCC_except_table835
+ GCC_except_table915
+ GCC_except_table929
+ GCC_except_table931
+ GCC_except_table953
+ GCC_except_table977
+ GCC_except_table979
+ GCC_except_table997
+ GCC_except_table999
+ _OBJC_CLASS_$_EMTStablePrefixState
+ _OBJC_CLASS_$_SFEntitledAssetConfig
+ _OBJC_CLASS_$_SFSpeechAssetManager
+ _OBJC_CLASS_$_SFUtilities
+ _OBJC_CLASS_$_UAFAssetSetManager
+ _OBJC_CLASS_$_UAFAssetSetSubscription
+ _OBJC_CLASS_$__LTDASRAssetModel
+ _OBJC_CLASS_$__LTDASRAssetService
+ _OBJC_CLASS_$__LTDStreamStabilizer
+ _OBJC_CLASS_$__LTDUAFAssetModel
+ _OBJC_CLASS_$__LTDUAFBridge
+ _OBJC_CLASS_$__LTSpeechTranslationRequest
+ _OBJC_CLASS_$__LTStabilizationTranslationResult
+ _OBJC_CLASS_$__LTStreamingOutput
+ _OBJC_IVAR_$__LTClientConnection._languageStatusSessionID
+ _OBJC_IVAR_$__LTDASRAssetModel._assetName
+ _OBJC_IVAR_$__LTDASRAssetModel._assetSubtype
+ _OBJC_IVAR_$__LTDASRAssetModel._assetURL
+ _OBJC_IVAR_$__LTDASRAssetModel._ltIdentifier
+ _OBJC_IVAR_$__LTDASRAssetModel._progress
+ _OBJC_IVAR_$__LTDASRAssetModel._provider
+ _OBJC_IVAR_$__LTDAssetModel._components
+ _OBJC_IVAR_$__LTDAssetModel._lock
+ _OBJC_IVAR_$__LTDAssetModel._progress
+ _OBJC_IVAR_$__LTDLanguageAssetCache._localeRanks
+ _OBJC_IVAR_$__LTDLanguageAssetCache._observationFilterConditions
+ _OBJC_IVAR_$__LTDLanguageAssetCacheObserver._taskHint
+ _OBJC_IVAR_$__LTDMAAssetModel._assetName
+ _OBJC_IVAR_$__LTDMAAssetModel._assetSubtype
+ _OBJC_IVAR_$__LTDMAAssetModel._provider
+ _OBJC_IVAR_$__LTDStreamStabilizer._lock
+ _OBJC_IVAR_$__LTDStreamStabilizer._stabilizationState
+ _OBJC_IVAR_$__LTDStreamStabilizer._stableSegments
+ _OBJC_IVAR_$__LTDTTSAssetModel._assetSubtype
+ _OBJC_IVAR_$__LTDTTSAssetModel._provider
+ _OBJC_IVAR_$__LTDUAFAssetModel._assetLanguage
+ _OBJC_IVAR_$__LTDUAFAssetModel._assetName
+ _OBJC_IVAR_$__LTDUAFAssetModel._assetSubtype
+ _OBJC_IVAR_$__LTDUAFAssetModel._assetUsages
+ _OBJC_IVAR_$__LTDUAFAssetModel._identifier
+ _OBJC_IVAR_$__LTDUAFAssetModel._progress
+ _OBJC_IVAR_$__LTDUAFAssetModel._provider
+ _OBJC_IVAR_$__LTMultilingualSpeechRecognizer._currentLocale
+ _OBJC_IVAR_$__LTMultilingualSpeechRecognizer._enableMultiFieldInput
+ _OBJC_IVAR_$__LTOfflineTranslationEngine._pendingStreamingSpeechResults
+ _OBJC_IVAR_$__LTOfflineTranslationEngine._speechRequestStablePrefixState
+ _OBJC_IVAR_$__LTOfflineTranslationEngine._taskHint
+ _OBJC_IVAR_$__LTServerSpeechSession._originalLocalePair
+ _OBJC_IVAR_$__LTServerSpeechSession._ownVoiceIsActive
+ _OBJC_IVAR_$__LTServerSpeechSession._ownVoicePendingSwapAndRestartTimer
+ _OBJC_IVAR_$__LTServerSpeechSession._pendingFinalTranslation
+ _OBJC_IVAR_$__LTServerSpeechSession._pendingSwapAndRestart
+ _OBJC_IVAR_$__LTSpeechRecognizer._enableStreamingSpeechTranslation
+ _OBJC_IVAR_$__LTSpeechRecognizer._taskHint
+ _OBJC_IVAR_$__LTTranslationServer._stabilizerMap
+ _OBJC_METACLASS_$__LTDASRAssetModel
+ _OBJC_METACLASS_$__LTDASRAssetService
+ _OBJC_METACLASS_$__LTDStreamStabilizer
+ _OBJC_METACLASS_$__LTDUAFAssetModel
+ _OBJC_METACLASS_$__LTDUAFBridge
+ __LTASRModelTaskString
+ __LTOSLogStabilization
+ __LTOSLogStabilization.cold.1
+ __LTOSLogStabilization.log
+ __LTOSLogStabilization.onceToken
+ __LTTranslationTaskHintString
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$_LTStatistics
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_TTSAsset_$_TranslationDaemonAdditions
+ __OBJC_$_CATEGORY_NSString_$_LTStatistics
+ __OBJC_$_CATEGORY_TTSAsset_$_TranslationDaemonAdditions
+ __OBJC_$_CLASS_METHODS__LTDASRAssetModel
+ __OBJC_$_CLASS_METHODS__LTDASRAssetService
+ __OBJC_$_CLASS_METHODS__LTDUAFBridge
+ __OBJC_$_INSTANCE_METHODS__LTDASRAssetModel
+ __OBJC_$_INSTANCE_METHODS__LTDStreamStabilizer
+ __OBJC_$_INSTANCE_METHODS__LTDUAFAssetModel
+ __OBJC_$_INSTANCE_VARIABLES__LTDASRAssetModel
+ __OBJC_$_INSTANCE_VARIABLES__LTDStreamStabilizer
+ __OBJC_$_INSTANCE_VARIABLES__LTDUAFAssetModel
+ __OBJC_$_PROP_LIST_TTSAsset_$_TranslationDaemonAdditions
+ __OBJC_$_PROP_LIST__LTDASRAssetModel
+ __OBJC_$_PROP_LIST__LTDStreamStabilizer
+ __OBJC_$_PROP_LIST__LTDUAFAssetModel
+ __OBJC_$_PROP_LIST__LTMultilingualSpeechRecognizer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__LTObservationFilteringConditions
+ __OBJC_$_PROTOCOL_METHOD_TYPES__LTObservationFilteringConditions
+ __OBJC_CLASS_PROTOCOLS_$__LTDASRAssetModel
+ __OBJC_CLASS_PROTOCOLS_$__LTDASRAssetService
+ __OBJC_CLASS_PROTOCOLS_$__LTDLanguageAssetCache
+ __OBJC_CLASS_PROTOCOLS_$__LTDUAFAssetModel
+ __OBJC_CLASS_RO_$__LTDASRAssetModel
+ __OBJC_CLASS_RO_$__LTDASRAssetService
+ __OBJC_CLASS_RO_$__LTDStreamStabilizer
+ __OBJC_CLASS_RO_$__LTDUAFAssetModel
+ __OBJC_CLASS_RO_$__LTDUAFBridge
+ __OBJC_LABEL_PROTOCOL_$__LTObservationFilteringConditions
+ __OBJC_METACLASS_RO_$__LTDASRAssetModel
+ __OBJC_METACLASS_RO_$__LTDASRAssetService
+ __OBJC_METACLASS_RO_$__LTDStreamStabilizer
+ __OBJC_METACLASS_RO_$__LTDUAFAssetModel
+ __OBJC_METACLASS_RO_$__LTDUAFBridge
+ __OBJC_PROTOCOL_$__LTObservationFilteringConditions
+ __ZN5apple4aiml12flatbuffers214DetachedBufferD1Ev
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__112basic_stringIDsNS_11char_traitsIDsEENS_9allocatorIDsEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIDsEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10AudioFrameEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10PronChoiceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10TTSPromptsEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10TokenPronsEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb11AudioPacketEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb11TokenProns_17SanitizedSequenceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12CategoryDataEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12FinishAudio_37ServerFeatureLatencyDistributionEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12ItnAlignmentEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12RepeatedSpanEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb13LmScorerTokenEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb13PronunciationEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14TTSReplacementEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14UserDataEntityEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14UserParametersEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14WordTimingInfoEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15AudioAnalytics_21AcousticFeaturesEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15AudioAnalytics_30SpeechRecognitionFeaturesEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15ChoiceAlignmentEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15NormalizedTokenEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15TTSWordPhonemesEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb16RecognitionTokenEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb17RecognitionChoiceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb17TTSNormalizedTextEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb18LanguageParametersEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb18SanitizedPronTokenEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb18TTSPhonemeSequenceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb19TextToSpeechRequestEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20ContextWithPronHintsEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20CorrectionsAlignmentEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20RecognitionCandidateEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20RepeatedItnAlignmentEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TextToSpeechRequest_16ContextInfoEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TranslationResponse_16TranslationTokenEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TranslationResponse_17TranslationPhraseEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb21RequestStatsResponse_10DoubleStatEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb21RequestStatsResponse_8BoolStatEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb21RequestStatsResponse_9Int32StatEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb21TranslationLocalePairEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb22NormalizedTokenVariantEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb23RecognitionPhraseTokensEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb23TextToSpeechCacheObjectEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24BatchTranslationRequest_9ParagraphEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24MTAlternativeDescriptionEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24TTSNeuralPhonemeSequenceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb25BatchTranslationResponse_17TranslationPhraseEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb25BatchTranslationResponse_18TranslatedSentenceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb25TextToSpeechVoiceResourceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb26ShortcutFuzzyMatchRequest_15StringTokenPairEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb26TranslationPhraseMetaInfo_23AlternativeSelectedSpanEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb26TranslationPhraseMetaInfo_24AlternativeSelectedSpan_11AlternativeEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSG_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb26TranslationPhraseMetaInfo_24AlternativeSelectedSpan_5RangeEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSG_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb27LanguageDetectionPredictionEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb27ShortcutFuzzyMatchResponse_17ShortcutScorePairEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb27TextToSpeechRequestContext_16ContextInfoEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb28SpeechTranslationMtResponse_17TranslationPhraseEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb30FinalSpeechRecognitionResponseEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb33TextToSpeechSpeechFeatureRequest_12LexiconEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb34StartTextToSpeechStreamingRequest_16ContextInfoEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb34TextToSpeechSpeechFeatureInputWordEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb35RecognitionPhraseTokensAlternativesEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb36PartialTextToSpeechStreamingResponseEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb37TextToSpeechSpeechFeatureInputPhonemeEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb38TextToSpeechSpeechFeatureOutputFeatureEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb38TranslationSupportedLanguagesResponse_12LanguagePairEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb4SpanEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb4WordEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb7KeywordEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb8VocTokenEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN5apple4aiml12flatbuffers26OffsetINS4_6StringEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10AudioFrameEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10PronChoiceEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10PronChoiceEEENS_9allocatorIS9_EEE9push_backB8ne200100EOS9_
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10TTSPromptsEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10TokenPronsEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10TokenPronsEEENS_9allocatorIS9_EEE9push_backB8ne200100EOS9_
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb11AudioPacketEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb11TokenProns_17SanitizedSequenceEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12CategoryDataEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12FinishAudio_37ServerFeatureLatencyDistributionEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12ItnAlignmentEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12ItnAlignmentEEENS_9allocatorIS9_EEE9push_backB8ne200100EOS9_
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12RepeatedSpanEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12RepeatedSpanEEENS_9allocatorIS9_EEE9push_backB8ne200100EOS9_
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb13LmScorerTokenEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb13PronunciationEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14TTSReplacementEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14UserDataEntityEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14UserParametersEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14UserParametersEEENS_9allocatorIS9_EEE9push_backB8ne200100EOS9_
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14WordTimingInfoEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14WordTimingInfoEEENS_9allocatorIS9_EEE9push_backB8ne200100EOS9_
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15AudioAnalytics_21AcousticFeaturesEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15AudioAnalytics_30SpeechRecognitionFeaturesEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15ChoiceAlignmentEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15NormalizedTokenEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15TTSWordPhonemesEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb16RecognitionTokenEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb16RecognitionTokenEEENS_9allocatorIS9_EEE9push_backB8ne200100EOS9_
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb17RecognitionChoiceEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb17RecognitionChoiceEEENS_9allocatorIS9_EEE9push_backB8ne200100EOS9_
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb17TTSNormalizedTextEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb18LanguageParametersEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb18SanitizedPronTokenEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb18TTSPhonemeSequenceEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb19TextToSpeechRequestEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20ContextWithPronHintsEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20CorrectionsAlignmentEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20RecognitionCandidateEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20RepeatedItnAlignmentEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TextToSpeechRequest_16ContextInfoEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TranslationResponse_16TranslationTokenEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TranslationResponse_17TranslationPhraseEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TranslationResponse_17TranslationPhraseEEENS_9allocatorISA_EEE9push_backB8ne200100EOSA_
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb21RequestStatsResponse_10DoubleStatEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb21RequestStatsResponse_8BoolStatEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb21RequestStatsResponse_9Int32StatEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb21TranslationLocalePairEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb22NormalizedTokenVariantEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb23RecognitionPhraseTokensEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb23RecognitionPhraseTokensEEENS_9allocatorIS9_EEE9push_backB8ne200100EOS9_
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb23TextToSpeechCacheObjectEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24BatchTranslationRequest_9ParagraphEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24MTAlternativeDescriptionEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24MTAlternativeDescriptionEEENS_9allocatorIS9_EEE9push_backB8ne200100EOS9_
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24TTSNeuralPhonemeSequenceEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb25BatchTranslationResponse_17TranslationPhraseEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb25BatchTranslationResponse_18TranslatedSentenceEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb25TextToSpeechVoiceResourceEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb26ShortcutFuzzyMatchRequest_15StringTokenPairEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb26TranslationPhraseMetaInfo_23AlternativeSelectedSpanEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb26TranslationPhraseMetaInfo_24AlternativeSelectedSpan_11AlternativeEEENS_9allocatorISB_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb26TranslationPhraseMetaInfo_24AlternativeSelectedSpan_5RangeEEENS_9allocatorISB_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb27LanguageDetectionPredictionEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb27LanguageDetectionPredictionEEENS_9allocatorIS9_EEE9push_backB8ne200100EOS9_
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb27ShortcutFuzzyMatchResponse_17ShortcutScorePairEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb27TextToSpeechRequestContext_16ContextInfoEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb28SpeechTranslationMtResponse_17TranslationPhraseEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb30FinalSpeechRecognitionResponseEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb33TextToSpeechSpeechFeatureRequest_12LexiconEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb34StartTextToSpeechStreamingRequest_16ContextInfoEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb34TextToSpeechSpeechFeatureInputWordEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb35RecognitionPhraseTokensAlternativesEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb35RecognitionPhraseTokensAlternativesEEENS_9allocatorIS9_EEE9push_backB8ne200100EOS9_
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb36PartialTextToSpeechStreamingResponseEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb37TextToSpeechSpeechFeatureInputPhonemeEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb38TextToSpeechSpeechFeatureOutputFeatureEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb38TranslationSupportedLanguagesResponse_12LanguagePairEEENS_9allocatorISA_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb4SpanEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb4SpanEEENS_9allocatorIS9_EEE9push_backB8ne200100EOS9_
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb4WordEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb7KeywordEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb8VocTokenEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetINS3_6StringEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5apple4aiml12flatbuffers26OffsetINS3_6StringEEENS_9allocatorIS6_EEE9push_backB8ne200100EOS6_
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE9push_backB8ne200100EOf
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE9push_backB8ne200100EOi
+ __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorItNS_9allocatorItEEEC2B8ne200100Em
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ ___105-[_LTOfflineTranslationEngine _handleTranslationResults:withContext:sourceString:sourceSpans:stabilizer:]_block_invoke
+ ___109-[_LTOfflineTranslationEngine _translateString:isFinal:withContext:toLocale:withSpans:stabilizer:completion:]_block_invoke
+ ___109-[_LTOfflineTranslationEngine _translateString:isFinal:withContext:toLocale:withSpans:stabilizer:completion:]_block_invoke.32
+ ___143-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:enableStreamingSpeechTranslation:enableMultiFieldInput:resultHandler:]_block_invoke
+ ___143-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:enableStreamingSpeechTranslation:enableMultiFieldInput:resultHandler:]_block_invoke.10
+ ___143-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:enableStreamingSpeechTranslation:enableMultiFieldInput:resultHandler:]_block_invoke.10.cold.1
+ ___143-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:enableStreamingSpeechTranslation:enableMultiFieldInput:resultHandler:]_block_invoke.5
+ ___143-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:enableStreamingSpeechTranslation:enableMultiFieldInput:resultHandler:]_block_invoke.7
+ ___143-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:enableStreamingSpeechTranslation:enableMultiFieldInput:resultHandler:]_block_invoke.8
+ ___143-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:enableStreamingSpeechTranslation:enableMultiFieldInput:resultHandler:]_block_invoke.cold.1
+ ___143-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:enableStreamingSpeechTranslation:enableMultiFieldInput:resultHandler:]_block_invoke.cold.2
+ ___143-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:enableStreamingSpeechTranslation:enableMultiFieldInput:resultHandler:]_block_invoke.cold.3
+ ___26-[_LTDAssetModel isEqual:]_block_invoke
+ ___28+[_LTDASRAssetService queue]_block_invoke
+ ___29+[_LTDUAFAssetService _queue]_block_invoke
+ ___29-[_LTDAssetModel isInstalled]_block_invoke
+ ___29-[_LTDStreamStabilizer reset]_block_invoke
+ ___34-[_LTHotfixManager refreshHotfix:]_block_invoke.20
+ ___34-[_LTHotfixManager refreshHotfix:]_block_invoke.20.cold.1
+ ___35-[_LTDAssetModel supportsTaskHint:]_block_invoke
+ ___36+[_LTDTTSAssetService _allTTSAssets]_block_invoke
+ ___36-[_LTDAssetModel addComponentAsset:]_block_invoke
+ ___37-[_LTTranslationServer _logStateSoon]_block_invoke.47
+ ___38-[_LTDStreamStabilizer stableSegments]_block_invoke
+ ___39+[_LTDUAFAssetService _allAssetLocales]_block_invoke
+ ___39+[_LTDUAFAssetService _allAssetLocales]_block_invoke.313
+ ___39+[_LTDUAFAssetService _allAssetLocales]_block_invoke_2
+ ___41+[_LTDTTSAssetService _subscribeToVoice:]_block_invoke
+ ___41+[_LTDTTSAssetService _subscribeToVoice:]_block_invoke.cold.1
+ ___42+[_LTDAssetService purgeAsset:completion:]_block_invoke
+ ___42+[_LTDAssetService purgeAsset:completion:]_block_invoke_2
+ ___42+[_LTDUAFAssetService _allAssetSpecifiers]_block_invoke
+ ___42-[_LTDStreamStabilizer setStableSegments:]_block_invoke
+ ___42-[_LTDStreamStabilizer stabilizationState]_block_invoke
+ ___45+[_LTDASRAssetService purgeAsset:completion:]_block_invoke
+ ___45+[_LTDUAFAssetService purgeAsset:completion:]_block_invoke
+ ___45-[_LTDAssetModel getLocalFileUrlForTaskHint:]_block_invoke
+ ___46+[_LTDASRAssetService _purgeAsset:completion:]_block_invoke
+ ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.345
+ ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.345.cold.1
+ ___46+[_LTDUAFAssetService _registerChangeHandler:]_block_invoke
+ ___47-[_LTServerSpeechSession swapLocalesAndRestart]_block_invoke
+ ___48+[_LTDUAFBridge assetUsagesForAssetType:locale:]_block_invoke
+ ___48-[_LTDLanguageAssetCache notify:ofObservations:]_block_invoke
+ ___49-[_LTServerSpeechSession translatorDidTranslate:]_block_invoke
+ ___49-[_LTTranslationServer scheduleAssetCleanupWork:]_block_invoke.61
+ ___49-[_LTTranslationServer updateOVADStreamingState:]_block_invoke
+ ___50-[_LTServerSpeechSession speechRecognitionResult:]_block_invoke
+ ___51+[_LTDUAFAssetService queryAssetType:filter:error:]_block_invoke
+ ___51+[_LTDUAFAssetService queryAssetType:filter:error:]_block_invoke_2
+ ___51-[_LTServerSpeechSession updateOVADStreamingState:]_block_invoke
+ ___52+[_LTDUAFAssetService _allAssetSpecifiersByLocaleId]_block_invoke
+ ___53+[_LTDASRAssetService availableAssetsWithCompletion:]_block_invoke
+ ___53+[_LTDASRAssetService availableAssetsWithCompletion:]_block_invoke_2
+ ___53+[_LTDASRAssetService availableAssetsWithCompletion:]_block_invoke_3
+ ___53+[_LTDASRAssetService installedAssetsWithCompletion:]_block_invoke
+ ___53+[_LTDASRAssetService installedAssetsWithCompletion:]_block_invoke_2
+ ___53+[_LTDASRAssetService installedAssetsWithCompletion:]_block_invoke_3
+ ___56+[_LTDUAFAssetService queryAssetType:filter:completion:]_block_invoke
+ ___56-[_LTDLanguageAssetCache setRequiredAssets:localeRanks:]_block_invoke
+ ___57+[_LTDAssetService refreshCatalogIfNeededWithCompletion:]_block_invoke.337
+ ___58+[_LTDASRAssetService _downloadAsset:progress:completion:]_block_invoke
+ ___58+[_LTDASRAssetService _downloadAsset:progress:completion:]_block_invoke_2
+ ___59+[_LTDAssetService assetsForLocales:includeTTS:completion:]_block_invoke.371
+ ___59-[_LTTranslationServer installedLocalesForTask:completion:]_block_invoke.54
+ ___60+[_LTDASRAssetService _supportedIdentifiersWithCommpletion:]_block_invoke
+ ___60+[_LTDASRAssetService _supportedIdentifiersWithCommpletion:]_block_invoke_2
+ ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.43
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.34
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.34.cold.1
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.34.cold.2
+ ___61+[_LTDUAFAssetService _registerForAsset:progress:completion:]_block_invoke
+ ___61+[_LTDUAFAssetService _registerForAsset:progress:completion:]_block_invoke_2
+ ___62+[_LTDAssetService downloadAsset:options:progress:completion:]_block_invoke
+ ___62+[_LTDAssetService downloadAsset:options:progress:completion:]_block_invoke.302
+ ___62+[_LTDAssetService downloadAsset:options:progress:completion:]_block_invoke_2
+ ___62+[_LTDAssetService downloadAsset:options:progress:completion:]_block_invoke_2.cold.1
+ ___62-[_LTTranslationServer speak:withContext:delegate:completion:]_block_invoke.37
+ ___62-[_LTTranslationServer speak:withContext:delegate:completion:]_block_invoke.37.cold.1
+ ___62-[_LTTranslationServer speak:withContext:delegate:completion:]_block_invoke.39
+ ___64+[_LTDMAAssetService downloadAsset:options:progress:completion:]_block_invoke.335
+ ___64+[_LTDMAAssetService downloadAsset:options:progress:completion:]_block_invoke_2.336
+ ___65+[_LTDASRAssetService downloadAsset:options:progress:completion:]_block_invoke
+ ___65+[_LTDASRAssetService downloadAsset:options:progress:completion:]_block_invoke_2
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.50
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.51
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.54
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.55
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.55.cold.1
+ ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.55.cold.2
+ ___65+[_LTDUAFAssetService downloadAsset:options:progress:completion:]_block_invoke
+ ___65+[_LTDUAFAssetService downloadAsset:options:progress:completion:]_block_invoke.330
+ ___65+[_LTDUAFAssetService downloadAsset:options:progress:completion:]_block_invoke.cold.1
+ ___65+[_LTDUAFAssetService downloadAsset:options:progress:completion:]_block_invoke_2
+ ___65+[_LTDUAFAssetService downloadAsset:options:progress:completion:]_block_invoke_2.cold.1
+ ___65-[_LTOfflineTranslationEngine _waitForLIDWithContext:completion:]_block_invoke.66
+ ___65-[_LTTranslationServer translateSentence:withContext:completion:]_block_invoke.22
+ ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.22
+ ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.27
+ ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.27.cold.1
+ ___66-[_LTServerSpeechSession updateOwnVoicePendingSwapAndRestartTimer]_block_invoke
+ ___66-[_LTServerSpeechSession updateOwnVoicePendingSwapAndRestartTimer]_block_invoke.cold.1
+ ___67+[_LTDConfigurationService supportedIdentifiersForTask:completion:]_block_invoke
+ ___67+[_LTDConfigurationService supportedIdentifiersForTask:completion:]_block_invoke_2
+ ___67-[_LTTranslationServer startSpeechTranslationWithContext:delegate:]_block_invoke.43
+ ___68-[_LTOfflineTranslationEngine _concatenatedAlignmentsFromSentences:]_block_invoke
+ ___71-[_LTTranslationServer translateStreamingInput:withContext:completion:]_block_invoke
+ ___71-[_LTTranslationServer translateStreamingInput:withContext:completion:]_block_invoke.27
+ ___71-[_LTTranslationServer translateStreamingInput:withContext:completion:]_block_invoke_2
+ ___71-[_LTTranslationServer translateStreamingInput:withContext:completion:]_block_invoke_2.cold.1
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.309
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.314
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.310
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.310.cold.1
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_3
+ ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_4
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.115
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.116
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.92
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.98
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.99
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.99.cold.1
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.99.cold.2
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke_2.117
+ ___76-[_LTMultilingualSpeechRecognizer initWithModelURLs:modelVersions:taskHint:]_block_invoke
+ ___78+[_LTDASRAssetService _sfInstalledLTIdentifiersForTaskHint:filter:completion:]_block_invoke
+ ___78+[_LTDASRAssetService _sfInstalledLTIdentifiersForTaskHint:filter:completion:]_block_invoke_2
+ ___78+[_LTDASRAssetService _sfInstalledLTIdentifiersForTaskHint:filter:completion:]_block_invoke_3
+ ___78+[_LTDASRAssetService _sfSupportedLTIdentifiersForTaskHint:filter:completion:]_block_invoke
+ ___78+[_LTDASRAssetService _sfSupportedLTIdentifiersForTaskHint:filter:completion:]_block_invoke_2
+ ___78+[_LTDASRAssetService _sfSupportedLTIdentifiersForTaskHint:filter:completion:]_block_invoke_3
+ ___78-[_LTTranslationServer startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.35
+ ___80-[_LTClientConnection startLanguageStatusChangeObservation:taskHint:completion:]_block_invoke
+ ___80-[_LTClientConnection startLanguageStatusChangeObservation:taskHint:completion:]_block_invoke_2
+ ___80-[_LTOfflineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.63
+ ___80-[_LTOfflineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.63.cold.1
+ ___82-[_LTTranslationResult(Daemon) updateAlignmentWithSourceSpans:offlineTargetSpans:]_block_invoke
+ ___82-[_LTTranslationResult(Daemon) updateAlignmentWithSourceSpans:offlineTargetSpans:]_block_invoke.cold.1
+ ___83-[_LTTranslationServer translateParagraphs:withContext:paragraphResult:completion:]_block_invoke.24
+ ___83-[_LTTranslationServer translateParagraphs:withContext:paragraphResult:completion:]_block_invoke.24.cold.1
+ ___85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.74
+ ___85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.74.cold.1
+ ___85-[_LTOfflineTranslationEngine translateStreamingInput:context:stabilizer:completion:]_block_invoke
+ ___85-[_LTOfflineTranslationEngine translateStreamingInput:context:stabilizer:completion:]_block_invoke_2
+ ___85-[_LTOfflineTranslationEngine translateStreamingInput:context:stabilizer:completion:]_block_invoke_2.cold.1
+ ___87-[_LTTextLanguageDetectionResult(Daemon) initWithScorer:lowConfidenceLocales:strategy:]_block_invoke
+ ___97+[_LTDLanguageAssetService startLanguageStatusSession:taskHint:progress:observations:completion:]_block_invoke
+ ___99-[_LTSpeechRecognizer startRecognitionWithAutoStop:enableStreamingSpeechTranslation:resultHandler:]_block_invoke
+ ____LTOSLogStabilization_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72r80r_e5_v8?0ls32l8s40l8r72l8s48l8s56l8r80l8s64l8
+ ___block_descriptor_104_ea8_32s40s48s56s64s72s80s88bs96w_e5_v8?0lw96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_112_ea8_32s40s48s56s64s72s80s88bs96w_e17_v16?0"NSArray"8lw96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88bs96r104r_e48_v24?0"_LTSpeechRecognitionResult"8"NSError"16lr96l8s32l8s40l8s48l8s88l8s56l8s64l8s72l8s80l8r104l8
+ ___block_descriptor_32_e41_B32?0"<_LTDAssetModelProtocol>"8Q16^B24l
+ ___block_descriptor_32_e43_"_LTDAssetModel"16?0"_LTDUAFAssetModel"8l
+ ___block_descriptor_40_e28_"NSString"16?0"NSString"8l
+ ___block_descriptor_40_e34_B16?0"<_LTDAssetModelProtocol>"8l
+ ___block_descriptor_40_e8_32bs_e27_v16?0"_LTDUAFAssetModel"8ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v16?0Q8ls32l8
+ ___block_descriptor_40_e8_32s_e18_B16?0"NSString"8ls32l8
+ ___block_descriptor_40_e8_32s_e34_B16?0"<_LTDAssetModelProtocol>"8ls32l8
+ ___block_descriptor_40_e8_32s_e38_B16?0"_LTLanguageStatusObservation"8ls32l8
+ ___block_descriptor_40_e8_32s_e61_"_LTLanguageStatusObservation"16?0"_LTLanguageAssetModel"8ls32l8
+ ___block_descriptor_40_e8_32s_e68_"_LTLanguageStatusObservation"16?0"_LTLanguageStatusObservation"8ls32l8
+ ___block_descriptor_40_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_41_ea8_32s_e16_v16?0"NSData"8ls32l8
+ ___block_descriptor_48_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e34_v16?0"<_LTDAssetModelProtocol>"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e39_v24?0"_LTDASRAssetModel"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e8_v16?0Q8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e46_v24?0"<_LTDAssetModelProtocol>"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e28_"NSString"16?0"NSString"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e37_"_LTAlignment"16?0"EMTProjection"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e18_v16?0"TTSAsset"8ls32l8
+ ___block_descriptor_49_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls40l8s32l8
+ ___block_descriptor_50_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e14_v32?0d8q16q24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e18_v16?0"TTSAsset"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e32_v16?0"MAProgressNotification"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e15_v16?0"NSSet"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSError"8ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s_e32_v32?0"NSLocale"8"NSURL"16^B24ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32bs40bs48w_e55_v24?0"_LTStabilizationTranslationResult"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40bs48r_e27_v16?0"UAFAssetSetStatus"8ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40r48r56r_e5_v8?0lr40l8s32l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e27_v24?0"NSSet"8"NSError"16lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_ea8_32s40s48s56s_e30_v16?0"_LTTranslationResult"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56bs_e17_v16?0"NSError"8ls32l8s48l8s40l8s56l8
+ ___block_descriptor_72_e8_32s40s48bs56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48bs56w_e5_v8?0lw56l8s32l8s48l8s40l8
+ ___block_descriptor_72_e8_32s40s48r_e29_v24?0"NSArray"8"NSError"16lr48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56bs64w_e14_v16?0?<v?>8lw64l8s32l8s56l8s40l8s48l8
+ ___block_descriptor_81_ea8_32s40s48s56s64bs72w_e30_v16?0"_LTTranslationResult"8lw72l8s64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56bs64bs_e29_v24?0"NSArray"8"NSError"16ls56l8s32l8s40l8s48l8s64l8
+ ___block_literal_global.301
+ ___block_literal_global.309
+ ___block_literal_global.316
+ ___block_literal_global.322
+ ___block_literal_global.323
+ ___block_literal_global.326
+ ___block_literal_global.340
+ ___block_literal_global.341
+ ___block_literal_global.342
+ ___block_literal_global.350
+ ___block_literal_global.353
+ ___block_literal_global.36
+ ___block_literal_global.44
+ ___block_literal_global.50
+ ___block_literal_global.8
+ __allAssetLocales.onceToken
+ __allAssetLocales.result
+ __allAssetSpecifiers.onceToken
+ __allAssetSpecifiers.result
+ __allAssetSpecifiersByLocaleId.onceToken
+ __allAssetSpecifiersByLocaleId.result
+ __cachedTTSAssets
+ _kLTASRAssetAverageSize
+ _kLTAssetMinimumSize
+ _kLTAssetTypeEndpoint_MA
+ _kLTAssetTypeMT_MA
+ _kLTAssetTypeTTS
+ _kLTAssetTypeUAF
+ _kLTDASRAssetTypeGASR
+ _kLTDASRAssetTypeNGASR
+ _kLTMTAssetAverageSize
+ _kLTMTPartialAssetAverageSize
+ _kLTPBAssetAverageSize
+ _kLTTTSAssetAverageSize
+ _kLTUAFASRLanguage
+ _kLTUAFDAssetSetName
+ _kLTUAFMTLanguage
+ _kUAFAssetMetadataAssetIdKey
+ _kUAFAssetMetadataAssetSpecifierKey
+ _kUAFAssetMetadataAssetVersionKey
+ _kUAFAssetMetadataDownloadSizeKey
+ _kUAFAssetMetadataUnarchivedSizeKey
+ _objc_msgSend$_addComponentAsset:
+ _objc_msgSend$_addSyntheticASREntriesToAssets:
+ _objc_msgSend$_allAssetLocales
+ _objc_msgSend$_allAssetSpecifiers
+ _objc_msgSend$_allAssetSpecifiersByLocaleId
+ _objc_msgSend$_allTTSAssets
+ _objc_msgSend$_assetProviderForAssetType:
+ _objc_msgSend$_assetStateForOfflineState:
+ _objc_msgSend$_assetTypesFoDevice
+ _objc_msgSend$_awaitDownloadForAsset:
+ _objc_msgSend$_catalog
+ _objc_msgSend$_concatenatedAlignmentsFromSentences:
+ _objc_msgSend$_configBundleURL
+ _objc_msgSend$_createSymlinkDirectoryForLocalePair:assets:configAsset:validateIfNeeded:
+ _objc_msgSend$_defaultAssetType
+ _objc_msgSend$_downloadAsset:progress:completion:
+ _objc_msgSend$_errorFor:message:
+ _objc_msgSend$_errorForAssetProviderResolutionForAssetType:
+ _objc_msgSend$_handleTranslationResults:withContext:sourceString:sourceSpans:stabilizer:
+ _objc_msgSend$_loadEtiquetteSanitizersForTaskHint:
+ _objc_msgSend$_localeRanks
+ _objc_msgSend$_mapIdentifierForSiriTTS:
+ _objc_msgSend$_offlineStateForAssetState:
+ _objc_msgSend$_prepareStabilizerForContext:
+ _objc_msgSend$_purgeAsset:completion:
+ _objc_msgSend$_registerForAsset:progress:completion:
+ _objc_msgSend$_requiredAssetSpecifiers
+ _objc_msgSend$_selectedLocales
+ _objc_msgSend$_sfInstalledLTIdentifiersForTaskHint:filter:completion:
+ _objc_msgSend$_sfSupportedLTIdentifiersForTaskHint:filter:completion:
+ _objc_msgSend$_sfTaskHintForLTTaskHint:
+ _objc_msgSend$_subscribe:completion:
+ _objc_msgSend$_subscribeToVoice:
+ _objc_msgSend$_subscribedAssetSpecifiers
+ _objc_msgSend$_subscriptions
+ _objc_msgSend$_supportedIdentifiersWithCommpletion:
+ _objc_msgSend$_taskHintForLTAssetType:
+ _objc_msgSend$_taskHintMap
+ _objc_msgSend$_translateString:isFinal:withContext:toLocale:withSpans:stabilizer:completion:
+ _objc_msgSend$_unsubscribe:completion:
+ _objc_msgSend$_updateOVADStreamingState_onQueue:
+ _objc_msgSend$_validTopLevelSymlinkDirectory:configAssetURL:assets:
+ _objc_msgSend$addComponentAsset:
+ _objc_msgSend$alignments
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$asrAssetWithIdentifier:taskHint:
+ _objc_msgSend$assetIdentifierForAssetSpecifier:
+ _objc_msgSend$assetSpecifierForAssetIdentifier:
+ _objc_msgSend$assetSpecifierForAssetUsages:
+ _objc_msgSend$assetSpecifiersForAssetType:locale:
+ _objc_msgSend$assetSubtype
+ _objc_msgSend$assetTypeForAssetSpecifier:
+ _objc_msgSend$assetTypeForAssetUsage:
+ _objc_msgSend$assetUsageValuesForAssetType:
+ _objc_msgSend$assetUsagesForAssetSpecifier:
+ _objc_msgSend$assetUsagesForAssetType:
+ _objc_msgSend$assetUsagesForAssetType:locale:
+ _objc_msgSend$availableAssetsWithCompletion:
+ _objc_msgSend$availableIdentifiers
+ _objc_msgSend$cancelOwnVoicePendingSwapAndRestartTimer
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$completedBytes
+ _objc_msgSend$components
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$dictionaryForKey:
+ _objc_msgSend$disambiguableResult
+ _objc_msgSend$discreteProgressWithIdentifier:offlineState:
+ _objc_msgSend$downloadStatus
+ _objc_msgSend$downloadStatusForSubscriber:subscriptionName:
+ _objc_msgSend$enableMultiFieldInput
+ _objc_msgSend$enableOfflineStreamStabilizer
+ _objc_msgSend$enableStreamingSpeechTranslation
+ _objc_msgSend$enableTranslationSemanticSegmentation
+ _objc_msgSend$endOfUtterance
+ _objc_msgSend$fetchAssetWithConfig:clientIdentifier:progress:completion:
+ _objc_msgSend$forcePendingSwapAndRestart
+ _objc_msgSend$generateSilentAudioDataWithDuration:
+ _objc_msgSend$getLocalFileUrlForTaskHint:
+ _objc_msgSend$hash
+ _objc_msgSend$initWithAssetSpecifier:
+ _objc_msgSend$initWithConfiguration:overrides:overrideConfigFiles:generalVoc:lexiconEnh:itnEnh:
+ _objc_msgSend$initWithConfiguration:useQuasarFormatter:overrides:
+ _objc_msgSend$initWithFormattedString:sanitizedFormattedString:confidence:lowConfidence:romanization:tokens:preToPostITN:stableString:
+ _objc_msgSend$initWithID:taskHint:progress:observations:completion:
+ _objc_msgSend$initWithLanguage:taskHint:
+ _objc_msgSend$initWithLocale:progress:downloadSize:status:rank:
+ _objc_msgSend$initWithLocalePair:taskHint:assetInfo:selfLoggingManager:
+ _objc_msgSend$initWithModelURL:language:modelVersion:taskHint:
+ _objc_msgSend$initWithModelURLs:modelVersions:taskHint:
+ _objc_msgSend$initWithName:assetSets:usageAliases:expires:
+ _objc_msgSend$initWithOutput:stableSegments:
+ _objc_msgSend$initWithPackage:locale:modelVersion:taskHint:isFinal:endOfUtterance:
+ _objc_msgSend$initWithResult:locale:modelVersion:taskHint:isFinal:
+ _objc_msgSend$initWithScorer:lowConfidenceLocales:strategy:
+ _objc_msgSend$initWithText:sourceText:locale:isFinal:sourceIdentifier:
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$installedLanguagesForTaskHint:completion:
+ _objc_msgSend$instancesRespondToSelector:
+ _objc_msgSend$isASRModelSupportingTaskHint:
+ _objc_msgSend$isCompleteBidirectionalModelForTaskHint:
+ _objc_msgSend$isCompletePassthroughModelForTaskHint:
+ _objc_msgSend$isGeneralASRSupportedOnDevice
+ _objc_msgSend$isSupportedTaskHint:
+ _objc_msgSend$knownUsagesForAssetSet:usageType:
+ _objc_msgSend$languageStatusChangedForTaskHint:progress:observations:
+ _objc_msgSend$location
+ _objc_msgSend$lt_asrModels
+ _objc_msgSend$lt_asrTask
+ _objc_msgSend$lt_asrTasks
+ _objc_msgSend$lt_firstObjectPassingTest:
+ _objc_msgSend$lt_mtCustomModel
+ _objc_msgSend$lt_overrides
+ _objc_msgSend$lt_stringArrayDebugDescription:
+ _objc_msgSend$ltd_invalidResultError
+ _objc_msgSend$managedAssetProvider
+ _objc_msgSend$minusSet:
+ _objc_msgSend$notify:ofObservations:
+ _objc_msgSend$observationFilterConditions
+ _objc_msgSend$observeAssetSet:queue:handler:
+ _objc_msgSend$pairNamesForLocaleIdentifiers:
+ _objc_msgSend$pairNamesForLocales:
+ _objc_msgSend$pathToAssetWithConfig:clientIdentifier:
+ _objc_msgSend$primaryLanguage
+ _objc_msgSend$removeObjectsInRange:
+ _objc_msgSend$resultWithPackage:locale:modelVersion:taskHint:isFinal:
+ _objc_msgSend$resultWithPackage:locale:modelVersion:taskHint:isFinal:endOfUtterance:
+ _objc_msgSend$resultWithResult:locale:modelVersion:taskHint:isFinal:
+ _objc_msgSend$retrieveAssetSet:usages:
+ _objc_msgSend$reverseObjectEnumerator
+ _objc_msgSend$setAssetName:
+ _objc_msgSend$setAssetPath:
+ _objc_msgSend$setAssetSubtype:
+ _objc_msgSend$setEndOfUtterance:
+ _objc_msgSend$setHotfixURL:
+ _objc_msgSend$setProvider:
+ _objc_msgSend$setRequiredAssets:localeRanks:
+ _objc_msgSend$setStablePrefixState:
+ _objc_msgSend$setStableSegments:
+ _objc_msgSend$setStableString:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$sharedManager
+ _objc_msgSend$sourceIdentifier
+ _objc_msgSend$speechModelURLForLocale:taskHint:
+ _objc_msgSend$speechTranslationAssetInfoForLocalePair:taskHint:error:
+ _objc_msgSend$stabilizationState
+ _objc_msgSend$stablePrefixState
+ _objc_msgSend$stableSegments
+ _objc_msgSend$startLanguageStatusSession:taskHint:progress:observations:completion:
+ _objc_msgSend$startRecognitionForLocale:autoEndpoint:enableStreamingSpeechTranslation:enableMultiFieldInput:resultHandler:
+ _objc_msgSend$startRecognitionWithAutoStop:enableStreamingSpeechTranslation:resultHandler:
+ _objc_msgSend$stateForAsset:
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$subscribe:subscriptions:queue:completion:
+ _objc_msgSend$subscribedVoices
+ _objc_msgSend$subscriptionsForSubscriber:
+ _objc_msgSend$supportedIdentifiersForTask:completion:
+ _objc_msgSend$supportedLanguagesForTaskHint:
+ _objc_msgSend$supportedLanguagesForTaskHint:completion:
+ _objc_msgSend$supportedLocaleIdentifiersForTaskHint:
+ _objc_msgSend$supportedLocalePairsForTask:completion:
+ _objc_msgSend$supportedLocalesSubsetForTask:
+ _objc_msgSend$supportsTaskHint:
+ _objc_msgSend$swapLocalesAndRestart
+ _objc_msgSend$swapLocalesAndRestartWithStateResetAndLogMessage:
+ _objc_msgSend$targetProjections
+ _objc_msgSend$targetText
+ _objc_msgSend$technology
+ _objc_msgSend$totalBytes
+ _objc_msgSend$translateStreamingInput:context:stabilizer:completion:
+ _objc_msgSend$translateStreamingInput:withContext:completion:
+ _objc_msgSend$unsubscribe:subscriptionNames:queue:completion:
+ _objc_msgSend$unsubscribeFromAssetWithConfig:clientIdentifier:completion:
+ _objc_msgSend$updateAlignmentWithSourceSpans:offlineTargetSpans:
+ _objc_msgSend$updateAssetsForSubscriber:subscriptionName:policies:queue:detailedProgress:completion:
+ _objc_msgSend$updateOVADStreamingState:
+ _objc_msgSend$updateOwnVoicePendingSwapAndRestartTimer
+ _objc_msgSend$updatePercentComplete:
+ _objc_msgSend$weight
+ _objc_msgSend$weightedLocaleWithStrategy:
+ _objc_retain_x11
+ _os_unfair_lock_assert_not_owner
- +[NSString(VS4CC) vs_stringFrom4CC:]
- +[NSUserDefaults(TranslationDaemonAdditions) lt_appGroupDefaults]
- +[NSUserDefaults(TranslationDaemonAdditions) lt_appGroupDefaults].cold.1
- +[_LTAudioDecoder sharedInstance]
- +[_LTAudioDecoder sharedInstance].cold.1
- +[_LTDAssetService _installConfigAsset:completion:].cold.3
- +[_LTDAssetService _pairNamesForLocales:]
- +[_LTDLanguageAssetService startLanguageStatusSession:observationType:progress:observations:completion:]
- +[_LTDTTSAssetService _availableTTSAssetsByLanguage]
- +[_LTDTTSAssetService _availableTTSAssetsByLanguage].cold.1
- +[_LTDTTSAssetService _availableTTSAssets]
- +[_LTDTTSAssetService _ttsAssetForLanguage:name:gender:]
- +[_LTDTTSAssetService installedAssetIdentifiers]
- +[_LTDTTSAssetService installedAssetIdentifiers].cold.1
- +[_LTDTTSAssetService setAutoDownloadedAssets:]
- +[_LTDTTSAssetService ttsAssetForLocaleIdentifier:].cold.2
- +[_LTDTTSAssetService ttsAssetForLocaleIdentifier:].cold.3
- +[_LTDUAFAssetService assetTypeForAssetIdentifier:]
- +[_LTSpeechRecognitionResult(Daemon) resultWithPackage:locale:modelVersion:isFinal:]
- +[_LTSpeechRecognitionResult(Daemon) resultWithResult:locale:modelVersion:isFinal:]
- +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:validateIfNeeded:].cold.1
- +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:validateIfNeeded:].cold.10
- +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:validateIfNeeded:].cold.2
- +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:validateIfNeeded:].cold.3
- +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:validateIfNeeded:].cold.4
- +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:validateIfNeeded:].cold.5
- +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:validateIfNeeded:].cold.6
- +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:validateIfNeeded:].cold.7
- +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:validateIfNeeded:].cold.8
- +[_LTSpeechTranslationAssetInfo _createSymlinkDirectoryForLocalePair:assets:validateIfNeeded:].cold.9
- -[_LTAudioDecoder _audioDecoderFrom:to:]
- -[_LTAudioDecoder _audioDecoderFrom:to:].cold.1
- -[_LTAudioDecoder beginChunkDecoderForStreamDescription:]
- -[_LTAudioDecoder dealloc]
- -[_LTAudioDecoder decodeChunk:outError:]
- -[_LTAudioDecoder decodeChunks:from:to:outError:]
- -[_LTAudioDecoder decodeTo48KHzPCMFromChunks:from:outError:]
- -[_LTAudioDecoder endChunkDecoding]
- -[_LTAudioDecoder extractAudioChunksFromOpusWithData:packetCount:packetDescriptions:]
- -[_LTAudioDecoder extractAudioChunksFromOpusWithData:packetCount:packetDescriptions:].cold.1
- -[_LTAudioDecoder get48khzPCMDescription]
- -[_LTClientConnection initWithConnection:server:trusted:].cold.4
- -[_LTClientConnection startLanguageStatusChangeObservation:type:completion:]
- -[_LTDLanguageAssetCache setRequiredAssets:]
- -[_LTDLanguageAssetCacheObserver initWithID:type:progress:observations:completion:]
- -[_LTDLanguageAssetCacheObserver type]
- -[_LTDMAAssetModel identifier].cold.1
- -[_LTDMAAssetModel initWithMAAsset:]
- -[_LTDMAAssetModel initWithMAAsset:].cold.1
- -[_LTDMAAssetModel maAsset]
- -[_LTDMAAssetModel setMaAsset:]
- -[_LTDTTSAssetModel ttsAsset]
- -[_LTMultilingualSpeechRecognizer initWithModelURLs:modelVersions:]
- -[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:resultHandler:]
- -[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:resultHandler:].cold.1
- -[_LTOfflineAssetManager speechTranslationAssetInfoForLocalePair:error:]
- -[_LTOfflineAssetManager speechTranslationAssetInfoForLocalePair:error:].cold.1
- -[_LTOfflineAssetManager speechTranslationAssetInfoForLocalePair:error:].cold.2
- -[_LTOfflineTranslationEngine _handleTranslationResults:withContext:sourceString:]
- -[_LTOfflineTranslationEngine _loadEtiquetteSanitizers]
- -[_LTOfflineTranslationEngine _loadEtiquetteSanitizers].cold.1
- -[_LTOfflineTranslationEngine _loadEtiquetteSanitizers].cold.2
- -[_LTOfflineTranslationEngine _loadRecognizersWithContext:].cold.3
- -[_LTOfflineTranslationEngine _loadTranslatorForTask:].cold.2
- -[_LTOfflineTranslationEngine _translateString:isFinal:withContext:toLocale:withSpans:completion:]
- -[_LTOfflineTranslationEngine initWithLocalePair:assetInfo:selfLoggingManager:]
- -[_LTSpeechRecognitionResult(Daemon) initWithPackage:locale:modelVersion:isFinal:]
- -[_LTSpeechRecognitionResult(Daemon) initWithPackage:locale:modelVersion:isFinal:].cold.1
- -[_LTSpeechRecognitionResult(Daemon) initWithResult:locale:modelVersion:isFinal:]
- -[_LTSpeechRecognizer initWithModelURL:language:modelVersion:]
- -[_LTSpeechRecognizer initWithModelURL:language:modelVersion:].cold.1
- -[_LTSpeechRecognizer initWithModelURL:language:modelVersion:].cold.2
- -[_LTSpeechRecognizer startRecognitionWithAutoStop:resultHandler:]
- -[_LTSpeechTranslationAssetInfo isCompleteBidirectionalModel]
- -[_LTSpeechTranslationAssetInfo isCompletePassthroughModel]
- -[_LTSpeechTranslationAssetInfo speechModelURLForLocale:]
- -[_LTTextLanguageDetectionResult(Daemon) initWithScorer:]
- -[_LTTextLanguageDetectorScorer weightedLocale].cold.1
- GCC_except_table100
- GCC_except_table1009
- GCC_except_table1017
- GCC_except_table1033
- GCC_except_table1035
- GCC_except_table1045
- GCC_except_table1049
- GCC_except_table1089
- GCC_except_table1091
- GCC_except_table1109
- GCC_except_table1141
- GCC_except_table1149
- GCC_except_table1178
- GCC_except_table1201
- GCC_except_table1203
- GCC_except_table1241
- GCC_except_table1247
- GCC_except_table1263
- GCC_except_table1265
- GCC_except_table1271
- GCC_except_table1301
- GCC_except_table1341
- GCC_except_table1343
- GCC_except_table1370
- GCC_except_table1392
- GCC_except_table1398
- GCC_except_table1404
- GCC_except_table1434
- GCC_except_table1440
- GCC_except_table1446
- GCC_except_table1467
- GCC_except_table1469
- GCC_except_table1491
- GCC_except_table1495
- GCC_except_table1504
- GCC_except_table1508
- GCC_except_table1512
- GCC_except_table1518
- GCC_except_table1571
- GCC_except_table1583
- GCC_except_table1601
- GCC_except_table1625
- GCC_except_table1627
- GCC_except_table1670
- GCC_except_table1688
- GCC_except_table1692
- GCC_except_table1724
- GCC_except_table1746
- GCC_except_table1760
- GCC_except_table1772
- GCC_except_table1794
- GCC_except_table1798
- GCC_except_table1806
- GCC_except_table1812
- GCC_except_table1818
- GCC_except_table1864
- GCC_except_table1878
- GCC_except_table1892
- GCC_except_table1896
- GCC_except_table1900
- GCC_except_table1902
- GCC_except_table1904
- GCC_except_table1948
- GCC_except_table1950
- GCC_except_table1954
- GCC_except_table1976
- GCC_except_table1984
- GCC_except_table2002
- GCC_except_table2008
- GCC_except_table2022
- GCC_except_table2028
- GCC_except_table2030
- GCC_except_table2032
- GCC_except_table2052
- GCC_except_table2067
- GCC_except_table2069
- GCC_except_table2070
- GCC_except_table2072
- GCC_except_table2073
- GCC_except_table2079
- GCC_except_table2091
- GCC_except_table2097
- GCC_except_table2104
- GCC_except_table2105
- GCC_except_table2111
- GCC_except_table2122
- GCC_except_table2123
- GCC_except_table2125
- GCC_except_table2126
- GCC_except_table2128
- GCC_except_table2129
- GCC_except_table2130
- GCC_except_table2131
- GCC_except_table2134
- GCC_except_table2140
- GCC_except_table2153
- GCC_except_table2154
- GCC_except_table2155
- GCC_except_table2158
- GCC_except_table2159
- GCC_except_table2160
- GCC_except_table2161
- GCC_except_table2162
- GCC_except_table2163
- GCC_except_table2164
- GCC_except_table2165
- GCC_except_table2166
- GCC_except_table2193
- GCC_except_table2194
- GCC_except_table2197
- GCC_except_table2198
- GCC_except_table2204
- GCC_except_table2213
- GCC_except_table2216
- GCC_except_table2217
- GCC_except_table2218
- GCC_except_table2219
- GCC_except_table2220
- GCC_except_table2222
- GCC_except_table2228
- GCC_except_table2238
- GCC_except_table2244
- GCC_except_table2246
- GCC_except_table2249
- GCC_except_table2250
- GCC_except_table2264
- GCC_except_table2265
- GCC_except_table2268
- GCC_except_table2269
- GCC_except_table2270
- GCC_except_table2280
- GCC_except_table2283
- GCC_except_table2288
- GCC_except_table2294
- GCC_except_table2299
- GCC_except_table2306
- GCC_except_table2309
- GCC_except_table2310
- GCC_except_table2313
- GCC_except_table2319
- GCC_except_table2325
- GCC_except_table2339
- GCC_except_table2340
- GCC_except_table2346
- GCC_except_table2349
- GCC_except_table2352
- GCC_except_table2353
- GCC_except_table2354
- GCC_except_table2355
- GCC_except_table2361
- GCC_except_table2365
- GCC_except_table2367
- GCC_except_table2376
- GCC_except_table2381
- GCC_except_table2389
- GCC_except_table2399
- GCC_except_table2405
- GCC_except_table2407
- GCC_except_table2409
- GCC_except_table2410
- GCC_except_table2411
- GCC_except_table2412
- GCC_except_table2413
- GCC_except_table2419
- GCC_except_table2421
- GCC_except_table2423
- GCC_except_table2425
- GCC_except_table2434
- GCC_except_table2439
- GCC_except_table2444
- GCC_except_table2447
- GCC_except_table2449
- GCC_except_table2459
- GCC_except_table2474
- GCC_except_table2479
- GCC_except_table2485
- GCC_except_table2490
- GCC_except_table2497
- GCC_except_table2500
- GCC_except_table2506
- GCC_except_table2511
- GCC_except_table2512
- GCC_except_table2518
- GCC_except_table2525
- GCC_except_table2526
- GCC_except_table2527
- GCC_except_table2538
- GCC_except_table2539
- GCC_except_table2541
- GCC_except_table2547
- GCC_except_table2549
- GCC_except_table2551
- GCC_except_table2553
- GCC_except_table2554
- GCC_except_table2562
- GCC_except_table2567
- GCC_except_table2577
- GCC_except_table2580
- GCC_except_table2581
- GCC_except_table2582
- GCC_except_table2586
- GCC_except_table2587
- GCC_except_table2588
- GCC_except_table2593
- GCC_except_table2607
- GCC_except_table2608
- GCC_except_table2612
- GCC_except_table2613
- GCC_except_table2616
- GCC_except_table2618
- GCC_except_table2619
- GCC_except_table2621
- GCC_except_table2622
- GCC_except_table2628
- GCC_except_table2653
- GCC_except_table2654
- GCC_except_table2661
- GCC_except_table2667
- GCC_except_table2668
- GCC_except_table2674
- GCC_except_table2676
- GCC_except_table2677
- GCC_except_table2680
- GCC_except_table2682
- GCC_except_table2696
- GCC_except_table2703
- GCC_except_table2708
- GCC_except_table2709
- GCC_except_table2710
- GCC_except_table2716
- GCC_except_table2721
- GCC_except_table2722
- GCC_except_table2723
- GCC_except_table2729
- GCC_except_table2731
- GCC_except_table2732
- GCC_except_table2734
- GCC_except_table2735
- GCC_except_table2736
- GCC_except_table2743
- GCC_except_table2745
- GCC_except_table2754
- GCC_except_table2756
- GCC_except_table2757
- GCC_except_table2758
- GCC_except_table2759
- GCC_except_table2766
- GCC_except_table2769
- GCC_except_table2772
- GCC_except_table2787
- GCC_except_table2799
- GCC_except_table2806
- GCC_except_table2808
- GCC_except_table2809
- GCC_except_table2812
- GCC_except_table2813
- GCC_except_table2814
- GCC_except_table2822
- GCC_except_table2835
- GCC_except_table2838
- GCC_except_table2840
- GCC_except_table2841
- GCC_except_table2842
- GCC_except_table2843
- GCC_except_table2851
- GCC_except_table2856
- GCC_except_table2862
- GCC_except_table2868
- GCC_except_table2870
- GCC_except_table2871
- GCC_except_table2872
- GCC_except_table2877
- GCC_except_table2879
- GCC_except_table2881
- GCC_except_table2887
- GCC_except_table2891
- GCC_except_table2893
- GCC_except_table2894
- GCC_except_table2896
- GCC_except_table2903
- GCC_except_table2916
- GCC_except_table2917
- GCC_except_table292
- GCC_except_table2923
- GCC_except_table2929
- GCC_except_table2930
- GCC_except_table2936
- GCC_except_table2943
- GCC_except_table2945
- GCC_except_table2946
- GCC_except_table2950
- GCC_except_table2951
- GCC_except_table2952
- GCC_except_table2955
- GCC_except_table2957
- GCC_except_table2971
- GCC_except_table2972
- GCC_except_table2974
- GCC_except_table2976
- GCC_except_table2977
- GCC_except_table2983
- GCC_except_table2985
- GCC_except_table2988
- GCC_except_table2993
- GCC_except_table2996
- GCC_except_table2997
- GCC_except_table2999
- GCC_except_table3007
- GCC_except_table3020
- GCC_except_table3026
- GCC_except_table3030
- GCC_except_table3042
- GCC_except_table3045
- GCC_except_table3046
- GCC_except_table3047
- GCC_except_table3059
- GCC_except_table3066
- GCC_except_table3070
- GCC_except_table3072
- GCC_except_table3074
- GCC_except_table3076
- GCC_except_table3083
- GCC_except_table3093
- GCC_except_table3096
- GCC_except_table3102
- GCC_except_table3109
- GCC_except_table523
- GCC_except_table559
- GCC_except_table561
- GCC_except_table565
- GCC_except_table585
- GCC_except_table591
- GCC_except_table593
- GCC_except_table599
- GCC_except_table619
- GCC_except_table623
- GCC_except_table635
- GCC_except_table653
- GCC_except_table673
- GCC_except_table699
- GCC_except_table721
- GCC_except_table723
- GCC_except_table737
- GCC_except_table741
- GCC_except_table763
- GCC_except_table783
- GCC_except_table785
- GCC_except_table787
- GCC_except_table803
- GCC_except_table825
- GCC_except_table841
- GCC_except_table859
- GCC_except_table883
- GCC_except_table889
- GCC_except_table891
- GCC_except_table903
- GCC_except_table905
- GCC_except_table937
- GCC_except_table959
- GCC_except_table985
- _AudioConverterReset
- _CFStringCreateWithCString
- _OBJC_IVAR_$__LTAudioDecoder._decoder
- _OBJC_IVAR_$__LTAudioDecoder._fromASBD
- _OBJC_IVAR_$__LTAudioDecoder._toASBD
- _OBJC_IVAR_$__LTDAssetModel._provider
- _OBJC_IVAR_$__LTDLanguageAssetCacheObserver._type
- _OBJC_IVAR_$__LTDMAAssetModel._identifier
- _OBJC_IVAR_$__LTDMAAssetModel._maAsset
- _OBJC_IVAR_$__LTDTTSAssetModel._ttsAsset
- _OBJC_METACLASS_$__LTAudioDecoder
- _VSCreate4CCString
- __DefaultRuneLocale
- __LTTranslationInternalErrorDomain
- __OBJC_$_CATEGORY_CLASS_METHODS_NSString_$_VS4CC
- __OBJC_$_CATEGORY_CLASS_METHODS_NSUserDefaults_$_TranslationDaemonAdditions
- __OBJC_$_CATEGORY_NSString_$_VS4CC
- __OBJC_$_CLASS_METHODS__LTAudioDecoder
- __OBJC_$_CLASS_PROP_LIST_NSUserDefaults_$_TranslationDaemonAdditions
- __OBJC_$_INSTANCE_METHODS_NSString(VS4CC|LTStatistics)
- __OBJC_$_INSTANCE_METHODS__LTAudioDecoder
- __OBJC_$_INSTANCE_VARIABLES__LTAudioDecoder
- __OBJC_CLASS_RO_$__LTAudioDecoder
- __OBJC_METACLASS_RO_$__LTAudioDecoder
- __ZN5apple4aiml12flatbuffers214DetachedBufferD2Ev
- __ZN5apple4aiml12flatbuffers215vector_downward12clear_bufferEv
- __ZNKSt3__112basic_stringIDsNS_11char_traitsIDsEENS_9allocatorIDsEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10AudioFrameEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10PronChoiceEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10TTSPromptsEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10TokenPronsEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb11AudioPacketEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb11TokenProns_17SanitizedSequenceEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12CategoryDataEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12FinishAudio_37ServerFeatureLatencyDistributionEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12ItnAlignmentEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12RepeatedSpanEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb13LmScorerTokenEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb13PronunciationEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14TTSReplacementEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14UserDataEntityEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14UserParametersEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14WordTimingInfoEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15AudioAnalytics_21AcousticFeaturesEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15AudioAnalytics_30SpeechRecognitionFeaturesEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15ChoiceAlignmentEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15NormalizedTokenEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15TTSWordPhonemesEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb16RecognitionTokenEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb17RecognitionChoiceEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb17TTSNormalizedTextEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb18LanguageParametersEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb18SanitizedPronTokenEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb18TTSPhonemeSequenceEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb19TextToSpeechRequestEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20ContextWithPronHintsEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20CorrectionsAlignmentEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20RecognitionCandidateEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20RepeatedItnAlignmentEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TextToSpeechRequest_16ContextInfoEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TranslationResponse_16TranslationTokenEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TranslationResponse_17TranslationPhraseEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb21RequestStatsResponse_10DoubleStatEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb21RequestStatsResponse_8BoolStatEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb21RequestStatsResponse_9Int32StatEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb21TranslationLocalePairEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb22NormalizedTokenVariantEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb23RecognitionPhraseTokensEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb23TextToSpeechCacheObjectEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24BatchTranslationRequest_9ParagraphEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24MTAlternativeDescriptionEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24TTSNeuralPhonemeSequenceEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb25BatchTranslationResponse_17TranslationPhraseEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb25BatchTranslationResponse_18TranslatedSentenceEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb25TextToSpeechVoiceResourceEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb26ShortcutFuzzyMatchRequest_15StringTokenPairEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb26TranslationPhraseMetaInfo_23AlternativeSelectedSpanEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb26TranslationPhraseMetaInfo_24AlternativeSelectedSpan_11AlternativeEEENS_9allocatorISB_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb26TranslationPhraseMetaInfo_24AlternativeSelectedSpan_5RangeEEENS_9allocatorISB_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb27LanguageDetectionPredictionEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb27ShortcutFuzzyMatchResponse_17ShortcutScorePairEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb27TextToSpeechRequestContext_16ContextInfoEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb28SpeechTranslationMtResponse_17TranslationPhraseEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb30FinalSpeechRecognitionResponseEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb33TextToSpeechSpeechFeatureRequest_12LexiconEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb34StartTextToSpeechStreamingRequest_16ContextInfoEntryEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb34TextToSpeechSpeechFeatureInputWordEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb35RecognitionPhraseTokensAlternativesEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb36PartialTextToSpeechStreamingResponseEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb37TextToSpeechSpeechFeatureInputPhonemeEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb38TextToSpeechSpeechFeatureOutputFeatureEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb38TranslationSupportedLanguagesResponse_12LanguagePairEEENS_9allocatorISA_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb4SpanEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb4WordEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb7KeywordEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb8VocTokenEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5apple4aiml12flatbuffers26OffsetINS3_6StringEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__112basic_stringIDsNS_11char_traitsIDsEENS_9allocatorIDsEEEC2B8ne190102EPKDsm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIDsEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10AudioFrameEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10PronChoiceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10TTSPromptsEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb10TokenPronsEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb11AudioPacketEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb11TokenProns_17SanitizedSequenceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12CategoryDataEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12FinishAudio_37ServerFeatureLatencyDistributionEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12ItnAlignmentEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb12RepeatedSpanEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb13LmScorerTokenEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb13PronunciationEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14TTSReplacementEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14UserDataEntityEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14UserParametersEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb14WordTimingInfoEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15AudioAnalytics_21AcousticFeaturesEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15AudioAnalytics_30SpeechRecognitionFeaturesEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15ChoiceAlignmentEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15NormalizedTokenEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb15TTSWordPhonemesEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb16RecognitionTokenEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb17RecognitionChoiceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb17TTSNormalizedTextEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb18LanguageParametersEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb18SanitizedPronTokenEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb18TTSPhonemeSequenceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb19TextToSpeechRequestEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20ContextWithPronHintsEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20CorrectionsAlignmentEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20RecognitionCandidateEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20RepeatedItnAlignmentEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TextToSpeechRequest_16ContextInfoEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TranslationResponse_16TranslationTokenEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb20TranslationResponse_17TranslationPhraseEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb21RequestStatsResponse_10DoubleStatEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb21RequestStatsResponse_8BoolStatEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb21RequestStatsResponse_9Int32StatEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb21TranslationLocalePairEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb22NormalizedTokenVariantEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb23RecognitionPhraseTokensEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb23TextToSpeechCacheObjectEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24BatchTranslationRequest_9ParagraphEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24MTAlternativeDescriptionEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb24TTSNeuralPhonemeSequenceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb25BatchTranslationResponse_17TranslationPhraseEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb25BatchTranslationResponse_18TranslatedSentenceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb25TextToSpeechVoiceResourceEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb26ShortcutFuzzyMatchRequest_15StringTokenPairEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb26TranslationPhraseMetaInfo_23AlternativeSelectedSpanEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb26TranslationPhraseMetaInfo_24AlternativeSelectedSpan_11AlternativeEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSG_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb26TranslationPhraseMetaInfo_24AlternativeSelectedSpan_5RangeEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSG_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb27LanguageDetectionPredictionEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb27ShortcutFuzzyMatchResponse_17ShortcutScorePairEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb27TextToSpeechRequestContext_16ContextInfoEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb28SpeechTranslationMtResponse_17TranslationPhraseEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb30FinalSpeechRecognitionResponseEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb33TextToSpeechSpeechFeatureRequest_12LexiconEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb34StartTextToSpeechStreamingRequest_16ContextInfoEntryEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb34TextToSpeechSpeechFeatureInputWordEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb35RecognitionPhraseTokensAlternativesEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb36PartialTextToSpeechStreamingResponseEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb37TextToSpeechSpeechFeatureInputPhonemeEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb38TextToSpeechSpeechFeatureOutputFeatureEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb38TranslationSupportedLanguagesResponse_12LanguagePairEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSF_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb4SpanEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb4WordEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb7KeywordEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetIN4siri6speech9schema_fb8VocTokenEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5apple4aiml12flatbuffers26OffsetINS4_6StringEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__16vectorItNS_9allocatorItEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorItNS_9allocatorItEEEC2B8ne190102Em
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___104+[_LTDLanguageAssetService startLanguageStatusSession:observationType:progress:observations:completion:]_block_invoke
- ___33+[_LTAudioDecoder sharedInstance]_block_invoke
- ___34-[_LTHotfixManager refreshHotfix:]_block_invoke.17
- ___34-[_LTHotfixManager refreshHotfix:]_block_invoke.17.cold.1
- ___37-[_LTTranslationServer _logStateSoon]_block_invoke.43
- ___40-[_LTAudioDecoder decodeChunk:outError:]_block_invoke
- ___40-[_LTAudioDecoder decodeChunk:outError:]_block_invoke.cold.1
- ___44-[_LTDLanguageAssetCache setRequiredAssets:]_block_invoke
- ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.63
- ___46+[_LTDAssetService configAssetWithCompletion:]_block_invoke.63.cold.1
- ___49-[_LTTranslationServer scheduleAssetCleanupWork:]_block_invoke.57
- ___51+[_LTDTTSAssetService ttsAssetForLocaleIdentifier:]_block_invoke
- ___55+[_LTDConfigurationService configurationForType:error:]_block_invoke
- ___55+[_LTDConfigurationService configurationForType:error:]_block_invoke.cold.1
- ___57+[_LTDAssetService refreshCatalogIfNeededWithCompletion:]_block_invoke.54
- ___59+[_LTDAssetService assetsForLocales:includeTTS:completion:]_block_invoke.92
- ___59-[_LTTranslationServer installedLocalesForTask:completion:]_block_invoke.50
- ___60+[_LTDLanguageAssetService _preheatMissingCacheStatesAfter:]_block_invoke.39
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.33
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.33.cold.1
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.33.cold.2
- ___62-[_LTTranslationServer speak:withContext:delegate:completion:]_block_invoke.33
- ___62-[_LTTranslationServer speak:withContext:delegate:completion:]_block_invoke.33.cold.1
- ___62-[_LTTranslationServer speak:withContext:delegate:completion:]_block_invoke.35
- ___64+[_LTDMAAssetService downloadAsset:options:progress:completion:]_block_invoke.326
- ___64+[_LTDMAAssetService downloadAsset:options:progress:completion:]_block_invoke_2.327
- ___65+[NSUserDefaults(TranslationDaemonAdditions) lt_appGroupDefaults]_block_invoke
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.41
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.42
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.45
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke.cold.2
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.46
- ___65+[_LTDTTSAssetService downloadAsset:options:progress:completion:]_block_invoke_2.46.cold.1
- ___65-[_LTOfflineTranslationEngine _waitForLIDWithContext:completion:]_block_invoke.64
- ___65-[_LTTranslationServer translateSentence:withContext:completion:]_block_invoke.21
- ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.20
- ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.25
- ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.25.cold.1
- ___66-[_LTSpeechRecognizer startRecognitionWithAutoStop:resultHandler:]_block_invoke
- ___67-[_LTMultilingualSpeechRecognizer initWithModelURLs:modelVersions:]_block_invoke
- ___67-[_LTTranslationServer startSpeechTranslationWithContext:delegate:]_block_invoke.39
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.23
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.27
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke.31
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.24
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.28
- ___74+[_LTDAssetService downloadAssets:forLocales:options:progress:completion:]_block_invoke_2.28.cold.1
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.112
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.89
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.90
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.96.cold.1
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.96.cold.2
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke_2.113
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke_2.92
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke_3
- ___76-[_LTClientConnection startLanguageStatusChangeObservation:type:completion:]_block_invoke
- ___76-[_LTClientConnection startLanguageStatusChangeObservation:type:completion:]_block_invoke_2
- ___78-[_LTTranslationServer startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.31
- ___80-[_LTOfflineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.61
- ___80-[_LTOfflineTranslationEngine translate:withContext:paragraphResult:completion:]_block_invoke.61.cold.1
- ___82-[_LTOfflineTranslationEngine _handleTranslationResults:withContext:sourceString:]_block_invoke
- ___83-[_LTTranslationServer translateParagraphs:withContext:paragraphResult:completion:]_block_invoke.23
- ___83-[_LTTranslationServer translateParagraphs:withContext:paragraphResult:completion:]_block_invoke.23.cold.1
- ___85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.71
- ___85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.71.cold.1
- ___88-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:resultHandler:]_block_invoke
- ___88-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:resultHandler:]_block_invoke.4
- ___88-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:resultHandler:]_block_invoke.6
- ___88-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:resultHandler:]_block_invoke.7
- ___88-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:resultHandler:]_block_invoke.9
- ___88-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:resultHandler:]_block_invoke.9.cold.1
- ___88-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:resultHandler:]_block_invoke.cold.1
- ___88-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:resultHandler:]_block_invoke.cold.2
- ___88-[_LTMultilingualSpeechRecognizer startRecognitionForLocale:autoEndpoint:resultHandler:]_block_invoke.cold.3
- ___98-[_LTOfflineTranslationEngine _translateString:isFinal:withContext:toLocale:withSpans:completion:]_block_invoke
- ___98-[_LTOfflineTranslationEngine _translateString:isFinal:withContext:toLocale:withSpans:completion:]_block_invoke.26
- ___block_descriptor_104_ea8_32s40s48s56s64s72s80bs88w_e17_v16?0"NSArray"8lw88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_112_e8_32s40s48s56s64s72s80bs88r96r_e48_v24?0"_LTSpeechRecognitionResult"8"NSError"16lr88l8s32l8s40l8s48l8s80l8s56l8s64l8s72l8r96l8
- ___block_descriptor_32_e61_"_LTLanguageStatusObservation"16?0"_LTLanguageAssetModel"8l
- ___block_descriptor_32_e68_"_LTLanguageStatusObservation"16?0"_LTLanguageStatusObservation"8l
- ___block_descriptor_40_e20_v20?0B8"NSError"12l
- ___block_descriptor_48_e8_32s40s_e32_v32?0"NSLocale"8"NSURL"16^B24ls32l8s40l8
- ___block_descriptor_48_ea8_32s40s_e30_v16?0"_LTTranslationResult"8ls32l8s40l8
- ___block_descriptor_49_e8_32bs40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_56_e8_32s40s_e18_v16?0"TTSAsset"8ls32l8s40l8
- ___block_descriptor_64_e8_32s40r48r_e86_i32?0^I8^{AudioBufferList=I[1{AudioBuffer=II^v}]}16^^{AudioStreamPacketDescription}24lr40l8s32l8r48l8
- ___block_descriptor_64_e8_32s40s48bs_e18_v16?0"TTSAsset"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs_e32_v16?0"MAProgressNotification"8ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56bs_e14_v32?0d8q16q24ls32l8s56l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_descriptor_80_e8_32s40s48bs56bs_e29_v24?0"NSArray"8"NSError"16ls48l8s32l8s40l8s56l8
- ___block_descriptor_80_e8_32s40s48s56bs64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_88_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
- ___block_descriptor_96_e8_32s40s48s56s64s72r80r_e5_v8?0ls32l8s40l8r72l8s48l8s56l8r80l8s64l8
- ___block_descriptor_96_ea8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_literal_global.23
- ___block_literal_global.30
- ___block_literal_global.39
- ___block_literal_global.43
- ___block_literal_global.48
- ___block_literal_global.53
- ___block_literal_global.65
- ___block_literal_global.71
- ___maskrune
- _lt_appGroupDefaults.appGroupDefaults
- _lt_appGroupDefaults.onceToken
- _objc_msgSend$_audioDecoderFrom:to:
- _objc_msgSend$_availableTTSAssets
- _objc_msgSend$_availableTTSAssetsByLanguage
- _objc_msgSend$_handleTranslationResults:withContext:sourceString:
- _objc_msgSend$_initWithSuiteName:container:
- _objc_msgSend$_loadEtiquetteSanitizers
- _objc_msgSend$_pairNamesForLocales:
- _objc_msgSend$_translateString:isFinal:withContext:toLocale:withSpans:completion:
- _objc_msgSend$_ttsAssetForLanguage:name:gender:
- _objc_msgSend$beginChunkDecoderForStreamDescription:
- _objc_msgSend$bestAssetOfTypes:matching:
- _objc_msgSend$containerURLForSecurityApplicationGroupIdentifier:
- _objc_msgSend$customVoice
- _objc_msgSend$decodeChunk:outError:
- _objc_msgSend$endChunkDecoding
- _objc_msgSend$initWithConfiguration:overrideConfigFiles:generalVoc:lexiconEnh:itnEnh:
- _objc_msgSend$initWithID:type:progress:observations:completion:
- _objc_msgSend$initWithLength:
- _objc_msgSend$initWithLocale:progress:status:
- _objc_msgSend$initWithLocalePair:assetInfo:selfLoggingManager:
- _objc_msgSend$initWithMAAsset:
- _objc_msgSend$initWithModelURL:language:modelVersion:
- _objc_msgSend$initWithModelURLs:modelVersions:
- _objc_msgSend$initWithPackage:locale:modelVersion:isFinal:
- _objc_msgSend$initWithResult:locale:modelVersion:isFinal:
- _objc_msgSend$initWithScorer:
- _objc_msgSend$isCompleteBidirectionalModel
- _objc_msgSend$isCompletePassthroughModel
- _objc_msgSend$languageStatusChangedForType:progress:observations:
- _objc_msgSend$maAsset
- _objc_msgSend$modelFromAsset:
- _objc_msgSend$preflightCheckForLocalePair:withModelURLs:
- _objc_msgSend$resultWithPackage:locale:modelVersion:isFinal:
- _objc_msgSend$resultWithResult:locale:modelVersion:isFinal:
- _objc_msgSend$setRequiredAssets:
- _objc_msgSend$setSubscribedVoices:
- _objc_msgSend$speechModelURLForLocale:
- _objc_msgSend$speechTranslationAssetInfoForLocalePair:error:
- _objc_msgSend$startLanguageStatusSession:observationType:progress:observations:completion:
- _objc_msgSend$startRecognitionForLocale:autoEndpoint:resultHandler:
- _objc_msgSend$startRecognitionWithAutoStop:resultHandler:
- _objc_msgSend$syncInstalledLocales
- _objc_msgSend$translateTokens:isFinal:spans:completion:
- _objc_msgSend$ttsAsset
- _objc_msgSend$vs_stringFrom4CC:
- _objc_msgSend$weightedLocale
- _sharedInstance.sSharedInstance
- _snprintf
CStrings:
+ "%@"
+ "%@.%@.%@"
+ "%@.%@.%@.%@"
+ "%@.%@.%@.%@.%@"
+ "-partial-"
+ "."
+ "<%@ %@, %@>"
+ "@\"<_LTObservationFilteringConditions>\""
+ "@\"EMTStablePrefixState\""
+ "@\"NSSet\"24@0:8q16"
+ "@\"NSString\"16@?0@\"NSString\"8"
+ "@\"SFEntitledAssetConfig\""
+ "@\"UAFAsset\""
+ "@\"_LTAlignment\"16@?0@\"EMTProjection\"8"
+ "@\"_LTDAssetModel\"16@?0@\"_LTDUAFAssetModel\"8"
+ "@24@0:8@\"NSString\"16"
+ "@32@0:8Q16@24"
+ "@48@0:8@16@24@32q40"
+ "@48@0:8@16q24@32@40"
+ "@52@0:8@16@24@32q40B48"
+ "@52@0:8@16q24B32@?36@?44"
+ "@56@0:8@16@24@32q40B48B52"
+ "@76@0:8@16@24d32B40@44@52@60@68"
+ "ASR asset service unsupported asset type"
+ "ASR failed to download asset %{public}@: %@"
+ "Add missing subscripton for %{public}@"
+ "Adding Barrier Pending Streaming Speech Result: %p"
+ "Asset download %{public}@ complete"
+ "Asset download %{public}@ failure %@"
+ "Asset download failed with error %@"
+ "Asset download for UAF asset %@ failed with error %@"
+ "Asset identifier does not contain sufficient components: %@ has %zu components"
+ "Asset model is not a UAF asset mode, abort purge"
+ "Asset model is not a UAF asset model, abort download"
+ "Asset purge completed with error %@"
+ "Asset purge failed with error %@"
+ "Asset service resolution failure for %@"
+ "Asset subscription %{public}@ failure %@"
+ "Asset subscription for UAF asset model failed"
+ "B16@?0@\"<_LTDAssetModelProtocol>\"8"
+ "B16@?0@\"NSString\"8"
+ "B16@?0@\"_LTLanguageStatusObservation\"8"
+ "B24@0:8@\"NSLocale\"16"
+ "B32@?0@\"<_LTDAssetModelProtocol>\"8Q16^B24"
+ "B44@0:8@16@24@32B40"
+ "Cache is nil during OVAD state change"
+ "Can't get speech asset info for pair %{public}@ because we don't have a complete bi-directional model: %@ taksHint: %@"
+ "Cannot initialize a LTDASRAssetModel using a non-ASR identifier: %{public}@"
+ "Cannot locate a TTSAsset for identifier: %{public}@"
+ "Changed segments for state %p from %{sensitive}@ to %{sensitive}@"
+ "Clear Pending Streaming Speech Results. Count: %lu"
+ "Configuration bundle is not installed"
+ "Confirmed download %zd / %zd: %{public}@"
+ "Confirmed download of %zd assets, running symlink validation"
+ "Confirming download of %zd assets"
+ "Connection application-identifier: %{public}@"
+ "Could not determine the Siri voice for asset: %@"
+ "Created a new EMTStablePrefixState %{public}p"
+ "Created new offline engine for locales: %{public}@, with taskHint: %{public}@"
+ "Creating alignment from range (%zul, %zul) in text \"%{sensitive}@\" with substring \"%{sensitive}@\""
+ "Creating multi recognizer: got sourceModelURL %{BOOL}i got targetModelURL %{BOOL}i %{private}@, %{private}@, %{public}@"
+ "DefaultAssetType"
+ "Deferring symlink validation to cleanupScheduler: %{public}@"
+ "Deliver Stashed Streaming Speech Result: %p"
+ "Deliver Streaming Speech Result: %p"
+ "Detected MA catalog but default provider is UAF."
+ "Detection result via weighted locale: %{public}@, however there are low-confidence locales: %{public}@"
+ "Did not find phrasebook link in symlink directory for %{public}@"
+ "Did not find quasar config in symlink directory for %{public}@"
+ "Did not find required top-level symlinks for %{public}@"
+ "Did not find translation model folder in symlink directory for %{public}@"
+ "Don't have a cleanupScheduler, directly doing work to validate symlinks"
+ "Download of asset completed %{public}@: %{public}@"
+ "Download of asset required: %{public}@"
+ "Download of component asset failed %{public}@: %{public}@"
+ "EMTProjection"
+ "Failed to map language %{public}@"
+ "Failed to match preferred locale for current locale %{public}@"
+ "Failed to obtain asset configuration"
+ "Failed to read current locale"
+ "Failed to read recommended locales for device locale %{public}@"
+ "Hotfix asset preflight from %{public}@ failure: %@"
+ "Ignoring OVAD signal because it's the same"
+ "Incomplete speech translation model for %@ taksHint: %@"
+ "Initializing _LTDStreamStabilizer with state %p and segments %{public}@"
+ "Invalid attempt to add LTDAssetModel as a component"
+ "Invalid attempt to add a different asset type as a component"
+ "Invalid attempt to add a duplicate asset as a component"
+ "LTASRModels"
+ "LTASRTask"
+ "LTASRTasks"
+ "LTMTCustomModel"
+ "LTOvadEnabled"
+ "LTOverrides"
+ "Nil asset model created for asset provider: %{public}@"
+ "Nil asset model created for asset specifier: %{public}@"
+ "No asset info found for pair %{public}@, taskHint: %{public}@"
+ "No asset provider defined for asset type: %{public}@"
+ "No asset specifier found for subscribed asset: %{public}@"
+ "Not attempting to create combined disambiguation result because the client didn't request gender disambiguation"
+ "OVAD assuming pending final translation for source: %@"
+ "OVAD cancelling own voice pending swap and restart timer"
+ "OVAD did finish while in pending locale swap and restart case for source: %@"
+ "OVAD forcing pending swap and restart"
+ "OVAD own voice pending swap and restart timer fired"
+ "OVAD received pending final translation for source: %@"
+ "OVAD speech recognized waiting for pending final translation: %@"
+ "OVAD streaming state changed to %{bool}i. _ownVoiceIsActive: %@, _pendingFinalTranslation: %@, _pendingSwapAndRestart: %@"
+ "OVAD transitioning to pending locale swap and restart state for source: %@"
+ "OVAD updating own voice pending swap and restart timer"
+ "Offline translation using custom model URLs: %{public}@"
+ "Preferred offline engine not available, using online"
+ "Q24@0:8q16"
+ "Received %lu stableSegments %{sensitive}@ with stablePrefixState %{public}p"
+ "Remove ophaned subscripton for %@"
+ "Removing Barrier Streaming Speech Result: %p"
+ "Reseting current EMTStablePrefixState %{public}p"
+ "Resetting stabilization state from %p -> %p; clearing old segments: %{sensitive}@"
+ "Retaining stabilization info for streaming"
+ "Reusing cached offline engine for locales: %{public}@, with taskHint: %{public}@"
+ "SiriTTS failed to locate TTS assets for identifier %{public}@"
+ "Skipping symlink directiory creation, found necessary symlinks on disk for %{public}@"
+ "Stabilization"
+ "Starting recognition with locale %{public}@, recognizers: %{public}@"
+ "Stashing Pending Streaming Speech Result: %p"
+ "Subscribing to voice: %@"
+ "SupportedLocales"
+ "Symlinks were modified"
+ "Symlinks were not modified"
+ "T@\"<_LTDAssetModelProtocol>\",&,N"
+ "T@\"<_LTObservationFilteringConditions>\",W,N,V_observationFilterConditions"
+ "T@\"EMTStablePrefixState\",R,N"
+ "T@\"MAAsset\",&,N,V_provider"
+ "T@\"NSArray\",R,C"
+ "T@\"NSArray\",R,N,V_components"
+ "T@\"NSDictionary\",R,&,N,V_assetUsages"
+ "T@\"NSLocale\",&,N,V_currentLocale"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_ownVoicePendingSwapAndRestartTimer"
+ "T@\"NSString\",&,N,V_assetName"
+ "T@\"SFEntitledAssetConfig\",&,N,V_provider"
+ "T@\"TTSAsset\",&,N,V_provider"
+ "T@\"UAFAsset\",&,N,V_provider"
+ "T@,R,N"
+ "TB,N,V_enableMultiFieldInput"
+ "TaskHint"
+ "Throttle concurrent downloads to %zd"
+ "Tq,R,N,V_taskHint"
+ "UAF asset download failure due to lack of space"
+ "UAF asset download failure due to network"
+ "UAF asset registration for %{public}@"
+ "UAF asset update event"
+ "Unexpectedly got nil result from offline engine"
+ "Unexpectedly got target span with identifier '%{public}@' that doesn't correspond to any source span identifier; ignoring span"
+ "Unexpectedly trying to look up stabilization helper without specifying a sessionID"
+ "Using model task name %{private}@"
+ "_LTDASRAssetModel"
+ "_LTDASRAssetService"
+ "_LTDStreamStabilizer"
+ "_LTDUAFAssetModel"
+ "_LTDUAFBridge"
+ "_LTObservationFilteringConditions"
+ "_addComponentAsset:"
+ "_addSyntheticASREntriesToAssets:"
+ "_allAssetLocales"
+ "_allAssetSpecifiers"
+ "_allAssetSpecifiersByLocaleId"
+ "_allTTSAssets"
+ "_assetLanguage"
+ "_assetProviderForAssetType:"
+ "_assetStateForOfflineState:"
+ "_assetSubtype"
+ "_assetTypesFoDevice"
+ "_assetURL"
+ "_assetUsages"
+ "_awaitDownloadForAsset:"
+ "_catalog"
+ "_components"
+ "_concatenatedAlignmentsFromSentences:"
+ "_configBundleURL"
+ "_createSymlinkDirectoryForLocalePair:assets:configAsset:validateIfNeeded:"
+ "_currentLocale"
+ "_defaultAssetType"
+ "_downloadAsset:progress:completion:"
+ "_enableMultiFieldInput"
+ "_enableStreamingSpeechTranslation"
+ "_errorFor:message:"
+ "_errorForAssetProviderResolutionForAssetType:"
+ "_handleTranslationResults:withContext:sourceString:sourceSpans:stabilizer:"
+ "_languageStatusSessionID"
+ "_loadEtiquetteSanitizersForTaskHint:"
+ "_localeRanks"
+ "_mapIdentifierForSiriTTS:"
+ "_observationFilterConditions"
+ "_offlineStateForAssetState:"
+ "_originalLocalePair"
+ "_ownVoiceIsActive"
+ "_ownVoicePendingSwapAndRestartTimer"
+ "_pendingFinalTranslation"
+ "_pendingStreamingSpeechResults"
+ "_pendingSwapAndRestart"
+ "_prepareStabilizerForContext:"
+ "_purgeAsset:completion:"
+ "_registerChangeHandler:"
+ "_registerForAsset:progress:completion:"
+ "_requiredAssetSpecifiers"
+ "_selectedLocales"
+ "_sfInstalledLTIdentifiersForTaskHint:filter:completion:"
+ "_sfSupportedLTIdentifiersForTaskHint:filter:completion:"
+ "_sfTaskHintForLTTaskHint:"
+ "_speechRequestStablePrefixState"
+ "_stabilizationState"
+ "_stabilizerMap"
+ "_stableSegments"
+ "_subscribe:completion:"
+ "_subscribeToVoice:"
+ "_subscribedAssetSpecifiers"
+ "_subscriptions"
+ "_supportedIdentifiersWithCommpletion:"
+ "_taskHintForLTAssetType:"
+ "_taskHintMap"
+ "_translateString:isFinal:withContext:toLocale:withSpans:stabilizer:completion:"
+ "_unsubscribe:completion:"
+ "_updateOVADStreamingState_onQueue:"
+ "_validTopLevelSymlinkDirectory:configAssetURL:assets:"
+ "a"
+ "addComponentAsset:"
+ "alignments"
+ "append:"
+ "arrayWithObject:"
+ "asr"
+ "asr.language"
+ "asrAssetWithIdentifier:taskHint:"
+ "assetIdentifierForAssetSpecifier:"
+ "assetSpecifierForAssetIdentifier:"
+ "assetSpecifierForAssetUsages:"
+ "assetSpecifiersForAssetType:locale:"
+ "assetSubtype"
+ "assetTypeForAssetSpecifier:"
+ "assetTypeForAssetUsage:"
+ "assetTypeForTaskHint:localeIdentifier:"
+ "assetTypesForLocaleIdentifier:"
+ "assetUsageValuesForAssetType:"
+ "assetUsages"
+ "assetUsagesForAssetSpecifier:"
+ "assetUsagesForAssetType:"
+ "assetUsagesForAssetType:locale:"
+ "asset_services_general_asr"
+ "asset_services_ngasr"
+ "availableAssetsWithCompletion:"
+ "availableIdentifiers"
+ "begin"
+ "cancelOwnVoicePendingSwapAndRestartTimer"
+ "characterSetWithCharactersInString:"
+ "com.apple.MobileAsset.SpeechTranslationAssets"
+ "com.apple.MobileAsset.UAF.Siri.Understanding"
+ "com.apple.MobileAsset.UAF.Speech.AutomaticSpeechRecognition"
+ "com.apple.MobileAsset.UAF.Translation.Assets"
+ "com.apple.sequoia.asset"
+ "com.apple.sequoia.asset.config"
+ "com.apple.translationd.ASRAssetService"
+ "com.apple.translationd.UAFAssetService"
+ "com.apple.translationd.asr"
+ "com.apple.translationd.uaf"
+ "completedBytes"
+ "components"
+ "dataWithLength:"
+ "de_DE"
+ "dictionaryForKey:"
+ "disambiguableResult"
+ "discreteProgressWithIdentifier:offlineState:"
+ "downloadStatus"
+ "downloadStatusForSubscriber:subscriptionName:"
+ "en_GB"
+ "en_IN"
+ "en_US"
+ "enableMultiFieldInput"
+ "enableOfflineStreamStabilizer"
+ "enableStreamingSpeechTranslation"
+ "enableTranslationSemanticSegmentation"
+ "end"
+ "endOfUtterance"
+ "es_ES"
+ "false"
+ "fetchAssetWithConfig:clientIdentifier:progress:completion:"
+ "forcePendingSwapAndRestart"
+ "fr_FR"
+ "generateSilentAudioDataWithDuration:"
+ "getLocalFileUrlForTaskHint:"
+ "initWithAssetSpecifier:"
+ "initWithConfiguration:overrides:overrideConfigFiles:generalVoc:lexiconEnh:itnEnh:"
+ "initWithConfiguration:useQuasarFormatter:overrides:"
+ "initWithFormattedString:sanitizedFormattedString:confidence:lowConfidence:romanization:tokens:preToPostITN:stableString:"
+ "initWithID:taskHint:progress:observations:completion:"
+ "initWithLanguage:taskHint:"
+ "initWithLocale:progress:downloadSize:status:rank:"
+ "initWithLocalePair:taskHint:assetInfo:selfLoggingManager:"
+ "initWithModelURL:language:modelVersion:taskHint:"
+ "initWithModelURLs:modelVersions:taskHint:"
+ "initWithName:assetSets:usageAliases:expires:"
+ "initWithOutput:stableSegments:"
+ "initWithPackage:locale:modelVersion:taskHint:isFinal:endOfUtterance:"
+ "initWithResult:locale:modelVersion:taskHint:isFinal:"
+ "initWithScorer:lowConfidenceLocales:strategy:"
+ "initWithText:sourceText:locale:isFinal:sourceIdentifier:"
+ "insertObject:atIndex:"
+ "installedLanguagesForTaskHint:completion:"
+ "instancesRespondToSelector:"
+ "isASRModelSupportingTaskHint:"
+ "isCompleteBidirectionalModelForTaskHint:"
+ "isCompletePassthroughModelForTaskHint:"
+ "isGeneralASRSupportedOnDevice"
+ "isSupportedTaskHint:"
+ "it_IT"
+ "ja_JP"
+ "knownUsagesForAssetSet:usageType:"
+ "ko_KR"
+ "languageStatusChangedForTaskHint:progress:observations:"
+ "lid"
+ "location"
+ "lt_asrModels"
+ "lt_asrTask"
+ "lt_asrTasks"
+ "lt_firstObjectPassingTest:"
+ "lt_mtCustomModel"
+ "lt_ovadEnabled"
+ "lt_overrides"
+ "lt_stringArrayDebugDescription:"
+ "ltd_invalidResultError"
+ "managedAssetProvider"
+ "messages"
+ "messaging"
+ "minusSet:"
+ "mt"
+ "mt.capability"
+ "mt.family"
+ "mt.language"
+ "neural"
+ "not set"
+ "notify:ofObservations:"
+ "observationFilterConditions"
+ "observeAssetSet:queue:handler:"
+ "ownVoicePendingSwapAndRestartTimer"
+ "pairNamesForLocaleIdentifiers:"
+ "pairNamesForLocales:"
+ "pathToAssetWithConfig:clientIdentifier:"
+ "pb"
+ "pb.language"
+ "primaryLanguage"
+ "pt_BR"
+ "q24@0:8q16"
+ "removeObjectsInRange:"
+ "resultWithPackage:locale:modelVersion:taskHint:isFinal:"
+ "resultWithPackage:locale:modelVersion:taskHint:isFinal:endOfUtterance:"
+ "resultWithResult:locale:modelVersion:taskHint:isFinal:"
+ "retrieveAssetSet:usages:"
+ "reverseObjectEnumerator"
+ "setAssetName:"
+ "setAssetPath:"
+ "setAssetSubtype:"
+ "setCurrentLocale:"
+ "setEnableMultiFieldInput:"
+ "setEndOfUtterance:"
+ "setHotfixURL:"
+ "setInitialObservationsForIdentifiers:"
+ "setObservationFilterConditions:"
+ "setOwnVoicePendingSwapAndRestartTimer:"
+ "setRequiredAssets:localeRanks:"
+ "setStablePrefixState:"
+ "setStableSegments:"
+ "setStableString:"
+ "setWithObject:"
+ "sharedManager"
+ "sourceIdentifier"
+ "speechModelURLForLocale:taskHint:"
+ "speechRecognizer:didProduceLoggableMultiUserPackages:"
+ "speechRecognizer:didRecognizeFinalResultMultiUserPackages:"
+ "speechTranslationAssetInfoForLocalePair:taskHint:error:"
+ "stabilizationState"
+ "stabilizationStreaming"
+ "stablePrefixState"
+ "stableSegments"
+ "startLanguageStatusChangeObservation:taskHint:completion:"
+ "startLanguageStatusSession:taskHint:progress:observations:completion:"
+ "startRecognitionForLocale:autoEndpoint:enableStreamingSpeechTranslation:enableMultiFieldInput:resultHandler:"
+ "startRecognitionWithAutoStop:enableStreamingSpeechTranslation:resultHandler:"
+ "stateForAsset:"
+ "stringForKey:"
+ "subscribe:subscriptions:queue:completion:"
+ "subscriptionsForSubscriber:"
+ "successfully"
+ "supportedIdentifiersForTask:completion:"
+ "supportedLanguagesForTaskHint:"
+ "supportedLanguagesForTaskHint:completion:"
+ "supportedLocaleIdentifiersForTaskHint:"
+ "supportedLocalesSubsetForTask:"
+ "supportsTaskHint:"
+ "swapLocalesAndRestart"
+ "swapLocalesAndRestartWithStateResetAndLogMessage:"
+ "targetProjections"
+ "targetText"
+ "technology"
+ "totalBytes"
+ "translateStreamingInput:context:stabilizer:completion:"
+ "translateStreamingInput:withContext:completion:"
+ "true"
+ "uafCatalog"
+ "uk"
+ "unsubscribe:subscriptionNames:queue:completion:"
+ "unsubscribeFromAssetWithConfig:clientIdentifier:completion:"
+ "updateAlignmentWithSourceSpans:offlineTargetSpans:"
+ "updateAssetsForSubscriber:subscriptionName:policies:queue:detailedProgress:completion:"
+ "updateOVADStreamingState:"
+ "updateOwnVoicePendingSwapAndRestartTimer"
+ "updatePercentComplete:"
+ "v16@?0@\"<_LTDAssetModelProtocol>\"8"
+ "v16@?0@\"NSSet\"8"
+ "v16@?0@\"UAFAssetSetStatus\"8"
+ "v16@?0@\"_LTDUAFAssetModel\"8"
+ "v24@0:8@\"NSNumber\"16"
+ "v24@?0@\"<_LTDAssetModelProtocol>\"8@\"NSError\"16"
+ "v24@?0@\"NSSet\"8@\"NSError\"16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v24@?0@\"_LTDASRAssetModel\"8@\"NSError\"16"
+ "v24@?0@\"_LTStabilizationTranslationResult\"8@\"NSError\"16"
+ "v32@0:8@\"<_LTDAssetModelProtocol>\"16@?<v@?@\"<_LTDAssetModelProtocol>\"@\"NSError\">24"
+ "v32@0:8@\"_EARSpeechRecognizer\"16@\"NSDictionary\"24"
+ "v32@0:8B16B20@?24"
+ "v36@0:8q16B24@\"NSArray\"28"
+ "v36@0:8q16B24@28"
+ "v40@0:8@\"NSUUID\"16q24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"_LTStreamingInput\"16@\"_LTTranslationContext\"24@?<v@?@\"_LTStabilizationTranslationResult\"@\"NSError\">32"
+ "v40@0:8@16q24@?32"
+ "v44@0:8@16B24B28B32@?36"
+ "v48@0:8@\"<_LTDAssetModelProtocol>\"16Q24@?<v@?@\"<_LTDAssetModelProtocol>\">32@?<v@?@\"NSError\">40"
+ "v48@0:8@\"_LTStreamingInput\"16@\"_LTTranslationContext\"24@\"_LTDStreamStabilizer\"32@?<v@?@\"_LTStabilizationTranslationResult\"@\"NSError\">40"
+ "v52@0:8@16q24B32@?36@?44"
+ "v68@0:8@16B24@28@36@44@52@?60"
+ "weight"
+ "weightedLocale for messages is %{public}@ with count %f on %zd words from %zu locales"
+ "weightedLocaleWithStrategy:"
+ "zh_CN"
+ "\x81"
- "\f"
- "%d"
- "0x%x"
- "@\"NSObject<_LTDAssetModelProtocol>\""
- "@112@0:8@16{AudioStreamBasicDescription=dIIIIIIII}24{AudioStreamBasicDescription=dIIIIIIII}64^@104"
- "@20@0:8i16"
- "@52@0:8@16Q24B32@?36@?44"
- "@56@0:8{AudioStreamBasicDescription=dIIIIIIII}16"
- "@72@0:8@16{AudioStreamBasicDescription=dIIIIIIII}24^@64"
- "Asset download and symlink creation completed"
- "Asset on disk quasar symlink not found for %{public}@"
- "Can't get speech asset info for pair %{public}@ because we don't have a complete bi-directional model: %@"
- "Client connection for: %{public}@"
- "Client didn't set application-identifier entitlement"
- "Complete download %zd of %zd: %{public}@"
- "Config source URL for type: %{public}@ lookup failure: %@"
- "Could not create Opus decoder: %{public}@"
- "Could not finish decoding, res %@"
- "Creating multi recognizer: %{private}@, %{private}@"
- "Deferring symlink creation to cleanupScheduler: %{public}@"
- "Disambiguation: Offline engine doesn't have EMTTranslationOptions on current device, translating with legacy method, and not setting enableDisambiguationAlternatives"
- "Don't have a cleanupScheduler, directly doing work to create symlinks"
- "Download of %zd assets complete, running symlink creation"
- "Download of already installed asset requested: %{public}@"
- "Download of asset requested: %{public}@"
- "EMTTranslationOptions"
- "Empty packet descriptions, cannot extract data chunks"
- "Enqueue download %zd of %zd: %{public}@"
- "Failed  initialize a LTDTTSAssetModel for %{public}@ via LT identifier: %{public}@"
- "Failed to create opus decoder"
- "Failed to read asset configuration: %@"
- "Failed to refresh asset catalog %@"
- "Incomplete speech translation model for %@"
- "Initializing LTDTTSAssetModel with: ttsIdentifier %@ | _ltIdentifier %@ | _language %@"
- "Installed config asset is already current version %zd"
- "No asset info found for pair %{public}@"
- "Offline translation preflight failed"
- "Only expecting to get 1 packet at a time, not %lu"
- "Reusing cached offline engine for locales: %{public}@"
- "SiriTTS available assets: %{public}@"
- "SiriTTS candidates for locale %{public}@ are: %{public}@"
- "SiriTTS failed to locate TTS assets for language prefix %{public}@"
- "SiriTTS found candidate %{public}@ for locale: %{public}@"
- "SiriTTS installed assets: %{public}@"
- "Skipping symlink directory creation, found quasar symlink on disk for %{public}@"
- "Starting download of %zd assets"
- "T@\"MAAsset\",&,N,V_maAsset"
- "T@\"NSObject<_LTDAssetModelProtocol>\",&,N,V_provider"
- "T@\"NSURL\",R,N,V_hotfixURL"
- "T@\"NSUserDefaults\",R,N"
- "T@\"TTSAsset\",R,&,N,V_ttsAsset"
- "TQ,R,N,V_type"
- "Throttle downloads to %zd concurrent requests"
- "VS4CC"
- "^{OpaqueAudioConverter=}96@0:8{AudioStreamBasicDescription=dIIIIIIII}16{AudioStreamBasicDescription=dIIIIIIII}56"
- "_LTAudioDecoder"
- "_audioDecoderFrom:to:"
- "_availableTTSAssets"
- "_availableTTSAssetsByLanguage"
- "_decoder"
- "_fromASBD"
- "_handleTranslationResults:withContext:sourceString:"
- "_initWithSuiteName:container:"
- "_loadEtiquetteSanitizers"
- "_maAsset"
- "_pairNamesForLocales:"
- "_toASBD"
- "_translateString:isFinal:withContext:toLocale:withSpans:completion:"
- "_ttsAsset"
- "_ttsAssetForLanguage:name:gender:"
- "_type"
- "assetTypeForAssetIdentifier:"
- "beginChunkDecoderForStreamDescription:"
- "bestAssetOfTypes:matching:"
- "com.apple.MobileAsset.Speech"
- "containerURLForSecurityApplicationGroupIdentifier:"
- "customVoice"
- "decodeChunk:outError:"
- "decoder gave us %d bytes bytes but we really only expected %d"
- "endChunkDecoding"
- "group.com.apple.private.translation"
- "initWithConfiguration:overrideConfigFiles:generalVoc:lexiconEnh:itnEnh:"
- "initWithID:type:progress:observations:completion:"
- "initWithLength:"
- "initWithLocale:progress:status:"
- "initWithLocalePair:assetInfo:selfLoggingManager:"
- "initWithMAAsset:"
- "initWithModelURL:language:modelVersion:"
- "initWithModelURLs:modelVersions:"
- "initWithPackage:locale:modelVersion:isFinal:"
- "initWithResult:locale:modelVersion:isFinal:"
- "initWithScorer:"
- "installedAssetIdentifiers"
- "isCompleteBidirectionalModel"
- "isCompletePassthroughModel"
- "languageStatusChangedForType:progress:observations:"
- "maAsset"
- "resultWithPackage:locale:modelVersion:isFinal:"
- "resultWithResult:locale:modelVersion:isFinal:"
- "setAutoDownloadedAssets:"
- "setMaAsset:"
- "setRequiredAssets:"
- "speechModelURLForLocale:"
- "speechTranslationAssetInfoForLocalePair:error:"
- "startLanguageStatusChangeObservation:type:completion:"
- "startLanguageStatusSession:observationType:progress:observations:completion:"
- "startRecognitionForLocale:autoEndpoint:resultHandler:"
- "startRecognitionWithAutoStop:resultHandler:"
- "translateTokens:isFinal:spans:completion:"
- "ttsAsset"
- "v32@0:8@\"_LTDAssetModel\"16@?<v@?@\"_LTDAssetModel\"@\"NSError\">24"
- "v36@0:8Q16B24@\"NSArray\"28"
- "v36@0:8Q16B24@28"
- "v40@0:8@\"NSUUID\"16Q24@?<v@?@\"NSError\">32"
- "v48@0:8@\"_LTDAssetModel\"16Q24@?<v@?@\"_LTDAssetModel\">32@?<v@?@\"NSError\">40"
- "v52@0:8@16Q24B32@?36@?44"
- "v60@0:8@16B24@28@36@44@?52"
- "vs_stringFrom4CC:"

```
