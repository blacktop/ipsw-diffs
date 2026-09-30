## SpeechRecognitionCore

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/SpeechRecognitionCore`

```diff

-6.3.68.2.0
-  __TEXT.__text: 0x11c80
-  __TEXT.__auth_stubs: 0xf90
-  __TEXT.__objc_methlist: 0x7ec
-  __TEXT.__cstring: 0x1448
-  __TEXT.__gcc_except_tab: 0x104c
+6.3.68.4.0
+  __TEXT.__text: 0x11524
+  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__objc_methlist: 0x6b4
+  __TEXT.__cstring: 0x13f8
+  __TEXT.__gcc_except_tab: 0x1034
   __TEXT.__const: 0xea
   __TEXT.__oslogstring: 0x470
   __TEXT.__ustring: 0xc
   __TEXT.__swift5_typeref: 0x28
   __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__unwind_info: 0x950
-  __TEXT.__objc_classname: 0x122
-  __TEXT.__objc_methname: 0x1390
-  __TEXT.__objc_methtype: 0x562
-  __TEXT.__objc_stubs: 0x9e0
-  __DATA_CONST.__got: 0x148
+  __TEXT.__unwind_info: 0x940
+  __TEXT.__objc_classname: 0x115
+  __TEXT.__objc_methname: 0xe90
+  __TEXT.__objc_methtype: 0x520
+  __TEXT.__objc_stubs: 0x7c0
+  __DATA_CONST.__got: 0x138
   __DATA_CONST.__const: 0x468
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f8
+  __DATA_CONST.__objc_selrefs: 0x410
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x7d8
+  __DATA_CONST.__objc_superrefs: 0x30
+  __AUTH_CONST.__auth_got: 0x7c0
   __AUTH_CONST.__const: 0x4f0
-  __AUTH_CONST.__cfstring: 0xcc0
-  __AUTH_CONST.__objc_const: 0xf40
-  __AUTH.__objc_data: 0x230
+  __AUTH_CONST.__cfstring: 0xc20
+  __AUTH_CONST.__objc_const: 0xcc0
+  __AUTH.__objc_data: 0x1e0
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0xa4
+  __DATA.__objc_ivar: 0x80
   __DATA.__data: 0x498
   __DATA.__bss: 0xe8
   __DATA.__common: 0x28

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0358A838-4E28-3EF9-B552-97F38AD94F8C
-  Functions: 478
-  Symbols:   1541
-  CStrings:  685
+  UUID: B0842282-0189-3B56-881C-273F4B52842B
+  Functions: 454
+  Symbols:   1453
+  CStrings:  623
 
Symbols:
- +[SRDMachTime supportsSecureCoding]
- -[SRDMachTime encodeWithCoder:]
- -[SRDMachTime initWithCoder:]
- -[SRDMachTime initWithMachTime:]
- -[SRDMachTime mach_time]
- -[SRDMachTime setMach_time:]
- -[SRDTranscriptionResult combineTokens:isLocaleWithNoSpaceSeparator:]
- -[SRDTranscriptionResult locale]
- -[SRDTranscriptionResult setLocale:]
- -[SRDTranscriptionResult setTimeAsrResultReceived:]
- -[SRDTranscriptionResult setTimeCommandExecutionEnded:]
- -[SRDTranscriptionResult setTimeCommandExecutionStarted:]
- -[SRDTranscriptionResult setTimeMatchedUtteranceSilenceStart:]
- -[SRDTranscriptionResult setTimeSRDResponseSent:]
- -[SRDTranscriptionResult setTimeUtteranceEnd:]
- -[SRDTranscriptionResult setTimeUtteranceStart:]
- -[SRDTranscriptionResult timeAsrResultReceived]
- -[SRDTranscriptionResult timeCommandExecutionEnded]
- -[SRDTranscriptionResult timeCommandExecutionStarted]
- -[SRDTranscriptionResult timeMatchedUtteranceSilenceStart]
- -[SRDTranscriptionResult timeSRDResponseSent]
- -[SRDTranscriptionResult timeUtteranceEnd]
- -[SRDTranscriptionResult timeUtteranceStart]
- -[SRDTranscriptionResult updateMatchedUtteranceSilenceStart:isLocaleWithNoSpaceSeparator:]
- _OBJC_CLASS_$_NSMutableString
- _OBJC_CLASS_$_SRDMachTime
- _OBJC_IVAR_$_SRDMachTime._mach_time
- _OBJC_IVAR_$_SRDTranscriptionResult._locale
- _OBJC_IVAR_$_SRDTranscriptionResult._timeAsrResultReceived
- _OBJC_IVAR_$_SRDTranscriptionResult._timeCommandExecutionEnded
- _OBJC_IVAR_$_SRDTranscriptionResult._timeCommandExecutionStarted
- _OBJC_IVAR_$_SRDTranscriptionResult._timeMatchedUtteranceSilenceStart
- _OBJC_IVAR_$_SRDTranscriptionResult._timeSRDResponseSent
- _OBJC_IVAR_$_SRDTranscriptionResult._timeUtteranceEnd
- _OBJC_IVAR_$_SRDTranscriptionResult._timeUtteranceStart
- _OBJC_METACLASS_$_SRDMachTime
- __OBJC_$_CLASS_METHODS_SRDMachTime
- __OBJC_$_CLASS_PROP_LIST_SRDMachTime
- __OBJC_$_INSTANCE_METHODS_SRDMachTime
- __OBJC_$_INSTANCE_VARIABLES_SRDMachTime
- __OBJC_$_PROP_LIST_SRDMachTime
- __OBJC_CLASS_PROTOCOLS_$_SRDMachTime
- __OBJC_CLASS_RO_$_SRDMachTime
- __OBJC_METACLASS_RO_$_SRDMachTime
- _objc_enumerationMutation
- _objc_msgSend$appendString:
- _objc_msgSend$caseInsensitiveCompare:
- _objc_msgSend$combineTokens:isLocaleWithNoSpaceSeparator:
- _objc_msgSend$count
- _objc_msgSend$countByEnumeratingWithState:objects:count:
- _objc_msgSend$decodeInt64ForKey:
- _objc_msgSend$encodeInt64:forKey:
- _objc_msgSend$lastObject
- _objc_msgSend$mach_time
- _objc_msgSend$nBestResults
- _objc_msgSend$objectAtIndexedSubscript:
- _objc_msgSend$setMach_time:
- _objc_msgSend$setTimeMatchedUtteranceSilenceStart:
- _objc_msgSend$silenceStart
- _objc_msgSend$timeMatchedUtteranceSilenceStart
- _objc_msgSend$tokenName
- _objc_msgSend$updateMatchedUtteranceSilenceStart:isLocaleWithNoSpaceSeparator:
- _objc_retain_x25
- _objc_retain_x27
CStrings:
+ "@80@0:8@16d24d32d40d48B56B60@64@72"
+ "Td,N,V_end"
+ "Td,N,V_silenceStart"
+ "Td,N,V_start"
- "@\"NSLocale\""
- "@\"SRDMachTime\""
- "@24@0:8Q16"
- "@28@0:8@16B24"
- "@80@0:8@16@24@32@40d48B56B60@64@72"
- "SRDMachTime"
- "T@\"NSLocale\",&,N,V_locale"
- "T@\"SRDMachTime\",&,N,V_end"
- "T@\"SRDMachTime\",&,N,V_silenceStart"
- "T@\"SRDMachTime\",&,N,V_start"
- "T@\"SRDMachTime\",&,N,V_timeAsrResultReceived"
- "T@\"SRDMachTime\",&,N,V_timeCommandExecutionEnded"
- "T@\"SRDMachTime\",&,N,V_timeCommandExecutionStarted"
- "T@\"SRDMachTime\",&,N,V_timeMatchedUtteranceSilenceStart"
- "T@\"SRDMachTime\",&,N,V_timeSRDResponseSent"
- "T@\"SRDMachTime\",&,N,V_timeUtteranceEnd"
- "T@\"SRDMachTime\",&,N,V_timeUtteranceStart"
- "TQ,N,V_mach_time"
- "_mach_time"
- "_timeAsrResultReceived"
- "_timeCommandExecutionEnded"
- "_timeCommandExecutionStarted"
- "_timeMatchedUtteranceSilenceStart"
- "_timeSRDResponseSent"
- "_timeUtteranceEnd"
- "_timeUtteranceStart"
- "appendString:"
- "asrResultReceived"
- "caseInsensitiveCompare:"
- "combineTokens:isLocaleWithNoSpaceSeparator:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "decodeInt64ForKey:"
- "encodeInt64:forKey:"
- "initWithMachTime:"
- "kUInt64MachTime"
- "lastObject"
- "mach_time"
- "objectAtIndexedSubscript:"
- "setLocale:"
- "setMach_time:"
- "setTimeAsrResultReceived:"
- "setTimeCommandExecutionEnded:"
- "setTimeCommandExecutionStarted:"
- "setTimeMatchedUtteranceSilenceStart:"
- "setTimeSRDResponseSent:"
- "setTimeUtteranceEnd:"
- "setTimeUtteranceStart:"
- "srdResponseSent"
- "timeAsrResultReceived"
- "timeCommandExecutionEnded"
- "timeCommandExecutionStarted"
- "timeMatchedUtteranceSilenceStart"
- "timeSRDResponseSent"
- "timeUtteranceEnd"
- "timeUtteranceStart"
- "updateMatchedUtteranceSilenceStart:isLocaleWithNoSpaceSeparator:"
- "utteranceEnd"
- "utteranceStart"
- "v28@0:8@16B24"

```
