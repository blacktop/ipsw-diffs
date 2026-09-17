## configd

> `/usr/libexec/configd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1446.0.0.0.0
-  __TEXT.__text: 0x6be88
+1452.0.0.0.0
+  __TEXT.__text: 0x6bf60
   __TEXT.__auth_stubs: 0x2450
   __TEXT.__objc_stubs: 0x1600
   __TEXT.__objc_methlist: 0xb64
   __TEXT.__const: 0x248
   __TEXT.__cstring: 0x3261
-  __TEXT.__oslogstring: 0x59ea
+  __TEXT.__oslogstring: 0x5a2c
   __TEXT.__objc_methname: 0x1c8d
   __TEXT.__objc_classname: 0x73
   __TEXT.__objc_methtype: 0x672

   - /usr/lib/libobjc.A.dylib
   Functions: 999
   Symbols:   819
-  CStrings:  1775
+  CStrings:  1776
 
Functions:
~ sub_10004c590 : 1372 -> 1588
CStrings:
+ "NetBIOS name: ptr query reply w/no hosts (query time = %ld.%3.3d)"
```
