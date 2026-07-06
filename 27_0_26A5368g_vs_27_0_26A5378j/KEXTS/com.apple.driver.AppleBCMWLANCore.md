## com.apple.driver.AppleBCMWLANCore

> `com.apple.driver.AppleBCMWLANCore`

```diff

   __TEXT.__os_log: 0x73b7
   __TEXT.__const: 0x2b88
-  __TEXT.__cstring: 0x6f8b1
-  __TEXT_EXEC.__text: 0x20fbbc
+  __TEXT.__cstring: 0x6fa5e
+  __TEXT_EXEC.__text: 0x210064
   __TEXT_EXEC.__auth_stubs: 0x1b30
   __DATA.__data: 0x492
   __DATA.__common: 0x478
   __DATA.__bss: 0xde0
   __DATA_CONST.__mod_init_func: 0x208
   __DATA_CONST.__mod_term_func: 0x1f8
-  __DATA_CONST.__const: 0x1f318
+  __DATA_CONST.__const: 0x1f320
   __DATA_CONST.__kalloc_type: 0x4440
   __DATA_CONST.__kalloc_var: 0x230
   __DATA_CONST.__auth_got: 0xd98
   __DATA_CONST.__got: 0x260
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 4341
-  Symbols:   8365
-  CStrings:  11575
+  Functions: 4342
+  Symbols:   8366
+  CStrings:  11582
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ __ZN24AppleBCMWLANNANInterface24setNAN_MULTICAST_PEER_OPEP32apple80211_nan_multicast_peer_op
+ __ZZN16AppleBCMWLANCore10setHeStatsEP6OSData19AppleBCMWLANSliceIdE22kalloc_type_view_16799
+ __ZZN16AppleBCMWLANCore11setOmiStatsEP6OSData19AppleBCMWLANSliceIdE22kalloc_type_view_16998
+ __ZZN16AppleBCMWLANCore15setCurEtheraddrERK10ether_addrE22kalloc_type_view_25541
+ __ZZN16AppleBCMWLANCore15setCurEtheraddrERK10ether_addrE22kalloc_type_view_25557
+ __ZZN16AppleBCMWLANCore17configureLPASModeEjE22kalloc_type_view_51937
+ __ZZN16AppleBCMWLANCore17configureLPASModeEjE22kalloc_type_view_51948
+ __ZZN16AppleBCMWLANCore17handleDynSAREventEP14wl_event_msg_tE22kalloc_type_view_23648
+ __ZZN16AppleBCMWLANCore17handleDynSAREventEP14wl_event_msg_tE22kalloc_type_view_23700
+ __ZZN16AppleBCMWLANCore18configPerPeerStatsEbhhP10ether_addrE22kalloc_type_view_30123
+ __ZZN16AppleBCMWLANCore18configPerPeerStatsEbhhP10ether_addrE22kalloc_type_view_30133
+ __ZZN16AppleBCMWLANCore20parseEventLogRecordsEP6OSDataPjE22kalloc_type_view_21691
+ __ZZN16AppleBCMWLANCore20parseEventLogRecordsEP6OSDataPjE22kalloc_type_view_21757
+ __ZZN16AppleBCMWLANCore20parseEventLogRecordsEP6OSDataPjE22kalloc_type_view_21770
+ __ZZN16AppleBCMWLANCore20parseEventLogRecordsEP6OSDataPjE22kalloc_type_view_21795
+ __ZZN16AppleBCMWLANCore26handleSetLpasAsyncCallBackER9CommandIDiR16CommandRxPayloadPvE22kalloc_type_view_12687
+ __ZZN16AppleBCMWLANCore26setMacAddressAsyncCallbackER9CommandIDiR16CommandRxPayloadPvE21kalloc_type_view_9378
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV2EP6OSDataE22kalloc_type_view_17076
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV2EP6OSDataE22kalloc_type_view_17159
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV3EP6OSDataE22kalloc_type_view_17187
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV3EP6OSDataE22kalloc_type_view_17273
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV4EP6OSDataE22kalloc_type_view_17298
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV4EP6OSDataE22kalloc_type_view_17351
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV6EP6OSDataE22kalloc_type_view_17380
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV6EP6OSDataE22kalloc_type_view_17481
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV7EP6OSDataE22kalloc_type_view_17510
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV7EP6OSDataE22kalloc_type_view_17621
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV9EP6OSDataE22kalloc_type_view_18113
+ __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV9EP6OSDataE22kalloc_type_view_18235
+ __ZZN16AppleBCMWLANCore33parseEventLogRecordBTCoexStatsV11EP6OSDataE22kalloc_type_view_17651
+ __ZZN16AppleBCMWLANCore33parseEventLogRecordBTCoexStatsV11EP6OSDataE22kalloc_type_view_17811
+ __ZZN16AppleBCMWLANCore33parseEventLogRecordBTCoexStatsV12EP6OSDataE22kalloc_type_view_17844
+ __ZZN16AppleBCMWLANCore33parseEventLogRecordBTCoexStatsV12EP6OSDataE22kalloc_type_view_18081
+ __ZZN16AppleBCMWLANCore34handlePeerStatsConfigAsyncCallbackER9CommandIDiR16CommandRxPayloadPvE22kalloc_type_view_29969
+ __ZZN16AppleBCMWLANCore36convertwlMgmtCntToAppleFrameCountersEP16wl_ctl_mgt_cnt_tP25apple80211_frame_countersE22kalloc_type_view_29054
+ __ZZN16AppleBCMWLANCore36convertwlMgmtCntToAppleFrameCountersEP16wl_ctl_mgt_cnt_tP25apple80211_frame_countersE22kalloc_type_view_29108
+ __ZZN16AppleBCMWLANCore47parseEventLogRecordControlManagementFrameCountsEP6OSDataE22kalloc_type_view_21187
+ __ZZN16AppleBCMWLANCore47parseEventLogRecordControlManagementFrameCountsEP6OSDataE22kalloc_type_view_21222
+ __ZZN30AppleBCMWLANCoreFirmwareLoader16initWithProviderEP9IOServiceE22kalloc_type_view_61827
+ __ZZN30AppleBCMWLANCoreFirmwareLoader4freeEvE22kalloc_type_view_61915
- __ZZN16AppleBCMWLANCore10setHeStatsEP6OSData19AppleBCMWLANSliceIdE22kalloc_type_view_16798
- __ZZN16AppleBCMWLANCore11setOmiStatsEP6OSData19AppleBCMWLANSliceIdE22kalloc_type_view_16997
- __ZZN16AppleBCMWLANCore15setCurEtheraddrERK10ether_addrE22kalloc_type_view_25540
- __ZZN16AppleBCMWLANCore15setCurEtheraddrERK10ether_addrE22kalloc_type_view_25556
- __ZZN16AppleBCMWLANCore17configureLPASModeEjE22kalloc_type_view_51936
- __ZZN16AppleBCMWLANCore17configureLPASModeEjE22kalloc_type_view_51947
- __ZZN16AppleBCMWLANCore17handleDynSAREventEP14wl_event_msg_tE22kalloc_type_view_23647
- __ZZN16AppleBCMWLANCore17handleDynSAREventEP14wl_event_msg_tE22kalloc_type_view_23699
- __ZZN16AppleBCMWLANCore18configPerPeerStatsEbhhP10ether_addrE22kalloc_type_view_30122
- __ZZN16AppleBCMWLANCore18configPerPeerStatsEbhhP10ether_addrE22kalloc_type_view_30132
- __ZZN16AppleBCMWLANCore20parseEventLogRecordsEP6OSDataPjE22kalloc_type_view_21690
- __ZZN16AppleBCMWLANCore20parseEventLogRecordsEP6OSDataPjE22kalloc_type_view_21756
- __ZZN16AppleBCMWLANCore20parseEventLogRecordsEP6OSDataPjE22kalloc_type_view_21769
- __ZZN16AppleBCMWLANCore20parseEventLogRecordsEP6OSDataPjE22kalloc_type_view_21794
- __ZZN16AppleBCMWLANCore26handleSetLpasAsyncCallBackER9CommandIDiR16CommandRxPayloadPvE22kalloc_type_view_12686
- __ZZN16AppleBCMWLANCore26setMacAddressAsyncCallbackER9CommandIDiR16CommandRxPayloadPvE21kalloc_type_view_9377
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV2EP6OSDataE22kalloc_type_view_17075
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV2EP6OSDataE22kalloc_type_view_17158
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV3EP6OSDataE22kalloc_type_view_17186
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV3EP6OSDataE22kalloc_type_view_17272
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV4EP6OSDataE22kalloc_type_view_17297
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV4EP6OSDataE22kalloc_type_view_17350
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV6EP6OSDataE22kalloc_type_view_17379
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV6EP6OSDataE22kalloc_type_view_17480
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV7EP6OSDataE22kalloc_type_view_17509
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV7EP6OSDataE22kalloc_type_view_17620
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV9EP6OSDataE22kalloc_type_view_18112
- __ZZN16AppleBCMWLANCore32parseEventLogRecordBTCoexStatsV9EP6OSDataE22kalloc_type_view_18234
- __ZZN16AppleBCMWLANCore33parseEventLogRecordBTCoexStatsV11EP6OSDataE22kalloc_type_view_17650
- __ZZN16AppleBCMWLANCore33parseEventLogRecordBTCoexStatsV11EP6OSDataE22kalloc_type_view_17810
- __ZZN16AppleBCMWLANCore33parseEventLogRecordBTCoexStatsV12EP6OSDataE22kalloc_type_view_17843
- __ZZN16AppleBCMWLANCore33parseEventLogRecordBTCoexStatsV12EP6OSDataE22kalloc_type_view_18080
- __ZZN16AppleBCMWLANCore34handlePeerStatsConfigAsyncCallbackER9CommandIDiR16CommandRxPayloadPvE22kalloc_type_view_29968
- __ZZN16AppleBCMWLANCore36convertwlMgmtCntToAppleFrameCountersEP16wl_ctl_mgt_cnt_tP25apple80211_frame_countersE22kalloc_type_view_29053
- __ZZN16AppleBCMWLANCore36convertwlMgmtCntToAppleFrameCountersEP16wl_ctl_mgt_cnt_tP25apple80211_frame_countersE22kalloc_type_view_29107
- __ZZN16AppleBCMWLANCore47parseEventLogRecordControlManagementFrameCountsEP6OSDataE22kalloc_type_view_21186
- __ZZN16AppleBCMWLANCore47parseEventLogRecordControlManagementFrameCountsEP6OSDataE22kalloc_type_view_21221
- __ZZN30AppleBCMWLANCoreFirmwareLoader16initWithProviderEP9IOServiceE22kalloc_type_view_61820
- __ZZN30AppleBCMWLANCoreFirmwareLoader4freeEvE22kalloc_type_view_61908
Functions:
~ __ZN23AppleBCMWLANRoamAdapter21getRoamProfilePerBandEP33apple80211_roam_profile_band_dataj : 2812 -> 2856
~ __ZN28AppleBCMWLANKeepAliveOffload20createKeepAliveFrameEPhjjttjjtRtS1_ : 680 -> 664
~ __ZN23AppleBCMWLANJoinAdapter11performJoinEP25apple80211AssocCandidates : 8000 -> 8044
~ __ZN23AppleBCMWLANJoinAdapter10handleAuthEP14wl_event_msg_t : 1080 -> 1064
~ __ZN23AppleBCMWLANJoinAdapter11handleAssocEP14wl_event_msg_t : 1060 -> 1036
~ __ZN23AppleBCMWLANJoinAdapter13handleSetSSIDEP14wl_event_msg_t : 1420 -> 1412
~ __ZN23AppleBCMWLANJoinAdapter21handleSupplicantEventEP14wl_event_msg_t : 944 -> 928
~ __ZN20AppleBCMWLANItemRing11hexDumpRingEv : 700 -> 720
~ __ZN26AppleBCMWLANTimeSyncEngine17freeTimestampTxIOEP13IO80211Buffer : 212 -> 200
~ __ZN26AppleBCMWLANTimeSyncEngine30processFirmwareTimeSyncMessageEytPKht : 3652 -> 3672
~ __ZN26AppleBCMWLANTimeSyncEngine17findTimestampTxIOEv : 224 -> 204
~ __ZN24AppleBCMWLANPowerManager41setMWSCoexIoVarsAsync_mws_ocl_coex_bitmapEP8OSObjectb : 1824 -> 1828
~ __ZN19AppleBCMWLANCommand7prepareERK9CommandIDtRK16CommandTxPayloadP16CommandRxPayloadRK17CommandRxExpectedRK17CommandCompletion20CommandBusPreference : 700 -> 708
~ __ZN24AppleBCMWLANBusInterface16stringFromReturnEi : 168 -> 176
~ __ZN24AppleBCMWLANBusInterface15errnoFromReturnEi : 200 -> 208
~ __ZN27AppleBCMWLANIOReportingCore24incrementEventLogCounterEhl : 1288 -> 1336
~ __ZN27AppleBCMWLANIOReportingCore17reportEventLogSetEht : 1096 -> 1128
~ __ZN27AppleBCMWLANIOReportingCore21reportEventLogSetSizeEht : 684 -> 700
~ __ZN16AppleBCMWLANCore19handleChanInfoTimerEP18IO80211TimerSource : 5240 -> 5228
~ __ZN16AppleBCMWLANCore21retrievePlatcfgStatusEv : 1704 -> 1692
~ __ZN16AppleBCMWLANCore27retrievePlatcfgXTLVDumpDataEv : 2340 -> 2332
~ __ZN16AppleBCMWLANCore27configureDefaultCountryCodeEv : 2288 -> 2300
~ __ZN16AppleBCMWLANCore20configureIeFilteringEv : 472 -> 476
~ __ZN16AppleBCMWLANCore13setPropertiesEP8OSObject : 29756 -> 29764
~ __ZN16AppleBCMWLANCore20handleRxStallReasonsEP20bcm_dngl_healthcheckRiS2_Ph : 2928 -> 2944
~ __ZN16AppleBCMWLANCore18handleRangingEventEP14wl_event_msg_t : 12044 -> 12004
~ __ZN16AppleBCMWLANCore13printRoamInfoEj : 3184 -> 3192
~ __ZN16AppleBCMWLANCore18parsePHYEcounterV3EP6OSData : 2068 -> 2064
~ __ZN16AppleBCMWLANCore18parsePHYEcounterV4EP6OSData : 2300 -> 2296
~ __ZN16AppleBCMWLANCore21parsePHYCalEcounterV1EP6OSData : 1716 -> 1712
~ __ZN16AppleBCMWLANCore28configureWeightAvgLQMUpdatesEPK20wl_wa_basic_params_t : 1068 -> 1060
~ __ZN16AppleBCMWLANCore22getNANDataMacAddressesEP10ether_addrPh : 684 -> 668
~ __ZN16AppleBCMWLANCore12get6GTxPowerEth : 372 -> 352
~ __ZN16AppleBCMWLANCore11getChanSpecEhjP10Bandwidths : 220 -> 236
~ __Z16stringFromReasonjj : 184 -> 188
~ __Z23stringFromStatusInEventjj : 896 -> 900
~ __ZN25AppleBCMWLANBGScanAdapter24setWCL_CONFIG_BG_NETWORKEP21apple80211_bg_network : 2188 -> 2176
~ __ZN31AppleBCMWLANProvisioningManager34generateProvisionedNVRAMParametersEP13IO80211BufferR6RangesPv : 5720 -> 5728
~ __ZN25AppleBCMWLANConfigManager16setBTCParametersEv : 676 -> 644
~ __ZN26AppleBCMWLANTxPowerManager24getDynSARPwrBoostPerRSSIEi : 104 -> 96
~ __ZN19AppleBCMWLANCoreDbg20cmdDumpTxPwrCapDebugEP24apple80211_debug_commandP16AppleBCMWLANCore : 4920 -> 4892
~ __ZN19AppleBCMWLANCoreDbg14cmdGetRoamInfoEP24apple80211_debug_commandP16AppleBCMWLANCore : 768 -> 772
~ __ZN33AppleBCMWLANIO80211APSTAInterface11handleEventEP14wl_event_msg_t : 9356 -> 9340
~ __ZN33AppleBCMWLANIO80211APSTAInterface18updateSTAAssocInfoEP14wl_event_msg_t : 1240 -> 1236
~ __ZN30AppleBCMWLANProximityInterface24buildChanSequenceCommandEP37apple80211_awdl_sync_channel_sequenceP37apple80211_nan_committed_availability : 4364 -> 4388
~ __ZN21AppleBCMWLANCommander12issueCommandERK9CommandIDRK16CommandTxPayloadP16CommandRxPayloadRK17CommandRxExpectedRK17CommandCompletion20CommandBusPreference : 6608 -> 6616
~ __ZN24AppleBCMWLANNANInterface14getHP2P_PARAMSEPvih : 2148 -> 2156
+ __ZN24AppleBCMWLANNANInterface24setNAN_MULTICAST_PEER_OPEP32apple80211_nan_multicast_peer_op
CStrings:
+ "\"AppleBCMWLANV3_Drivers-1570.56\""
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwZAAu/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLAN11beAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwZAAu/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANBSSBeacon.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwZAAu/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANBssManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwZAAu/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCommandMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwZAAu/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCommander.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwZAAu/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCore.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwZAAu/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCoreDbg.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwZAAu/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANIOReportingPerSlice.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwZAAu/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANJoinAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwZAAu/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANLQM.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwZAAu/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANNANInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwZAAu/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANPowerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwZAAu/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANProximityInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwZAAu/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANScanAdapter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwZAAu/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANTimeSyncEngine.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwZAAu/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANTxPowerManager.cpp"
+ "AppleBCMWLANV3_Drivers-1570.56"
+ "Debug: WL_NAN_CMD_CFG_SET_PEER_KEY (mcast_peer) bytestream: "
+ "Jun 29 2026 23:27:48"
+ "[ik] %s@%d:%s invalid operation %u\n"
+ "[ik] %s@%d:%s invalid peer count %u\n"
+ "[ik] %s@%d:%s: op=%u count=%u laddr=%02x:%02x:%02x:%02x:%02x:%02x mcast=%02x:%02x:%02x:%02x:%02x:%02x\n"
+ "[ik] %s@%d:ERROR: Unable to set NAN multicast peer, ret = %d\n"
+ "setNAN_MULTICAST_PEER_OP"
+ "virtual int32_t AppleBCMWLANNANInterface::setNAN_MULTICAST_PEER_OP(apple80211_nan_multicast_peer_op_t *)"
- "\"AppleBCMWLANV3_Drivers-1570.51\""
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HLJz9Q/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLAN11beAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HLJz9Q/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANBSSBeacon.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HLJz9Q/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANBssManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HLJz9Q/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCommandMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HLJz9Q/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCommander.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HLJz9Q/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCore.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HLJz9Q/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANCoreDbg.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HLJz9Q/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANIOReportingPerSlice.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HLJz9Q/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANJoinAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HLJz9Q/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANLQM.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HLJz9Q/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANNANInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HLJz9Q/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANPowerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HLJz9Q/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANProximityInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HLJz9Q/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANScanAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HLJz9Q/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANTimeSyncEngine.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HLJz9Q/Sources/AppleBCMWLANV3_Drivers/AppleBCMWLANTxPowerManager.cpp"
- "AppleBCMWLANV3_Drivers-1570.51"
- "Jun 15 2026 22:21:11"

```
