## SiriActivationFoundation

> `/System/Library/PrivateFrameworks/SiriActivationFoundation.framework/SiriActivationFoundation`

```diff

-3605.30.1.0.0
-  __TEXT.__text: 0x387ec
-  __TEXT.__objc_methlist: 0x285c
+3605.31.1.11.2
+  __TEXT.__text: 0x38ce0
+  __TEXT.__objc_methlist: 0x291c
   __TEXT.__const: 0x205c
-  __TEXT.__cstring: 0x450b
+  __TEXT.__cstring: 0x46eb
   __TEXT.__oslogstring: 0xb8a
   __TEXT.__constg_swiftt: 0xc58
   __TEXT.__swift5_typeref: 0x1616

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8a8
+  __DATA_CONST.__const: 0x8b0
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1110
+  __DATA_CONST.__objc_selrefs: 0x1150
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x560
   __DATA_CONST.__got: 0x3e8
   __AUTH_CONST.__const: 0x2c08
-  __AUTH_CONST.__cfstring: 0x3bc0
-  __AUTH_CONST.__objc_const: 0x5a98
+  __AUTH_CONST.__cfstring: 0x3d00
+  __AUTH_CONST.__objc_const: 0x5c18
   __AUTH_CONST.__objc_intobj: 0x810
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x950
+  __AUTH_CONST.__auth_got: 0x958
   __AUTH.__objc_data: 0x1f8
   __AUTH.__data: 0x138
-  __DATA.__objc_ivar: 0x360
+  __DATA.__objc_ivar: 0x380
   __DATA.__data: 0xe60
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__data: 0xde0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1911
-  Symbols:   2092
-  CStrings:  606
+  Functions: 1927
+  Symbols:   2117
+  CStrings:  616
 
Symbols:
+ -[SAFRequestOptions isOdeonProxyVoiceTrigger]
+ -[SAFRequestOptions setIsOdeonProxyVoiceTrigger:]
+ -[SAFRequestOptions setTriggerDuration:]
+ -[SAFRequestOptions setTriggeredPhrase:]
+ -[SAFRequestOptions setTwoShotFeedbackDelay:]
+ -[SAFRequestOptions triggerDuration]
+ -[SAFRequestOptions triggeredPhrase]
+ -[SAFRequestOptions twoShotFeedbackDelay]
+ -[SAFTVLongPressButtonContext isOdeonProxyVoiceTrigger]
+ -[SAFTVLongPressButtonContext setIsOdeonProxyVoiceTrigger:]
+ -[SAFTVLongPressButtonContext setTriggerDuration:]
+ -[SAFTVLongPressButtonContext setTriggeredPhrase:]
+ -[SAFTVLongPressButtonContext setTwoShotFeedbackDelay:]
+ -[SAFTVLongPressButtonContext triggerDuration]
+ -[SAFTVLongPressButtonContext triggeredPhrase]
+ -[SAFTVLongPressButtonContext twoShotFeedbackDelay]
+ _AFIsATVOnly
+ _OBJC_IVAR_$_SAFRequestOptions._isOdeonProxyVoiceTrigger
+ _OBJC_IVAR_$_SAFRequestOptions._triggerDuration
+ _OBJC_IVAR_$_SAFRequestOptions._triggeredPhrase
+ _OBJC_IVAR_$_SAFRequestOptions._twoShotFeedbackDelay
+ _OBJC_IVAR_$_SAFTVLongPressButtonContext._isOdeonProxyVoiceTrigger
+ _OBJC_IVAR_$_SAFTVLongPressButtonContext._triggerDuration
+ _OBJC_IVAR_$_SAFTVLongPressButtonContext._triggeredPhrase
+ _OBJC_IVAR_$_SAFTVLongPressButtonContext._twoShotFeedbackDelay
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
