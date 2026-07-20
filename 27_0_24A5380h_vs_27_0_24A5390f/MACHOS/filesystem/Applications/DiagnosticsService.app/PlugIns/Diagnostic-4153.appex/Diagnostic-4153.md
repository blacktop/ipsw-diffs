## Diagnostic-4153

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4153.appex/Diagnostic-4153`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1374.0.5.0.0
-  __TEXT.__text: 0x8494
-  __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_stubs: 0x2480
-  __TEXT.__objc_methlist: 0xc08
-  __TEXT.__const: 0x60
+1374.0.27.0.0
+  __TEXT.__text: 0x8940
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_stubs: 0x2560
+  __TEXT.__objc_methlist: 0xc38
+  __TEXT.__const: 0x70
   __TEXT.__cstring: 0x3c1
-  __TEXT.__oslogstring: 0x282
+  __TEXT.__oslogstring: 0x3bd
   __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methname: 0x2cf8
-  __TEXT.__objc_methtype: 0xc54
+  __TEXT.__objc_methname: 0x2db0
+  __TEXT.__objc_methtype: 0xc72
   __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__unwind_info: 0x1d0
+  __TEXT.__unwind_info: 0x1e0
   __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__cfstring: 0x8c0
   __DATA_CONST.__objc_classlist: 0x38

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x220
-  __DATA_CONST.__got: 0x1f0
-  __DATA.__objc_const: 0x1238
-  __DATA.__objc_selrefs: 0xc40
-  __DATA.__objc_ivar: 0xdc
+  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x1f8
+  __DATA.__objc_const: 0x1268
+  __DATA.__objc_selrefs: 0xc80
+  __DATA.__objc_ivar: 0xe0
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x2a0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 203
-  Symbols:   172
-  CStrings:  711
+  Functions: 207
+  Symbols:   175
+  CStrings:  730
 
Symbols:
+ _CGRectGetMidX
+ _CGRectGetMidY
+ _OBJC_CLASS_$_CATransaction
CStrings:
+ "@\"AVCaptureVideoPreviewLayer\""
+ "Device does not have Exclaves. Skipping stat capture."
+ "Display pipe stats captured"
+ "Exclaves is not supported, skipping status."
+ "Exclaves is supported."
+ "Platform has display pipe stats, preparing to capture"
+ "Retrieving display pipe stats..."
+ "Returning %lu stats for display pipe client"
+ "Starting display pipe stat capture"
+ "T@\"AVCaptureVideoPreviewLayer\",&,N,V_previewLayer"
+ "_previewLayer"
+ "begin"
+ "commit"
+ "layoutSubviews"
+ "previewLayer"
+ "setAutoresizingMask:"
+ "setDisableActions:"
+ "setPreviewLayer:"
+ "viewDidLayoutSubviews"
```
