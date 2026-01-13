## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1533.3.0.0.0
-  __TEXT.__text: 0x2b3a4c
+1533.4.0.0.0
+  __TEXT.__text: 0x2b3a94
   __TEXT.__auth_stubs: 0x2560
   __TEXT.__init_offsets: 0x1c0
-  __TEXT.__cstring: 0x7fed0
+  __TEXT.__cstring: 0x7ff0c
   __TEXT.__const: 0x3d160
   __TEXT.__unwind_info: 0x5ed0
   __TEXT.__eh_frame: 0x38

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: CAD06580-88B9-3668-B08A-4089749044B2
-  Functions: 13163
-  Symbols:   16391
-  CStrings:  12859
+  UUID: E0A1CF5B-A1AF-3482-9E85-7995522786DB
+  Functions: 13164
+  Symbols:   16392
+  CStrings:  12860
 
Symbols:
+ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.17
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2255
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2255.cold.1
+ __block_descriptor_tmp.1955
+ __block_descriptor_tmp.2253
+ __block_descriptor_tmp.2257
+ __block_descriptor_tmp.2275
+ __block_descriptor_tmp.2310
+ __block_descriptor_tmp.2642
+ __block_descriptor_tmp.2679
+ __block_descriptor_tmp.3151
+ __block_descriptor_tmp.3228
+ __block_descriptor_tmp.3245
+ __block_descriptor_tmp.3248
+ __block_descriptor_tmp.3254
+ __block_descriptor_tmp.3292
+ __block_literal_global.2277
+ __block_literal_global.2312
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2253
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2253.cold.1
- __block_descriptor_tmp.1953
- __block_descriptor_tmp.2251
- __block_descriptor_tmp.2255
- __block_descriptor_tmp.2273
- __block_descriptor_tmp.2308
- __block_descriptor_tmp.2640
- __block_descriptor_tmp.2677
- __block_descriptor_tmp.3149
- __block_descriptor_tmp.3226
- __block_descriptor_tmp.3241
- __block_descriptor_tmp.3246
- __block_descriptor_tmp.3252
- __block_descriptor_tmp.3290
- __block_literal_global.2275
- __block_literal_global.2310
Functions:
~ __ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData : 5808 -> 5776
~ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.6 : 96 -> 104
~ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.7 : 88 -> 96
~ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.12 : 244 -> 88
~ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.13 : 100 -> 244
~ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.14 : 244 -> 100
~ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.15 : 96 -> 244
~ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.16 : 100 -> 96
+ _ZN16AppleBCMWLANCore30parseAMPDUStatsGlobalContainerEP6OSData.cold.17
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1533.4\""
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.MacOSX25.3.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLAN11beAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBSSBeacon.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBssManager.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommandMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommander.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCore.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCoreDbg.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingHelpers.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingPerSlice.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANJoinAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANLQM.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANNANInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANPowerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANProximityInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANScanAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANTxPowerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANBusInterfacePCIe.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CGCxugC8YsKY_Hj8gwSOamo-46gc6wQCXlPIOTc/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANPCIeSkywalk.cpp"
+ "AppleBCMWLANV3_driverkit-1533.4"
+ "Jan  4 2026 19:20:52"
+ "[dk] %s@%d:aggrDistLen %d exceeds buffer size %lu, capping\n"
- "\"AppleBCMWLANV3_driverkit-1533.3\""
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.MacOSX25.3.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLAN11beAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBSSBeacon.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBssManager.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommandMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommander.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCore.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCoreDbg.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingHelpers.hpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingPerSlice.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANJoinAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANLQM.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANNANInterface.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANPowerManager.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANProximityInterface.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANScanAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANTxPowerManager.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANBusInterfacePCIe.cpp"
- "/AppleInternal/Library/BuildRoots/4~CD24ugAxvU9wxVEj25OXs6zlGo0mhmrHfpssWBQ/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANPCIeSkywalk.cpp"
- "AppleBCMWLANV3_driverkit-1533.3"
- "Dec  5 2025 23:10:28"

```
