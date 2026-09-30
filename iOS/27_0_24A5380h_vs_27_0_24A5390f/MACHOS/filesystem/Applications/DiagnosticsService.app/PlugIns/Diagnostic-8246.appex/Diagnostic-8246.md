## Diagnostic-8246

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8246.appex/Diagnostic-8246`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1374.0.5.0.0
-  __TEXT.__text: 0x4950
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_stubs: 0x1620
-  __TEXT.__objc_methlist: 0x694
-  __TEXT.__const: 0x58
-  __TEXT.__objc_methname: 0x1795
+1374.0.27.0.0
+  __TEXT.__text: 0x4c60
+  __TEXT.__auth_stubs: 0x3e0
+  __TEXT.__objc_stubs: 0x1660
+  __TEXT.__objc_methlist: 0x6ac
+  __TEXT.__const: 0x60
+  __TEXT.__objc_methname: 0x1802
   __TEXT.__cstring: 0x1c8
   __TEXT.__objc_classname: 0xc5
-  __TEXT.__objc_methtype: 0x41b
-  __TEXT.__gcc_except_tab: 0x70
-  __TEXT.__oslogstring: 0x3f2
-  __TEXT.__unwind_info: 0x148
-  __DATA_CONST.__const: 0x138
+  __TEXT.__objc_methtype: 0x41e
+  __TEXT.__oslogstring: 0x52d
+  __TEXT.__unwind_info: 0x140
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__auth_got: 0x1f8
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__got: 0x1e8
   __DATA.__objc_const: 0xaf8
-  __DATA.__objc_selrefs: 0x730
+  __DATA.__objc_selrefs: 0x760
   __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x180

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 124
-  Symbols:   143
-  CStrings:  427
+  Functions: 126
+  Symbols:   144
+  CStrings:  441
 
Symbols:
+ _CGRectGetMidX
+ _CGRectGetMidY
+ _OBJC_CLASS_$_CATransaction
- __Unwind_Resume
- ___objc_personality_v0
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
+ "T@\"AVCaptureVideoPreviewLayer\",&,N,V_capturePreviewLayer"
+ "_capturePreviewLayer"
+ "begin"
+ "capturePreviewLayer"
+ "commit"
+ "layoutSubviews"
+ "setAutoresizingMask:"
+ "setCapturePreviewLayer:"
+ "setDisableActions:"
+ "viewDidLayoutSubviews"
- "@\"DAExclavesStatusCapture\""
- "T@\"DAExclavesStatusCapture\",&,N,V_exclavesCapture"
- "_exclavesCapture"
- "exclavesCapture"
- "setExclavesCapture:"
```
