## VisualPairing

> `/System/Library/PrivateFrameworks/VisualPairing.framework/VisualPairing`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-205.200.1.0.0
-  __TEXT.__text: 0x1dba4
-  __TEXT.__objc_methlist: 0x75c
+205.300.1.0.0
+  __TEXT.__text: 0x1dd38
+  __TEXT.__objc_methlist: 0x774
   __TEXT.__const: 0x34bd4
   __TEXT.__cstring: 0xc2d
-  __TEXT.__gcc_except_tab: 0x474
-  __TEXT.__unwind_info: 0x5a0
+  __TEXT.__gcc_except_tab: 0x4cc
+  __TEXT.__unwind_info: 0x5c0
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x750
+  __DATA_CONST.__objc_selrefs: 0x760
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__got: 0x200
   __AUTH_CONST.__const: 0x450
   __AUTH_CONST.__cfstring: 0x2a0
-  __AUTH_CONST.__objc_const: 0xf30
+  __AUTH_CONST.__objc_const: 0xf50
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x100
-  __DATA.__data: 0x360
+  __DATA.__objc_ivar: 0x104
+  __DATA.__data: 0x368
   __DATA_DIRTY.__objc_data: 0x1e0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 337
-  Symbols:   680
+  Functions: 339
+  Symbols:   685
   CStrings:  111
 
Symbols:
+ -[VPScannerView _applyPreviewRotationFromCoordinator]
+ -[VPScannerView observeValueForKeyPath:ofObject:change:context:]
+ GCC_except_table18
+ GCC_except_table19
+ _NSStringFromSelector
+ _OBJC_CLASS_$_AVCaptureDeviceRotationCoordinator
+ _objc_retain_x23
- _UIApp
- _gLogCategory_SV
Functions:
~ -[VPScannerView stop] : 416 -> 512
~ -[VPScannerView _setupCapture] : 1572 -> 1512
+ -[VPScannerView observeValueForKeyPath:ofObject:change:context:]
+ -[VPScannerView _handleCaptureSessionStopped:]
~ -[VPScannerView .cxx_destruct] : 200 -> 216
```
