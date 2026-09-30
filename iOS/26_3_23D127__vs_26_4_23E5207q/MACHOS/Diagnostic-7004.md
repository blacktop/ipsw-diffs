## Diagnostic-7004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-7004.appex/Diagnostic-7004`

```diff

-921.80.171.0.1
-  __TEXT.__text: 0x39c
-  __TEXT.__auth_stubs: 0x130
-  __TEXT.__objc_stubs: 0x180
+921.100.255.0.0
+  __TEXT.__text: 0x2e8
+  __TEXT.__auth_stubs: 0xf0
+  __TEXT.__objc_stubs: 0x100
   __TEXT.__objc_methlist: 0x19c
   __TEXT.__const: 0x50
   __TEXT.__oslogstring: 0xb
-  __TEXT.__cstring: 0x6f
+  __TEXT.__cstring: 0x4a
   __TEXT.__objc_classname: 0x4e
-  __TEXT.__objc_methname: 0x294
+  __TEXT.__objc_methname: 0x26a
   __TEXT.__objc_methtype: 0x100
-  __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__cfstring: 0x80
+  __TEXT.__unwind_info: 0x70
+  __DATA_CONST.__auth_got: 0x80
+  __DATA_CONST.__got: 0x18
+  __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x78
+  __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x2d8
-  __DATA.__objc_selrefs: 0x130
+  __DATA.__objc_selrefs: 0x118
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
-  - /System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 17F578A7-2D45-366B-BEF7-BF7727A7DB35
+  UUID: 872E89CE-C50B-3AC8-9D05-F4E88F4DB476
   Functions: 7
-  Symbols:   40
-  CStrings:  77
+  Symbols:   34
+  CStrings:  70
 
Symbols:
+ _objc_release
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
- _MGGetBoolAnswer
- _OBJC_CLASS_$_CRPearlController
- _OBJC_CLASS_$_NSNumber
- _objc_claimAutoreleasedReturnValue
- _objc_release_x24
- _objc_release_x25
- _objc_release_x26
- _objc_retain_x2
- _objc_retain_x21
- _objc_retain_x8
Functions:
~ sub_100000d90 -> sub_100000d18 : 312 -> 320
~ sub_100000ec8 -> sub_100000e58 : 544 -> 296
~ sub_1000010fc -> sub_100000f94 : 20 -> 80
CStrings:
- "3kmXfug8VcxLI5yEmsqQKw"
- "InternalBuild"
- "code"
- "numberWithInteger:"
- "powerCycleSensor:"

```
