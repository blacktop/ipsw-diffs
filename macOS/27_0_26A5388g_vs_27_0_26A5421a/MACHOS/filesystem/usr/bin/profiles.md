## profiles

> `/usr/bin/profiles`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1841.0.0.0.0
+1842.1.1.0.0
   __TEXT.__text: 0x111c4
   __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_stubs: 0x1220
+  __TEXT.__objc_stubs: 0x1240
   __TEXT.__objc_methlist: 0x68
   __TEXT.__cstring: 0x7e9c
   __TEXT.__const: 0xd0

   __TEXT.__gcc_except_tab: 0x60
   __TEXT.__objc_classname: 0x12
   __TEXT.__objc_methtype: 0x4b
-  __TEXT.__objc_methname: 0xd7d
+  __TEXT.__objc_methname: 0xd91
   __TEXT.__unwind_info: 0x260
   __DATA_CONST.__const: 0x228
   __DATA_CONST.__cfstring: 0x1220

   __DATA_CONST.__got: 0x270
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x488
+  __DATA.__objc_selrefs: 0x490
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x590
   __DATA.__common: 0x1b8

   - /usr/lib/libobjc.A.dylib
   Functions: 245
   Symbols:   261
-  CStrings:  877
+  CStrings:  878
 
CStrings:
+ "03:05:49"
+ "Aug 10 2026"
+ "newlineCharacterSet"
- "01:29:03"
- "Jul 11 2026"
```
