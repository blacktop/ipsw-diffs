## captiveagent

> `/usr/libexec/captiveagent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-541.0.0.0.0
-  __TEXT.__text: 0x1111c
-  __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_stubs: 0x16a0
+542.0.0.0.1
+  __TEXT.__text: 0x11178
+  __TEXT.__auth_stubs: 0x9f0
+  __TEXT.__objc_stubs: 0x1720
   __TEXT.__objc_methlist: 0xcb8
-  __TEXT.__const: 0x13e
+  __TEXT.__const: 0x146
   __TEXT.__oslogstring: 0x18ee
   __TEXT.__gcc_except_tab: 0x2a4
   __TEXT.__objc_methname: 0x1d9a
   __TEXT.__cstring: 0x7e0
   __TEXT.__objc_classname: 0xc8
   __TEXT.__objc_methtype: 0xa05
-  __TEXT.__unwind_info: 0x480
-  __DATA_CONST.__const: 0x590
+  __TEXT.__unwind_info: 0x488
+  __DATA_CONST.__const: 0x530
   __DATA_CONST.__cfstring: 0x8c0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__auth_got: 0x508
+  __DATA_CONST.__auth_got: 0x510
   __DATA_CONST.__got: 0x1e8
   __DATA.__objc_const: 0x1948
   __DATA.__objc_selrefs: 0x880

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   Functions: 331
-  Symbols:   229
+  Symbols:   230
   CStrings:  728
 
Symbols:
+ _objc_retainBlock
```
