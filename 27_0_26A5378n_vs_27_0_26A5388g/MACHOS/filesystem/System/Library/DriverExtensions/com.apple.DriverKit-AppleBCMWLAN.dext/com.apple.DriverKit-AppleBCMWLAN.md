## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__osclassinfo`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-1570.56.0.0.0
-  __TEXT.__text: 0x28d348
-  __TEXT.__auth_stubs: 0x25a0
+1570.62.0.0.0
+  __TEXT.__text: 0x28d6bc
+  __TEXT.__auth_stubs: 0x25b0
   __TEXT.__init_offsets: 0x1c0
-  __TEXT.__cstring: 0x827d6
+  __TEXT.__cstring: 0x8289b
   __TEXT.__const: 0x3d858
-  __TEXT.__unwind_info: 0x6020
+  __TEXT.__unwind_info: 0x6028
   __TEXT.__eh_frame: 0x38
   __TEXT.__oslogstring: 0x1e7a
-  __DATA_CONST.__const: 0x21228
+  __DATA_CONST.__const: 0x21248
   __DATA_CONST.__osclassinfo: 0x390
-  __DATA_CONST.__auth_got: 0x12d0
+  __DATA_CONST.__auth_got: 0x12d8
   __DATA_CONST.__got: 0x108
   __DATA.__data: 0x388
   __DATA.__bss: 0x950

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 14165
-  Symbols:   12053
-  CStrings:  13074
+  Functions: 14167
+  Symbols:   12055
+  CStrings:  13079
 
Symbols:
+ __ZN16IODispatchSource6CancelEU13block_pointerFvvEPFiP15OSMetaClassBase5IORPCE
+ ____ZN28AppleBCMWLANBusInterfacePCIe18detachPCIeBusGatedEP11IOPCIDeviceb_block_invoke_2
Functions:
~ __ZN28AppleBCMWLANNANDataInterface5startEP16AppleBCMWLANCoreP16RegistrationInfo : 1256 -> 1260
~ __ZN24AppleBCMWLANNANInterface5startEP16AppleBCMWLANCoreP16RegistrationInfo : 1104 -> 1108
~ __ZN30AppleBCMWLANProximityInterface5startEP16AppleBCMWLANCoreP16RegistrationInfo : 1076 -> 1080
~ __ZN19AppleBCMWLANCoreDbg10cmdTXStallEP24apple80211_debug_commandP16AppleBCMWLANCore : 236 -> 232
~ __ZN28AppleBCMWLANSkywalkInterface5startEP16AppleBCMWLANCoreP16RegistrationInfo : 1700 -> 1704
~ __ZN16AppleBCMWLANCore4initEP12OSDictionary : 4400 -> 4380
~ __ZN16AppleBCMWLANCore18getNanRxPktCounterEv : 44 -> 28
~ __ZN16AppleBCMWLANCore15dumpWmeCountersEPcii : 868 -> 836
~ __ZN16AppleBCMWLANCore15processChipCapsEv : 608 -> 600
~ __ZN16AppleBCMWLANCore17parseEventLogScanEP6OSData : 6892 -> 6896
~ __ZN16AppleBCMWLANCore35parseExtendedEventLogRecordScanChanEP6OSData : 2392 -> 2384
~ __ZN16AppleBCMWLANCore26updateRC2CoexStatsReportV1EP6OSData : 1488 -> 1492
~ __ZN16AppleBCMWLANCore26updateRC2CoexStatsReportV3EP6OSData : 2000 -> 2012
~ __ZN16AppleBCMWLANCore24postRoamCompletionStatusER21AppleBCMWLANBSSBeacon : 876 -> 872
~ __ZN16AppleBCMWLANCore26handleCCAOnlyChanQualEventEP14wl_event_msg_t : 2140 -> 2132
~ __ZN16AppleBCMWLANCore26collectSCTxBlankingSummaryEv : 228 -> 204
~ __ZN16AppleBCMWLANCore22captureRequestCallbackEPKcPK11CCTimestamp : 472 -> 480
~ __ZN16AppleBCMWLANCore23getWCL_TRAFFIC_COUNTERSEP31apple80211_wcl_traffic_counters : 180 -> 164
~ __ZN16AppleBCMWLANCore19getPOWER_DEBUG_INFOEP27apple80211_power_debug_info : 620 -> 636
~ _OUTLINED_FUNCTION_111 : 20 -> 32
~ _OUTLINED_FUNCTION_112 : 32 -> 20
~ _OUTLINED_FUNCTION_442 : 24 -> 16
~ _OUTLINED_FUNCTION_443 : 16 -> 24
~ __ZN28AppleBCMWLANBusInterfacePCIe18detachPCIeBusGatedEP11IOPCIDeviceb : 1104 -> 1172
~ ____ZN28AppleBCMWLANBusInterfacePCIe18detachPCIeBusGatedEP11IOPCIDeviceb_block_invoke : 24 -> 204
+ ____ZN28AppleBCMWLANBusInterfacePCIe18detachPCIeBusGatedEP11IOPCIDeviceb_block_invoke_2
~ ____ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke : 440 -> 972
~ __ZN16AppleBCMWLANCore25handleLinkInactivityCheckEP18IO80211TimerSource : 1148 -> 1160
~ __ZN16AppleBCMWLANCore17handleEventPacketEPKN16AppleBCMWLANUtil12DeviceBufferE : 6656 -> 6652
~ __ZN16AppleBCMWLANCore10setCHANNELEP23apple80211_channel_data : 1156 -> 1148
+ ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.cold.1
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1570.62\""
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLAN11beAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBSSBeacon.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBssManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommandMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommander.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCore.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCoreDbg.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingHelpers.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingPerSlice.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANJoinAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANLQM.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANNANInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANPowerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANProximityInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANScanAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANTxPowerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANBusInterfacePCIe.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.S9cL4R/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANPCIeSkywalk.cpp"
+ "AppleBCMWLANV3_driverkit-1570.62"
+ "Jul 10 2026 22:07:08"
+ "[dk] %s@%d:APB CB error-log registers before readOTP:\n"
+ "[dk] %s@%d:CB0[0x%x] = 0x%08x\n"
+ "[dk] %s@%d:CB0[0x%x] read failed: 0x%x\n"
+ "[dk] %s@%d:CB1[0x%x] = 0x%08x\n"
+ "[dk] %s@%d:CB1[0x%x] read failed: 0x%x\n"
- "\"AppleBCMWLANV3_driverkit-1570.56\""
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLAN11beAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBSSBeacon.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANBssManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommandMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCommander.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCore.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANCoreDbg.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingHelpers.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANIOReportingPerSlice.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANJoinAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANLQM.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANNANInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANPowerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANProximityInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANScanAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLANTxPowerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANBusInterfacePCIe.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Gfgvk2/Sources/AppleBCMWLANV3_driverkit/Busses/PCIe/AppleBCMWLANPCIeSkywalk.cpp"
- "AppleBCMWLANV3_driverkit-1570.56"
- "Jun 29 2026 21:22:14"
```
