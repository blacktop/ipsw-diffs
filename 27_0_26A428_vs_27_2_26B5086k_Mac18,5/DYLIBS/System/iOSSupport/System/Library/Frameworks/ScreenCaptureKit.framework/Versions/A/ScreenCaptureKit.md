## ScreenCaptureKit

> `/System/iOSSupport/System/Library/Frameworks/ScreenCaptureKit.framework/Versions/A/ScreenCaptureKit`

```diff

-740.62.1.0.0
-  __TEXT.__text: 0x3e944
+765.9.1.0.0
+  __TEXT.__text: 0x3e960
   __TEXT.__objc_methlist: 0x38a4
   __TEXT.__const: 0x21e
-  __TEXT.__oslogstring: 0x3e87
-  __TEXT.__cstring: 0x6848
+  __TEXT.__oslogstring: 0x3e48
+  __TEXT.__cstring: 0x6858
   __TEXT.__gcc_except_tab: 0x76c
   __TEXT.__swift5_typeref: 0x5f
   __TEXT.__constg_swiftt: 0x54

   __TEXT.__swift5_fieldmd: 0x74
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1390
+  __TEXT.__unwind_info: 0x1388
   __TEXT.__eh_frame: 0x68
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__got: 0x530
   __AUTH_CONST.__const: 0x278
   __AUTH_CONST.__cfstring: 0x28e0
-  __AUTH_CONST.__objc_const: 0x8a68
+  __AUTH_CONST.__objc_const: 0x8a88
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x780
+  __AUTH_CONST.__auth_got: 0x778
   __AUTH.__objc_data: 0x7a8
-  __DATA.__objc_ivar: 0x58c
+  __DATA.__objc_ivar: 0x590
   __DATA.__data: 0x810
   __DATA_DIRTY.__objc_data: 0x848
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1545
+  Functions: 1542
   Symbols:   3478
-  CStrings:  948
+  CStrings:  947
 
Symbols:
+ OBJC_IVAR_$_SCControlCenterManager._observerLock
- _notify_register_check
Functions:
~ -[RPThermalPressure startMonitoring] : 176 -> 160
~ -[SCControlCenterManager init] : 652 -> 656
~ ___43-[SCControlCenterManager registerObserver:]_block_invoke : 564 -> 592
~ ___45-[SCControlCenterManager unregisterObserver:]_block_invoke : 564 -> 592
~ -[SCControlCenterManager callObserver:] : 376 -> 404
~ ___59-[SCStream(SCContentSharing) startRemoteVideoReceiveQueue:]_block_invoke : 2676 -> 2736
~ ___59-[SCStream(SCContentSharing) startRemoteAudioReceiveQueue:]_block_invoke : 568 -> 636
~ ___64-[SCStream(SCContentSharing) startRemoteMicrophoneReceiveQueue:]_block_invoke : 552 -> 620
~ __59-[SCStream(SCContentSharing) startRemoteVideoReceiveQueue:]_block_invoke.cold.8 : 80 -> 96
~ __59-[SCStream(SCContentSharing) startRemoteVideoReceiveQueue:]_block_invoke.cold.9 : 96 -> 116
- __59-[SCStream(SCContentSharing) startRemoteVideoReceiveQueue:]_block_invoke.cold.10
~ __59-[SCStream(SCContentSharing) startRemoteAudioReceiveQueue:]_block_invoke.cold.2 : 80 -> 116
- __59-[SCStream(SCContentSharing) startRemoteAudioReceiveQueue:]_block_invoke.cold.3
~ __64-[SCStream(SCContentSharing) startRemoteMicrophoneReceiveQueue:]_block_invoke.cold.2 : 80 -> 116
- __64-[SCStream(SCContentSharing) startRemoteMicrophoneReceiveQueue:]_block_invoke.cold.3
CStrings:
+ " [DEBUG] %{public}s:%d streamOutput NOT found. Dropping frame"
- " [ERROR] %{public}s:%d stream output NOT found. Dropping frame"
- " [ERROR] %{public}s:%d streamOutput NOT found. Dropping frame"
```
