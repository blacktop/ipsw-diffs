## BuiltinAudioPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BuiltinAudioPlugin.driver/BuiltinAudioPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-200.16.0.0.0
-  __TEXT.__text: 0x1284
-  __TEXT.__auth_stubs: 0x1e0
+200.17.0.0.0
+  __TEXT.__text: 0x12dc
+  __TEXT.__auth_stubs: 0x1f0
   __TEXT.__objc_stubs: 0x260
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x44
   __TEXT.__cstring: 0x261
   __TEXT.__const: 0x20
   __TEXT.__oslogstring: 0x74
-  __TEXT.__gcc_except_tab: 0x198
+  __TEXT.__gcc_except_tab: 0x1a4
   __TEXT.__objc_classname: 0x26
   __TEXT.__objc_methtype: 0x8
   __TEXT.__objc_methname: 0x13d

   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__auth_got: 0x108
   __DATA_CONST.__got: 0x138
   __DATA.__objc_const: 0x120
   __DATA.__objc_selrefs: 0x98

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 9
-  Symbols:   87
+  Symbols:   88
   CStrings:  56
 
Symbols:
+ _objc_release_x23
Functions:
~ sub_1178 : 3192 -> 3280
CStrings:
+ "200.17"
- "200.16"
```
