## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

 1256.104.0.0.0
-  __TEXT.__text: 0x279bd4
+  __TEXT.__text: 0x2818a4
   __TEXT.__auth_stubs: 0x2480
-  __TEXT.__init_offsets: 0x1ac
-  __TEXT.__cstring: 0x7c09e
-  __TEXT.__const: 0x69a70
+  __TEXT.__init_offsets: 0x1b8
+  __TEXT.__cstring: 0x7daef
+  __TEXT.__const: 0x77630
   __TEXT.__oslogstring: 0x1f59
-  __TEXT.__unwind_info: 0x3750
+  __TEXT.__unwind_info: 0x37d8
   __DATA_CONST.__auth_got: 0x1240
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x1efa0
-  __DATA_CONST.__osclassinfo: 0x368
+  __DATA_CONST.__const: 0x1f7b8
+  __DATA_CONST.__osclassinfo: 0x378
   __DATA.__data: 0x590
-  __DATA.__bss: 0x940
-  __DATA.__common: 0x368
+  __DATA.__bss: 0x958
+  __DATA.__common: 0x378
   - /System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit
   - /System/DriverKit/System/Library/Frameworks/NetworkingDriverKit.framework/NetworkingDriverKit
   - /System/DriverKit/System/Library/Frameworks/PCIDriverKit.framework/PCIDriverKit

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 6795
-  Symbols:   9462
-  CStrings:  12481
+  Functions: 6887
+  Symbols:   9585
+  CStrings:  12647
 
Symbols:
+ __ZN23AppleBCMWLAN11beAdapter12getMloStatusEv
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439928getFWDebugPMUCoreRegionTableEv
+ __ZThn24_N23AppleBCMWLAN11beAdapter4freeEv
+ __ZN15AppleBCMWLANLQM23updateMloLinkChangeInfoEP25wl_mlo_link_info_event_v1
+ __ZN25AppleBCMWLANChipBackplane26writeOOBRouterWrapperReg32Ejj
+ __ZN25AppleBCMWLANChipBackplane27readAMNIScanMacWrapperReg32EjRj
+ __block_descriptor_tmp.936
+ __ZNK28AppleBCMWLANBusInterfacePCIe12checkPMNIAPBEv
+ __ZL35kBCOM4399FWDebugPCIEFunc0CoreRanges
+ __ZL27kBCOM4399UCodeSHMRegionInfo
+ __block_descriptor_tmp.331
+ __ZN25AppleBCMWLANChipBackplane27readAMNIScanPhyWrapperReg32EjRj
+ __block_descriptor_tmp.1650
+ __ZN15AppleBCMWLANLQM27updateMloTrafficSwitchStateEh
+ _ZN15AppleBCMWLANLQM18getMloPerLinkStatsEh.cold.1
+ __ZN23AppleBCMWLAN11beAdapter13dumpMloStatusEPcjj
+ __ZL33fileValidation4399ImagesSHA_array
+ __ZN23AppleBCMWLAN11beAdapter4freeEv
+ __block_descriptor_tmp.835
+ __block_descriptor_tmp.573
+ __block_descriptor_tmp.1134
+ __block_descriptor_tmp.845
+ _gAppleBCMWLAN11beAdapter_Declaration
+ __ZThn64_N28AppleBCMWLANBusInterfacePCIe14readcoexSoCRAMEjP6OSDataPyj
+ __block_descriptor_tmp.383
+ __block_descriptor_tmp.1133
+ __block_descriptor_tmp.1124
+ __ZN25AppleBCMWLANChipBackplane25readPMNIWLAPBWrapperReg32EjRj
+ __block_descriptor_tmp.3225
+ __ZN25AppleBCMWLANChipBackplane30readAMNIChipCommonWrapperReg32EjRj
+ __ZNK22AppleBCMWLANChipMemory11readCoexRAMEjjP13IO80211Bufferj
+ __ZN23AppleBCMWLAN11beAdapter15setupJoinConfigEbR10ether_addrb
+ __ZNK28AppleBCMWLANBusInterfacePCIe17dumpPMNIRegistersEv
+ __block_descriptor_tmp.385
+ __ZN15AppleBCMWLANLQM18getMloPerLinkStatsEh
+ __ZN31AppleBCMWLANChipManagerPCIe439931getFWDebugCommonCoreRegionTableEv
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439928getFWDebugARMCoreRegionTableEv
+ __ZN15AppleBCMWLANLQM15getMloPerfStatsEv
+ __ZN27AppleBCMWLANChipManagerPCIe23setCoexCPUTrapSupportedEb
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439921isSecureBootSupportedEv
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439932getFWDebugARMCoreRegionTableSizeEv
+ __ZN31AppleBCMWLANChipManagerPCIe439932getFWDebugPMUCoreRegionTableSizeEv
+ __ZN19AppleBCMWLANCoreDbg12cmdMloStatusEP24apple80211_debug_commandP16AppleBCMWLANCore
+ __block_descriptor_tmp.2273
+ __ZN28AppleBCMWLANBusInterfacePCIe14readcoexSoCRAMEjP6OSDataPyj
+ __block_literal_global.2307
+ __ZN25AppleBCMWLANChipBackplane26readAMNIAuxPhyWrapperReg32EjRj
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439931getFWDebugCommonCoreRegionTableEv
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.685
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439935getFWDebugCommonCoreRegionTableSizeEv
+ __ZTV40AppleBCMWLANChipManagerPCIe4399MetaClass
+ __ZN23AppleBCMWLAN11beAdapter22setMultilinkActiveModeEj
+ __ZN31AppleBCMWLANChipManagerPCIe439928getFWDebugPMUCoreRegionTableEv
+ _gAppleBCMWLANChipManagerPCIe4399_Declaration
+ _gAppleBCMWLAN11beAdapterMetaClass
+ __ZL27kBCOM4399UCodeSCRRegionInfo
+ _ZN23AppleBCMWLAN11beAdapter12configureMloEtR12mloAddrArray.cold.1
+ __ZN31AppleBCMWLANChipManagerPCIe43998withChipEjh
+ __block_descriptor_tmp.3290
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439915prepareHardwareEP27AppleBCMWLANChipConfigSpaceP25AppleBCMWLANChipBackplane
+ __ZN40AppleBCMWLANChipManagerPCIe4399MetaClass3NewEP8OSObject
+ __ZZN25AppleBCMWLANChipBackplane28dumpOOBConfigStatusRegistersEPcmE11oobCoreRegs
+ __ZN25AppleBCMWLANChipBackplane19dumpMNIIDMRegistersEPcm
+ __ZN28AppleBCMWLANBusInterfacePCIe20attachCoexSoCRAMFileEP13CCFaultReport
+ __ZL29kBCOM4399FWDebugPMUCoreRanges
+ __block_descriptor_tmp.728
+ __block_descriptor_tmp.718
+ __ZL29kBCOM4399FWDebugARMCoreRanges
+ __block_descriptor_tmp.3252
+ __ZL34kBCOM4399ChipConfigSpaceStateTable
+ __ZN23AppleBCMWLAN11beAdapter15setupInitConfigEv
+ __block_descriptor_tmp.206
+ __block_descriptor_tmp.688
+ __block_descriptor_tmp.3243
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439915hasMNIInterfaceEv
+ _GLOBAL__sub_I_AppleBCMWLAN11beAdapter.cpp
+ _gAppleBCMWLANChipManagerPCIe4399MetaClass
+ __ZL18kBCOM4399ChipCores
+ __ZN31AppleBCMWLANChipManagerPCIe439923getDARSecurityStatusRegEP25AppleBCMWLANChipBackplane
+ __block_descriptor_tmp.257
+ __ZN31AppleBCMWLANChipManagerPCIe439938getFWDebugPCIEFunc0CoreRegionTableSizeEv
+ __ZN25AppleBCMWLANChipBackplane39dumpCoreRegisterRegionswithMNIInterfaceEPcm
+ __block_descriptor_tmp.717
+ __ZN23AppleBCMWLAN11beAdapter20configureMloFeaturesEb
+ __ZN25AppleBCMWLANChipBackplane28dumpOOBConfigStatusRegistersEPcm
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439912initWithChipEjh
+ __ZN23AppleBCMWLAN11beAdapter15isMloConnectionEv
+ __ZN31AppleBCMWLANChipManagerPCIe439928getFWDebugARMCoreRegionTableEv
+ __ZN23AppleBCMWLAN11beAdapter12configureMloEtR12mloAddrArray
+ _AppleBCMWLAN11beAdapter_Class
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439938getFWDebugPCIEFunc0CoreRegionTableSizeEv
+ __ZL16kBCOM4399ChipOTP
+ __ZNK16AppleBCMWLANCore14get11beAdapterEv
+ _GLOBAL__sub_I_AppleBCMWLANChipManagerPCIe4399.cpp
+ __ZN25AppleBCMWLANChipBackplane25readPMNICBAPBWrapperReg32EjRj
+ __ZN31AppleBCMWLANChipManagerPCIe439921isSecureBootSupportedEv
+ __ZL50OSClassDescription_AppleBCMWLANChipManagerPCIe4399
+ __block_descriptor_tmp.683
+ __ZN25AppleBCMWLANChipBackplane23readHMNIGCIWrapperReg32EjRj
+ _ZN23AppleBCMWLAN11beAdapter15isMloConnectionEv.cold.1
+ __ZN23AppleBCMWLAN11beAdapter14initWithDriverEP16AppleBCMWLANCore
+ __ZTV32AppleBCMWLAN11beAdapterMetaClass
+ __ZZN20AppleBCMWLANChanSpec19getAppleChannelSpecEtE21chanIdToCenterlMap320
+ __ZN25AppleBCMWLANChipBackplane22readHMNIBTWrapperReg32EjRj
+ __ZL27AppleBCMWLAN11beAdapter_NewP11OSMetaClass
+ _ZN23AppleBCMWLAN11beAdapter12getMloStatusEv.cold.1
+ __ZTV23AppleBCMWLAN11beAdapter
+ __ZN31AppleBCMWLANChipManagerPCIe439912initWithChipEjh
+ __ZN32AppleBCMWLAN11beAdapterMetaClass3NewEP8OSObject
+ __block_descriptor_tmp.1957
+ __block_descriptor_tmp.2668
+ __block_descriptor_tmp.1131
+ __ZN31AppleBCMWLANChipManagerPCIe439935getFWDebugCommonCoreRegionTableSizeEv
+ __ZN31AppleBCMWLANChipManagerPCIe439913checkHardwareEP27AppleBCMWLANChipConfigSpaceP25AppleBCMWLANChipBackplane
+ __ZL21kBCOM4399ChipMemories
+ __ZL21kBCOM4399ChipWrappers
+ __ZN15AppleBCMWLANLQM16storeMloLinkInfoEhtRK10ether_addr
+ _AppleBCMWLANChipManagerPCIe4399_Class
+ __block_descriptor_tmp.836
+ __ZL20kBCOM4399ChipUserOTP
+ __ZN27AppleBCMWLANChipManagerPCIe32setFatalErrorIndicationSupportedEb
+ __ZN31AppleBCMWLANChipManagerPCIe439934getFWDebugPCIEFunc0CoreRegionTableEv
+ __block_descriptor_tmp.794
+ __block_descriptor_tmp.2305
+ __ZL29kBCOM4399ChipBackplaneWindows
+ ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1128
+ __ZL32kBCOM4399FWDebugCommonCoreRanges
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439913checkHardwareEP27AppleBCMWLANChipConfigSpaceP25AppleBCMWLANChipBackplane
+ __block_descriptor_tmp.3246
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2253
+ __block_literal_global.2275
+ __block_descriptor_tmp.2255
+ __ZN25AppleBCMWLANChipBackplane25readPMNIAONPBWrapperReg32EjRj
+ __ZN31AppleBCMWLANChipManagerPCIe439932getFWDebugARMCoreRegionTableSizeEv
+ __ZN23AppleBCMWLAN11beAdapter16configureMloPrefEv
+ __ZNK27AppleBCMWLANChipManagerPCIe22isCoexCPUTrapSupportedEv
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439923getDARSecurityStatusRegEP25AppleBCMWLANChipBackplane
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439934getFWDebugPCIEFunc0CoreRegionTableEv
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439932getFWDebugPMUCoreRegionTableSizeEv
+ __block_descriptor_tmp.2251
+ __ZN23AppleBCMWLAN11beAdapter10withDriverEP16AppleBCMWLANCore
+ __ZL42OSClassDescription_AppleBCMWLAN11beAdapter
+ __block_descriptor_tmp.3140
+ __ZN25AppleBCMWLANChipBackplane27readAMNIMainPhyWrapperReg32EjRj
+ __block_descriptor_tmp.3241
+ __ZN23AppleBCMWLAN11beAdapter18handleMloLinkEventEP14wl_event_msg_t
+ __ZN23AppleBCMWLAN11beAdapter24configureMloFeaturesInitEv
+ __ZZN25AppleBCMWLANChipBackplane19dumpMNIIDMRegistersEPcmE10dmpMNIRegs
+ __block_descriptor_tmp.707
+ __ZN15AppleBCMWLANLQM19updateNumOfMloLinksEh
+ __block_descriptor_tmp.530
+ _GLOBAL__sub_I_AppleBCMWLANChipManagerPCIe4399.iig.cpp
+ __ZL20kBCOM4399CoreIDTable
+ __ZN31AppleBCMWLANChipManagerPCIe439915prepareHardwareEP27AppleBCMWLANChipConfigSpaceP25AppleBCMWLANChipBackplane
+ __block_descriptor_tmp.2632
+ __block_descriptor_tmp.580
+ __ZTV31AppleBCMWLANChipManagerPCIe4399
+ __ZN31AppleBCMWLANChipManagerPCIe439915hasMNIInterfaceEv
+ __ZN25AppleBCMWLANChipBackplane17readSRCBCoreReg32EjRj
+ __block_descriptor_tmp.726
+ __block_descriptor_tmp.657
+ _ZN23AppleBCMWLAN11beAdapter15setupJoinConfigEbR10ether_addrb.cold.1
+ _ZN23AppleBCMWLAN11beAdapter13dumpMloStatusEPcjj.cold.1
+ __ZL35AppleBCMWLANChipManagerPCIe4399_NewP11OSMetaClass
+ __block_descriptor_tmp.702
+ __ZN25AppleBCMWLANChipBackplane27readSysmemSlaveWrapperReg32EjRj
- __block_descriptor_tmp.2667
- __block_descriptor_tmp.711
- __block_descriptor_tmp.578
- __block_descriptor_tmp.1087
- __block_descriptor_tmp.1956
- __block_descriptor_tmp.3245
- __block_descriptor_tmp.1088
- __block_descriptor_tmp.381
- __block_descriptor_tmp.699
- __block_descriptor_tmp.3289
- __block_descriptor_tmp.1085
- __block_descriptor_tmp.3242
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2252
- __block_descriptor_tmp.704
- __block_descriptor_tmp.3139
- __block_descriptor_tmp.2631
- __block_descriptor_tmp.935
- __block_descriptor_tmp.840
- __block_descriptor_tmp.685
- __block_descriptor_tmp.680
- __block_descriptor_tmp.831
- __block_descriptor_tmp.1649
- __block_descriptor_tmp.571
- __block_descriptor_tmp.2304
- __block_descriptor_tmp.725
- __block_descriptor_tmp.1078
- __block_descriptor_tmp.3251
- __block_descriptor_tmp.723
- __block_descriptor_tmp.715
- __block_descriptor_tmp.656
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.682
- __block_descriptor_tmp.528
- __block_literal_global.2274
- __block_descriptor_tmp.255
- __block_descriptor_tmp.830
- ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1082
- __block_descriptor_tmp.793
- __block_descriptor_tmp.204
- __block_descriptor_tmp.2254
- __block_descriptor_tmp.329
- __block_descriptor_tmp.3240
- __block_descriptor_tmp.3224
- __block_descriptor_tmp.2272
- __block_descriptor_tmp.379
- __block_literal_global.2306
- __block_descriptor_tmp.2250
CStrings:
+ "PNOScanOffChDur"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read Sysmem DMP ctrl register (0x%!x(MISSING)) , 0x%!x(MISSING) \n"
+ "kBCOMMNIIDMTimeoutValue"
+ "setMultilinkActiveMode"
+ "[dk] %!s(MISSING)@%!d(MISSING):MLO Enabled=<%!d(MISSING)> numberOfLinks<%!d(MISSING)>-><%!d(MISSING)> force=%!d(MISSING)\n"
+ "kBCOMMNIIDMInterruptStatus"
+ "kBCOMMNIIDMResetStatus_ns"
+ "btmc"
+ "PMNI_WLANCB"
+ "dumpMloStatus"
+ "[dk] %!s(MISSING)@%!d(MISSING):[%!d(MISSING):%!d(MISSING)]=link_id=<%!d(MISSING)> link_idx<%!d(MISSING)>  local link adrr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING), peer link adrr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING), peer mld adrr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "PMNI_APB-AAON"
+ "UserScanOffChDur"
+ "configureMlo"
+ "AppleBCMWLAN11beAdapter driver is null\n"
+ "[dk] %!s(MISSING)@%!d(MISSING): User Roam Cache (%!d(MISSING)) BSSID %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING), MLD:%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING), RSSI %!d(MISSING) chanspec %!d(MISSING) age %!d(MISSING) load %!d(MISSING)\n"
+ "MainD11Mac"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper resetctl: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper kBCOMWrapperRegSILDBG: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING): mloFeaturesConfig_t mask:0x%!x(MISSING) enab:0x%!x(MISSING)  --> %!d(MISSING)[%!s(MISSING)], low-latency = %!s(MISSING) \n"
+ "GCI"
+ "/AppleInternal/Library/BuildRoots/f82e4213-595f-11ef-b136-76625042721f/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "checkPMNIAPB"
+ "[dk] %!s(MISSING)@%!d(MISSING):len=<%!d(MISSING)> mode<%!d(MISSING)>  num_links=<%!d(MISSING)>   local mld_addr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper resetctl: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper kBCOMWrapperRegIntMaskNs: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):v=<%!d(MISSING)> len=<%!d(MISSING)> opcode<%!d(MISSING)> role=<%!d(MISSING)> num_links=<%!d(MISSING)>  pref_band_link_idx=<%!d(MISSING)> mld_addr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "AMNI_AuxMAC"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper kBCOMWrapperRegIntMaskNs: 0x%!x(MISSING)\n"
+ "attachCoexSoCRAMFile"
+ "mlo numberOfLinks is %!d(MISSING)  local mld addr= %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING) peer mld add %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING) \n"
+ "getMloPerLinkStats"
+ "coex_SoC_RAM.bin"
+ "[dk] %!s(MISSING)@%!d(MISSING):Bail out Coex SoCRAM dump: TCM Not accessible.\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper errorlogstatus: 0x%!x(MISSING)\n"
+ "isMloConnection"
+ "ScanD11Mac"
+ "kBCOMMNIIDMErrAddrMSB"
+ "kBCOMMNIIDMErrAddrMSB_ns"
+ "[dk] %!s(MISSING)@%!d(MISSING):link id =<%!d(MISSING)> %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI AON APB wrapper IDB Device ID: 0x%!x(MISSING)\n"
+ "kBCOMOOBCoreDMPControl"
+ "mlo numberOfLinks is 0 \n"
+ "[dk] %!s(MISSING)@%!d(MISSING): Unable to create 11be Adapter object!\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper kBCOMWrapperRegIDMDeviceID: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper kBCOMWrapperRegIntMaskNs: 0x%!x(MISSING)\n"
+ "Set 42 eMLSR"
+ "Core Register Regions with MNI interface"
+ "AppleBCMWLAN11beAdapter Failed to init fLogger\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read Sysmem slave wrapper reset ctrl register (0x%!x(MISSING)) , 0x%!x(MISSING) \n"
+ "kBCOMOOBCoreDMPStatus"
+ "kBCOMMNIIDMErrMisc0_ns"
+ "updateMloLinkChangeInfo"
+ "[dk] %!s(MISSING)@%!d(MISSING): mloConfigPref_t %!d(MISSING)[%!s(MISSING)]\n"
+ "kBCOMMNIIDMInterurptStatus_ns"
+ "cant create a random mac address after 100 tries"
+ "[dk] %!s(MISSING)@%!d(MISSING): wlan.pcie.disableCoexCPUDumpSupport %!d(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):ampdu_stats_type_int larger than max known WL_AMPDU_STATS_TYPE_MLO_LINK_INFO\n"
+ "kBCOMMNIIDMAccessWriteID"
+ "AuxD11Mac"
+ "kBCOMMNIIDMErrMisc0"
+ "LHL"
+ "HMNI_BT"
+ "AMNI_CCI"
+ "OtherScanOffChDur"
+ "HMNI_GCI"
+ "PMNI_APB-CB"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI CB APB wrapper IDB Device ID: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper errorlogstatus: 0x%!x(MISSING)\n"
+ "readcoexSoCRAM"
+ "kBCOMMNIIDMErrStatus_ns"
+ "%!s(MISSING)[%!x(MISSING)]%!s(MISSING): 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Coex SoCRAM ivars->fCoexCPUTrapped  %!d(MISSING)  ivars->fCoexCPUTrapRequested %!d(MISSING)\n"
+ "RoamScanOffChDur"
+ "AppleBCMWLAN11beAdapter super init failied\n"
+ "kBCOMMNIIDMConfig"
+ "kBCOMMNIIDMErrCtrl"
+ "OOB config and status"
+ "[dk] %!s(MISSING)@%!d(MISSING): (%!d(MISSING)) BSSID %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING), MLD:%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING) RSSI %!d(MISSING) chanspec %!d(MISSING) age %!d(MISSING) load %!d(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI WL APB wrapper Interrupt Mask: 0x%!x(MISSING)\n"
+ "AMNI_CHIPCOMMON"
+ "[dk] %!s(MISSING)@%!d(MISSING): multilink_active mode %!d(MISSING)[%!s(MISSING)] set<%!d(MISSING)> \n"
+ "coex_socRam"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI WL APB wrapper IDB Device ID: 0x%!x(MISSING)\n"
+ "AssocScanOffChDur"
+ "[dk] %!s(MISSING)@%!d(MISSING): mloFeaturesConfig_t mask:0x%!x(MISSING) enab:0x%!x(MISSING)  --> %!d(MISSING)[%!s(MISSING)] \n"
+ "AMNI_AuxPHY"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI WL APB errorlogstatus wrapper reg non-zero: data1: 0x%!x(MISSING) data2: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper kBCOMWrapperRegIDMDeviceID: 0x%!x(MISSING)\n"
+ "btsc"
+ "[dk] %!s(MISSING)@%!d(MISSING):i =<%!d(MISSING)> if_idx=<%!d(MISSING)> cfg_idx=<%!d(MISSING)> link_id<%!d(MISSING)> link_idx=<%!d(MISSING)> chanspec=<%!x(MISSING)> link_addr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "kBCOMMNIIDMAccessReadID"
+ "kBCOMMNIIDMResetWriteID_ns"
+ "kBCOMMNIIDMErrMisc1"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI WL APB resetctl wrapper reg non-zero: 0x%!x(MISSING)\n"
+ "mlo"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper kBCOMWrapperRegSILDBG: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI CB APB wrapper SILDBG: 0x%!x(MISSING)\n"
+ "Failed to allocate AppleBCMWLAN11beAdapter_IVars\n"
+ "AMNI_MainPHY"
+ "[dk] %!s(MISSING)@%!d(MISSING):Dump the PMNI Wrapper registers for debug \n"
+ "kBCOMMNIIDMResetControl"
+ "configureMloFeaturesInit"
+ "Aug 13 2024 20:23:59"
+ "configureMloPref"
+ "AMNI_ScanPHY"
+ "[dk] %!s(MISSING)@%!d(MISSING): getMloStatus %!d(MISSING)[%!s(MISSING)] \n"
+ "kBCOMMNIIDMErrMisc1_ns"
+ "kBCOMMNIIDMAccessStatus"
+ "configureMloFeatures"
+ "Saqm"
+ "kBCOMMNIIDMDeivceID"
+ "ArmCA7"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper kBCOMWrapperRegIDMDeviceID: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):TCM memory is accessible. reset ctrl:0x%!x(MISSING) 0x%!x(MISSING) DMP ctrl:0x%!x(MISSING) 0x%!x(MISSING)\n"
+ "Sysmem"
+ "kBCOMMNIIDMInterruptMask_ns"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI CB APB errorlogstatus wrapper reg non-zero: data1: 0x%!x(MISSING) data2: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper kBCOMWrapperRegSILDBG: 0x%!x(MISSING)\n"
+ "kBCOMMNIIDMAccessControl"
+ "mlo_status"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI CB APB wrapper Interrupt Mask: 0x%!x(MISSING)\n"
+ "i=%!d(MISSING)  channel=%!d(MISSING) band = %!d(MISSING), local link addr= %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING) peer link addr %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING) \n"
+ "setupJoinConfig"
+ "kBCOMMNIIDMAccessWriteID_ns"
+ "[dk] %!s(MISSING)@%!d(MISSING): getMloStatus %!d(MISSING) [%!s(MISSING)] \n"
+ "kBCOMMNIIDMAccessReadID_ns"
+ "kBCOMMNIIDMErrAddrLSB_ns"
+ "AMNI_PCIeF0"
+ "Set 41 Rate Selection"
+ "BCMWLAN Chip Coex Trap"
+ "kBCOMOOBCoreClockPwrReq"
+ "AMNI_MainMAC"
+ "kBCOMMNIIDMAccessStatus_ns"
+ "ChipC"
+ "wlan.pcie.disableCoexCPUDumpSupport"
+ "PCIE"
+ "[dk] %!s(MISSING)@%!d(MISSING):Coex CPU trap Indicated\n"
+ "AMNI_ScanMAC"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI AON APB errorlogstatus wrapper reg non-zero: data1: 0x%!x(MISSING) data2: 0x%!x(MISSING)\n"
+ "AppleBCMWLAN11beAdapter commander is null\n"
+ "kBCOMMNIIDMResetWriteiID"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI WL APB wrapper SILDBG: 0x%!x(MISSING)\n"
+ "kBCOMMNIIDMResetStatus"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper errorlogstatus: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Bail out Coex SoCRAM dump: No Memory\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI AON APB resetctl wrapper reg non-zero: 0x%!x(MISSING)\n"
+ "getMloStatus"
+ "kBCOMMNISILDBG"
+ "kBCOMMNIIDMErrAddrLSB"
+ "[dk] %!s(MISSING)@%!d(MISSING):TCM memory is not accessible. reset ctrl:0x%!x(MISSING) 0x%!x(MISSING) DMP ctrl:0x%!x(MISSING) 0x%!x(MISSING)\n"
+ "dumpPMNIRegisters"
+ "kBCOMMNIIDMInterurptMask"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI AON APB wrapper Interrupt Mask: 0x%!x(MISSING)\n"
+ "kBCOMMNIIDMErrStatus"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI CB APB resetctl wrapper reg non-zero: 0x%!x(MISSING)\n"
+ "SRCB"
+ "kBCOMMNIIDMResetReadID_ns"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper resetctl: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):configureMlo %!d(MISSING)[%!s(MISSING)] numberOfLinks=<%!d(MISSING)> %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI AON APB wrapper SILDBG: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read ARM CA7 DMP ctrl register (0x%!x(MISSING)) , 0x%!x(MISSING) \n"
+ "kBCOMMNIIDMTimeoutControl"
+ "[dk] %!s(MISSING)@%!d(MISSING):Coex CPU trap Requested\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):MLO Stats [%!s(MISSING) Preferred:%!u(MISSING)] chan: %!u(MISSING) / %!s(MISSING) rssi: [%!d(MISSING), %!d(MISSING)] tx_pkts: %!d(MISSING) rx_pkts: %!d(MISSING) tx_rate: %!d(MISSING) rx_rate: %!d(MISSING) tx_fail: %!d(MISSING) ex_retry: %!d(MISSING) idle: %!d(MISSING) ovflo: %!s(MISSING)\n"
+ "kBCOMOOBCoreExtRsrcReq"
+ "kBCOMMNIIDMResetReadID"
+ "/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLAN11beAdapter.cpp"
+ "Set 40 MLO Link Info"
- "Aug 13 2024 21:09:58"
- "[dk] %!s(MISSING)@%!d(MISSING):ampdu_stats_type_int larger than max known WL_AMPDU_STATS_TYPE_TXHEx4\n"
- "/AppleInternal/Library/BuildRoots/e9a73e96-5963-11ef-a918-8ece77934383/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"

```
