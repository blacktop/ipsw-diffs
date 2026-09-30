## audiomxd

> `usr/libexec/audiomxd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-1556.705.0.0.0
-  __TEXT.__text: 0x137d8
+1556.709.0.0.0
+  __TEXT.__text: 0x1393c
   __TEXT.__auth_stubs: 0xb60
   __TEXT.__objc_stubs: 0xe0
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x1a8
-  __TEXT.__gcc_except_tab: 0x11e8
+  __TEXT.__gcc_except_tab: 0x1204
   __TEXT.__cstring: 0xbda
-  __TEXT.__oslogstring: 0x325b
+  __TEXT.__oslogstring: 0x32d0
   __TEXT.__objc_classname: 0xb
   __TEXT.__objc_methtype: 0x8
   __TEXT.__objc_methname: 0x4e

   - /usr/lib/libobjc.A.dylib
   Functions: 179
   Symbols:   237
-  CStrings:  355
+  CStrings:  357
 
Functions:
~ sub_10000856c : 3120 -> 3420
~ sub_10000e9c0 -> sub_10000eaec : 2044 -> 2100
CStrings:
+ "%25s:%-5d Could not successfully allocate magic cookie buffer"
+ "%25s:%-5d Could not successfully allocate packet table"
```
