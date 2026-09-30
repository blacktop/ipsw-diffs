## hangreporter

> `/usr/libexec/hangreporter`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 398.2.0.0.0
-  __TEXT.__text: 0x404b4
+  __TEXT.__text: 0x4050c
   __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_stubs: 0x2d40
+  __TEXT.__objc_stubs: 0x2d60
   __TEXT.__objc_methlist: 0xfa4
-  __TEXT.__const: 0x298
+  __TEXT.__const: 0x2c8
   __TEXT.__cstring: 0x315c9
   __TEXT.__oslogstring: 0x4b03
-  __TEXT.__gcc_except_tab: 0xc00
-  __TEXT.__objc_methname: 0x530d
+  __TEXT.__gcc_except_tab: 0xc18
+  __TEXT.__objc_methname: 0x5325
   __TEXT.__objc_classname: 0x147
   __TEXT.__objc_methtype: 0x87b
   __TEXT.__unwind_info: 0x538

   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x26d0
-  __DATA.__objc_selrefs: 0x1080
+  __DATA.__objc_selrefs: 0x1088
   __DATA.__objc_ivar: 0x264
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x638

   - /usr/lib/libz.1.dylib
   Functions: 701
   Symbols:   329
-  CStrings:  5140
+  CStrings:  5141
 
Functions:
~ sub_100002d98 : 12932 -> 12992
~ sub_10001b510 -> sub_10001b54c : 7272 -> 7300
CStrings:
+ "setDisplayKernelFrames:"
```
