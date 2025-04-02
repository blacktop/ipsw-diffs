## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1425.41.0.0.0
-  __TEXT.__text: 0x2ad028
+1425.42.0.0.0
+  __TEXT.__text: 0x2ad3ec
   __TEXT.__auth_stubs: 0x24e0
   __TEXT.__init_offsets: 0x1c0
-  __TEXT.__cstring: 0x7dfd7
-  __TEXT.__const: 0x3d0a0
-  __TEXT.__unwind_info: 0x5da8
+  __TEXT.__cstring: 0x7e1d7
+  __TEXT.__const: 0x3d0b0
+  __TEXT.__unwind_info: 0x5db0
   __TEXT.__eh_frame: 0x38
   __TEXT.__oslogstring: 0x1ea5
   __DATA_CONST.__auth_got: 0x1270
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x20358
+  __DATA_CONST.__const: 0x20368
   __DATA_CONST.__osclassinfo: 0x390
   __DATA.__data: 0x388
   __DATA.__bss: 0x960

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 13059
-  Symbols:   16273
-  CStrings:  12643
+  Functions: 13063
+  Symbols:   16277
+  CStrings:  12649
 
Symbols:
+ _ZN16AppleBCMWLANCore13setRESET_CHIPEP24apple80211_reset_command.cold.1
+ _ZN16AppleBCMWLANCore13setRESET_CHIPEP24apple80211_reset_command.cold.2
+ _ZN16AppleBCMWLANCore13setRESET_CHIPEP24apple80211_reset_command.cold.3
+ _ZN16AppleBCMWLANCore13setRESET_CHIPEP24apple80211_reset_command.cold.4
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2239
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2239.cold.1
+ __block_descriptor_tmp.2241
+ __block_descriptor_tmp.2259
+ __block_descriptor_tmp.2294
+ __block_descriptor_tmp.2625
+ __block_descriptor_tmp.2662
+ __block_descriptor_tmp.3127
+ __block_descriptor_tmp.3204
+ __block_descriptor_tmp.3219
+ __block_descriptor_tmp.3221
+ __block_descriptor_tmp.3224
+ __block_descriptor_tmp.3230
+ __block_descriptor_tmp.3268
+ __block_literal_global.2261
+ __block_literal_global.2296
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2235
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2235.cold.1
- __block_descriptor_tmp.2233
- __block_descriptor_tmp.2255
- __block_descriptor_tmp.2290
- __block_descriptor_tmp.2621
- __block_descriptor_tmp.2658
- __block_descriptor_tmp.3123
- __block_descriptor_tmp.3200
- __block_descriptor_tmp.3215
- __block_descriptor_tmp.3217
- __block_descriptor_tmp.3220
- __block_descriptor_tmp.3226
- __block_descriptor_tmp.3264
- __block_literal_global.2257
- __block_literal_global.2292
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1425.42\""
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.MacOSX24.5.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLAN11beAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBSSBeacon.cpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBssManager.cpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommandMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommander.cpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCore.cpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCoreDbg.cpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingHelpers.hpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingPerSlice.cpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANJoinAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANLQM.cpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANNANInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANPowerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANProximityInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANScanAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANTxPowerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANBusInterfacePCIe.cpp"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANPCIeSkywalk.cpp"
+ "AppleBCMWLANV3_driverkit-1425.42"
+ "LinkLoss"
+ "LinkTestFailure"
+ "Mar 21 2025 21:17:37"
+ "[dk] %s@%d:Exiting setRESET_CHIP after calling FaultReport with kFaultActionFullCapture"
+ "[dk] %s@%d:This call to setRESET_CHIP will not actually reset the chip nor collect CoreCapture! Forwarding to dbgTriggerWatchdog()"
+ "[dk] %s@%d:This call to setRESET_CHIP will not actually reset the chip nor collect CoreCapture! returning ENODEV, calling message %s"
+ "[dk] %s@%d:This call to setRESET_CHIP will not actually reset the chip! isTrap=%u, isUserspaceReset=%u, calling message %s"
+ "[dk] %s@%d:isTrap=%u, isUserspaceReset=%u, trap reason %u, message: %s"
- "\"AppleBCMWLANV3_driverkit-1425.41\""
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.MacOSX24.4.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLAN11beAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBSSBeacon.cpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBssManager.cpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommandMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommander.cpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCore.cpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCoreDbg.cpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingHelpers.hpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingPerSlice.cpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANJoinAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANLQM.cpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANNANInterface.cpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANPowerManager.cpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANProximityInterface.cpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANScanAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANTxPowerManager.cpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANBusInterfacePCIe.cpp"
- "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANPCIeSkywalk.cpp"
- "AppleBCMWLANV3_driverkit-1425.41"
- "Mar  9 2025 20:58:41"
- "[dk] %s@%d:isTrap=%u, isUserspaceReset=%u, trap reason %u\n"

```
