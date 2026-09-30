## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-3404.82.3.0.0
-  __TEXT.__text: 0x16dba0
+3405.20.3.0.0
+  __TEXT.__text: 0x16e358
   __TEXT.__auth_stubs: 0x1420
-  __TEXT.__objc_stubs: 0x1d340
-  __TEXT.__objc_methlist: 0x1858c
+  __TEXT.__objc_stubs: 0x1d3a0
+  __TEXT.__objc_methlist: 0x185e4
   __TEXT.__const: 0x360
   __TEXT.__gcc_except_tab: 0x3a7c
-  __TEXT.__cstring: 0x277f7
-  __TEXT.__objc_methname: 0x3bc50
-  __TEXT.__oslogstring: 0x205e3
-  __TEXT.__objc_classname: 0x32ef
-  __TEXT.__objc_methtype: 0x7c06
+  __TEXT.__cstring: 0x27c18
+  __TEXT.__objc_methname: 0x3beec
+  __TEXT.__oslogstring: 0x20652
+  __TEXT.__objc_classname: 0x3314
+  __TEXT.__objc_methtype: 0x7c82
   __TEXT.__dlopen_cstrs: 0x11a
   __TEXT.__unwind_info: 0x5360
   __DATA_CONST.__auth_got: 0xa28
-  __DATA_CONST.__got: 0x11d8
+  __DATA_CONST.__got: 0x11e8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x5c30
+  __DATA_CONST.__const: 0x5cd8
   __DATA_CONST.__cfstring: 0x76e0
   __DATA_CONST.__objc_classlist: 0x8f0
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x4c0
+  __DATA_CONST.__objc_protolist: 0x4c8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x748
-  __DATA_CONST.__objc_arraydata: 0x248
+  __DATA_CONST.__objc_arraydata: 0x250
   __DATA_CONST.__objc_dictobj: 0x2a8
   __DATA_CONST.__objc_floatobj: 0x490
   __DATA_CONST.__objc_intobj: 0xc30
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_doubleobj: 0x60
-  __DATA.__objc_const: 0x26af8
-  __DATA.__objc_selrefs: 0xb080
-  __DATA.__objc_ivar: 0x1e38
+  __DATA.__objc_const: 0x26b80
+  __DATA.__objc_selrefs: 0xb0c8
+  __DATA.__objc_ivar: 0x1e40
   __DATA.__objc_data: 0x5960
-  __DATA.__data: 0x3900
+  __DATA.__data: 0x3960
   __DATA.__bss: 0x690
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9296
-  Symbols:   911
-  CStrings:  14833
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 9303
+  Symbols:   928
+  CStrings:  14857
 
Symbols:
+ _OBJC_CLASS_$_SSRVTUITrainingListener
+ _OBJC_CLASS_$_SSRVTUITrainingMessageHandler
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftIOKit
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "\x0f\x02"
+ "%s Got unexpected phrase id: %lu with phrase count: %lu, not constructing VTEI"
+ "%s Overriding SSR node requirement"
+ "%s Overriding SSR setting for xpc listener"
+ "-[CSAttSiriController initWithEndpointerNode:osdNode:ssrNode:asrNode:uresNode:needsSSRNode:aFtmNode:speechDetectionNode:ccController:isContinuousConverationEnabled:speechManager:siriEnabledMonitor:siriClientBehaviorMonitor:rcHandler:supportsAcousticProgressiveChecker:supportsUnderstandingOnDevice:requireASROnDevice:supportsHybridUnderstandingOnDevice:]"
+ "-[CSIntuitiveConvRequestHandler initWithAudioSrcNode:endpointerNode:osdNode:ssrNode:speechRecognitionNode:uresNode:needsSSRNode:aFtmNode:speechManager:siriEnabledMonitor:siriClientBehaviorMonitor:intuitiveConvAudioCaptureMonitor:rcHandler:tcuGenerator:continuityEndDetector:bridgeMessageHandler:audioCoordinator:magusSupportedPolicy:supportsAcousticProgressiveChecker:supportsUnderstandingOnDevice:requireASROnDevice:supportsHybridUnderstandingOnDevice:supportsLogger:supportTCU:audioSessionInfoProvider:]"
+ "-[CSVoiceTriggerSecondPass _constructVTEIFromExclaveKeywordResult:speakerDetectionResult:phraseId:triggerTimestamp:triggerStartSampleCount:triggerEndSampleCount:]"
+ "-[CSVoiceTriggerSecondPass initWithFirstPassSource:phsEnabled:speechManager:supportsMphDetection:secondPassQueue:]"
+ "@\"SSRVTUITrainingListener\""
+ "@\"SSRVTUITrainingMessageHandler\""
+ "@48@0:8Q16B24@28B36@40"
+ "@60@0:8Q16Q24I32Q36Q44Q52"
+ "SSRVTUITrainingAudioSessionDelegate"
+ "T@\"SSRVTUITrainingListener\",&,N,V_vtuiTrainingListener"
+ "T@\"SSRVTUITrainingMessageHandler\",&,N,V_trainingMessageHandler"
+ "_constructVTEIFromExclaveKeywordResult:speakerDetectionResult:phraseId:triggerTimestamp:triggerStartSampleCount:triggerEndSampleCount:"
+ "_trainingMessageHandler"
+ "_vtuiTrainingListener"
+ "constructVTEIFromExclaveKeywordResult:speakerDetectionResult:phraseId:triggerTimestamp:triggerStartSampleCount:triggerEndSampleCount:"
+ "contextForVoiceTriggerTraining"
+ "deinitializeSecondPass"
+ "exclaveSecondPassVoiceTriggerAnalyzerForFirstPassSource:"
+ "historicalaudiod"
+ "initWithFirstPassSource:phsEnabled:speechManager:supportsMphDetection:secondPassQueue:"
+ "initWithMessageHandler:"
+ "requestAudioProviderForTrainingWithSyncBlock:"
+ "setTrainingMessageHandler:"
+ "setVtuiTrainingListener:"
+ "shouldDisableSpeakerRecognition"
+ "trainingMessageHandler"
+ "v24@0:8@?<v@?@\"CSAudioProvider\">16"
+ "vtuiTrainingListener"
- "\x0f"
- "%s Initializing Secure VoiceTriggerSecondPass"
- "-[CSVoiceTriggerSecondPass initWithPHSEnabled:speechManager:supportsMphDetection:secondPassQueue:]"
- "@40@0:8B16@20B28@32"
- "exclaveSecondPassVoiceTriggerAnalyzer"
- "initWithPHSEnabled:"
- "initWithPHSEnabled:speechManager:supportsMphDetection:secondPassQueue:"
- "initWithPHSEnabled:targetQueue:"

```
