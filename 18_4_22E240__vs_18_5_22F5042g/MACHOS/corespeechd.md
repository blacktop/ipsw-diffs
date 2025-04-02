## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-3404.82.3.0.0
-  __TEXT.__text: 0x173d50
+3405.20.3.0.0
+  __TEXT.__text: 0x174334
   __TEXT.__auth_stubs: 0x17a0
-  __TEXT.__objc_stubs: 0x1efe0
-  __TEXT.__objc_methlist: 0x194bc
+  __TEXT.__objc_stubs: 0x1f000
+  __TEXT.__objc_methlist: 0x194fc
   __TEXT.__dlopen_cstrs: 0x2c5
   __TEXT.__const: 0x390
   __TEXT.__gcc_except_tab: 0x41d0
-  __TEXT.__objc_methname: 0x3f203
-  __TEXT.__cstring: 0x2a5df
-  __TEXT.__oslogstring: 0x21b2e
+  __TEXT.__objc_methname: 0x3f3a7
+  __TEXT.__cstring: 0x2aa03
+  __TEXT.__oslogstring: 0x21b9d
   __TEXT.__objc_classname: 0x3521
-  __TEXT.__objc_methtype: 0x8762
-  __TEXT.__unwind_info: 0x58a0
+  __TEXT.__objc_methtype: 0x87a0
+  __TEXT.__unwind_info: 0x58b0
   __DATA_CONST.__auth_got: 0xbe8
   __DATA_CONST.__got: 0x13e0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x5df8
-  __DATA_CONST.__cfstring: 0x8540
+  __DATA_CONST.__const: 0x5e90
+  __DATA_CONST.__cfstring: 0x8520
   __DATA_CONST.__objc_classlist: 0x980
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x4f0

   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_dictobj: 0x348
   __DATA_CONST.__objc_floatobj: 0x4b0
-  __DATA.__objc_const: 0x28598
-  __DATA.__objc_selrefs: 0xbb20
-  __DATA.__objc_ivar: 0x1f34
+  __DATA.__objc_const: 0x28608
+  __DATA.__objc_selrefs: 0xbb40
+  __DATA.__objc_ivar: 0x1f3c
   __DATA.__objc_data: 0x5f00
   __DATA.__data: 0x3b40
   __DATA.__bss: 0x748

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9657
-  Symbols:   1029
-  CStrings:  15829
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
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
+  Functions: 9664
+  Symbols:   1043
+  CStrings:  15842
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
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
+ "\x0f\b"
+ "%s Got unexpected phrase id: %lu with phrase count: %lu, not constructing VTEI"
+ "%s Overriding SSR node requirement"
+ "%s Overriding SSR setting for xpc listener"
+ "-[CSAttSiriController initWithEndpointerNode:osdNode:ssrNode:asrNode:uresNode:needsSSRNode:aFtmNode:speechDetectionNode:ccController:isContinuousConverationEnabled:speechManager:siriEnabledMonitor:siriClientBehaviorMonitor:rcHandler:supportsAcousticProgressiveChecker:supportsUnderstandingOnDevice:requireASROnDevice:supportsHybridUnderstandingOnDevice:]"
+ "-[CSIntuitiveConvRequestHandler initWithAudioSrcNode:endpointerNode:osdNode:ssrNode:speechRecognitionNode:uresNode:needsSSRNode:aFtmNode:speechManager:siriEnabledMonitor:siriClientBehaviorMonitor:intuitiveConvAudioCaptureMonitor:rcHandler:tcuGenerator:continuityEndDetector:bridgeMessageHandler:audioCoordinator:magusSupportedPolicy:supportsAcousticProgressiveChecker:supportsUnderstandingOnDevice:requireASROnDevice:supportsHybridUnderstandingOnDevice:supportsLogger:supportTCU:audioSessionInfoProvider:aggressiveECHandler:]"
+ "-[CSVoiceTriggerSecondPass _constructVTEIFromExclaveKeywordResult:speakerDetectionResult:phraseId:triggerTimestamp:triggerStartSampleCount:triggerEndSampleCount:]"
+ "-[CSVoiceTriggerSecondPass initWithFirstPassSource:phsEnabled:speechManager:supportsMphDetection:secondPassQueue:]"
+ "@\"CSCoreSpeechDKeepAliveHandler\""
+ "@48@0:8Q16B24@28B36@40"
+ "@60@0:8Q16Q24I32Q36Q44Q52"
+ "T@\"CSCoreSpeechDKeepAliveHandler\",&,N,V_keepAliveHandler"
+ "_constructVTEIFromExclaveKeywordResult:speakerDetectionResult:phraseId:triggerTimestamp:triggerStartSampleCount:triggerEndSampleCount:"
+ "_keepAliveHandler"
+ "constructVTEIFromExclaveKeywordResult:speakerDetectionResult:phraseId:triggerTimestamp:triggerStartSampleCount:triggerEndSampleCount:"
+ "deinitializeSecondPass"
+ "exclaveSecondPassVoiceTriggerAnalyzerForFirstPassSource:"
+ "initWithFirstPassSource:phsEnabled:speechManager:supportsMphDetection:secondPassQueue:"
+ "keepAliveHandler"
+ "setKeepAliveHandler:"
+ "shouldDisableSpeakerRecognition"
- "\x0f\a"
- "%s Initializing Secure VoiceTriggerSecondPass"
- "-[CSVoiceTriggerSecondPass initWithPHSEnabled:speechManager:supportsMphDetection:secondPassQueue:]"
- "@40@0:8B16@20B28@32"
- "exclaveSecondPassVoiceTriggerAnalyzer"
- "initWithPHSEnabled:"
- "initWithPHSEnabled:speechManager:supportsMphDetection:secondPassQueue:"
- "initWithPHSEnabled:targetQueue:"

```
