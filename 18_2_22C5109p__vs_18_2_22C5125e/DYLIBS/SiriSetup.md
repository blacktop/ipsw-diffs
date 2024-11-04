## SiriSetup

> `/System/Library/PrivateFrameworks/SiriSetup.framework/SiriSetup`

```diff

-3402.30.1.0.0
-  __TEXT.__text: 0x325cc
-  __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_methlist: 0xd2c
-  __TEXT.__const: 0x1224
-  __TEXT.__cstring: 0x3b78
-  __TEXT.__constg_swiftt: 0x268c
-  __TEXT.__swift5_typeref: 0xb08
-  __TEXT.__swift5_reflstr: 0x1165
-  __TEXT.__swift5_fieldmd: 0xf84
+3402.38.2.0.0
+  __TEXT.__text: 0x381b0
+  __TEXT.__auth_stubs: 0x1090
+  __TEXT.__objc_methlist: 0xd3c
+  __TEXT.__const: 0x1314
+  __TEXT.__cstring: 0x3f88
+  __TEXT.__constg_swiftt: 0x2794
+  __TEXT.__swift5_typeref: 0xb88
+  __TEXT.__swift5_reflstr: 0x1215
+  __TEXT.__swift5_fieldmd: 0x1028
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__swift5_capture: 0x418
-  __TEXT.__swift5_proto: 0xfc
-  __TEXT.__swift5_types: 0xc0
+  __TEXT.__swift5_proto: 0x104
+  __TEXT.__swift5_types: 0xc8
+  __TEXT.__swift5_capture: 0x518
   __TEXT.__swift5_protos: 0x44
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0xc90
-  __TEXT.__eh_frame: 0x4e4
+  __TEXT.__unwind_info: 0xd10
+  __TEXT.__eh_frame: 0x47c
   __TEXT.__objc_classname: 0x261
-  __TEXT.__objc_methname: 0x2ed5
+  __TEXT.__objc_methname: 0x2f69
   __TEXT.__objc_methtype: 0xc93
-  __TEXT.__objc_stubs: 0x7c0
-  __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__const: 0x200
-  __DATA_CONST.__objc_classlist: 0x158
+  __TEXT.__objc_stubs: 0x7e0
+  __DATA_CONST.__got: 0x3f0
+  __DATA_CONST.__const: 0x250
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaa0
+  __DATA_CONST.__objc_selrefs: 0xad0
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x7e0
-  __AUTH_CONST.__auth_ptr: 0x310
-  __AUTH_CONST.__const: 0x1f50
-  __AUTH_CONST.__cfstring: 0x2a0
-  __AUTH_CONST.__objc_const: 0x41f0
+  __AUTH_CONST.__auth_got: 0x850
+  __AUTH_CONST.__auth_ptr: 0x330
+  __AUTH_CONST.__const: 0x21a0
+  __AUTH_CONST.__cfstring: 0x2c0
+  __AUTH_CONST.__objc_const: 0x4348
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x30e8
-  __AUTH.__data: 0xb88
+  __AUTH.__objc_data: 0x3168
+  __AUTH.__data: 0xc60
   __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0xe70
-  __DATA.__bss: 0xdb0
-  __DATA.__common: 0x8
+  __DATA.__data: 0xf00
+  __DATA.__bss: 0xeb0
+  __DATA.__common: 0x9
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVKit.framework/AVKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1198
-  Symbols:   559
-  CStrings:  1065
+  Functions: 1284
+  Symbols:   577
+  CStrings:  1095
 
Symbols:
+ _MGGetSInt32Answer
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSThread
+ _SRSGetDeviceClass
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ _free
+ _malloc
CStrings:
+ " and iCloudAltDSID "
+ " configuration: "
+ "%!T(MISSING)ARGET_DEVICE_NAMES%!"(MISSING)
+ "(hasVoiceProfileInCloud = "
+ ") and set matching siri language for SiriSetup "
+ "), but no matching siri language was found"
+ "; returning key value"
+ "; siriEnabled = "
+ "; siriSharedUserId = "
+ "Apple Vision Pro"
+ "Completed sharedUserId fetch with error "
+ "DATA_SHARING_DETAIL"
+ "DeviceClassNumber"
+ "Fetching sharedUserId for iCloudAltDSID "
+ "Initializing Defaults for "
+ "No enrolled users yet, performing an owner sharedUserId lookup"
+ "Operation timed out"
+ "Storing voice profile with siriSharedUserId "
+ "Training manager was initialized w/o siriProfileId"
+ "_TtC9SiriSetup20DaemonSessionWrapper"
+ "_configuration"
+ "applying configuration: "
+ "com.apple.siri.setup.AssistantConnection"
+ "com.apple.siri.setup.default"
+ "could not find localizable string for key "
+ "daemonSession"
+ "getAudioSessionID:"
+ "init(enrollmentMode:navigationController:delegate:assistantConfiguration:)"
+ "init(hasVoiceProfileInCloud:siriEnabled:siriLanguage:siriSharedUserId:siriVoice:recognizeMyVoiceEnabled:voiceTriggerEnabled:siriInCallEnabled:siriDataSharingStatus:systemLanguage:)"
+ "initWithDomain:code:userInfo:"
+ "isMainThread"
+ "lastPlayedTryAgain"
+ "localizedStringForKey:gender:table:bundle:languageCode:"
+ "markEnrollmentSucceeded(_:)"
+ "retrieveLocalizedString(_:gender:localDevice:targetDevice:)"
+ "setValue:forKey:"
+ "system language was given ("
+ "v12@?0I8"
+ "valueForKey:"
+ "viewConfiguration"
- ", fetching sharedUserId for iCloudAltDSID "
- "DATA_SHARING_DETAIL_IPHONE"
- "DATA_SHARING_DETAIL_MAC"
- "INTRO_SECONDARY_MAC"
- "INTRO_SECONDARY_iOS"
- "Initializing Defaults"
- "No enrolled users yet, performing a owner sharedUserId lookup"
- "There are already enrolled users "
- "com.apple.siri.amnesia"
- "init(enrollmentMode:navigationController:delegate:)"

```
