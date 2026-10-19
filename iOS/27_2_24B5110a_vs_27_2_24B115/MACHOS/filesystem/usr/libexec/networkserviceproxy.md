## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 990.40.2.0.0
-  __TEXT.__text: 0xc0888
+  __TEXT.__text: 0xc08dc
   __TEXT.__auth_stubs: 0x18e0
   __TEXT.__objc_stubs: 0xd260
   __TEXT.__objc_methlist: 0x5044
   __TEXT.__const: 0x2a8
   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__gcc_except_tab: 0x3898
-  __TEXT.__oslogstring: 0x11846
-  __TEXT.__cstring: 0xdfe1
+  __TEXT.__oslogstring: 0x11885
+  __TEXT.__cstring: 0xdfec
   __TEXT.__objc_methname: 0x10474
   __TEXT.__objc_classname: 0xc2e
   __TEXT.__objc_methtype: 0x2a77
   __TEXT.__unwind_info: 0x1f30
   __DATA_CONST.__const: 0x22f8
-  __DATA_CONST.__cfstring: 0x8ce0
+  __DATA_CONST.__cfstring: 0x8d00
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0

   - /usr/lib/libobjc.A.dylib
   Functions: 2162
   Symbols:   645
-  CStrings:  6336
+  CStrings:  6338
 
Functions:
~ sub_100017154 : 3028 -> 3104
~ sub_10004a5c8 -> sub_10004a614 : 560 -> 568
CStrings:
+ "Ignoring proxy match dictionary, not applicable for internal"
+ "Ignoring proxy match dictionary, not applicable for public"
+ "Internal"
+ "Public"
- "Ignoring proxy match dictionary, not applicable for seed"
- "Seed"
```
