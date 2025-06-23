## com.apple.DriverKit-AppleEthernetMLX5

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetMLX5.dext/com.apple.DriverKit-AppleEthernetMLX5`

```diff

-109.0.1.0.0
-  __TEXT.__text: 0x19730
+109.0.2.0.0
+  __TEXT.__text: 0x19ad4
   __TEXT.__auth_stubs: 0x660
-  __TEXT.__cstring: 0x3fc3
-  __TEXT.__const: 0x1138
+  __TEXT.__cstring: 0x3ff3
+  __TEXT.__const: 0x2338
   __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0x330
   __DATA_CONST.__got: 0x28

   - /System/DriverKit/System/Library/Frameworks/NetworkingDriverKit.framework/NetworkingDriverKit
   - /System/DriverKit/System/Library/Frameworks/PCIDriverKit.framework/PCIDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: 96DC5D31-3454-3EBC-B821-296E43C8221F
-  Functions: 595
-  Symbols:   3440
-  CStrings:  602
+  UUID: 82037823-08CD-36DC-A360-6AC2E1D664C4
+  Functions: 598
+  Symbols:   3457
+  CStrings:  603
 
Symbols:
+ __ZL14ext_mode_table
+ __ZN33DriverKit_AppleEthernetMLX5_IVars12queryMCAMRegEPjhh
+ __ZN33DriverKit_AppleEthernetMLX5_IVars12queryPCAMRegEPjhh
+ __ZN33DriverKit_AppleEthernetMLX5_IVars12queryQCAMRegEPjhh
+ __ZN33DriverKit_AppleEthernetMLX5_IVars12setPortProtoEjib
- __ZN33DriverKit_AppleEthernetMLX5_IVars12setPortProtoEji
CStrings:
+ "mlx5: Could not find operational media subtype\n"

```
