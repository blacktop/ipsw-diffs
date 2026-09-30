## Diagnostic-8340

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8340.appex/Diagnostic-8340`

```diff

-591.0.0.0.0
-  __TEXT.__text: 0x2f88
-  __TEXT.__auth_stubs: 0x340
+604.0.0.0.0
+  __TEXT.__text: 0x3150
+  __TEXT.__auth_stubs: 0x350
   __TEXT.__objc_stubs: 0x560
   __TEXT.__objc_methlist: 0x1c4
   __TEXT.__const: 0x30
   __TEXT.__cstring: 0x43c
-  __TEXT.__oslogstring: 0x483
+  __TEXT.__oslogstring: 0x4b6
   __TEXT.__objc_classname: 0x52
   __TEXT.__objc_methname: 0x87a
   __TEXT.__objc_methtype: 0x147
   __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__auth_got: 0x1b0
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x3c0

   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface
   - /usr/lib/libFDR.dylib
+  - /usr/lib/libFDRDecode.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
-  Functions: 55
-  Symbols:   88
-  CStrings:  247
+  Functions: 56
+  Symbols:   89
+  CStrings:  249
 
Symbols:
+ _AMFDRDecodeFDR2Data
CStrings:
+ "AuthInstall error is 3194."
+ "Decoded FDR2 format"
+ "Failed to decode PSD2: %!d(MISSING)"
- "Failed to decode PSD2"

```
