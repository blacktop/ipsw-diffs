## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3605.30.1.0.0
-  __TEXT.__text: 0x742c8
-  __TEXT.__objc_methlist: 0x72dc
+3605.31.1.11.2
+  __TEXT.__text: 0x74b7c
+  __TEXT.__objc_methlist: 0x73f4
   __TEXT.__const: 0x124c
-  __TEXT.__cstring: 0xd0d2
+  __TEXT.__cstring: 0xd2a2
   __TEXT.__oslogstring: 0x9bc3
   __TEXT.__gcc_except_tab: 0xd00
   __TEXT.__dlopen_cstrs: 0x1bc

   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__swift_as_cont: 0x8c
-  __TEXT.__unwind_info: 0x2740
+  __TEXT.__unwind_info: 0x2760
   __TEXT.__eh_frame: 0xf58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1910
+  __DATA_CONST.__const: 0x1918
   __DATA_CONST.__objc_classlist: 0x3a8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3658
+  __DATA_CONST.__objc_selrefs: 0x36a0
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x2e0
+  __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x510
   __DATA_CONST.__got: 0xaa8
   __AUTH_CONST.__const: 0x14b0
-  __AUTH_CONST.__cfstring: 0x50a0
-  __AUTH_CONST.__objc_const: 0xb640
+  __AUTH_CONST.__cfstring: 0x51c0
+  __AUTH_CONST.__objc_const: 0xb7c0
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__auth_got: 0xbf0
+  __AUTH_CONST.__auth_got: 0xbf8
   __AUTH.__objc_data: 0x2190
   __AUTH.__data: 0x118
-  __DATA.__objc_ivar: 0x750
+  __DATA.__objc_ivar: 0x770
   __DATA.__data: 0x1710
   __DATA.__common: 0x270
   __DATA_DIRTY.__objc_data: 0x5f0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2988
-  Symbols:   4764
-  CStrings:  1867
+  Functions: 3011
+  Symbols:   4796
+  CStrings:  1876
 
Symbols:
+ -[SASRequestOptions isOdeonProxyVoiceTrigger]
+ -[SASRequestOptions setIsOdeonProxyVoiceTrigger:]
+ -[SASRequestOptions setTriggerDuration:]
+ -[SASRequestOptions setTriggeredPhrase:]
+ -[SASRequestOptions setTwoShotFeedbackDelay:]
+ -[SASRequestOptions triggerDuration]
+ -[SASRequestOptions triggeredPhrase]
+ -[SASRequestOptions twoShotFeedbackDelay]
+ -[SASSystemState _inNanoPressDemoMode]
+ -[SiriTVActivationSource _clearOdeonProxyVoiceTriggerState]
+ -[SiriTVActivationSource didRecognizeButtonSinglePressUp]
+ -[SiriTVActivationSource didRecognizeLongPressInteraction:]
+ -[SiriTVActivationSource setIsOdeonProxyVoiceTrigger:]
+ -[SiriTVActivationSource setTriggerDuration:]
+ -[SiriTVActivationSource setTriggeredPhrase:]
+ -[SiriTVActivationSource setTwoShotFeedbackDelay:]
+ -[SiriTVLongPressButtonContext isOdeonProxyVoiceTrigger]
+ -[SiriTVLongPressButtonContext setIsOdeonProxyVoiceTrigger:]
+ -[SiriTVLongPressButtonContext setTriggerDuration:]
+ -[SiriTVLongPressButtonContext setTriggeredPhrase:]
+ -[SiriTVLongPressButtonContext setTwoShotFeedbackDelay:]
+ -[SiriTVLongPressButtonContext triggerDuration]
+ -[SiriTVLongPressButtonContext triggeredPhrase]
+ -[SiriTVLongPressButtonContext twoShotFeedbackDelay]
+ _AFIsATVOnly
+ _OBJC_IVAR_$_SASRequestOptions._isOdeonProxyVoiceTrigger
+ _OBJC_IVAR_$_SASRequestOptions._triggerDuration
+ _OBJC_IVAR_$_SASRequestOptions._triggeredPhrase
+ _OBJC_IVAR_$_SASRequestOptions._twoShotFeedbackDelay
+ _OBJC_IVAR_$_SiriTVLongPressButtonContext._isOdeonProxyVoiceTrigger
+ _OBJC_IVAR_$_SiriTVLongPressButtonContext._triggerDuration
+ _OBJC_IVAR_$_SiriTVLongPressButtonContext._triggeredPhrase
+ _OBJC_IVAR_$_SiriTVLongPressButtonContext._twoShotFeedbackDelay
- -[SASSystemState _inPressDemoMode]
CStrings:
+ ";isOdeonProxyVoiceTrigger=%i;triggerDuration=%.3f;twoShotFeedbackDelay=%.3f;triggeredPhrase=%@"
+ "<SiriTVLongPressButtonContext contextOverride:%@ buttonDownTimestamp:%@,activeDeviceBluetoothIdentifier:%@,remoteType:%@,isListening:%d,isSourcePTTEligible:%d,isOdeonProxyVoiceTrigger:%d,triggerDuration:%f,twoShotFeedbackDelay:%f,triggeredPhrase:%@>"
+ "SASRequestOptionsIsOdeonProxyVoiceTriggerCodingKey"
+ "SASRequestOptionsTriggerDurationCodingKey"
+ "SASRequestOptionsTriggeredPhraseCodingKey"
+ "SASRequestOptionsTwoShotFeedbackDelayCodingKey"
+ "SiriTVRemoteTypeSiriRemote2026"
+ "isOdeonProxyVoiceTrigger"
+ "triggerDuration"
+ "triggeredPhrase"
+ "twoShotFeedbackDelay"
- "<SiriTVLongPressButtonContext contextOverride:%@ buttonDownTimestamp:%@,activeDeviceBluetoothIdentifier:%@,remoteType:%@,isListening:%d,isSourcePTTEligible:%d>"
- "PressDemoMode"
```
