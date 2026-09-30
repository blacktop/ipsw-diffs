## mobile_obliterator

> `/usr/libexec/mobile_obliterator`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-400.0.0.0.0
-  __TEXT.__text: 0x1b77c
+402.0.0.0.0
+  __TEXT.__text: 0x1b76c
   __TEXT.__auth_stubs: 0x1540
   __TEXT.__objc_stubs: 0x920
   __TEXT.__objc_methlist: 0x1fc
-  __TEXT.__cstring: 0xacf5
+  __TEXT.__cstring: 0xad42
   __TEXT.__const: 0x6f8
   __TEXT.__gcc_except_tab: 0x144
   __TEXT.__objc_methname: 0x809

   __TEXT.__objc_methtype: 0x159
   __TEXT.__unwind_info: 0x408
   __DATA_CONST.__const: 0x678
-  __DATA_CONST.__cfstring: 0x20e0
+  __DATA_CONST.__cfstring: 0x2140
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libz.1.dylib
   Functions: 276
   Symbols:   402
-  CStrings:  1404
+  CStrings:  1407
 
Functions:
~ sub_1000025b4 : 29504 -> 29488
CStrings:
+ "MobileActivation/dcrt"
+ "removeExcept /dcrt.der/ /sdcrt.der/"
+ "removeExcept /log/"
```
