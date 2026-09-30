## SiriSetup

> `/System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup`

```diff

-3402.41.1.0.0
-  __TEXT.__text: 0x38fac
-  __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_methlist: 0xd3c
-  __TEXT.__const: 0x1314
-  __TEXT.__cstring: 0x3fa8
-  __TEXT.__constg_swiftt: 0x27e4
-  __TEXT.__swift5_typeref: 0xba4
-  __TEXT.__swift5_reflstr: 0x1265
-  __TEXT.__swift5_fieldmd: 0x1058
+3404.19.1.0.0
+  __TEXT.__text: 0x3d4f8
+  __TEXT.__auth_stubs: 0x1090
+  __TEXT.__objc_methlist: 0x138c
+  __TEXT.__const: 0x13f4
+  __TEXT.__cstring: 0x3e78
+  __TEXT.__constg_swiftt: 0x2894
+  __TEXT.__swift5_typeref: 0xbca
+  __TEXT.__swift5_reflstr: 0x1295
+  __TEXT.__swift5_fieldmd: 0x1088
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_proto: 0x104
   __TEXT.__swift5_types: 0xc8
-  __TEXT.__swift5_capture: 0x5a4
+  __TEXT.__swift5_capture: 0x5f8
   __TEXT.__swift5_protos: 0x44
+  __TEXT.__swift_as_entry: 0x24
+  __TEXT.__swift_as_ret: 0x38
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0xd40
-  __TEXT.__eh_frame: 0x4d8
+  __TEXT.__unwind_info: 0xce8
+  __TEXT.__eh_frame: 0x5e8
   __TEXT.__objc_classname: 0x261
-  __TEXT.__objc_methname: 0x2f69
-  __TEXT.__objc_methtype: 0xc93
-  __TEXT.__objc_stubs: 0x7e0
-  __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0x250
+  __TEXT.__objc_methname: 0x30aa
+  __TEXT.__objc_methtype: 0xcaa
+  __TEXT.__objc_stubs: 0x820
+  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__const: 0x240
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad0
+  __DATA_CONST.__objc_selrefs: 0xe40
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x860
-  __AUTH_CONST.__auth_ptr: 0x370
-  __AUTH_CONST.__const: 0x2250
+  __AUTH_CONST.__auth_got: 0x850
+  __AUTH_CONST.__auth_ptr: 0x410
+  __AUTH_CONST.__const: 0x2348
   __AUTH_CONST.__cfstring: 0x2c0
-  __AUTH_CONST.__objc_const: 0x43a8
+  __AUTH_CONST.__objc_const: 0x38b0
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x3178
-  __AUTH.__data: 0xc90
-  __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0xf30
+  __AUTH.__objc_data: 0x3228
+  __AUTH.__data: 0xc98
+  __DATA.__objc_ivar: 0x68
+  __DATA.__data: 0xf38
   __DATA.__bss: 0xeb0
-  __DATA.__common: 0x9
+  __DATA.__common: 0x11
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVKit.framework/AVKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit
+  - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
   - /System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1299
-  Symbols:   578
-  CStrings:  1098
+  Functions: 1282
+  Symbols:   593
+  CStrings:  1108
 
Symbols:
+ _BYSetupAssistantNeedsToRun
+ _OBJC_CLASS_$_PRXActionCustomColors
+ _objc_retain_x3
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- __swift_FORCE_LOAD_$_swiftFileProvider
CStrings:
+ " fetch with error "
+ "@\"NSNumber\""
+ "Adding personaId to voice profile "
+ "Completed sharedUserId "
+ "Configuring Myriad and RMS for training"
+ "Dismiss enrollment from page: "
+ "SiriDataSharingStatus is unspecified, returning without setting"
+ "VOICE_TRAINING_NAV_TITLE_ONE"
+ "VOICE_TRAINING_NAV_TITLE_THREE"
+ "VOICE_TRAINING_NAV_TITLE_TWO"
+ "actionWithTitle:customColors:handler:"
+ "compactVoiceTriggerEnabled"
+ "compactVoiceTriggerEnabledOverride"
+ "convertToAudioTone:"
+ "getUserPreferredVoiceTriggerPhraseTypeForDeviceType:endpointId:error:"
+ "i24@0:8q16"
+ "initWithBackgroundColor:textColor:"
+ "isFirstTimeSetup"
+ "overrideCompactVoiceTriggerEnabled:"
+ "personaId"
+ "playSoundEffectWithAudioTone:"
+ "primaryAction"
+ "removeAction:"
+ "secondaryAction"
+ "skipTraining(notifyDelegate:)"
+ "systemBlueColor"
- "Completed sharedUserId fetch with error "
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "dismiss enrollment from page: "
- "invalid Collection: less than 'count' elements in collection"
- "isExpressTraining"

```
