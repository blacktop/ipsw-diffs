## fdesetup

> `/usr/bin/fdesetup`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
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

-1841.0.0.0.0
-  __TEXT.__text: 0x2c198
+1842.1.1.0.0
+  __TEXT.__text: 0x2c2d4
   __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_stubs: 0x2780
+  __TEXT.__objc_stubs: 0x27a0
   __TEXT.__objc_methlist: 0x61c
   __TEXT.__const: 0x109
-  __TEXT.__gcc_except_tab: 0x920
+  __TEXT.__gcc_except_tab: 0x964
   __TEXT.__oslogstring: 0x98bf
   __TEXT.__cstring: 0xf767
   __TEXT.__objc_classname: 0x6d
-  __TEXT.__objc_methname: 0x23c5
+  __TEXT.__objc_methname: 0x23d9
   __TEXT.__objc_methtype: 0x377
   __TEXT.__unwind_info: 0x728
   __DATA_CONST.__const: 0x590

   __DATA_CONST.__got: 0x398
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x4a0
-  __DATA.__objc_selrefs: 0xab8
+  __DATA.__objc_selrefs: 0xac0
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x4ae

   - /usr/lib/libodfde.dylib
   Functions: 731
   Symbols:   379
-  CStrings:  1802
+  CStrings:  1803
 
Functions:
~ sub_100002fa4 : 528 -> 552
~ sub_100003b10 -> sub_100003b28 : 280 -> 352
~ sub_100003c28 -> sub_100003c88 : 176 -> 200
~ sub_100003cd8 -> sub_100003d50 : 792 -> 816
~ sub_100004480 -> sub_100004510 : 652 -> 668
~ sub_10000470c -> sub_1000047ac : 1204 -> 1220
~ sub_100004bc0 -> sub_100004c70 : 608 -> 624
~ sub_100004e20 -> sub_100004ee0 : 1136 -> 1152
~ sub_1000054e8 -> sub_1000055b8 : 108 -> 124
~ sub_100005554 -> sub_100005634 : 1060 -> 1076
~ sub_100005978 -> sub_100005a68 : 1268 -> 1292
~ sub_100005e6c -> sub_100005f74 : 696 -> 720
~ sub_100006dac -> sub_100006ecc : 596 -> 620
~ sub_100007000 -> sub_100007138 : 516 -> 532
~ sub_100026bcc -> sub_100026d14 : 68 -> 56
CStrings:
+ "03:01:59"
+ "Aug 10 2026"
+ "newlineCharacterSet"
- "01:25:28"
- "Jul 11 2026"
```
