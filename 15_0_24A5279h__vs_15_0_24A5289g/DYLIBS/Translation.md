## Translation

> `/System/Library/Frameworks/Translation.framework/Versions/A/Translation`

```diff

-284.0.0.0.0
-  __TEXT.__text: 0x45870
+286.1.0.0.0
+  __TEXT.__text: 0x45ea4
   __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_methlist: 0x4328
+  __TEXT.__objc_methlist: 0x4350
   __TEXT.__const: 0x56a
-  __TEXT.__cstring: 0x241e
-  __TEXT.__oslogstring: 0x3cd5
+  __TEXT.__cstring: 0x245e
+  __TEXT.__oslogstring: 0x3d05
   __TEXT.__gcc_except_tab: 0xa00
   __TEXT.__swift5_typeref: 0x1d9
   __TEXT.__constg_swiftt: 0x1d4

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__unwind_info: 0x14a0
+  __TEXT.__unwind_info: 0x14c0
   __TEXT.__eh_frame: 0x400
   __TEXT.__objc_classname: 0x9e1
-  __TEXT.__objc_methname: 0x9615
-  __TEXT.__objc_methtype: 0x16a3
-  __TEXT.__objc_stubs: 0x52c0
+  __TEXT.__objc_methname: 0x9706
+  __TEXT.__objc_methtype: 0x16d4
+  __TEXT.__objc_stubs: 0x5300
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__const: 0x4f8
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e78
+  __DATA_CONST.__objc_selrefs: 0x1e98
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x548
   __AUTH_CONST.__auth_ptr: 0x170
-  __AUTH_CONST.__const: 0x2128
-  __AUTH_CONST.__cfstring: 0x2920
-  __AUTH_CONST.__objc_const: 0x9cc0
+  __AUTH_CONST.__const: 0x21b8
+  __AUTH_CONST.__cfstring: 0x2980
+  __AUTH_CONST.__objc_const: 0x9d30
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x12c0
   __AUTH.__data: 0x3b8
-  __DATA.__objc_ivar: 0x694
+  __DATA.__objc_ivar: 0x698
   __DATA.__data: 0x828
   __DATA.__bss: 0x620
   __DATA.__common: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2125
-  Symbols:   4317
-  CStrings:  435
+  Functions: 2136
+  Symbols:   4335
+  CStrings:  438
 
Symbols:
+ +[NSError(LTTranslationError) lt_unsupportedLanguageError:]
+ +[_LTSELFLoggingInvocation translationTTSPlayedWithInvocationId:sourceOrTargetLanguage:isAutoplayTranslation:ttsPlaybackSpeed:audioChannel:]
+ +[_LTTranslator addLanguages:useCellular:]
+ +[_LTTranslator removeLanguages:]
+ -[_LTSELFLoggingTranslateAppContext initWithDisplayMode:localePair:isGenderAlternativeEnabled:tabName:tabSessionId:conversationTabView:isPlayTranslationsEnabled:autoTranslateSessionId:audioChannel:languageIdentificationEnabled:]
+ -[_LTSELFLoggingTranslateAppContext languageIdentificationEnabled]
+ OBJC_IVAR_$__LTSELFLoggingTranslateAppContext._languageIdentificationEnabled
+ __21-[_LTTranslator log:]_block_invoke.151
+ __24-[_LTTranslator cleanup]_block_invoke.131
+ __31+[_LTTranslator _deleteHotfix:]_block_invoke.51
+ __31+[_LTTranslator _getAssetSize:]_block_invoke.59
+ __31+[_LTTranslator _updateHotfix:]_block_invoke.50
+ __33+[_LTTranslator removeLanguages:]_block_invoke.37
+ __33+[_LTTranslator removeLanguages:]_block_invoke.cold.1
+ __34+[_LTTranslator _updateAllAssets:]_block_invoke.49
+ __34+[_LTTranslator installedLocales:]_block_invoke.52
+ __39+[_LTTranslator onDeviceModeSupported:]_block_invoke.72
+ __39-[_LTTranslator preheatForRequestSync:]_block_invoke.123
+ __40+[_LTTranslator _offlineLanguageStatus:]_block_invoke.38
+ __42+[_LTTranslator addLanguages:useCellular:]_block_invoke.32
+ __42+[_LTTranslator addLanguages:useCellular:]_block_invoke.cold.1
+ __42+[_LTTranslator selfLoggingEventWithData:]_block_invoke.154
+ __44+[_LTTranslator languageForText:completion:]_block_invoke.92
+ __46-[_LTTranslator preheatForRequest:completion:]_block_invoke.128
+ __50+[_LTTranslator installOfflineLocales:completion:]_block_invoke.63
+ __51+[_LTTranslator modalitiesPerLocaleWithCompletion:]_block_invoke.81
+ __52+[_LTTranslator installedLocalesForTask:completion:]_block_invoke.56
+ __52-[_LTTranslator translate:useDedicatedTextMachPort:]_block_invoke.143
+ __52-[_LTTranslator translate:useDedicatedTextMachPort:]_block_invoke.146
+ __52-[_LTTranslator translate:useDedicatedTextMachPort:]_block_invoke.146.cold.1
+ __52-[_LTTranslator translate:useDedicatedTextMachPort:]_block_invoke.147
+ __54+[_LTTranslator task:isSupportedInCountry:completion:]_block_invoke.89
+ __58+[_LTTranslator textStreamingConfigurationWithCompletion:]_block_invoke.85
+ __59+[_LTTranslator _purgeAllAssetsExcludingConfig:completion:]_block_invoke.46
+ __59+[_LTTranslator taskIsSupportedInCurrentRegion:completion:]_block_invoke.78
+ __60+[_LTTranslator configInfoForLocale:otherLocale:completion:]_block_invoke.68
+ __64+[_LTTranslator autoDetectSpeechUnsupportedPairsWithCompletion:]_block_invoke.80
+ __65+[_LTTranslator _getServiceProxyWithDelegate:errorHandler:block:]_block_invoke.114
+ __69+[_LTTranslator _purgeAssetForLanguagePair:userInitiated:completion:]_block_invoke.45
+ __70+[_LTTranslator additionalLikelyPreferredLocalesForLocale:completion:]_block_invoke.65
+ __72+[_LTTranslator _downloadAssetForLanguagePair:userInitiated:completion:]_block_invoke.41
+ __77+[_LTTranslator availableLocalePairsForTask:useDedicatedMachPort:completion:]_block_invoke.64
+ __81+[_LTTranslator selfLoggingInvocationStartedWithData:invocationStartedTier1Data:]_block_invoke.155
+ __84+[_LTTranslator shouldPresentSystemFirstUseConsentWithDedicatedMachPort:completion:]_block_invoke.77
+ __90+[_LTTranslator languagesForText:usingModel:strategy:useDedicatedTextMachPort:completion:]_block_invoke.102
+ __94+[_LTTranslator _getTextServiceProxyWithDelegate:useDedicatedTextMachPort:errorHandler:block:]_block_invoke.120
+ ___33+[_LTTranslator removeLanguages:]_block_invoke
+ ___40-[_LTPreflightConfiguration description]_block_invoke
+ ___42+[_LTTranslator addLanguages:useCellular:]_block_invoke
+ ___block_descriptor_41_e8_32s_e42_v24?0"<_LTTranslationService>"8?<v?>16l
+ __block_literal_global.130
+ __block_literal_global.133
+ __block_literal_global.150
+ __block_literal_global.36
+ _objc_msgSend$addLanguages:useCellular:
+ _objc_msgSend$initWithDisplayMode:localePair:isGenderAlternativeEnabled:tabName:tabSessionId:conversationTabView:isPlayTranslationsEnabled:autoTranslateSessionId:audioChannel:languageIdentificationEnabled:
+ _objc_msgSend$removeLanguages:
- -[_LTSELFLoggingInvocation translationTTSPlayed:isAutoplayTranslation:ttsPlaybackSpeed:audioChannel:]
- -[_LTSELFLoggingTranslateAppContext initWithDisplayMode:localePair:isGenderAlternativeEnabled:tabName:tabSessionId:conversationTabView:isPlayTranslationsEnabled:autoTranslateSessionId:audioChannel:]
- __21-[_LTTranslator log:]_block_invoke.143
- __24-[_LTTranslator cleanup]_block_invoke.123
- __31+[_LTTranslator _deleteHotfix:]_block_invoke.43
- __31+[_LTTranslator _getAssetSize:]_block_invoke.51
- __31+[_LTTranslator _updateHotfix:]_block_invoke.42
- __34+[_LTTranslator _updateAllAssets:]_block_invoke.41
- __34+[_LTTranslator installedLocales:]_block_invoke.44
- __39+[_LTTranslator onDeviceModeSupported:]_block_invoke.64
- __39-[_LTTranslator preheatForRequestSync:]_block_invoke.115
- __40+[_LTTranslator _offlineLanguageStatus:]_block_invoke.30
- __42+[_LTTranslator selfLoggingEventWithData:]_block_invoke.146
- __44+[_LTTranslator languageForText:completion:]_block_invoke.84
- __46-[_LTTranslator preheatForRequest:completion:]_block_invoke.120
- __50+[_LTTranslator installOfflineLocales:completion:]_block_invoke.55
- __51+[_LTTranslator modalitiesPerLocaleWithCompletion:]_block_invoke.73
- __52+[_LTTranslator installedLocalesForTask:completion:]_block_invoke.48
- __52-[_LTTranslator translate:useDedicatedTextMachPort:]_block_invoke.135
- __52-[_LTTranslator translate:useDedicatedTextMachPort:]_block_invoke.138
- __52-[_LTTranslator translate:useDedicatedTextMachPort:]_block_invoke.138.cold.1
- __52-[_LTTranslator translate:useDedicatedTextMachPort:]_block_invoke.139
- __54+[_LTTranslator task:isSupportedInCountry:completion:]_block_invoke.81
- __58+[_LTTranslator textStreamingConfigurationWithCompletion:]_block_invoke.77
- __59+[_LTTranslator _purgeAllAssetsExcludingConfig:completion:]_block_invoke.38
- __59+[_LTTranslator taskIsSupportedInCurrentRegion:completion:]_block_invoke.70
- __60+[_LTTranslator configInfoForLocale:otherLocale:completion:]_block_invoke.60
- __64+[_LTTranslator autoDetectSpeechUnsupportedPairsWithCompletion:]_block_invoke.72
- __65+[_LTTranslator _getServiceProxyWithDelegate:errorHandler:block:]_block_invoke.106
- __69+[_LTTranslator _purgeAssetForLanguagePair:userInitiated:completion:]_block_invoke.37
- __70+[_LTTranslator additionalLikelyPreferredLocalesForLocale:completion:]_block_invoke.57
- __72+[_LTTranslator _downloadAssetForLanguagePair:userInitiated:completion:]_block_invoke.33
- __77+[_LTTranslator availableLocalePairsForTask:useDedicatedMachPort:completion:]_block_invoke.56
- __81+[_LTTranslator selfLoggingInvocationStartedWithData:invocationStartedTier1Data:]_block_invoke.147
- __84+[_LTTranslator shouldPresentSystemFirstUseConsentWithDedicatedMachPort:completion:]_block_invoke.69
- __90+[_LTTranslator languagesForText:usingModel:strategy:useDedicatedTextMachPort:completion:]_block_invoke.94
- __94+[_LTTranslator _getTextServiceProxyWithDelegate:useDedicatedTextMachPort:errorHandler:block:]_block_invoke.112
- __block_literal_global.114
- __block_literal_global.117
- __block_literal_global.142
- _objc_msgSend$initWithDisplayMode:localePair:isGenderAlternativeEnabled:tabName:tabSessionId:conversationTabView:isPlayTranslationsEnabled:autoTranslateSessionId:audioChannel:
CStrings:
+ "UNSUPPORTED_LANGUAGE_ERROR_DESCRIPTION"
+ "languageIdentificationEnabled"
+ "nil"

```
