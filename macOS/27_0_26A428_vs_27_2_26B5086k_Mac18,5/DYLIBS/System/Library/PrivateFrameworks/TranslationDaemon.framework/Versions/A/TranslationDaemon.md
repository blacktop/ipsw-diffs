## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/Versions/A/TranslationDaemon`

```diff

-389.0.0.0.0
-  __TEXT.__text: 0x1ae57c
-  __TEXT.__objc_methlist: 0x1a390
-  __TEXT.__const: 0xad0
-  __TEXT.__gcc_except_tab: 0x1b3e8
-  __TEXT.__cstring: 0x647b
-  __TEXT.__oslogstring: 0xda70
+393.1.0.0.0
+  __TEXT.__text: 0x1b1d08
+  __TEXT.__objc_methlist: 0x1a5b0
+  __TEXT.__const: 0x9e0
+  __TEXT.__gcc_except_tab: 0x1b558
+  __TEXT.__cstring: 0x64cb
+  __TEXT.__oslogstring: 0xde2a
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__swift5_typeref: 0x381
   __TEXT.__swift5_capture: 0xe0
-  __TEXT.__constg_swiftt: 0x154
+  __TEXT.__constg_swiftt: 0x104
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x90
-  __TEXT.__swift5_fieldmd: 0xf8
+  __TEXT.__swift5_reflstr: 0x8e
+  __TEXT.__swift5_fieldmd: 0xcc
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_proto: 0x40
-  __TEXT.__swift5_types: 0x1c
+  __TEXT.__swift5_proto: 0x34
+  __TEXT.__swift5_types: 0x14
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x10f98
+  __TEXT.__unwind_info: 0x110a8
   __TEXT.__eh_frame: 0x388
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x17f0
+  __DATA_CONST.__const: 0x1810
   __DATA_CONST.__objc_classlist: 0x11d8
   __DATA_CONST.__objc_catlist: 0x140
-  __DATA_CONST.__objc_protolist: 0xf8
+  __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b78
+  __DATA_CONST.__objc_selrefs: 0x6cd8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x1120
-  __DATA_CONST.__objc_arraydata: 0x3c8
-  __DATA_CONST.__got: 0xf18
-  __AUTH_CONST.__const: 0x42a8
-  __AUTH_CONST.__cfstring: 0x7da0
-  __AUTH_CONST.__objc_const: 0x2d118
+  __DATA_CONST.__objc_superrefs: 0x1128
+  __DATA_CONST.__objc_arraydata: 0x3e8
+  __DATA_CONST.__got: 0xf78
+  __AUTH_CONST.__const: 0x4358
+  __AUTH_CONST.__cfstring: 0x7f40
+  __AUTH_CONST.__objc_const: 0x2d2f8
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__objc_intobj: 0x300
-  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__objc_intobj: 0x348
+  __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0xbc8
-  __AUTH.__objc_data: 0xa1c0
-  __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0x11e0
-  __DATA.__data: 0xd30
-  __DATA.__common: 0x8
+  __AUTH_CONST.__auth_got: 0xbf8
+  __AUTH.__objc_data: 0xa210
+  __DATA.__objc_ivar: 0x1200
+  __DATA.__data: 0xdc0
   __DATA_DIRTY.__objc_data: 0x10e0
-  __DATA_DIRTY.__data: 0x278
-  __DATA_DIRTY.__bss: 0x390
+  __DATA_DIRTY.__data: 0x288
+  __DATA_DIRTY.__bss: 0x310
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/Versions/A/AudioToolboxCore
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/Versions/A/EmbeddedAcousticRecognition
-  - /System/Library/PrivateFrameworks/FeatureFlags.framework/Versions/A/FeatureFlags
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/Versions/A/GenerativeModels
   - /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset
   - /System/Library/PrivateFrameworks/ModelCatalog.framework/Versions/A/ModelCatalog

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10583
-  Symbols:   21453
-  CStrings:  2279
+  Functions: 10628
+  Symbols:   21568
+  CStrings:  2298
 
Symbols:
+ +[_LTHotfixManager _errorForHTTPResponse:]
+ +[_LTHotfixManager _hotfixBasePath]
+ +[_LTHotfixManager _hotfixDirectoryNameForEntry:]
+ +[_LTHotfixManager _selectHotfixEntryFromMapping:minimumFormatVersion:maximumFormatVersion:]
+ +[_LTTranslationServer _aiInferenceLocationErrorForContext:]
+ +[_LTTranslationServer _contextForcesPrivateCloudCompute:]
+ -[_LTAIAdapterTranslationEngine aiInferenceLocation]
+ -[_LTAIAdapterTranslationEngine initWithLocalePair:taskHint:selfLoggingManager:processIdentifier:aiInferenceLocation:]
+ -[_LTAIAdapterTranslationEngine initWithLocalePair:taskHint:selfLoggingManager:processIdentifier:aiInferenceLocation:translator:]
+ -[_LTDLanguageAssetCache _traditionalObservationsWithLocaleRanks:]
+ -[_LTDLanguageAssetCache observationList:canReportAILanguagesForConfiguration:]
+ -[_LTDLanguageAssetCache observationList:filterAIObservations:forConfiguration:]
+ -[_LTDLanguageStatusObservationList .cxx_destruct]
+ -[_LTDLanguageStatusObservationList _baseObservationsForEngineType:]
+ -[_LTDLanguageStatusObservationList _cachedObservationsForKey:build:]
+ -[_LTDLanguageStatusObservationList _calculateCombinedObservations]
+ -[_LTDLanguageStatusObservationList _invalidateCachedObservationsForEngineTypes:]
+ -[_LTDLanguageStatusObservationList _invalidateCachedObservationsIncludingPCC]
+ -[_LTDLanguageStatusObservationList _makeIndeterminateObservations:]
+ -[_LTDLanguageStatusObservationList _mergeObservation:withObservation:]
+ -[_LTDLanguageStatusObservationList _observationByFoldingPCCObservation:intoObservation:]
+ -[_LTDLanguageStatusObservationList _observationsByFoldingPCCIntoObservations:]
+ -[_LTDLanguageStatusObservationList _observationsForEffectiveConfiguration:]
+ -[_LTDLanguageStatusObservationList aiObservations]
+ -[_LTDLanguageStatusObservationList combinedObservations]
+ -[_LTDLanguageStatusObservationList delegate]
+ -[_LTDLanguageStatusObservationList init]
+ -[_LTDLanguageStatusObservationList observationsForConfiguration:]
+ -[_LTDLanguageStatusObservationList pccObservations]
+ -[_LTDLanguageStatusObservationList setAiObservations:]
+ -[_LTDLanguageStatusObservationList setDelegate:]
+ -[_LTDLanguageStatusObservationList setPccObservations:]
+ -[_LTDLanguageStatusObservationList setTraditionalObservations:]
+ -[_LTDLanguageStatusObservationList traditionalObservations]
+ -[_LTHotfixManager _CDNURLForPathComponent:]
+ -[_LTHotfixManager _archiveRequestForURL:]
+ -[_LTHotfixManager _downloadWithRequest:completion:]
+ -[_LTHotfixManager _installNewestSupportedHotfix:]
+ -[_LTHotfixManager _mappingPlistRequest]
+ -[_LTOnlineTranslationEngine _clearCurrentSpeechSessionIfEqualTo:]
+ -[_LTOnlineTranslationEngine _currentSpeechSession]
+ -[_LTOnlineTranslationEngine _ongoingSpeechSession]
+ -[_LTOnlineTranslationEngine _setCurrentSpeechSession:]
+ -[_LTOnlineTranslationEngine _speechSessionCompletedWithError:session:]
+ -[_LTOnlineTranslationEngine _takeCurrentSpeechSession]
+ OBJC_IVAR_$__LTAIAdapterTranslationEngine._aiInferenceLocation
+ OBJC_IVAR_$__LTDLanguageStatusObservationList._aiObservations
+ OBJC_IVAR_$__LTDLanguageStatusObservationList._cachedObservations
+ OBJC_IVAR_$__LTDLanguageStatusObservationList._delegate
+ OBJC_IVAR_$__LTDLanguageStatusObservationList._pccObservations
+ OBJC_IVAR_$__LTDLanguageStatusObservationList._traditionalObservations
+ OBJC_IVAR_$__LTHotfixManager._hotfixURLLock
+ OBJC_IVAR_$__LTOnlineTranslationEngine._speechSessionLock
+ _NSURLIsDirectoryKey
+ _OBJC_CLASS_$_NSHTTPURLResponse
+ _OBJC_CLASS_$_NSMutableURLRequest
+ _OBJC_CLASS_$_NSScanner
+ _OBJC_CLASS_$__LTDLanguageStatusObservationList
+ _OBJC_METACLASS_$__LTDLanguageStatusObservationList
+ __50-[_LTHotfixManager _installNewestSupportedHotfix:]_block_invoke
+ __52-[_LTHotfixManager _downloadWithRequest:completion:]_block_invoke
+ __76-[_LTDLanguageStatusObservationList _observationsForEffectiveConfiguration:]_block_invoke
+ __LTAIInferenceLocationString
+ __OBJC_$_CLASS_METHODS__LTTranslationServer
+ __OBJC_$_INSTANCE_METHODS__LTDLanguageStatusObservationList
+ __OBJC_$_INSTANCE_VARIABLES__LTDLanguageStatusObservationList
+ __OBJC_$_PROP_LIST__LTDLanguageStatusObservationList
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__LTDLanguageStatusObservationListDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__LTDLanguageStatusObservationListDelegate
+ __OBJC_$_PROTOCOL_REFS__LTDLanguageStatusObservationListDelegate
+ __OBJC_CLASS_RO_$__LTDLanguageStatusObservationList
+ __OBJC_LABEL_PROTOCOL_$__LTDLanguageStatusObservationListDelegate
+ __OBJC_METACLASS_RO_$__LTDLanguageStatusObservationList
+ __OBJC_PROTOCOL_$__LTDLanguageStatusObservationListDelegate
+ ___29-[_LTHotfixManager hotfixURL]_block_invoke
+ ___33-[_LTHotfixManager setHotfixURL:]_block_invoke
+ ___50-[_LTHotfixManager _installNewestSupportedHotfix:]_block_invoke
+ ___51-[_LTOnlineTranslationEngine _currentSpeechSession]_block_invoke
+ ___52-[_LTHotfixManager _downloadWithRequest:completion:]_block_invoke
+ ___55-[_LTOnlineTranslationEngine _setCurrentSpeechSession:]_block_invoke
+ ___55-[_LTOnlineTranslationEngine _takeCurrentSpeechSession]_block_invoke
+ ___66-[_LTDLanguageAssetCache _traditionalObservationsWithLocaleRanks:]_block_invoke
+ ___66-[_LTOnlineTranslationEngine _clearCurrentSpeechSessionIfEqualTo:]_block_invoke
+ ___68-[_LTDLanguageStatusObservationList _makeIndeterminateObservations:]_block_invoke
+ ___76-[_LTDLanguageStatusObservationList _observationsForEffectiveConfiguration:]_block_invoke
+ ___PCCLanguageExpansion_isAvailable
+ ___block_descriptor_40_e8_32s_e12_"NSURL"8?0l
+ ___block_descriptor_48_e8_32s40s_e14_"NSArray"8?0l
+ ___block_descriptor_48_e8_32s_e14_"NSArray"8?0l
+ ___block_descriptor_48_ea8_32s40r_e5_v8?0l
+ ___block_descriptor_48_ea8_32w40w_e17_v16?0"NSError"8l
+ ___block_descriptor_56_ea8_32s40s48r_e5_v8?0l
+ ___block_descriptor_56_ea8_32s40w48w_e17_v16?0"NSError"8l
+ ___block_descriptor_73_ea8_32s40s48s56bs64w_e17_v16?0"NSArray"8l
+ ___block_descriptor_81_ea8_32s40s48s56s64s72bs_e5_v8?0l
+ ___block_descriptor_89_e8_32s40s48s56s64bs72r_e15_v16?0?<v?B>8l
+ ___copy_helper_block_ea8_32s40r
+ ___copy_helper_block_ea8_32s40s48r
+ ___copy_helper_block_ea8_32s40w48w
+ ___copy_helper_block_ea8_32w40w
+ ___destroy_helper_block_ea8_32s40w48w
+ ___destroy_helper_block_ea8_32w40w
+ ___swift_memcpy16_8
+ _hotfixReplacementPhaseName
+ _objc_msgSend$URL
+ _objc_msgSend$_CDNURLForPathComponent:
+ _objc_msgSend$_aiInferenceLocationErrorForContext:
+ _objc_msgSend$_archiveRequestForURL:
+ _objc_msgSend$_baseObservationsForEngineType:
+ _objc_msgSend$_cachedObservationsForKey:build:
+ _objc_msgSend$_calculateCombinedObservations
+ _objc_msgSend$_clearCurrentSpeechSessionIfEqualTo:
+ _objc_msgSend$_contextForcesPrivateCloudCompute:
+ _objc_msgSend$_currentSpeechSession
+ _objc_msgSend$_downloadWithRequest:completion:
+ _objc_msgSend$_errorForHTTPResponse:
+ _objc_msgSend$_hotfixDirectoryNameForEntry:
+ _objc_msgSend$_installNewestSupportedHotfix:
+ _objc_msgSend$_invalidateCachedObservationsForEngineTypes:
+ _objc_msgSend$_invalidateCachedObservationsIncludingPCC
+ _objc_msgSend$_mappingPlistRequest
+ _objc_msgSend$_observationByFoldingPCCObservation:intoObservation:
+ _objc_msgSend$_observationsByFoldingPCCIntoObservations:
+ _objc_msgSend$_observationsForEffectiveConfiguration:
+ _objc_msgSend$_ongoingSpeechSession
+ _objc_msgSend$_selectHotfixEntryFromMapping:minimumFormatVersion:maximumFormatVersion:
+ _objc_msgSend$_setCurrentSpeechSession:
+ _objc_msgSend$_speechSessionCompletedWithError:session:
+ _objc_msgSend$_takeCurrentSpeechSession
+ _objc_msgSend$_traditionalObservationsWithLocaleRanks:
+ _objc_msgSend$aiInferenceLocation
+ _objc_msgSend$allowsPrivateCloudComputeLanguages
+ _objc_msgSend$canReportAILanguagesForConfiguration:
+ _objc_msgSend$dataTaskWithRequest:completionHandler:
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$initWithLocalePair:taskHint:processIdentifier:aiInferenceLocation:hotfixURL:
+ _objc_msgSend$initWithLocalePair:taskHint:selfLoggingManager:processIdentifier:aiInferenceLocation:
+ _objc_msgSend$initWithLocalePair:taskHint:selfLoggingManager:processIdentifier:aiInferenceLocation:translator:
+ _objc_msgSend$initWithTranslation:romanization:alignments:engineInfo:
+ _objc_msgSend$lt_invalidRequestErrorWithDescription:
+ _objc_msgSend$observationList:canReportAILanguagesForConfiguration:
+ _objc_msgSend$observationList:filterAIObservations:forConfiguration:
+ _objc_msgSend$observationsForConfiguration:
+ _objc_msgSend$pathComponents
+ _objc_msgSend$pccObservationsWithLocaleRanks:
+ _objc_msgSend$requestWithURL:
+ _objc_msgSend$scanInt:
+ _objc_msgSend$scannerWithString:
+ _objc_msgSend$sessionCreationError
+ _objc_msgSend$setAiObservations:
+ _objc_msgSend$setAllowsPrivateCloudComputeLanguages:
+ _objc_msgSend$setCachePolicy:
+ _objc_msgSend$setEngineType:
+ _objc_msgSend$setPccObservations:
+ _objc_msgSend$setTraditionalObservations:
+ _objc_msgSend$statusCode
+ _objc_msgSend$statusConfiguration
+ _parseHotfixEntryVersions
+ _parseHotfixVersionNumber
+ _symbolic Say_____GSg 10Foundation6LocaleV
+ _symbolic _____Sg 12ModelCatalog17UseCaseIdentifierV
+ _symbolic _____Sg 20TranslationInference0A17ExecutionLocationO
+ _symbolic _____Sg 20TranslationInference0A9ModelTypeO
+ _symbolic _____Sg_ABt 12ModelCatalog17UseCaseIdentifierV
+ _symbolic _____Sg_ABt 20TranslationInference0A9ModelTypeO
- -[_LTAIAdapterTranslationEngine initWithLocalePair:taskHint:selfLoggingManager:processIdentifier:]
- -[_LTAIAdapterTranslationEngine initWithLocalePair:taskHint:selfLoggingManager:processIdentifier:translator:]
- -[_LTDLanguageAssetCache _makeIndeterminateObservations:]
- -[_LTDLanguageAssetCache _mergeObservation:withObservation:]
- -[_LTHotfixManager _CDNURL:]
- -[_LTHotfixManager _downloadWithURL:completion:]
- -[_LTHotfixManager _updateHotfixInternal:]
- -[_LTOnlineTranslationEngine _hasOngoingSpeechSession]
- -[_LTOnlineTranslationEngine _speechSessionCompletedWithError:]
- _OBJC_CLASS_$__TtCs12_SwiftObject
- _OBJC_METACLASS_$__TtCs12_SwiftObject
- __42-[_LTHotfixManager _updateHotfixInternal:]_block_invoke
- __48-[_LTHotfixManager _downloadWithURL:completion:]_block_invoke
- __DATA__TtC17TranslationDaemon32TranslationInferenceUserDefaults
- __IVARS__TtC17TranslationDaemon32TranslationInferenceUserDefaults
- __METACLASS_DATA__TtC17TranslationDaemon32TranslationInferenceUserDefaults
- ___42-[_LTHotfixManager _updateHotfixInternal:]_block_invoke
- ___44-[_LTDLanguageAssetCache multicastObservers]_block_invoke
- ___48-[_LTHotfixManager _downloadWithURL:completion:]_block_invoke
- ___57-[_LTDLanguageAssetCache _makeIndeterminateObservations:]_block_invoke
- ___block_descriptor_40_ea8_32w_e17_v16?0"NSError"8l
- ___block_descriptor_48_ea8_32s40w_e17_v16?0"NSError"8l
- ___block_descriptor_56_ea8_32s40s48s_e5_v8?0l
- ___block_descriptor_65_ea8_32s40s48bs56w_e17_v16?0"NSArray"8l
- ___block_descriptor_73_ea8_32s40s48s56s64bs_e5_v8?0l
- ___block_descriptor_81_e8_32s40s48s56bs64r_e15_v16?0?<v?B>8l
- ___copy_helper_block_ea8_32s40s48s
- ___copy_helper_block_ea8_32s40s48s56s64b
- ___swift_memcpy0_1
- _associated conformance 17TranslationDaemon0aB8FeaturesOSHAASQ
- _objc_msgSend$_CDNURL:
- _objc_msgSend$_downloadWithURL:completion:
- _objc_msgSend$_hasOngoingSpeechSession
- _objc_msgSend$_speechSessionCompletedWithError:
- _objc_msgSend$_updateHotfixInternal:
- _objc_msgSend$canReportAILanguagesForObserver:
- _objc_msgSend$dataTaskWithURL:completionHandler:
- _objc_msgSend$doubleForKey:
- _objc_msgSend$initWithLocalePair:taskHint:processIdentifier:hotfixURL:
- _objc_msgSend$initWithLocalePair:taskHint:selfLoggingManager:processIdentifier:
- _objc_msgSend$initWithLocalePair:taskHint:selfLoggingManager:processIdentifier:translator:
- _objc_msgSend$initWithTranslation:alignments:engineInfo:
- _objc_msgSend$useDedicatedMachPort
- _swift_deallocClassInstance
- _swift_lookUpClassMethod
- _symbolic So14NSUserDefaultsC
- _symbolic _____ 17TranslationDaemon0A21InferenceUserDefaultsC
- _symbolic _____ 17TranslationDaemon0aB8FeaturesO
- _symbolic _____Sg 20TranslationInference0A9ModelInfoV0C4TypeO
- _symbolic _____Sg_ABt 20TranslationInference0A9ModelInfoV0C4TypeO
CStrings:
+ "%d-%d"
+ "%zd-%zd"
+ ".."
+ "@\"NSArray\"8@?0"
+ "@\"NSURL\"8@?0"
+ "A"
+ "AI translator has no inference session, reporting the session creation failure instead of an unsupported pair: %@"
+ "Archive contained no entries"
+ "Archive contained no entries, refusing to treat it as an install"
+ "Can't report AI languages for configuration because there's no `provider`; configuration: %{public}@"
+ "Context forces PCC, restricting engine selection to the AI adapter; route: %ld"
+ "Context's aiInferenceLocation can't be honored, returning no engine: %@"
+ "Creating AI adapter engine; requested aiInferenceLocation: %{public}@, route: %ld, onDeviceEngineType: %ld"
+ "Failed to lookup child folders of Hotfix base path %{public}@ with error: %@"
+ "Failed to read archive entry"
+ "Failed to read archive entry: %s"
+ "Finished extracting %zu entries to: %{public}@"
+ "Hotfix CDN returned HTTP %ld"
+ "Hotfix CDN returned an empty response"
+ "Hotfix entry does not name a version to install"
+ "Hotfix manager %{public}@ phase completed"
+ "Hotfix manager %{public}@ phase failed: %@"
+ "Ignoring hotfix directory whose name isn't <formatVersion>-<assetVersion>: %{public}@"
+ "Ignoring hotfix entry that isn't a directory: %{public}@"
+ "Ignoring hotfix entry whose asset name is not a single path component: %{public}@"
+ "Ignoring hotfix entry whose versions don't name a hotfix: FormatVersion=%{public}@ HotfixAssetVersion=%{public}@"
+ "No versioned hotfix directory under %{public}@"
+ "Not retiring speech session %p because it's no longer the current session"
+ "PCCLanguageExpansion"
+ "Received %{public}@ request; trusted: %{BOOL}i, aiInferenceLocation: %{public}@, route: %ld"
+ "Refusing to install a hotfix entry that names no version: %@"
+ "Replaced online speech session %p with %p"
+ "Retired online speech session %p"
+ "Unexpectedly asked for unsupported engineType %zu, can't return base observations"
+ "aiInferenceLocation is .pcc, but forcedOfflineTranslation makes this request incompatible with PCC"
+ "aiInferenceLocation is .pcc, but onDeviceEngineType is .traditional, which can't use AI inference"
+ "commit"
+ "invalid(%ld)"
+ "prepare"
+ "rollback"
- "\r"
- "Can't create AI adapter inference engine because the feature flag is disabled"
- "Can't report AI languages for observer because there's no `provider`; observer: %{public}@"
- "Failed to lookup child folders of Hotfix base path %{public}@"
- "Feature flag is disabled"
- "Finished extracting archive to: %{public}@"
- "Hotfix manager refresh completed"
- "Hotfix manager refresh failure: %@"
- "Hotfix manager replace phase commit"
- "Hotfix manager replace phase prepare"
- "Hotfix manager replace phase rollback"
- "Reporting empty LLM observations because feature flag is disabled"
- "Skipping observer multicast for non-traditional engine"
- "SpeechEngineAudioDetokenizerModelPath"
- "SpeechEngineAudioDetokenizerUseCase"
- "SpeechEngineAudioTokenizerModelPath"
- "SpeechEngineAudioTokenizerUseCase"
- "SpeechToSpeechAutoEndPointAfterSeconds"
- "SpeechToSpeechModelBundleIdentifierOverride"
- "SpeechToSpeechSkipANEVersionCheck"
- "ai_adapter_inference"
```
