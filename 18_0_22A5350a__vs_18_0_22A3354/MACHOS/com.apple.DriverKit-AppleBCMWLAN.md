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
+ __ZL29kBCOM4399FWDebugARMCoreRanges
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439928getFWDebugARMCoreRegionTableEv
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439931getFWDebugCommonCoreRegionTableEv
+ __ZN25AppleBCMWLANChipBackplane30readAMNIChipCommonWrapperReg32EjRj
+ __ZTV31AppleBCMWLANChipManagerPCIe4399
+ __block_descriptor_tmp.1131
+ __ZNK28AppleBCMWLANBusInterfacePCIe17dumpPMNIRegistersEv
+ __block_literal_global.2307
+ __ZN31AppleBCMWLANChipManagerPCIe439928getFWDebugPMUCoreRegionTableEv
+ __ZZN20AppleBCMWLANChanSpec19getAppleChannelSpecEtE21chanIdToCenterlMap320
+ __block_descriptor_tmp.206
+ __block_descriptor_tmp.794
+ __ZN31AppleBCMWLANChipManagerPCIe439931getFWDebugCommonCoreRegionTableEv
+ _gAppleBCMWLANChipManagerPCIe4399_Declaration
+ __ZN31AppleBCMWLANChipManagerPCIe439923getDARSecurityStatusRegEP25AppleBCMWLANChipBackplane
+ __ZNK22AppleBCMWLANChipMemory11readCoexRAMEjjP13IO80211Bufferj
+ __ZTV40AppleBCMWLANChipManagerPCIe4399MetaClass
+ __block_descriptor_tmp.1957
+ __ZN31AppleBCMWLANChipManagerPCIe439938getFWDebugPCIEFunc0CoreRegionTableSizeEv
+ __ZN25AppleBCMWLANChipBackplane23readHMNIGCIWrapperReg32EjRj
+ __ZN31AppleBCMWLANChipManagerPCIe439932getFWDebugPMUCoreRegionTableSizeEv
+ __block_descriptor_tmp.3241
+ _gAppleBCMWLAN11beAdapterMetaClass
+ __ZNK16AppleBCMWLANCore14get11beAdapterEv
+ __ZL50OSClassDescription_AppleBCMWLANChipManagerPCIe4399
+ __ZN23AppleBCMWLAN11beAdapter15setupInitConfigEv
+ __block_descriptor_tmp.383
+ __ZN25AppleBCMWLANChipBackplane25readPMNIAONPBWrapperReg32EjRj
+ __ZN25AppleBCMWLANChipBackplane22readHMNIBTWrapperReg32EjRj
+ __block_descriptor_tmp.718
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2253
+ _ZN23AppleBCMWLAN11beAdapter12getMloStatusEv.cold.1
+ __block_descriptor_tmp.331
+ __block_descriptor_tmp.845
+ __ZL27AppleBCMWLAN11beAdapter_NewP11OSMetaClass
+ __ZN25AppleBCMWLANChipBackplane26readAMNIAuxPhyWrapperReg32EjRj
+ __block_descriptor_tmp.2668
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439938getFWDebugPCIEFunc0CoreRegionTableSizeEv
+ _ZN23AppleBCMWLAN11beAdapter15isMloConnectionEv.cold.1
+ __ZL21kBCOM4399ChipMemories
+ __block_descriptor_tmp.3140
+ __ZN31AppleBCMWLANChipManagerPCIe439912initWithChipEjh
+ __ZTV32AppleBCMWLAN11beAdapterMetaClass
+ _ZN23AppleBCMWLAN11beAdapter13dumpMloStatusEPcjj.cold.1
+ __ZThn64_N28AppleBCMWLANBusInterfacePCIe14readcoexSoCRAMEjP6OSDataPyj
+ __block_descriptor_tmp.385
+ __ZN15AppleBCMWLANLQM18getMloPerLinkStatsEh
+ __ZL29kBCOM4399FWDebugPMUCoreRanges
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439915prepareHardwareEP27AppleBCMWLANChipConfigSpaceP25AppleBCMWLANChipBackplane
+ __block_descriptor_tmp.657
+ __block_literal_global.2275
+ _ZN23AppleBCMWLAN11beAdapter12configureMloEtR12mloAddrArray.cold.1
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439915hasMNIInterfaceEv
+ __block_descriptor_tmp.936
+ __block_descriptor_tmp.2305
+ ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1128
+ __block_descriptor_tmp.726
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439934getFWDebugPCIEFunc0CoreRegionTableEv
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439932getFWDebugARMCoreRegionTableSizeEv
+ __ZL16kBCOM4399ChipOTP
+ __ZL42OSClassDescription_AppleBCMWLAN11beAdapter
+ __ZZN25AppleBCMWLANChipBackplane19dumpMNIIDMRegistersEPcmE10dmpMNIRegs
+ __ZN19AppleBCMWLANCoreDbg12cmdMloStatusEP24apple80211_debug_commandP16AppleBCMWLANCore
+ _AppleBCMWLANChipManagerPCIe4399_Class
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439932getFWDebugPMUCoreRegionTableSizeEv
+ __ZN31AppleBCMWLANChipManagerPCIe439928getFWDebugARMCoreRegionTableEv
+ __ZL20kBCOM4399ChipUserOTP
+ __ZN23AppleBCMWLAN11beAdapter15setupJoinConfigEbR10ether_addrb
+ __ZN31AppleBCMWLANChipManagerPCIe439915prepareHardwareEP27AppleBCMWLANChipConfigSpaceP25AppleBCMWLANChipBackplane
+ _ZN15AppleBCMWLANLQM18getMloPerLinkStatsEh.cold.1
+ __block_descriptor_tmp.702
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439935getFWDebugCommonCoreRegionTableSizeEv
+ __block_descriptor_tmp.580
+ __ZL32kBCOM4399FWDebugCommonCoreRanges
+ __ZN15AppleBCMWLANLQM27updateMloTrafficSwitchStateEh
+ __ZN23AppleBCMWLAN11beAdapter12getMloStatusEv
+ __block_descriptor_tmp.257
+ __ZThn24_N23AppleBCMWLAN11beAdapter4freeEv
+ __ZN25AppleBCMWLANChipBackplane19dumpMNIIDMRegistersEPcm
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439912initWithChipEjh
+ __ZN15AppleBCMWLANLQM19updateNumOfMloLinksEh
+ _ZN23AppleBCMWLAN11beAdapter15setupJoinConfigEbR10ether_addrb.cold.1
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439913checkHardwareEP27AppleBCMWLANChipConfigSpaceP25AppleBCMWLANChipBackplane
+ __ZNK28AppleBCMWLANBusInterfacePCIe12checkPMNIAPBEv
+ _GLOBAL__sub_I_AppleBCMWLANChipManagerPCIe4399.iig.cpp
+ _GLOBAL__sub_I_AppleBCMWLAN11beAdapter.cpp
+ __ZL20kBCOM4399CoreIDTable
+ __ZL34kBCOM4399ChipConfigSpaceStateTable
+ __ZTV23AppleBCMWLAN11beAdapter
+ __ZN28AppleBCMWLANBusInterfacePCIe14readcoexSoCRAMEjP6OSDataPyj
+ __ZN25AppleBCMWLANChipBackplane27readAMNIScanMacWrapperReg32EjRj
+ _GLOBAL__sub_I_AppleBCMWLANChipManagerPCIe4399.cpp
+ _gAppleBCMWLANChipManagerPCIe4399MetaClass
+ __block_descriptor_tmp.836
+ __block_descriptor_tmp.2273
+ __ZN31AppleBCMWLANChipManagerPCIe439915hasMNIInterfaceEv
+ __block_descriptor_tmp.573
+ __ZN31AppleBCMWLANChipManagerPCIe439921isSecureBootSupportedEv
+ __ZN25AppleBCMWLANChipBackplane27readAMNIMainPhyWrapperReg32EjRj
+ __ZN23AppleBCMWLAN11beAdapter24configureMloFeaturesInitEv
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439928getFWDebugPMUCoreRegionTableEv
+ __ZL29kBCOM4399ChipBackplaneWindows
+ __ZNK27AppleBCMWLANChipManagerPCIe22isCoexCPUTrapSupportedEv
+ __ZN23AppleBCMWLAN11beAdapter20configureMloFeaturesEb
+ __ZN25AppleBCMWLANChipBackplane17readSRCBCoreReg32EjRj
+ __ZL35kBCOM4399FWDebugPCIEFunc0CoreRanges
+ _gAppleBCMWLAN11beAdapter_Declaration
+ __ZN31AppleBCMWLANChipManagerPCIe439913checkHardwareEP27AppleBCMWLANChipConfigSpaceP25AppleBCMWLANChipBackplane
+ __ZN28AppleBCMWLANBusInterfacePCIe20attachCoexSoCRAMFileEP13CCFaultReport
+ __block_descriptor_tmp.3252
+ __block_descriptor_tmp.707
+ __ZN23AppleBCMWLAN11beAdapter13dumpMloStatusEPcjj
+ __ZZN25AppleBCMWLANChipBackplane28dumpOOBConfigStatusRegistersEPcmE11oobCoreRegs
+ __ZN25AppleBCMWLANChipBackplane25readPMNICBAPBWrapperReg32EjRj
+ __block_descriptor_tmp.835
+ __block_descriptor_tmp.3243
+ __ZN23AppleBCMWLAN11beAdapter14initWithDriverEP16AppleBCMWLANCore
+ __ZL18kBCOM4399ChipCores
+ __ZN31AppleBCMWLANChipManagerPCIe439932getFWDebugARMCoreRegionTableSizeEv
+ __ZN23AppleBCMWLAN11beAdapter22setMultilinkActiveModeEj
+ __block_descriptor_tmp.2632
+ __ZN15AppleBCMWLANLQM23updateMloLinkChangeInfoEP25wl_mlo_link_info_event_v1
+ __ZN23AppleBCMWLAN11beAdapter15isMloConnectionEv
+ __ZN31AppleBCMWLANChipManagerPCIe43998withChipEjh
+ __ZN25AppleBCMWLANChipBackplane27readAMNIScanPhyWrapperReg32EjRj
+ __ZN25AppleBCMWLANChipBackplane26writeOOBRouterWrapperReg32Ejj
+ __block_descriptor_tmp.2255
+ __ZN27AppleBCMWLANChipManagerPCIe23setCoexCPUTrapSupportedEb
+ __block_descriptor_tmp.1124
+ __block_descriptor_tmp.1133
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439921isSecureBootSupportedEv
+ __block_descriptor_tmp.530
+ __ZL27kBCOM4399UCodeSHMRegionInfo
+ __ZN25AppleBCMWLANChipBackplane27readSysmemSlaveWrapperReg32EjRj
+ __ZN23AppleBCMWLAN11beAdapter16configureMloPrefEv
+ __ZN15AppleBCMWLANLQM15getMloPerfStatsEv
+ __block_descriptor_tmp.3246
+ __ZN23AppleBCMWLAN11beAdapter10withDriverEP16AppleBCMWLANCore
+ __ZN31AppleBCMWLANChipManagerPCIe439934getFWDebugPCIEFunc0CoreRegionTableEv
+ __block_descriptor_tmp.688
+ __ZN23AppleBCMWLAN11beAdapter12configureMloEtR12mloAddrArray
+ __block_descriptor_tmp.683
+ __block_descriptor_tmp.2251
+ __block_descriptor_tmp.3290
+ __ZN31AppleBCMWLANChipManagerPCIe439935getFWDebugCommonCoreRegionTableSizeEv
+ __ZL27kBCOM4399UCodeSCRRegionInfo
+ __ZN25AppleBCMWLANChipBackplane28dumpOOBConfigStatusRegistersEPcm
+ __block_descriptor_tmp.728
+ __block_descriptor_tmp.717
+ __ZL33fileValidation4399ImagesSHA_array
+ __ZN15AppleBCMWLANLQM16storeMloLinkInfoEhtRK10ether_addr
+ __ZN25AppleBCMWLANChipBackplane25readPMNIWLAPBWrapperReg32EjRj
+ __ZN32AppleBCMWLAN11beAdapterMetaClass3NewEP8OSObject
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.685
+ __ZL35AppleBCMWLANChipManagerPCIe4399_NewP11OSMetaClass
+ __ZL21kBCOM4399ChipWrappers
+ __ZN23AppleBCMWLAN11beAdapter4freeEv
+ __ZN23AppleBCMWLAN11beAdapter18handleMloLinkEventEP14wl_event_msg_t
+ __ZN40AppleBCMWLANChipManagerPCIe4399MetaClass3NewEP8OSObject
+ _AppleBCMWLAN11beAdapter_Class
+ __block_descriptor_tmp.1134
+ __ZN25AppleBCMWLANChipBackplane39dumpCoreRegisterRegionswithMNIInterfaceEPcm
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439923getDARSecurityStatusRegEP25AppleBCMWLANChipBackplane
+ __block_descriptor_tmp.1650
+ __block_descriptor_tmp.3225
+ __ZN27AppleBCMWLANChipManagerPCIe32setFatalErrorIndicationSupportedEb
- __block_descriptor_tmp.680
- __block_descriptor_tmp.571
- __block_descriptor_tmp.1085
- __block_descriptor_tmp.656
- __block_descriptor_tmp.2667
- __block_descriptor_tmp.1078
- __block_descriptor_tmp.1087
- __block_descriptor_tmp.3242
- __block_descriptor_tmp.381
- __block_descriptor_tmp.831
- __block_descriptor_tmp.1088
- __block_descriptor_tmp.379
- __block_descriptor_tmp.1649
- __block_descriptor_tmp.830
- __block_descriptor_tmp.704
- __block_descriptor_tmp.2631
- __block_descriptor_tmp.255
- __block_descriptor_tmp.2250
- __block_descriptor_tmp.3251
- __block_descriptor_tmp.3240
- __block_descriptor_tmp.699
- __block_literal_global.2306
- __block_descriptor_tmp.3289
- __block_descriptor_tmp.725
- __block_descriptor_tmp.711
- __block_literal_global.2274
- __block_descriptor_tmp.685
- __block_descriptor_tmp.3245
- __block_descriptor_tmp.3224
- __block_descriptor_tmp.3139
- __block_descriptor_tmp.793
- __block_descriptor_tmp.840
- __block_descriptor_tmp.2304
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2252
- __block_descriptor_tmp.204
- __block_descriptor_tmp.935
- __block_descriptor_tmp.723
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.682
- __block_descriptor_tmp.715
- __block_descriptor_tmp.578
- ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1082
- __block_descriptor_tmp.528
- __block_descriptor_tmp.2254
- __block_descriptor_tmp.2272
- __block_descriptor_tmp.329
- __block_descriptor_tmp.1956
CStrings:
+ "kBCOMMNIIDMErrAddrMSB"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper kBCOMWrapperRegIDMDeviceID: 0x%!x(MISSING)\n"
+ "mlo_status"
+ "coex_SoC_RAM.bin"
+ "kBCOMOOBCoreExtRsrcReq"
+ "dumpMloStatus"
+ "mlo numberOfLinks is %!d(MISSING)  local mld addr= %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING) peer mld add %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING) \n"
+ "isMloConnection"
+ "%!s(MISSING)[%!x(MISSING)]%!s(MISSING): 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI AON APB errorlogstatus wrapper reg non-zero: data1: 0x%!x(MISSING) data2: 0x%!x(MISSING)\n"
+ "kBCOMMNIIDMResetWriteID_ns"
+ "getMloPerLinkStats"
+ "LHL"
+ "[dk] %!s(MISSING)@%!d(MISSING):len=<%!d(MISSING)> mode<%!d(MISSING)>  num_links=<%!d(MISSING)>   local mld_addr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "AMNI_ScanMAC"
+ "kBCOMMNISILDBG"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read Sysmem DMP ctrl register (0x%!x(MISSING)) , 0x%!x(MISSING) \n"
+ "AMNI_AuxPHY"
+ "kBCOMMNIIDMResetReadID_ns"
+ "btmc"
+ "setupJoinConfig"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper kBCOMWrapperRegIDMDeviceID: 0x%!x(MISSING)\n"
+ "kBCOMMNIIDMDeivceID"
+ "kBCOMMNIIDMErrAddrLSB_ns"
+ "kBCOMMNIIDMAccessReadID_ns"
+ "kBCOMMNIIDMAccessWriteID_ns"
+ "GCI"
+ "[dk] %!s(MISSING)@%!d(MISSING):v=<%!d(MISSING)> len=<%!d(MISSING)> opcode<%!d(MISSING)> role=<%!d(MISSING)> num_links=<%!d(MISSING)>  pref_band_link_idx=<%!d(MISSING)> mld_addr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "HMNI_GCI"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper errorlogstatus: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI WL APB wrapper IDB Device ID: 0x%!x(MISSING)\n"
+ "Set 41 Rate Selection"
+ "AMNI_CHIPCOMMON"
+ "RoamScanOffChDur"
+ "[dk] %!s(MISSING)@%!d(MISSING): mloFeaturesConfig_t mask:0x%!x(MISSING) enab:0x%!x(MISSING)  --> %!d(MISSING)[%!s(MISSING)] \n"
+ "[dk] %!s(MISSING)@%!d(MISSING): multilink_active mode %!d(MISSING)[%!s(MISSING)] set<%!d(MISSING)> \n"
+ "getMloStatus"
+ "[dk] %!s(MISSING)@%!d(MISSING): (%!d(MISSING)) BSSID %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING), MLD:%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING) RSSI %!d(MISSING) chanspec %!d(MISSING) age %!d(MISSING) load %!d(MISSING)\n"
+ "readcoexSoCRAM"
+ "[dk] %!s(MISSING)@%!d(MISSING):Coex SoCRAM ivars->fCoexCPUTrapped  %!d(MISSING)  ivars->fCoexCPUTrapRequested %!d(MISSING)\n"
+ "SRCB"
+ "configureMlo"
+ "mlo"
+ "wlan.pcie.disableCoexCPUDumpSupport"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper resetctl: 0x%!x(MISSING)\n"
+ "setMultilinkActiveMode"
+ "PMNI_APB-CB"
+ "kBCOMMNIIDMResetStatus"
+ "kBCOMMNIIDMTimeoutControl"
+ "Core Register Regions with MNI interface"
+ "Set 40 MLO Link Info"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper resetctl: 0x%!x(MISSING)\n"
+ "kBCOMMNIIDMConfig"
+ "kBCOMMNIIDMErrAddrMSB_ns"
+ "kBCOMMNIIDMAccessWriteID"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI AON APB wrapper SILDBG: 0x%!x(MISSING)\n"
+ "AMNI_PCIeF0"
+ "ScanD11Mac"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI WL APB resetctl wrapper reg non-zero: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper kBCOMWrapperRegSILDBG: 0x%!x(MISSING)\n"
+ "MainD11Mac"
+ "[dk] %!s(MISSING)@%!d(MISSING):Bail out Coex SoCRAM dump: No Memory\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Dump the PMNI Wrapper registers for debug \n"
+ "[dk] %!s(MISSING)@%!d(MISSING):MLO Enabled=<%!d(MISSING)> numberOfLinks<%!d(MISSING)>-><%!d(MISSING)> force=%!d(MISSING)\n"
+ "coex_socRam"
+ "kBCOMMNIIDMInterruptMask_ns"
+ "AMNI_AuxMAC"
+ "PMNI_APB-AAON"
+ "[dk] %!s(MISSING)@%!d(MISSING): mloConfigPref_t %!d(MISSING)[%!s(MISSING)]\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper resetctl: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):configureMlo %!d(MISSING)[%!s(MISSING)] numberOfLinks=<%!d(MISSING)> %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper errorlogstatus: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper kBCOMWrapperRegIntMaskNs: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Coex CPU trap Requested\n"
+ "kBCOMMNIIDMInterurptMask"
+ "UserScanOffChDur"
+ "kBCOMOOBCoreDMPStatus"
+ "kBCOMOOBCoreDMPControl"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read ARM CA7 DMP ctrl register (0x%!x(MISSING)) , 0x%!x(MISSING) \n"
+ "/AppleInternal/Library/BuildRoots/f82e4213-595f-11ef-b136-76625042721f/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "kBCOMMNIIDMInterruptStatus"
+ "[dk] %!s(MISSING)@%!d(MISSING):i =<%!d(MISSING)> if_idx=<%!d(MISSING)> cfg_idx=<%!d(MISSING)> link_id<%!d(MISSING)> link_idx=<%!d(MISSING)> chanspec=<%!x(MISSING)> link_addr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "configureMloFeaturesInit"
+ "[dk] %!s(MISSING)@%!d(MISSING):Coex CPU trap Indicated\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI AON APB wrapper IDB Device ID: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI WL APB wrapper SILDBG: 0x%!x(MISSING)\n"
+ "mlo numberOfLinks is 0 \n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI CB APB wrapper SILDBG: 0x%!x(MISSING)\n"
+ "kBCOMMNIIDMAccessControl"
+ "Saqm"
+ "AppleBCMWLAN11beAdapter super init failied\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):link id =<%!d(MISSING)> %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "AMNI_ScanPHY"
+ "[dk] %!s(MISSING)@%!d(MISSING):ampdu_stats_type_int larger than max known WL_AMPDU_STATS_TYPE_MLO_LINK_INFO\n"
+ "kBCOMMNIIDMResetStatus_ns"
+ "configureMloPref"
+ "OtherScanOffChDur"
+ "kBCOMMNIIDMErrMisc1_ns"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI WL APB wrapper Interrupt Mask: 0x%!x(MISSING)\n"
+ "AssocScanOffChDur"
+ "AppleBCMWLAN11beAdapter driver is null\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper kBCOMWrapperRegIDMDeviceID: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):MLO Stats [%!s(MISSING) Preferred:%!u(MISSING)] chan: %!u(MISSING) / %!s(MISSING) rssi: [%!d(MISSING), %!d(MISSING)] tx_pkts: %!d(MISSING) rx_pkts: %!d(MISSING) tx_rate: %!d(MISSING) rx_rate: %!d(MISSING) tx_fail: %!d(MISSING) ex_retry: %!d(MISSING) idle: %!d(MISSING) ovflo: %!s(MISSING)\n"
+ "kBCOMMNIIDMTimeoutValue"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read Sysmem slave wrapper reset ctrl register (0x%!x(MISSING)) , 0x%!x(MISSING) \n"
+ "btsc"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI WL APB errorlogstatus wrapper reg non-zero: data1: 0x%!x(MISSING) data2: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING): Unable to create 11be Adapter object!\n"
+ "[dk] %!s(MISSING)@%!d(MISSING): mloFeaturesConfig_t mask:0x%!x(MISSING) enab:0x%!x(MISSING)  --> %!d(MISSING)[%!s(MISSING)], low-latency = %!s(MISSING) \n"
+ "Failed to allocate AppleBCMWLAN11beAdapter_IVars\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper kBCOMWrapperRegSILDBG: 0x%!x(MISSING)\n"
+ "PMNI_WLANCB"
+ "Sysmem"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI CB APB resetctl wrapper reg non-zero: 0x%!x(MISSING)\n"
+ "AMNI_MainPHY"
+ "kBCOMMNIIDMResetControl"
+ "kBCOMMNIIDMErrMisc0"
+ "kBCOMMNIIDMErrStatus_ns"
+ "/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLAN11beAdapter.cpp"
+ "[dk] %!s(MISSING)@%!d(MISSING):Bail out Coex SoCRAM dump: TCM Not accessible.\n"
+ "kBCOMOOBCoreClockPwrReq"
+ "Aug 13 2024 20:23:59"
+ "AppleBCMWLAN11beAdapter commander is null\n"
+ "attachCoexSoCRAMFile"
+ "kBCOMMNIIDMErrAddrLSB"
+ "[dk] %!s(MISSING)@%!d(MISSING): User Roam Cache (%!d(MISSING)) BSSID %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING), MLD:%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING), RSSI %!d(MISSING) chanspec %!d(MISSING) age %!d(MISSING) load %!d(MISSING)\n"
+ "cant create a random mac address after 100 tries"
+ "PCIE"
+ "[dk] %!s(MISSING)@%!d(MISSING):TCM memory is accessible. reset ctrl:0x%!x(MISSING) 0x%!x(MISSING) DMP ctrl:0x%!x(MISSING) 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI CB APB wrapper Interrupt Mask: 0x%!x(MISSING)\n"
+ "AMNI_CCI"
+ "kBCOMMNIIDMResetWriteiID"
+ "kBCOMMNIIDMErrStatus"
+ "kBCOMMNIIDMResetReadID"
+ "dumpPMNIRegisters"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper kBCOMWrapperRegIntMaskNs: 0x%!x(MISSING)\n"
+ "ChipC"
+ "AppleBCMWLAN11beAdapter Failed to init fLogger\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):[%!d(MISSING):%!d(MISSING)]=link_id=<%!d(MISSING)> link_idx<%!d(MISSING)>  local link adrr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING), peer link adrr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING), peer mld adrr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "kBCOMMNIIDMErrMisc0_ns"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper kBCOMWrapperRegIntMaskNs: 0x%!x(MISSING)\n"
+ "HMNI_BT"
+ "Set 42 eMLSR"
+ "[dk] %!s(MISSING)@%!d(MISSING): wlan.pcie.disableCoexCPUDumpSupport %!d(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper kBCOMWrapperRegSILDBG: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING): getMloStatus %!d(MISSING)[%!s(MISSING)] \n"
+ "kBCOMMNIIDMAccessStatus_ns"
+ "ArmCA7"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper errorlogstatus: 0x%!x(MISSING)\n"
+ "kBCOMMNIIDMAccessReadID"
+ "kBCOMMNIIDMErrMisc1"
+ "AMNI_MainMAC"
+ "OOB config and status"
+ "BCMWLAN Chip Coex Trap"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI AON APB resetctl wrapper reg non-zero: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):TCM memory is not accessible. reset ctrl:0x%!x(MISSING) 0x%!x(MISSING) DMP ctrl:0x%!x(MISSING) 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI CB APB wrapper IDB Device ID: 0x%!x(MISSING)\n"
+ "kBCOMMNIIDMInterurptStatus_ns"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI AON APB wrapper Interrupt Mask: 0x%!x(MISSING)\n"
+ "updateMloLinkChangeInfo"
+ "configureMloFeatures"
+ "AuxD11Mac"
+ "kBCOMMNIIDMErrCtrl"
+ "[dk] %!s(MISSING)@%!d(MISSING): getMloStatus %!d(MISSING) [%!s(MISSING)] \n"
+ "PNOScanOffChDur"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI CB APB errorlogstatus wrapper reg non-zero: data1: 0x%!x(MISSING) data2: 0x%!x(MISSING)\n"
+ "checkPMNIAPB"
+ "i=%!d(MISSING)  channel=%!d(MISSING) band = %!d(MISSING), local link addr= %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING) peer link addr %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING) \n"
+ "kBCOMMNIIDMAccessStatus"
- "[dk] %!s(MISSING)@%!d(MISSING):ampdu_stats_type_int larger than max known WL_AMPDU_STATS_TYPE_TXHEx4\n"
- "/AppleInternal/Library/BuildRoots/e9a73e96-5963-11ef-a918-8ece77934383/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "Aug 13 2024 21:09:58"

```
