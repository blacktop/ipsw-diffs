## com.apple.DriverKit-AppleEthernetMLX5

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleEthernetMLX5.dext/com.apple.DriverKit-AppleEthernetMLX5`

```diff

-62.0.0.0.0
-  __TEXT.__text: 0x1afd0
+62.100.1.0.0
+  __TEXT.__text: 0x1b114
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__cstring: 0x48a8
-  __TEXT.__const: 0x26f0
+  __TEXT.__cstring: 0x4861
+  __TEXT.__const: 0x27b8
   __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0x320
   __DATA_CONST.__got: 0x28

   - /System/DriverKit/System/Library/Frameworks/NetworkingDriverKit.framework/NetworkingDriverKit
   - /System/DriverKit/System/Library/Frameworks/PCIDriverKit.framework/PCIDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 714
+  Functions: 713
   Symbols:   473
-  CStrings:  643
+  CStrings:  641
 
Symbols:
+ __ZN33DriverKit_AppleEthernetMLX5_NetIf18setHardwareAssistsEjj
+ __ZThn48_N33DriverKit_AppleEthernetMLX5_NetIf18setHardwareAssistsEjj
- __ZN21IOUserNetworkEthernet18setHardwareAssistsEjj
- __ZThn48_N21IOUserNetworkEthernet18setHardwareAssistsEjj
CStrings:
- "build_rx_mbuf"
- "mlx5:%s:%d HW LRO session aggregated packets counter %d\n"

```
