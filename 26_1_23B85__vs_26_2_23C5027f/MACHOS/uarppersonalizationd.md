## uarppersonalizationd

> `/usr/libexec/uarppersonalizationd`

```diff

-1338.40.31.0.1
-  __TEXT.__text: 0x4430
-  __TEXT.__auth_stubs: 0x470
+1338.60.16.0.0
+  __TEXT.__text: 0x4604
+  __TEXT.__auth_stubs: 0x480
   __TEXT.__objc_stubs: 0x8c0
   __TEXT.__objc_methlist: 0x1a0
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0xcc
   __TEXT.__objc_methname: 0x857
   __TEXT.__cstring: 0xbd5
-  __TEXT.__oslogstring: 0x817
+  __TEXT.__oslogstring: 0x8b3
   __TEXT.__objc_classname: 0x9b
   __TEXT.__objc_methtype: 0x1d7
   __TEXT.__unwind_info: 0x190
-  __DATA_CONST.__auth_got: 0x248
+  __DATA_CONST.__auth_got: 0x250
   __DATA_CONST.__got: 0x108
   __DATA_CONST.__const: 0x4a0
   __DATA_CONST.__cfstring: 0xd00

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3A217AFF-65DE-31DB-B00F-BBC2936A1CEB
+  UUID: 6912B6C2-98F2-3BEF-AFE7-E772FEEAAF44
   Functions: 105
-  Symbols:   113
-  CStrings:  415
+  Symbols:   114
+  CStrings:  417
 
Symbols:
+ _MKBGetDeviceLockState
Functions:
~ sub_10000143c -> sub_1000014a4 : 708 -> 952
~ sub_100003554 -> sub_1000036b0 : 1352 -> 1576
CStrings:
+ "%s: UARP: current keybag state <%d> for apple connect based personalization"
+ "%s: UARP: unsupported keybag state <%d> for apple connect based personalization"

```
