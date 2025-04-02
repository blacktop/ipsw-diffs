## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3404.82.3.0.0
-  __TEXT.__text: 0x158404
+3405.20.3.0.0
+  __TEXT.__text: 0x158860
   __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_methlist: 0x15494
+  __TEXT.__objc_methlist: 0x154a4
   __TEXT.__const: 0x5e0
   __TEXT.__dlopen_cstrs: 0x197
   __TEXT.__gcc_except_tab: 0x3fd4
-  __TEXT.__cstring: 0x27205
-  __TEXT.__oslogstring: 0x1f90f
+  __TEXT.__cstring: 0x272b8
+  __TEXT.__oslogstring: 0x1f930
   __TEXT.__unwind_info: 0x5030
   __TEXT.__objc_classname: 0x2e98
-  __TEXT.__objc_methname: 0x3855c
-  __TEXT.__objc_methtype: 0x7c6c
-  __TEXT.__objc_stubs: 0x1c580
+  __TEXT.__objc_methname: 0x386b1
+  __TEXT.__objc_methtype: 0x7c89
+  __TEXT.__objc_stubs: 0x1c5c0
   __DATA_CONST.__got: 0x1aa8
-  __DATA_CONST.__const: 0x4190
+  __DATA_CONST.__const: 0x41b8
   __DATA_CONST.__objc_classlist: 0x858
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x490
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaa38
+  __DATA_CONST.__objc_selrefs: 0xaa50
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x450
   __AUTH_CONST.__auth_got: 0xe10
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x1e00
-  __AUTH_CONST.__cfstring: 0x9000
+  __AUTH_CONST.__cfstring: 0x8fe0
   __AUTH_CONST.__objc_const: 0x21b98
   __AUTH_CONST.__objc_intobj: 0xa20
   __AUTH_CONST.__objc_doubleobj: 0xb0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8273
-  Symbols:   10084
-  CStrings:  14570
+  Functions: 8276
+  Symbols:   10087
+  CStrings:  14575
 
CStrings:
+ "%s Got unexpected phrase id: %lu with phrase count: %lu, not constructing VTEI"
+ "%s _activateAudioSessionWithDelay has failed. startRecordWithSettings has failed"
+ "-[CSVoiceTriggerSecondPass _constructVTEIFromExclaveKeywordResult:speakerDetectionResult:phraseId:triggerTimestamp:triggerStartSampleCount:triggerEndSampleCount:]"
+ "-[CSVoiceTriggerSecondPass initWithFirstPassSource:phsEnabled:speechManager:supportsMphDetection:secondPassQueue:]"
+ "@48@0:8Q16B24@28B36@40"
+ "@60@0:8Q16Q24I32Q36Q44Q52"
+ "_constructVTEIFromExclaveKeywordResult:speakerDetectionResult:phraseId:triggerTimestamp:triggerStartSampleCount:triggerEndSampleCount:"
+ "_shouldUseSpeakerRecognitionProxy"
+ "constructVTEIFromExclaveKeywordResult:speakerDetectionResult:phraseId:triggerTimestamp:triggerStartSampleCount:triggerEndSampleCount:"
+ "deinitializeSecondPass"
+ "exclaveSecondPassVoiceTriggerAnalyzerForFirstPassSource:"
+ "initWithFirstPassSource:phsEnabled:speechManager:supportsMphDetection:secondPassQueue:"
+ "shouldDisableSpeakerRecognition"
- "%s Initializing Secure VoiceTriggerSecondPass"
- "%s _activateAudoiSessionWithDelay has failed. startRecordWithSettings has failed"
- "-[CSVoiceTriggerSecondPass initWithPHSEnabled:speechManager:supportsMphDetection:secondPassQueue:]"
- "@40@0:8B16@20B28@32"
- "exclaveSecondPassVoiceTriggerAnalyzer"
- "initWithPHSEnabled:"
- "initWithPHSEnabled:speechManager:supportsMphDetection:secondPassQueue:"
- "initWithPHSEnabled:targetQueue:"

```
