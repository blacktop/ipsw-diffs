## captiveagent

> `/usr/libexec/captiveagent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 542.0.0.0.1
-  __TEXT.__text: 0x107a8
-  __TEXT.__auth_stubs: 0xb60
+  __TEXT.__text: 0x106ec
+  __TEXT.__auth_stubs: 0xb50
   __TEXT.__objc_stubs: 0x1720
   __TEXT.__objc_methlist: 0xcb8
   __TEXT.__const: 0x146

   __TEXT.__cstring: 0x7ce
   __TEXT.__objc_classname: 0xc8
   __TEXT.__objc_methtype: 0xa05
-  __TEXT.__unwind_info: 0x468
+  __TEXT.__unwind_info: 0x470
   __DATA_CONST.__const: 0x4b0
   __DATA_CONST.__cfstring: 0x8c0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__auth_got: 0x5c8
+  __DATA_CONST.__auth_got: 0x5c0
   __DATA_CONST.__got: 0x1f8
   __DATA.__objc_const: 0x1948
   __DATA.__objc_selrefs: 0x880

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   Functions: 316
-  Symbols:   255
+  Symbols:   254
   CStrings:  730
 
Symbols:
- _objc_retainBlock
Functions:
~ sub_100002264 : 140 -> 112
~ sub_100003524 -> sub_100003508 : 3248 -> 3220
~ sub_100004e18 -> sub_100004de0 : 96 -> 80
~ sub_1000052b4 -> sub_10000526c : 164 -> 136
~ sub_100007dcc -> sub_100007d68 : 156 -> 120
~ sub_100010b14 -> sub_100010a8c : 88 -> 64
~ sub_100010b6c -> sub_100010acc : 164 -> 136
```
