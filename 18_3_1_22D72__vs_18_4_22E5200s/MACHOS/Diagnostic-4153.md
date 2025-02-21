## Diagnostic-4153

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4153.appex/Diagnostic-4153`

```diff

-820.82.2.0.0
-  __TEXT.__text: 0x7450
-  __TEXT.__auth_stubs: 0x2d0
+820.100.56.0.0
+  __TEXT.__text: 0x7494
+  __TEXT.__auth_stubs: 0x2e0
   __TEXT.__objc_stubs: 0x2200
-  __TEXT.__objc_methlist: 0x7d0
+  __TEXT.__objc_methlist: 0xb20
   __TEXT.__objc_methname: 0x2a72
   __TEXT.__objc_classname: 0x12c
   __TEXT.__objc_methtype: 0xbae
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x267
+  __TEXT.__cstring: 0x281
   __TEXT.__oslogstring: 0x22e
   __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__auth_got: 0x170
+  __DATA_CONST.__auth_got: 0x178
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__const: 0x190
-  __DATA_CONST.__cfstring: 0x560
+  __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x1668
-  __DATA.__objc_selrefs: 0x9e0
+  __DATA.__objc_const: 0x1028
+  __DATA.__objc_selrefs: 0xb98
   __DATA.__objc_ivar: 0xc8
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x2a0

   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 181
-  Symbols:   143
-  CStrings:  654
+  Functions: 180
+  Symbols:   144
+  CStrings:  655
 
Symbols:
+ _MGGetSInt32Answer
CStrings:
+ "FrontCameraRotationForISP"

```
