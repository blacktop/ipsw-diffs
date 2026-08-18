## captiveagent

> `/usr/libexec/captiveagent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 514.160.1.0.1
-  __TEXT.__text: 0x11e78
-  __TEXT.__auth_stubs: 0xb00
+  __TEXT.__text: 0x11dbc
+  __TEXT.__auth_stubs: 0xaf0
   __TEXT.__objc_stubs: 0x1720
   __TEXT.__objc_methlist: 0xcb8
   __TEXT.__const: 0x146

   __TEXT.__cstring: 0x7c5
   __TEXT.__objc_classname: 0xd1
   __TEXT.__objc_methtype: 0xa05
-  __TEXT.__unwind_info: 0x548
-  __DATA_CONST.__auth_got: 0x598
+  __TEXT.__unwind_info: 0x550
+  __DATA_CONST.__auth_got: 0x590
   __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x4b0
   __DATA_CONST.__cfstring: 0x8c0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   Functions: 316
-  Symbols:   249
+  Symbols:   248
   CStrings:  730
 
Symbols:
- _objc_retainBlock
Functions:
~ sub_1000023e0 : 144 -> 116
~ sub_100003910 -> sub_1000038f4 : 3248 -> 3220
~ sub_1000052a4 -> sub_10000526c : 96 -> 80
~ sub_1000057cc -> sub_100005784 : 168 -> 140
~ sub_1000087dc -> sub_100008778 : 160 -> 124
~ sub_10001213c -> sub_1000120b4 : 92 -> 68
~ sub_100012198 -> sub_1000120f8 : 168 -> 140
```
