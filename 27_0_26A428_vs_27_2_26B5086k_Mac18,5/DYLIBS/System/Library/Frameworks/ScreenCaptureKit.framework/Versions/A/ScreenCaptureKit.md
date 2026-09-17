## ScreenCaptureKit

> `/System/Library/Frameworks/ScreenCaptureKit.framework/Versions/A/ScreenCaptureKit`

```diff

-740.62.1.0.0
-  __TEXT.__text: 0x3f470
+765.9.1.0.0
+  __TEXT.__text: 0x3f494
   __TEXT.__objc_methlist: 0x37ec
   __TEXT.__const: 0x21a
-  __TEXT.__oslogstring: 0x3e8c
-  __TEXT.__cstring: 0x6a75
+  __TEXT.__oslogstring: 0x3e4d
+  __TEXT.__cstring: 0x6a76
   __TEXT.__gcc_except_tab: 0x7d4
   __TEXT.__constg_swiftt: 0x54
   __TEXT.__swift5_typeref: 0x2e

   __TEXT.__swift5_fieldmd: 0x74
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x13c8
+  __TEXT.__unwind_info: 0x13c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__got: 0x538
   __AUTH_CONST.__const: 0xff8
   __AUTH_CONST.__cfstring: 0x2a60
-  __AUTH_CONST.__objc_const: 0x86c8
+  __AUTH_CONST.__objc_const: 0x86e8
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x658
+  __AUTH_CONST.__auth_got: 0x650
   __AUTH.__objc_data: 0x7a8
-  __DATA.__objc_ivar: 0x58c
+  __DATA.__objc_ivar: 0x590
   __DATA.__data: 0x730
   __DATA_DIRTY.__objc_data: 0x848
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1576
+  Functions: 1573
   Symbols:   3502
-  CStrings:  960
+  CStrings:  959
 
Symbols:
+ OBJC_IVAR_$_SCControlCenterManager._observerLock
- _notify_register_check
Functions:
~ -[RPThermalPressure startMonitoring] : 176 -> 160
~ -[SCControlCenterManager init] : 688 -> 692
~ ___43-[SCControlCenterManager registerObserver:]_block_invoke : 572 -> 600
~ ___45-[SCControlCenterManager unregisterObserver:]_block_invoke : 572 -> 600
~ -[SCControlCenterManager callObserver:] : 392 -> 428
~ ___59-[SCStream(SCContentSharing) startRemoteVideoReceiveQueue:]_block_invoke : 2764 -> 2824
~ ___59-[SCStream(SCContentSharing) startRemoteAudioReceiveQueue:]_block_invoke : 580 -> 648
~ ___64-[SCStream(SCContentSharing) startRemoteMicrophoneReceiveQueue:]_block_invoke : 564 -> 632
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
