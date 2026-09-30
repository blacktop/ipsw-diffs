## LiveTranscription

> `/System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription`

```diff

-545.3.11.0.0
-  __TEXT.__text: 0x2f8fc
-  __TEXT.__auth_stubs: 0x1000
-  __TEXT.__objc_methlist: 0x159c
-  __TEXT.__const: 0x960
-  __TEXT.__cstring: 0xfca
-  __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__oslogstring: 0x2694
+545.12.0.0.0
+  __TEXT.__text: 0x3098c
+  __TEXT.__auth_stubs: 0xfc0
+  __TEXT.__objc_methlist: 0x15cc
+  __TEXT.__const: 0x910
+  __TEXT.__cstring: 0x8fa
+  __TEXT.__gcc_except_tab: 0x8c
+  __TEXT.__oslogstring: 0x2784
   __TEXT.__dlopen_cstrs: 0x6a
-  __TEXT.__swift5_typeref: 0x44a
+  __TEXT.__swift5_typeref: 0x3f6
   __TEXT.__swift5_reflstr: 0x21a
   __TEXT.__swift5_assocty: 0x78
-  __TEXT.__constg_swiftt: 0x50c
+  __TEXT.__constg_swiftt: 0x4fc
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_fieldmd: 0x250
+  __TEXT.__swift5_fieldmd: 0x244
   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_types: 0x28
-  __TEXT.__swift5_capture: 0x2fc
+  __TEXT.__swift5_capture: 0x308
   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x78
-  __TEXT.__unwind_info: 0xa80
-  __TEXT.__eh_frame: 0xb80
-  __TEXT.__objc_classname: 0x21b
-  __TEXT.__objc_methname: 0x361b
-  __TEXT.__objc_methtype: 0xbfe
-  __TEXT.__objc_stubs: 0x2760
+  __TEXT.__unwind_info: 0xb90
+  __TEXT.__eh_frame: 0xb70
+  __TEXT.__objc_classname: 0x34e
+  __TEXT.__objc_methname: 0x3bf9
+  __TEXT.__objc_methtype: 0xd8c
+  __TEXT.__objc_stubs: 0x2940
   __DATA_CONST.__got: 0x3d0
-  __DATA_CONST.__const: 0x598
+  __DATA_CONST.__const: 0x590
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe20
+  __DATA_CONST.__objc_selrefs: 0xe40
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x810
-  __AUTH_CONST.__const: 0x980
+  __AUTH_CONST.__auth_got: 0x7f0
+  __AUTH_CONST.__const: 0x998
   __AUTH_CONST.__cfstring: 0x740
-  __AUTH_CONST.__objc_const: 0x2978
+  __AUTH_CONST.__objc_const: 0x2958
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0xa50
-  __AUTH.__data: 0x148
+  __AUTH.__objc_data: 0xa38
+  __AUTH.__data: 0x140
   __DATA.__objc_ivar: 0x180
-  __DATA.__data: 0x6b8
+  __DATA.__data: 0x6a8
   __DATA.__bss: 0x688
-  __DATA.__common: 0x78
+  __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0x248
   __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__bss: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreAudio_Private.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 14AB5849-EFA7-3DC2-BA84-178C4F04F22E
-  Functions: 1036
-  Symbols:   1990
-  CStrings:  1173
+  UUID: 8C3103E4-BFFD-311D-B889-E1C3AC345EBE
+  Functions: 1042
+  Symbols:   2018
+  CStrings:  1145
 
Symbols:
+ -[AXLTAudioOutManager startTranscriptionForPID:appID:appName:excludingPIDs:locale:error:]
+ -[AXLTAudioOutManager stopTranscriptionForPID:error:]
+ GCC_except_table15
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ ___49-[AXLTSpeechTranscriber setupTranscriberIfNeeded]_block_invoke.316
+ ___49-[AXLTSpeechTranscriber setupTranscriberIfNeeded]_block_invoke.319
+ ___51-[AXLTAudioOutTranscriber setupTranscriberIfNeeded]_block_invoke.298
+ ___51-[AXLTAudioOutTranscriber setupTranscriberIfNeeded]_block_invoke.302
+ ___54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke.307
+ ___54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke_2.308
+ ___79-[AXLTLanguageAssetManager downloadSpeechAssetForTaskHint:progress:completion:]_block_invoke.296
+ ___80-[AXLTTranscriber startTranscriptionForPID:appName:callback:completionCallback:]_block_invoke.298
+ ___block_literal_global.322
+ _objc_msgSend$_calcHistogramForBuffer:packetCount:isSilence:
+ _objc_msgSend$_deviceLanguage
+ _objc_msgSend$convertToBuffer:error:withInputFromBlock:
+ _objc_msgSend$currentThread
+ _objc_msgSend$dateToString:
+ _objc_msgSend$fractionCompleted
+ _objc_msgSend$initFromFormat:toFormat:
+ _objc_msgSend$inputFormat
+ _objc_msgSend$isEqual:
+ _objc_msgSend$outputFormat
+ _objc_msgSend$sampleRate
+ _objc_msgSend$setSuppressUsingIndependentInputRoute:
+ _objc_msgSend$setTranscriberVersion:
+ _objc_msgSend$startTranscriptionForPID:appID:appName:excludingPIDs:locale:error:
+ _objc_msgSend$stopTranscriptionForPID:error:
+ _objectdestroy.100Tm
+ _objectdestroy.28Tm
- -[AXLTLiveTranscription startTranscribing:targetPID:excludingPIDs:callbackBlock:audioInfoBlock:error:].cold.1
- -[AXLTLiveTranscription startTranscribing:targetPID:excludingPIDs:callbackBlock:audioInfoBlock:error:].cold.2
- GCC_except_table13
- ___49-[AXLTSpeechTranscriber setupTranscriberIfNeeded]_block_invoke.307
- ___49-[AXLTSpeechTranscriber setupTranscriberIfNeeded]_block_invoke.310
- ___51-[AXLTAudioOutTranscriber setupTranscriberIfNeeded]_block_invoke.289
- ___51-[AXLTAudioOutTranscriber setupTranscriberIfNeeded]_block_invoke.293
- ___54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke.298
- ___54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke_2.299
- ___79-[AXLTLanguageAssetManager downloadSpeechAssetForTaskHint:progress:completion:]_block_invoke.287
- ___80-[AXLTTranscriber startTranscriptionForPID:appName:callback:completionCallback:]_block_invoke.289
- ___block_literal_global.313
- __swiftEmptySetSingleton
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_LiveTranscription
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objectdestroy.107Tm
- _objectdestroy.19Tm
- _objectdestroy.59Tm
- _symbolic SDy__________G 10Foundation6LocaleV 6Speech25AssetsInstallationRequestC
- _symbolic SS_SSt
- _symbolic Si6offset______7elementtSg 10Foundation6LocaleV
- _symbolic ___________t 10Foundation6LocaleV 6Speech25AssetsInstallationRequestC
- _symbolic _____y__________G s18_DictionaryStorageC 10Foundation6LocaleV 6Speech25AssetsInstallationRequestC
CStrings:
+ "API stopTranscribing: failed for pid: %d to receive transcription updates for: %ld, error: %@"
+ "API stopTranscribing: failed to register pid: %d to receive transcription updates for: %ld, error: %@"
+ "API stopTranscribing: registered pid: %d to receive transcription updates for: %ld, key: %@"
+ "API stopTranscribing: removing pid: %d to receive transcription updates for: %ld, key: %@"
+ "APIv2 liveCaptionsResult sourceType: %s"
+ "APIv2 start pid:%s locale: %s"
+ "APIv2 start pid:%s, error: %@"
+ "APIv2 stop pid: %s"
+ "APIv2 stop pid: %s, error: %@"
+ "AXLiveCaptions"
+ "AudioManager: Starting transcription for locale: %@"
+ "B44@0:8i16@20^@28@?36"
+ "LiveTranscription"
+ "TranscriberV2: Audio converter destination buffer is nil"
+ "TranscriberV2: Not clearing SR: %s %s %s"
+ "TranscriberV2: asset downloading just started for locale: %s"
+ "TranscriberV2: startTranscription Skipped Source: %s Transcribing Source: cleared"
+ "TranscriberV2: stop for source: %s"
+ "localesDownloadState"
+ "startForPid:locale:error:transcriptionResult:"
+ "startTranscriptionForPID:appID:appName:excludingPIDs:locale:error:"
+ "stopForPid:error:"
+ "stopTranscriptionForPID:error:"
- "APIv2 liveCaptionsResult sourceType: %ld"
- "AudioManager: Starting transcription"
- "TranscriberV2: startTranscription Skipped Source: %s Transcribing Source: NULL"
- "downloadProgresses"
- "downloaders"
- "fail to register pid: %d to receive transcription updates for: %ld, error: %@"
- "fail to remove pid: %d to receive transcription updates for: %ld, error: %@"
- "registered pid: %d to receive transcription updates for: %ld, key: %@"
- "removed pid: %d to receive transcription updates for: %ld, key: %@"
- "startTranscriptionWithRequestType:AXLiveTranscriptionRequestAudio"
- "startTranscriptionWithRequestType:AXLiveTranscriptionRequestSpeech"
- "stopTranscription thread: %s"

```
