## osascript

> `/usr/bin/osascript`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-410.1.0.0.0
-  __TEXT.__text: 0x2384
-  __TEXT.__auth_stubs: 0x630
+411.0.0.0.0
+  __TEXT.__text: 0x24ec
+  __TEXT.__auth_stubs: 0x640
   __TEXT.__objc_stubs: 0x640
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x38

   __TEXT.__objc_methname: 0x3d3
   __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methtype: 0xb
-  __TEXT.__info_plist: 0x4cd
+  __TEXT.__info_plist: 0x4cb
   __TEXT.__unwind_info: 0x108
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__cfstring: 0x160

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x328
+  __DATA_CONST.__auth_got: 0x330
   __DATA_CONST.__got: 0xe8
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x1d0

   - /usr/lib/libedit.3.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 35
-  Symbols:   139
+  Symbols:   140
   CStrings:  115
 
Symbols:
+ _isatty
Functions:
~ sub_10000128c : 3448 -> 3808
```
