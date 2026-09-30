## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1267.338.0.0.0
-  __TEXT.__text: 0x48ba08
-  __TEXT.__auth_stubs: 0x2500
+1267.402.0.0.0
+  __TEXT.__text: 0x48d3d0
+  __TEXT.__auth_stubs: 0x2570
   __TEXT.__objc_stubs: 0x740
-  __TEXT.__init_offsets: 0x4c0
+  __TEXT.__init_offsets: 0x4c4
   __TEXT.__objc_methlist: 0x134
-  __TEXT.__gcc_except_tab: 0x54174
-  __TEXT.__const: 0xb07be
-  __TEXT.__cstring: 0x27688
+  __TEXT.__gcc_except_tab: 0x543a8
+  __TEXT.__const: 0xb07de
+  __TEXT.__cstring: 0x276e1
   __TEXT.__objc_classname: 0x34
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_capture: 0x158
-  __TEXT.__oslogstring: 0x4cd6e
+  __TEXT.__oslogstring: 0x4cde4
   __TEXT.__objc_methname: 0x5b9
   __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_reflstr: 0x4c

   __TEXT.__dof_VirtualAu: 0x303
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0xf2e0
+  __TEXT.__unwind_info: 0xf388
   __TEXT.__eh_frame: 0x7a8
-  __DATA_CONST.__auth_got: 0x1298
-  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__auth_got: 0x12d0
+  __DATA_CONST.__got: 0x450
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x23db8
+  __DATA_CONST.__const: 0x23f18
   __DATA_CONST.__cfstring: 0x39c0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0x268
   __DATA.__data: 0x338
-  __DATA.__bss: 0x211a0
+  __DATA.__bss: 0x211a8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /System/Library/PrivateFrameworks/TimeSync.framework/TimeSync
+  - /System/Library/PrivateFrameworks/VoiceProcessor.framework/VoiceProcessor
   - /System/Library/PrivateFrameworks/WirelessCoexManager.framework/WirelessCoexManager
   - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libMobileGestalt.dylib
+  - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9830
-  Symbols:   727
-  CStrings:  10493
+  Functions: 9854
+  Symbols:   735
+  CStrings:  10498
 
Symbols:
+ _SMCCloseConnection
+ _SMCGetKeyInfo
+ _SMCOpenConnectionWithDefaultService
+ _SMCWriteKeyWithKnownSize
+ __dispatch_source_type_timer
+ _dispatch_activate
+ _dispatch_source_cancel
+ _dispatch_source_set_timer
CStrings:
+ "%25s:%-5d EXCEPTION (std::logic_error): \"Failure to create the timer source\""
+ "%25s:%-5d Failed to open SMC connection."
+ "@@ Strips Dec  6 2024 01:51:36"
+ "Failure to create the timer source"
+ "Speaker Power Collector"
+ "SpeakerPowerUsageIODelegate.mm"
+ "SpeakerProtection_HAL_Interface.mm"
- "@@ Strips Nov 10 2024 03:42:45"
- "SpeakerProtection_HAL_Interface.cpp"

```
