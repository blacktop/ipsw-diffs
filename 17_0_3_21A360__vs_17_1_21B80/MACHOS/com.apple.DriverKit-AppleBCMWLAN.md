## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1151.54.0.1.0
-  __TEXT.__text: 0x25728c
-  __TEXT.__auth_stubs: 0x2d50
-  __TEXT.__init_offsets: 0x1d0
-  __TEXT.__cstring: 0x84ba6
-  __TEXT.__const: 0x694a0
-  __TEXT.__oslogstring: 0x314f
-  __TEXT.__unwind_info: 0x3cbc
-  __DATA_CONST.__auth_got: 0x16a8
+1153.5.0.0.0
+  __TEXT.__text: 0x2593cc
+  __TEXT.__auth_stubs: 0x2d80
+  __TEXT.__init_offsets: 0x1d4
+  __TEXT.__cstring: 0x84f03
+  __TEXT.__const: 0x695e0
+  __TEXT.__oslogstring: 0x3150
+  __TEXT.__unwind_info: 0x3cc4
+  __DATA_CONST.__auth_got: 0x16c0
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x21a30
-  __DATA_CONST.__osclassinfo: 0x390
+  __DATA_CONST.__const: 0x21b98
+  __DATA_CONST.__osclassinfo: 0x398
   __DATA.__data: 0x710
-  __DATA.__bss: 0x948
-  __DATA.__common: 0x390
+  __DATA.__bss: 0x950
+  __DATA.__common: 0x398
   - /System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit
   - /System/DriverKit/System/Library/Frameworks/NetworkingDriverKit.framework/NetworkingDriverKit
   - /System/DriverKit/System/Library/Frameworks/PCIDriverKit.framework/PCIDriverKit

   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
   - @rpath/BroadcomWLANDriverKit.framework/BroadcomWLANDriverKit
-  UUID: D0707D1F-1F56-3EF6-BE4D-0CA064B4CCA7
-  Functions: 7499
-  Symbols:   10338
-  CStrings:  13319
+  UUID: 61F7475D-897D-3B36-BA37-2DA74203D88A
+  Functions: 7520
+  Symbols:   10369
+  CStrings:  13338
 
Symbols:
+ _AppleBCMWLANSensingAdapter_Class
+ _GLOBAL__sub_I_AppleBCMWLANSensingAdapter.cpp
+ _ZN40AppleBCMWLANPCIeSkywalkTxSubmissionQueue14dequeuePacketsEP8OSObjectPP20IO80211NetworkPacketjPv.cold.1
+ __Z27IO80211_io80211isDebuggablev
+ __Z9isMemZeroPKcj
+ __ZL30AppleBCMWLANSensingAdapter_NewP11OSMetaClass
+ __ZL45OSClassDescription_AppleBCMWLANSensingAdapter
+ __ZN11AppleOLYHAL23setDictPropertyHelperDKEP8OSStringP12OSDictionary
+ __ZN11AppleOLYHAL25setStringPropertyHelperDKEP8OSStringS1_
+ __ZN16AppleBCMWLANCore16isSensingCapableEv
+ __ZN16AppleBCMWLANCore29isSensingOSFeatureFlagEnabledEv
+ __ZN25AppleBCMWLANPCIeFlowQueue7setBusyEv
+ __ZN25AppleBCMWLANPCIeFlowQueue9clearBusyEv
+ __ZN26AppleBCMWLANSensingAdapter10withDriverEP16AppleBCMWLANCore
+ __ZN26AppleBCMWLANSensingAdapter13freeResourcesEv
+ __ZN26AppleBCMWLANSensingAdapter14initWithDriverEP16AppleBCMWLANCore
+ __ZN26AppleBCMWLANSensingAdapter15getSENSING_DATAEP25apple80211_sensing_data_t
+ __ZN26AppleBCMWLANSensingAdapter17setSENSING_ENABLEEP27apple80211_sensing_enable_t
+ __ZN26AppleBCMWLANSensingAdapter18handleSensingEventEP14wl_event_msg_t
+ __ZN26AppleBCMWLANSensingAdapter18setSENSING_DISABLEEP28apple80211_sensing_disable_t
+ __ZN26AppleBCMWLANSensingAdapter20getSENSING_DATA_INFOEP30apple80211_sensing_data_info_t
+ __ZN26AppleBCMWLANSensingAdapter20handleSensingVersionER9CommandIDiR16CommandRxPayloadPv
+ __ZN26AppleBCMWLANSensingAdapter20updateSensingVersionEv
+ __ZN26AppleBCMWLANSensingAdapter4freeEv
+ __ZN28AppleBCMWLANBusInterfacePCIe23setOLYHALPropertyHelperEPKcP8OSObject
+ __ZN35AppleBCMWLANSensingAdapterMetaClass3NewEP8OSObject
+ __ZN40AppleBCMWLANPCIeSkywalkTxSubmissionQueue21findOrCreateFlowQueueEP20IO80211FlowQueueHash
+ __ZTV26AppleBCMWLANSensingAdapter
+ __ZTV35AppleBCMWLANSensingAdapterMetaClass
+ __ZThn24_N26AppleBCMWLANSensingAdapter4freeEv
+ __ZThn48_N28AppleBCMWLANBusInterfacePCIe23setOLYHALPropertyHelperEPKcP8OSObject
+ __ZThn56_N25AppleBCMWLANPCIeFlowQueue7setBusyEv
+ __ZThn56_N25AppleBCMWLANPCIeFlowQueue9clearBusyEv
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2490
+ ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1045
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.652
+ __block_descriptor_tmp.1041
+ __block_descriptor_tmp.1050
+ __block_descriptor_tmp.1051
+ __block_descriptor_tmp.1088
+ __block_descriptor_tmp.1586
+ __block_descriptor_tmp.1819
+ __block_descriptor_tmp.2114
+ __block_descriptor_tmp.2488
+ __block_descriptor_tmp.2492
+ __block_descriptor_tmp.2509
+ __block_descriptor_tmp.2541
+ __block_descriptor_tmp.2869
+ __block_descriptor_tmp.2905
+ __block_descriptor_tmp.304
+ __block_descriptor_tmp.3455
+ __block_descriptor_tmp.3537
+ __block_descriptor_tmp.354
+ __block_descriptor_tmp.3549
+ __block_descriptor_tmp.3551
+ __block_descriptor_tmp.3554
+ __block_descriptor_tmp.3560
+ __block_descriptor_tmp.3579
+ __block_descriptor_tmp.499
+ __block_descriptor_tmp.541
+ __block_descriptor_tmp.548
+ __block_descriptor_tmp.650
+ __block_descriptor_tmp.655
+ __block_descriptor_tmp.669
+ __block_descriptor_tmp.674
+ __block_descriptor_tmp.681
+ __block_descriptor_tmp.684
+ __block_descriptor_tmp.685
+ __block_descriptor_tmp.695
+ __block_descriptor_tmp.796
+ __block_descriptor_tmp.800
+ __block_descriptor_tmp.801
+ __block_descriptor_tmp.810
+ __block_literal_global.2543
+ _gAppleBCMWLANSensingAdapterMetaClass
+ _gAppleBCMWLANSensingAdapter_Declaration
- __ZN11AppleOLYHAL19setPropertyHelperDKEP8OSStringS1_
- __ZN16AppleBCMWLANCore20getSENSING_DATA_INFOEP30apple80211_sensing_data_info_t
- __ZN28AppleBCMWLANBusInterfacePCIe23setOLYHALPropertyHelperEPKcP8OSString
- __ZThn48_N28AppleBCMWLANBusInterfacePCIe23setOLYHALPropertyHelperEPKcP8OSString
- __ZThn64_N16AppleBCMWLANCore20getSENSING_DATA_INFOEP30apple80211_sensing_data_info_t
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2495
- ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1043
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.650
- __block_descriptor_tmp.1039
- __block_descriptor_tmp.1046
- __block_descriptor_tmp.1049
- __block_descriptor_tmp.1087
- __block_descriptor_tmp.1585
- __block_descriptor_tmp.1818
- __block_descriptor_tmp.2113
- __block_descriptor_tmp.2493
- __block_descriptor_tmp.2497
- __block_descriptor_tmp.2514
- __block_descriptor_tmp.2546
- __block_descriptor_tmp.2873
- __block_descriptor_tmp.2909
- __block_descriptor_tmp.302
- __block_descriptor_tmp.3459
- __block_descriptor_tmp.350
- __block_descriptor_tmp.3541
- __block_descriptor_tmp.3553
- __block_descriptor_tmp.3555
- __block_descriptor_tmp.3558
- __block_descriptor_tmp.3564
- __block_descriptor_tmp.3583
- __block_descriptor_tmp.497
- __block_descriptor_tmp.539
- __block_descriptor_tmp.546
- __block_descriptor_tmp.648
- __block_descriptor_tmp.653
- __block_descriptor_tmp.667
- __block_descriptor_tmp.672
- __block_descriptor_tmp.679
- __block_descriptor_tmp.682
- __block_descriptor_tmp.683
- __block_descriptor_tmp.691
- __block_descriptor_tmp.795
- __block_descriptor_tmp.798
- __block_descriptor_tmp.799
- __block_descriptor_tmp.808
- __block_literal_global.2548
CStrings:
+ " AWDL if creation timedout error %x"
+ " AWDL if deletion timedout error %x"
+ "\"AppleBCMWLANV3_driverkit-1153.5\""
+ "%c [dk] %s@%d:  Modified BSSID Priority List: BSSID %02x:%02x:%02x:%02x:%02x:%02x is in Channel %u RSSI %d \n"
+ "%c [dk] %s@%d:  Most likely the Association Scan (FW) did not find SSID \"%s\"\n"
+ "%c [dk] %s@%d: %s::%s getting sib coex mode %d , timeToTST %d\n"
+ "/AppleInternal/Library/BuildRoots/e3fd56b6-6080-11ee-999f-c6501008687b/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS23.1.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANCore::%s/%u: AdjustBusy(-1)! busystate %u, fAdjustBusyCnt %u, kAdjustBusyTimeout_ms %u\n"
+ "AppleBCMWLANV3_driverkit-1153.5"
+ "Interface NULL!"
+ "Oct  1 2023 20:23:29"
+ "WLC_SET_VAR: actframe"
+ "[dk] %s@%d: AWDL interface index is: %u (bsscfg=%u), fwVer %d opcode %d\n"
+ "[dk] %s@%d: Modified BSSID Priority List: BSSID %02x:%02x:%02x:%02x:%02x:%02x is in Channel %u RSSI %d \n"
+ "[dk] %s@%d: Most likely the Association Scan (FW) did not find SSID \"%s\"\n"
+ "[dk] %s@%d: Network with BSSID %02x:%02x:%02x:%02x:%02x:%02x is Fully Loaded \n"
+ "[dk] %s@%d: Network with BSSID %02x:%02x:%02x:%02x:%02x:%02x is in Peer Channel %u  RSSI %d \n"
+ "[dk] %s@%d: No such network with BSSID: %02x:%02x:%02x:%02x:%02x:%02x \n"
+ "[dk] %s@%d: Ranging result V2: session=%d, flags=0x%x, status=%d(%s), peer=%02X:%02X:%02X:%02X:%02X:%02X, state=%d,avg_dist=%d.%04dm,  num RTT samples=%d, valid=%d, num_ftm %d, burst_num  %d\n "
+ "[dk] %s@%d: Trying to force BSSID to %02x:%02x:%02x:%02x:%02x:%02x \n"
+ "[dk] %s@%d: Unable to create fSensingAdapter\n"
+ "[dk] %s@%d: Unable to get fFaultReporter\n"
+ "[dk] %s@%d: Unable to setProperty() on OLYHAL\n"
+ "[dk] %s@%d: requested bandwidth %d and actually bandwidth %d\n"
+ "[dk] %s@%d:%s::%s getting sib coex mode %d , timeToTST %d\n"
+ "[dk] %s@%d:AWDL i/f deletion timedout Error = %s(%d)\n"
+ "[dk] %s@%d:AppleBCMWLANCore::%s/%u: AdjustBusy(-1)! busystate %u, fAdjustBusyCnt %u, kAdjustBusyTimeout_ms %u\n"
+ "[dk] %s@%d:Join Addr: %02x:%02x:%02x:%02x:%02x:%02x Join retVal: 0x%x Join ieeeStatus: 0x%x\n"
+ "[dk] %s@%d:No matching property type for key %s\n"
+ "[dk] %s@%d:Payload length is not of expected value, expected %zu, received %u\n"
+ "[dk] %s@%d:Sensing adapter version is %d\n"
+ "[dk] %s@%d:Sensing not supported %d\n"
+ "[dk] %s@%d:Unable to get WL_CSI_SUBCMD_VERSION: %s\n"
+ "[dk] %s@%d:Unable to get sensing version from FW %d\n"
+ "[dk] %s@%d:Updating WPA3 Feature support addr = %02x:%02x:%02x:%02x:%02x:%02x \n"
+ "[dk] %s@%d:{%d} BSSID Addr: %02x:%02x:%02x:%02x:%02x:%02x flags 0x%x authStatus 0x%x authReason 0x%x assocStatus 0x%x assocReason 0x%x setSsidStatus 0x%x setSsidReason 0x%x supplEvStatus 0x%x supplEvReason 0x%x\n"
+ "handleSensingVersion"
+ "setOLYHALPropertyHelper"
+ "updateSensingVersion"
- "\"AppleBCMWLANV3_driverkit-1151.54.0.1\""
- "%c [dk] %s@%d:  Modified BSSID Priority List: BSSID %x %x %x %x %x %x is in Channel %u RSSI %d \n"
- "%c [dk] %s@%d:  Most likely the Association Scan (FW) did not find SSID \"%s\" (see <rdar://11682490>)\n"
- "%c [dk] %s@%d: %s:%s() getting sib coex mode %d \n"
- "/AppleInternal/Library/BuildRoots/495afeab-4054-11ee-8fa3-46d450270006/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS23.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANCore::%s/%u: AdjustBusy(-1) timeout in %u ms! busystate %u, fAdjustBusyCnt %u\n"
- "AppleBCMWLANV3_driverkit-1151.54.0.1"
- "Aug 21 2023 19:53:05"
- "[dk] %s@%d: AWDL interface index is: %u (bsscfg=%u), fwVer %d\n"
- "[dk] %s@%d: Modified BSSID Priority List: BSSID %x %x %x %x %x %x is in Channel %u RSSI %d \n"
- "[dk] %s@%d: Most likely the Association Scan (FW) did not find SSID \"%s\" (see <rdar://11682490>)\n"
- "[dk] %s@%d: Network with BSSID %x %x %x %x %x %x is Fully Loaded \n"
- "[dk] %s@%d: No such network with BSSID: %02X:%02X:%02X:%02X:%02X:%02X \n"
- "[dk] %s@%d: Ranging result V2: session=%d, flags=0x%x, status=%d(%s), peer=%02X:%02X:%02X:%02X:%02X:%02X, state=%d,avg_dist=%s%d.%04dm,  num RTT samples=%d, valid=%d, num_ftm %d, burst_num  %d\n "
- "[dk] %s@%d: Trying to force BSSID to %02X:%02X:%02X:%02X:%02X:%02X \n"
- "[dk] %s@%d:%s:%s() getting sib coex mode %d \n"
- "[dk] %s@%d:AppleBCMWLANCore::%s/%u: AdjustBusy(-1) timeout in %u ms! busystate %u, fAdjustBusyCnt %u\n"
- "[dk] %s@%d:Join Addr: 0x%x:0x%x:0x%x:0x:%x:0x%x:0x%x Join retVal: 0x%x Join ieeeStatus: 0x%x\n"
- "[dk] %s@%d:Updating WPA3 Feature support addr = %02x:%02x:%02x:%02x:%02x:%02x\n"
- "[dk] %s@%d:{%d} BSSID Addr: 0x%x:0x%x:0x%x:0x:%x:0x%x:0x%x flags 0x%x authStatus 0x%x authReason 0x%x assocStatus 0x%x assocReason 0x%x setSsidStatus 0x%x setSsidReason 0x%x supplEvStatus 0x%x supplEvReason 0x%x\n"

```
