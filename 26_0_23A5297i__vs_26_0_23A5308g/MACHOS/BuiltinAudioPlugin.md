## BuiltinAudioPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BuiltinAudioPlugin.driver/BuiltinAudioPlugin`

```diff

-100.4.0.0.0
-  __TEXT.__text: 0x10b8
+100.6.0.0.0
+  __TEXT.__text: 0x10d0
   __TEXT.__auth_stubs: 0x1d0
   __TEXT.__objc_stubs: 0x240
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__cstring: 0x1c6
+  __TEXT.__cstring: 0x1dd
   __TEXT.__const: 0x18
   __TEXT.__oslogstring: 0x6a
   __TEXT.__gcc_except_tab: 0x17c

   __TEXT.__objc_methname: 0x12d
   __TEXT.__unwind_info: 0x98
   __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__got: 0x120
   __DATA_CONST.__const: 0x60
-  __DATA_CONST.__cfstring: 0x240
+  __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E29ACF0C-53CC-3DBC-842E-4C1FD0D04BA5
+  UUID: F8ADA4AF-3380-34B1-B3E0-979418B8FBE5
   Functions: 8
-  Symbols:   79
-  CStrings:  67
+  Symbols:   80
+  CStrings:  69
 
Symbols:
+ _kASDTConfigKeyDeviceExclavesSensorName
Functions:
~ sub_1388 : 2740 -> 2764
CStrings:
+ "100.6"
+ "com.apple.sensors.test"
- "100.4"

```
