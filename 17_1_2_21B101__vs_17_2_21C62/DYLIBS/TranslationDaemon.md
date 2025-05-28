## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

-252.2.1.0.0
-  __TEXT.__text: 0x18db74
-  __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_methlist: 0x18a74
-  __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x4e72
-  __TEXT.__oslogstring: 0x8893
-  __TEXT.__gcc_except_tab: 0x19c38
-  __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0xfa70
+252.11.0.0.0
+  __TEXT.__text: 0x18f5f0
+  __TEXT.__auth_stubs: 0xce0
+  __TEXT.__objc_methlist: 0x18aac
+  __TEXT.__const: 0x250
+  __TEXT.__cstring: 0x4f63
+  __TEXT.__oslogstring: 0x8b99
+  __TEXT.__gcc_except_tab: 0x19cd0
+  __TEXT.__dlopen_cstrs: 0xb2
+  __TEXT.__unwind_info: 0xfaa4
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x4858
-  __TEXT.__objc_methname: 0x18769
-  __TEXT.__objc_methtype: 0xe022
-  __TEXT.__objc_stubs: 0x104c0
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x3428
+  __TEXT.__objc_classname: 0x485b
+  __TEXT.__objc_methname: 0x18947
+  __TEXT.__objc_methtype: 0xe078
+  __TEXT.__objc_stubs: 0x105e0
+  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__const: 0x3508
   __DATA_CONST.__objc_classlist: 0x11e0
   __DATA_CONST.__objc_catlist: 0x118
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1ff08
-  __DATA_CONST.__objc_selrefs: 0x5cf0
-  __DATA_CONST.__objc_arraydata: 0xa0
+  __DATA_CONST.__objc_const: 0x1ffa8
+  __DATA_CONST.__objc_selrefs: 0x5d38
+  __DATA_CONST.__objc_arraydata: 0x80
   __AUTH_CONST.__objc_const: 0xc9f8
-  __AUTH_CONST.__cfstring: 0x6960
-  __AUTH_CONST.__const: 0x6e0
+  __AUTH_CONST.__cfstring: 0x69c0
+  __AUTH_CONST.__const: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__objc_intobj: 0x150
+  __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x670
+  __AUTH_CONST.__auth_got: 0x688
   __AUTH.__objc_data: 0xa960
   __DATA.__objc_classrefs: 0x10f0
   __DATA.__objc_superrefs: 0x1170
-  __DATA.__objc_ivar: 0x10d0
+  __DATA.__objc_ivar: 0x10e4
   __DATA.__data: 0x8f0
-  __DATA.__bss: 0xe0
+  __DATA.__bss: 0xf0
   __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__bss: 0x148
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage
   - /System/Library/Frameworks/SoundAnalysis.framework/SoundAnalysis
-  - /System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10225
-  Symbols:   32573
-  CStrings:  7343
+  Functions: 10245
+  Symbols:   32639
+  CStrings:  7382
 
Symbols:
+ +[_LTDAssetService _installConfigAsset:completion:].cold.3
+ +[_LTOfflineTranslationEngine _needToWaitForBothFinalTranslationResultsWithContext:lidResult:]
+ +[_LTWordTimingInfo(Daemon) smoothedWordTimingWithTextRangeInfoFrom:wordTimingInfo:]
+ +[_LTWordTimingInfo(Daemon) smoothedWordTimingWithTextRangeInfoFrom:wordTimingInfo:].cold.1
+ +[_LTWordTimingInfo(Daemon) wordTimingInfoFromSiriTTSService:text:]
+ -[_LTAudioDecoder decodeTo48KHzPCMFromChunks:from:outError:]
+ -[_LTAudioDecoder extractAudioChunksFromOpusWithData:packetCount:packetDescriptions:]
+ -[_LTAudioDecoder extractAudioChunksFromOpusWithData:packetCount:packetDescriptions:].cold.1
+ -[_LTAudioDecoder get48khzPCMDescription]
+ -[_LTLanguageDetector isLowConfidencePair]
+ -[_LTLanguageDetectorFeatureCombinationModel estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:isLowConfidencePair:]
+ -[_LTLanguageDetectorFeatureCombinationModel estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:useFinalThresholds:isLowConfidencePair:]
+ -[_LTLanguageDetectorFeatureCombinationModel estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:useFinalThresholds:isLowConfidencePair:].cold.1
+ -[_LTLanguageDetectorFeatureCombinationModel estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:useFinalThresholds:isLowConfidencePair:].cold.2
+ -[_LTLanguageDetectorFeatureCombinationModel estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:useFinalThresholds:isLowConfidencePair:].cold.3
+ -[_LTLanguageDetectorFeatureCombinationModel estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:useFinalThresholds:isLowConfidencePair:].cold.4
+ -[_LTLanguageDetectorFeatureCombinationModel estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:useFinalThresholds:isLowConfidencePair:].cold.5
+ -[_LTOspreySpeechTranslationSession _handleFinalBlazarResponse:].cold.2
+ -[_LTOspreySpeechTranslationSession _receivedEmptyFinalASRResults]
+ -[_LTPlaybackService .cxx_destruct]
+ -[_LTPlaybackService _currentOutputRouteIsSpeaker]
+ -[_LTPlaybackService start].cold.2
+ _AppleNeuralEngineLibraryCore.frameworkLibrary
+ _NSIntersectionRange
+ _NSSelectorFromString
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_CLASS_$_SiriTTSSynthesisRequest
+ _OBJC_IVAR_$__LTLanguageDetector._lowConfidenceLanguagePairs
+ _OBJC_IVAR_$__LTOfflineSpeechSynthesizer._audioDecoder
+ _OBJC_IVAR_$__LTOfflineSpeechSynthesizer._currentAudioData
+ _OBJC_IVAR_$__LTOfflineSpeechSynthesizer._currentAudioStreamDescription
+ _OBJC_IVAR_$__LTOfflineSpeechSynthesizer._currentWordTimingInfo
+ _OBJC_IVAR_$__LTPlaybackService._context
+ __LTPreferencesDebugForceLowConfidenceLID
+ ___37-[_LTTranslationServer _logStateSoon]_block_invoke.40
+ ___42-[_LTOfflineAssetManager updateAllAssets:]_block_invoke.33
+ ___42-[_LTOfflineAssetManager updateAllAssets:]_block_invoke.37
+ ___42-[_LTOfflineAssetManager updateAllAssets:]_block_invoke_2.36
+ ___42-[_LTOfflineAssetManager updateAllAssets:]_block_invoke_2.36.cold.1
+ ___44-[_LTOfflineAssetManager _refreshAllAssets:]_block_invoke.3
+ ___44-[_LTOfflineAssetManager _refreshAllAssets:]_block_invoke.3.cold.1
+ ___49-[_LTOfflineSpeechSynthesizer speak:withContext:]_block_invoke.11
+ ___49-[_LTOfflineSpeechSynthesizer speak:withContext:]_block_invoke.13
+ ___49-[_LTOfflineSpeechSynthesizer speak:withContext:]_block_invoke.13.cold.1
+ ___49-[_LTOfflineSpeechSynthesizer speak:withContext:]_block_invoke.16
+ ___49-[_LTOfflineSpeechSynthesizer speak:withContext:]_block_invoke.9
+ ___49-[_LTOfflineSpeechSynthesizer speak:withContext:]_block_invoke.9.cold.1
+ ___49-[_LTOfflineSpeechSynthesizer speak:withContext:]_block_invoke_2
+ ___49-[_LTOfflineSpeechSynthesizer speak:withContext:]_block_invoke_2.cold.1
+ ___58+[_LTWordTimingInfo(Daemon) wordTimingInfoFromArray:text:]_block_invoke
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.25
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.25.cold.1
+ ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.25.cold.2
+ ___65-[_LTOfflineAssetManager _queryLanguagePairStatusWithCompletion:]_block_invoke.16
+ ___65-[_LTOfflineAssetManager _queryLanguagePairStatusWithCompletion:]_block_invoke.16.cold.1
+ ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.20
+ ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke_2.22
+ ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke_2.22.cold.1
+ ___67+[_LTWordTimingInfo(Daemon) wordTimingInfoFromSiriTTSService:text:]_block_invoke
+ ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke.28
+ ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke.31
+ ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke.31.cold.1
+ ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke_2.29
+ ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke_3.30
+ ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke_3.30.cold.1
+ ___70-[_LTOspreySpeechTranslationSession initWithService:context:delegate:]_block_invoke.50
+ ___70-[_LTOspreySpeechTranslationSession initWithService:context:delegate:]_block_invoke.50.cold.1
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.109
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.89
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.93
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.93.cold.1
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.93.cold.2
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke_2.110
+ ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke_2.92
+ ___78-[_LTOfflineAssetManager _updateAsset:catalogAssets:downloadGroup:completion:]_block_invoke.32
+ ___78-[_LTOfflineAssetManager _updateAsset:catalogAssets:downloadGroup:completion:]_block_invoke.32.cold.1
+ ___81-[_LTOfflineAssetManager downloadAssetsForLanguagePair:userInitiated:completion:]_block_invoke.51
+ ___85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.69
+ ___85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.69.cold.1
+ ___86-[_LTOfflineAssetManager _downloadPassthroughAssetForLocale:userInitiated:completion:]_block_invoke.39
+ ___86-[_LTOfflineAssetManager _downloadPassthroughAssetForLocale:userInitiated:completion:]_block_invoke.39.cold.1
+ ___AppleNeuralEngineLibraryCore_block_invoke
+ ___block_descriptor_121_ea8_32s40s48s56s64s72s80s88bs96r104r_e30_v16?0"_LTTranslationResult"8ls32l8s40l8s48l8s56l8r96l8s64l8s72l8s80l8r104l8s88l8
+ ___block_descriptor_40_e8_32s_e23_v32?0"NSData"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e33_v32?0"FTWordTimingInfo"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e38_v32?0"SiriTTSWordTimingInfo"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8lw32l8
+ ___block_descriptor_40_e8_32w_e26_v16?0"SiriTTSAudioData"8lw32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSTimer"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_48_ea8_32bs40w_e34_v24?0"_LTAudioData"8"NSError"16lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e24_v16?0"_LTDAssetModel"8ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_88_ea8_32s40s48s56bs64bs72r80r_e5_v8?0ls32l8s40l8r72l8s48l8r80l8s56l8s64l8
+ ___block_descriptor_96_ea8_32s40s48s56s64bs72r80r88w_e39_v20?0"_LTSpeechRecognitionResult"8B16lw88l8s32l8s40l8s48l8s56l8r72l8r80l8s64l8
+ ___block_literal_global.27
+ ___block_literal_global.35
+ ___block_literal_global.72
+ ___get_ANEDeviceInfoClass_block_invoke
+ ___get_ANEDeviceInfoClass_block_invoke.cold.1
+ __unnamed_array_storage.22
+ __unnamed_array_storage.23
+ _audit_stringAppleNeuralEngine
+ _get_ANEDeviceInfoClass.softClass
+ _kLTDebugForceLowConfidenceLIDKey
+ _objc_msgSend$_currentOutputRouteIsSpeaker
+ _objc_msgSend$_needToWaitForBothFinalTranslationResultsWithContext:lidResult:
+ _objc_msgSend$_receivedEmptyFinalASRResults
+ _objc_msgSend$audioData
+ _objc_msgSend$decodeTo48KHzPCMFromChunks:from:outError:
+ _objc_msgSend$estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:useFinalThresholds:isLowConfidencePair:
+ _objc_msgSend$extractAudioChunksFromOpusWithData:packetCount:packetDescriptions:
+ _objc_msgSend$get48khzPCMDescription
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$isLowConfidencePair
+ _objc_msgSend$mapUtf8RangeToUtf16:inText:
+ _objc_msgSend$methodForSelector:
+ _objc_msgSend$muteTTSBasedOnRingerSwitchIfPossible
+ _objc_msgSend$scheduledTimerWithTimeInterval:repeats:block:
+ _objc_msgSend$setDidGenerateAudio:
+ _objc_msgSend$setDidGenerateWordTimings:
+ _objc_msgSend$setMXSessionProperty:value:error:
+ _objc_msgSend$smoothedWordTimingWithTextRangeInfoFrom:wordTimingInfo:
+ _objc_msgSend$synthesizeWithRequest:didFinish:
+ _objc_msgSend$wordTimingInfoFromSiriTTSService:text:
+ _objc_retain_x10
- +[_LTDLanguageAssetService flushCache]
- +[_LTOfflineTranslationEngine _needToWaitForBothASRSystemsWithContext:lidResult:]
- +[_LTWordTimingInfo(Daemon) extraBytesFromUTF8ToUTF16With:totalLength:begin:end:]
- +[_LTWordTimingInfo(Daemon) extraBytesFromUTF8ToUTF16With:totalLength:begin:end:].cold.1
- +[_LTWordTimingInfo(Daemon) utf16TimingInfoWithUTF8Range:withText:]
- +[_LTWordTimingInfo(Daemon) wordTimingWithTextRangeInfoFrom:wordTimingInfo:]
- -[_LTLanguageDetectorFeatureCombinationModel estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:]
- -[_LTLanguageDetectorFeatureCombinationModel estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:useFinalThresholds:]
- -[_LTLanguageDetectorFeatureCombinationModel estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:useFinalThresholds:].cold.1
- -[_LTLanguageDetectorFeatureCombinationModel estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:useFinalThresholds:].cold.2
- -[_LTLanguageDetectorFeatureCombinationModel estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:useFinalThresholds:].cold.3
- -[_LTLanguageDetectorFeatureCombinationModel estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:useFinalThresholds:].cold.4
- -[_LTLanguageDetectorFeatureCombinationModel estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:useFinalThresholds:].cold.5
- -[_LTOfflineAssetManager _clearCaches]
- -[_LTServerSpeakSession _playback:context:completion:audioStartHandler:].cold.5
- _OBJC_CLASS_$_SiriTTSSpeechRequest
- _OBJC_CLASS_$__ANEDeviceInfo
- _OBJC_IVAR_$__LTAudioData._data
- ___42-[_LTOfflineAssetManager updateAllAssets:]_block_invoke.34
- ___42-[_LTOfflineAssetManager updateAllAssets:]_block_invoke.38
- ___42-[_LTOfflineAssetManager updateAllAssets:]_block_invoke_2.37
- ___42-[_LTOfflineAssetManager updateAllAssets:]_block_invoke_2.37.cold.1
- ___44-[_LTOfflineAssetManager _refreshAllAssets:]_block_invoke.7
- ___44-[_LTOfflineAssetManager _refreshAllAssets:]_block_invoke.7.cold.1
- ___49-[_LTOfflineSpeechSynthesizer speak:withContext:]_block_invoke.7
- ___49-[_LTOfflineSpeechSynthesizer speak:withContext:]_block_invoke.7.cold.1
- ___49-[_LTOfflineSpeechSynthesizer speak:withContext:]_block_invoke.8
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.24
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.24.cold.1
- ___61+[_LTDLanguageAssetService _purgeUnusedAssetsWithCompletion:]_block_invoke.24.cold.2
- ___65-[_LTOfflineAssetManager _queryLanguagePairStatusWithCompletion:]_block_invoke.17
- ___65-[_LTOfflineAssetManager _queryLanguagePairStatusWithCompletion:]_block_invoke.17.cold.1
- ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.21
- ___66+[_LTDLanguageAssetService setAssets:options:progress:completion:]_block_invoke.21.cold.1
- ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke.29
- ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke.32
- ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke.32.cold.1
- ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke_2.30
- ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke_3.31
- ___67-[_LTOfflineAssetManager purgeAllAssetsExcludingConfig:completion:]_block_invoke_3.31.cold.1
- ___70-[_LTOspreySpeechTranslationSession initWithService:context:delegate:]_block_invoke_2
- ___70-[_LTOspreySpeechTranslationSession initWithService:context:delegate:]_block_invoke_2.cold.1
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.106
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.85
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.88
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke.90.cold.1
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke_2.107
- ___74-[_LTOfflineTranslationEngine startSpeechTranslationWithContext:delegate:]_block_invoke_2.89
- ___76+[_LTWordTimingInfo(Daemon) wordTimingWithTextRangeInfoFrom:wordTimingInfo:]_block_invoke
- ___78-[_LTOfflineAssetManager _updateAsset:catalogAssets:downloadGroup:completion:]_block_invoke.33
- ___78-[_LTOfflineAssetManager _updateAsset:catalogAssets:downloadGroup:completion:]_block_invoke.33.cold.1
- ___81-[_LTOfflineAssetManager downloadAssetsForLanguagePair:userInitiated:completion:]_block_invoke.52
- ___85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.68
- ___85-[_LTOfflineTranslationEngine startTextToSpeechTranslationWithContext:text:delegate:]_block_invoke.68.cold.1
- ___86-[_LTOfflineAssetManager _downloadPassthroughAssetForLocale:userInitiated:completion:]_block_invoke.40
- ___86-[_LTOfflineAssetManager _downloadPassthroughAssetForLocale:userInitiated:completion:]_block_invoke.40.cold.1
- ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8lw32l8
- ___block_descriptor_48_e8_32s40bs_e24_v16?0"_LTDAssetModel"8ls32l8s40l8
- ___block_descriptor_48_ea8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s48l8s40l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e33_v32?0"FTWordTimingInfo"8Q16^B24lr56l8r64l8s32l8s40l8s48l8
- ___block_descriptor_88_ea8_32s40s48s56bs64bs72r80r_e5_v8?0ls32l8r72l8s40l8s48l8r80l8s56l8s64l8
- ___block_descriptor_88_ea8_32s40s48s56s64bs72r80w_e36_v16?0"_LTSpeechRecognitionResult"8lw80l8s32l8s40l8s48l8s56l8r72l8s64l8
- ___block_descriptor_88_ea8_32s40s48s56s64bs72r_e30_v16?0"_LTTranslationResult"8ls32l8s40l8s48l8s56l8r72l8s64l8
- ___block_literal_global.36
- ___block_literal_global.6
- ___block_literal_global.71
- __unnamed_array_storage.30
- __unnamed_array_storage.31
- _objc_msgSend$_clearCaches
- _objc_msgSend$_needToWaitForBothASRSystemsWithContext:lidResult:
- _objc_msgSend$aneSubType
- _objc_msgSend$characterIsMember:
- _objc_msgSend$estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:useFinalThresholds:
- _objc_msgSend$extraBytesFromUTF8ToUTF16With:totalLength:begin:end:
- _objc_msgSend$lengthOfBytesUsingEncoding:
- _objc_msgSend$setAudioSessionId:
- _objc_msgSend$speakWithSpeechRequest:didFinish:
- _objc_msgSend$utf16TimingInfoWithUTF8Range:withText:
- _objc_msgSend$wordTimingWithTextRangeInfoFrom:wordTimingInfo:
CStrings:
+ "\x02D\x12#!"
+ "\x03S"
+ " | action-button"
+ "@\"SiriTTSSynthesisRequest\""
+ "@\"_LTAudioDecoder\""
+ "@64@0:8@16@24@32@40@48B56B60"
+ "@72@0:8@16{AudioStreamBasicDescription=dIIIIIIII}24^@64"
+ "Asset symlink skip accounting for %{public}@"
+ "Asset symlink validation for %{public}@ failed due to missing assets %zu or no assets %zu"
+ "Config asset is outdated, downloading version %zd"
+ "Converted to %ld bytes"
+ "Corrected FTWordTimingInfo UTF8(%@) range to UTF16(%@), word length: %zu"
+ "Empty packet descriptions, cannot extract data chunks"
+ "Encountered error setting MutesAudioBasedOnRingerSwitchState: %@"
+ "Finished downloading config asset version %zd"
+ "Installed config asset is already current version %zd"
+ "Merging _LTWordTimingInfo to previous one because same start timestamp"
+ "MutesAudioBasedOnRingerSwitchState"
+ "Q\x12"
+ "Send out no translation results caused by empty recognition"
+ "Sending out new %{public}@ LID result, detected %{public}@, confident %{BOOL}i"
+ "SiriTTSNSRangeUtil"
+ "Smoothed _LTWordTimingInfo:\n%@"
+ "Smoothing _LTWordTimingInfo: %@"
+ "Speaker"
+ "Unable to request final translation yet missing relevant ASR result based on confident acoustic LID result"
+ "Union of _LTWordTimingInfo ranges length(%zu) does not match text length(%zu)"
+ "Unsupported audio format from TTS"
+ "Using client header value: %{public}@"
+ "_ANEDeviceInfo"
+ "_LTWordTimingInfo text range(%@) is out of range from total text(text.length: %zu)"
+ "_LTWordTimingInfo text range(%@) overlaps with previous one(%@)"
+ "_LTWordTimingInfo word length(%zu) and text range length(%zu) don't match"
+ "_audioDecoder"
+ "_currentAudioData"
+ "_currentAudioStreamDescription"
+ "_currentOutputRouteIsSpeaker"
+ "_currentWordTimingInfo"
+ "_lowConfidenceLanguagePairs"
+ "_needToWaitForBothFinalTranslationResultsWithContext:lidResult:"
+ "_receivedEmptyFinalASRResults"
+ "audioData"
+ "decodeTo48KHzPCMFromChunks:from:outError:"
+ "estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:isLowConfidencePair:"
+ "estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:useFinalThresholds:isLowConfidencePair:"
+ "extractAudioChunksFromOpusWithData:packetCount:packetDescriptions:"
+ "get48khzPCMDescription"
+ "initWithArray:"
+ "isLowConfidencePair"
+ "mapUtf8RangeToUtf16:inText:"
+ "methodForSelector:"
+ "muteTTSBasedOnRingerSwitchIfPossible"
+ "scheduledTimerWithTimeInterval:repeats:block:"
+ "setDidGenerateAudio:"
+ "setDidGenerateWordTimings:"
+ "setMXSessionProperty:value:error:"
+ "smoothedWordTimingWithTextRangeInfoFrom:wordTimingInfo:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine"
+ "synthesizeWithRequest:didFinish:"
+ "v16@?0@\"NSTimer\"8"
+ "v16@?0@\"SiriTTSAudioData\"8"
+ "v20@?0@\"_LTSpeechRecognitionResult\"8B16"
+ "v32@?0@\"NSData\"8Q16^B24"
+ "v32@?0@\"SiriTTSWordTimingInfo\"8Q16^B24"
+ "wordTimingInfoFromSiriTTSService:text:"
+ "\xd1"
- "\x02C\x12#!"
- "@\"SiriTTSSpeechRequest\""
- "Asset count on disk %zd does not match config count %zd for %{public}@"
- "Asset identifier on disk %{public}@ does not match config identifier %{public}@ for %{public}@"
- "Asset manager clearing caches"
- "Asset on disk config not found for %{public}@"
- "Config asset needs to be downloaded"
- "Finished downloading config asset"
- "Out of word boundary: %ld is greater than %ld"
- "Pre-decode packet count: %ld. Post-decode packet count: %ld"
- "Q\x13"
- "Q48@0:8r*16Q24Q32Q40"
- "Sending out new %{public}@ LID result, detected %{public}@"
- "_clearCaches"
- "_needToWaitForBothASRSystemsWithContext:lidResult:"
- "ar_SA"
- "characterIsMember:"
- "estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:"
- "estimateLanguage:languageDetectionResults:partialSpeechResultConfidences:finalSpeechResults:modelVersions:useFinalThresholds:"
- "extraBytesFromUTF8ToUTF16With:totalLength:begin:end:"
- "lengthOfBytesUsingEncoding:"
- "setAudioSessionId:"
- "speakWithSpeechRequest:didFinish:"
- "th_TH"
- "utf16TimingInfoWithUTF8Range:withText:"
- "wordTimingWithTextRangeInfoFrom:wordTimingInfo:"
- "\xc1"

```
