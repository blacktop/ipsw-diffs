## Diagnostic-8079

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8079.appex/Diagnostic-8079`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1374.2.2.0.0
-  __TEXT.__text: 0x8b58
+  __TEXT.__text: 0x8c7c
   __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_stubs: 0x2400
+  __TEXT.__objc_stubs: 0x2420
   __TEXT.__objc_methlist: 0xb94
-  __TEXT.__cstring: 0x6d6
-  __TEXT.__objc_methname: 0x291f
+  __TEXT.__cstring: 0x6e3
+  __TEXT.__objc_methname: 0x2936
   __TEXT.__objc_classname: 0x1a0
   __TEXT.__objc_methtype: 0x36f
-  __TEXT.__const: 0x88
+  __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0x118
-  __TEXT.__oslogstring: 0xbf7
-  __TEXT.__unwind_info: 0x228
+  __TEXT.__oslogstring: 0xbf8
+  __TEXT.__unwind_info: 0x220
   __DATA_CONST.__const: 0x260
-  __DATA_CONST.__cfstring: 0xc80
+  __DATA_CONST.__cfstring: 0xca0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x2b8
   __DATA_CONST.__got: 0x170
   __DATA.__objc_const: 0x1938
-  __DATA.__objc_selrefs: 0xa38
+  __DATA.__objc_selrefs: 0xa40
   __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x180

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 240
+  Functions: 238
   Symbols:   185
-  CStrings:  700
+  CStrings:  703
 
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
