## Diagnostic-8268

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8268.appex/Diagnostic-8268`

```diff

-645.60.42.502.1
-  __TEXT.__text: 0x3c4c
-  __TEXT.__auth_stubs: 0x300
+645.60.48.0.0
+  __TEXT.__text: 0x3cc0
+  __TEXT.__auth_stubs: 0x330
   __TEXT.__objc_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x124
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x3be
-  __TEXT.__oslogstring: 0x4e7
+  __TEXT.__oslogstring: 0x496
+  __TEXT.__cstring: 0x400
   __TEXT.__objc_classname: 0x3c
   __TEXT.__objc_methname: 0x5e5
   __TEXT.__objc_methtype: 0x159
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x188
-  __DATA_CONST.__got: 0x88
+  __TEXT.__unwind_info: 0xc0
+  __DATA_CONST.__auth_got: 0x1a0
+  __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x80
-  __DATA_CONST.__cfstring: 0x380
+  __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 48
-  Symbols:   80
+  Functions: 46
+  Symbols:   85
   CStrings:  209
 
Symbols:
+ _NSUnderlyingErrorKey
+ _createCRError
+ _objc_release_x28
+ _objc_retain_x1
+ _objc_retain_x20
CStrings:
+ "Failed to get remote data class"
+ "Failed to request FDR Permissions"
- "Failed to get remote data class, error: %!@(MISSING)"
- "Failed to request FDR Permissions: %!@(MISSING)"

```
