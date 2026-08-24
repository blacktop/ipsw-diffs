## iCloud

> `/System/Library/CoreServices/iCloud.app/Contents/MacOS/iCloud`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2710.116.0.0.0
-  __TEXT.__text: 0x18e58
+2710.120.0.0.0
+  __TEXT.__text: 0x18e90
   __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_stubs: 0x37e0
+  __TEXT.__objc_stubs: 0x3800
   __TEXT.__objc_methlist: 0xf48
   __TEXT.__const: 0xd0
   __TEXT.__gcc_except_tab: 0x584
-  __TEXT.__objc_methname: 0x44c4
+  __TEXT.__objc_methname: 0x44dc
   __TEXT.__oslogstring: 0x1a84
-  __TEXT.__cstring: 0x2c54
+  __TEXT.__cstring: 0x2c5c
   __TEXT.__objc_classname: 0xee
   __TEXT.__objc_methtype: 0x93a
   __TEXT.__ustring: 0x2a0
   __TEXT.__unwind_info: 0x4c0
   __DATA_CONST.__const: 0x948
-  __DATA_CONST.__cfstring: 0x2340
+  __DATA_CONST.__cfstring: 0x2360
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__auth_got: 0x200
   __DATA_CONST.__got: 0x430
   __DATA.__objc_const: 0x10c8
-  __DATA.__objc_selrefs: 0x10b8
+  __DATA.__objc_selrefs: 0x10c0
   __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x1e0

   - /usr/lib/libobjc.A.dylib
   Functions: 347
   Symbols:   206
-  CStrings:  1192
+  CStrings:  1194
 
Functions:
~ sub_100003394 : 200 -> 256
CStrings:
+ "pathForResource:ofType:"
+ "strings"
```
