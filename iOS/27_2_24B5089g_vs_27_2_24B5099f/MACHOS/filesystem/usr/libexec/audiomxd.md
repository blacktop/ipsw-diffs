## audiomxd

> `/usr/libexec/audiomxd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`

```diff

-1638.209.1.0.0
-  __TEXT.__text: 0x42ec
+1638.211.0.0.0
+  __TEXT.__text: 0x43a8
   __TEXT.__auth_stubs: 0x890
   __TEXT.__objc_stubs: 0xc0
   __TEXT.__const: 0xa0
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__gcc_except_tab: 0x374
-  __TEXT.__cstring: 0x4c0
+  __TEXT.__gcc_except_tab: 0x378
+  __TEXT.__cstring: 0x4ca
   __TEXT.__oslogstring: 0x326
   __TEXT.__objc_methname: 0x7f
   __TEXT.__unwind_info: 0x228

   - /usr/lib/libobjc.A.dylib
   Functions: 77
   Symbols:   171
-  CStrings:  92
+  CStrings:  93
 
Functions:
~ sub_100004268 : 1520 -> 1708
CStrings:
+ "ftruncate"
```
