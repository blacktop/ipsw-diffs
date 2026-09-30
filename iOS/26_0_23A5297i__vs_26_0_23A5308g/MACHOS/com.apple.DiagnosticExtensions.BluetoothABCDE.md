## com.apple.DiagnosticExtensions.BluetoothABCDE

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/com.apple.DiagnosticExtensions.BluetoothABCDE.appex/com.apple.DiagnosticExtensions.BluetoothABCDE`

```diff

-190.47.3.0.0
-  __TEXT.__text: 0x808
-  __TEXT.__auth_stubs: 0x150
-  __TEXT.__objc_stubs: 0x380
-  __TEXT.__objc_methlist: 0x2c
-  __TEXT.__cstring: 0x26c
-  __TEXT.__oslogstring: 0x41
+190.50.0.0.0
+  __TEXT.__text: 0x990
+  __TEXT.__auth_stubs: 0x1a0
+  __TEXT.__objc_stubs: 0x3a0
+  __TEXT.__objc_methlist: 0x38
+  __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x29d
+  __TEXT.__oslogstring: 0x5e
   __TEXT.__objc_classname: 0xf
-  __TEXT.__objc_methname: 0x2ee
-  __TEXT.__objc_methtype: 0x21
-  __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0xb0
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x40
+  __TEXT.__objc_methname: 0x305
+  __TEXT.__objc_methtype: 0x29
+  __TEXT.__unwind_info: 0x80
+  __DATA_CONST.__auth_got: 0xd8
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__const: 0x80
   __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0xf0
+  __DATA.__objc_selrefs: 0xf8
   __DATA.__objc_data: 0x50
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1F9FE0F7-E163-3BAB-9B8F-A1E6E8E1E189
-  Functions: 4
-  Symbols:   44
-  CStrings:  62
+  UUID: 6CE5DD21-2192-3548-B33F-87A69D78D5A6
+  Functions: 7
+  Symbols:   50
+  CStrings:  70
 
Symbols:
+ _IOObjectRelease
+ _IOServiceGetMatchingService
+ _IOServiceNameMatching
+ _dispatch_once
+ _kIOMainPortDefault
+ _objc_release_x28
+ _objc_retain_x28
- _objc_retain_x27
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
