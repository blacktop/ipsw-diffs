## thermalmonitord

> `/usr/libexec/thermalmonitord`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`
- `__DATA.__common`

```diff

-2076.0.0.0.0
-  __TEXT.__text: 0x111f0
+2081.0.0.0.1
+  __TEXT.__text: 0x11320
   __TEXT.__auth_stubs: 0xc70
   __TEXT.__objc_stubs: 0x1c20
   __TEXT.__objc_methlist: 0xe74
   __TEXT.__const: 0x17e
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__objc_methname: 0x2b45
-  __TEXT.__cstring: 0x52f8
+  __TEXT.__cstring: 0x5330
   __TEXT.__objc_classname: 0x1a0
   __TEXT.__objc_methtype: 0xf62
   __TEXT.__oslogstring: 0x6f
-  __TEXT.__unwind_info: 0x410
+  __TEXT.__unwind_info: 0x408
   __DATA_CONST.__const: 0x8d8
-  __DATA_CONST.__cfstring: 0x5620
+  __DATA_CONST.__cfstring: 0x5640
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_intobj: 0x4e0
-  __DATA_CONST.__objc_arraydata: 0x2dfc8
-  __DATA_CONST.__objc_dictobj: 0x2c650
-  __DATA_CONST.__objc_arrayobj: 0x31c8
+  __DATA_CONST.__objc_arraydata: 0x2e0c8
+  __DATA_CONST.__objc_dictobj: 0x2c718
+  __DATA_CONST.__objc_arrayobj: 0x31f8
   __DATA_CONST.__objc_doubleobj: 0xa2a0
   __DATA_CONST.__auth_got: 0x648
   __DATA_CONST.__got: 0x130

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 377
+  Functions: 376
   Symbols:   245
-  CStrings:  1414
+  CStrings:  1415
 
CStrings:
+ "Failed to upgrade NVRAM V2 to V3, resetting persistence"
```
