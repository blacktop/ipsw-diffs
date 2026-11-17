## searchd

> `/System/Library/PrivateFrameworks/Search.framework/searchd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2465.2.7.101.0
-  __TEXT.__text: 0x60d68
+2465.2.13.0.0
+  __TEXT.__text: 0x60d8c
   __TEXT.__auth_stubs: 0x1900
-  __TEXT.__objc_stubs: 0xa7e0
-  __TEXT.__objc_methlist: 0x2b40
+  __TEXT.__objc_stubs: 0xa820
+  __TEXT.__objc_methlist: 0x2b58
   __TEXT.__const: 0x23c
   __TEXT.__cstring: 0x52a2
-  __TEXT.__objc_methname: 0xaec1
+  __TEXT.__objc_methname: 0xaef8
   __TEXT.__objc_classname: 0x42e
   __TEXT.__objc_methtype: 0x1822
   __TEXT.__oslogstring: 0x37a3

   __DATA_CONST.__got: 0x11e0
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x7d10
-  __DATA.__objc_selrefs: 0x3018
+  __DATA.__objc_selrefs: 0x3028
   __DATA.__objc_ivar: 0x384
   __DATA.__objc_data: 0xb90
   __DATA.__data: 0x670

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1238
+  Functions: 1240
   Symbols:   981
-  CStrings:  3332
+  CStrings:  3334
 
Functions:
~ sub_100025a64 : 1748 -> 1768
+ sub_100026a04
+ sub_1000617d4
CStrings:
+ "enableRecycleOnProcessFdLimit"
+ "recyclesOnProcessFdLimit"
```
