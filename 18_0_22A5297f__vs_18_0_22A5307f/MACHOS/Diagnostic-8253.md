## Diagnostic-8253

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253`

```diff

-44.0.1.0.0
+45.0.0.0.0
   __TEXT.__text: 0x12888
   __TEXT.__auth_stubs: 0x6a0
   __TEXT.__objc_stubs: 0x740

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/MediaToolbox.framework/MediaToolbox
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/H10ISPServices.framework/H10ISPServices
-  - /System/Library/PrivateFrameworks/JasperDepth.framework/JasperDepth
   - /System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

```
