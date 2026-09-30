## DOT Driver

> `/System/Library/ScreenReader/BrailleDrivers/DOT Driver.brailledriver/Contents/MacOS/DOT Driver`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1042.0.0.0.0
-  __TEXT.__text: 0x2dd8
-  __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__objc_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x71c
+1045.0.0.0.0
+  __TEXT.__text: 0x2c50
+  __TEXT.__auth_stubs: 0x210
+  __TEXT.__objc_stubs: 0xc60
+  __TEXT.__objc_methlist: 0x724
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x153
   __TEXT.__oslogstring: 0x205
-  __TEXT.__objc_methname: 0x11a6
+  __TEXT.__objc_methname: 0x11d4
   __TEXT.__objc_classname: 0xc5
   __TEXT.__objc_methtype: 0x668
-  __TEXT.__unwind_info: 0x108
+  __TEXT.__unwind_info: 0x100
   __DATA_CONST.__const: 0xb0
   __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x18

   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__auth_got: 0x110
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x9e0
-  __DATA.__objc_selrefs: 0x5b8
+  __DATA.__objc_const: 0x9e8
+  __DATA.__objc_selrefs: 0x5d0
   __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x2a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 74
-  Symbols:   55
-  CStrings:  338
+  Symbols:   57
+  CStrings:  341
 
Symbols:
+ _memcpy
+ _objc_retainAutorelease
Functions:
~ sub_115c : 536 -> 144
CStrings:
+ "brailleCellData"
+ "bytes"
+ "modelIdentifierForPlist"
```
