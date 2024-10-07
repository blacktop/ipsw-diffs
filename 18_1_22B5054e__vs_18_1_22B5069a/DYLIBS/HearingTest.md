## HearingTest

> `/System/Library/PrivateFrameworks/HearingTest.framework/HearingTest`

```diff

-210.41.0.0.0
-  __TEXT.__text: 0x9fb3c
-  __TEXT.__auth_stubs: 0x1630
-  __TEXT.__objc_methlist: 0x12c
-  __TEXT.__const: 0x2d40
-  __TEXT.__cstring: 0x236a
-  __TEXT.__constg_swiftt: 0x1d8c
-  __TEXT.__swift5_typeref: 0x1094
-  __TEXT.__swift5_proto: 0x1e0
-  __TEXT.__swift5_types: 0x128
-  __TEXT.__swift5_capture: 0x3308
-  __TEXT.__swift5_reflstr: 0x20e7
-  __TEXT.__swift5_fieldmd: 0x1bd8
-  __TEXT.__oslogstring: 0x6221
+210.50.2.0.0
+  __TEXT.__text: 0xa2ae4
+  __TEXT.__auth_stubs: 0x1740
+  __TEXT.__objc_methlist: 0x190
+  __TEXT.__const: 0x2df0
+  __TEXT.__cstring: 0x25ba
+  __TEXT.__constg_swiftt: 0x1eb8
+  __TEXT.__swift5_typeref: 0x112a
+  __TEXT.__swift5_proto: 0x1ec
+  __TEXT.__swift5_types: 0x13c
+  __TEXT.__swift5_capture: 0x2818
+  __TEXT.__swift5_reflstr: 0x2137
+  __TEXT.__swift5_fieldmd: 0x1c48
+  __TEXT.__oslogstring: 0x6a51
   __TEXT.__swift5_assocty: 0x2b0
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_mpenum: 0xd0
-  __TEXT.__unwind_info: 0x1700
-  __TEXT.__eh_frame: 0x1bf4
+  __TEXT.__unwind_info: 0x1768
+  __TEXT.__eh_frame: 0x1d84
   __TEXT.__objc_classname: 0x63
-  __TEXT.__objc_methname: 0xd02
+  __TEXT.__objc_methname: 0xde3
   __TEXT.__objc_methtype: 0x3f3
-  __DATA_CONST.__got: 0x4d0
+  __DATA_CONST.__got: 0x4f8
   __DATA_CONST.__const: 0x190
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x390
+  __DATA_CONST.__objc_selrefs: 0x400
   __DATA_CONST.__objc_protorefs: 0x28
-  __AUTH_CONST.__auth_got: 0xb18
-  __AUTH_CONST.__auth_ptr: 0x670
-  __AUTH_CONST.__const: 0xc4c8
-  __AUTH_CONST.__objc_const: 0x2aa8
-  __AUTH.__objc_data: 0xee8
-  __AUTH.__data: 0x1530
-  __DATA.__data: 0xf50
-  __DATA.__bss: 0x3a00
+  __AUTH_CONST.__auth_got: 0xba0
+  __AUTH_CONST.__auth_ptr: 0x678
+  __AUTH_CONST.__const: 0xa990
+  __AUTH_CONST.__objc_const: 0x2d00
+  __AUTH.__objc_data: 0x1088
+  __AUTH.__data: 0x16e0
+  __DATA.__data: 0xff0
+  __DATA.__bss: 0x3b80
   __DATA.__common: 0x31
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3134
-  Symbols:   364
-  CStrings:  888
+  Functions: 2975
+  Symbols:   380
+  CStrings:  955
 
Symbols:
+ _AVAudioSessionCategoryPlayback
+ _AVAudioSessionModeRaw
+ _OBJC_CLASS_$_AVAudioPlayer
+ _UISceneDidActivateNotification
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getErrorValue
+ _swift_getObjCClassFromMetadata
+ _swift_initStructMetadata
+ _swift_storeEnumTagSinglePayloadGeneric
- _UISceneWillEnterForegroundNotification
CStrings:
+ "Block not found!"
+ "Division by zero"
+ "Division results in an overflow"
+ "HTAudioRouteRequirementManager handler but AirPods out of ear caused route chamge, ignoring"
+ "HTAudioRouteRequirementManager handler route changed with both AirPods both in-ear, ending test"
+ "HTAudioRouteRequirementManager handler: %!{(MISSING)bool}d"
+ "HearingTest.HTAudioRouteRequirementManager"
+ "No Captured Ports"
+ "Swift/IntegerTypes.swift"
+ "UID"
+ "[%!{(MISSING)public}s] Flags count index out of range"
+ "[%!{(MISSING)public}s] audio session route change  - capture route BT ports if none"
+ "[%!{(MISSING)public}s] audio session route change  - no reason"
+ "[%!{(MISSING)public}s] audio session route change  - no userInfo"
+ "[%!{(MISSING)public}s] audio session route change reason: %!l(MISSING)u"
+ "[%!{(MISSING)public}s] audioPortValid no valid output found in %!s(MISSING)"
+ "[%!{(MISSING)public}s] audioPortValid valid output found in %!s(MISSING)"
+ "[%!{(MISSING)public}s] capture device ports %!s(MISSING)"
+ "[%!{(MISSING)public}s] cleanup notifications"
+ "[%!{(MISSING)public}s] deinit"
+ "[%!{(MISSING)public}s] failed to setup player! %!s(MISSING)"
+ "[%!{(MISSING)public}s] found route"
+ "[%!{(MISSING)public}s] found route - but it was already found previously"
+ "[%!{(MISSING)public}s] handleDeviceChanged device placement %!s(MISSING) inEar %!s(MISSING) "
+ "[%!{(MISSING)public}s] handleDeviceChanged device placement %!s(MISSING) outEar %!s(MISSING)"
+ "[%!{(MISSING)public}s] init"
+ "[%!{(MISSING)public}s] lost route"
+ "[%!{(MISSING)public}s] lost route - but it was already lost previously"
+ "[%!{(MISSING)public}s] no current captured output ports - attempting to capture session BT A2DP output ports"
+ "[%!{(MISSING)public}s] player playing"
+ "[%!{(MISSING)public}s] posted notification %!s(MISSING) on app activation"
+ "[%!{(MISSING)public}s] searching - expected %!l(MISSING)d ports, session port count: %!l(MISSING)d - port name sets are %!s(MISSING)"
+ "[%!{(MISSING)public}s] searching - expected port name list is empty"
+ "[%!{(MISSING)public}s] searching - session has no output names"
+ "[%!{(MISSING)public}s] searching - session has no outputs"
+ "[%!{(MISSING)public}s] searching for expected audio route"
+ "[%!{(MISSING)public}s] setup notifications"
+ "[%!{(MISSING)public}s] setupPlayer failed to start player! %!s(MISSING)"
+ "[%!{(MISSING)public}s] status: %!s(MISSING)"
+ "[%!{(MISSING)public}s] stop playing"
+ "[%!{(MISSING)public}s] update interruptions based on capture count - status: %!s(MISSING)"
+ "[%!{(MISSING)public}s] updateDevice given device with no identifier"
+ "[%!{(MISSING)public}s] updateDevice has no device identifer yet"
+ "[%!{(MISSING)public}s] updateDevice ignoring unknown identifier %!s(MISSING), expected %!s(MISSING)"
+ "_TtC11HearingTest30HTAudioRouteRequirementManager"
+ "_TtC11HearingTestP33_E1CF8936D0F3BEC6A29D15D29986B99912CapturedPort"
+ "_TtC11HearingTestP33_E1CF8936D0F3BEC6A29D15D29986B99914CapturedDevice"
+ "audioRouteRequirementManager"
+ "audioSessionRouteChangeHander:"
+ "bundleForClass:"
+ "capturedDevice"
+ "capturedPorts"
+ "continuationLock"
+ "continuationsCache"
+ "externalInterruptionHandler"
+ "initWithContentsOfURL:error:"
+ "isInterrupted"
+ "isPlaying"
+ "notifyTestResumed"
+ "pathForResource:ofType:"
+ "play"
+ "player"
+ "prepareToPlay"
+ "setActive:error:"
+ "setCategory:error:"
+ "setMode:error:"
+ "setNumberOfLoops:"
+ "stop"
+ "uid"
- "[%!{(MISSING)public}s] handleDeviceChanged device placement inEar %!s(MISSING)"
- "[%!{(MISSING)public}s] handleDeviceChanged device placement outEar %!s(MISSING)"
- "lastLoggedStatus"

```
