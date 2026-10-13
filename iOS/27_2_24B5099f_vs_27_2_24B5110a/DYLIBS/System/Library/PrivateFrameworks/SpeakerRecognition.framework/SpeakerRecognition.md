## SpeakerRecognition

> `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`

```diff

-3605.31.3.0.0
-  __TEXT.__text: 0xb6b44
+3605.32.1.0.0
+  __TEXT.__text: 0xb6e50
   __TEXT.__objc_methlist: 0x6de0
   __TEXT.__const: 0xfa8
   __TEXT.__dlopen_cstrs: 0xa6
   __TEXT.__cstring: 0x11068
   __TEXT.__swift5_typeref: 0x696
-  __TEXT.__oslogstring: 0xef41
+  __TEXT.__oslogstring: 0xefa8
   __TEXT.__swift5_capture: 0x230
   __TEXT.__constg_swiftt: 0x910
   __TEXT.__swift5_reflstr: 0x57f

   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x1028
+  __AUTH_CONST.__auth_got: 0x1030
   __AUTH.__objc_data: 0x1b8
   __AUTH.__data: 0x90
   __DATA.__objc_ivar: 0x878

   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0x2680
   __DATA_DIRTY.__data: 0x580
-  __DATA_DIRTY.__bss: 0x70
+  __DATA_DIRTY.__bss: 0x78
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 3103
-  Symbols:   5009
-  CStrings:  2658
+  Symbols:   5010
+  CStrings:  2662
 
Symbols:
+ _CSIsJ265
Functions:
~ -[SSRVTUITrainingManager initWithLocaleIdentifier:withAppDomain:withSiriSharedUserId:withAudioProviderSelector:shouldTrainViaXPC:] : 532 -> 552
~ -[SSRVTUITrainingManager createKeywordDetector] : 464 -> 1104
~ ___106-[SSRVTUITrainingManager _trainUtteranceLocally:shouldUseASR:mhUUID:referenceString:completionWithResult:]_block_invoke_2 : 1152 -> 1172
~ -[SSRVTUITrainingManager CSVTUITrainingSession:hasTrainUtterance:languageCode:payload:] : 340 -> 432
~ +[SSRUtils isMphVTUIKeywordDetectorSupportedPlatform] : 44 -> 52
CStrings:
+ "%s _currentSecureAsset: %@"
+ "%s keywordDetector: %@"
+ "%s useRecognizerCombination: %u"
+ "%s useSecureAsset:%u"
```
