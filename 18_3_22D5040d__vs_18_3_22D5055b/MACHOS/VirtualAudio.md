## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1267.404.0.0.0
-  __TEXT.__text: 0x48d7c0
-  __TEXT.__auth_stubs: 0x2570
+1267.406.30.2.0
+  __TEXT.__text: 0x48ddc8
+  __TEXT.__auth_stubs: 0x2530
   __TEXT.__objc_stubs: 0x740
   __TEXT.__init_offsets: 0x4c4
   __TEXT.__objc_methlist: 0x134
-  __TEXT.__gcc_except_tab: 0x543c4
+  __TEXT.__gcc_except_tab: 0x5445c
   __TEXT.__const: 0xb07de
-  __TEXT.__cstring: 0x276e1
+  __TEXT.__cstring: 0x27764
   __TEXT.__objc_classname: 0x34
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_capture: 0x158
-  __TEXT.__oslogstring: 0x4ce3a
+  __TEXT.__oslogstring: 0x4cf10
   __TEXT.__objc_methname: 0x5b9
   __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_reflstr: 0x4c

   __TEXT.__dof_VirtualAu: 0x303
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0xf390
+  __TEXT.__unwind_info: 0xf3c8
   __TEXT.__eh_frame: 0x7a8
-  __DATA_CONST.__auth_got: 0x12d0
+  __DATA_CONST.__auth_got: 0x12b0
   __DATA_CONST.__got: 0x450
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x23f78
+  __DATA_CONST.__const: 0x23ef8
   __DATA_CONST.__cfstring: 0x39c0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_selrefs: 0x208
   __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0x268
-  __DATA.__data: 0x338
+  __DATA.__data: 0x3b8
   __DATA.__bss: 0x21198
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/WirelessCoexManager.framework/WirelessCoexManager
   - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libMobileGestalt.dylib
-  - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9858
-  Symbols:   735
-  CStrings:  10499
+  Functions: 9865
+  Symbols:   731
+  CStrings:  10509
 
Symbols:
- _SMCCloseConnection
- _SMCGetKeyInfo
- _SMCOpenConnectionWithDefaultService
- _SMCWriteKeyWithKnownSize
CStrings:
+ "%25s:%-5d Closing connection to SMC for speaker power telemetry"
+ "%25s:%-5d Opening connection to SMC for speaker power telemetry"
+ "%25s:%-5d Stopping ref counted IODelegate"
+ "%25s:%-5d Unable to find/load SMC functions"
+ "/usr/lib/libSMC.dylib"
+ "@@ Strips Jan  7 2025 00:58:40"
+ "IODelegate.cpp"
+ "SMCCloseConnection"
+ "SMCGetKeyInfo"
+ "SMCOpenConnectionWithDefaultService"
+ "SMCWriteKeyWithKnownSize"
- "@@ Strips Dec 16 2024 14:00:04"

```
