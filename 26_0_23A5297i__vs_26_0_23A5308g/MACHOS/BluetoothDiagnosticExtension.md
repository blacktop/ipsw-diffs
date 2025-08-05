## BluetoothDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/BluetoothDiagnosticExtension.appex/BluetoothDiagnosticExtension`

```diff

-190.47.3.0.0
-  __TEXT.__text: 0xfc0
-  __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_stubs: 0x400
-  __TEXT.__objc_methlist: 0x2c
-  __TEXT.__gcc_except_tab: 0x270
-  __TEXT.__cstring: 0x199
-  __TEXT.__oslogstring: 0xf1
+190.50.0.0.0
+  __TEXT.__text: 0x1148
+  __TEXT.__auth_stubs: 0x270
+  __TEXT.__objc_stubs: 0x420
+  __TEXT.__objc_methlist: 0x38
+  __TEXT.__gcc_except_tab: 0x274
+  __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x1ca
+  __TEXT.__oslogstring: 0x10e
   __TEXT.__objc_classname: 0x1f
-  __TEXT.__objc_methname: 0x325
-  __TEXT.__objc_methtype: 0x21
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x128
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x40
+  __TEXT.__objc_methname: 0x33c
+  __TEXT.__objc_methtype: 0x29
+  __TEXT.__unwind_info: 0xd8
+  __DATA_CONST.__auth_got: 0x148
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__const: 0x80
   __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x110
+  __DATA.__objc_selrefs: 0x118
   __DATA.__objc_data: 0x50
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7032B460-47C2-3C39-8005-DF9138532439
-  Functions: 10
-  Symbols:   66
-  CStrings:  72
+  UUID: BD0BE465-40CF-3158-9F21-EB3FA20F2830
+  Functions: 13
+  Symbols:   71
+  CStrings:  80
 
Symbols:
+ _IOObjectRelease
+ _IOServiceGetMatchingService
+ _IOServiceNameMatching
+ _dispatch_once
+ _kIOMainPortDefault
CStrings:
+ "B16@0:8"
+ "CoreCapture collection is %s"
+ "DISABLED"
+ "ENABLED"
+ "bluetooth-pcie"
+ "marconi-bt"
+ "shouldAllowCoreCapture"
+ "v8@?0"

```
