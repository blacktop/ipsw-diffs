## captiveagent

> `/usr/libexec/captiveagent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-514.120.2.0.0
-  __TEXT.__text: 0x12650
-  __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_stubs: 0x16a0
+514.160.1.0.1
+  __TEXT.__text: 0x126a8
+  __TEXT.__auth_stubs: 0x9b0
+  __TEXT.__objc_stubs: 0x1720
   __TEXT.__objc_methlist: 0xcb8
   __TEXT.__const: 0x146
   __TEXT.__oslogstring: 0x18c0

   __TEXT.__objc_classname: 0xd1
   __TEXT.__objc_methtype: 0xa05
   __TEXT.__unwind_info: 0x550
-  __DATA_CONST.__auth_got: 0x4e8
+  __DATA_CONST.__auth_got: 0x4f0
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x550
+  __DATA_CONST.__const: 0x4f0
   __DATA_CONST.__cfstring: 0x8c0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   Functions: 327
-  Symbols:   225
+  Symbols:   226
   CStrings:  723
 
Symbols:
+ _objc_retainBlock
```
