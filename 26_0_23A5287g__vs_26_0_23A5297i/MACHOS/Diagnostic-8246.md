## Diagnostic-8246

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8246.appex/Diagnostic-8246`

```diff

-1066.0.19.502.1
-  __TEXT.__text: 0x42c0
-  __TEXT.__auth_stubs: 0x320
-  __TEXT.__objc_stubs: 0x1500
-  __TEXT.__objc_methlist: 0x61c
+1066.0.41.0.0
+  __TEXT.__text: 0x4698
+  __TEXT.__auth_stubs: 0x350
+  __TEXT.__objc_stubs: 0x1540
+  __TEXT.__objc_methlist: 0x62c
   __TEXT.__const: 0x50
-  __TEXT.__objc_methname: 0x163b
-  __TEXT.__cstring: 0x131
+  __TEXT.__objc_methname: 0x166b
+  __TEXT.__cstring: 0x1bd
   __TEXT.__objc_classname: 0xb6
   __TEXT.__objc_methtype: 0x39b
   __TEXT.__gcc_except_tab: 0x70
-  __TEXT.__oslogstring: 0x39e
-  __TEXT.__unwind_info: 0x120
-  __DATA_CONST.__auth_got: 0x1a0
-  __DATA_CONST.__got: 0x1d0
+  __TEXT.__oslogstring: 0x3f2
+  __TEXT.__unwind_info: 0x128
+  __DATA_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0x110
-  __DATA_CONST.__cfstring: 0x2e0
+  __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x108
   __DATA.__objc_const: 0x9d8
-  __DATA.__objc_selrefs: 0x6e0
+  __DATA.__objc_selrefs: 0x6f0
   __DATA.__objc_ivar: 0x70
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/CameraUI.framework/CameraUI
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
+  - /System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D9EE7F71-D256-3A06-A495-A3ECE1AE6B05
-  Functions: 111
-  Symbols:   129
-  CStrings:  415
+  UUID: C9B6537C-2D63-339C-90C0-FC3A4A559F77
+  Functions: 114
+  Symbols:   133
+  CStrings:  445
 
Symbols:
+ _EXDisplayPipeClose
+ _EXDisplayPipeGetStats
+ _EXDisplayPipeOpen
+ _OBJC_CLASS_$_NSNumber
CStrings:
+ "Failed to get ExDisplayPipe status!"
+ "Failed to open ExDisplayPipe client for status!"
+ "_exDisplayPipeStats"
+ "brightness"
+ "dcpTransportHealth"
+ "displayPipeStats"
+ "globalHealth"
+ "link"
+ "numberWithUnsignedLongLong:"
+ "pipe"
+ "scaAlgorithm"
+ "scaDriver"
+ "sclDriver"
+ "sclHealth"
+ "tconCRC"
+ "tconHPD"
+ "tconHealth"

```
