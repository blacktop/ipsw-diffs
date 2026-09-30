## Diagnostic-4009

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009.appex/Diagnostic-4009`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

 1374.2.2.0.0
-  __TEXT.__text: 0x77c8
+  __TEXT.__text: 0x7a38
   __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0x1820
-  __TEXT.__objc_methlist: 0xd5c
-  __TEXT.__cstring: 0xac1
-  __TEXT.__const: 0x48
+  __TEXT.__objc_stubs: 0x1880
+  __TEXT.__objc_methlist: 0xd64
+  __TEXT.__cstring: 0xb33
+  __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0x168
   __TEXT.__objc_classname: 0x153
-  __TEXT.__objc_methname: 0x1abf
+  __TEXT.__objc_methname: 0x1b0d
   __TEXT.__objc_methtype: 0x777
-  __TEXT.__oslogstring: 0x46c
-  __TEXT.__unwind_info: 0x2b0
-  __DATA_CONST.__const: 0x238
-  __DATA_CONST.__cfstring: 0x9e0
+  __TEXT.__oslogstring: 0x46d
+  __TEXT.__unwind_info: 0x2a8
+  __DATA_CONST.__const: 0x240
+  __DATA_CONST.__cfstring: 0xa20
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x1f8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__auth_got: 0x368
-  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__got: 0x1e8
   __DATA.__objc_const: 0x13d0
-  __DATA.__objc_selrefs: 0x750
+  __DATA.__objc_selrefs: 0x768
   __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x410
-  __DATA.__data: 0x2e0
+  __DATA.__data: 0x300
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 245
-  Symbols:   207
-  CStrings:  569
+  Functions: 244
+  Symbols:   210
+  CStrings:  578
 
Symbols:
+ _EXDisplayPipeOpenDisplay
+ _OBJC_CLASS_$_NSMutableArray
+ _kFigCapturePortType_RenoFrontFacingSuperWideCamera
+ _kIdentifierInnerFrontSuperWide
- _EXDisplayPipeOpen
CStrings:
+ "/System/Library/MediaCapture/ISP.mediacapture"
+ "AppleCamera"
+ "ISPCaptureDeviceCreate"
+ "InnerFrontSuperWide"
+ "Returning %ld stat sets"
+ "Stats found on index %u."
+ "_innerFrontSuperWideCameraWithDevice:error:"
+ "addObject:"
+ "displayIndex"
+ "numberWithUnsignedInt:"
- "Failed to open ExDisplayPipe client for status!"
```
