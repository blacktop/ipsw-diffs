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

-1580.63.0.0.0
-  __TEXT.__text: 0x29103c
-  __TEXT.__auth_stubs: 0x25b0
+1580.68.0.0.0
+  __TEXT.__text: 0x2913ac
+  __TEXT.__auth_stubs: 0x25c0
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x8300f
+  __TEXT.__cstring: 0x830d4
   __TEXT.__const: 0x7f168
   __TEXT.__oslogstring: 0x1f27
-  __TEXT.__unwind_info: 0x5fd0
+  __TEXT.__unwind_info: 0x5fd8
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__const: 0x21100
+  __DATA_CONST.__const: 0x21120
   __DATA_CONST.__osclassinfo: 0x388
-  __DATA_CONST.__auth_got: 0x12d8
+  __DATA_CONST.__auth_got: 0x12e0
   __DATA_CONST.__got: 0x108
   __DATA.__data: 0x390
   __DATA.__bss: 0x948

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 14172
-  Symbols:   12055
-  CStrings:  13125
+  Functions: 14174
+  Symbols:   12057
+  CStrings:  13130
 
Symbols:
+ __ZN16IODispatchSource6CancelEU13block_pointerFvvEPFiP15OSMetaClassBase5IORPCE
+ ____ZN28AppleBCMWLANBusInterfacePCIe18detachPCIeBusGatedEP11IOPCIDeviceb_block_invoke_2
Functions:
~ __ZN28AppleBCMWLANNANDataInterface5startEP16AppleBCMWLANCoreP16RegistrationInfo : 1260 -> 1256
~ __ZN24AppleBCMWLANNANInterface5startEP16AppleBCMWLANCoreP16RegistrationInfo : 1108 -> 1104
~ __ZN30AppleBCMWLANProximityInterface5startEP16AppleBCMWLANCoreP16RegistrationInfo : 1080 -> 1076
~ __ZN19AppleBCMWLANCoreDbg10cmdTXStallEP24apple80211_debug_commandP16AppleBCMWLANCore : 236 -> 232
~ __ZN28AppleBCMWLANSkywalkInterface5startEP16AppleBCMWLANCoreP16RegistrationInfo : 1532 -> 1528
~ __ZN16AppleBCMWLANCore4initEP12OSDictionary : 4400 -> 4380
~ __ZN16AppleBCMWLANCore18getNanRxPktCounterEv : 44 -> 28
~ __ZN16AppleBCMWLANCore15dumpWmeCountersEPcii : 868 -> 836
~ __ZN16AppleBCMWLANCore15processChipCapsEv : 708 -> 700
~ __ZN16AppleBCMWLANCore17parseEventLogScanEP6OSData : 6892 -> 6896
~ __ZN16AppleBCMWLANCore26updateRC2CoexStatsReportV1EP6OSData : 1488 -> 1492
~ __ZN16AppleBCMWLANCore26updateRC2CoexStatsReportV3EP6OSData : 2000 -> 2012
~ __ZN16AppleBCMWLANCore26updateRC1CoexStatsReportV1EP6OSData : 1004 -> 1000
~ __ZN16AppleBCMWLANCore26updateRC1CoexStatsReportV2EP6OSData : 1136 -> 1140
~ __ZN16AppleBCMWLANCore26updateRC1CoexStatsReportV4EP6OSData : 1324 -> 1328
~ __ZN16AppleBCMWLANCore24postRoamCompletionStatusER21AppleBCMWLANBSSBeacon : 876 -> 872
~ __ZN16AppleBCMWLANCore26handleCCAOnlyChanQualEventEP14wl_event_msg_t : 2132 -> 2140
~ __ZN16AppleBCMWLANCore26collectSCTxBlankingSummaryEv : 228 -> 204
~ __ZN16AppleBCMWLANCore22captureRequestCallbackEPKcPK11CCTimestamp : 472 -> 480
~ __ZN16AppleBCMWLANCore23getWCL_TRAFFIC_COUNTERSEP31apple80211_wcl_traffic_counters : 180 -> 164
~ __ZN16AppleBCMWLANCore19getPOWER_DEBUG_INFOEP27apple80211_power_debug_info : 624 -> 632
~ _OUTLINED_FUNCTION_169 : 16 -> 36
~ _OUTLINED_FUNCTION_170 : 36 -> 16
~ _OUTLINED_FUNCTION_433 : 12 -> 28
~ _OUTLINED_FUNCTION_434 : 28 -> 12
~ _OUTLINED_FUNCTION_608 : 20 -> 12
~ _OUTLINED_FUNCTION_615 : 12 -> 20
~ __ZN28AppleBCMWLANBusInterfacePCIe18detachPCIeBusGatedEP11IOPCIDeviceb : 1104 -> 1172
~ ____ZN28AppleBCMWLANBusInterfacePCIe18detachPCIeBusGatedEP11IOPCIDeviceb_block_invoke : 24 -> 204
+ ____ZN28AppleBCMWLANBusInterfacePCIe18detachPCIeBusGatedEP11IOPCIDeviceb_block_invoke_2
~ ____ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke : 440 -> 972
~ __ZN16AppleBCMWLANCore25handleLinkInactivityCheckEP18IO80211TimerSource : 1164 -> 1168
~ __ZN16AppleBCMWLANCore17handleEventPacketEPKN16AppleBCMWLANUtil12DeviceBufferE : 6220 -> 6216
~ __ZN16AppleBCMWLANCore10setCHANNELEP23apple80211_channel_data : 1148 -> 1156
+ ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.cold.1
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1580.68\""
+ "AppleBCMWLANV3_driverkit-1580.68"
+ "Jul 10 2026 21:53:28"
+ "[dk] %s@%d:APB CB error-log registers before readOTP:\n"
+ "[dk] %s@%d:CB0[0x%x] = 0x%08x\n"
+ "[dk] %s@%d:CB0[0x%x] read failed: 0x%x\n"
+ "[dk] %s@%d:CB1[0x%x] = 0x%08x\n"
+ "[dk] %s@%d:CB1[0x%x] read failed: 0x%x\n"
- "\"AppleBCMWLANV3_driverkit-1580.63\""
- "AppleBCMWLANV3_driverkit-1580.63"
- "Jul  1 2026 23:33:59"
```
