## ParrotAudioPlugin

> `/System/Library/Templates/Data/Library/Audio/Plug-Ins/HAL/ParrotAudioPlugin.driver/Contents/MacOS/ParrotAudioPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-400.29.0.0.0
-  __TEXT.__text: 0x24464
+400.30.0.0.0
+  __TEXT.__text: 0x2456c
   __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_stubs: 0x25c0
+  __TEXT.__objc_stubs: 0x25e0
   __TEXT.__objc_methlist: 0xea4
-  __TEXT.__gcc_except_tab: 0x32c8
-  __TEXT.__objc_methname: 0x2ba9
+  __TEXT.__gcc_except_tab: 0x32f8
+  __TEXT.__objc_methname: 0x2bb9
   __TEXT.__objc_classname: 0x32e
   __TEXT.__objc_methtype: 0x91e
   __TEXT.__cstring: 0x1768
   __TEXT.__const: 0x592
-  __TEXT.__oslogstring: 0x1fcd
+  __TEXT.__oslogstring: 0x2024
   __TEXT.__unwind_info: 0xf80
   __DATA_CONST.__const: 0x1060
   __DATA_CONST.__cfstring: 0x880

   __DATA_CONST.__auth_got: 0x3f0
   __DATA_CONST.__got: 0x1a8
   __DATA.__objc_const: 0x1e68
-  __DATA.__objc_selrefs: 0xb98
+  __DATA.__objc_selrefs: 0xba0
   __DATA.__objc_ivar: 0xec
   __DATA.__objc_data: 0x9b0
   __DATA.__data: 0x148

   - /usr/lib/libobjc.A.dylib
   Functions: 819
   Symbols:   469
-  CStrings:  976
+  CStrings:  979
 
Functions:
~ sub_683c : 3716 -> 3980
CStrings:
+ "MATTapStreamEnabled = %d"
+ "MATTapStreamEnabled has no persisted value; defaulting to YES"
+ "setBool:forKey:"
```
