## BuiltinAudioPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BuiltinAudioPlugin.driver/BuiltinAudioPlugin`

```diff

-240.34.0.0.0
-  __TEXT.__text: 0xf40
-  __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__objc_stubs: 0x1e0
+100.4.0.0.0
+  __TEXT.__text: 0x10b8
+  __TEXT.__auth_stubs: 0x1d0
+  __TEXT.__objc_stubs: 0x240
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__oslogstring: 0x54
-  __TEXT.__cstring: 0x17d
-  __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x158
+  __TEXT.__cstring: 0x1c6
+  __TEXT.__const: 0x18
+  __TEXT.__oslogstring: 0x6a
+  __TEXT.__gcc_except_tab: 0x17c
   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0x8
-  __TEXT.__objc_methname: 0xfe
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0xe8
-  __DATA_CONST.__got: 0x110
+  __TEXT.__objc_methname: 0x12d
+  __TEXT.__unwind_info: 0x98
+  __DATA_CONST.__auth_got: 0xf8
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__const: 0x60
-  __DATA_CONST.__cfstring: 0x220
+  __DATA_CONST.__cfstring: 0x240
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x78
+  __DATA.__objc_selrefs: 0x90
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x8
   __DATA.__bss: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3869EB58-A310-3EF3-9CAA-AE9B34D2D5A0
+  UUID: CA3F185B-910A-37F6-8995-5841C9485DFB
   Functions: 8
-  Symbols:   76
-  CStrings:  58
+  Symbols:   79
+  CStrings:  67
 
Symbols:
+ _OBJC_CLASS_$_NSString
+ __ZN4ASDT10IORegistry15GetObjectForKeyEPKcS2_
+ _objc_alloc
+ _objc_release_x9
- _objc_release_x1
Functions:
~ _BuiltinAudioFactory -> _BuiltinLogType : 232 -> 56
~ _BuiltinLogType -> sub_dd0 : 56 -> 52
~ sub_eb8 -> _BuiltinAudioFactory : 52 -> 296
~ sub_f8c -> sub_fcc : 60 -> 372
CStrings:
+ "%s: No devices for this platform."
+ "100.4"
+ "BuiltinAudioPlugin factory version %s"
+ "IODeviceTree:/product/audio"
+ "builtin-plugin-name"
+ "initWithData:encoding:"
+ "isEqualToString:"
+ "length"
- "BuiltinAudioFactory factory for AudioServerPlugin"

```
