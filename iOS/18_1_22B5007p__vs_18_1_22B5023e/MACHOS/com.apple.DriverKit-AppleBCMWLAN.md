## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1256.92.0.0.0
-  __TEXT.__text: 0x27a398
-  __TEXT.__auth_stubs: 0x24a0
+1256.100.0.0.0
+  __TEXT.__text: 0x279bb4
+  __TEXT.__auth_stubs: 0x2480
   __TEXT.__init_offsets: 0x1ac
-  __TEXT.__cstring: 0x7c261
+  __TEXT.__cstring: 0x7c09e
   __TEXT.__const: 0x69a70
   __TEXT.__oslogstring: 0x1f59
-  __TEXT.__unwind_info: 0x3770
-  __DATA_CONST.__auth_got: 0x1250
+  __TEXT.__unwind_info: 0x3750
+  __DATA_CONST.__auth_got: 0x1240
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x1f040
+  __DATA_CONST.__const: 0x1efa0
   __DATA_CONST.__osclassinfo: 0x368
   __DATA.__data: 0x590
   __DATA.__bss: 0x940

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 6804
-  Symbols:   9481
-  CStrings:  12491
+  Functions: 6795
+  Symbols:   9462
+  CStrings:  12481
 
Symbols:
+ __ZN16AppleBCMWLANCore22configureScanParamModsEv
+ __ZN19IOUserNetworkPacket12initWithPoolEP29IOUserNetworkPacketBufferPoolP29IOUserNetworkPacketDescriptorj
+ __ZN19IOUserNetworkPacket4freeEv
+ __ZN23AppleBCMWLANJoinAdapter25handleDeauthDisassocEventEt
+ __ZN25AppleBCMWLANChipBackplane16setPCIeLinkStateE13PCIeLinkState
+ __ZN25AppleBCMWLANConfigManager11isNewDeviceEv
+ __ZN31AppleBCMWLANIOReportingPerSlice22reportUcodeCntPerSliceEP6OSData19AppleBCMWLANSliceId25AppleBCMWLANuCodeStatsVerP21apple80211_chip_statsb
+ __ZThn40_N19IOUserNetworkPacket12initWithPoolEP29IOUserNetworkPacketBufferPoolP29IOUserNetworkPacketDescriptorj
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2252
+ ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1082
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.682
+ __block_descriptor_tmp.1078
+ __block_descriptor_tmp.1085
+ __block_descriptor_tmp.1088
+ __block_descriptor_tmp.1649
+ __block_descriptor_tmp.1956
+ __block_descriptor_tmp.2250
+ __block_descriptor_tmp.2254
+ __block_descriptor_tmp.2272
+ __block_descriptor_tmp.2304
+ __block_descriptor_tmp.2631
+ __block_descriptor_tmp.2667
+ __block_descriptor_tmp.3139
+ __block_descriptor_tmp.3224
+ __block_descriptor_tmp.3240
+ __block_descriptor_tmp.3242
+ __block_descriptor_tmp.3245
+ __block_descriptor_tmp.3251
+ __block_descriptor_tmp.3289
+ __block_descriptor_tmp.329
+ __block_descriptor_tmp.379
+ __block_descriptor_tmp.381
+ __block_descriptor_tmp.528
+ __block_descriptor_tmp.571
+ __block_descriptor_tmp.578
+ __block_descriptor_tmp.656
+ __block_descriptor_tmp.680
+ __block_descriptor_tmp.685
+ __block_descriptor_tmp.699
+ __block_descriptor_tmp.704
+ __block_descriptor_tmp.711
+ __block_descriptor_tmp.715
+ __block_descriptor_tmp.723
+ __block_descriptor_tmp.725
+ __block_descriptor_tmp.793
+ __block_descriptor_tmp.831
+ __block_descriptor_tmp.840
+ __block_descriptor_tmp.935
+ __block_literal_global.2274
+ __block_literal_global.2306
- __ZN15IODispatchQueue7OnQueueEv
- __ZN16AppleBCMWLANCore19setMANUFACTURE_DATEEP27apple80211_manufacture_date
- __ZN16AppleBCMWLANCore21disableHtSisoOnlySafeEv
- __ZN16AppleBCMWLANCore26setFIRST_BOOT_COUNTRY_CODEEP28apple80211_country_code_data
- __ZN16AppleBCMWLANUtil24getCounterValueSafeIOBMDEPilP24IOBufferMemoryDescriptorj
- __ZN16AppleBCMWLANUtil29AutoreleasedAlignedIOBufferMDC2EP6OSDatam
- __ZN20IO80211NetworkPacket12initWithPoolEP29IOUserNetworkPacketBufferPoolP29IOUserNetworkPacketDescriptorj
- __ZN20IO80211NetworkPacket14getPrivateDataEv
- __ZN20IO80211NetworkPacket14setPrivateDataEPv
- __ZN20IO80211NetworkPacket4freeEv
- __ZN20IO80211NetworkPacket8getEntryEv
- __ZN22AppleBCMWLANWnmAdapter24unconfigureWNMKeepAlivesEv
- __ZN23AppleBCMWLANJoinAdapter25handleDeauthDisassocEventEv
- __ZN24IOBufferMemoryDescriptor6CreateEyyyPPS_
- __ZN25AppleBCMWLANInfraProtocol19setMANUFACTURE_DATEEP27apple80211_manufacture_date
- __ZN25AppleBCMWLANInfraProtocol26setFIRST_BOOT_COUNTRY_CODEEP28apple80211_country_code_data
- __ZN31AppleBCMWLANIOReportingPerSlice22reportUcodeCntPerSliceEP6OSData19AppleBCMWLANSliceId14AppleBCMWLANBwP21apple80211_chip_statsb
- __ZThn112_N25AppleBCMWLANInfraProtocol19setMANUFACTURE_DATEEP27apple80211_manufacture_date
- __ZThn112_N25AppleBCMWLANInfraProtocol26setFIRST_BOOT_COUNTRY_CODEEP28apple80211_country_code_data
- __ZThn128_N25AppleBCMWLANInfraProtocol19setMANUFACTURE_DATEEP27apple80211_manufacture_date
- __ZThn128_N25AppleBCMWLANInfraProtocol26setFIRST_BOOT_COUNTRY_CODEEP28apple80211_country_code_data
- __ZThn40_N20IO80211NetworkPacket12initWithPoolEP29IOUserNetworkPacketBufferPoolP29IOUserNetworkPacketDescriptorj
- __ZThn56_N20IO80211NetworkPacket14getPrivateDataEv
- __ZThn56_N20IO80211NetworkPacket14setPrivateDataEPv
- __ZThn56_N20IO80211NetworkPacket8getEntryEv
- __ZThn64_N16AppleBCMWLANCore19setMANUFACTURE_DATEEP27apple80211_manufacture_date
- __ZThn64_N16AppleBCMWLANCore26setFIRST_BOOT_COUNTRY_CODEEP28apple80211_country_code_data
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2251
- ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1081
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.681
- __block_descriptor_tmp.1077
- __block_descriptor_tmp.1084
- __block_descriptor_tmp.1086
- __block_descriptor_tmp.1651
- __block_descriptor_tmp.1955
- __block_descriptor_tmp.2249
- __block_descriptor_tmp.2253
- __block_descriptor_tmp.2271
- __block_descriptor_tmp.2303
- __block_descriptor_tmp.2632
- __block_descriptor_tmp.2668
- __block_descriptor_tmp.3140
- __block_descriptor_tmp.3225
- __block_descriptor_tmp.3241
- __block_descriptor_tmp.3243
- __block_descriptor_tmp.3246
- __block_descriptor_tmp.3252
- __block_descriptor_tmp.328
- __block_descriptor_tmp.3290
- __block_descriptor_tmp.378
- __block_descriptor_tmp.380
- __block_descriptor_tmp.527
- __block_descriptor_tmp.570
- __block_descriptor_tmp.577
- __block_descriptor_tmp.659
- __block_descriptor_tmp.679
- __block_descriptor_tmp.684
- __block_descriptor_tmp.698
- __block_descriptor_tmp.703
- __block_descriptor_tmp.710
- __block_descriptor_tmp.713
- __block_descriptor_tmp.722
- __block_descriptor_tmp.724
- __block_descriptor_tmp.796
- __block_descriptor_tmp.829
- __block_descriptor_tmp.839
- __block_descriptor_tmp.938
- __block_literal_global.2273
- __block_literal_global.2305
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1256.100\""
+ "/AppleInternal/Library/BuildRoots/6bc26dac-5425-11ef-9730-5a7ac3341c94/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.1.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANCore::Start_Impl: done: failed: ret[0x%!x(MISSING)], this[%!p(MISSING)] provider[%!p(MISSING)], fProvider[%!p(MISSING)], reason[%!u(MISSING)] line[%!u(MISSING)], init failed[%!u(MISSING)]\n"
+ "AppleBCMWLANV3_driverkit-1256.100"
+ "Aug  6 2024 20:34:36"
+ "BCMWLAN Join Program PMK failed"
+ "Skywalk Packet init fail\n"
+ "WLC_SET_WSEC_PMK key len %!x(MISSING)"
+ "[dk] %!s(MISSING)@%!d(MISSING): Error: P2p Peer stats %!s(MISSING) iovar for [%!X(MISSING):%!X(MISSING):%!X(MISSING):%!X(MISSING):%!X(MISSING):%!X(MISSING)], peers %!u(MISSING), index %!u(MISSING), status %!u(MISSING) busy %!d(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Associated Sleep issued not setting beaocn intervals for active mode\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Error parsing parseV30CntContainer\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):GE40_UCODE_V1 alignment fails\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):GE80_UCODE_V1 alignment fails\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):GE88_UCODE_RX_V1 alignment fails\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):GE88_UCODE_TX_V1 alignment fails\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):done: succcess: ret[0x%!x(MISSING)], this[%!p(MISSING)] provider[%!p(MISSING)], fProvider[%!p(MISSING)], reason[%!u(MISSING)] line[%!u(MISSING)], init failed[%!u(MISSING)]\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):parseV30CntContainer TLV on slice 2\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):parseV30CntContainer TLV on slice 2 ignored\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):tag id %!d(MISSING) Not implemented \n"
+ "[dk] %!s(MISSING)@%!d(MISSING):wlan core start failed, reason[%!u(MISSING)] line[%!u(MISSING)], init failed[%!u(MISSING)]\n"
+ "configureScanParamMods"
+ "forcePower"
+ "scanparams_mods"
+ "unexpected port error"
+ "wlan.debug.isNewDevice"
- "\"AppleBCMWLANV3_driverkit-1256.92\""
- "/AppleInternal/Library/BuildRoots/671bf17b-4179-11ef-9ec9-1aec23608739/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.1.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANCore::Start_Impl: done: failed: ret[0x%!x(MISSING)], this[%!p(MISSING)] provider[%!p(MISSING)], fProvider[%!p(MISSING)]\n"
- "AppleBCMWLANV3_driverkit-1256.92"
- "AutoreleasedAlignedIOBufferMD fIOBMD allocation failure size %!l(MISSING)d\n"
- "AutoreleasedAlignedIOBufferMD is not %!z(MISSING)u aligned %!p(MISSING)"
- "ERROR getCounterValueSafeIOBMD GetAddressRange failed\n"
- "ERROR getCounterValueSafeIOBMD Unsupported read size\n"
- "ERROR getCounterValueSafeIOBMD offset %!d(MISSING) sizeOfRead %!z(MISSING)d seg.length %!l(MISSING)lu\n"
- "ERROR getCounterValueSafeIOBMD read uint16_t failed\n"
- "ERROR getCounterValueSafeIOBMD read uint32_t failed\n"
- "ERROR getCounterValueSafeIOBMD read uint64_t failed\n"
- "ERROR getCounterValueSafeIOBMD seg.address not aligned at offset %!d(MISSING) sizeOfRead %!z(MISSING)d addr buf 0x%!l(MISSING)lx"
- "Jul 13 2024 18:43:23"
- "[dk] %!s(MISSING)@%!d(MISSING): Error: P2p Peer stats %!s(MISSING) iovar for [%!X(MISSING):%!X(MISSING):%!X(MISSING):%!X(MISSING):%!X(MISSING):%!X(MISSING)], peers %!u(MISSING), index %!u(MISSING), status %!u(MISSING) \n"
- "[dk] %!s(MISSING)@%!d(MISSING): Error: Unable to Get WNM Keep-Alive State:  Ret %!s(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING): Error: Unable to Reset WNM Keep Alives:  Ret %!s(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Not a german device but Siso enable, lets disable it cc<%!c(MISSING) %!c(MISSING)> siso=<%!d(MISSING)> isAssociated=<%!d(MISSING)>\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Old device=<%!d(MISSING)>  date<%!d(MISSING)/%!d(MISSING)/%!d(MISSING)> limit<%!d(MISSING)/%!d(MISSING)/%!d(MISSING)> siso=<%!d(MISSING)> isAssociated=<%!d(MISSING)>\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Skywalk Packet init fail\n"
- "[dk] %!s(MISSING)@%!d(MISSING):disable HT Siso \n"
- "[dk] %!s(MISSING)@%!d(MISSING):done: succcess: ret[0x%!x(MISSING)], this[%!p(MISSING)] provider[%!p(MISSING)], fProvider[%!p(MISSING)]\n"
- "[dk] %!s(MISSING)@%!d(MISSING):isAllowHtSiso false \n"
- "[dk] %!s(MISSING)@%!d(MISSING):parseV30CntContainer\n"
- "[dk] %!s(MISSING)@%!d(MISSING):wlan core start failed\n"
- "disableHtSisoOnlySafe"
- "initWithPool"
- "setFIRST_BOOT_COUNTRY_CODE"
- "setMANUFACTURE_DATE"
- "unconfigureWNMKeepAlives"
- "updateInfraGenericStatistics"
- "wlan.isAllowHtSiso"
- "wlan.mf.day"
- "wlan.mf.month"
- "wlan.mf.year"

```
