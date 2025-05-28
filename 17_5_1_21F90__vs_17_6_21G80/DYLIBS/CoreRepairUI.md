## CoreRepairUI

> `/System/Library/PrivateFrameworks/CoreRepairUI.framework/CoreRepairUI`

```diff

-397.120.5.0.0
-  __TEXT.__text: 0x10e10
+397.140.7.0.0
+  __TEXT.__text: 0x10ee8
   __TEXT.__auth_stubs: 0x600
   __TEXT.__objc_methlist: 0xb20
   __TEXT.__const: 0x74
   __TEXT.__gcc_except_tab: 0xdc
-  __TEXT.__cstring: 0x118e
-  __TEXT.__oslogstring: 0xe43
+  __TEXT.__cstring: 0x118f
+  __TEXT.__oslogstring: 0xe83
   __TEXT.__unwind_info: 0x2f0
   __TEXT.__objc_classname: 0x41e
   __TEXT.__objc_methname: 0x1a6b

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 294
+  Functions: 296
   Symbols:   187
-  CStrings:  726
+  CStrings:  728
 
Symbols:
+ _IOPSGetBatteryHealthState
- _IOPSCopyPowerSourcesByType
CStrings:
+ "Battery Health State%@"
+ "Failed to get battery health state (%x)\n"
+ "IOPSBatteryHealthState"
- "Battery Service State"

```
