## captiveagent

> `/usr/libexec/captiveagent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-  __TEXT.__text: 0x11e34
-  __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_stubs: 0x16a0
+  __TEXT.__text: 0x11e78
+  __TEXT.__auth_stubs: 0xb00
+  __TEXT.__objc_stubs: 0x1720
   __TEXT.__objc_methlist: 0xcb8
   __TEXT.__const: 0x146
   __TEXT.__oslogstring: 0x193e

   __TEXT.__objc_classname: 0xd1
   __TEXT.__objc_methtype: 0xa05
   __TEXT.__unwind_info: 0x548
-  __DATA_CONST.__auth_got: 0x590
+  __DATA_CONST.__auth_got: 0x598
   __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x500
+  __DATA_CONST.__const: 0x4b0
   __DATA_CONST.__cfstring: 0x8c0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   Functions: 316
-  Symbols:   248
+  Symbols:   249
   CStrings:  730
 
Symbols:
+ _objc_retainBlock
Functions:
~ sub_1000014ec : 236 -> 232
~ sub_1000015d8 -> sub_1000015d4 : 88 -> 104
~ sub_100001630 -> sub_10000163c : 408 -> 404
~ sub_1000017c8 -> sub_1000017d0 : 608 -> 604
~ sub_100001a28 -> sub_100001a2c : 272 -> 260
~ sub_100001b38 -> sub_100001b30 : 252 -> 240
~ sub_100001c34 -> sub_100001c20 : 572 -> 568
~ sub_100001e70 -> sub_100001e58 : 592 -> 584
~ sub_100002400 -> sub_1000023e0 : 136 -> 144
~ sub_100003928 -> sub_100003910 : 3220 -> 3248
~ sub_1000052a0 -> sub_1000052a4 : 80 -> 96
~ sub_1000057b8 -> sub_1000057cc : 160 -> 168
~ sub_1000087c0 -> sub_1000087dc : 152 -> 160
~ sub_100012118 -> sub_10001213c : 68 -> 92
~ sub_10001215c -> sub_100012198 : 160 -> 168
```
