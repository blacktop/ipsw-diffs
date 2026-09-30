## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1485.4.0.0.0
-  __TEXT.__text: 0x2b1138
-  __TEXT.__auth_stubs: 0x24f0
+1526.62.0.0.0
+  __TEXT.__text: 0x2b3afc
+  __TEXT.__auth_stubs: 0x2530
   __TEXT.__init_offsets: 0x1bc
-  __TEXT.__cstring: 0x7e80f
-  __TEXT.__const: 0x7e320
+  __TEXT.__cstring: 0x7f833
+  __TEXT.__const: 0x7ec70
   __TEXT.__oslogstring: 0x1f52
-  __TEXT.__unwind_info: 0x5d70
+  __TEXT.__unwind_info: 0x5e08
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x1278
+  __DATA_CONST.__auth_got: 0x1298
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x20238
+  __DATA_CONST.__const: 0x209b0
   __DATA_CONST.__osclassinfo: 0x388
   __DATA.__data: 0x390
   __DATA.__bss: 0x958

   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: 00140447-F5C5-34E5-92A3-CCBA16502827
-  Functions: 13075
-  Symbols:   16288
-  CStrings:  12699
+  UUID: 94C93CF8-7867-3409-BB27-59041E9FAB7A
+  Functions: 13102
+  Symbols:   16306
+  CStrings:  12840
 
Symbols:
+ _OUTLINED_FUNCTION_132
+ _OUTLINED_FUNCTION_145
+ _OUTLINED_FUNCTION_278
+ _ZN16AppleBCMWLANCore18parsePHYEcounterV7EP6OSData.cold.9
+ _ZN16AppleBCMWLANCore19setWiFiCallPoliciesE33apple80211_wifiFaceTimeCallStatus.cold.1
+ _ZN16AppleBCMWLANCore19setWiFiCallPoliciesE33apple80211_wifiFaceTimeCallStatus.cold.2
+ _ZN16AppleBCMWLANCore20handleRxStallReasonsEP20bcm_dngl_healthcheckRiS2_Ph.cold.4
+ _ZN16AppleBCMWLANCore20handleRxStallReasonsEP20bcm_dngl_healthcheckRiS2_Ph.cold.5
+ _ZN16AppleBCMWLANCore20handleRxStallReasonsEP20bcm_dngl_healthcheckRiS2_Ph.cold.6
+ _ZN16AppleBCMWLANCore20handleRxStallReasonsEP20bcm_dngl_healthcheckRiS2_Ph.cold.7
+ _ZN16AppleBCMWLANCore21setAdaptive11rFromASREv.cold.1
+ _ZN16AppleBCMWLANCore23handleDongleEventPacketEPKN16AppleBCMWLANUtil12DeviceBufferE.cold.17
+ _ZN16AppleBCMWLANCore30configureRxHCRTSCTSEventParamsEjh.cold.1
+ _ZN16AppleBCMWLANCore30configureRxHCRTSCTSEventParamsEjh.cold.2
+ _ZN16AppleBCMWLANCore30configureRxHCRTSCTSEventParamsEjh.cold.3
+ _ZN16AppleBCMWLANCore30configureRxHCRTSCTSEventParamsEjh.cold.4
+ _ZN21AppleBCMWLANCommander14initWithConfigEP16AppleBCMWLANCoreP24AppleBCMWLANBusInterfacej.cold.7
+ _ZN22AppleBCMWLANNetAdapter11setLinkDownEv.cold.1
+ _ZN23AppleBCMWLAN11beAdapter13getMloContextER17apple_mlo_contextR10ether_addr.cold.1
+ _ZN23AppleBCMWLAN11beAdapter13getMloContextER17apple_mlo_contextR10ether_addr.cold.2
+ _ZN23AppleBCMWLANJoinAdapter21abortFirmwareJoinSyncEb.cold.1
+ _ZN23AppleBCMWLANRoamAdapter22setROAM_PROFILE_CONFIGEP30apple80211_roam_profile_config.cold.5
+ _ZN23AppleBCMWLANRoamAdapter25cfgRoamPruneRssiThresholdEa.cold.1
+ _ZN23AppleBCMWLANRoamAdapter46handlePruneThresholdConfigurationAsyncCallbackER9CommandIDiR16CommandRxPayloadPv.cold.1
+ _ZN24AppleBCMWLANNANInterface11setNAN_INITEP19apple80211_nan_init.cold.7
+ _ZN24AppleBCMWLANNANInterface13setNAN_DP_REQEP25apple80211_nan_dp_request.cold.2
+ _ZN24AppleBCMWLANNANInterface13setNAN_DP_REQEP25apple80211_nan_dp_request.cold.3
+ _ZN24AppleBCMWLANNANInterface14setNAN_PUBLISHEP27apple80211_nan_publish_data.cold.2
+ _ZN24AppleBCMWLANNANInterface23getNAN_deviceCapabilityEP32apple80211_p2p_device_capability.cold.1
+ _ZN24AppleBCMWLANNANInterface23getNAN_deviceCapabilityEP32apple80211_p2p_device_capability.cold.2
+ _ZN24AppleBCMWLANNANInterface23getNAN_deviceCapabilityEP32apple80211_p2p_device_capability.cold.3
+ _ZN24AppleBCMWLANNANInterface23setNAN_NDC_AVAILABILITYEP40apple80211_nan_data_cluster_availability.cold.3
+ _ZN24AppleBCMWLANNANInterface24getNAN_DEVICE_CAPABILITYEP32apple80211_nan_device_capability.cold.4
+ _ZN24AppleBCMWLANNANInterface24getNAN_DEVICE_CAPABILITYEP32apple80211_nan_device_capability.cold.5
+ _ZN28AppleBCMWLANBusInterfacePCIe10configHMAPEv.cold.5
+ _ZN28AppleBCMWLANBusInterfacePCIe10readSoCRAMEjP24IOBufferMemoryDescriptoryj.cold.1
+ _ZN28AppleBCMWLANBusInterfacePCIe10readSoCRAMEjP24IOBufferMemoryDescriptoryj.cold.2
+ _ZN28AppleBCMWLANBusInterfacePCIe10readSoCRAMEjP24IOBufferMemoryDescriptoryj.cold.3
+ _ZN28AppleBCMWLANBusInterfacePCIe10readSoCRAMEjP24IOBufferMemoryDescriptoryj.cold.4
+ _ZN30AppleBCMWLANProximityInterface21setPEER_CACHE_CONTROLEP29apple80211_peer_cache_control.cold.9
+ _ZN30AppleBCMWLANProximityInterface29setAWDL_RTG_PEER_STATS_CONFIGEP29apple80211_rtg_peer_stats_cfg.cold.1
+ __Z40IO80211CalculateMaxNSSAndVHTMCSForMCSMaptPjS_
+ __ZN14IO80211CoreDbg11soiCmdPrintEP24apple80211_debug_commandP17IO80211ControllerPc
+ __ZN16AppleBCMWLANCore14getBssPhyModdeEP21AppleBCMWLANBSSBeacon
+ __ZN16AppleBCMWLANCore14getIsInfraOn2GEv
+ __ZN16AppleBCMWLANCore16getHE_CAPABILITYEP24apple80211_he_capability
+ __ZN16AppleBCMWLANCore17setWCL_JOIN_ABORTEP25apple80211_wcl_abort_join
+ __ZN16AppleBCMWLANCore19setWiFiCallPoliciesE33apple80211_wifiFaceTimeCallStatus
+ __ZN16AppleBCMWLANCore21setAdaptive11rFromASREv
+ __ZN16AppleBCMWLANCore24getP2P_DEVICE_CAPABILITYEP32apple80211_p2p_device_capability
+ __ZN16AppleBCMWLANCore30configureRxHCRTSCTSEventParamsEjh
+ __ZN17IO80211BssManager12setAssocSSIDEPKhm
+ __ZN17IO80211Controller18getACCESSORY_STATEEP23IO80211SkywalkInterfaceP32apple80211_device_accessory_info
+ __ZN17IO80211Controller18setACCESSORY_STATEEP23IO80211SkywalkInterfaceP32apple80211_device_accessory_info
+ __ZN17IO80211Controller21getDEVICE_ORIENTATIONEP23IO80211SkywalkInterfaceP29apple80211_device_orientation
+ __ZN17IO80211Controller21setDEVICE_ORIENTATIONEP23IO80211SkywalkInterfaceP29apple80211_device_orientation
+ __ZN17IOUserNetworkWLAN15addSteeringRuleE40IOUserNetworkEthernetTrafficSteeringRuleP21IOUserNetworkQueueSetPA16_h
+ __ZN17IOUserNetworkWLAN17removeLogicalLinkEP24IOUserNetworkLogicalLink
+ __ZN17IOUserNetworkWLAN18removeSteeringRuleEPh
+ __ZN21AppleBCMWLANCommander20checkCurrentCmdStuckEP18IO80211TimerSource
+ __ZN21IO80211InfraInterface12setLinkStateE16IO80211LinkStatejbjj
+ __ZN21IO80211InfraInterface20setLinkStateInternalE16IO80211LinkStatejbjj
+ __ZN21IO80211InfraInterface24createLinkQualityMonitorEP11IO80211Peerb
+ __ZN21IO80211InfraInterface24setWCL_LINK_STATE_UPDATEEP32apple80211_wcl_update_link_state
+ __ZN22AppleBCMWLANNetAdapter11setLinkDownEv
+ __ZN22AppleBCMWLANNetAdapter18configureWmeParamsER12edcf_acparam
+ __ZN22AppleBCMWLANNetAdapter23configureAggressiveEDCAEb
+ __ZN23AppleBCMWLAN11beAdapter10disableMloER10ether_addr
+ __ZN23AppleBCMWLAN11beAdapter10setMloAddrER12mloAddrArray
+ __ZN23AppleBCMWLAN11beAdapter13getMloContextER17apple_mlo_contextR10ether_addr
+ __ZN23AppleBCMWLAN11beAdapter15setupJoinConfigEbR12mloAddrArrayb
+ __ZN23AppleBCMWLANJoinAdapter21abortFirmwareJoinSyncEb
+ __ZN23AppleBCMWLANRoamAdapter16setReassocParamsEab
+ __ZN23AppleBCMWLANRoamAdapter20restoreReassocParamsEv
+ __ZN23AppleBCMWLANRoamAdapter25cfgRoamPruneRssiThresholdEa
+ __ZN23AppleBCMWLANRoamAdapter46handlePruneThresholdConfigurationAsyncCallbackER9CommandIDiR16CommandRxPayloadPv
+ __ZN23AppleBCMWLANRoamAdapter5resetEv
+ __ZN23IO80211SkywalkInterface12syncDPSStatsEv
+ __ZN23IO80211SkywalkInterface24createLinkQualityMonitorEP11IO80211Peerb
+ __ZN23IO80211VirtualInterface4stopEP9IOService
+ __ZN24AppleBCMWLANNANInterface23getNAN_deviceCapabilityEP32apple80211_p2p_device_capability
+ __ZN24IOBufferMemoryDescriptor6CreateEyyyPPS_
+ __ZN25AppleBCMWLANInfraProtocol16getHE_CAPABILITYEP24apple80211_he_capability
+ __ZN25AppleBCMWLANInfraProtocol17getLQM_STATISTICSEP25apple80211_lqm_statistics
+ __ZN25AppleBCMWLANInfraProtocol17setWCL_JOIN_ABORTEP25apple80211_wcl_abort_join
+ __ZN25AppleBCMWLANInfraProtocol18getSMARTCCA_OPMODEEP26apple80211_smartcca_opmode
+ __ZN25AppleBCMWLANInfraProtocol21setBTCOEX_EXT_PROFILEEP29apple80211_btcoex_ext_profile
+ __ZN25AppleBCMWLANInfraProtocol24getP2P_DEVICE_CAPABILITYEP32apple80211_p2p_device_capability
+ __ZN28AppleBCMWLANBusInterfacePCIe10readSoCRAMEjP24IOBufferMemoryDescriptoryj
+ __ZN28AppleBCMWLANNANDataInterface12getSTA_STATSEP25apple80211_sta_stats_data
+ __ZN28AppleBCMWLANSkywalkInterface13setMacAddressER12mloAddrArray
+ __ZN31AppleBCMWLANLowLatencyInterface13setMacAddressER12mloAddrArray
+ __ZN40AppleBCMWLANPCIeSkywalkTxSubmissionQueue15validateMacAddrEP29AppleBCMWLANPCIeSkywalkPacketP28AppleBCMWLANSkywalkInterface
+ __ZNK16IO80211BSSBeacon12isEhtEnabledEv
+ __ZNK16IO80211BSSBeacon14isOnRSNNetworkEPKhhjjtj
+ __ZNK16IO80211BSSBeacon20getChanPrimarySWSpecEv
+ __ZNK16IO80211BSSBeacon7getBandEv
+ __ZThn112_N25AppleBCMWLANInfraProtocol16getHE_CAPABILITYEP24apple80211_he_capability
+ __ZThn112_N25AppleBCMWLANInfraProtocol17getLQM_STATISTICSEP25apple80211_lqm_statistics
+ __ZThn112_N25AppleBCMWLANInfraProtocol17setWCL_JOIN_ABORTEP25apple80211_wcl_abort_join
+ __ZThn112_N25AppleBCMWLANInfraProtocol18getSMARTCCA_OPMODEEP26apple80211_smartcca_opmode
+ __ZThn112_N25AppleBCMWLANInfraProtocol21setBTCOEX_EXT_PROFILEEP29apple80211_btcoex_ext_profile
+ __ZThn112_N25AppleBCMWLANInfraProtocol24getP2P_DEVICE_CAPABILITYEP32apple80211_p2p_device_capability
+ __ZThn112_N28AppleBCMWLANNANDataInterface12getSTA_STATSEP25apple80211_sta_stats_data
+ __ZThn128_N25AppleBCMWLANInfraProtocol16getHE_CAPABILITYEP24apple80211_he_capability
+ __ZThn128_N25AppleBCMWLANInfraProtocol17getLQM_STATISTICSEP25apple80211_lqm_statistics
+ __ZThn128_N25AppleBCMWLANInfraProtocol17setWCL_JOIN_ABORTEP25apple80211_wcl_abort_join
+ __ZThn128_N25AppleBCMWLANInfraProtocol18getSMARTCCA_OPMODEEP26apple80211_smartcca_opmode
+ __ZThn128_N25AppleBCMWLANInfraProtocol21setBTCOEX_EXT_PROFILEEP29apple80211_btcoex_ext_profile
+ __ZThn128_N25AppleBCMWLANInfraProtocol24getP2P_DEVICE_CAPABILITYEP32apple80211_p2p_device_capability
+ __ZThn128_N28AppleBCMWLANNANDataInterface12getSTA_STATSEP25apple80211_sta_stats_data
+ __ZThn40_NK16IO80211BSSBeacon14isOnRSNNetworkEPKhhjjtj
+ __ZThn40_NK16IO80211BSSBeacon20getChanPrimarySWSpecEv
+ __ZThn40_NK16IO80211BSSBeacon7getBandEv
+ __ZThn48_N17IO80211Controller18getACCESSORY_STATEEP23IO80211SkywalkInterfaceP32apple80211_device_accessory_info
+ __ZThn48_N17IO80211Controller18setACCESSORY_STATEEP23IO80211SkywalkInterfaceP32apple80211_device_accessory_info
+ __ZThn48_N17IO80211Controller21getDEVICE_ORIENTATIONEP23IO80211SkywalkInterfaceP29apple80211_device_orientation
+ __ZThn48_N17IO80211Controller21setDEVICE_ORIENTATIONEP23IO80211SkywalkInterfaceP29apple80211_device_orientation
+ __ZThn64_N16AppleBCMWLANCore16getHE_CAPABILITYEP24apple80211_he_capability
+ __ZThn64_N16AppleBCMWLANCore24getP2P_DEVICE_CAPABILITYEP32apple80211_p2p_device_capability
+ __ZThn64_N17IOUserNetworkWLAN15addSteeringRuleE40IOUserNetworkEthernetTrafficSteeringRuleP21IOUserNetworkQueueSetPA16_h
+ __ZThn64_N17IOUserNetworkWLAN17removeLogicalLinkEP24IOUserNetworkLogicalLink
+ __ZThn64_N17IOUserNetworkWLAN18removeSteeringRuleEPh
+ __ZThn64_N28AppleBCMWLANBusInterfacePCIe10readSoCRAMEjP24IOBufferMemoryDescriptoryj
+ __ZThn80_N21IO80211InfraInterface24createLinkQualityMonitorEP11IO80211Peerb
+ __ZThn80_N23IO80211SkywalkInterface12syncDPSStatsEv
+ __ZThn80_N23IO80211SkywalkInterface24createLinkQualityMonitorEP11IO80211Peerb
+ __ZThn96_N21IO80211InfraInterface12setLinkStateE16IO80211LinkStatejbjj
+ __ZThn96_N21IO80211InfraInterface20setLinkStateInternalE16IO80211LinkStatejbjj
+ __ZThn96_N24AppleBCMWLANNANInterface13setMacAddressER10ether_addr
+ __ZThn96_N25AppleBCMWLANInfraProtocol24setWCL_LINK_STATE_UPDATEEP32apple80211_wcl_update_link_state
+ __ZThn96_N28AppleBCMWLANNANDataInterface13setMacAddressER10ether_addr
+ __ZThn96_N28AppleBCMWLANSkywalkInterface13setMacAddressER12mloAddrArray
+ __ZThn96_N30AppleBCMWLANProximityInterface13setMacAddressER10ether_addr
+ __ZThn96_N31AppleBCMWLANLowLatencyInterface13setMacAddressER12mloAddrArray
+ __ZThn96_N33AppleBCMWLANIO80211APSTAInterface13setMacAddressER10ether_addr
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2266
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2266.cold.1
+ ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1183
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.706
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.706.cold.1
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.706.cold.2
+ __block_descriptor_tmp.1186
+ __block_descriptor_tmp.1188
+ __block_descriptor_tmp.1189
+ __block_descriptor_tmp.129
+ __block_descriptor_tmp.1967
+ __block_descriptor_tmp.2264
+ __block_descriptor_tmp.2286
+ __block_descriptor_tmp.2320
+ __block_descriptor_tmp.2646
+ __block_descriptor_tmp.2682
+ __block_descriptor_tmp.549
+ __block_descriptor_tmp.592
+ __block_descriptor_tmp.599
+ __block_descriptor_tmp.673
+ __block_descriptor_tmp.704
+ __block_descriptor_tmp.709
+ __block_descriptor_tmp.723
+ __block_descriptor_tmp.728
+ __block_descriptor_tmp.738
+ __block_descriptor_tmp.739
+ __block_descriptor_tmp.747
+ __block_descriptor_tmp.749
+ __block_descriptor_tmp.801
+ __block_descriptor_tmp.857
+ __block_descriptor_tmp.858
+ __block_descriptor_tmp.867
+ __block_descriptor_tmp.942
+ __block_literal_global.2288
+ __block_literal_global.2322
- _OUTLINED_FUNCTION_133
- _OUTLINED_FUNCTION_146
- _ZN16AppleBCMWLANCore19setWiFiCallPoliciesEP33apple80211_wifiFaceTimeCallStatus.cold.1
- _ZN16AppleBCMWLANCore19setWiFiCallPoliciesEP33apple80211_wifiFaceTimeCallStatus.cold.2
- _ZN16AppleBCMWLANCore20setWIFI_BT_5G_POLICYEP30apple80211_wifi_bt_5g_policy_t.cold.1
- _ZN16AppleBCMWLANCore20setWIFI_BT_5G_POLICYEP30apple80211_wifi_bt_5g_policy_t.cold.2
- _ZN16AppleBCMWLANCore20setWIFI_BT_5G_POLICYEP30apple80211_wifi_bt_5g_policy_t.cold.3
- _ZN16AppleBCMWLANCore20setWIFI_BT_5G_POLICYEP30apple80211_wifi_bt_5g_policy_t.cold.4
- _ZN16AppleBCMWLANCore25cfgRoamPruneRssiThresholdEi.cold.1
- _ZN16AppleBCMWLANCore25cfgRoamPruneRssiThresholdEi.cold.2
- _ZN16AppleBCMWLANCore27configureFigaro5GTDDSupportEb.cold.1
- _ZN16AppleBCMWLANCore46handlePruneThresholdConfigurationAsyncCallbackER9CommandIDiR16CommandRxPayloadPv.cold.1
- _ZN22AppleBCMWLANNetAdapter11setLinkDownEbj.cold.1
- _ZN23AppleBCMWLAN11beAdapter14initWithDriverEP16AppleBCMWLANCore.cold.1
- _ZN23AppleBCMWLAN11beAdapter15isMloConnectionEv.cold.1
- _ZN23AppleBCMWLAN11beAdapter15isMloConnectionEv.cold.2
- _ZN23AppleBCMWLAN11beAdapter15setupJoinConfigEbR10ether_addrb.cold.1
- _ZN23AppleBCMWLANJoinAdapter21abortFirmwareJoinSyncEv.cold.1
- _ZN23AppleBCMWLANPCIeSkywalk24attachTxSubmissionQueuesEP23IO80211SkywalkInterface.cold.4
- _ZN24AppleBCMWLANNANInterface19getNAN_FwCapabilityEv.cold.3
- _ZN28AppleBCMWLANBusInterfacePCIe10readSoCRAMEjP6OSDatayj.cold.1
- _ZN28AppleBCMWLANBusInterfacePCIe10readSoCRAMEjP6OSDatayj.cold.2
- _ZN40AppleBCMWLANPCIeSkywalkTxSubmissionQueue18dequeueInfraPacketEP29AppleBCMWLANPCIeSkywalkPacketb.cold.1
- _ZN40AppleBCMWLANPCIeSkywalkTxSubmissionQueue18dequeueInfraPacketEP29AppleBCMWLANPCIeSkywalkPacketb.cold.2
- __ZL21kLPASRSSIRoamBrackets
- __ZN14IO80211CoreDbg11soiCmdPrintEP24apple80211_debug_commandP17IO80211Controllerj
- __ZN16AppleBCMWLANCore17setWCL_JOIN_ABORTEPv
- __ZN16AppleBCMWLANCore19setWiFiCallPoliciesEP33apple80211_wifiFaceTimeCallStatus
- __ZN16AppleBCMWLANCore20getWIFI_BT_5G_POLICYEP30apple80211_wifi_bt_5g_policy_t
- __ZN16AppleBCMWLANCore20setWIFI_BT_5G_POLICYEP30apple80211_wifi_bt_5g_policy_t
- __ZN16AppleBCMWLANCore25cfgRoamPruneRssiThresholdEi
- __ZN16AppleBCMWLANCore27configureFigaro5GTDDSupportEb
- __ZN16AppleBCMWLANCore46handlePruneThresholdConfigurationAsyncCallbackER9CommandIDiR16CommandRxPayloadPv
- __ZN17IO80211BssManager12setAssocSSIDEPKhy
- __ZN20IO80211NetworkPacket14getInterfaceIDEv
- __ZN20IO80211NetworkPacket14setInterfaceIDEi
- __ZN21IO80211InfraInterface12setLinkStateE16IO80211LinkStatejbj
- __ZN21IO80211InfraInterface20setLinkStateInternalE16IO80211LinkStatejbj
- __ZN21IO80211InfraInterface24createLinkQualityMonitorEP11IO80211PeerP9IOService
- __ZN22AppleBCMWLANNetAdapter11setLinkDownEbj
- __ZN23AppleBCMWLAN11beAdapter15isMloConnectionEv
- __ZN23AppleBCMWLAN11beAdapter15setupJoinConfigEbR10ether_addrb
- __ZN23AppleBCMWLANJoinAdapter21abortFirmwareJoinSyncEv
- __ZN23IO80211SkywalkInterface12setLinkStateE16IO80211LinkStatejbj
- __ZN23IO80211SkywalkInterface24createLinkQualityMonitorEP11IO80211PeerP9IOService
- __ZN23IO80211SkywalkInterface4stopEP9IOService
- __ZN24IOUserNetworkPacketQueue12SetDataQueueEP25IODataQueueDispatchSource
- __ZN25AppleBCMWLANInfraProtocol10set6G_MODEEP18apple80211_6G_mode
- __ZN25AppleBCMWLANInfraProtocol17setWCL_JOIN_ABORTEPv
- __ZN25AppleBCMWLANInfraProtocol20getWIFI_BT_5G_POLICYEP30apple80211_wifi_bt_5g_policy_t
- __ZN25AppleBCMWLANInfraProtocol20setWIFI_BT_5G_POLICYEP30apple80211_wifi_bt_5g_policy_t
- __ZN28AppleBCMWLANBusInterfacePCIe10readSoCRAMEjP6OSDatayj
- __ZN28AppleBCMWLANSkywalkInterface13setMacAddressER10ether_addr
- __ZN31AppleBCMWLANLowLatencyInterface13setMacAddressER10ether_addr
- __ZNK16IO80211BSSBeacon14isOnRSNNetworkEPKhhjjtPbj
- __ZNK16IO80211BSSBeacon21getOWETransChanSWSpecEv
- __ZNK16IO80211BSSBeacon26retrieveRnrBssidSameSsid6GEPhj
- __ZThn112_N25AppleBCMWLANInfraProtocol10set6G_MODEEP18apple80211_6G_mode
- __ZThn112_N25AppleBCMWLANInfraProtocol17setWCL_JOIN_ABORTEPv
- __ZThn112_N25AppleBCMWLANInfraProtocol20getWIFI_BT_5G_POLICYEP30apple80211_wifi_bt_5g_policy_t
- __ZThn112_N25AppleBCMWLANInfraProtocol20setWIFI_BT_5G_POLICYEP30apple80211_wifi_bt_5g_policy_t
- __ZThn112_N25AppleBCMWLANInfraProtocol24setWCL_LINK_STATE_UPDATEEP32apple80211_wcl_update_link_state
- __ZThn128_N25AppleBCMWLANInfraProtocol10set6G_MODEEP18apple80211_6G_mode
- __ZThn128_N25AppleBCMWLANInfraProtocol17setWCL_JOIN_ABORTEPv
- __ZThn128_N25AppleBCMWLANInfraProtocol20getWIFI_BT_5G_POLICYEP30apple80211_wifi_bt_5g_policy_t
- __ZThn128_N25AppleBCMWLANInfraProtocol20setWIFI_BT_5G_POLICYEP30apple80211_wifi_bt_5g_policy_t
- __ZThn128_N25AppleBCMWLANInfraProtocol24setWCL_LINK_STATE_UPDATEEP32apple80211_wcl_update_link_state
- __ZThn40_N24IOUserNetworkPacketQueue12SetDataQueueEP25IODataQueueDispatchSource
- __ZThn40_NK16IO80211BSSBeacon14isOnRSNNetworkEPKhhjjtPbj
- __ZThn40_NK16IO80211BSSBeacon21getOWETransChanSWSpecEv
- __ZThn40_NK16IO80211BSSBeacon26retrieveRnrBssidSameSsid6GEPhj
- __ZThn56_N20IO80211NetworkPacket14getInterfaceIDEv
- __ZThn56_N20IO80211NetworkPacket14setInterfaceIDEi
- __ZThn64_N16AppleBCMWLANCore20getWIFI_BT_5G_POLICYEP30apple80211_wifi_bt_5g_policy_t
- __ZThn64_N16AppleBCMWLANCore20setWIFI_BT_5G_POLICYEP30apple80211_wifi_bt_5g_policy_t
- __ZThn64_N28AppleBCMWLANBusInterfacePCIe10readSoCRAMEjP6OSDatayj
- __ZThn80_N21IO80211InfraInterface12setLinkStateE16IO80211LinkStatejbj
- __ZThn80_N21IO80211InfraInterface24createLinkQualityMonitorEP11IO80211PeerP9IOService
- __ZThn80_N23IO80211SkywalkInterface12setLinkStateE16IO80211LinkStatejbj
- __ZThn80_N23IO80211SkywalkInterface24createLinkQualityMonitorEP11IO80211PeerP9IOService
- __ZThn80_N24AppleBCMWLANNANInterface13setMacAddressER10ether_addr
- __ZThn80_N28AppleBCMWLANNANDataInterface13setMacAddressER10ether_addr
- __ZThn80_N28AppleBCMWLANSkywalkInterface13setMacAddressER10ether_addr
- __ZThn80_N30AppleBCMWLANProximityInterface13setMacAddressER10ether_addr
- __ZThn80_N31AppleBCMWLANLowLatencyInterface13setMacAddressER10ether_addr
- __ZThn80_N33AppleBCMWLANIO80211APSTAInterface13setMacAddressER10ether_addr
- __ZThn96_N21IO80211InfraInterface20setLinkStateInternalE16IO80211LinkStatejbj
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2270
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2270.cold.1
- ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1173
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.702
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.702.cold.1
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.702.cold.2
- __block_descriptor_tmp.1169
- __block_descriptor_tmp.1176
- __block_descriptor_tmp.1178
- __block_descriptor_tmp.130
- __block_descriptor_tmp.1971
- __block_descriptor_tmp.2272
- __block_descriptor_tmp.2290
- __block_descriptor_tmp.2324
- __block_descriptor_tmp.2650
- __block_descriptor_tmp.2686
- __block_descriptor_tmp.547
- __block_descriptor_tmp.590
- __block_descriptor_tmp.597
- __block_descriptor_tmp.672
- __block_descriptor_tmp.700
- __block_descriptor_tmp.705
- __block_descriptor_tmp.719
- __block_descriptor_tmp.724
- __block_descriptor_tmp.731
- __block_descriptor_tmp.734
- __block_descriptor_tmp.743
- __block_descriptor_tmp.745
- __block_descriptor_tmp.804
- __block_descriptor_tmp.853
- __block_descriptor_tmp.854
- __block_descriptor_tmp.863
- __block_descriptor_tmp.945
- __block_literal_global.2292
- __block_literal_global.2326
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1526.62\""
+ "%s: ignoring built-in device because wifibt-external is set\n"
+ "%s: ignoring external device because wifibt-external is not set\n"
+ "%s: wifibt-external %s set\n"
+ "/AppleInternal/Library/BuildRoots/4~B2ABugDkslcChvMwGs2VprQQs5HqnFa0rHHuL4E/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS25.0.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AppleBCMWLANV3_driverkit-1526.62"
+ "BCMWLAN Firmware Rx Stall - V4"
+ "BCMWLAN Firmware Rx Stall V4 - AMPDU Dup"
+ "BCMWLAN Firmware Rx Stall V4 - BCMC Decrypt Fail"
+ "BCMWLAN Firmware Rx Stall V4 - BCMC Decrypt Fail KeyID Mismatch"
+ "BCMWLAN Firmware Rx Stall V4 - Excessive SF in AMSDU"
+ "BCMWLAN Firmware Rx Stall V4 - No Unicast Data after RTS/CTS"
+ "BCMWLAN Firmware Rx Stall V4 - Unicast Decrypt Fail"
+ "BCMWLAN Firmware Rx Stall V4 - Unicast Replay"
+ "BCOM unable to scan any channel on LPSC due to BSP policy"
+ "Boosting"
+ "Debug: WL_NAN_CMD_CFG_SET_PEER_KEY bytestream: "
+ "Debug: WL_NAN_CMD_DATA_DATAREQ bytestream: "
+ "Debug: WL_NAN_CMD_SD_PUBLISH bytestream: "
+ "Logic:\t%u\nData SOI Low:\t%u\nData SOI High:\t%u\nRx Pkt Threshold:\t%u\nTx Pkt Threshold:\t%u\nTx Rx Pkt Threshold:\t%u\nRx Bytes Threshold:\t%u\nTx Bytes Threshold:\t%u\nTx Rx Bytes Threshold:\t%u\n"
+ "May 30 2025 19:23:25"
+ "Restoring"
+ "WLC_E_ADPS"
+ "WLC_E_AIBSS_TXFAIL"
+ "WLC_E_AIRIQ_EVENT"
+ "WLC_E_ALLOW_CREDIT_BORROW"
+ "WLC_E_AMSDU_RX_WAKEUP"
+ "WLC_E_AMT"
+ "WLC_E_AP_BCN_DRIFT"
+ "WLC_E_ASSOC_IND_NDIS"
+ "WLC_E_ASSOC_REQ_IE"
+ "WLC_E_AUTHORIZED"
+ "WLC_E_AUTH_REQ"
+ "WLC_E_AUTH_START"
+ "WLC_E_BCMC_CREDIT_SUPPORT"
+ "WLC_E_BCNRECV_ABORTED"
+ "WLC_E_BCN_TSF"
+ "WLC_E_BEACON_FRAME_RX"
+ "WLC_E_BSSID"
+ "WLC_E_BSSTRANS_RESP"
+ "WLC_E_BSS_LOAD"
+ "WLC_E_C2C"
+ "WLC_E_CSA_DONE_IND"
+ "WLC_E_CSA_FAILURE_IND"
+ "WLC_E_CSA_IGNORED"
+ "WLC_E_CSA_START_IND"
+ "WLC_E_CSI_DATA"
+ "WLC_E_DPSTA_INTF_IND"
+ "WLC_E_EDS_EVENT"
+ "WLC_E_FBT_AUTH_REQ_IND"
+ "WLC_E_GTK_KEYROT_NO_CHANSW"
+ "WLC_E_GTK_PLUMBED"
+ "WLC_E_HTSFSYNC"
+ "WLC_E_IBSS_COALESCE"
+ "WLC_E_ICM"
+ "WLC_E_INVALID_IE"
+ "WLC_E_LEAKY_AP_STATS"
+ "WLC_E_LINK_QUALITY"
+ "WLC_E_MACDBG"
+ "WLC_E_MBO"
+ "WLC_E_MIMO_PWR_SAVE"
+ "WLC_E_MLO_LINK_INFO"
+ "WLC_E_MODE_SWITCH"
+ "WLC_E_MSCH"
+ "WLC_E_NATIVE"
+ "WLC_E_NATOE_NFCT"
+ "WLC_E_OBSS_DETECTION"
+ "WLC_E_OVERLAY_REQ"
+ "WLC_E_OWE_INFO"
+ "WLC_E_P2PO_ADD_DEVICE"
+ "WLC_E_P2PO_DEL_DEVICE"
+ "WLC_E_PEER_TIMEOUT"
+ "WLC_E_PFN_GSCAN_FULL_RESULT"
+ "WLC_E_PFN_PARTIAL_RESULT"
+ "WLC_E_PFN_SCAN_COMPLETE"
+ "WLC_E_PFN_SSID_EXT"
+ "WLC_E_PFN_SWC"
+ "WLC_E_PHY_CAL"
+ "WLC_E_PKTDELAY_IND"
+ "WLC_E_PKT_FILTER"
+ "WLC_E_PRE_ASSOC_RSEP_IND"
+ "WLC_E_PROBREQ_MSG_RX"
+ "WLC_E_PSTA_PRIMARY_INTF_IND"
+ "WLC_E_RADAR_DETECTED"
+ "WLC_E_RANGING_EVENT"
+ "WLC_E_REASSOC_IND_NDIS"
+ "WLC_E_REQUEST_CLM"
+ "WLC_E_RESERVED"
+ "WLC_E_RMC_EVENT"
+ "WLC_E_RM_COMPLETE"
+ "WLC_E_ROAM_EXP_EVENT"
+ "WLC_E_RPSNOA"
+ "WLC_E_RRM"
+ "WLC_E_RSSI_LQM"
+ "WLC_E_RXDMA_RECOVERY_ATMPT"
+ "WLC_E_SBI_SC_EVENT"
+ "WLC_E_SCAN"
+ "WLC_E_SERVICE_FOUND"
+ "WLC_E_SLOTTED_BSS_PEER_OP"
+ "WLC_E_SPEEDY_RECREATE_FAIL"
+ "WLC_E_SPW_TXINHIBIT"
+ "WLC_E_SSID_MITIGATION"
+ "WLC_E_TDLS_PEER_EVENT"
+ "WLC_E_TEMP_THROTTLE"
+ "WLC_E_TWT"
+ "WLC_E_TWT_SETUP"
+ "WLC_E_TXFAIL_THRESH"
+ "WLC_E_ULMU_DISABLED_REASON_UPD"
+ "WLC_E_ULP"
+ "WLC_E_VLPTPC"
+ "WLC_E_WNM_STA_SLEEP"
+ "[dk] %s@%d: %s BE traffic"
+ "[dk] %s@%d: Cannot set wme_ac_sta (BE): ret %x %s\n"
+ "[dk] %s@%d: LTECX TxBlanking --> msg12_rx_cnt = %u, 40m_timeout_cnt = %u, blanked_duration = %u\n"
+ "[dk] %s@%d: Nan-FwCapability XTLV Id=0x%0x XTLV Len:%0x\n "
+ "[dk] %s@%d: Rx RTS CTS Mitigation Enhancement is not supported!\n"
+ "[dk] %s@%d: Set RTS CTS hold down params::t %u tot len %d sub_len %d ver %d len %d prog %d hold_down %d!\n"
+ "[dk] %s@%d: Set adaptive11r (fbt_11r_asr) to %u : %s \n"
+ "[dk] %s@%d: Unable to set RTS CTS hold down params: %s\n"
+ "[dk] %s@%d: Unexpected length %u %u \n"
+ "[dk] %s@%d: applying channel spec for %s||%s channel (%d) infraChan=%d, chanSpec=%d, bcmSpec=0x%x bw=%d\n"
+ "[dk] %s@%d: getMloContext %d [%s] \n"
+ "[dk] %s@%d: requested bandwidth %d and actually bandwidth %d for channel %d\n"
+ "[dk] %s@%d:%s %d Length check failed withreasonCode %d"
+ "[dk] %s@%d:%s::%s adding HE IE \n"
+ "[dk] %s@%d:Allocation subcmd_payload_len for return %d %d \n"
+ "[dk] %s@%d:Buffer overflow detected\n"
+ "[dk] %s@%d:Cannot set PEER_STATS_CONFIG sync state: %s CreatingChipIF %s"
+ "[dk] %s@%d:DPReq-GTK: fNANGTKenable:%d, gtk_required:%d, set SEC_GTK_CSID(5) \n"
+ "[dk] %s@%d:DPReq-legacy: fNANGTKenable:%d gtk_required:%d, cipher_suite_id is %d, Not setting SEC_GTK_CSID \n"
+ "[dk] %s@%d:HMAP is not supported for external device\n"
+ "[dk] %s@%d:HostPairing/enableGTK is enabled: setting NAN config-control-ext for xGTKs\n"
+ "[dk] %s@%d:Mac adress mismatch local %02x:%02x:%02x:%02x:%02x:%02x  packet %02x:%02x:%02x:%02x:%02x:%02x \n"
+ "[dk] %s@%d:Nan host pairing enabled, Chip %u\n"
+ "[dk] %s@%d:Nan-FwCapability Flag1=0x%0x\n "
+ "[dk] %s@%d:Nan-FwCapability Flag1=0x%0x max_svc_publishes:%0x max_svc_subscribes:%0x max_lcl_sched_maps:%0x\n               max_lcl_ndc_entries:%0x max_lcl_ndi_interfaces:%0x max_peer_entries:%0x max_ndp_sessions:%0x, hostpairing:%d\n "
+ "[dk] %s@%d:Processed RX Stall V2\n"
+ "[dk] %s@%d:Processed RX Stall V3\n"
+ "[dk] %s@%d:Processed RX Stall V4\n"
+ "[dk] %s@%d:Publish-GTK: fNANGTKenable:%d, control:%x, set CFG_SEC_GTK_CSID \n"
+ "[dk] %s@%d:Publish-legacy: fNANGTKenable:%d control:%x, dpReq->cipher_suite_id is %d, not setting SEC_GTK_CSID \n"
+ "[dk] %s@%d:Removing NDC availability for id %d"
+ "[dk] %s@%d:Skip setting defualt boost, since we are in the middle of reassoc \n"
+ "[dk] %s@%d:Skiping disable bracket band<%d> bracket<%d> \n"
+ "[dk] %s@%d:cipher_suite_ids (%d)\n"
+ "[dk] %s@%d:cmd is stuck more than diff<%llu> now<%llu> qTime<%llu> \n"
+ "[dk] %s@%d:disbaling nan host pairing, Chip %u\n"
+ "[dk] %s@%d:pBuffer is NULL\n"
+ "[dk] %s@%d:pMemoryDescriptor is NULL\n"
+ "[dk] %s@%d:poorlqmOffset %d activeTrafficOffset %d BtAudioActiveOffset %d useMotionOffset %d useAdaptiveRoamMode %d\n"
+ "built-in"
+ "checkCurrentCmdStuck"
+ "configureAggressiveEDCA"
+ "configureRxHCRTSCTSEventParams"
+ "fbt_11r_asr"
+ "getMloContext"
+ "getNAN_deviceCapability"
+ "is"
+ "is not"
+ "operator()"
+ "setAWDL_RTG_PEER_STATS_CONFIG"
+ "setAdaptive11rFromASR"
+ "soiCmd"
+ "validateMacAddr"
+ "wlan.enableGTK"
+ "wlan.platformconfig.bypasscheck"
+ "wlan.validateMacAddrOption"
- "\"AppleBCMWLANV3_driverkit-1485.4\""
- "%s: status = %lu %s, reason = %lu, flags = 0x%x, authtype = %lu, addr = %02X:%02X:%02X:%02X:%02X:%02X\n"
- "/AppleInternal/Library/BuildRoots/0eecfda0-225e-11f0-a036-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS24.5.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1485.4"
- "Apr 27 2025 18:51:40"
- "[dk] %s@%d: Tearing down link (debounce=%d) debounceTimeout = %d \n"
- "[dk] %s@%d: applying bcm channel spec for %s||%s channel (%d) infraChan=%d, chanSpec=%d, bcmSpec=0x%x\n"
- "[dk] %s@%d: requested bandwidth %d and actually bandwidth %d\n"
- "[dk] %s@%d:Failed to configure Wifi BT 5GHz Full TDD support %d reason %s\n"
- "[dk] %s@%d:Nan-FwCapability Flag1=0x%0x max_svc_publishes:%0x max_svc_subscribes:%0x max_lcl_sched_maps:%0x\n               max_lcl_ndc_entries:%0x max_lcl_ndi_interfaces:%0x max_peer_entries:%0x max_ndp_sessions:%0x\n "
- "[dk] %s@%d:Request to attach, while not connected\n"
- "[dk] %s@%d:Unable to set wifi_bt5g_policy %d: %s\n"
- "[dk] %s@%d:[%s]: Setting WiFi BT 5G Policy to TDD during band-switch \n"
- "[dk] %s@%d:[%s]: Setting WiFi BT 5G Policy to assoc delay for band-switch \n"
- "[dk] %s@%d:[%s]: Setting WiFi BT 5G Policy to full TDD \n"
- "[dk] %s@%d:mlo linked address is %d \n"
- "[dk] %s@%d:useLpasOffset %d useWoWOffset %d poorlqmOffset %d activeTrafficOffset %d BtAudioActiveOffset %d useMotionOffset %d useAdaptiveRoamMode %d\n"
- "[dk] %s@%d:useLpasOffset roam_prof Roam profile[%d], Band[%d]: to FW with lpas offset %d\n"
- "cant create a random mac address after 100 tries"
- "configureFigaro5GTDDSupport"
- "handleReassocEvent"
- "infra_mac"
- "isMloConnection"
- "setWIFI_BT_5G_POLICY"
- "soi"
- "wifi_bt5g_policy"

```
