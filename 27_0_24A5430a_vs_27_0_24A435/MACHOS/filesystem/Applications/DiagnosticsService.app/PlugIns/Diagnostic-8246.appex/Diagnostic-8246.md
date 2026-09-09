## Diagnostic-8246

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8246.appex/Diagnostic-8246`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1374.2.2.0.0
-  __TEXT.__text: 0x50f0
+  __TEXT.__text: 0x5228
   __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_stubs: 0x18e0
+  __TEXT.__objc_stubs: 0x1900
   __TEXT.__objc_methlist: 0x74c
   __TEXT.__const: 0x60
-  __TEXT.__objc_methname: 0x1b47
-  __TEXT.__cstring: 0x1c8
+  __TEXT.__objc_methname: 0x1b5e
+  __TEXT.__cstring: 0x1d5
   __TEXT.__objc_classname: 0xc5
   __TEXT.__objc_methtype: 0x52e
-  __TEXT.__oslogstring: 0x52d
+  __TEXT.__oslogstring: 0x52e
   __TEXT.__unwind_info: 0x140
   __DATA_CONST.__const: 0x130
-  __DATA_CONST.__cfstring: 0x480
+  __DATA_CONST.__cfstring: 0x4a0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x208
   __DATA_CONST.__got: 0x1f0
   __DATA.__objc_const: 0xbe8
-  __DATA.__objc_selrefs: 0x800
+  __DATA.__objc_selrefs: 0x808
   __DATA.__objc_ivar: 0x90
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x180

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 139
+  Functions: 138
   Symbols:   147
-  CStrings:  478
+  CStrings:  481
 
Symbols:
+ _EXDisplayPipeOpenDisplay
- _EXDisplayPipeOpen
CStrings:
+ "Returning %ld stat sets"
+ "Stats found on index %u."
+ "displayIndex"
+ "numberWithUnsignedInt:"
- "Failed to open ExDisplayPipe client for status!"
```
