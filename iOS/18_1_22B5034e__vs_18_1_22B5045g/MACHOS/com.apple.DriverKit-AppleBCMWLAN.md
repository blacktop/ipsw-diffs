## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1260.1.0.0.0
-  __TEXT.__text: 0x279578
+1260.5.0.0.0
+  __TEXT.__text: 0x280e70
   __TEXT.__auth_stubs: 0x2480
-  __TEXT.__init_offsets: 0x1ac
-  __TEXT.__cstring: 0x7bde1
-  __TEXT.__const: 0x69b70
-  __TEXT.__oslogstring: 0x1f59
-  __TEXT.__unwind_info: 0x3748
+  __TEXT.__init_offsets: 0x1b8
+  __TEXT.__cstring: 0x7d859
+  __TEXT.__const: 0x7cff0
+  __TEXT.__oslogstring: 0x1e6a
+  __TEXT.__unwind_info: 0x37e0
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
-  Functions: 6793
-  Symbols:   9460
-  CStrings:  12462
+  Functions: 6885
+  Symbols:   9583
+  CStrings:  12627
 
Symbols:
+ __ZN31AppleBCMWLANChipManagerPCIe439932getFWDebugPMUCoreRegionTableSizeEv
+ __ZN25AppleBCMWLANChipBackplane25readPMNIAONPBWrapperReg32EjRj
+ _ZN23AppleBCMWLAN11beAdapter15isMloConnectionEv.cold.1
+ __ZN25AppleBCMWLANChipBackplane25readPMNICBAPBWrapperReg32EjRj
+ _GLOBAL__sub_I_AppleBCMWLANChipManagerPCIe4399.cpp
+ __block_descriptor_tmp.1134
+ __block_descriptor_tmp.1650
+ __ZN25AppleBCMWLANChipBackplane28dumpOOBConfigStatusRegistersEPcm
+ __ZL21kBCOM4399ChipMemories
+ __ZN23AppleBCMWLAN11beAdapter20configureMloFeaturesEb
+ __ZL50OSClassDescription_AppleBCMWLANChipManagerPCIe4399
+ __block_descriptor_tmp.385
+ __ZN23AppleBCMWLAN11beAdapter12configureMloEtR12mloAddrArray
+ __block_descriptor_tmp.3243
+ __ZN25AppleBCMWLANChipBackplane27readAMNIScanPhyWrapperReg32EjRj
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439912initWithChipEjh
+ __ZL35AppleBCMWLANChipManagerPCIe4399_NewP11OSMetaClass
+ __ZN27AppleBCMWLANChipManagerPCIe23setCoexCPUTrapSupportedEb
+ __block_descriptor_tmp.3290
+ __ZNK28AppleBCMWLANBusInterfacePCIe17dumpPMNIRegistersEv
+ _GLOBAL__sub_I_AppleBCMWLANChipManagerPCIe4399.iig.cpp
+ __ZN15AppleBCMWLANLQM23updateMloLinkChangeInfoEP25wl_mlo_link_info_event_v1
+ __ZN23AppleBCMWLAN11beAdapter16configureMloPrefEv
+ __ZNK22AppleBCMWLANChipMemory11readCoexRAMEjjP13IO80211Bufferj
+ __ZN23AppleBCMWLAN11beAdapter4freeEv
+ __ZN31AppleBCMWLANChipManagerPCIe439934getFWDebugPCIEFunc0CoreRegionTableEv
+ __block_descriptor_tmp.718
+ _AppleBCMWLANChipManagerPCIe4399_Class
+ __ZN15AppleBCMWLANLQM16storeMloLinkInfoEhtRK10ether_addr
+ __block_descriptor_tmp.726
+ __ZN23AppleBCMWLAN11beAdapter10withDriverEP16AppleBCMWLANCore
+ __block_descriptor_tmp.657
+ __ZZN20AppleBCMWLANChanSpec19getAppleChannelSpecEtE21chanIdToCenterlMap320
+ ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1128
+ __ZN25AppleBCMWLANChipBackplane39dumpCoreRegisterRegionswithMNIInterfaceEPcm
+ __ZN15AppleBCMWLANLQM15getMloPerfStatsEv
+ __ZN31AppleBCMWLANChipManagerPCIe439928getFWDebugARMCoreRegionTableEv
+ __ZThn64_N28AppleBCMWLANBusInterfacePCIe14readcoexSoCRAMEjP6OSDataPyj
+ __ZL29kBCOM4399FWDebugPMUCoreRanges
+ __block_descriptor_tmp.2255
+ __block_descriptor_tmp.1131
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439915prepareHardwareEP27AppleBCMWLANChipConfigSpaceP25AppleBCMWLANChipBackplane
+ __ZN31AppleBCMWLANChipManagerPCIe43998withChipEjh
+ __ZN25AppleBCMWLANChipBackplane30readAMNIChipCommonWrapperReg32EjRj
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439934getFWDebugPCIEFunc0CoreRegionTableEv
+ __ZN23AppleBCMWLAN11beAdapter15setupInitConfigEv
+ __block_literal_global.2307
+ __ZL32kBCOM4399FWDebugCommonCoreRanges
+ __block_descriptor_tmp.2273
+ __ZN31AppleBCMWLANChipManagerPCIe439923getDARSecurityStatusRegEP25AppleBCMWLANChipBackplane
+ __ZN25AppleBCMWLANChipBackplane27readSysmemSlaveWrapperReg32EjRj
+ _AppleBCMWLAN11beAdapter_Class
+ __ZL34kBCOM4399ChipConfigSpaceStateTable
+ _gAppleBCMWLANChipManagerPCIe4399MetaClass
+ __ZN31AppleBCMWLANChipManagerPCIe439928getFWDebugPMUCoreRegionTableEv
+ __ZN28AppleBCMWLANBusInterfacePCIe20attachCoexSoCRAMFileEP13CCFaultReport
+ __ZN25AppleBCMWLANChipBackplane23readHMNIGCIWrapperReg32EjRj
+ __ZTV32AppleBCMWLAN11beAdapterMetaClass
+ __ZN23AppleBCMWLAN11beAdapter15setupJoinConfigEbR10ether_addrb
+ __block_descriptor_tmp.206
+ __block_descriptor_tmp.2632
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439931getFWDebugCommonCoreRegionTableEv
+ __ZN15AppleBCMWLANLQM27updateMloTrafficSwitchStateEh
+ __block_descriptor_tmp.688
+ __block_descriptor_tmp.530
+ __ZL33fileValidation4399ImagesSHA_array
+ __ZN28AppleBCMWLANBusInterfacePCIe14readcoexSoCRAMEjP6OSDataPyj
+ _GLOBAL__sub_I_AppleBCMWLAN11beAdapter.cpp
+ __ZN31AppleBCMWLANChipManagerPCIe439935getFWDebugCommonCoreRegionTableSizeEv
+ __ZL29kBCOM4399ChipBackplaneWindows
+ __ZL21kBCOM4399ChipWrappers
+ __block_descriptor_tmp.836
+ __block_descriptor_tmp.936
+ __ZL16kBCOM4399ChipOTP
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439921isSecureBootSupportedEv
+ __block_descriptor_tmp.707
+ __block_descriptor_tmp.794
+ __ZL42OSClassDescription_AppleBCMWLAN11beAdapter
+ _ZN23AppleBCMWLAN11beAdapter15setupJoinConfigEbR10ether_addrb.cold.1
+ __ZN23AppleBCMWLAN11beAdapter12getMloStatusEv
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.685
+ __ZZN25AppleBCMWLANChipBackplane28dumpOOBConfigStatusRegistersEPcmE11oobCoreRegs
+ __ZN31AppleBCMWLANChipManagerPCIe439921isSecureBootSupportedEv
+ __ZN31AppleBCMWLANChipManagerPCIe439931getFWDebugCommonCoreRegionTableEv
+ _ZN23AppleBCMWLAN11beAdapter12getMloStatusEv.cold.1
+ _ZN23AppleBCMWLAN11beAdapter13dumpMloStatusEPcjj.cold.1
+ __block_descriptor_tmp.573
+ __ZN23AppleBCMWLAN11beAdapter22setMultilinkActiveModeEj
+ __ZN23AppleBCMWLAN11beAdapter14initWithDriverEP16AppleBCMWLANCore
+ __ZN31AppleBCMWLANChipManagerPCIe439915hasMNIInterfaceEv
+ __ZN23AppleBCMWLAN11beAdapter24configureMloFeaturesInitEv
+ __ZN23AppleBCMWLAN11beAdapter18handleMloLinkEventEP14wl_event_msg_t
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2253
+ __block_descriptor_tmp.3225
+ __ZN31AppleBCMWLANChipManagerPCIe439932getFWDebugARMCoreRegionTableSizeEv
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439915hasMNIInterfaceEv
+ __block_descriptor_tmp.2305
+ __block_descriptor_tmp.580
+ __block_descriptor_tmp.702
+ __ZTV31AppleBCMWLANChipManagerPCIe4399
+ __ZL27AppleBCMWLAN11beAdapter_NewP11OSMetaClass
+ __block_descriptor_tmp.1124
+ __ZN25AppleBCMWLANChipBackplane26writeOOBRouterWrapperReg32Ejj
+ __block_descriptor_tmp.1133
+ __ZN31AppleBCMWLANChipManagerPCIe439912initWithChipEjh
+ __ZL27kBCOM4399UCodeSHMRegionInfo
+ __block_descriptor_tmp.683
+ __block_descriptor_tmp.2251
+ __block_descriptor_tmp.717
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439913checkHardwareEP27AppleBCMWLANChipConfigSpaceP25AppleBCMWLANChipBackplane
+ __ZL18kBCOM4399ChipCores
+ __ZNK27AppleBCMWLANChipManagerPCIe22isCoexCPUTrapSupportedEv
+ __ZZN25AppleBCMWLANChipBackplane19dumpMNIIDMRegistersEPcmE10dmpMNIRegs
+ __ZN31AppleBCMWLANChipManagerPCIe439938getFWDebugPCIEFunc0CoreRegionTableSizeEv
+ __block_descriptor_tmp.835
+ _gAppleBCMWLAN11beAdapter_Declaration
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439928getFWDebugARMCoreRegionTableEv
+ __ZN25AppleBCMWLANChipBackplane22readHMNIBTWrapperReg32EjRj
+ __block_descriptor_tmp.3140
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439932getFWDebugPMUCoreRegionTableSizeEv
+ __block_literal_global.2275
+ __ZL35kBCOM4399FWDebugPCIEFunc0CoreRanges
+ __ZTV40AppleBCMWLANChipManagerPCIe4399MetaClass
+ __ZN25AppleBCMWLANChipBackplane19dumpMNIIDMRegistersEPcm
+ __ZTV23AppleBCMWLAN11beAdapter
+ __block_descriptor_tmp.2668
+ __ZL29kBCOM4399FWDebugARMCoreRanges
+ __ZN25AppleBCMWLANChipBackplane27readAMNIScanMacWrapperReg32EjRj
+ __ZN15AppleBCMWLANLQM18getMloPerLinkStatsEh
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439923getDARSecurityStatusRegEP25AppleBCMWLANChipBackplane
+ __ZN25AppleBCMWLANChipBackplane26readAMNIAuxPhyWrapperReg32EjRj
+ __block_descriptor_tmp.3246
+ __ZThn24_N23AppleBCMWLAN11beAdapter4freeEv
+ __ZN15AppleBCMWLANLQM19updateNumOfMloLinksEh
+ __ZN23AppleBCMWLAN11beAdapter15isMloConnectionEv
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439928getFWDebugPMUCoreRegionTableEv
+ __ZN19AppleBCMWLANCoreDbg12cmdMloStatusEP24apple80211_debug_commandP16AppleBCMWLANCore
+ __ZN27AppleBCMWLANChipManagerPCIe32setFatalErrorIndicationSupportedEb
+ _ZN23AppleBCMWLAN11beAdapter12configureMloEtR12mloAddrArray.cold.1
+ __ZN31AppleBCMWLANChipManagerPCIe439913checkHardwareEP27AppleBCMWLANChipConfigSpaceP25AppleBCMWLANChipBackplane
+ __ZNK28AppleBCMWLANBusInterfacePCIe12checkPMNIAPBEv
+ __ZL20kBCOM4399CoreIDTable
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439938getFWDebugPCIEFunc0CoreRegionTableSizeEv
+ __ZN31AppleBCMWLANChipManagerPCIe439915prepareHardwareEP27AppleBCMWLANChipConfigSpaceP25AppleBCMWLANChipBackplane
+ __ZN25AppleBCMWLANChipBackplane27readAMNIMainPhyWrapperReg32EjRj
+ __ZN40AppleBCMWLANChipManagerPCIe4399MetaClass3NewEP8OSObject
+ __ZN25AppleBCMWLANChipBackplane17readSRCBCoreReg32EjRj
+ __ZL20kBCOM4399ChipUserOTP
+ _gAppleBCMWLAN11beAdapterMetaClass
+ __block_descriptor_tmp.3241
+ __block_descriptor_tmp.383
+ _gAppleBCMWLANChipManagerPCIe4399_Declaration
+ __block_descriptor_tmp.845
+ __ZN25AppleBCMWLANChipBackplane25readPMNIWLAPBWrapperReg32EjRj
+ __ZN32AppleBCMWLAN11beAdapterMetaClass3NewEP8OSObject
+ __block_descriptor_tmp.728
+ __ZL27kBCOM4399UCodeSCRRegionInfo
+ _ZN15AppleBCMWLANLQM18getMloPerLinkStatsEh.cold.1
+ __ZNK16AppleBCMWLANCore14get11beAdapterEv
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439935getFWDebugCommonCoreRegionTableSizeEv
+ __block_descriptor_tmp.1957
+ __block_descriptor_tmp.3252
+ __block_descriptor_tmp.257
+ __ZN23AppleBCMWLAN11beAdapter13dumpMloStatusEPcjj
+ __ZThn56_N31AppleBCMWLANChipManagerPCIe439932getFWDebugARMCoreRegionTableSizeEv
+ __block_descriptor_tmp.331
- __block_descriptor_tmp.831
- __block_descriptor_tmp.2272
- __block_descriptor_tmp.711
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2252
- __block_descriptor_tmp.578
- __block_descriptor_tmp.1649
- __block_descriptor_tmp.1956
- __block_descriptor_tmp.935
- __block_descriptor_tmp.204
- __block_descriptor_tmp.379
- __block_descriptor_tmp.255
- __block_descriptor_tmp.723
- __block_literal_global.2274
- __block_descriptor_tmp.3251
- __block_descriptor_tmp.1078
- __block_descriptor_tmp.680
- __block_descriptor_tmp.1088
- __block_descriptor_tmp.2254
- __block_descriptor_tmp.3224
- __block_literal_global.2306
- __block_descriptor_tmp.830
- __block_descriptor_tmp.725
- __block_descriptor_tmp.3139
- __block_descriptor_tmp.840
- __block_descriptor_tmp.1087
- __block_descriptor_tmp.656
- __block_descriptor_tmp.381
- __block_descriptor_tmp.2667
- __block_descriptor_tmp.1085
- __block_descriptor_tmp.3240
- __block_descriptor_tmp.3242
- __block_descriptor_tmp.329
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.682
- __block_descriptor_tmp.699
- __block_descriptor_tmp.571
- __block_descriptor_tmp.2250
- __block_descriptor_tmp.715
- __block_descriptor_tmp.3245
- ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1082
- __block_descriptor_tmp.3289
- __block_descriptor_tmp.793
- __block_descriptor_tmp.528
- __block_descriptor_tmp.2304
- __block_descriptor_tmp.685
- __block_descriptor_tmp.704
- __block_descriptor_tmp.2631
CStrings:
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read ARM CA7 DMP ctrl register (0x%!x(MISSING)) , 0x%!x(MISSING) \n"
+ "OtherScanOffChDur"
+ "[dk] %!s(MISSING)@%!d(MISSING):MLO Enabled=<%!d(MISSING)> numberOfLinks<%!d(MISSING)>-><%!d(MISSING)> force=%!d(MISSING)\n"
+ "\"AppleBCMWLANV3_driverkit-1260.5\""
+ "[dk] %!s(MISSING)@%!d(MISSING):Bail out Coex SoCRAM dump: No Memory\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI WL APB wrapper SILDBG: 0x%!x(MISSING)\n"
+ "kBCOMMNIIDMInterruptStatus"
+ "AMNI_MainPHY"
+ "[dk] %!s(MISSING)@%!d(MISSING):Dump the PMNI Wrapper registers for debug \n"
+ "Sep  2 2024 22:10:18"
+ "Sysmem"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI CB APB wrapper Interrupt Mask: 0x%!x(MISSING)\n"
+ "getMloStatus"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper resetctl: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper errorlogstatus: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING): Unable to create 11be Adapter object!\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI AON APB wrapper IDB Device ID: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):i =<%!d(MISSING)> if_idx=<%!d(MISSING)> cfg_idx=<%!d(MISSING)> link_id<%!d(MISSING)> link_idx=<%!d(MISSING)> chanspec=<%!x(MISSING)> link_addr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "configureMlo"
+ "kBCOMMNIIDMErrAddrMSB_ns"
+ "kBCOMMNIIDMInterurptMask"
+ "kBCOMMNIIDMResetControl"
+ "i=%!d(MISSING)  channel=%!d(MISSING) band = %!d(MISSING), local link addr= %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING) peer link addr %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING) \n"
+ "kBCOMMNIIDMAccessControl"
+ "kBCOMMNIIDMErrAddrLSB"
+ "[dk] %!s(MISSING)@%!d(MISSING):link id =<%!d(MISSING)> %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI AON APB wrapper Interrupt Mask: 0x%!x(MISSING)\n"
+ "setMultilinkActiveMode"
+ "PMNI_APB-CB"
+ "kBCOMOOBCoreDMPStatus"
+ "[dk] %!s(MISSING)@%!d(MISSING): mloFeaturesConfig_t mask:0x%!x(MISSING) enab:0x%!x(MISSING)  --> %!d(MISSING)[%!s(MISSING)] \n"
+ "%!s(MISSING)[%!x(MISSING)]%!s(MISSING): 0x%!x(MISSING)\n"
+ "AppleBCMWLAN11beAdapter driver is null\n"
+ "AssocScanOffChDur"
+ "kBCOMMNIIDMResetReadID"
+ "/Library/Caches/com.apple.xbs/Sources/AppleBCMWLANV3_driverkit/AppleBCMWLAN11beAdapter.cpp"
+ "[dk] %!s(MISSING)@%!d(MISSING):len=<%!d(MISSING)> mode<%!d(MISSING)>  num_links=<%!d(MISSING)>   local mld_addr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI WL APB wrapper Interrupt Mask: 0x%!x(MISSING)\n"
+ "ArmCA7"
+ "[dk] %!s(MISSING)@%!d(MISSING):[%!d(MISSING):%!d(MISSING)]=link_id=<%!d(MISSING)> link_idx<%!d(MISSING)>  local link adrr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING), peer link adrr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING), peer mld adrr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper kBCOMWrapperRegIntMaskNs: 0x%!x(MISSING)\n"
+ "kBCOMMNIIDMErrMisc0"
+ "kBCOMMNIIDMInterruptMask_ns"
+ "AMNI_MainMAC"
+ "kBCOMMNIIDMAccessReadID"
+ "kBCOMMNIIDMResetStatus"
+ "UserScanOffChDur"
+ "AMNI_ScanMAC"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI CB APB errorlogstatus wrapper reg non-zero: data1: 0x%!x(MISSING) data2: 0x%!x(MISSING)\n"
+ "kBCOMMNIIDMTimeoutValue"
+ "kBCOMMNIIDMResetStatus_ns"
+ "kBCOMMNIIDMAccessStatus_ns"
+ "kBCOMMNISILDBG"
+ "kBCOMMNIIDMAccessStatus"
+ "Set 41 Rate Selection"
+ "[dk] %!s(MISSING)@%!d(MISSING): wlan.pcie.disableCoexCPUDumpSupport %!d(MISSING)\n"
+ "dumpMloStatus"
+ "AMNI_CHIPCOMMON"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI WL APB errorlogstatus wrapper reg non-zero: data1: 0x%!x(MISSING) data2: 0x%!x(MISSING)\n"
+ "kBCOMMNIIDMErrMisc0_ns"
+ "configureMloPref"
+ "AMNI_AuxMAC"
+ "[dk] %!s(MISSING)@%!d(MISSING):configureMlo %!d(MISSING)[%!s(MISSING)] numberOfLinks=<%!d(MISSING)> %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "MainD11Mac"
+ "PMNI_WLANCB"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI WL APB resetctl wrapper reg non-zero: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI AON APB wrapper SILDBG: 0x%!x(MISSING)\n"
+ "RoamScanOffChDur"
+ "kBCOMMNIIDMAccessWriteID_ns"
+ "isMloConnection"
+ "/AppleInternal/Library/BuildRoots/e2b39c6c-690e-11ef-9b05-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.1.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper kBCOMWrapperRegIntMaskNs: 0x%!x(MISSING)\n"
+ "AuxD11Mac"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI CB APB wrapper SILDBG: 0x%!x(MISSING)\n"
+ "kBCOMMNIIDMAccessWriteID"
+ "kBCOMMNIIDMErrStatus"
+ "[dk] %!s(MISSING)@%!d(MISSING):No valid channels num req %!d(MISSING) \n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper kBCOMWrapperRegSILDBG: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper resetctl: 0x%!x(MISSING)\n"
+ "Saqm"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper errorlogstatus: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI AON APB errorlogstatus wrapper reg non-zero: data1: 0x%!x(MISSING) data2: 0x%!x(MISSING)\n"
+ "mlo numberOfLinks is %!d(MISSING)  local mld addr= %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING) peer mld add %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING) \n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Coex SoCRAM ivars->fCoexCPUTrapped  %!d(MISSING)  ivars->fCoexCPUTrapRequested %!d(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING): mloConfigPref_t %!d(MISSING)[%!s(MISSING)]\n"
+ "ScanD11Mac"
+ "[dk] %!s(MISSING)@%!d(MISSING):ampdu_stats_type_int larger than max known WL_AMPDU_STATS_TYPE_MLO_LINK_INFO\n"
+ "kBCOMOOBCoreExtRsrcReq"
+ "PMNI_APB-AAON"
+ "Failed to allocate AppleBCMWLAN11beAdapter_IVars\n"
+ "[dk] %!s(MISSING)@%!d(MISSING): getMloStatus %!d(MISSING)[%!s(MISSING)] \n"
+ "AppleBCMWLAN11beAdapter commander is null\n"
+ "kBCOMMNIIDMDeivceID"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper kBCOMWrapperRegSILDBG: 0x%!x(MISSING)\n"
+ "kBCOMMNIIDMErrStatus_ns"
+ "readcoexSoCRAM"
+ "attachCoexSoCRAMFile"
+ "AppleBCMWLAN11beAdapter Failed to init fLogger\n"
+ "getMloPerLinkStats"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper kBCOMWrapperRegIDMDeviceID: 0x%!x(MISSING)\n"
+ "HMNI_GCI"
+ "OOB config and status"
+ "[dk] %!s(MISSING)@%!d(MISSING): multilink_active mode %!d(MISSING)[%!s(MISSING)] set<%!d(MISSING)> \n"
+ "setupJoinConfig"
+ "kBCOMMNIIDMErrAddrMSB"
+ "kBCOMOOBCoreDMPControl"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read Sysmem DMP ctrl register (0x%!x(MISSING)) , 0x%!x(MISSING) \n"
+ "[dk] %!s(MISSING)@%!d(MISSING): mloFeaturesConfig_t mask:0x%!x(MISSING) enab:0x%!x(MISSING)  --> %!d(MISSING)[%!s(MISSING)], low-latency = %!s(MISSING) \n"
+ "kBCOMMNIIDMErrMisc1_ns"
+ "AppleBCMWLAN11beAdapter super init failied\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):TCM memory is not accessible. reset ctrl:0x%!x(MISSING) 0x%!x(MISSING) DMP ctrl:0x%!x(MISSING) 0x%!x(MISSING)\n"
+ "coex_SoC_RAM.bin"
+ "[dk] %!s(MISSING)@%!d(MISSING):TCM memory is accessible. reset ctrl:0x%!x(MISSING) 0x%!x(MISSING) DMP ctrl:0x%!x(MISSING) 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI WL APB wrapper kBCOMWrapperRegIDMDeviceID: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI AON APB resetctl wrapper reg non-zero: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):MLO Stats [%!s(MISSING) Preferred:%!u(MISSING)] chan: %!u(MISSING) / %!s(MISSING) rssi: [%!d(MISSING), %!d(MISSING)] tx_pkts: %!d(MISSING) rx_pkts: %!d(MISSING) tx_rate: %!d(MISSING) rx_rate: %!d(MISSING) tx_fail: %!d(MISSING) ex_retry: %!d(MISSING) idle: %!d(MISSING) ovflo: %!s(MISSING)\n"
+ "Set 42 eMLSR"
+ "configureMloFeaturesInit"
+ "[dk] %!s(MISSING)@%!d(MISSING):v=<%!d(MISSING)> len=<%!d(MISSING)> opcode<%!d(MISSING)> role=<%!d(MISSING)> num_links=<%!d(MISSING)>  pref_band_link_idx=<%!d(MISSING)> mld_addr =%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
+ "kBCOMMNIIDMErrAddrLSB_ns"
+ "btsc"
+ "AMNI_AuxPHY"
+ "cant create a random mac address after 100 tries"
+ "configureMloFeatures"
+ "AMNI_CCI"
+ "mlo numberOfLinks is 0 \n"
+ "HMNI_BT"
+ "wlan.pcie.disableCoexCPUDumpSupport"
+ "mlo_status"
+ "mlo"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper errorlogstatus: 0x%!x(MISSING)\n"
+ "kBCOMMNIIDMResetReadID_ns"
+ "Set 40 MLO Link Info"
+ "btmc"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI CB APB wrapper IDB Device ID: 0x%!x(MISSING)\n"
+ "coex_socRam"
+ "PNOScanOffChDur"
+ "[dk] %!s(MISSING)@%!d(MISSING):Bail out Coex SoCRAM dump: TCM Not accessible.\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Coex CPU trap Requested\n"
+ "kBCOMMNIIDMConfig"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper kBCOMWrapperRegIDMDeviceID: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):PMNI CB APB resetctl wrapper reg non-zero: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Invaid chanspec channel=%!d(MISSING) flags=0x%!x(MISSING). skipping channel -> WA for wifid bug!\n"
+ "kBCOMMNIIDMResetWriteID_ns"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper resetctl: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING): getMloStatus %!d(MISSING) [%!s(MISSING)] \n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Coex CPU trap Indicated\n"
+ "GCI"
+ "BCMWLAN Chip Coex Trap"
+ "updateMloLinkChangeInfo"
+ "Core Register Regions with MNI interface"
+ "AppleBCMWLANV3_driverkit-1260.5"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI AON APB wrapper kBCOMWrapperRegIntMaskNs: 0x%!x(MISSING)\n"
+ "AMNI_PCIeF0"
+ "PCIE"
+ "kBCOMMNIIDMErrMisc1"
+ "kBCOMMNIIDMInterurptStatus_ns"
+ "kBCOMMNIIDMErrCtrl"
+ "SRCB"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read PMNI CB APB wrapper kBCOMWrapperRegSILDBG: 0x%!x(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Failed to read Sysmem slave wrapper reset ctrl register (0x%!x(MISSING)) , 0x%!x(MISSING) \n"
+ "kBCOMMNIIDMResetWriteiID"
+ "[dk] %!s(MISSING)@%!d(MISSING): User Roam Cache (%!d(MISSING)) BSSID %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING), MLD:%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING), RSSI %!d(MISSING) chanspec %!d(MISSING) age %!d(MISSING) load %!d(MISSING)\n"
+ "[dk] %!s(MISSING)@%!d(MISSING):Debug data PMNI WL APB wrapper IDB Device ID: 0x%!x(MISSING)\n"
+ "kBCOMOOBCoreClockPwrReq"
+ "kBCOMMNIIDMTimeoutControl"
+ "[dk] %!s(MISSING)@%!d(MISSING): (%!d(MISSING)) BSSID %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING), MLD:%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING) RSSI %!d(MISSING) chanspec %!d(MISSING) age %!d(MISSING) load %!d(MISSING)\n"
+ "checkPMNIAPB"
+ "ChipC"
+ "LHL"
+ "kBCOMMNIIDMAccessReadID_ns"
+ "AMNI_ScanPHY"
+ "dumpPMNIRegisters"
- "\"AppleBCMWLANV3_driverkit-1260.1\""
- "Aug 16 2024 00:16:44"
- "[dk] %!s(MISSING)@%!d(MISSING):ampdu_stats_type_int larger than max known WL_AMPDU_STATS_TYPE_TXHEx4\n"
- "/AppleInternal/Library/BuildRoots/b3afb696-5af4-11ef-b143-56363ce8160b/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.1.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "%!c(MISSING) [dk] %!s(MISSING)@%!d(MISSING):  status = %!l(MISSING)u %!s(MISSING), f/w reason = %!l(MISSING)u %!s(MISSING), flags = 0x%!x(MISSING), authtype = %!l(MISSING)u, addr = %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
- "%!c(MISSING) [dk] %!s(MISSING)@%!d(MISSING): status = %!l(MISSING)u %!s(MISSING), reason = %!l(MISSING)u %!s(MISSING), flags = 0x%!x(MISSING), authtype = %!l(MISSING)u, addr = %!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING):%!x(MISSING)\n"
- "[dk] %!s(MISSING)@%!d(MISSING):Invaid chanspec channel=%!d(MISSING) flags=0x%!x(MISSING). NOT able to configure pfn_cfg. Bail out!\n"
- "AppleBCMWLANV3_driverkit-1260.1"

```
