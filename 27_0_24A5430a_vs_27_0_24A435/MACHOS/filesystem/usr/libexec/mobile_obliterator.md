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

 402.0.0.0.0
-  __TEXT.__text: 0x1ba48
+  __TEXT.__text: 0x1bc18
   __TEXT.__auth_stubs: 0x1540
   __TEXT.__objc_stubs: 0x920
   __TEXT.__objc_methlist: 0x1fc
-  __TEXT.__cstring: 0xadf4
+  __TEXT.__cstring: 0xaeae
   __TEXT.__const: 0x708
   __TEXT.__gcc_except_tab: 0x144
   __TEXT.__objc_methname: 0x809

   __TEXT.__objc_methtype: 0x159
   __TEXT.__unwind_info: 0x420
   __DATA_CONST.__const: 0x678
-  __DATA_CONST.__cfstring: 0x2140
+  __DATA_CONST.__cfstring: 0x2180
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libz.1.dylib
   Functions: 277
   Symbols:   402
-  CStrings:  1411
+  CStrings:  1417
 
Functions:
~ sub_100014104 : 828 -> 856
~ sub_100014440 -> sub_10001445c : 472 -> 480
~ sub_1000150c4 -> sub_1000150e8 : 1132 -> 1176
~ sub_100016380 -> sub_1000163d0 : 1936 -> 2320
CStrings:
+ "IODeviceTree:/product/display%d"
+ "ctx[%d]: display \"%s\" (display index %d)\n"
+ "display%d: display-boot-rotation = %u\n"
+ "display%d: display-rotation = %u\n"
+ "display-boot-rotation"
+ "display-rotation"
```
