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

 985.0.0.0.0
-  __TEXT.__text: 0xc1cd4
+  __TEXT.__text: 0xc1d28
   __TEXT.__auth_stubs: 0x18e0
   __TEXT.__objc_stubs: 0xd260
   __TEXT.__objc_methlist: 0x5044
   __TEXT.__const: 0x2a0
   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__gcc_except_tab: 0x3858
-  __TEXT.__oslogstring: 0x1176c
-  __TEXT.__cstring: 0xdf2a
+  __TEXT.__oslogstring: 0x117ab
+  __TEXT.__cstring: 0xdf35
   __TEXT.__objc_methname: 0x1043c
   __TEXT.__objc_classname: 0xc2e
   __TEXT.__objc_methtype: 0x2a77
   __TEXT.__unwind_info: 0x19c0
   __DATA_CONST.__const: 0x22f8
-  __DATA_CONST.__cfstring: 0x8c20
+  __DATA_CONST.__cfstring: 0x8c40
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0

   - /usr/lib/libobjc.A.dylib
   Functions: 2162
   Symbols:   645
-  CStrings:  6326
+  CStrings:  6328
 
Functions:
~ sub_100017898 : 3040 -> 3116
~ sub_10004b3a8 -> sub_10004b3f4 : 560 -> 568
CStrings:
+ "Ignoring proxy match dictionary, not applicable for internal"
+ "Ignoring proxy match dictionary, not applicable for public"
+ "Internal"
+ "Public"
- "Ignoring proxy match dictionary, not applicable for seed"
- "Seed"
```
