## VirtualAudio

> `/Library/Audio/Plug-Ins/HAL/VirtualAudio.plugin/VirtualAudio`

```diff

-1267.110.1.0.0
-  __TEXT.__text: 0x4a1640
+1267.114.0.0.0
+  __TEXT.__text: 0x4a1bfc
   __TEXT.__auth_stubs: 0x2150
   __TEXT.__objc_stubs: 0x820
   __TEXT.__init_offsets: 0x4b0
   __TEXT.__objc_methlist: 0x2c4
   __TEXT.__const: 0xb0bff
-  __TEXT.__gcc_except_tab: 0x55368
-  __TEXT.__oslogstring: 0x4d332
-  __TEXT.__cstring: 0x27a9b
+  __TEXT.__gcc_except_tab: 0x55420
+  __TEXT.__oslogstring: 0x4d460
+  __TEXT.__cstring: 0x27ad1
   __TEXT.__objc_methname: 0xc28
   __TEXT.__objc_classname: 0x8d
   __TEXT.__objc_methtype: 0xbde
   __TEXT.__dof_VirtualAu: 0x303
   __TEXT.__dof_Aggregate: 0x5ec
   __TEXT.__dof_VirtualA0: 0x2aa
-  __TEXT.__unwind_info: 0xf5e0
+  __TEXT.__unwind_info: 0xf5f8
   __TEXT.__eh_frame: 0x60
   __DATA_CONST.__auth_got: 0x10b8
   __DATA_CONST.__got: 0x400
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x23498
+  __DATA_CONST.__const: 0x234f0
   __DATA_CONST.__cfstring: 0x3b80
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9811
+  Functions: 9813
   Symbols:   679
-  CStrings:  10685
+  CStrings:  10687
 
CStrings:
+ "%!s(MISSING):%!d(MISSING) AggregateDevice_ANCMonitor should have been destroyed in EnableANCMonitorIODelegate::Teardown().This may lead to unexpected ANC behaviour due to asynchronous device destruction."
+ "%!s(MISSING):%!d(MISSING) EXCEPTION (kAudioHardwareUnspecifiedError): \"Invalid location ID returned from device for property %!s(MISSING).\""
+ "@@ Strips Jul 12 2024 06:41:35"
+ "VirtualAudio PlugIn is not initialized yet. Initialization state: "
+ "preferredOutputRoute_v2"
- "@@ Strips Jul  1 2024 22:09:46"
- "DSP chain mutex"
- "preferredOutputRoute"

```
