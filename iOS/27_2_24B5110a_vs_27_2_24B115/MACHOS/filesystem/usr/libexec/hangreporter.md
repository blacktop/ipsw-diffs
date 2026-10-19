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
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 430.0.0.0.0
-  __TEXT.__text: 0x2622c
+  __TEXT.__text: 0x26264
   __TEXT.__auth_stubs: 0xf30
-  __TEXT.__objc_stubs: 0x3460
+  __TEXT.__objc_stubs: 0x3480
   __TEXT.__objc_methlist: 0x1374
-  __TEXT.__const: 0x2b0
+  __TEXT.__const: 0x2e0
   __TEXT.__cstring: 0x4378
   __TEXT.__oslogstring: 0x4d97
   __TEXT.__objc_classname: 0x183
-  __TEXT.__objc_methname: 0x5c96
+  __TEXT.__objc_methname: 0x5cae
   __TEXT.__objc_methtype: 0x8f8
-  __TEXT.__gcc_except_tab: 0xcc4
+  __TEXT.__gcc_except_tab: 0xcdc
   __TEXT.__unwind_info: 0x900
   __DATA_CONST.__const: 0x16f8
   __DATA_CONST.__cfstring: 0x5340

   __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x2eb8
-  __DATA.__objc_selrefs: 0x12a0
+  __DATA.__objc_selrefs: 0x12a8
   __DATA.__objc_ivar: 0x2e0
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x758

   - /usr/lib/libz.1.dylib
   Functions: 766
   Symbols:   335
-  CStrings:  2141
+  CStrings:  2142
 
Functions:
~ sub_100002c44 : 12820 -> 12848
~ sub_10000b808 -> sub_10000b824 : 7656 -> 7684
CStrings:
+ "setDisplayKernelFrames:"
```
