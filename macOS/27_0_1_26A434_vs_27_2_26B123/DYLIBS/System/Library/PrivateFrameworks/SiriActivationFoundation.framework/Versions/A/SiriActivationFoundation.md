## SiriActivationFoundation

> `/System/Library/PrivateFrameworks/SiriActivationFoundation.framework/Versions/A/SiriActivationFoundation`

```diff

-3600.55.37.14.1
-  __TEXT.__text: 0x3bad0
-  __TEXT.__objc_methlist: 0x280c
+3605.31.1.14.1
+  __TEXT.__text: 0x3c11c
+  __TEXT.__objc_methlist: 0x28f4
   __TEXT.__const: 0x205c
-  __TEXT.__cstring: 0x44ab
+  __TEXT.__cstring: 0x468b
   __TEXT.__oslogstring: 0xb5a
   __TEXT.__constg_swiftt: 0xc58
   __TEXT.__swift5_typeref: 0x15f4

   __TEXT.__swift_as_cont: 0xfc
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x1170
+  __TEXT.__unwind_info: 0x1178
   __TEXT.__eh_frame: 0x16d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x878
+  __DATA_CONST.__const: 0x880
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10c0
+  __DATA_CONST.__objc_selrefs: 0x1110
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x560
   __DATA_CONST.__got: 0x3d0
   __AUTH_CONST.__const: 0x2b98
-  __AUTH_CONST.__cfstring: 0x3b80
-  __AUTH_CONST.__objc_const: 0x5a18
+  __AUTH_CONST.__cfstring: 0x3cc0
+  __AUTH_CONST.__objc_const: 0x5bc0
   __AUTH_CONST.__objc_intobj: 0x810
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x798
+  __AUTH_CONST.__auth_got: 0x7a0
   __AUTH_CONST.__auth_ptr: 0x370
   __AUTH.__objc_data: 0x1f8
   __AUTH.__data: 0x138
-  __DATA.__objc_ivar: 0x35c
-  __DATA.__data: 0xe40
+  __DATA.__objc_ivar: 0x37c
+  __DATA.__data: 0xe30
   __DATA.__bss: 0x1220
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__data: 0xd68

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1894
-  Symbols:   2447
-  CStrings:  602
+  Functions: 1913
+  Symbols:   2484
+  CStrings:  612
 
Symbols:
+ -[SAFRequestOptions isOdeonProxyVoiceTrigger]
+ -[SAFRequestOptions setIsOdeonProxyVoiceTrigger:]
+ -[SAFRequestOptions setTriggerDuration:]
+ -[SAFRequestOptions setTriggeredPhrase:]
+ -[SAFRequestOptions setTwoShotFeedbackDelay:]
+ -[SAFRequestOptions triggerDuration]
+ -[SAFRequestOptions triggeredPhrase]
+ -[SAFRequestOptions twoShotFeedbackDelay]
+ -[SAFTVLongPressButtonContext copyWithZone:]
+ -[SAFTVLongPressButtonContext isOdeonProxyVoiceTrigger]
+ -[SAFTVLongPressButtonContext setIsOdeonProxyVoiceTrigger:]
+ -[SAFTVLongPressButtonContext setTriggerDuration:]
+ -[SAFTVLongPressButtonContext setTriggeredPhrase:]
+ -[SAFTVLongPressButtonContext setTwoShotFeedbackDelay:]
+ -[SAFTVLongPressButtonContext triggerDuration]
+ -[SAFTVLongPressButtonContext triggeredPhrase]
+ -[SAFTVLongPressButtonContext twoShotFeedbackDelay]
+ OBJC_IVAR_$_SAFRequestOptions._isOdeonProxyVoiceTrigger
+ OBJC_IVAR_$_SAFRequestOptions._triggerDuration
+ OBJC_IVAR_$_SAFRequestOptions._triggeredPhrase
+ OBJC_IVAR_$_SAFRequestOptions._twoShotFeedbackDelay
+ OBJC_IVAR_$_SAFTVLongPressButtonContext._isOdeonProxyVoiceTrigger
+ OBJC_IVAR_$_SAFTVLongPressButtonContext._triggerDuration
+ OBJC_IVAR_$_SAFTVLongPressButtonContext._triggeredPhrase
+ OBJC_IVAR_$_SAFTVLongPressButtonContext._twoShotFeedbackDelay
+ _AFIsATVOnly
+ __PROPERTIES_SAFSiriUnavailabilityStatus
+ _objc_msgSend$currentOrchestrationMode
+ _objc_msgSend$isOdeonProxyVoiceTrigger
+ _objc_msgSend$setIsOdeonProxyVoiceTrigger:
+ _objc_msgSend$setSourcePTTEligibility:
+ _objc_msgSend$setTriggerDuration:
+ _objc_msgSend$setTriggeredPhrase:
+ _objc_msgSend$setTwoShotFeedbackDelay:
+ _objc_msgSend$triggerDuration
+ _objc_msgSend$triggeredPhrase
+ _objc_msgSend$twoShotFeedbackDelay
CStrings:
+ ";isOdeonProxyVoiceTrigger=%i;triggerDuration=%.3f;twoShotFeedbackDelay=%.3f;triggeredPhrase=%@"
+ "<SiriTVLongPressButtonContext contextOverride:%@ buttonDownTimestamp:%@,activeDeviceBluetoothIdentifier:%@,remoteType:%@,isListening:%d,isSourcePTTEligible:%d,isOdeonProxyVoiceTrigger:%d,triggerDuration:%f,twoShotFeedbackDelay:%f,triggeredPhrase:%@>"
+ "SAFRequestOptionsIsOdeonProxyVoiceTriggerCodingKey"
+ "SAFRequestOptionsTriggerDurationCodingKey"
+ "SAFRequestOptionsTriggeredPhraseCodingKey"
+ "SAFRequestOptionsTwoShotFeedbackDelayCodingKey"
+ "SAFTVRemoteTypeSiriRemote2026"
+ "isOdeonProxyVoiceTrigger"
+ "triggerDuration"
+ "triggeredPhrase"
+ "twoShotFeedbackDelay"
- "<SiriTVLongPressButtonContext contextOverride:%@ buttonDownTimestamp:%@,activeDeviceBluetoothIdentifier:%@,remoteType:%@,isListening:%d,isSourcePTTEligible:%d>"
```
