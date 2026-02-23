## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1550.17.0.0.0
-  __TEXT.__text: 0x284334
+1550.20.0.0.0
+  __TEXT.__text: 0x284364
   __TEXT.__auth_stubs: 0x24b0
   __TEXT.__init_offsets: 0x1bc
   __TEXT.__cstring: 0x80baa
   __TEXT.__const: 0x7eaf8
   __TEXT.__oslogstring: 0x1f3b
-  __TEXT.__unwind_info: 0x5e58
+  __TEXT.__unwind_info: 0x5e60
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x1258
   __DATA_CONST.__got: 0x108

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: 8F24977D-A4BC-3B9F-A83A-76648372368C
-  Functions: 13965
-  Symbols:   17216
+  UUID: FD94C84C-25D2-340B-8626-FCA2FAA466C0
+  Functions: 13966
+  Symbols:   17217
   CStrings:  12934
 
Symbols:
+ __ZN24AppleBCMWLANNANInterface12debugHexdumpEPKcPKhj
Functions:
~ __ZNK15AppleBCMWLANLQM9dumpStatsEPcjj : 1668 -> 1644
+ __ZN24AppleBCMWLANNANInterface12debugHexdumpEPKcPKhj
~ __ZN24AppleBCMWLANNANInterface14setNAN_PUBLISHEP27apple80211_nan_publish_data : 1992 -> 1916
~ __ZN24AppleBCMWLANNANInterface13setNAN_DP_REQEP25apple80211_nan_dp_request : 1504 -> 1436
~ __ZN24AppleBCMWLANNANInterface22setNAN_ADDITIONAL_ATTREP29apple80211_nan_vendor_payload : 1732 -> 1628
~ __ZN24AppleBCMWLANNANInterface19setNAN_PAIRING_KEYSEP30apple80211_nan_encryption_keys : 2144 -> 2008
~ __ZN16AppleBCMWLANCore34sendRC2CoexStatsEventCoreAnalyticsEv : 9104 -> 9376
~ __ZNK21AppleBCMWLANCommander9dumpStateEPcjj : 2660 -> 2620
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1550.20\""
+ "/AppleInternal/Library/BuildRoots/4~CJRhugCx2SMgSa7FWtIpuGcmS3DfeWY7NNY89fY/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.4.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLAN11beAdapter.cpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBSSBeacon.cpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBssManager.cpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommandMonitor.cpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommander.cpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCore.cpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCoreDbg.cpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingHelpers.hpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingPerSlice.cpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANJoinAdapter.cpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANLQM.cpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANNANInterface.cpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANPowerManager.cpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANProximityInterface.cpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANScanAdapter.cpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANTxPowerManager.cpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANBusInterfacePCIe.cpp"
+ "/Library/Caches/com.apple.xbs/33333C8D-9D70-4EF4-90AE-9943A158E9A6/TemporaryDirectory.ZqaofD/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANPCIeSkywalk.cpp"
+ "AppleBCMWLANV3_driverkit-1550.20"
+ "Feb 17 2026 21:56:39"
- "\"AppleBCMWLANV3_driverkit-1550.17\""
- "/AppleInternal/Library/BuildRoots/4~CIsPugBR09hrKDaRodzw3QFFVxQz1ops0rIsGzM/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.4.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLAN11beAdapter.cpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBSSBeacon.cpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBssManager.cpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommandMonitor.cpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommander.cpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCore.cpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCoreDbg.cpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingHelpers.hpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingPerSlice.cpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANJoinAdapter.cpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANLQM.cpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANNANInterface.cpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANPowerManager.cpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANProximityInterface.cpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANScanAdapter.cpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANTxPowerManager.cpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANBusInterfacePCIe.cpp"
- "/Library/Caches/com.apple.xbs/62ADA6C3-3403-4AC5-AAE2-213599F636ED/TemporaryDirectory.OFPBzv/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANPCIeSkywalk.cpp"
- "AppleBCMWLANV3_driverkit-1550.17"
- "Feb  9 2026 23:02:42"

```
