## ScreenCaptureKit

> `/System/Library/Frameworks/ScreenCaptureKit.framework/ScreenCaptureKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-740.63.1.2.0
-  __TEXT.__text: 0x364f0
+765.9.1.0.0
+  __TEXT.__text: 0x365b0
   __TEXT.__objc_methlist: 0x386c
   __TEXT.__const: 0x1fe
-  __TEXT.__oslogstring: 0x3c42
+  __TEXT.__oslogstring: 0x3c03
   __TEXT.__cstring: 0x5cd8
   __TEXT.__gcc_except_tab: 0x55c
   __TEXT.__swift5_typeref: 0x5f

   __TEXT.__swift5_fieldmd: 0x74
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x11c8
+  __TEXT.__unwind_info: 0x11b8
   __TEXT.__eh_frame: 0x68
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2300
+  __DATA_CONST.__objc_selrefs: 0x2308
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x5c8
+  __DATA_CONST.__got: 0x5d0
   __AUTH_CONST.__const: 0x298
   __AUTH_CONST.__cfstring: 0x2600
-  __AUTH_CONST.__objc_const: 0x8b30
+  __AUTH_CONST.__objc_const: 0x8b50
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH_CONST.__auth_got: 0x6c8
   __AUTH.__objc_data: 0xf00
-  __DATA.__objc_ivar: 0x5a0
+  __DATA.__objc_ivar: 0x5a4
   __DATA.__data: 0x818
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1456
-  Symbols:   3366
-  CStrings:  871
+  Functions: 1453
+  Symbols:   3368
+  CStrings:  870
 
Symbols:
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_IVAR_$_SCControlCenterManager._observerLock
+ _objc_msgSend$processInfo
- _notify_register_check
Functions:
~ -[SCContentFilter setContentsAndStreamTypeEmbedded] : 800 -> 956
~ -[RPThermalPressure startMonitoring] : 176 -> 160
~ -[SCControlCenterManager init] : 652 -> 656
~ ___43-[SCControlCenterManager registerObserver:]_block_invoke : 564 -> 592
~ ___45-[SCControlCenterManager unregisterObserver:]_block_invoke : 564 -> 592
~ -[SCControlCenterManager callObserver:] : 376 -> 404
~ ___59-[SCStream(SCContentSharing) startRemoteVideoReceiveQueue:]_block_invoke : 2008 -> 2064
~ ___59-[SCStream(SCContentSharing) startRemoteAudioReceiveQueue:]_block_invoke : 568 -> 636
~ ___64-[SCStream(SCContentSharing) startRemoteMicrophoneReceiveQueue:]_block_invoke : 552 -> 620
~ ___59-[SCStream(SCContentSharing) startRemoteVideoReceiveQueue:]_block_invoke.cold.8 : 76 -> 88
~ ___59-[SCStream(SCContentSharing) startRemoteVideoReceiveQueue:]_block_invoke.cold.9 : 88 -> 96
~ ___59-[SCStream(SCContentSharing) startRemoteVideoReceiveQueue:]_block_invoke.cold.10 : 96 -> 112
- ___59-[SCStream(SCContentSharing) startRemoteVideoReceiveQueue:]_block_invoke.cold.11
~ ___59-[SCStream(SCContentSharing) startRemoteAudioReceiveQueue:]_block_invoke.cold.2 : 76 -> 112
- ___59-[SCStream(SCContentSharing) startRemoteAudioReceiveQueue:]_block_invoke.cold.3
~ ___64-[SCStream(SCContentSharing) startRemoteMicrophoneReceiveQueue:]_block_invoke.cold.2 : 76 -> 112
- ___64-[SCStream(SCContentSharing) startRemoteMicrophoneReceiveQueue:]_block_invoke.cold.3
CStrings:
+ " [DEBUG] %{public}s:%d streamOutput NOT found. Dropping frame"
- " [ERROR] %{public}s:%d stream output NOT found. Dropping frame"
- " [ERROR] %{public}s:%d streamOutput NOT found. Dropping frame"
```
