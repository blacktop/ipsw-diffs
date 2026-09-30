## SiriRemembers

> `/System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers`

```diff

-3605.12.1.0.0
-  __TEXT.__text: 0xaf88c
+3605.13.1.0.0
+  __TEXT.__text: 0xb11a0
   __TEXT.__objc_methlist: 0x224
-  __TEXT.__const: 0x9b54
-  __TEXT.__cstring: 0x33d1
-  __TEXT.__oslogstring: 0x3f25
-  __TEXT.__constg_swiftt: 0x203c
-  __TEXT.__swift5_typeref: 0x28c1
-  __TEXT.__swift5_reflstr: 0x12c2
-  __TEXT.__swift5_fieldmd: 0x25c0
+  __TEXT.__const: 0x9bc4
+  __TEXT.__cstring: 0x3461
+  __TEXT.__oslogstring: 0x4165
+  __TEXT.__constg_swiftt: 0x209c
+  __TEXT.__swift5_typeref: 0x28f9
+  __TEXT.__swift5_reflstr: 0x12d2
+  __TEXT.__swift5_fieldmd: 0x25f8
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_proto: 0x85c
-  __TEXT.__swift5_types: 0x2b4
+  __TEXT.__swift5_types: 0x2bc
   __TEXT.__swift5_assocty: 0x2d0
-  __TEXT.__swift5_capture: 0xc60
+  __TEXT.__swift5_capture: 0xccc
   __TEXT.__swift5_mpenum: 0x30
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__unwind_info: 0x3668
-  __TEXT.__eh_frame: 0x4d48
+  __TEXT.__unwind_info: 0x36f8
+  __TEXT.__eh_frame: 0x4d70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x718
+  __DATA_CONST.__objc_selrefs: 0x748
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x7428
-  __AUTH_CONST.__objc_const: 0x1468
-  __AUTH_CONST.__auth_got: 0x17e8
-  __AUTH.__data: 0x4c8
-  __DATA.__data: 0x1510
+  __AUTH_CONST.__const: 0x7648
+  __AUTH_CONST.__objc_const: 0x1540
+  __AUTH_CONST.__auth_got: 0x1810
+  __AUTH.__data: 0x570
+  __DATA.__data: 0x1550
   __DATA.__common: 0xa8
   __DATA_DIRTY.__objc_data: 0x118
   __DATA_DIRTY.__data: 0x2c18

   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal
+  - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5133
-  Symbols:   1822
-  CStrings:  548
+  Functions: 5189
+  Symbols:   1842
+  CStrings:  555
 
Symbols:
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterRemoveObserver
+ _NSStringFromAFSiriOrchestrationMode
+ _NSStringFromAFSiriUnavailabilityReasons
+ _OBJC_CLASS_$_AFSiriAvailability
+ __DATA__TtC13SiriRemembersP33_9FF6230672138D50B412B1ABD10EC6DE20CapabilitiesObserver
+ __IVARS__TtC13SiriRemembersP33_9FF6230672138D50B412B1ABD10EC6DE20CapabilitiesObserver
+ __METACLASS_DATA__TtC13SiriRemembersP33_9FF6230672138D50B412B1ABD10EC6DE20CapabilitiesObserver
+ _objc_msgSend$desiredOrchestrationMode
+ _objc_msgSend$fromPreferences
+ _objc_msgSend$isAvailable
+ _objc_msgSend$missingDesiredCapabilitiesFor:
+ _objc_msgSend$siriLocale
+ _objc_msgSend$unavailabilityReasons
+ _symbolic SbSgIgl_
+ _symbolic _____ 13SiriRemembers0aB20TranscriptForwardingO
+ _symbolic _____ 13SiriRemembers20CapabilitiesObserver33_9FF6230672138D50B412B1ABD10EC6DELLC
+ _symbolic _____XDXMT 13SiriRemembers20CapabilitiesObserver33_9FF6230672138D50B412B1ABD10EC6DELLC
+ _symbolic _____ySbSgG 13SiriRemembers6AtomicC
CStrings:
+ "SiriRemembersDonationFromAppIntentsListener: ignored event since Siri is not orchestrating on Linwood"
+ "TranscriptForwarding: AFSiriAvailability.fromPreferences() is nil, reading from app.intents (context=%{public}s)"
+ "TranscriptForwarding: allowTranscriptDonationForward is off, reading from app.intents (context=%{public}s)"
+ "TranscriptForwarding: isEnabled=%{bool}d, context=%{public}s, desiredOrchestrationMode=%{public}s, isAvailable=%{bool}d, siriLocale=%{public}s, unavailabilityReasons=%{public}s, missingLinwoodCapabilities=%{public}s"
+ "capabilitiesDidChange"
+ "com.apple.SiriRemembers.TranscriptForwarding"
+ "com.apple.siri.orchestration.capabilities.didChange"
```
