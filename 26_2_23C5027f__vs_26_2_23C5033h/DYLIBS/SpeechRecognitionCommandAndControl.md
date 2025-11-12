## SpeechRecognitionCommandAndControl

> `/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl`

```diff

-148.1.5.0.0
-  __TEXT.__text: 0xa0e38
-  __TEXT.__auth_stubs: 0x2120
-  __TEXT.__objc_methlist: 0xabec
+148.1.6.0.0
+  __TEXT.__text: 0xa12cc
+  __TEXT.__auth_stubs: 0x2130
+  __TEXT.__objc_methlist: 0xac2c
   __TEXT.__const: 0xe24
-  __TEXT.__oslogstring: 0x29c5
-  __TEXT.__cstring: 0x7107
-  __TEXT.__gcc_except_tab: 0x1f88
+  __TEXT.__oslogstring: 0x2a54
+  __TEXT.__cstring: 0x7127
+  __TEXT.__gcc_except_tab: 0x1fac
   __TEXT.__ustring: 0x3a
   __TEXT.__constg_swiftt: 0x2dc
   __TEXT.__swift5_typeref: 0xd5e

   __TEXT.__swift5_fieldmd: 0x134
   __TEXT.__unwind_info: 0x2940
   __TEXT.__eh_frame: 0x218
-  __TEXT.__objc_classname: 0x1651
-  __TEXT.__objc_methname: 0x1e574
+  __TEXT.__objc_classname: 0x1650
+  __TEXT.__objc_methname: 0x1e72b
   __TEXT.__objc_methtype: 0x3f3b
-  __TEXT.__objc_stubs: 0x13b80
-  __DATA_CONST.__got: 0xec0
+  __TEXT.__objc_stubs: 0x13d00
+  __DATA_CONST.__got: 0xed0
   __DATA_CONST.__const: 0x1a80
   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7098
+  __DATA_CONST.__objc_selrefs: 0x7108
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x858
-  __AUTH_CONST.__auth_got: 0x10a0
+  __AUTH_CONST.__auth_got: 0x10a8
   __AUTH_CONST.__const: 0x18e8
-  __AUTH_CONST.__cfstring: 0x89c0
-  __AUTH_CONST.__objc_const: 0xf0b0
+  __AUTH_CONST.__cfstring: 0x8a00
+  __AUTH_CONST.__objc_const: 0xf110
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0x2bc0
   __AUTH.__data: 0x288
-  __DATA.__objc_ivar: 0xa3c
+  __DATA.__objc_ivar: 0xa44
   __DATA.__data: 0x1b10
   __DATA.__bss: 0x990
   __DATA.__common: 0x1b8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E0F294D6-3FF5-3A47-8273-C20C8FC0BBCF
-  Functions: 4261
-  Symbols:   14973
-  CStrings:  8035
+  UUID: A23C799F-7E97-37F5-B649-360DF736D7AF
+  Functions: 4266
+  Symbols:   15000
+  CStrings:  8058
 
Symbols:
+ -[CACMessageTracerUtilities logSpokenCommand:]
+ -[CACMessageTracerUtilities sendCoreAnalyticsForRecognizedCommand:appIdentifier:]
+ -[CACSpokenCommand asrLatency]
+ -[CACSpokenCommand calculateLatency]
+ -[CACSpokenCommand executionLatency]
+ -[CACSpokenCommand isExecutionCompletionDeterminedBySpokenCommandItself]
+ -[CACSpokenCommand setAsrLatency:]
+ -[CACSpokenCommand setExecutionCompleted:]
+ -[CACSpokenCommand setExecutionCompletionDeterminedBySpokenCommandItself:]
+ -[CACSpokenCommand setExecutionLatency:]
+ -[CACSpokenCommand spokenCommandExecutionDidNotComplete]
+ -[CACTextEditingProvider setExecutionCompleted:]
+ -[CACTextEditingProvider setExecutionCompletionDeterminedBySpokenCommandItself:]
+ _OBJC_CLASS_$_SRDMachTime
+ _OBJC_CLASS_$_VCCommon
+ _OBJC_IVAR_$_CACSpokenCommand._asrLatency
+ _OBJC_IVAR_$_CACSpokenCommand._executionCompletionDeterminedBySpokenCommandItself
+ _OBJC_IVAR_$_CACSpokenCommand._executionLatency
+ _OBJC_IVAR_$_CACSpokenCommand._executionTimer
+ ___35-[CACSpokenCommand searchSpotlight]_block_invoke.736
+ ___35-[CACSpokenCommand searchSpotlight]_block_invoke.736.cold.1
+ ___39-[CACDisplayManager carPlayDidConnect:]_block_invoke.691
+ ___53-[CACSpokenCommandManager beginObservingApplications]_block_invoke.652
+ ____NotificationLiveMicrophoneDidTurnOnAfterInterruption_block_invoke.1726
+ ___block_literal_global.1214
+ ___block_literal_global.1699
+ ___block_literal_global.1701
+ ___block_literal_global.1704
+ ___block_literal_global.1706
+ ___block_literal_global.1725
+ ___block_literal_global.1728
+ ___block_literal_global.291
+ ___block_literal_global.293
+ ___block_literal_global.295
+ ___block_literal_global.299
+ ___block_literal_global.301
+ ___block_literal_global.303
+ ___block_literal_global.305
+ ___block_literal_global.311
+ ___block_literal_global.317
+ ___block_literal_global.319
+ ___block_literal_global.321
+ ___block_literal_global.323
+ ___block_literal_global.333
+ ___block_literal_global.335
+ ___block_literal_global.337
+ ___block_literal_global.339
+ ___block_literal_global.341
+ ___block_literal_global.343
+ ___block_literal_global.360
+ ___block_literal_global.364
+ ___block_literal_global.365
+ ___block_literal_global.366
+ ___block_literal_global.367
+ ___block_literal_global.368
+ ___block_literal_global.370
+ ___block_literal_global.372
+ ___block_literal_global.401
+ ___block_literal_global.403
+ ___block_literal_global.424
+ ___block_literal_global.449
+ ___block_literal_global.596
+ ___block_literal_global.599
+ ___block_literal_global.611
+ ___block_literal_global.614
+ ___block_literal_global.627
+ ___block_literal_global.630
+ ___block_literal_global.632
+ ___block_literal_global.652
+ ___block_literal_global.654
+ ___block_literal_global.659
+ ___block_literal_global.676
+ ___block_literal_global.683
+ ___block_literal_global.690
+ ___block_literal_global.708
+ ___block_literal_global.710
+ ___block_literal_global.712
+ ___block_literal_global.720
+ ___block_literal_global.723
+ ___block_literal_global.735
+ ___block_literal_global.771
+ ___block_literal_global.793
+ ___block_literal_global.795
+ ___block_literal_global.800
+ ___block_literal_global.808
+ ___block_literal_global.866
+ ___block_literal_global.983
+ _displayRecognizedMessageUsingAttributedString:.recSoundInit.512
+ _mach_absolute_time
+ _objc_msgSend$asrLatency
+ _objc_msgSend$calculateLatency
+ _objc_msgSend$executionLatency
+ _objc_msgSend$initWithMachTime:
+ _objc_msgSend$logSpokenCommand:
+ _objc_msgSend$machAbsoluteTimeToMilliseconds:
+ _objc_msgSend$mach_time
+ _objc_msgSend$sendCoreAnalyticsForRecognizedCommand:appIdentifier:
+ _objc_msgSend$setExecutionCompleted:
+ _objc_msgSend$setExecutionCompletionDeterminedBySpokenCommandItself:
+ _objc_msgSend$setTimeCommandExecutionEnded:
+ _objc_msgSend$setTimeCommandExecutionStarted:
+ _objc_msgSend$timeAsrResultReceived
+ _objc_msgSend$timeCommandExecutionEnded
+ _objc_msgSend$timeMatchedUtteranceSilenceStart
+ _objc_msgSend$timeSRDResponseSent
- -[CACMessageTracerUtilities logCommandWithIdentifier:]
- -[CACMessageTracerUtilities sendCoreAnalyticsForRecognizedCommandIdentifier:appIdentifier:]
- -[CACSpokenCommand isCompletionDeterminedManually]
- -[CACSpokenCommand isExectuting]
- -[CACSpokenCommand setCompletionDeterminedManually:]
- -[CACSpokenCommand setExecuting:]
- -[CACTextEditingProvider setCompletionDeterminedManually:]
- -[CACTextEditingProvider setExecuting:]
- _OBJC_IVAR_$_CACSpokenCommand._exectutionStartTime
- _OBJC_IVAR_$_CACSpokenCommand._executionCompletionDeterminedManually
- ___35-[CACSpokenCommand searchSpotlight]_block_invoke.723
- ___35-[CACSpokenCommand searchSpotlight]_block_invoke.723.cold.1
- ___39-[CACDisplayManager carPlayDidConnect:]_block_invoke.682
- ___53-[CACSpokenCommandManager beginObservingApplications]_block_invoke.643
- ____NotificationLiveMicrophoneDidTurnOnAfterInterruption_block_invoke.1717
- ___block_literal_global.1205
- ___block_literal_global.1686
- ___block_literal_global.1688
- ___block_literal_global.1690
- ___block_literal_global.1692
- ___block_literal_global.1716
- ___block_literal_global.1719
- ___block_literal_global.282
- ___block_literal_global.284
- ___block_literal_global.286
- ___block_literal_global.287
- ___block_literal_global.289
- ___block_literal_global.290
- ___block_literal_global.292
- ___block_literal_global.294
- ___block_literal_global.297
- ___block_literal_global.300
- ___block_literal_global.302
- ___block_literal_global.304
- ___block_literal_global.308
- ___block_literal_global.310
- ___block_literal_global.312
- ___block_literal_global.314
- ___block_literal_global.320
- ___block_literal_global.326
- ___block_literal_global.328
- ___block_literal_global.330
- ___block_literal_global.332
- ___block_literal_global.342
- ___block_literal_global.352
- ___block_literal_global.355
- ___block_literal_global.357
- ___block_literal_global.359
- ___block_literal_global.383
- ___block_literal_global.394
- ___block_literal_global.415
- ___block_literal_global.440
- ___block_literal_global.587
- ___block_literal_global.590
- ___block_literal_global.602
- ___block_literal_global.605
- ___block_literal_global.617
- ___block_literal_global.618
- ___block_literal_global.623
- ___block_literal_global.628
- ___block_literal_global.639
- ___block_literal_global.645
- ___block_literal_global.667
- ___block_literal_global.674
- ___block_literal_global.677
- ___block_literal_global.695
- ___block_literal_global.697
- ___block_literal_global.699
- ___block_literal_global.707
- ___block_literal_global.711
- ___block_literal_global.714
- ___block_literal_global.722
- ___block_literal_global.762
- ___block_literal_global.784
- ___block_literal_global.786
- ___block_literal_global.791
- ___block_literal_global.799
- ___block_literal_global.857
- ___block_literal_global.974
- _displayRecognizedMessageUsingAttributedString:.recSoundInit.503
- _objc_msgSend$logCommandWithIdentifier:
- _objc_msgSend$sendCoreAnalyticsForRecognizedCommandIdentifier:appIdentifier:
- _objc_msgSend$setCompletionDeterminedManually:
- _objc_msgSend$setExecuting:
CStrings:
+ "ASRLatency"
+ "CAC, CmdRec: Performed action. %@ ASRLatency = %llu, CommandMatchingLatency = %llu,  TotalExecutionLatency = %llu"
+ "ExecutionLatency"
+ "Sent %{public}@ event to CoreAnalytics with data %{public}@."
+ "TQ,V_asrLatency"
+ "TQ,V_executionLatency"
+ "_asrLatency"
+ "_executionCompletionDeterminedBySpokenCommandItself"
+ "_executionLatency"
+ "_executionTimer"
+ "asrLatency"
+ "calculateLatency"
+ "executionLatency"
+ "initWithMachTime:"
+ "isExecutionCompletionDeterminedBySpokenCommandItself"
+ "logSpokenCommand:"
+ "machAbsoluteTimeToMilliseconds:"
+ "mach_time"
+ "sendCoreAnalyticsForRecognizedCommand:appIdentifier:"
+ "setAsrLatency:"
+ "setExecutionCompleted:"
+ "setExecutionCompletionDeterminedBySpokenCommandItself:"
+ "setExecutionLatency:"
+ "setTimeCommandExecutionEnded:"
+ "setTimeCommandExecutionStarted:"
+ "spokenCommandExecutionDidNotComplete"
+ "timeAsrResultReceived"
+ "timeCommandExecutionEnded"
+ "timeMatchedUtteranceSilenceStart"
+ "timeSRDResponseSent"
- "Sent %@ event to CoreAnalytics."
- "_exectutionStartTime"
- "_executionCompletionDeterminedManually"
- "isCompletionDeterminedManually"
- "isExectuting"
- "logCommandWithIdentifier:"
- "sendCoreAnalyticsForRecognizedCommandIdentifier:appIdentifier:"
- "setCompletionDeterminedManually:"
- "setExecuting:"

```
