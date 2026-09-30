## com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-747.0.2.502.1
-  __TEXT.__text: 0x4eff0
-  __TEXT.__auth_stubs: 0x1010
-  __TEXT.__objc_stubs: 0x70e0
+747.0.6.0.0
+  __TEXT.__text: 0x4ef90
+  __TEXT.__auth_stubs: 0x1000
+  __TEXT.__objc_stubs: 0x7080
   __TEXT.__objc_methlist: 0x30b8
   __TEXT.__const: 0x150
   __TEXT.__gcc_except_tab: 0x1adc
-  __TEXT.__cstring: 0x43fc
-  __TEXT.__objc_methname: 0x7c49
+  __TEXT.__cstring: 0x43ff
+  __TEXT.__objc_methname: 0x7bf4
   __TEXT.__oslogstring: 0x836f
   __TEXT.__objc_classname: 0x757
   __TEXT.__objc_methtype: 0x1176
   __TEXT.__unwind_info: 0xcf8
   __DATA_CONST.__const: 0x1560
-  __DATA_CONST.__cfstring: 0x3d20
+  __DATA_CONST.__cfstring: 0x3d40
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x818
+  __DATA_CONST.__auth_got: 0x810
   __DATA_CONST.__got: 0x7c0
-  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x5470
-  __DATA.__objc_selrefs: 0x2040
+  __DATA.__objc_selrefs: 0x2028
   __DATA.__objc_ivar: 0x2d0
   __DATA.__objc_data: 0x1220
   __DATA.__data: 0x5a8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 1420
-  Symbols:   511
-  CStrings:  2880
+  Symbols:   510
+  CStrings:  2878
 
Symbols:
- _memset
Functions:
~ sub_100015498 : 540 -> 444
CStrings:
+ "%d"
+ "appendFormat:"
- "decimalDigitCharacterSet"
- "invertedSet"
- "rangeOfCharacterFromSet:options:"
- "stringWithCharacters:length:"
```
