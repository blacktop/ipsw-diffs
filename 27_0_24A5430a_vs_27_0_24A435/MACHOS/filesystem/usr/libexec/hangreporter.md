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

 426.0.0.0.0
-  __TEXT.__text: 0x260d0
+  __TEXT.__text: 0x26120
   __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_stubs: 0x3460
+  __TEXT.__objc_stubs: 0x3480
   __TEXT.__objc_methlist: 0x136c
-  __TEXT.__const: 0x2b0
+  __TEXT.__const: 0x2e0
   __TEXT.__cstring: 0x431b
   __TEXT.__oslogstring: 0x4d4f
   __TEXT.__objc_classname: 0x183
-  __TEXT.__objc_methname: 0x5c82
+  __TEXT.__objc_methname: 0x5c9a
   __TEXT.__objc_methtype: 0x8f8
-  __TEXT.__gcc_except_tab: 0xc7c
+  __TEXT.__gcc_except_tab: 0xc94
   __TEXT.__unwind_info: 0x600
   __DATA_CONST.__const: 0x1680
   __DATA_CONST.__cfstring: 0x5320

   __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x2eb8
-  __DATA.__objc_selrefs: 0x1298
+  __DATA.__objc_selrefs: 0x12a0
   __DATA.__objc_ivar: 0x2e0
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x758

   - /usr/lib/libz.1.dylib
   Functions: 757
   Symbols:   334
-  CStrings:  2136
+  CStrings:  2137
 
Functions:
~ sub_100002c54 : 12160 -> 12208
~ sub_10000baa4 -> sub_10000bad4 : 7656 -> 7684
~ sub_1000116d4 -> sub_100011720 : 16 -> 12
~ sub_1000116e4 -> sub_10001172c : 12 -> 36
~ sub_1000116f0 -> sub_100011750 : 36 -> 16
~ sub_100024a5c -> sub_100024aa8 : 488 -> 492
CStrings:
+ "setDisplayKernelFrames:"
```
