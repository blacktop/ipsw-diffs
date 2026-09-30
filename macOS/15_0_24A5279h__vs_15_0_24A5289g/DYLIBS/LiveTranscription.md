## LiveTranscription

> `/System/Library/PrivateFrameworks/LiveTranscription.framework/Versions/A/LiveTranscription`

```diff

-488.0.0.0.0
-  __TEXT.__text: 0x1073c
+491.0.0.0.0
+  __TEXT.__text: 0x10a90
   __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_methlist: 0xf00
+  __TEXT.__objc_methlist: 0xf20
   __TEXT.__const: 0x292
-  __TEXT.__cstring: 0x70a
+  __TEXT.__cstring: 0x71a
   __TEXT.__gcc_except_tab: 0x168
-  __TEXT.__oslogstring: 0x115e
+  __TEXT.__oslogstring: 0x1225
   __TEXT.__swift5_typeref: 0x64
   __TEXT.__swift5_reflstr: 0xc5
   __TEXT.__swift5_assocty: 0x30

   __TEXT.__swift5_fieldmd: 0xc0
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x500
+  __TEXT.__unwind_info: 0x520
   __TEXT.__objc_classname: 0x264
-  __TEXT.__objc_methname: 0x2fc7
-  __TEXT.__objc_methtype: 0xbbb
-  __TEXT.__objc_stubs: 0x2560
-  __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__const: 0x130
+  __TEXT.__objc_methname: 0x3063
+  __TEXT.__objc_methtype: 0xbcd
+  __TEXT.__objc_stubs: 0x25c0
+  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb98
+  __DATA_CONST.__objc_selrefs: 0xbb8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x70
   __AUTH_CONST.__auth_got: 0x2f0
   __AUTH_CONST.__auth_ptr: 0x78
-  __AUTH_CONST.__const: 0x6c8
+  __AUTH_CONST.__const: 0x788
   __AUTH_CONST.__cfstring: 0x640
-  __AUTH_CONST.__objc_const: 0x2490
+  __AUTH_CONST.__objc_const: 0x24b0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x154
+  __DATA.__objc_ivar: 0x158
   __DATA.__data: 0x450
   __DATA.__bss: 0x320
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
-  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 551
-  Symbols:   1300
-  CStrings:  70
+  Functions: 556
+  Symbols:   1313
+  CStrings:  72
 
Symbols:
+ -[AXLTLanguageAssetManager deleteSpeechAssetForTaskHint:]
+ -[AXLTLanguageAssetManager downloadSpeechAssetForTaskHint:progress:completion:]
+ -[AXLTLanguageAssetManager languageAssetAvaliableForTaskHint:completion:]
+ -[AXLTLanguageAssetManager languageAssetAvaliableForTaskHint:completion:].cold.1
+ -[AXLTTranscriber isAssetPending]
+ -[AXLTTranscriber isAssetPending].cold.1
+ -[AXLTTranscriber isAssetPending].cold.2
+ -[AXLTTranscriber isPending]
+ -[AXLTTranscriber setIsPending:]
+ OBJC_IVAR_$_AXLTTranscriber._isPending
+ _OBJC_CLASS_$_SFEntitledAssetConfig
+ __54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke.273
+ __54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke_2.274
+ __57-[AXLTLanguageAssetManager deleteSpeechAssetForTaskHint:]_block_invoke.cold.1
+ __79-[AXLTLanguageAssetManager downloadSpeechAssetForTaskHint:progress:completion:]_block_invoke.254
+ __79-[AXLTLanguageAssetManager downloadSpeechAssetForTaskHint:progress:completion:]_block_invoke.256
+ __79-[AXLTLanguageAssetManager downloadSpeechAssetForTaskHint:progress:completion:]_block_invoke.cold.1
+ ___57-[AXLTLanguageAssetManager deleteSpeechAssetForTaskHint:]_block_invoke
+ ___73-[AXLTLanguageAssetManager languageAssetAvaliableForTaskHint:completion:]_block_invoke
+ ___79-[AXLTLanguageAssetManager downloadSpeechAssetForTaskHint:progress:completion:]_block_invoke
+ ___80-[AXLTTranscriber startTranscriptionForPID:appName:callback:completionCallback:]_block_invoke
+ ___block_descriptor_44_e8_32s_e8_v12?0B8l
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8l
+ ___block_descriptor_48_e8_32s_e8_v12?0B8l
+ ___block_descriptor_64_e8_32s40bs48bs_e8_v12?0B8l
+ ___copy_helper_block_e8_32s40b
+ ___copy_helper_block_e8_32s40b48b
+ _objc_msgSend$downloadSpeechAssetForTaskHint:progress:completion:
+ _objc_msgSend$fetchAssetWithConfig:clientIdentifier:progress:completion:
+ _objc_msgSend$initWithLanguage:taskHint:
+ _objc_msgSend$isAssetPending
+ _objc_msgSend$isPending
+ _objc_msgSend$languageAssetAvaliableForTaskHint:completion:
+ _objc_msgSend$setIsPending:
+ _objc_msgSend$supportedLanguagesForTaskHint:completion:
+ _objc_msgSend$unsubscribeFromAssetWithConfig:clientIdentifier:error:
- -[AXLTLanguageAssetManager deleteSpeechAsset]
- -[AXLTLanguageAssetManager deleteSpeechAsset].cold.1
- -[AXLTLanguageAssetManager downloadSpeechAsset:completion:]
- -[AXLTLanguageAssetManager downloadSpeechAsset:completion:].cold.1
- -[AXLTLanguageAssetManager languageAssetAvaliable]
- -[AXLTTranscriber resumeTranscriptionForPID:].cold.4
- -[AXLTTranscriber startTranscriptionForPID:appName:callback:completionCallback:].cold.3
- -[AXLTTranscriber stopTranscriptionForPID:].cold.3
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- __54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke.270
- __54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke_2.271
- __59-[AXLTLanguageAssetManager downloadSpeechAsset:completion:]_block_invoke.253
- ___59-[AXLTLanguageAssetManager downloadSpeechAsset:completion:]_block_invoke
- __swift_FORCE_LOAD_$_swiftOSLog
- __swift_FORCE_LOAD_$_swiftOSLog_$_LiveTranscription
- _objc_msgSend$_calcHistogramForBuffer:packetCount:isSilence:
- _objc_msgSend$downloadSpeechAsset:completion:
- _objc_msgSend$fetchAssetsForLanguage:clientIdentifier:urgent:forceUpgrade:progress:completion:
- _objc_msgSend$installedLanguages
- _objc_msgSend$languageAssetAvaliable
- _objc_msgSend$purgeAssetsForLanguage:clientIdentifier:error:
CStrings:
+ "v12@?0B8"
+ "v16@?0@\"NSArray\"8"

```
