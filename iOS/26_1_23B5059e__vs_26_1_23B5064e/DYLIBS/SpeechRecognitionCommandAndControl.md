## SpeechRecognitionCommandAndControl

> `/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl`

```diff

-148.1.1.0.0
-  __TEXT.__text: 0xa0698
-  __TEXT.__auth_stubs: 0x2110
-  __TEXT.__objc_methlist: 0xabcc
+148.1.2.0.0
+  __TEXT.__text: 0xa0c10
+  __TEXT.__auth_stubs: 0x2120
+  __TEXT.__objc_methlist: 0xac1c
   __TEXT.__const: 0xc04
-  __TEXT.__oslogstring: 0x29c5
-  __TEXT.__cstring: 0x70e7
-  __TEXT.__gcc_except_tab: 0x1f88
+  __TEXT.__oslogstring: 0x2a54
+  __TEXT.__cstring: 0x70f7
+  __TEXT.__gcc_except_tab: 0x2008
   __TEXT.__ustring: 0x3a
   __TEXT.__constg_swiftt: 0x2dc
   __TEXT.__swift5_typeref: 0xd5e

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_fieldmd: 0x134
-  __TEXT.__unwind_info: 0x2958
+  __TEXT.__unwind_info: 0x2950
   __TEXT.__eh_frame: 0x218
-  __TEXT.__objc_classname: 0x1651
-  __TEXT.__objc_methname: 0x1e54b
+  __TEXT.__objc_classname: 0x1650
+  __TEXT.__objc_methname: 0x1e749
   __TEXT.__objc_methtype: 0x3f3b
-  __TEXT.__objc_stubs: 0x13b80
-  __DATA_CONST.__got: 0xec0
+  __TEXT.__objc_stubs: 0x13d20
+  __DATA_CONST.__got: 0xed0
   __DATA_CONST.__const: 0x1a80
   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7080
+  __DATA_CONST.__objc_selrefs: 0x7110
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x858
-  __AUTH_CONST.__auth_got: 0x1098
+  __AUTH_CONST.__auth_got: 0x10a0
   __AUTH_CONST.__const: 0x18e8
-  __AUTH_CONST.__cfstring: 0x89a0
-  __AUTH_CONST.__objc_const: 0xf038
+  __AUTH_CONST.__cfstring: 0x89e0
+  __AUTH_CONST.__objc_const: 0xf110
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0x2bc0
   __AUTH.__data: 0x288
-  __DATA.__objc_ivar: 0xa3c
+  __DATA.__objc_ivar: 0xa44
   __DATA.__data: 0x1b08
   __DATA.__bss: 0x990
   __DATA.__common: 0x1b8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6F979420-AC22-3279-9AC7-FDE08CCD9E8E
-  Functions: 4261
-  Symbols:   14904
-  CStrings:  8030
+  UUID: 1A9995F5-E468-3B96-AFFB-EFD0C326D731
+  Functions: 4265
+  Symbols:   14930
+  CStrings:  8057
 
Symbols:
+ -[CACMessageTracerUtilities logSpokenCommand:]
+ -[CACMessageTracerUtilities sendCoreAnalyticsForRecognizedCommand:appIdentifier:]
+ -[CACSpokenCommand asrLatency]
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
+ ___35-[CACSpokenCommand searchSpotlight]_block_invoke.723
+ ___35-[CACSpokenCommand searchSpotlight]_block_invoke.723.cold.1
+ ____NotificationLiveMicrophoneDidTurnOnAfterInterruption_block_invoke.1719
+ ___block_literal_global.1207
+ ___block_literal_global.1694
+ ___block_literal_global.1699
+ ___block_literal_global.1718
+ ___block_literal_global.1721
+ ___block_literal_global.617
+ ___block_literal_global.639
+ ___block_literal_global.646
+ ___block_literal_global.669
+ ___block_literal_global.677
+ ___block_literal_global.695
+ ___block_literal_global.697
+ ___block_literal_global.707
+ ___block_literal_global.722
+ ___block_literal_global.788
+ ___block_literal_global.793
+ ___block_literal_global.801
+ ___block_literal_global.859
+ ___block_literal_global.976
+ _mach_absolute_time
+ _objc_msgSend$adjustCapsAndSpacingUsingLeadingText:preITNTokens:customVocabularies:localeIdentifier:
+ _objc_msgSend$asrLatency
+ _objc_msgSend$executionLatency
+ _objc_msgSend$initWithMachTime:
+ _objc_msgSend$logSpokenCommand:
+ _objc_msgSend$machAbsoluteTimeToMilliseconds:
+ _objc_msgSend$mach_time
+ _objc_msgSend$sendCoreAnalyticsForRecognizedCommand:appIdentifier:
+ _objc_msgSend$setAsrLatency:
+ _objc_msgSend$setExecutionCompleted:
+ _objc_msgSend$setExecutionCompletionDeterminedBySpokenCommandItself:
+ _objc_msgSend$setExecutionLatency:
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
- ___35-[CACSpokenCommand searchSpotlight]_block_invoke.720
- ___35-[CACSpokenCommand searchSpotlight]_block_invoke.720.cold.1
- ____NotificationLiveMicrophoneDidTurnOnAfterInterruption_block_invoke.1717
- ___block_literal_global.1205
- ___block_literal_global.1686
- ___block_literal_global.1695
- ___block_literal_global.1716
- ___block_literal_global.1719
- ___block_literal_global.614
- ___block_literal_global.636
- ___block_literal_global.643
- ___block_literal_global.667
- ___block_literal_global.692
- ___block_literal_global.694
- ___block_literal_global.704
- ___block_literal_global.719
- ___block_literal_global.786
- ___block_literal_global.791
- ___block_literal_global.799
- ___block_literal_global.857
- ___block_literal_global.974
- _objc_msgSend$adjustCapsAndSpacingUsingLeadingText:firstPreITNToken:customVocabularies:localeIdentifier:
- _objc_msgSend$logCommandWithIdentifier:
- _objc_msgSend$sendCoreAnalyticsForRecognizedCommandIdentifier:appIdentifier:
- _objc_msgSend$setCompletionDeterminedManually:
- _objc_msgSend$setExecuting:
CStrings:
+ "ASRLatency"
+ "CAC, CmdRec: Performed action. %@ ASRLatency = %llu, CommandMatchingLatency = %llu,  TotalExecutionLatency = %llu"
+ "ExcutionLatency"
+ "Sent %{public}@ event to CoreAnalytics with data %{public}@."
+ "TQ,V_asrLatency"
+ "TQ,V_executionLatency"
+ "_asrLatency"
+ "_executionCompletionDeterminedBySpokenCommandItself"
+ "_executionLatency"
+ "_executionTimer"
+ "adjustCapsAndSpacingUsingLeadingText:preITNTokens:customVocabularies:localeIdentifier:"
+ "asrLatency"
+ "cellTopOffset"
+ "executionLatency"
+ "initWithMachTime:"
+ "isExecutionCompletionDeterminedBySpokenCommandItself"
+ "lineTopOffset"
+ "logSpokenCommand:"
+ "machAbsoluteTimeToMilliseconds:"
+ "mach_time"
+ "outerGridPadding"
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
- "adjustCapsAndSpacingUsingLeadingText:firstPreITNToken:customVocabularies:localeIdentifier:"
- "isCompletionDeterminedManually"
- "isExectuting"
- "logCommandWithIdentifier:"
- "sendCoreAnalyticsForRecognizedCommandIdentifier:appIdentifier:"

```
