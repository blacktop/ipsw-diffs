## Translation

> `/System/Library/Frameworks/Translation.framework/Translation`

```diff

-365.13.0.0.0
-  __TEXT.__text: 0x5c6c4
-  __TEXT.__auth_stubs: 0x1320
-  __TEXT.__objc_methlist: 0x5810
-  __TEXT.__const: 0xf88
-  __TEXT.__cstring: 0x30d4
-  __TEXT.__oslogstring: 0x4b36
-  __TEXT.__gcc_except_tab: 0xbac
+380.1.0.0.0
+  __TEXT.__text: 0x5b720
+  __TEXT.__objc_methlist: 0x5b88
+  __TEXT.__const: 0xf68
+  __TEXT.__cstring: 0x3324
+  __TEXT.__oslogstring: 0x5146
+  __TEXT.__gcc_except_tab: 0xb3c
   __TEXT.__ustring: 0x90
-  __TEXT.__swift5_typeref: 0x627
-  __TEXT.__swift5_capture: 0x19c
+  __TEXT.__swift5_typeref: 0x607
   __TEXT.__constg_swiftt: 0x3e4
   __TEXT.__swift5_reflstr: 0x3da
   __TEXT.__swift5_fieldmd: 0x3a0
+  __TEXT.__swift5_capture: 0x14c
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x108
   __TEXT.__swift5_proto: 0x7c
   __TEXT.__swift5_types: 0x50
   __TEXT.__swift_as_entry: 0x4c
   __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0x1c78
-  __TEXT.__eh_frame: 0x8f8
-  __TEXT.__objc_classname: 0xc96
-  __TEXT.__objc_methname: 0xc0cd
-  __TEXT.__objc_methtype: 0x1f8e
-  __TEXT.__objc_stubs: 0x6cc0
-  __DATA_CONST.__got: 0x568
-  __DATA_CONST.__const: 0x1e48
-  __DATA_CONST.__objc_classlist: 0x2f8
+  __TEXT.__swift_as_cont: 0x84
+  __TEXT.__unwind_info: 0x1c10
+  __TEXT.__eh_frame: 0x8e0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1e58
+  __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26e0
+  __DATA_CONST.__objc_selrefs: 0x2840
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x280
+  __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0x178
-  __AUTH_CONST.__auth_got: 0x9a0
-  __AUTH_CONST.__const: 0x1020
-  __AUTH_CONST.__cfstring: 0x3880
-  __AUTH_CONST.__objc_const: 0xb430
+  __DATA_CONST.__got: 0x580
+  __AUTH_CONST.__const: 0x1010
+  __AUTH_CONST.__cfstring: 0x3c00
+  __AUTH_CONST.__objc_const: 0xbaf8
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1380
-  __AUTH.__data: 0x6b0
-  __DATA.__objc_ivar: 0x84c
-  __DATA.__data: 0xbc0
-  __DATA.__bss: 0x1090
-  __DATA.__common: 0x80
-  __DATA_DIRTY.__objc_data: 0x9b0
-  __DATA_DIRTY.__bss: 0x80
+  __AUTH_CONST.__auth_got: 0xa60
+  __AUTH.__objc_data: 0x98
+  __AUTH.__data: 0x338
+  __DATA.__objc_ivar: 0x898
+  __DATA.__data: 0xb70
+  __DATA.__bss: 0x1080
+  __DATA.__common: 0x30
+  __DATA_DIRTY.__objc_data: 0x1dd8
+  __DATA_DIRTY.__data: 0x3a8
+  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
-  - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage
   - /System/Library/Frameworks/Speech.framework/Speech
+  - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore
   - /System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation
   - /System/Library/PrivateFrameworks/ToolKit.framework/ToolKit
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FF3ECD73-CA01-3149-A511-82966C882C9A
-  Functions: 2763
-  Symbols:   7710
-  CStrings:  3699
+  UUID: 581A2956-B614-33B3-BF77-27FB02FE1E95
+  Functions: 2838
+  Symbols:   7995
+  CStrings:  1385
 
Symbols:
+ +[_LTAudioEncoder addWAVHeaders:format:]
+ +[_LTAudioEncoder addWAVHeaders:format:].cold.1
+ +[_LTAudioEncoder addWAVHeaders:format:].cold.2
+ +[_LTAudioEncoder convertToWAVData:sourceFormat:]
+ +[_LTAudioEncoder convertToWAVData:sourceFormat:].cold.1
+ +[_LTAudioEncoder convertToWAVData:sourceFormat:].cold.2
+ +[_LTAudioEncoder convertToWAVData:sourceFormat:].cold.3
+ +[_LTAudioEncoder convertToWAVData:sourceFormat:].cold.4
+ +[_LTAudioEncoder convertToWAVData:sourceFormat:].cold.5
+ +[_LTAudioEncoder convertToWAVData:sourceFormat:].cold.6
+ +[_LTLanguageDetectionConfiguration supportsSecureCoding]
+ +[_LTLanguageStatus canGetStatusWithMachPort:]
+ +[_LTLanguageStatusConfiguration supportsSecureCoding]
+ +[_LTLanguageStatusObservation describeModalities:]
+ +[_LTSpeechTranslationAudioResult supportsSecureCoding]
+ +[_LTTranslator languagesForText:configuration:completion:]
+ -[NSString(TranslationAdditions) lt_stringByReplacingInvalidUTF8Characters]
+ -[NSString(TranslationAdditions) lt_stringByReplacingInvalidUTF8Characters].cold.1
+ -[NSString(TranslationAdditions) lt_stringByReplacingInvalidUTF8Characters].cold.2
+ -[_LTLanguageAssetModel modalities]
+ -[_LTLanguageAvailability _returnUnsupportedStatusInsteadOfError:]
+ -[_LTLanguageAvailability preflightChecker:continueCheckingFromStep:forConfiguration:completion:].cold.3
+ -[_LTLanguageDetectionConfiguration copyWithZone:]
+ -[_LTLanguageDetectionConfiguration encodeWithCoder:]
+ -[_LTLanguageDetectionConfiguration engineType]
+ -[_LTLanguageDetectionConfiguration initWithCoder:]
+ -[_LTLanguageDetectionConfiguration initWithTaskHint:]
+ -[_LTLanguageDetectionConfiguration model]
+ -[_LTLanguageDetectionConfiguration setEngineType:]
+ -[_LTLanguageDetectionConfiguration setModel:]
+ -[_LTLanguageDetectionConfiguration setStrategy:]
+ -[_LTLanguageDetectionConfiguration setUseDedicatedTextMachPort:]
+ -[_LTLanguageDetectionConfiguration strategy]
+ -[_LTLanguageDetectionConfiguration taskHint]
+ -[_LTLanguageDetectionConfiguration useDedicatedTextMachPort]
+ -[_LTLanguageStatus _broadcastStatus:]
+ -[_LTLanguageStatus _initWithConfiguration:multicaster:observations:]
+ -[_LTLanguageStatus _scheduleNextHeartbeat]
+ -[_LTLanguageStatus _sendHeartbeatNow]
+ -[_LTLanguageStatus _setUpHeartbeatIfNeeded]
+ -[_LTLanguageStatus configuration]
+ -[_LTLanguageStatus initWithConfiguration:observations:]
+ -[_LTLanguageStatus modalities]
+ -[_LTLanguageStatusConfiguration copyWithZone:]
+ -[_LTLanguageStatusConfiguration encodeWithCoder:]
+ -[_LTLanguageStatusConfiguration engineType]
+ -[_LTLanguageStatusConfiguration hash]
+ -[_LTLanguageStatusConfiguration initWithCoder:]
+ -[_LTLanguageStatusConfiguration initWithTaskHint:engineType:useDedicatedMachPort:]
+ -[_LTLanguageStatusConfiguration init]
+ -[_LTLanguageStatusConfiguration isEqual:]
+ -[_LTLanguageStatusConfiguration needsHeartbeat]
+ -[_LTLanguageStatusConfiguration setEngineType:]
+ -[_LTLanguageStatusConfiguration setNeedsHeartbeat:]
+ -[_LTLanguageStatusConfiguration setTaskHint:]
+ -[_LTLanguageStatusConfiguration setUseDedicatedMachPort:]
+ -[_LTLanguageStatusConfiguration taskHint]
+ -[_LTLanguageStatusConfiguration useDedicatedMachPort]
+ -[_LTLanguageStatusMulticaster _cancelWithConnectionIdentifier:useDedicatedMachPort:]
+ -[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:configuration:synchronous:]
+ -[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:configuration:synchronous:].cold.1
+ -[_LTLanguageStatusMulticaster _multicastObservations:configuration:]
+ -[_LTLanguageStatusMulticaster _reconnectIfStreamingWithConnectionIdentifier:configuration:]
+ -[_LTLanguageStatusMulticaster _reconnectIfStreamingWithConnectionIdentifier:configuration:].cold.1
+ -[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:configuration:]
+ -[_LTLanguageStatusMulticaster languageStatusChangedForConfiguration:observations:]
+ -[_LTLanguageStatusObservation initWithLocale:progress:downloadSize:status:sources:modalities:rank:]
+ -[_LTLanguageStatusObservation modalities]
+ -[_LTLanguageVariantFilter preventFilteringLocalesForFilter:]
+ -[_LTSpeechRecognitionResult setUtteranceID:]
+ -[_LTSpeechRecognitionResult utteranceID]
+ -[_LTSpeechTranslationAudioResult .cxx_destruct]
+ -[_LTSpeechTranslationAudioResult audioData]
+ -[_LTSpeechTranslationAudioResult audioFormatSettings]
+ -[_LTSpeechTranslationAudioResult description]
+ -[_LTSpeechTranslationAudioResult encodeWithCoder:]
+ -[_LTSpeechTranslationAudioResult endOfUtterance]
+ -[_LTSpeechTranslationAudioResult initWithCoder:]
+ -[_LTSpeechTranslationAudioResult initWithLocale:audioData:audioFormatSettings:endOfUtterance:utteranceID:isFinal:]
+ -[_LTSpeechTranslationAudioResult isFinal]
+ -[_LTSpeechTranslationAudioResult locale]
+ -[_LTSpeechTranslationAudioResult setAudioData:]
+ -[_LTSpeechTranslationAudioResult setAudioFormatSettings:]
+ -[_LTSpeechTranslationAudioResult setEndOfUtterance:]
+ -[_LTSpeechTranslationAudioResult setLocale:]
+ -[_LTSpeechTranslationAudioResult setUtteranceID:]
+ -[_LTSpeechTranslationAudioResult utteranceID]
+ -[_LTTranslationResult setUtteranceID:]
+ -[_LTTranslationResult utteranceID]
+ GCC_except_table22
+ GCC_except_table28
+ GCC_except_table35
+ GCC_except_table43
+ GCC_except_table46
+ GCC_except_table48
+ GCC_except_table53
+ _AVNumberOfChannelsKey
+ _AVSampleRateKey
+ _OBJC_CLASS_$__LTAudioEncoder
+ _OBJC_CLASS_$__LTLanguageDetectionConfiguration
+ _OBJC_CLASS_$__LTLanguageStatusConfiguration
+ _OBJC_CLASS_$__LTSpeechTranslationAudioResult
+ _OBJC_IVAR_$__LTLanguageAssetModel._modalities
+ _OBJC_IVAR_$__LTLanguageDetectionConfiguration._engineType
+ _OBJC_IVAR_$__LTLanguageDetectionConfiguration._model
+ _OBJC_IVAR_$__LTLanguageDetectionConfiguration._strategy
+ _OBJC_IVAR_$__LTLanguageDetectionConfiguration._taskHint
+ _OBJC_IVAR_$__LTLanguageDetectionConfiguration._useDedicatedTextMachPort
+ _OBJC_IVAR_$__LTLanguageStatus._configuration
+ _OBJC_IVAR_$__LTLanguageStatus._isCancelled
+ _OBJC_IVAR_$__LTLanguageStatus._modalities
+ _OBJC_IVAR_$__LTLanguageStatusConfiguration._engineType
+ _OBJC_IVAR_$__LTLanguageStatusConfiguration._needsHeartbeat
+ _OBJC_IVAR_$__LTLanguageStatusConfiguration._taskHint
+ _OBJC_IVAR_$__LTLanguageStatusConfiguration._useDedicatedMachPort
+ _OBJC_IVAR_$__LTLanguageStatusObservation._modalities
+ _OBJC_IVAR_$__LTSpeechRecognitionResult._utteranceID
+ _OBJC_IVAR_$__LTSpeechTranslationAudioResult._audioData
+ _OBJC_IVAR_$__LTSpeechTranslationAudioResult._audioFormatSettings
+ _OBJC_IVAR_$__LTSpeechTranslationAudioResult._endOfUtterance
+ _OBJC_IVAR_$__LTSpeechTranslationAudioResult._isFinal
+ _OBJC_IVAR_$__LTSpeechTranslationAudioResult._locale
+ _OBJC_IVAR_$__LTSpeechTranslationAudioResult._utteranceID
+ _OBJC_IVAR_$__LTTranslationResult._utteranceID
+ _OBJC_METACLASS_$__LTAudioEncoder
+ _OBJC_METACLASS_$__LTLanguageDetectionConfiguration
+ _OBJC_METACLASS_$__LTLanguageStatusConfiguration
+ _OBJC_METACLASS_$__LTSpeechTranslationAudioResult
+ _SANDBOX_CHECK_NO_REPORT
+ __LTOSLogAudioEncoder
+ __LTOSLogAudioEncoder.cold.1
+ __LTOSLogAudioEncoder.log
+ __LTOSLogAudioEncoder.onceToken
+ __LTSandboxAllowsXPCWithTranslationd
+ __LTSandboxAllowsXPCWithTranslationd.cold.1
+ __LTSandboxAllowsXPCWithTranslationd.cold.2
+ __OBJC_$_CLASS_METHODS__LTAudioEncoder
+ __OBJC_$_CLASS_METHODS__LTLanguageDetectionConfiguration
+ __OBJC_$_CLASS_METHODS__LTLanguageStatus
+ __OBJC_$_CLASS_METHODS__LTLanguageStatusConfiguration
+ __OBJC_$_CLASS_METHODS__LTSpeechTranslationAudioResult
+ __OBJC_$_CLASS_PROP_LIST__LTLanguageDetectionConfiguration
+ __OBJC_$_CLASS_PROP_LIST__LTLanguageStatusConfiguration
+ __OBJC_$_CLASS_PROP_LIST__LTSpeechTranslationAudioResult
+ __OBJC_$_INSTANCE_METHODS__LTLanguageDetectionConfiguration
+ __OBJC_$_INSTANCE_METHODS__LTLanguageStatusConfiguration
+ __OBJC_$_INSTANCE_METHODS__LTSpeechTranslationAudioResult
+ __OBJC_$_INSTANCE_VARIABLES__LTLanguageDetectionConfiguration
+ __OBJC_$_INSTANCE_VARIABLES__LTLanguageStatusConfiguration
+ __OBJC_$_INSTANCE_VARIABLES__LTSpeechTranslationAudioResult
+ __OBJC_$_PROP_LIST__LTLanguageDetectionConfiguration
+ __OBJC_$_PROP_LIST__LTLanguageStatusConfiguration
+ __OBJC_$_PROP_LIST__LTSpeechTranslationAudioResult
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__LTLanguageVariantFilterDelegate
+ __OBJC_CLASS_PROTOCOLS_$__LTLanguageDetectionConfiguration
+ __OBJC_CLASS_PROTOCOLS_$__LTLanguageStatusConfiguration
+ __OBJC_CLASS_PROTOCOLS_$__LTSpeechTranslationAudioResult
+ __OBJC_CLASS_RO_$__LTAudioEncoder
+ __OBJC_CLASS_RO_$__LTLanguageDetectionConfiguration
+ __OBJC_CLASS_RO_$__LTLanguageStatusConfiguration
+ __OBJC_CLASS_RO_$__LTSpeechTranslationAudioResult
+ __OBJC_METACLASS_RO_$__LTAudioEncoder
+ __OBJC_METACLASS_RO_$__LTLanguageDetectionConfiguration
+ __OBJC_METACLASS_RO_$__LTLanguageStatusConfiguration
+ __OBJC_METACLASS_RO_$__LTSpeechTranslationAudioResult
+ ___21-[_LTTranslator log:]_block_invoke.99
+ ___24-[_LTTranslator cleanup]_block_invoke.84
+ ___29+[_LTTranslator _clearCaches]_block_invoke.18
+ ___31+[_LTTranslator _deleteHotfix:]_block_invoke.39
+ ___31+[_LTTranslator _getAssetSize:]_block_invoke.43
+ ___31+[_LTTranslator _updateHotfix:]_block_invoke.38
+ ___33+[_LTTranslator removeLanguages:]_block_invoke.32
+ ___34+[_LTTranslator _updateAllAssets:]_block_invoke.37
+ ___34+[_LTTranslator installedLocales:]_block_invoke.40
+ ___38-[_LTLanguageStatus _broadcastStatus:]_block_invoke
+ ___39+[_LTTranslator onDeviceModeSupported:]_block_invoke.50
+ ___39-[_LTTranslator preheatForRequestSync:]_block_invoke.78
+ ___40+[_LTTranslator _offlineLanguageStatus:]_block_invoke.33
+ ___42+[_LTTranslator addLanguages:useCellular:]_block_invoke.29
+ ___42+[_LTTranslator selfLoggingEventWithData:]_block_invoke.102
+ ___42-[_LTTranslator updateOVADStreamingState:]_block_invoke.109
+ ___43-[_LTLanguageStatus _scheduleNextHeartbeat]_block_invoke
+ ___43-[_LTLanguageStatus _scheduleNextHeartbeat]_block_invoke_2
+ ___44+[_LTTranslator languageForText:completion:]_block_invoke.62
+ ___46-[_LTTranslator preheatForRequest:completion:]_block_invoke.81
+ ___49+[_LTAudioEncoder convertToWAVData:sourceFormat:]_block_invoke
+ ___50+[_LTTranslator installOfflineLocales:completion:]_block_invoke.45
+ ___51+[_LTTranslator modalitiesPerLocaleWithCompletion:]_block_invoke.57
+ ___52+[_LTTranslator installedLocalesForTask:completion:]_block_invoke.42
+ ___52-[_LTTranslator translate:useDedicatedTextMachPort:]_block_invoke.95
+ ___54+[_LTTranslator languageAssetsWithOptions:completion:]_block_invoke.22
+ ___54+[_LTTranslator selfLoggingInvocationCancelledForIDs:]_block_invoke.105
+ ___54+[_LTTranslator task:isSupportedInCountry:completion:]_block_invoke.61
+ ___58+[_LTTranslator textStreamingConfigurationWithCompletion:]_block_invoke.59
+ ___59+[_LTTranslator _purgeAllAssetsExcludingConfig:completion:]_block_invoke.36
+ ___59+[_LTTranslator languagesForText:configuration:completion:]_block_invoke
+ ___59+[_LTTranslator languagesForText:configuration:completion:]_block_invoke.71
+ ___59+[_LTTranslator languagesForText:configuration:completion:]_block_invoke.cold.1
+ ___59+[_LTTranslator languagesForText:configuration:completion:]_block_invoke_2
+ ___59+[_LTTranslator taskIsSupportedInCurrentRegion:completion:]_block_invoke.54
+ ___60+[_LTTranslator configInfoForLocale:otherLocale:completion:]_block_invoke.48
+ ___60+[_LTTranslator selfLoggingInvocationDidError:invocationId:]_block_invoke.106
+ ___63+[_LTTranslator setLanguageAssets:options:progress:completion:]_block_invoke.26
+ ___64+[_LTTranslator autoDetectSpeechUnsupportedPairsWithCompletion:]_block_invoke.56
+ ___65+[_LTTranslator _getServiceProxyWithDelegate:errorHandler:block:]_block_invoke.74
+ ___69+[_LTTranslator _purgeAssetForLanguagePair:userInitiated:completion:]_block_invoke.35
+ ___69+[_LTTranslator onDeviceModeEnabledWithDedicatedMachPort:completion:]_block_invoke.13
+ ___69-[_LTLanguageStatus _initWithConfiguration:multicaster:observations:]_block_invoke
+ ___69-[_LTLanguageStatus _initWithConfiguration:multicaster:observations:]_block_invoke.4
+ ___69-[_LTLanguageStatus _initWithConfiguration:multicaster:observations:]_block_invoke_2
+ ___69-[_LTLanguageStatusMulticaster _multicastObservations:configuration:]_block_invoke
+ ___70+[_LTTranslator additionalLikelyPreferredLocalesForLocale:completion:]_block_invoke.47
+ ___71+[_LTTranslator selfLoggingLanguageIdentificationCompletedWithLIDData:]_block_invoke.104
+ ___72+[_LTTranslator _downloadAssetForLanguagePair:userInitiated:completion:]_block_invoke.34
+ ___77+[_LTTranslator availableLocalePairsForTask:useDedicatedMachPort:completion:]_block_invoke.46
+ ___77-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:configuration:]_block_invoke
+ ___77-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:configuration:]_block_invoke.27
+ ___77-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:configuration:]_block_invoke.cold.1
+ ___77-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:configuration:]_block_invoke_2
+ ___77-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:configuration:]_block_invoke_3
+ ___77-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:configuration:]_block_invoke_4
+ ___77-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:configuration:]_block_invoke_4.cold.1
+ ___81+[_LTTranslator selfLoggingInvocationStartedWithData:invocationStartedTier1Data:]_block_invoke.103
+ ___84+[_LTTranslator shouldPresentSystemFirstUseConsentWithDedicatedMachPort:completion:]_block_invoke.53
+ ___85-[_LTLanguageStatusMulticaster _cancelWithConnectionIdentifier:useDedicatedMachPort:]_block_invoke
+ ___85-[_LTLanguageStatusMulticaster _cancelWithConnectionIdentifier:useDedicatedMachPort:]_block_invoke.32
+ ___85-[_LTLanguageStatusMulticaster _cancelWithConnectionIdentifier:useDedicatedMachPort:]_block_invoke.cold.1
+ ___85-[_LTLanguageStatusMulticaster _cancelWithConnectionIdentifier:useDedicatedMachPort:]_block_invoke_2
+ ___88-[_LTTextTranslationRequest _replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:]_block_invoke.241
+ ___88-[_LTTextTranslationRequest _replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:]_block_invoke.241.cold.1
+ ___92-[_LTLanguageStatusMulticaster _reconnectIfStreamingWithConnectionIdentifier:configuration:]_block_invoke
+ ___94+[_LTTranslator _getTextServiceProxyWithDelegate:useDedicatedTextMachPort:errorHandler:block:]_block_invoke.75
+ ___95-[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:configuration:synchronous:]_block_invoke
+ ____LTOSLogAudioEncoder_block_invoke
+ ___block_descriptor_32_e48_"NSString"16?0"_LTLanguageStatusObservation"8l
+ ___block_descriptor_40_e8_32s_e21_?<v?"NSArray">8?0ls32l8
+ ___block_descriptor_40_e8_32s_e5_B8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e46_v24?0"<_LTTextTranslationService>"8?<v?>16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48w_e46_v24?0"<_LTTextTranslationService>"8?<v?>16lw48l8s32l8s40l8
+ ___block_descriptor_58_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e17_v16?0"NSError"8lw56l8s48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e5_v8?0ls32l8s40l8s48l8w64l8s56l8
+ ___block_literal_global.108
+ ___block_literal_global.21
+ ___block_literal_global.45
+ ___block_literal_global.77
+ ___block_literal_global.80
+ ___block_literal_global.83
+ ___block_literal_global.86
+ ___block_literal_global.98
+ ___error
+ ___swift__destructor
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.12
+ ___swift_closure_destructor.14
+ ___swift_closure_destructor.16
+ ___swift_closure_destructor.20
+ ___swift_closure_destructor.31
+ ___swift_closure_destructor.34
+ ___swift_closure_destructor.38
+ ___swift_closure_destructor.4
+ ___swift_closure_destructor.42
+ ___swift_closure_destructor.4Tm
+ ___swift_closure_destructor.76
+ ___swift_closure_destructor.8
+ ___swift_closure_destructor.82
+ ___swift_closure_destructor.9
+ ___swift_closure_destructorTm
+ ___swift_get_extra_inhabitant_index.39Tm
+ ___swift_store_extra_inhabitant_index.40Tm
+ __keyForConfig
+ __swift_implicitisolationactor_to_executor_cast
+ _block_copy_helper.16
+ _block_copy_helper.22
+ _block_copy_helper.72
+ _block_copy_helper.78
+ _block_copy_helper.8
+ _block_copy_helper.84
+ _block_descriptor.10
+ _block_descriptor.18
+ _block_descriptor.24
+ _block_descriptor.74
+ _block_descriptor.80
+ _block_descriptor.86
+ _block_destroy_helper.17
+ _block_destroy_helper.23
+ _block_destroy_helper.73
+ _block_destroy_helper.79
+ _block_destroy_helper.85
+ _block_destroy_helper.9
+ _getpid
+ _kLTDebugPreventLanguageVariantFilteringPreferenceKey
+ _kLTEntitlementMachPortName
+ _kLTIncludeAIOnlyLanguagesInAllTasksKey
+ _kLTNonEntitlementMachPortName
+ _malloc_type_malloc
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_broadcastStatus:
+ _objc_msgSend$_cancelWithConnectionIdentifier:useDedicatedMachPort:
+ _objc_msgSend$_closeConnectionForced:forIdentifier:configuration:synchronous:
+ _objc_msgSend$_initWithConfiguration:multicaster:observations:
+ _objc_msgSend$_multicastObservations:configuration:
+ _objc_msgSend$_reconnectIfStreamingWithConnectionIdentifier:configuration:
+ _objc_msgSend$_returnUnsupportedStatusInsteadOfError:
+ _objc_msgSend$_scheduleNextHeartbeat
+ _objc_msgSend$_sendHeartbeatNow
+ _objc_msgSend$_setUpHeartbeatIfNeeded
+ _objc_msgSend$_startWithConnectionIdentifier:configuration:
+ _objc_msgSend$addWAVHeaders:format:
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$audioBufferList
+ _objc_msgSend$audioData
+ _objc_msgSend$channelCount
+ _objc_msgSend$configuration
+ _objc_msgSend$data
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$describeModalities:
+ _objc_msgSend$endOfUtterance
+ _objc_msgSend$getCharacters:range:
+ _objc_msgSend$initWithCharactersNoCopy:length:freeWhenDone:
+ _objc_msgSend$initWithCommonFormat:sampleRate:channels:interleaved:
+ _objc_msgSend$initWithTaskHint:
+ _objc_msgSend$initWithTaskHint:engineType:useDedicatedMachPort:
+ _objc_msgSend$languagesForText:configuration:completion:
+ _objc_msgSend$lt_appGroupDefaults
+ _objc_msgSend$modalities
+ _objc_msgSend$model
+ _objc_msgSend$needsHeartbeat
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$preventFilteringLocalesForFilter:
+ _objc_msgSend$sampleRate
+ _objc_msgSend$setDownmix:
+ _objc_msgSend$setEngineType:
+ _objc_msgSend$setModel:
+ _objc_msgSend$setNeedsHeartbeat:
+ _objc_msgSend$setPrimeMethod:
+ _objc_msgSend$setStrategy:
+ _objc_msgSend$setUseDedicatedMachPort:
+ _objc_msgSend$setUseDedicatedTextMachPort:
+ _objc_msgSend$startLanguageStatusChangeObservation:configuration:completion:
+ _objc_msgSend$strategy
+ _objc_msgSend$unsignedShortValue
+ _objc_msgSend$useDedicatedTextMachPort
+ _objc_msgSend$utteranceID
+ _objc_release_x2
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
+ _sandbox_check
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
- -[_LTLanguageStatus _initWithTaskHint:engineType:useDedicatedMachPort:multicaster:observations:]
- -[_LTLanguageStatus observations]
- -[_LTLanguageStatusMulticaster _cancelWithConnectionIdentifier:taskHint:useDedicatedMachPort:]
- -[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:synchronous:]
- -[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:synchronous:].cold.1
- -[_LTLanguageStatusMulticaster _multicastObservations:taskHint:engineType:progress:]
- -[_LTLanguageStatusMulticaster _reconnectIfStreamingWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]
- -[_LTLanguageStatusMulticaster _replayLastObservationsOnHeartbeat:]
- -[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]
- -[_LTLanguageStatusMulticaster languageStatusChangedForTaskHint:engineType:progress:observations:]
- -[_LTLanguageStatusObservation initWithLocale:progress:downloadSize:status:rank:]
- -[_LTLanguageStatusObservation initWithLocale:progress:downloadSize:status:sources:rank:]
- GCC_except_table29
- GCC_except_table34
- GCC_except_table38
- GCC_except_table42
- GCC_except_table44
- GCC_except_table47
- GCC_except_table52
- GCC_except_table9
- _OBJC_IVAR_$__LTLanguageStatus._engineType
- _OBJC_IVAR_$__LTLanguageStatus._taskHint
- _OBJC_IVAR_$__LTLanguageStatus._useDedicatedMachPort
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_9
- ___104-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]_block_invoke
- ___104-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]_block_invoke.21
- ___104-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]_block_invoke.cold.1
- ___104-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]_block_invoke_2
- ___104-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]_block_invoke_3
- ___104-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]_block_invoke_3.cold.1
- ___119-[_LTLanguageStatusMulticaster _reconnectIfStreamingWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]_block_invoke
- ___122-[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:synchronous:]_block_invoke
- ___21-[_LTTranslator log:]_block_invoke.98
- ___24-[_LTTranslator cleanup]_block_invoke.83
- ___29+[_LTTranslator _clearCaches]_block_invoke.12
- ___31+[_LTTranslator _deleteHotfix:]_block_invoke.33
- ___31+[_LTTranslator _getAssetSize:]_block_invoke.37
- ___31+[_LTTranslator _updateHotfix:]_block_invoke.32
- ___33+[_LTTranslator removeLanguages:]_block_invoke.26
- ___34+[_LTTranslator _updateAllAssets:]_block_invoke.31
- ___34+[_LTTranslator installedLocales:]_block_invoke.34
- ___39+[_LTTranslator onDeviceModeSupported:]_block_invoke.44
- ___39-[_LTTranslator preheatForRequestSync:]_block_invoke.77
- ___40+[_LTTranslator _offlineLanguageStatus:]_block_invoke.27
- ___42+[_LTTranslator addLanguages:useCellular:]_block_invoke.23
- ___42+[_LTTranslator selfLoggingEventWithData:]_block_invoke.101
- ___42-[_LTTranslator updateOVADStreamingState:]_block_invoke.108
- ___44+[_LTTranslator languageForText:completion:]_block_invoke.56
- ___46-[_LTTranslator preheatForRequest:completion:]_block_invoke.80
- ___50+[_LTTranslator installOfflineLocales:completion:]_block_invoke.39
- ___51+[_LTTranslator modalitiesPerLocaleWithCompletion:]_block_invoke.51
- ___52+[_LTTranslator installedLocalesForTask:completion:]_block_invoke.36
- ___52-[_LTTranslator translate:useDedicatedTextMachPort:]_block_invoke.93
- ___54+[_LTTranslator languageAssetsWithOptions:completion:]_block_invoke.16
- ___54+[_LTTranslator selfLoggingInvocationCancelledForIDs:]_block_invoke.104
- ___54+[_LTTranslator task:isSupportedInCountry:completion:]_block_invoke.55
- ___58+[_LTTranslator textStreamingConfigurationWithCompletion:]_block_invoke.53
- ___59+[_LTTranslator _purgeAllAssetsExcludingConfig:completion:]_block_invoke.30
- ___59+[_LTTranslator taskIsSupportedInCurrentRegion:completion:]_block_invoke.48
- ___60+[_LTTranslator configInfoForLocale:otherLocale:completion:]_block_invoke.42
- ___60+[_LTTranslator selfLoggingInvocationDidError:invocationId:]_block_invoke.105
- ___63+[_LTTranslator setLanguageAssets:options:progress:completion:]_block_invoke.20
- ___64+[_LTTranslator autoDetectSpeechUnsupportedPairsWithCompletion:]_block_invoke.50
- ___65+[_LTTranslator _getServiceProxyWithDelegate:errorHandler:block:]_block_invoke.70
- ___67-[_LTLanguageStatusMulticaster _replayLastObservationsOnHeartbeat:]_block_invoke
- ___69+[_LTTranslator _purgeAssetForLanguagePair:userInitiated:completion:]_block_invoke.29
- ___69+[_LTTranslator onDeviceModeEnabledWithDedicatedMachPort:completion:]_block_invoke.7
- ___70+[_LTTranslator additionalLikelyPreferredLocalesForLocale:completion:]_block_invoke.41
- ___71+[_LTTranslator selfLoggingLanguageIdentificationCompletedWithLIDData:]_block_invoke.103
- ___72+[_LTTranslator _downloadAssetForLanguagePair:userInitiated:completion:]_block_invoke.28
- ___77+[_LTTranslator availableLocalePairsForTask:useDedicatedMachPort:completion:]_block_invoke.40
- ___81+[_LTTranslator selfLoggingInvocationStartedWithData:invocationStartedTier1Data:]_block_invoke.102
- ___84+[_LTTranslator shouldPresentSystemFirstUseConsentWithDedicatedMachPort:completion:]_block_invoke.47
- ___84-[_LTLanguageStatusMulticaster _multicastObservations:taskHint:engineType:progress:]_block_invoke
- ___88-[_LTTextTranslationRequest _replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:]_block_invoke.243
- ___88-[_LTTextTranslationRequest _replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:]_block_invoke.243.cold.1
- ___94+[_LTTranslator _getTextServiceProxyWithDelegate:useDedicatedTextMachPort:errorHandler:block:]_block_invoke.74
- ___94-[_LTLanguageStatusMulticaster _cancelWithConnectionIdentifier:taskHint:useDedicatedMachPort:]_block_invoke
- ___94-[_LTLanguageStatusMulticaster _cancelWithConnectionIdentifier:taskHint:useDedicatedMachPort:]_block_invoke.25
- ___94-[_LTLanguageStatusMulticaster _cancelWithConnectionIdentifier:taskHint:useDedicatedMachPort:]_block_invoke.cold.1
- ___94-[_LTLanguageStatusMulticaster _cancelWithConnectionIdentifier:taskHint:useDedicatedMachPort:]_block_invoke_2
- ___96-[_LTLanguageStatus _initWithTaskHint:engineType:useDedicatedMachPort:multicaster:observations:]_block_invoke
- ___96-[_LTLanguageStatus _initWithTaskHint:engineType:useDedicatedMachPort:multicaster:observations:]_block_invoke.3
- ___96-[_LTLanguageStatus _initWithTaskHint:engineType:useDedicatedMachPort:multicaster:observations:]_block_invoke_2
- ___99+[_LTTranslator languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:]_block_invoke
- ___99+[_LTTranslator languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:]_block_invoke.64
- ___99+[_LTTranslator languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:]_block_invoke.cold.1
- ___99+[_LTTranslator languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:]_block_invoke_2
- ___block_descriptor_40_e8_32s_e48_"NSString"16?0"_LTLanguageStatusObservation"8ls32l8
- ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_65_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
- ___block_descriptor_65_e8_32s40w_e46_v24?0"<_LTTextTranslationService>"8?<v?>16lw40l8s32l8
- ___block_descriptor_65_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_67_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_72_e8_32s40bs_e46_v24?0"<_LTTextTranslationService>"8?<v?>16ls32l8s40l8
- ___block_descriptor_73_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s40l8s32l8
- ___block_descriptor_81_e8_32s40s48bs56w_e5_v8?0ls32l8s40l8w56l8s48l8
- ___block_literal_global.107
- ___block_literal_global.15
- ___block_literal_global.24
- ___block_literal_global.5
- ___block_literal_global.76
- ___block_literal_global.79
- ___block_literal_global.82
- ___block_literal_global.85
- ___block_literal_global.97
- ___swift_get_extra_inhabitant_index.45Tm
- ___swift_store_extra_inhabitant_index.46Tm
- __keyForTaskHint
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_Translation
- _block_copy_helper.14
- _block_copy_helper.24
- _block_copy_helper.30
- _block_copy_helper.79
- _block_copy_helper.85
- _block_copy_helper.91
- _block_descriptor.16
- _block_descriptor.26
- _block_descriptor.32
- _block_descriptor.81
- _block_descriptor.87
- _block_descriptor.93
- _block_destroy_helper.15
- _block_destroy_helper.25
- _block_destroy_helper.31
- _block_destroy_helper.80
- _block_destroy_helper.86
- _block_destroy_helper.92
- _objc_msgSend$_cancelWithConnectionIdentifier:taskHint:useDedicatedMachPort:
- _objc_msgSend$_closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:synchronous:
- _objc_msgSend$_initWithTaskHint:engineType:useDedicatedMachPort:multicaster:observations:
- _objc_msgSend$_multicastObservations:taskHint:engineType:progress:
- _objc_msgSend$_reconnectIfStreamingWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:
- _objc_msgSend$_replayLastObservationsOnHeartbeat:
- _objc_msgSend$_startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:
- _objc_msgSend$initWithLocale:progress:downloadSize:status:sources:rank:
- _objc_msgSend$languagesForText:usingModel:strategy:taskHint:completion:
- _objc_msgSend$languagesForText:usingModel:strategy:useDedicatedTextMachPort:completion:
- _objc_msgSend$observations
- _objc_msgSend$startLanguageStatusChangeObservation:taskHint:engineType:completion:
- _objectdestroy.19Tm
- _objectdestroy.4Tm
- _objectdestroy.77Tm
- _symbolic SS_ypt
- _symbolic ScESg
- _symbolic _____Sg 11Translation0A5ErrorV
- _symbolic _____SgXw 11Translation20LanguageAvailabilityC
CStrings:
+ "%.2f"
+ "%@%@%@"
+ "%@%@%@:%@"
+ "%@:%ld Downloading [%f] of %zu %@"
+ "%@:%ld Installed %@"
+ "%@:%ld Not Installed %@"
+ "%@|%@"
+ ":"
+ "<%@: %p; locale = %@; audioDataLength = %lu bytes; endOfUtterance = %@; utteranceID = %@; isFinal = %@>"
+ "@?<v@?@\"NSArray\">8@?0"
+ "Added WAV headers: 44 bytes header + %zu bytes PCM data = %zu bytes total"
+ "Audio conversion failed: %@"
+ "AudioEncoder"
+ "B8@?0"
+ "Client didn't request observation heartbeat, not setting up timer for listener %{public}@"
+ "DebugPreventLanguageVariantFiltering"
+ "Failed to create WAV audio format"
+ "Failed to create audio converter"
+ "Failed to create output buffer"
+ "Failed to encode WAV header strings"
+ "Failed to establish a connection for language status observation: %@"
+ "Failed to lookup sandbox permission to talk to translationd over %{public}@: %i"
+ "Failed to malloc a buffer for string, so can't replace invalid UTF8 characters. Using an empty string instead"
+ "IncludeAIOnlyLanguagesInAllTasks"
+ "LID determined the source text is %{public}@, which isn't a supported language; won't ask the user to disambiguate, reporting unsupported status"
+ "LTLanguageStatus %{public}@ alloc task:%zd engineType:%zd dedicated:%{BOOL}i"
+ "LTLanguageStatus %{public}@ cancel"
+ "LTLanguageStatus %{public}@ dealloc"
+ "LTLanguageStatus %{public}@ receive multicast with %zd observations"
+ "No audio buffers to convert"
+ "No converted data generated"
+ "Not sending next heartbeat since status listener %{public}@ was already cancelled"
+ "Obsv replay [%{public}@]"
+ "Preflight checks determined a language or pairing isn't supported; returning unsupported status rather than an error"
+ "Processed %zu buffers using AVAudioConverter, generated %zu bytes WAV file"
+ "RIFF"
+ "S"
+ "Sandbox allows connecting to translationd over %{public}@"
+ "Sandbox does not allow connecting to translationd over %{public}@"
+ "Setting up heartbeat for listener %{public}@"
+ "String contains characters not encodable as UTF-8; replacing lone surrogates"
+ "T"
+ "Unexpected return value %i from sandbox_check(); reporting sandbox is not allowed over %{public}@"
+ "WAVE"
+ "_LTLanguageStatus failed to connect to translationd and the sandbox doesn't allow it, so will not attempt to reconnect. The _LTLanguageStatus instance will not get any updates. If you see this in your process, the caller of _LTLanguageStatus should be first checking `+[_LTLanguageStatus canGetStatusWithMachPort:]` to know that querying status isn't possible from this process"
+ "a"
+ "audioData"
+ "audioFormatSettings"
+ "data"
+ "dedicated mach port"
+ "entitlement mach port"
+ "fmt "
+ "mach-lookup"
+ "modalities"
+ "model"
+ "needsHeartbeat"
+ "s"
+ "strategy"
+ "t"
+ "useDedicatedTextMachPort"
+ "utteranceID"
- "#16@0:8"
- "%@:%@:%.2f"
- "%@:%@:%@"
- "%@:%ld Downloading [%f] of %zu"
- "%@:%ld Installed"
- "%@:%ld Not Installed"
- ".cxx_destruct"
- "2!"
- "@\"<_LTDisambiguableResultDelegate>\""
- "@\"<_LTDisambiguableSentenceDelegate>\""
- "@\"<_LTDisambiguableSentenceHistoryProviding>\""
- "@\"<_LTLanguageAvailabilityDelegate>\""
- "@\"<_LTLanguageVariantFilterDelegate>\""
- "@\"<_LTPreflightCheckerDelegate>\""
- "@\"<_LTPreflightLocaleResolving>\""
- "@\"<_LTSpeechTranslationDelegate>\""
- "@\"<_LTStreamingUtteranceTranslating>\""
- "@\"<_LTStreamingUtteranceTranslatorDelegate>\""
- "@\"<_LTTextSessionDelegate>\""
- "@\"<_LTTextSessionLocaleProviding>\""
- "@\"<_LTTextSessionTranslating>\""
- "@\"<_LTTextTranslationService>\""
- "@\"<_LTTranslationService>\""
- "@\"AVAudioConverter\""
- "@\"AVAudioFile\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"24@0:8@\"_LTLanguageVariantFilter\"16"
- "@\"NSAttributedString\""
- "@\"NSCountedSet\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSHashTable\""
- "@\"NSLocale\""
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\"24@0:8@\"_LTDisambiguableSentence\"16"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"SFSpeechRecognitionResult\""
- "@\"_LTAssetProgress\""
- "@\"_LTAssetProgress\"16@0:8"
- "@\"_LTDirectedEdge\""
- "@\"_LTDisambiguableResult\""
- "@\"_LTGenmojiReplacementManager\""
- "@\"_LTLanguageAvailability\""
- "@\"_LTLanguageDetectionResult\""
- "@\"_LTLanguageStatus\""
- "@\"_LTLanguageStatusMulticaster\""
- "@\"_LTLocalePair\""
- "@\"_LTPreflightChecker\""
- "@\"_LTRateLimiter\""
- "@\"_LTSELFLoggingInvocationOptions\""
- "@\"_LTSELFLoggingTranslateAppContext\""
- "@\"_LTSELFLoggingTranslationLIDData\""
- "@\"_LTSELFLoggingTranslationTTSData\""
- "@\"_LTSafariLatencyLoggingRequest\""
- "@\"_LTSpeechRecognitionSausage\""
- "@\"_LTStreamingInput\""
- "@\"_LTStreamingOutput\""
- "@\"_LTSupportedLocaleList\""
- "@\"_LTTextToSpeechTranslationRequest\""
- "@\"_LTTranslationSession\""
- "@\"_LTTranslationStatistics\""
- "@\"_LTTranslator\""
- "@112@0:8@16{AudioStreamBasicDescription=dIIIIIIII}24{AudioStreamBasicDescription=dIIIIIIII}64^@104"
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16^@24"
- "@32@0:8@16d24"
- "@32@0:8@16q24"
- "@32@0:8Q16Q24"
- "@32@0:8Q16q24"
- "@32@0:8q16@24"
- "@36@0:8@16@24B32"
- "@36@0:8@16B24@28"
- "@36@0:8@16B24@?28"
- "@36@0:8Q16B24@?28"
- "@36@0:8q16B24@?28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16@24Q32"
- "@40@0:8@16@24q32"
- "@40@0:8@16Q24Q32"
- "@40@0:8@16q24@32"
- "@40@0:8@16q24q32"
- "@40@0:8Q16@24@?32"
- "@40@0:8Q16Q24@32"
- "@40@0:8q16@24@32"
- "@44@0:8@16@24@32B40"
- "@44@0:8@16@24q32B40"
- "@44@0:8q16B24q28q36"
- "@44@0:8q16q24B32@?36"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32@?40"
- "@48@0:8@16Q24@?32@?40"
- "@48@0:8@16q24@32@40"
- "@48@0:8Q16@24Q32Q40"
- "@48@0:8Q16Q24Q32Q40"
- "@48@0:8q16@24@32@40"
- "@48@0:8q16q24q32@40"
- "@52@0:8@16@24@32B40@44"
- "@52@0:8q16q24B32@36@?44"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24@32@?40@?48"
- "@56@0:8@16@24d32d40d48"
- "@56@0:8@16d24Q32q40q48"
- "@56@0:8@16{_NSRange=QQ}24{_NSRange=QQ}40"
- "@56@0:8Q16@24@32@40@48"
- "@56@0:8Q16@24@32@40@?48"
- "@56@0:8d16d24d32q40q48"
- "@56@0:8{AudioStreamBasicDescription=dIIIIIIII}16"
- "@56@0:8{_NSRange=QQ}16{_NSRange=QQ}32@48"
- "@60@0:8@16@24@32B40@?44@?52"
- "@64@0:8@16d24Q32q40Q48q56"
- "@64@0:8@16q24@32@40@48@56"
- "@64@0:8Q16Q24@32@40@48@56"
- "@64@0:8Q16Q24Q32@40@48@56"
- "@68@0:8@16{_NSRange=QQ}24{_NSRange=QQ}40@56B64"
- "@68@0:8@16{_NSRange=QQ}24{_NSRange=QQ}40B56@60"
- "@72@0:8@16@24@32@40@48@56@64"
- "@72@0:8@16{AudioStreamBasicDescription=dIIIIIIII}24^@64"
- "@72@0:8{_NSRange=QQ}16{_NSRange=QQ}32@48@56@64"
- "@84@0:8q16@24B32q36@44q52B60@64q72B80"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"_LTPreflightChecker\"16"
- "B24@0:8@16"
- "B24@0:8@?16"
- "B24@0:8Q16"
- "B24@0:8d16"
- "B32@0:8#16#24"
- "B32@0:8@16Q24"
- "B32@0:8@16q24"
- "B32@0:8q16@24"
- "B32@0:8q16q24"
- "B32@0:8{_NSRange=QQ}16"
- "I"
- "I16@0:8"
- "JSON"
- "JSONRepresentation"
- "LTArrayExtensions"
- "LTLanguageStatus %@ alloc task:%zd dedicated:%{BOOL}i"
- "LTLanguageStatus %@ cancel"
- "LTLanguageStatus %@ dealloc"
- "LTLanguageStatus %@ receive multicast with %zd observations"
- "LTLocaleIdentifier"
- "LTParagraphs"
- "LTTextUtilities"
- "LTTranslationError"
- "Language status observation connection closed due to error: %@"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Obsv replay [%@]"
- "Preflight checks determined the language pairing isn't supported; returning unsupported rather than an error"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q32@0:8@16q24"
- "Q40@0:8@16Q24Q32"
- "Replaying last language status observations"
- "Schedule replay of last language status observationsin in %fs"
- "T#,R"
- "T@\"<_LTDisambiguableResultDelegate>\",W,N,V_delegate"
- "T@\"<_LTDisambiguableSentenceDelegate>\",W,N,V_delegate"
- "T@\"<_LTDisambiguableSentenceHistoryProviding>\",W,N,V_historyProvider"
- "T@\"<_LTLanguageAvailabilityDelegate>\",W,N,V_delegate"
- "T@\"<_LTLanguageVariantFilterDelegate>\",W,N,V_delegate"
- "T@\"<_LTPreflightCheckerDelegate>\",W,N,V_delegate"
- "T@\"<_LTPreflightLocaleResolving>\",W,N"
- "T@\"<_LTPreflightLocaleResolving>\",W,N,V_localeResolver"
- "T@\"<_LTSpeechTranslationDelegate>\",W,N,V_delegate"
- "T@\"<_LTStreamingUtteranceTranslating>\",W,N,V_utteranceTranslator"
- "T@\"<_LTStreamingUtteranceTranslatorDelegate>\",W,N,V_delegate"
- "T@\"<_LTTextSessionDelegate>\",W,N,V_delegate"
- "T@\"<_LTTextSessionLocaleProviding>\",W,N"
- "T@\"<_LTTextSessionLocaleProviding>\",W,N,V_localeProvider"
- "T@\"<_LTTextSessionTranslating>\",W,N,V_textTranslator"
- "T@\"<_LTTextTranslationService>\",&,N,V_service"
- "T@\"NSArray\",&,N,V__offlineASRModelURLs"
- "T@\"NSArray\",&,N,V_alternatives"
- "T@\"NSArray\",&,N,V_bins"
- "T@\"NSArray\",&,N,V_lowConfidenceLocales"
- "T@\"NSArray\",&,N,V_transcriptions"
- "T@\"NSArray\",C,N,V_alignments"
- "T@\"NSArray\",C,N,V_asrModelURLs"
- "T@\"NSArray\",C,N,V_genderAlternatives"
- "T@\"NSArray\",C,N,V_ignoringAttributes"
- "T@\"NSArray\",C,N,V_labels"
- "T@\"NSArray\",C,N,V_locales"
- "T@\"NSArray\",C,N,V_localesRequiringAppleIntelligence"
- "T@\"NSArray\",C,N,V_lowConfidenceLocales"
- "T@\"NSArray\",C,N,V_paragraphs"
- "T@\"NSArray\",C,N,V_pauseCounts"
- "T@\"NSArray\",C,N,V_preToPostITN"
- "T@\"NSArray\",C,N,V_ranges"
- "T@\"NSArray\",C,N,V_replacementInfos"
- "T@\"NSArray\",C,N,V_senses"
- "T@\"NSArray\",C,N,V_tokens"
- "T@\"NSArray\",C,N,V_translations"
- "T@\"NSArray\",C,N,V_userInteractedSenses"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,C,N,V_assets"
- "T@\"NSArray\",R,C,N,V_batch"
- "T@\"NSArray\",R,C,N,V_cachedStatus"
- "T@\"NSArray\",R,C,N,V_localeList"
- "T@\"NSArray\",R,C,N,V_paragraphRequests"
- "T@\"NSArray\",R,C,N,V_paragraphResults"
- "T@\"NSArray\",R,C,N,V_sentences"
- "T@\"NSArray\",R,C,N,V_sourceStrings"
- "T@\"NSArray\",R,C,N,V_spans"
- "T@\"NSArray\",R,C,N,V_supportedLocales"
- "T@\"NSArray\",R,C,N,V_targetPhrases"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_adjacencyList"
- "T@\"NSArray\",R,N,V_links"
- "T@\"NSArray\",R,N,V_stableSegments"
- "T@\"NSArray\",R,N,V_supportedLocalePairs"
- "T@\"NSArray\",R,N,V_unvalidatedAdjacencyList"
- "T@\"NSAttributedString\",C,N,V_attributedText"
- "T@\"NSAttributedString\",C,N,V_text"
- "T@\"NSAttributedString\",R,C,N"
- "T@\"NSAttributedString\",R,C,N,V_attributedText"
- "T@\"NSAttributedString\",R,C,N,V_sourceAttributedText"
- "T@\"NSAttributedString\",R,C,N,V_targetAttributedText"
- "T@\"NSCountedSet\",&,N,V_localeDetectionCount"
- "T@\"NSCountedSet\",&,N,V_unsupportedLanguageCounts"
- "T@\"NSData\",C,N,V_metaInfoData"
- "T@\"NSDictionary\",C,N,V_confidences"
- "T@\"NSDictionary\",C,N,V_metaInfo"
- "T@\"NSDictionary\",C,N,V_sourceAttributes"
- "T@\"NSDictionary\",R,C,N"
- "T@\"NSDictionary\",R,N"
- "T@\"NSDictionary\",R,N,V_modalitiesPerLocale"
- "T@\"NSError\",C,N,V_invocationEndedError"
- "T@\"NSLocale\",&,N,V_topLocale"
- "T@\"NSLocale\",C,N"
- "T@\"NSLocale\",C,N,V_dominantLanguage"
- "T@\"NSLocale\",C,N,V_dominantLocale"
- "T@\"NSLocale\",C,N,V_lidUnsupportedLocale"
- "T@\"NSLocale\",C,N,V_locale"
- "T@\"NSLocale\",C,N,V_requestedSourceLocale"
- "T@\"NSLocale\",C,N,V_requestedTargetLocale"
- "T@\"NSLocale\",C,N,V_resolvedSourceLocale"
- "T@\"NSLocale\",C,N,V_resolvedTargetLocale"
- "T@\"NSLocale\",C,N,V_selectedLocale"
- "T@\"NSLocale\",C,N,V_systemLocale"
- "T@\"NSLocale\",C,N,V_targetLocale"
- "T@\"NSLocale\",R,C,N"
- "T@\"NSLocale\",R,C,N,V_locale"
- "T@\"NSLocale\",R,C,N,V_sourceLocale"
- "T@\"NSLocale\",R,C,N,V_targetLocale"
- "T@\"NSLocale\",R,N"
- "T@\"NSLocale\",R,N,V_locale"
- "T@\"NSLocale\",R,N,V_sourceLocale"
- "T@\"NSLocale\",R,N,V_targetLocale"
- "T@\"NSNumber\",C,N,V_group"
- "T@\"NSNumber\",R,C,N,V_genderNumber"
- "T@\"NSNumber\",R,N,V_defaultGender"
- "T@\"NSNumber\",R,N,V_gender"
- "T@\"NSNumber\",R,N,V_targetGender"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_handlerQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_translationQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N"
- "T@\"NSSet\",R,N"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_defaultGender"
- "T@\"NSString\",&,N,V_detailedModelVersion"
- "T@\"NSString\",&,N,V_modelVersion"
- "T@\"NSString\",&,N,V_mtState"
- "T@\"NSString\",&,N,V_sourceASRState"
- "T@\"NSString\",&,N,V_sourceTTSState"
- "T@\"NSString\",&,N,V_targetASRState"
- "T@\"NSString\",&,N,V_targetTTSState"
- "T@\"NSString\",&,N,V_text"
- "T@\"NSString\",&,N,V_word"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_appIdentifier"
- "T@\"NSString\",C,N,V_clientBundleID"
- "T@\"NSString\",C,N,V_conversationID"
- "T@\"NSString\",C,N,V_definition"
- "T@\"NSString\",C,N,V_errorsAsJSON"
- "T@\"NSString\",C,N,V_formattedString"
- "T@\"NSString\",C,N,V_identifier"
- "T@\"NSString\",C,N,V_invocationCancelledReason"
- "T@\"NSString\",C,N,V_localeIdentifier"
- "T@\"NSString\",C,N,V_processName"
- "T@\"NSString\",C,N,V_requestID"
- "T@\"NSString\",C,N,V_romanization"
- "T@\"NSString\",C,N,V_safariVersion"
- "T@\"NSString\",C,N,V_sanitizedFormattedString"
- "T@\"NSString\",C,N,V_sanitizedSourceString"
- "T@\"NSString\",C,N,V_senseID"
- "T@\"NSString\",C,N,V_sentence"
- "T@\"NSString\",C,N,V_sessionID"
- "T@\"NSString\",C,N,V_sourceContentAsJSON"
- "T@\"NSString\",C,N,V_sourceMatch"
- "T@\"NSString\",C,N,V_sourceString"
- "T@\"NSString\",C,N,V_stableString"
- "T@\"NSString\",C,N,V_targetContentAsJSON"
- "T@\"NSString\",C,N,V_targetMatch"
- "T@\"NSString\",C,N,V_text"
- "T@\"NSString\",C,N,V_translationPayload"
- "T@\"NSString\",C,N,V_trustedClientIdentifier"
- "T@\"NSString\",C,N,V_uniqueID"
- "T@\"NSString\",C,N,V_untrustedClientIdentifier"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_appIdentifier"
- "T@\"NSString\",R,C,N,V_clientIdentifier"
- "T@\"NSString\",R,C,N,V_deviceOS"
- "T@\"NSString\",R,C,N,V_deviceType"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,C,N,V_ltIdentifier"
- "T@\"NSString\",R,C,N,V_meaningDescription"
- "T@\"NSString\",R,C,N,V_originalSubstring"
- "T@\"NSString\",R,C,N,V_placeholderString"
- "T@\"NSString\",R,C,N,V_requestUniqueID"
- "T@\"NSString\",R,C,N,V_sessionID"
- "T@\"NSString\",R,C,N,V_sourceSnippet"
- "T@\"NSString\",R,C,N,V_sourceText"
- "T@\"NSString\",R,C,N,V_targetText"
- "T@\"NSString\",R,C,N,V_text"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_menuDescription"
- "T@\"NSString\",R,N,V_romanization"
- "T@\"NSString\",R,N,V_sourceText"
- "T@\"NSString\",R,N,V_targetPreview"
- "T@\"NSString\",R,N,V_text"
- "T@\"NSString\",R,N,V_translatedText"
- "T@\"NSURL\",&,N,V__lidModelURL"
- "T@\"NSURL\",&,N,V__offlineMTModelURL"
- "T@\"NSURL\",&,N,V_outputFileURL"
- "T@\"NSURL\",C,N,V_URL"
- "T@\"NSURL\",C,N,V_mtModelURL"
- "T@\"NSURL\",C,N,V_outputFileURL"
- "T@\"NSURL\",C,N,V_sourceURL"
- "T@\"NSURL\",C,N,V_webpageURL"
- "T@\"NSURL\",R,N,V_offlineMTModelURL"
- "T@\"NSUUID\",C,N,V_batchSessionUUID"
- "T@\"NSUUID\",C,N,V_logIdentifier"
- "T@\"NSUUID\",C,N,V_qssSessionId"
- "T@\"NSUUID\",C,N,V_selfLoggingID"
- "T@\"NSUUID\",C,N,V_sourceIdentifier"
- "T@\"NSUUID\",R,C,N,V_autoTranslateSessionId"
- "T@\"NSUUID\",R,C,N,V_invocationId"
- "T@\"NSUUID\",R,C,N,V_logIdentifier"
- "T@\"NSUUID\",R,C,N,V_sessionID"
- "T@\"NSUUID\",R,C,N,V_sourceIdentifier"
- "T@\"NSUUID\",R,C,N,V_tabSessionId"
- "T@\"NSUUID\",R,N,V_UUID"
- "T@\"NSUUID\",R,N,V_identifier"
- "T@\"NSUUID\",R,N,V_invocationId"
- "T@\"NSUserDefaults\",R,N"
- "T@\"SFSpeechRecognitionResult\",R,N,V_asrResult"
- "T@\"_LTAssetProgress\",&,N,V_progress"
- "T@\"_LTAssetProgress\",R,N"
- "T@\"_LTAssetProgress\",R,N,V_progress"
- "T@\"_LTDirectedEdge\",R,C,N,V_edge"
- "T@\"_LTDisambiguableResult\",&,N,V_disambiguableResult"
- "T@\"_LTDisambiguableResult\",C,N,V_disambiguableResult"
- "T@\"_LTDisambiguationNode\",R,N"
- "T@\"_LTInterruptionHandler\",R,N"
- "T@\"_LTLanguageDetectionResult\",&,N,V_lidResult"
- "T@\"_LTLanguageInstallationStatus\",R,C,N"
- "T@\"_LTLocalePair\",&,N,V_pair"
- "T@\"_LTLocalePair\",C,N,V_localePair"
- "T@\"_LTLocalePair\",C,N,V_translationLocalePair"
- "T@\"_LTLocalePair\",R,C,N,V_localePair"
- "T@\"_LTLocalePair\",R,N,V_localePair"
- "T@\"_LTPreflightChecker\",R,N,V_preflightChecker"
- "T@\"_LTRateLimiter\",&,N,V_rateLimiter"
- "T@\"_LTSELFLoggingInvocationOptions\",&,N,V_startInvocationOptions"
- "T@\"_LTSELFLoggingTranslateAppContext\",R,&,N,V_translateAppContext"
- "T@\"_LTSELFLoggingTranslationLIDData\",&,N,V_translationLIDData"
- "T@\"_LTSELFLoggingTranslationTTSData\",&,N,V_translationTTSData"
- "T@\"_LTSpeechRecognitionSausage\",&,N,V_bestRecognitionAlternatives"
- "T@\"_LTStreamingInput\",C,N,V_input"
- "T@\"_LTStreamingOutput\",R,N,V_output"
- "T@\"_LTTranslationStatistics\",C,N,V_statistics"
- "T@\"_LTTranslator\",&,N,V_translator"
- "T@?,C,N"
- "T@?,C,N,V_audioStartHandler"
- "T@?,C,N,V_completionHandler"
- "T@?,C,N,V_handler"
- "T@?,C,N,V_progressHandler"
- "T@?,C,N,V_textHandler"
- "T@?,C,N,V_textTranslationHandler"
- "T@?,C,N,V_translationHandler"
- "T@?,R,C,N,V_completion"
- "T@?,R,C,N,V_progress"
- "T@?,R,N,V_observations"
- "TB,N"
- "TB,N,GisFinal,V_final"
- "TB,N,GisLowConfidence,V_lowConfidence"
- "TB,N,GisPhrasebookMatch,V_phrasebookMatch"
- "TB,N,GisStable,V_stable"
- "TB,N,V__forcedOnlineTranslation"
- "TB,N,V__supportsGenderDisambiguation"
- "TB,N,V_allowOnlineTranslation"
- "TB,N,V_allowsAIInference"
- "TB,N,V_autoEndpoint"
- "TB,N,V_autodetectLanguage"
- "TB,N,V_cancelOnCleanup"
- "TB,N,V_censorSpeech"
- "TB,N,V_cleanUpExistingSpeechSession"
- "TB,N,V_deviceSupportsTranslation"
- "TB,N,V_enableAirPodsOwnVAD"
- "TB,N,V_enableMultiFieldInput"
- "TB,N,V_enableOfflineStreamStabilizer"
- "TB,N,V_enableStreamingSpeechTranslation"
- "TB,N,V_enableTranslationSemanticSegmentation"
- "TB,N,V_enableVAD"
- "TB,N,V_endOfUtterance"
- "TB,N,V_endSent"
- "TB,N,V_forceSourceLocale"
- "TB,N,V_forcedOfflineTranslation"
- "TB,N,V_hasSpaceAfter"
- "TB,N,V_isAutoplayTranslation"
- "TB,N,V_isConfident"
- "TB,N,V_isFinal"
- "TB,N,V_isForDownloadApprovalOnly"
- "TB,N,V_isHeadless"
- "TB,N,V_isStable"
- "TB,N,V_muteTTSBasedOnRingerSwitchIfPossible"
- "TB,N,V_needsUpdate"
- "TB,N,V_overrideOngoingSessionIfNeeded"
- "TB,N,V_preferOnDeviceIfAvailable"
- "TB,N,V_requiresMultiParagraphPathway"
- "TB,N,V_shouldTranslate"
- "TB,N,V_supportsGenderDisambiguation"
- "TB,N,V_test_avoidXPCConnections"
- "TB,N,V_useCellular"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_endOfUtterance"
- "TB,R,N,V_isFinal"
- "TB,R,N,V_isForDownloadRequest"
- "TB,R,N,V_isGenderAlternativeEnabled"
- "TB,R,N,V_isHeadless"
- "TB,R,N,V_isIndeterminateProgress"
- "TB,R,N,V_isPlayTranslationsEnabled"
- "TB,R,N,V_languageIdentificationEnabled"
- "TB,R,N,V_shouldTranslate"
- "TB,R,N,V_useDedicatedMachPort"
- "TI,N,V_audioSessionID"
- "TI,N,V_length"
- "TI,N,V_offset"
- "TI,N,V_sampleIndex"
- "TQ,N,V_bestAlternativeIndex"
- "TQ,N,V_maximumDynamicContentRequests"
- "TQ,N,V_maximumPageLoadRequests"
- "TQ,N,V_selectedPhraseIndex"
- "TQ,R"
- "TQ,R,N,V_downloadSize"
- "TQ,R,N,V_linkIndex"
- "TQ,R,N,V_options"
- "TQ,R,N,V_sources"
- "TQ,R,N,V_targetLinkIndex"
- "TQ,R,N,V_targetPhraseIndex"
- "TQ,R,N,V_type"
- "Td,N,V_confidence"
- "Td,N,V_eosLikelihood"
- "Td,N,V_maxConfidence"
- "Td,N,V_minConfidence"
- "Td,N,V_silencePosterior"
- "Td,N,V_startTime"
- "Td,N,V_ttsPlaybackRate"
- "Td,R,N"
- "Td,R,N,V_firstParagraphComplete"
- "Td,R,N,V_firstResponse"
- "Td,R,N,V_maxTimeBetweenTranslations"
- "Td,R,N,V_minTimeBetweenTranslations"
- "Td,R,N,V_pageComplete"
- "Td,R,N,V_progress"
- "Td,R,N,V_progressComplete"
- "Td,R,N,V_start"
- "Td,R,N,V_userIdleTime"
- "TextSessionSupport"
- "Tq,N"
- "Tq,N,V__asrConfidenceThreshold"
- "Tq,N,V__lidThreshold"
- "Tq,N,V__mtConfidenceThreshold"
- "Tq,N,V_asrConfidenceThreshold"
- "Tq,N,V_audioChannel"
- "Tq,N,V_category"
- "Tq,N,V_confidence"
- "Tq,N,V_dataSharingOptInStatus"
- "Tq,N,V_generation"
- "Tq,N,V_inputSource"
- "Tq,N,V_inputSubtokenCount"
- "Tq,N,V_inputTokenCount"
- "Tq,N,V_lidThreshold"
- "Tq,N,V_onDeviceEngineType"
- "Tq,N,V_pairState"
- "Tq,N,V_playbackSpeed"
- "Tq,N,V_preferredStrategy"
- "Tq,N,V_processIdentifier"
- "Tq,N,V_processedAudioDurationInMilliseconds"
- "Tq,N,V_route"
- "Tq,N,V_sourceOrTargetLanguage"
- "Tq,N,V_sourceOrigin"
- "Tq,N,V_taskHint"
- "Tq,N,V_trailingSilenceDuration"
- "Tq,N,V_wordCount"
- "Tq,R,N"
- "Tq,R,N,V_conversationTabView"
- "Tq,R,N,V_displayMode"
- "Tq,R,N,V_engineType"
- "Tq,R,N,V_inputMode"
- "Tq,R,N,V_invocationType"
- "Tq,R,N,V_maxPartialTranslationAttempts"
- "Tq,R,N,V_minNumberOfCharactersForTranslation"
- "Tq,R,N,V_preferredStrategy"
- "Tq,R,N,V_rank"
- "Tq,R,N,V_route"
- "Tq,R,N,V_status"
- "Tq,R,N,V_tabName"
- "Tq,R,N,V_task"
- "Tq,R,N,V_taskHint"
- "Tq,R,N,V_type"
- "TranslationAdditions"
- "T{_NSRange=QQ},N,V_sourceRange"
- "T{_NSRange=QQ},N,V_targetRange"
- "T{_NSRange=QQ},N,V_textRange"
- "T{_NSRange=QQ},R,N,V_codePointsRange"
- "T{_NSRange=QQ},R,N,V_codeUnitsRange"
- "T{_NSRange=QQ},R,N,V_originalRange"
- "T{_NSRange=QQ},R,N,V_replacementRange"
- "T{_NSRange=QQ},R,N,V_sourceRange"
- "T{_NSRange=QQ},R,N,V_targetRange"
- "URL"
- "URLForResource:withExtension:"
- "UUIDString"
- "VS4CC"
- "Vv16@0:8"
- "^{OpaqueAudioConverter=}"
- "^{OpaqueAudioConverter=}96@0:8{AudioStreamBasicDescription=dIIIIIIII}16{AudioStreamBasicDescription=dIIIIIIII}56"
- "^{_NSZone=}16@0:8"
- "_LTAlignment"
- "_LTAssetProgress"
- "_LTAssetProgressReporting"
- "_LTAudioDecoder"
- "_LTBatchTextTranslationRequest"
- "_LTBlockBasedInterruptionHandler"
- "_LTCombinedRouteParagraphTranslationRequest"
- "_LTCombinedTranslationResult"
- "_LTDirectedEdge"
- "_LTDisambiguableResult"
- "_LTDisambiguableSentence"
- "_LTDisambiguableSentenceDelegate"
- "_LTDisambiguableSentenceHistoryProviding"
- "_LTDisambiguationChangeManager"
- "_LTDisambiguationChangeSet"
- "_LTDisambiguationLinkConfiguration"
- "_LTDisambiguationNode"
- "_LTDisambiguationUserSelection"
- "_LTGenmojiReplacementInfo"
- "_LTGenmojiReplacementManager"
- "_LTInstallRequest"
- "_LTInterruptionHandler"
- "_LTInterruptionObserving"
- "_LTLanguageAssetModel"
- "_LTLanguageAssetRequest"
- "_LTLanguageAssetRequestProtocol"
- "_LTLanguageAvailability"
- "_LTLanguageDetectionResult"
- "_LTLanguageInstallationStatus"
- "_LTLanguageListHelper"
- "_LTLanguagePairOfflineAvailability"
- "_LTLanguageStatus"
- "_LTLanguageStatusMulticaster"
- "_LTLanguageStatusObservation"
- "_LTLanguageStatusSnapshot"
- "_LTLanguageVariantFilter"
- "_LTLanguageVariantFilterDelegate"
- "_LTLocaleModalities"
- "_LTLocalePair"
- "_LTLoggingRequest"
- "_LTMultiParagraphTranslationRequest"
- "_LTParagraphTranslationRequest"
- "_LTPreflightChecker"
- "_LTPreflightCheckerDelegate"
- "_LTPreflightConfiguration"
- "_LTPreflightLocaleResolving"
- "_LTRateLimiter"
- "_LTSELFLoggingEventData"
- "_LTSELFLoggingInvocation"
- "_LTSELFLoggingInvocationOptions"
- "_LTSELFLoggingInvocationProvider"
- "_LTSELFLoggingTranslateAppContext"
- "_LTSELFLoggingTranslationLIDData"
- "_LTSELFLoggingTranslationTTSData"
- "_LTSafariLatencyLoggingRequest"
- "_LTServerEndpointerFeatures"
- "_LTSpeakRequest"
- "_LTSpeechLIDLoggingRequest"
- "_LTSpeechRecognitionBin"
- "_LTSpeechRecognitionResult"
- "_LTSpeechRecognitionSausage"
- "_LTSpeechRecognitionTokensAlternative"
- "_LTSpeechTranscription"
- "_LTSpeechTranslationDelegate"
- "_LTSpeechTranslationRequest"
- "_LTStabilizationTranslationRequest"
- "_LTStabilizationTranslationResult"
- "_LTStreamingInput"
- "_LTStreamingOutput"
- "_LTStreamingSpeakableOutput"
- "_LTStreamingUtteranceTranslating"
- "_LTStreamingUtteranceTranslator"
- "_LTSupportedLocaleList"
- "_LTTaskContext"
- "_LTTextInput"
- "_LTTextLanguageDetectionResult"
- "_LTTextResult"
- "_LTTextSession"
- "_LTTextSessionLocaleProviding"
- "_LTTextSessionRequest"
- "_LTTextSessionTranslating"
- "_LTTextStreamingConfiguration"
- "_LTTextToSpeechSanitizer"
- "_LTTextToSpeechTranslationRequest"
- "_LTTextTranslationRequest"
- "_LTTextTranslationService"
- "_LTTranslationCandidate"
- "_LTTranslationContext"
- "_LTTranslationFeedback"
- "_LTTranslationGenderAlternative"
- "_LTTranslationParagraph"
- "_LTTranslationRange"
- "_LTTranslationRequest"
- "_LTTranslationResult"
- "_LTTranslationSense"
- "_LTTranslationSensesLoggingRequest"
- "_LTTranslationService"
- "_LTTranslationSession"
- "_LTTranslationSpan"
- "_LTTranslationStatistics"
- "_LTTranslationToken"
- "_LTTranslationToolKit"
- "_LTTranslator"
- "_LTUnvalidatedEdgeInfo"
- "_LTWordTimingInfo"
- "_TtC11Translation15_LTASTextResult"
- "_TtC11Translation17_AttributeManager"
- "_TtC11Translation18TranslationSession"
- "_TtC11Translation20LanguageAvailability"
- "_URL"
- "_UUID"
- "__asrConfidenceThreshold"
- "__forcedOnlineTranslation"
- "__lidModelURL"
- "__lidThreshold"
- "__mtConfidenceThreshold"
- "__offlineASRModelURLs"
- "__offlineMTModelURL"
- "__supportsGenderDisambiguation"
- "_addAlignmentAttributesToResult:requestIdentifier:"
- "_adjacencyList"
- "_aiLocaleStatus"
- "_aiSupportedPairs"
- "_alignmentAttributeKeyFromRequestIdentifier:alignmentIdentifier:"
- "_alignments"
- "_allLocalePairsForLocales:"
- "_allowOnlineTranslation"
- "_allowsAIInference"
- "_alternatives"
- "_appIdentifier"
- "_appendAudioPCMBuffer:"
- "_appendAudioSampleBuffer:simulateRealtime:"
- "_asrConfidenceThreshold"
- "_asrModelURLs"
- "_asrResult"
- "_assets"
- "_attributedText"
- "_audioCaptureEnabled"
- "_audioChannel"
- "_audioDecoderFrom:to:"
- "_audioSessionID"
- "_audioStartHandler"
- "_autoEndpoint"
- "_autoTranslateSessionId"
- "_autodetectLanguage"
- "_batch"
- "_batchSessionUUID"
- "_beginBatchRequest:"
- "_bestAlternativeIndex"
- "_bestRecognitionAlternatives"
- "_bins"
- "_cachedLocaleStatusWithCompletion:"
- "_cachedStatus"
- "_cachedSupportedLocaleList"
- "_callCompletionHandlersWithResult:error:"
- "_callDelegateOrGiveError:forConfiguration:completion:"
- "_canUseTextService"
- "_cancelOnCleanup"
- "_cancelWithConnectionIdentifier:taskHint:useDedicatedMachPort:"
- "_cancellationStatus"
- "_category"
- "_censorSpeech"
- "_changeMapping"
- "_checkDownloadStatusForConfiguration:completion:"
- "_checkSpeakableSegmentsForResult:expectedGeneration:"
- "_checkStatusWithSourceLanguage:targetLanguage:sourceSample:completion:"
- "_checkTranslationSupportForConfiguration:completion:"
- "_cleanUp"
- "_cleanUpExistingSpeechSession"
- "_cleanUpTemporaryStorage"
- "_clearCaches"
- "_clientBundleID"
- "_clientIdentifier"
- "_closeConnectionForObserver:"
- "_closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:synchronous:"
- "_codePointsRange"
- "_codeUnitsRange"
- "_commonInit"
- "_commonInitWithSuggestedSessionID:"
- "_completedResultMap"
- "_completedUnitCount"
- "_completion"
- "_completionHandler"
- "_componentFilter"
- "_components"
- "_confidence"
- "_confidences"
- "_connectObserverIfNeeded:"
- "_connection"
- "_connectionIdentifiers"
- "_constructFinalParagraphResult"
- "_conversationID"
- "_conversationTabView"
- "_convertAndFeedPCMBuffer:"
- "_converter"
- "_count"
- "_currentGeneration"
- "_currentObservers"
- "_dataSharingOptInStatus"
- "_decoder"
- "_defaultGender"
- "_definition"
- "_delegate"
- "_deleteHotfix:"
- "_detailedModelVersion"
- "_deviceOS"
- "_deviceSupportsTranslation"
- "_deviceType"
- "_didEnterBackground:"
- "_didEnterForeground:"
- "_didFinishMultiParagraphRequestWithUUID:"
- "_didReceiveInterruption"
- "_didUpdateCachedValues"
- "_directedEdgeFromUnvalidatedEdge:"
- "_disambiguableResult"
- "_displayMode"
- "_displayName"
- "_dominantLanguage"
- "_dominantLocale"
- "_done"
- "_downloadAssetForLanguagePair:userInitiated:completion:"
- "_downloadSize"
- "_drainAndClearAudioConverter"
- "_edge"
- "_enableAirPodsOwnVAD"
- "_enableMultiFieldInput"
- "_enableOfflineStreamStabilizer"
- "_enableStreamingSpeechTranslation"
- "_enableTranslationSemanticSegmentation"
- "_enableVAD"
- "_endOfUtterance"
- "_endSent"
- "_engineType"
- "_ensureServiceConnection:useDedicatedTextMachPort:"
- "_enumerateEmojiTokensInRange:block:"
- "_eosLikelihood"
- "_errorsAsJSON"
- "_fastReadTotal:completed:"
- "_final"
- "_finalASRInputCaptureFile"
- "_finishValidating"
- "_firstParagraphComplete"
- "_firstResponse"
- "_forceSourceLocale"
- "_forcedOfflineTranslation"
- "_forcedOnlineTranslation"
- "_formattedString"
- "_fromASBD"
- "_gender"
- "_genderAlternatives"
- "_genderForLinkIndex:inPhraseIndex:"
- "_genderNumber"
- "_generateAttributedStringForLocation:result:excludedTypes:globalAttributes:attributeProvider:"
- "_generateParagraphRequests"
- "_generation"
- "_genmojiReplacementManager"
- "_getAssetSize:"
- "_getServiceProxyWithDelegate:errorHandler:block:"
- "_getStoredAttributesForRequestIdentifier:alignmentIdentifier:"
- "_getSyncServiceProxyWithDelegate:errorHandler:block:"
- "_getTextServiceProxyWithDelegate:useDedicatedTextMachPort:errorHandler:block:"
- "_group"
- "_handleError:"
- "_handleParagraphResponse:error:"
- "_handler"
- "_handlerQueue"
- "_hasCalledCompletionHandler"
- "_hasOverlapInRangeArray:"
- "_hasReceivedFirstItem"
- "_hasSpaceAfter"
- "_history"
- "_historyForEncoding"
- "_historyProvider"
- "_identifier"
- "_identifierPrefix"
- "_ignoringAttributes"
- "_inProgressMultiParagraphRequestByUUID"
- "_inProgressRequestCompletion"
- "_inProgressRequestCount"
- "_includedTypesFromDelegate"
- "_includedTypesFromExcludedTypes:"
- "_infoMap"
- "_initWithBatch:sourceLocale:targetLocale:isForDownloadRequest:itemHandler:completionHandler:"
- "_initWithSuiteName:container:"
- "_initWithTargetPhraseIndex:targetLinkIndex:type:meaningDescription:gender:defaultGender:"
- "_initWithTargetPhraseIndex:type:targetPreview:targetGender:defaultGender:menuDescription:"
- "_initWithTaskHint:engineType:useDedicatedMachPort:multicaster:observations:"
- "_initWithText:attributedText:localePair:completionHandler:"
- "_input"
- "_inputMode"
- "_inputSource"
- "_inputSubtokenCount"
- "_inputTokenCount"
- "_insertPrefix:"
- "_installationStatusWithCompletion:"
- "_installedAssets"
- "_invocationCancelledReason"
- "_invocationCancelledSELFLogging"
- "_invocationEndedError"
- "_invocationEndedWithErrorSELFLogging:"
- "_invocationId"
- "_invocationStartedSELFLogging:"
- "_invocationType"
- "_isAutoplayTranslation"
- "_isCancelled"
- "_isConfident"
- "_isFinal"
- "_isFinished"
- "_isForDownloadApprovalOnly"
- "_isForDownloadRequest"
- "_isGenderAlternativeEnabled"
- "_isHeadless"
- "_isIndeterminateProgress"
- "_isPlayTranslationsEnabled"
- "_isStable"
- "_itemHandler"
- "_labels"
- "_languageAvailability"
- "_languageIdentificationEnabled"
- "_languageStatusCompletionHandler"
- "_languageStatusListener"
- "_lastSpokenGeneration"
- "_lastStatusObservations"
- "_legacySupportedPairs"
- "_length"
- "_lidModelURL"
- "_lidResult"
- "_lidThreshold"
- "_lidUnsupportedLocale"
- "_linkIndex"
- "_links"
- "_locale"
- "_localeDetectionCount"
- "_localeIdentifier"
- "_localeList"
- "_localePair"
- "_localeProvider"
- "_localeResolver"
- "_locales"
- "_localesRequiringAppleIntelligence"
- "_localesRequiringAppleIntelligenceWithCompletion:"
- "_lock"
- "_logIdentifier"
- "_logging"
- "_lowConfidence"
- "_lowConfidenceLocales"
- "_ltAttributedStringByTrimmingCharactersInSet:"
- "_ltCompactMap:"
- "_ltCsLocaleIdentifier"
- "_ltEqual:"
- "_ltIdentifier"
- "_ltLocaleIdentifier"
- "_lt_displayNameForContext:inTargetLocale:alongsideLocales:"
- "_lt_displayNameForContext:inTargetLocale:alongsideLocales:languagesNeedingRegionInList:"
- "_lt_displaySubnameForContext:inTargetLocale:alongsideLocales:languagesNeedingRegionInList:"
- "_lt_isChinese"
- "_lt_isSimplifiedChinese"
- "_lt_isTraditionalCantonese"
- "_lt_isTraditionalChinese"
- "_lt_shouldCapitalizeDisplayNameForContext:inTargetLocale:"
- "_maxConfidence"
- "_maxPartialTranslationAttempts"
- "_maxTimeBetweenTranslations"
- "_maximumDynamicContentRequests"
- "_maximumPageLoadRequests"
- "_meaningDescription"
- "_menuDescription"
- "_metaInfo"
- "_metaInfoData"
- "_minConfidence"
- "_minNumberOfCharactersForTranslation"
- "_minTimeBetweenTranslations"
- "_modalitiesPerLocale"
- "_modelVersion"
- "_mtConfidenceThreshold"
- "_mtModelURL"
- "_mtState"
- "_multicastObservations:taskHint:engineType:progress:"
- "_multicaster"
- "_muteTTSBasedOnRingerSwitchIfPossible"
- "_needsUpdate"
- "_observations"
- "_observers"
- "_offlineASRModelURLs"
- "_offlineLanguageStatus:"
- "_offlineMTModelURL"
- "_offset"
- "_onDeviceEngineType"
- "_ongoingRequestInvocationIDs"
- "_options"
- "_originalRange"
- "_originalSubstring"
- "_output"
- "_outputFileURL"
- "_outstandingCount"
- "_outstandingRequests"
- "_overrideOngoingSessionIfNeeded"
- "_pageComplete"
- "_pageLoaded"
- "_pair"
- "_pairState"
- "_paragraphOrder"
- "_paragraphRequestForText:"
- "_paragraphRequests"
- "_paragraphResults"
- "_paragraphs"
- "_pauseCounts"
- "_phrasebookMatch"
- "_placeholderString"
- "_playbackSpeed"
- "_preToPostITN"
- "_preferOnDeviceIfAvailable"
- "_preferredEdgeFromEdgesWithDuplicateMeaning:forLinkIndex:inPhrase:"
- "_preferredGenderFromEdgesWithDuplicateMeaning:forLinkIndex:inPhrase:"
- "_preferredStrategy"
- "_preflightChecker"
- "_prepareRequest:"
- "_processIdentifier"
- "_processName"
- "_processedAudioDurationInMilliseconds"
- "_progress"
- "_progressComplete"
- "_progressHandler"
- "_purgeAllAssets:"
- "_purgeAllAssetsExcludingConfig:completion:"
- "_purgeAssetForLanguagePair:userInitiated:completion:"
- "_qssSessionId"
- "_queue"
- "_queuedBuffers"
- "_ranges"
- "_rank"
- "_rateLimiter"
- "_receivedParagraphs"
- "_reconnectIfStreamingWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:"
- "_regularExpression"
- "_removeAllLinks"
- "_removeAllObservers"
- "_removeObserver:forceCloseConnection:synchronous:"
- "_removeRomanization"
- "_removeUnvalidatedAdjacencyLists"
- "_replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:"
- "_replacementInfos"
- "_replacementRange"
- "_replayLastObservationsOnHeartbeat:"
- "_request"
- "_requestID"
- "_requestUniqueID"
- "_requestedSourceLocale"
- "_requestedTargetLocale"
- "_requiresMultiParagraphPathway"
- "_resolveLocalePairingForConfiguration:completion:"
- "_resolveSourceLocaleIfNeeded:completion:"
- "_resolveTargetLocaleIfNeeded:completion:"
- "_resolvedSourceLocale"
- "_resolvedTargetLocale"
- "_restoreChanges:"
- "_resultMap"
- "_romanization"
- "_route"
- "_safariVersion"
- "_sampleIndex"
- "_sanitizedFormattedString"
- "_sanitizedSourceString"
- "_saveAttributes:forRequestUniqueID:alignmentIdentifier:"
- "_savedAttributes"
- "_selectedLocale"
- "_selectedPhraseIndex"
- "_selfLoggingID"
- "_senseID"
- "_senses"
- "_sentence"
- "_sentences"
- "_service"
- "_session"
- "_sessionID"
- "_setInitialSupportedStatus"
- "_setQueue:"
- "_sharedQueue"
- "_shouldTranslate"
- "_signpostID"
- "_silencePosterior"
- "_simulateRealtimeBehavior:"
- "_sourceASRState"
- "_sourceAttributedText"
- "_sourceAttributes"
- "_sourceContentAsJSON"
- "_sourceIdentifier"
- "_sourceLocale"
- "_sourceMatch"
- "_sourceOrTargetLanguage"
- "_sourceOrigin"
- "_sourceRange"
- "_sourceSnippet"
- "_sourceString"
- "_sourceStrings"
- "_sourceTTSState"
- "_sourceText"
- "_sourceURL"
- "_sources"
- "_spans"
- "_spokenSegments"
- "_stable"
- "_stableSegments"
- "_stableString"
- "_start"
- "_startInstallationWithService:done:"
- "_startInvocationOptions"
- "_startTime"
- "_startTranslationWithService:done:"
- "_startTranslationWithTextService:done:"
- "_startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:"
- "_statistics"
- "_status"
- "_statusForLocale:withEngine:"
- "_statusForPair:withEngine:"
- "_statusObservers"
- "_storage"
- "_stringReplacingRedactionsInString:withMarker:"
- "_submitMessagesSELFLoggingIfNeededForInvocationStart:error:"
- "_supportedLocaleList"
- "_supportedLocaleListCompletionHandler"
- "_supportedLocaleListWithCompletion:"
- "_supportedLocalePairs"
- "_supportedLocalePairsWithCompletion:"
- "_supportedLocalePairsWithCompletionHandler:"
- "_supportedLocales"
- "_supportsGenderDisambiguation"
- "_synchronizationQueue"
- "_systemLocale"
- "_tabName"
- "_tabSessionId"
- "_targetASRState"
- "_targetAttributedText"
- "_targetContentAsJSON"
- "_targetGender"
- "_targetLinkIndex"
- "_targetLocale"
- "_targetMatch"
- "_targetPhraseIndex"
- "_targetPhrases"
- "_targetPreview"
- "_targetRange"
- "_targetTTSState"
- "_targetText"
- "_task"
- "_taskHint"
- "_test_avoidXPCConnections"
- "_text"
- "_textHandler"
- "_textRange"
- "_textTranslationHandler"
- "_textTranslator"
- "_toASBD"
- "_tokens"
- "_topLocale"
- "_totalUnitCount"
- "_traditionalLocaleStatus"
- "_trailingSilenceDuration"
- "_transcriptions"
- "_translateAppContext"
- "_translateRequest:perItemHandler:"
- "_translatedText"
- "_translatedTextWithAttributesForResult:"
- "_translationFailedWithError:"
- "_translationFinished"
- "_translationHandler"
- "_translationLIDData"
- "_translationLocalePair"
- "_translationPayload"
- "_translationQueue"
- "_translationSession"
- "_translationTTSData"
- "_translations"
- "_translator"
- "_trustedClientIdentifier"
- "_ttsPlaybackRate"
- "_type"
- "_uniqueID"
- "_uniqueLocalesFromSupportedPairs:"
- "_uniqueSupportedLanguages"
- "_unsupportedLanguageCounts"
- "_untrustedClientIdentifier"
- "_unvalidatedAdjacencyList"
- "_unvalidatedEdgeFromAdjacencyListMatchingTargetNodeIndex:"
- "_updateAllAssets:"
- "_updateCachedValues"
- "_updateHotfix:"
- "_useCellular"
- "_useDedicatedMachPort"
- "_userIdleTime"
- "_userInteractedSenses"
- "_userSelectionFromIndex:toIndex:"
- "_utteranceTranslator"
- "_validateAndPopulateEdges"
- "_validateWithAdjacencyList:gender:defaultGender:"
- "_vsLocaleIdentifier"
- "_waitingForService"
- "_webpageURL"
- "_withHandlerQueue:"
- "_word"
- "_wordCount"
- "addAttribute:value:range:"
- "addAttributes:range:"
- "addComponent:"
- "addEntriesFromDictionary:"
- "addInput:"
- "addLanguages:useCellular:"
- "addNodeIndexToHistory:"
- "addObject:"
- "addObjectsFromArray:"
- "addObservationBlock:"
- "addObserver:"
- "addObserver:selector:name:object:"
- "addReplacementInfo:"
- "addSpeechAudioData:"
- "addUserSelection:"
- "additionalLikelyPreferredLocalesForLocale:completion:"
- "allKeys"
- "allObjects"
- "allSupportedPairs"
- "allValues"
- "allocWithZone:"
- "allowOnlineTranslation"
- "allowedForRequests:"
- "allowsAIInference"
- "appBackgroundedWithPayload:localePair:"
- "append:simulateRealtime:"
- "appendAttributedString:"
- "appendAudioPCMBuffer:"
- "appendData:"
- "appendFormat:"
- "appendString:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayByAddingObject:"
- "arrayByAddingObjectsFromArray:"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "assetRequestHandler:"
- "assetRequestWithService:done:"
- "assetResponseWithProgress:finished:error:"
- "attemptToCancelRequestsWithSessionID:"
- "attributedSubstringFromRange:"
- "attributedText"
- "attributesAtIndex:effectiveRange:"
- "attributesAtIndex:longestEffectiveRange:inRange:"
- "audioStartHandler"
- "autoDetectSpeechUnsupportedPairsWithCompletion:"
- "autorelease"
- "availableLocalePairsForTask:completion:"
- "availableLocalePairsForTask:useDedicatedMachPort:completion:"
- "baseLanguageFromLanguage:"
- "batchSessionUUID"
- "beginChunkDecoderForStreamDescription:"
- "beginChunkDecoderTo48KhzPCMForStreamDescription:"
- "bestAlternativeIndex"
- "bestRecognitionAlternatives"
- "bestTranscription"
- "boolForKey:"
- "boolValue"
- "bundleForClass:"
- "bytes"
- "cachedStatus"
- "cancel"
- "cancel:"
- "cancelLanguageStatusChangeObservation:"
- "cancelPendingWork"
- "cancelWithReason:localePair:qssSessionId:"
- "canonicalIdentifier"
- "canonicalLocalePair"
- "capitalizedString"
- "capitalizedStringWithLocale:"
- "changeMapping"
- "characterDirectionForLanguage:"
- "characterSetWithCharactersInString:"
- "class"
- "cleanup"
- "clearCaches"
- "clientBundleID"
- "clientIdentifier"
- "close"
- "code"
- "combineResults:joinedWithString:"
- "combinedDisambiguableResultFromTranslationResults:joinedWithString:"
- "combinedLocaleIdentifier"
- "commonFormat"
- "compare:"
- "completion"
- "completionHandler"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "configInfoForLocale:otherLocale:completion:"
- "conformsToProtocol:"
- "containerURLForSecurityApplicationGroupIdentifier:"
- "containsAlignment"
- "containsObject:"
- "containsString:"
- "convertToBuffer:error:withInputFromBlock:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countForObject:"
- "currentLanguageStatusSnapshotWithLocaleList:completion:"
- "currentLocale"
- "d"
- "d16@0:8"
- "dataSharingOptInStatus"
- "dataWithBytes:length:"
- "dataWithContentsOfURL:"
- "dataWithJSONObject:options:error:"
- "dataWithLength:"
- "date"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeChunk:outError:"
- "decodeChunks:from:to:outError:"
- "decodeDoubleForKey:"
- "decodeInt32ForKey:"
- "decodeIntegerForKey:"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decodeTo48KHzPCMFromChunks:from:outError:"
- "defaultCenter"
- "defaultManager"
- "delegate"
- "describeObservations:"
- "description"
- "dict"
- "dictionary"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "didComplete"
- "didReceiveError:forInput:"
- "didReceiveInterruptionFromHandler:"
- "didStartTranslating"
- "didTranslateInput:withResult:"
- "disambiguableResult:didChangeResultForSentence:withSelection:"
- "disambiguableResultDidUpdate:"
- "disambiguableSentence:didSelectNode:atIndex:withSelection:"
- "discreteProgressWithIdentifier:offlineState:"
- "discreteProgressWithIdentifier:totalUnitCount:"
- "displayName"
- "displayNameForLocale:context:inTargetLocale:"
- "domain"
- "dominantUnsupportedLocale"
- "doubleValue"
- "downloadRequiresAppleIntelligence"
- "edge"
- "edgeTypes"
- "effectiveSourceLocale"
- "effectiveTargetLocale"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeInt32:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endAudio"
- "endChunkDecoding"
- "endSent"
- "endSuccessfullyWithQSSSessionId:localePair:"
- "endWithError:localePair:qssSessionId:"
- "enumerateAttribute:inRange:options:usingBlock:"
- "enumerateAttributesInRange:options:usingBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumerateTagsInRange:unit:scheme:options:usingBlock:"
- "errorWithDomain:code:userInfo:"
- "exceptionWithName:reason:userInfo:"
- "excludedTypesForDisambiguableSentence:"
- "excludedTypesForResult:"
- "extractAudioChunksFromOpusWithData:packetCount:packetDescriptions:"
- "fileURLWithPath:isDirectory:"
- "firstObject"
- "forcedOfflineTranslation"
- "format"
- "fractionCompleted"
- "frameLength"
- "genderAlternativeFromDictionary:withGroup:"
- "genderAlternatives"
- "genderAlternativesFromDictionary:"
- "genderEdgeInfoWithTargetPhraseIndex:targetLinkIndex:gender:defaultGender:"
- "genderEdgeWithTargetPhraseIndex:targetPreview:gender:defaultGender:"
- "genderNumber"
- "generateAttributedStringForLocation:withGlobalAttributes:attributeProvider:"
- "generateSilentAudioDataWithDuration:"
- "get48khzPCMDescription"
- "getBytes:range:"
- "handler"
- "handlerQueue"
- "hasAnyChangeOfType:"
- "hasComponents"
- "hasDisambiguations"
- "hasDisambiguationsOfType:"
- "hasPrefix:"
- "hasSpaceAfter"
- "hasSuffix:"
- "hash"
- "historyProvider"
- "hybridEndpointerFoundEndpoint"
- "identifierForDownloads"
- "identifierPrefix"
- "ignoringAttributes"
- "indexOfObject:"
- "indexOfObjectPassingTest:"
- "infoDictionary"
- "init"
- "initForDownloadRequestWithSourceLocale:targetLocale:completionHandler:"
- "initForFutureServiceWithSessionID:selfLoggingInvocationId:"
- "initForWriting:settings:commonFormat:interleaved:error:"
- "initFromFormat:toFormat:"
- "initWithASRResult:"
- "initWithArray:"
- "initWithArray:copyItems:"
- "initWithAttributedString:"
- "initWithAttributedString:localePair:completionHandler:"
- "initWithBatch:sourceLocale:targetLocale:itemHandler:completionHandler:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithDictionary:"
- "initWithDictionary:copyItems:"
- "initWithDisplayMode:localePair:isGenderAlternativeEnabled:tabName:tabSessionId:conversationTabView:isPlayTranslationsEnabled:autoTranslateSessionId:audioChannel:languageIdentificationEnabled:"
- "initWithEdge:sourceSnippet:linkIndex:"
- "initWithFormattedString:locale:confidence:minConfidence:maxConfidence:"
- "initWithIdentifier:codePointsRange:codeUnitsRange:"
- "initWithIdentifier:codePointsRange:codeUnitsRange:shouldTranslate:metaInfoData:"
- "initWithIdentifier:offlineState:"
- "initWithIdentifier:sourceRange:targetRange:targetText:shouldTranslate:"
- "initWithIdentifier:text:shouldTranslate:"
- "initWithIdentifier:text:spans:"
- "initWithIdentifier:text:spans:isFinal:"
- "initWithIdentifier:totalUnitCount:completedUnitCount:"
- "initWithInstallationStatus:"
- "initWithInvocationId:"
- "initWithInvocationId:inputSource:topLocale:lowConfidenceLocales:"
- "initWithLanguageAssets:options:progress:completion:"
- "initWithLength:"
- "initWithLocale:"
- "initWithLocale:progress:"
- "initWithLocale:progress:downloadSize:status:rank:"
- "initWithLocale:progress:downloadSize:status:sources:rank:"
- "initWithLocale:state:"
- "initWithLocaleIdentifier:"
- "initWithLocaleIdentifier:offlineState:"
- "initWithLocaleIdentifier:progress:"
- "initWithLocaleList:"
- "initWithLocalePair:"
- "initWithLocalePair:completion:"
- "initWithLocalePair:offlineMTModel:taskHint:"
- "initWithLocalePair:sourceAttributedText:targetAttributedText:clientIdentifier:"
- "initWithLocalePair:sourceText:targetText:clientIdentifier:"
- "initWithLocalePair:suggestedUniqueID:"
- "initWithLocales:"
- "initWithLocales:useCellular:"
- "initWithLocales:useCellular:delegate:"
- "initWithLocales:useCellular:progressHandler:"
- "initWithMachServiceName:options:"
- "initWithMaximumPageLoadRequest:maximumDynamicContentRequests:"
- "initWithMinTimeBetweenTranslations:maxTimeBetweenTranslations:userIdleTime:maxPartialTranslationAttempts:minNumberOfCharactersForTranslation:"
- "initWithModalitiesPerLocale:"
- "initWithObservationType:useDedicatedMachPort:observations:"
- "initWithOriginalRange:replacementRange:requestID:originalSubstring:placeholderString:"
- "initWithOutput:stableSegments:"
- "initWithPCMFormat:frameCapacity:"
- "initWithParagraphResults:localePair:"
- "initWithPreferredStrategy:"
- "initWithSentences:"
- "initWithSentences:joinedWithString:"
- "initWithServiceName:options:"
- "initWithSession:request:supportedLocalePairs:"
- "initWithSessionID:taskHint:localePair:deviceOS:deviceType:appIdentifier:"
- "initWithSourceAttributedText:clientIdentifier:"
- "initWithSourceIdentifier:targetIdentifier:"
- "initWithSourceLocale:targetLocale:"
- "initWithSourceLocale:targetLocale:handlerQueue:"
- "initWithSourceLocale:targetLocale:preferredStrategy:"
- "initWithSourceLocale:targetLocale:preferredStrategy:isHeadless:"
- "initWithSourceLocale:targetLocale:suggestedUniqueID:"
- "initWithSourceOrTargetLanguage:isAutoplayTranslation:ttsPlaybackSpeed:audioChannel:"
- "initWithSourceRange:targetRange:adjacencyList:gender:defaultGender:"
- "initWithSourceRange:targetRange:unvalidatedAdjacencyList:"
- "initWithSourceStrings:supportedLocalePairs:"
- "initWithSourceText:clientIdentifier:"
- "initWithSourceText:sourceSnippet:targetText:targetSnippet:adjacencyList:gender:defaultGender:"
- "initWithSourceText:sourceSnippet:targetText:targetSnippet:unvalidatedAdjacencyList:"
- "initWithSourceText:targetPhrases:selectedPhraseIndex:"
- "initWithStreamDescription:"
- "initWithString:"
- "initWithSupportedLocales:"
- "initWithSupportedLocales:asrLocales:ttsLocales:"
- "initWithTagSchemes:"
- "initWithTask:inputMode:invocationType:translateAppContext:"
- "initWithTaskHint:engineType:useDedicatedMachPort:observations:"
- "initWithTaskHint:useDedicatedMachPort:observations:"
- "initWithText:confidence:"
- "initWithText:isFinal:"
- "initWithText:links:romanization:"
- "initWithText:locale:"
- "initWithText:localePair:completionHandler:"
- "initWithText:sourceText:locale:isFinal:sourceIdentifier:"
- "initWithTranslator:selfLoggingInvocationId:"
- "initWithType:invocationId:"
- "initWithUnit:"
- "initialize"
- "inputDidFinish"
- "inputFormat"
- "installOfflineLocales:completion:"
- "installationStatus"
- "installedLocales:"
- "installedLocalesForTask:completion:"
- "int16ChannelData"
- "intValue"
- "integerValue"
- "interfaceWithProtocol:"
- "interruptionController"
- "interruptionHandler"
- "intersectSet:"
- "intersectsSet:"
- "invalidate"
- "invertedSet"
- "isBidirectionalEqual:"
- "isCancelled"
- "isEqual:"
- "isEqualToArray:"
- "isEqualToString:"
- "isFinished"
- "isForDownloadRequest"
- "isGenderDisambiguationEnabled"
- "isInterleaved"
- "isKindOfClass:"
- "isLowConfidence"
- "isMemberOfClass:"
- "isPassthrough"
- "isPhrasebookMatch"
- "isProxy"
- "isTranslationSupportedOnCurrentDeviceForPreflightChecker:"
- "isValidJSONObject:"
- "isVariantPair"
- "jsonRepresentation"
- "keyEnumerator"
- "keyboardsForFilter:"
- "languageAssetsWithOptions:completion:"
- "languageAvailabilityDidUpdate:"
- "languageCode"
- "languageDetectionCompleted"
- "languageDetectionResult:"
- "languageForText:completion:"
- "languageIdentificationCompletedWithInputSource:topLocale:lowConfidenceLocales:"
- "languageIdentifier"
- "languageInstallProgressed:error:"
- "languageStatusChangedForTaskHint:engineType:progress:observations:"
- "languagesForText:completion:"
- "languagesForText:usingModel:completion:"
- "languagesForText:usingModel:strategy:taskHint:completion:"
- "languagesForText:usingModel:strategy:taskHint:useDedicatedTextMachPort:completion:"
- "languagesForText:usingModel:strategy:useDedicatedTextMachPort:completion:"
- "languagesForText:usingModel:useDedicatedTextMachPort:completion:"
- "lastObject"
- "launchAppWithCompletionHandler:"
- "linkIndex"
- "locale:supportsModality:"
- "localeList"
- "localePairsForStrategy:"
- "localeProvider"
- "localeProviderSupportedLocaleListWithCompletion:"
- "localeResolver"
- "localeWithLocaleIdentifier:"
- "localesExclusiveToStrategy:"
- "localizedDescription"
- "localizedStringForKey:value:table:"
- "localizedStringForLanguage:context:"
- "localizedStringForLanguageCode:"
- "localizedStringForRegion:context:short:"
- "log:"
- "logWithRequestData:"
- "loggingType"
- "lowercaseStringWithLocale:"
- "lt_appGroupDefaults"
- "lt_attributedStringByJoiningComponents:withAttributedString:"
- "lt_attributedStringByJoiningComponents:withString:"
- "lt_bestMatchForPreferredLocales:fromSupportedLocales:"
- "lt_bestMatchesForPreferredLocales:fromSupportedLocales:"
- "lt_codePointsRangeFromCodeUnitsRange:"
- "lt_codeUnitsRangeFromCodePointsRange:"
- "lt_containsSubstringWithAttribute:"
- "lt_defaultTargetForSource:systemLocale:availableLocales:targetMap:"
- "lt_displayNameForContext:inTargetLocale:"
- "lt_displaySubnameForContext:inTargetLocale:"
- "lt_ensureElementType:"
- "lt_ensureTypesForKeys:values:"
- "lt_errorWithCode:description:userInfo:"
- "lt_fallbackForLocale:"
- "lt_filterUsingBlock:"
- "lt_firstObjectPassingTest:"
- "lt_hasObjectPassingTest:"
- "lt_invalidRequestErrorWithDescription:"
- "lt_isWhiteSpaceOnlyString"
- "lt_localeIdentifier"
- "lt_localeWithLTIdentifier:"
- "lt_nlLanguageCode"
- "lt_offlineNotImplementedError"
- "lt_onlineNotImplementedError"
- "lt_preferredLocales"
- "lt_sentences"
- "lt_speechLimitExceeded"
- "lt_speechTranslationOngoing"
- "lt_stringArrayDebugDescription:"
- "lt_suffixWithMaxLength:"
- "lt_translationTimeout"
- "lt_unsupportedLanguageError:"
- "lt_unsupportedPairingErrorWithSource:target:"
- "lt_unsupportedSourceLanguageError:"
- "lt_unsupportedTargetLanguageError:"
- "lt_validSubrange:"
- "lt_wordRangesWithLocale:"
- "lt_wordRangesWithoutOmittingPunctuationWithLocale:"
- "mainBundle"
- "markFirstParagraphComplete"
- "markPageComplete"
- "markPageLoaded"
- "markProgressDone"
- "markResponse"
- "matchedLanguagesFromAvailableLanguages:forPreferredLanguages:"
- "maximumDynamicContentRequests"
- "maximumPageLoadRequests"
- "meaningDescription"
- "meaningDescriptionForLinkIndex:inTargetPhrase:"
- "meaningEdgeInfoWithTargetPhraseIndex:targetLinkIndex:meaningDescription:"
- "meaningEdgeWithTargetPhraseIndex:targetPreview:meaningDescription:targetGender:defaultGender:"
- "menuConfigurationsForLinkIndex:"
- "metaInfo"
- "minusSet:"
- "modalitiesForLocale:"
- "modalitiesPerLocaleWithCompletion:"
- "mutableAudioBufferList"
- "mutableBytes"
- "mutableCopy"
- "nativeAudioFormat"
- "needsUserInterventionForTextSession:configuration:completion:"
- "nextStep"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForInfoDictionaryKey:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observations"
- "observers"
- "offlineMTModelURL"
- "offlineState"
- "onDeviceModeEnabled:"
- "onDeviceModeEnabledWithDedicatedMachPort:completion:"
- "onDeviceModeSupported:"
- "opaqueSessionID"
- "oppositeToLocale:"
- "originalRange"
- "originalSubstring"
- "pairNamesForLocaleIdentifiers:"
- "pairNamesForLocales:"
- "pairWithIdentifiers:"
- "paragraphRequests"
- "paragraphTranslation:result:error:"
- "paragraphs"
- "path"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "phrasebookMatch"
- "placeholderString"
- "preToPostITN"
- "preferOnDeviceIfAvailable"
- "preferredLanguages"
- "preferredLanguagesForFilter:"
- "preflightChecker"
- "preflightChecker:continueCheckingFromStep:forConfiguration:completion:"
- "preflightConfiguration:completion:"
- "preheatForRequest:completion:"
- "preheatForRequestSync:"
- "preheatWithContext:completion:"
- "prepareDownloadsWithCompletion:"
- "prepareWithService:"
- "processIdentifier"
- "processInfo"
- "progressHandler"
- "propertyListWithData:options:format:error:"
- "provideFeedback:"
- "provideFeedback:withContext:"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "qssSessionID"
- "raise"
- "rangeOfCharacterFromSet:"
- "rangeOfCharacterFromSet:options:"
- "rangeOfFirstMatchInString:options:range:"
- "rangeOfString:"
- "rangeValue"
- "ranges"
- "rareEmojiPlaceholderCandidates"
- "rateLimiter"
- "recommendedLocales"
- "regionCode"
- "regularExpressionWithPattern:options:error:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllComponents"
- "removeAllObjects"
- "removeComponent:"
- "removeLanguages:"
- "removeLastObject"
- "removeObject:"
- "removeObjectForKey:"
- "removeObserver:"
- "replaceCharactersInRange:withString:"
- "replaceMatchesInString:options:range:withTemplate:"
- "replacementInfoForRequestID:"
- "replacementInfos"
- "replacementRange"
- "requestContext"
- "requestUniqueID"
- "requiredLocalesForFilter:"
- "requiresMultiParagraphPathway"
- "reset"
- "resolveSourceLocaleForConfiguration:completion:"
- "resolveTargetLocaleIfNeeded:completion:"
- "respondsToSelector:"
- "restoreChangesToResult:"
- "resume"
- "retain"
- "retainCount"
- "reverseObjectEnumerator"
- "reversedPair"
- "sanitizedCopyForUntrustedTextTranslation"
- "scriptCode"
- "selectedTargetPhrase"
- "self"
- "selfLoggingEventWithData:"
- "selfLoggingInvocationCancelledForIDs:"
- "selfLoggingInvocationDidError:invocationId:"
- "selfLoggingInvocationStartedWithData:invocationStartedTier1Data:"
- "selfLoggingLanguageIdentificationCompletedWithLIDData:"
- "sendEventWithPayload:localePair:type:"
- "sendUserEndedTypingEventWithPayload:localePair:type:"
- "senseFromDictionary:"
- "senseID"
- "senseWithPhrasebookMatchMeta:"
- "sensesFromArray:"
- "sentence"
- "sentenceWithUUID:"
- "serverEndpointerFeatures:locale:"
- "service"
- "serviceDelegate"
- "set"
- "setAlignments:"
- "setAllowOnlineTranslation:"
- "setAllowsAIInference:"
- "setAlternatives:"
- "setAppIdentifier:"
- "setAsrConfidenceThreshold:"
- "setAsrModelURLs:"
- "setAttributedText:"
- "setAttributes:range:"
- "setAudioChannel:"
- "setAudioSessionID:"
- "setAudioStartHandler:"
- "setAutoEndpoint:"
- "setAutodetectLanguage:"
- "setBatchSessionUUID:"
- "setBestAlternativeIndex:"
- "setBestRecognitionAlternatives:"
- "setBins:"
- "setCancelOnCleanup:"
- "setCategory:"
- "setCensorSpeech:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCleanUpExistingSpeechSession:"
- "setClientBundleID:"
- "setCompletionHandler:"
- "setComponentFilter:"
- "setConfidence:"
- "setConfidences:"
- "setConversationID:"
- "setDataSharingOptInStatus:"
- "setDateFormat:"
- "setDefaultGender:"
- "setDefinition:"
- "setDelegate:"
- "setDetailedModelVersion:"
- "setDeviceSupportsTranslation:"
- "setDisambiguableResult:"
- "setDominantLanguage:"
- "setDominantLocale:"
- "setEnableAirPodsOwnVAD:"
- "setEnableMultiFieldInput:"
- "setEnableOfflineStreamStabilizer:"
- "setEnableStreamingSpeechTranslation:"
- "setEnableTranslationSemanticSegmentation:"
- "setEnableVAD:"
- "setEndOfUtterance:"
- "setEndSent:"
- "setEosLikelihood:"
- "setErrorsAsJSON:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFinal:"
- "setForceSourceLocale:"
- "setForcedOfflineTranslation:"
- "setFormattedString:"
- "setFrameLength:"
- "setGenderAlternatives:"
- "setGeneration:"
- "setGreaterThanOrEqualToOfflineState:"
- "setGroup:"
- "setHandler:"
- "setHandlerQueue:"
- "setHasSpaceAfter:"
- "setHistoryProvider:"
- "setIdentifier:"
- "setIgnoringAttributes:"
- "setInput:"
- "setInputSource:"
- "setInputSubtokenCount:"
- "setInputTokenCount:"
- "setInterruptionHandler:"
- "setInvocationCancelledReason:"
- "setInvocationEndedError:"
- "setIsAutoplayTranslation:"
- "setIsConfident:"
- "setIsFinal:"
- "setIsForDownloadApprovalOnly:"
- "setIsHeadless:"
- "setIsStable:"
- "setLabels:"
- "setLanguage:range:"
- "setLanguageAssets:options:progress:completion:"
- "setLength:"
- "setLidResult:"
- "setLidThreshold:"
- "setLidUnsupportedLocale:"
- "setLocale:"
- "setLocaleDetectionCount:"
- "setLocaleIdentifier:"
- "setLocalePair:"
- "setLocaleProvider:"
- "setLocaleResolver:"
- "setLocales:"
- "setLocales:forStrategy:"
- "setLocalesRequiringAppleIntelligence:"
- "setLogIdentifier:"
- "setLowConfidence:"
- "setLowConfidenceLocales:"
- "setMaxConfidence:"
- "setMaximumDynamicContentRequests:"
- "setMaximumPageLoadRequests:"
- "setMetaInfo:"
- "setMetaInfoData:"
- "setMinConfidence:"
- "setModelVersion:"
- "setMtModelURL:"
- "setMtState:"
- "setMuteTTSBasedOnRingerSwitchIfPossible:"
- "setNeedsUpdate:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOfflineState:"
- "setOffset:"
- "setOnDeviceEngineType:"
- "setOutputFileURL:"
- "setOverrideOngoingSessionIfNeeded:"
- "setPair:"
- "setPairState:"
- "setParagraphs:"
- "setPauseCounts:"
- "setPhrasebookMatch:"
- "setPlaybackSpeed:"
- "setPreToPostITN:"
- "setPreferOnDeviceIfAvailable:"
- "setPreferredStrategy:"
- "setProcessIdentifier:"
- "setProcessName:"
- "setProcessedAudioDurationInMilliseconds:"
- "setProgress:"
- "setProgressHandler:"
- "setQssSessionId:"
- "setRanges:"
- "setRateLimiter:"
- "setRemoteObjectInterface:"
- "setReplacementInfos:"
- "setRequestID:"
- "setRequestedSourceLocale:"
- "setRequestedTargetLocale:"
- "setRequiresMultiParagraphPathway:"
- "setResolvedSourceLocale:"
- "setResolvedTargetLocale:"
- "setRomanization:"
- "setRoute:"
- "setSafariVersion:"
- "setSampleIndex:"
- "setSampleRateConverterQuality:"
- "setSanitizedFormattedString:"
- "setSanitizedSourceString:"
- "setSelectedLocale:"
- "setSelectedPhraseIndex:"
- "setSelfLoggingID:"
- "setSenseID:"
- "setSenses:"
- "setSentence:"
- "setService:"
- "setSessionID:"
- "setShouldTranslate:"
- "setSilencePosterior:"
- "setSourceASRState:"
- "setSourceAttributes:"
- "setSourceContentAsJSON:"
- "setSourceIdentifier:"
- "setSourceMatch:"
- "setSourceOrTargetLanguage:"
- "setSourceOrigin:"
- "setSourceRange:"
- "setSourceString:"
- "setSourceTTSState:"
- "setSourceURL:"
- "setStable:"
- "setStableString:"
- "setStartInvocationOptions:"
- "setStartTime:"
- "setStatistics:"
- "setStatus:forLocale:withEngine:"
- "setString:"
- "setSupportedPairs:forStrategy:"
- "setSupportsGenderDisambiguation:"
- "setSystemLocale:"
- "setTargetASRState:"
- "setTargetContentAsJSON:"
- "setTargetLocale:"
- "setTargetMatch:"
- "setTargetRange:"
- "setTargetTTSState:"
- "setTaskHint:"
- "setTest_avoidXPCConnections:"
- "setText:"
- "setTextHandler:"
- "setTextRange:"
- "setTextTranslationHandler:"
- "setTextTranslator:"
- "setTokens:"
- "setTopLocale:"
- "setTrailingSilenceDuration:"
- "setTranscriptions:"
- "setTranslationHandler:"
- "setTranslationLIDData:"
- "setTranslationLocalePair:"
- "setTranslationPayload:"
- "setTranslationQueue:"
- "setTranslationTTSData:"
- "setTranslations:"
- "setTranslator:"
- "setTrustedClientIdentifier:"
- "setTtsPlaybackRate:"
- "setURL:"
- "setUniqueID:"
- "setUnsupportedLanguageCounts:"
- "setUntrustedClientIdentifier:"
- "setUpAudioCaptureFile:withFormat:"
- "setUseCellular:"
- "setUserInteractedSenses:"
- "setUtteranceTranslator:"
- "setWebpageURL:"
- "setWithArray:"
- "setWord:"
- "setWordCount:"
- "set_asrConfidenceThreshold:"
- "set_forcedOnlineTranslation:"
- "set_lidModelURL:"
- "set_lidThreshold:"
- "set_mtConfidenceThreshold:"
- "set_offlineASRModelURLs:"
- "set_offlineMTModelURL:"
- "set_supportsGenderDisambiguation:"
- "settings"
- "shared"
- "sharedInstance"
- "shouldPresentSystemFirstUseConsent:"
- "shouldPresentSystemFirstUseConsentWithDedicatedMachPort:completion:"
- "sleepForTimeInterval:"
- "sortedArrayUsingComparator:"
- "sortedArrayUsingSelector:"
- "sourceAttributedText"
- "sourceAttributes"
- "sourceLanguage"
- "sourceSnippet"
- "sourceTextSnippetForLinkIndex:"
- "speak:withContext:completion:"
- "speechActivityDetected"
- "speechRecognitionResult:"
- "splitIntoSentences"
- "standardUserDefaults"
- "startInstallRequest:"
- "startInvocationWithTask:inputMode:invocationType:translateAppContext:"
- "startLanguageStatusChangeObservation:taskHint:engineType:completion:"
- "startPersonalTranslationSession:"
- "startSpeechTranslationWithContext:"
- "startTextToSpeechTranslationWithContext:text:"
- "startTranslationSession"
- "startTranslationSessionWithSELFLoggingInvocationId:"
- "startedWithClientIdentifier:"
- "state"
- "statusForSourceSample:toLanguage:completion:"
- "statusFromLanguage:toLanguage:completion:"
- "statusFromSingleEngineForPair:"
- "string"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringContainsRedaction:"
- "stringForKey:"
- "stringFromDate:"
- "stringReplacingRedactionsWithBeepMarker:"
- "stringWithFormat:"
- "stringWithString:"
- "strongToWeakObjectsMapTable"
- "subarrayWithRange:"
- "subdataWithRange:"
- "substringWithRange:"
- "superclass"
- "supportedLanguagesWithCompletion:"
- "supportedLocalePairsWithCompletion:"
- "supportedLocales"
- "supportsLocalePair:forStrategy:"
- "supportsSecureCoding"
- "synchronizationQueue"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "systemUptime"
- "targetAttributedText"
- "targetLanguage"
- "targetLinkIndex"
- "targetText"
- "task:isSupportedInCountry:completion:"
- "taskIsSupportedInCurrentRegion:completion:"
- "test_avoidXPCConnections"
- "textHandler"
- "textStreamingConfigurationWithCompletion:"
- "textTranslationHandler"
- "textTranslator"
- "tokensForRange:"
- "translate:"
- "translate:useDedicatedTextMachPort:"
- "translate:withContext:completion:"
- "translateAttributedString:completionHandler:"
- "translateBatch:itemHandler:completionHandler:"
- "translateInput:withGeneration:completion:"
- "translateParagraphs:withContext:completion:"
- "translateRequest:forSession:perItemHandler:"
- "translateSentence:withContext:completion:"
- "translateStreamingInput:withContext:completion:"
- "translateString:completionHandler:"
- "translationDidFinishWithError:"
- "translationHandler"
- "translationParagraph"
- "translationQueue"
- "translationTTSPlayedWithInvocationId:sourceOrTargetLanguage:isAutoplayTranslation:ttsPlaybackSpeed:audioChannel:"
- "translator"
- "translator:didEncounterError:"
- "translator:didProduceSpeakableOutput:"
- "translator:didProduceTranslatedOutputs:"
- "translatorDidFinish:"
- "translatorDidTranslate:"
- "trimPrependingPunctuation:locale:"
- "trustedClientIdentifier"
- "ttsAudioStarted:duration:"
- "underlyingAvailability"
- "underlyingTextSession"
- "unionSet:"
- "unredactedDescription"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsupportedLanguageCounts"
- "unvalidatedAdjacencyList"
- "updateMinTimeBetweenTranslations:maxTimeBetweenTranslations:userIdleTime:"
- "updateOVADStreamingState:"
- "updatePercentComplete:"
- "updateTotalUnitCount:completedUnitCount:"
- "userEndedTypingWithInvocationId:payload:localePair:reason:"
- "userEndedTypingWithPayload:localePair:reason:"
- "userInfo"
- "utteranceTranslator"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSData\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"NSNumber\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@\"NSUUID\"16"
- "v24@0:8@\"_LTInstallRequest\"16"
- "v24@0:8@\"_LTInterruptionHandler\"16"
- "v24@0:8@\"_LTLanguageAssetRequest\"16"
- "v24@0:8@\"_LTLanguageDetectionResult\"16"
- "v24@0:8@\"_LTSELFLoggingEventData\"16"
- "v24@0:8@\"_LTSELFLoggingTranslationLIDData\"16"
- "v24@0:8@\"_LTSpeechRecognitionResult\"16"
- "v24@0:8@\"_LTTranslationContext\"16"
- "v24@0:8@\"_LTTranslationResult\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSNumber\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"_LTLocaleModalities\">16"
- "v24@0:8@?<v@?@\"_LTSupportedLocaleList\">16"
- "v24@0:8@?<v@?@\"_LTTextStreamingConfiguration\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v24@?0@\"_LTTextResult\"8@\"NSError\"16"
- "v28@0:8@\"NSArray\"16B24"
- "v28@0:8@16B24"
- "v28@0:8@?16B24"
- "v28@0:8B16@20"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\">20"
- "v28@0:8^{opaqueCMSampleBuffer=}16B24"
- "v32@0:8@\"NSArray\"16@\"NSError\"24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"_LTTextLanguageDetectionResult\">24"
- "v32@0:8@\"NSArray\"16d24"
- "v32@0:8@\"NSError\"16@\"NSUUID\"24"
- "v32@0:8@\"NSLocale\"16@?<v@?@\"NSArray\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"_LTLanguageDetectionResult\">24"
- "v32@0:8@\"_LTPreflightConfiguration\"16@?<v@?@\"NSLocale\"@\"NSArray\">24"
- "v32@0:8@\"_LTSELFLoggingEventData\"16@\"_LTSELFLoggingEventData\"24"
- "v32@0:8@\"_LTServerEndpointerFeatures\"16@\"NSLocale\"24"
- "v32@0:8@\"_LTSupportedLocaleList\"16@?<v@?@\"_LTLanguageStatusSnapshot\">24"
- "v32@0:8@\"_LTTranslationContext\"16@\"NSString\"24"
- "v32@0:8@\"_LTTranslationContext\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"_LTTranslationFeedback\"16@\"_LTTaskContext\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16B24B28"
- "v32@0:8@16d24"
- "v32@0:8@16q24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8^q16^q24"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?@\"NSArray\">24"
- "v32@0:8{_NSRange=QQ}16"
- "v36@0:8@\"NSArray\"16B24@\"NSError\"28"
- "v36@0:8@\"_LTLocalePair\"16B24@?<v@?@\"NSError\">28"
- "v36@0:8@16B24@28"
- "v36@0:8@16B24@?28"
- "v36@0:8@16q24B32"
- "v36@0:8q16B24@?28"
- "v40@0:8@\"NSArray\"16@\"_LTTranslationContext\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSLocale\"16@\"NSLocale\"24@?<v@?@\"NSDictionary\">32"
- "v40@0:8@\"NSString\"16@\"_LTTranslationContext\"24@?<v@?@\"NSURL\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"_LTTranslationContext\"24@?<v@?@\"_LTTranslationResult\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"_LTTranslationResult\"24@\"NSError\"32"
- "v40@0:8@\"_LTStreamingInput\"16@\"_LTTranslationContext\"24@?<v@?@\"_LTStabilizationTranslationResult\"@\"NSError\">32"
- "v40@0:8@\"_LTStreamingInput\"16q24@?<v@?@\"_LTStabilizationTranslationResult\"@\"NSError\">32"
- "v40@0:8@\"_LTTextSessionRequest\"16@\"_LTTextSession\"24@?<v@?@\"_LTTextResult\"Q@\"NSError\">32"
- "v40@0:8@\"_LTTranslationParagraph\"16@\"_LTTranslationContext\"24@?<v@?@\"_LTTranslationResult\"@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24q32"
- "v40@0:8@16@?24@?32"
- "v40@0:8@16Q24@?32"
- "v40@0:8@16q24@?32"
- "v40@0:8Q16@24q32"
- "v40@0:8d16d24d32"
- "v40@0:8q16@\"NSString\"24@?<v@?B>32"
- "v40@0:8q16@24@32"
- "v40@0:8q16@24@?32"
- "v44@0:8@16B24@?28@?36"
- "v44@0:8@16Q24B32@?36"
- "v44@0:8@16q24q32B40"
- "v44@0:8q16q24B32@\"NSArray\"36"
- "v44@0:8q16q24B32@36"
- "v48@0:8@\"NSUUID\"16q24q32@?<v@?@\"NSError\">40"
- "v48@0:8@\"_LTDisambiguableSentence\"16@\"_LTDisambiguationNode\"24Q32@\"_LTDisambiguationUserSelection\"40"
- "v48@0:8@\"_LTPreflightChecker\"16q24@\"_LTPreflightConfiguration\"32@?<v@?@\"_LTPreflightConfiguration\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24@32q40"
- "v48@0:8@16@24Q32@40"
- "v48@0:8@16Q24@?32@?40"
- "v48@0:8@16q24@32@?40"
- "v48@0:8@16q24q32@?40"
- "v52@0:8@16Q24Q32B40@?44"
- "v52@0:8@16q24B32q36q44"
- "v52@0:8B16@20q28q36B44B48"
- "v56@0:8@\"NSArray\"16Q24Q32q40@?<v@?@\"_LTTextLanguageDetectionResult\">48"
- "v56@0:8@16Q24Q32q40@?48"
- "v60@0:8@16Q24Q32q40B48@?52"
- "valueWithRange:"
- "vs_stringFrom4CC:"
- "weakObjectsHashTable"
- "whitespaceAndNewlineCharacterSet"
- "writeFromBuffer:error:"
- "zone"
- "{AudioStreamBasicDescription=\"mSampleRate\"d\"mFormatID\"I\"mFormatFlags\"I\"mBytesPerPacket\"I\"mFramesPerPacket\"I\"mBytesPerFrame\"I\"mChannelsPerFrame\"I\"mBitsPerChannel\"I\"mReserved\"I}"
- "{AudioStreamBasicDescription=dIIIIIIII}16@0:8"
- "{_NSRange=\"location\"Q\"length\"Q}"
- "{_NSRange=QQ}16@0:8"
- "{_NSRange=QQ}32@0:8{_NSRange=QQ}16"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
