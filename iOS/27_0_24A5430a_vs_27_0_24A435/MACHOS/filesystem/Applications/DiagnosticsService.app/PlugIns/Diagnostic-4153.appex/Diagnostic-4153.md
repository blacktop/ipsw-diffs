## Diagnostic-4153

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4153.appex/Diagnostic-4153`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1374.2.2.0.0
-  __TEXT.__text: 0x8dd0
+  __TEXT.__text: 0x8f84
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_stubs: 0x27c0
+  __TEXT.__objc_stubs: 0x27e0
   __TEXT.__objc_methlist: 0xcd8
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x3c1
-  __TEXT.__oslogstring: 0x3bd
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x3e2
+  __TEXT.__oslogstring: 0x3be
   __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methname: 0x30f2
+  __TEXT.__objc_methname: 0x3109
   __TEXT.__objc_methtype: 0xced
   __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__unwind_info: 0x1e0
-  __DATA_CONST.__const: 0x1e0
-  __DATA_CONST.__cfstring: 0x8c0
+  __TEXT.__unwind_info: 0x1d8
+  __DATA_CONST.__const: 0x1e8
+  __DATA_CONST.__cfstring: 0x900
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__auth_got: 0x240
-  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__got: 0x208
   __DATA.__objc_const: 0x1358
-  __DATA.__objc_selrefs: 0xd18
+  __DATA.__objc_selrefs: 0xd20
   __DATA.__objc_ivar: 0xf4
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x2a0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 220
-  Symbols:   178
-  CStrings:  763
+  Functions: 219
+  Symbols:   180
+  CStrings:  767
 
Symbols:
+ _AVCaptureDeviceTypeBuiltInRenoUltraWideCamera
+ _DAIdentifierInnerFrontSuperWide
+ _EXDisplayPipeOpenDisplay
- _EXDisplayPipeOpen
CStrings:
+ "InnerFrontSuperWide"
+ "Returning %ld stat sets"
+ "Stats found on index %u."
+ "displayIndex"
+ "numberWithUnsignedInt:"
- "Failed to open ExDisplayPipe client for status!"
```
