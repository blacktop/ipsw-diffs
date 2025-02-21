## Diagnostic-8246

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8246.appex/Diagnostic-8246`

```diff

-820.82.2.0.0
-  __TEXT.__text: 0x3bbc
-  __TEXT.__auth_stubs: 0x280
+820.100.56.0.0
+  __TEXT.__text: 0x3be4
+  __TEXT.__auth_stubs: 0x290
   __TEXT.__objc_stubs: 0x1360
-  __TEXT.__objc_methlist: 0x448
+  __TEXT.__objc_methlist: 0x5cc
   __TEXT.__const: 0x50
   __TEXT.__objc_methname: 0x14f9
-  __TEXT.__cstring: 0x6d
+  __TEXT.__cstring: 0x87
   __TEXT.__objc_classname: 0xa4
   __TEXT.__objc_methtype: 0x35c
   __TEXT.__oslogstring: 0x39e
   __TEXT.__unwind_info: 0xf8
-  __DATA_CONST.__auth_got: 0x148
+  __DATA_CONST.__auth_got: 0x150
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__const: 0xe8
-  __DATA_CONST.__cfstring: 0x120
+  __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0xc0
-  __DATA.__objc_const: 0xbe0
-  __DATA.__objc_selrefs: 0x5d0
+  __DATA.__objc_const: 0x918
+  __DATA.__objc_selrefs: 0x680
   __DATA.__objc_ivar: 0x6c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/CameraUI.framework/CameraUI
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 106
-  Symbols:   113
-  CStrings:  361
+  Functions: 105
+  Symbols:   114
+  CStrings:  362
 
Symbols:
+ _MGGetSInt32Answer
CStrings:
+ "FrontCameraRotationForISP"

```
