## com.apple.DriverKit-AppleBCMWLAN

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleBCMWLAN.dext/com.apple.DriverKit-AppleBCMWLAN`

```diff

-1153.8.3.1.0
-  __TEXT.__text: 0x259f00
+1160.11.0.0.0
+  __TEXT.__text: 0x25c7dc
   __TEXT.__auth_stubs: 0x2d80
   __TEXT.__init_offsets: 0x1d4
-  __TEXT.__cstring: 0x84f83
-  __TEXT.__const: 0x66520
-  __TEXT.__oslogstring: 0x31cc
-  __TEXT.__unwind_info: 0x3cbc
+  __TEXT.__cstring: 0x85d5e
+  __TEXT.__const: 0x723a0
+  __TEXT.__oslogstring: 0x34c5
+  __TEXT.__unwind_info: 0x3cf4
   __DATA_CONST.__auth_got: 0x16c0
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x21b98
+  __DATA_CONST.__const: 0x21c90
   __DATA_CONST.__osclassinfo: 0x398
-  __DATA.__data: 0x710
+  __DATA.__data: 0x720
   __DATA.__bss: 0x950
   __DATA.__common: 0x398
   - /System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit

   - /System/DriverKit/System/Library/PrivateFrameworks/OLYHALDriverKit.framework/OLYHALDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
   - @rpath/BroadcomWLANDriverKit.framework/BroadcomWLANDriverKit
-  UUID: 8CEBECC0-7E8F-3B47-B5BA-CB97687F3EA5
-  Functions: 7520
-  Symbols:   10369
-  CStrings:  13340
+  UUID: 6305B833-C7A6-3289-8FE6-8258A970BB01
+  Functions: 7545
+  Symbols:   10396
+  CStrings:  13396
 
Symbols:
+ _IOMallocZeroTyped
+ __Block_byref_object_copy_.193
+ __Block_byref_object_copy_.290
+ __Block_byref_object_dispose_.194
+ __Block_byref_object_dispose_.291
+ __ZN15AppleBCMWLANLQM28setInfraSpecificStatsVersionEt
+ __ZN15AppleBCMWLANLQM36updateInfraMuticastBroadcastDurationEP31apple80211_power_debug_sub_info
+ __ZN16AppleBCMWLANCore10is4387C2UpEv
+ __ZN16AppleBCMWLANCore14getCCResetTimeEv
+ __ZN16AppleBCMWLANCore14isChannelValidEh5Bands
+ __ZN16AppleBCMWLANCore14setCCResetTimeEy
+ __ZN16AppleBCMWLANCore20handleRxStallReasonsEP20bcm_dngl_healthcheckRiS2_Ph
+ __ZN16AppleBCMWLANCore26updateRC1CoexStatsReportV4EP6OSData
+ __ZN16AppleBCMWLANCore26updateRC1CoexStatsReportV5EP6OSData
+ __ZN16AppleBCMWLANCore28parseEventLogRecordKvrReportEP6OSData
+ __ZN21IO80211InfraInterface26setInfraSpecificFrameStatsEP22apple80211_stat_reportP31apple80211_infra_specific_stats
+ __ZN22AppleBCMWLANNetManager18triggerCoreCaptureEP14ManagementInfo
+ __ZN23IO80211VirtualInterface26setInfraSpecificFrameStatsEP22apple80211_stat_reportP31apple80211_infra_specific_stats
+ __ZN27IO80211NeighborCacheManager13addHotChannelER18AppleChannelSpec_t
+ __ZN28AppleBCMWLANBusInterfacePCIe16notifyDriverFailEv
+ __ZN32AppleBCMWLANNeighborCacheManager18isChannelSpecValidER18AppleChannelSpec_t
+ __ZNK16IO80211BSSBeacon26retrieveRnrBssidSameSsid6GEPhj
+ __ZNK19IO80211BufferCursor6asTypeI24wl_roam_11kvr_dms_req_v1EEN7libkern11bounded_ptrIKT_N9os_detail21panic_trapping_policyEEEmm
+ __ZNK19IO80211BufferCursor6asTypeI25wl_roam_11kvr_dms_resp_v1EEN7libkern11bounded_ptrIKT_N9os_detail21panic_trapping_policyEEEmm
+ __ZNK19IO80211BufferCursor6asTypeI28wl_roam_11kvr_bcn_rpt_req_v1EEN7libkern11bounded_ptrIKT_N9os_detail21panic_trapping_policyEEEmm
+ __ZNK19IO80211BufferCursor6asTypeI28wl_roam_11kvr_nbr_rpt_req_v1EEN7libkern11bounded_ptrIKT_N9os_detail21panic_trapping_policyEEEmm
+ __ZNK19IO80211BufferCursor6asTypeI29wl_roam_11kvr_bcn_rpt_resp_v1EEN7libkern11bounded_ptrIKT_N9os_detail21panic_trapping_policyEEEmm
+ __ZNK19IO80211BufferCursor6asTypeI29wl_roam_11kvr_nbr_rpt_resp_v1EEN7libkern11bounded_ptrIKT_N9os_detail21panic_trapping_policyEEEmm
+ __ZNK19IO80211BufferCursor6asTypeIjEEN7libkern11bounded_ptrIKT_N9os_detail21panic_trapping_policyEEEmm
+ __ZNK19IO80211BufferCursor7_asTypeI24wl_roam_11kvr_dms_req_v1EEN7libkern11bounded_ptrIT_N9os_detail21panic_trapping_policyEEEmm
+ __ZNK19IO80211BufferCursor7_asTypeI25wl_roam_11kvr_dms_resp_v1EEN7libkern11bounded_ptrIT_N9os_detail21panic_trapping_policyEEEmm
+ __ZNK19IO80211BufferCursor7_asTypeI28wl_roam_11kvr_bcn_rpt_req_v1EEN7libkern11bounded_ptrIT_N9os_detail21panic_trapping_policyEEEmm
+ __ZNK19IO80211BufferCursor7_asTypeI28wl_roam_11kvr_nbr_rpt_req_v1EEN7libkern11bounded_ptrIT_N9os_detail21panic_trapping_policyEEEmm
+ __ZNK19IO80211BufferCursor7_asTypeI29wl_roam_11kvr_bcn_rpt_resp_v1EEN7libkern11bounded_ptrIT_N9os_detail21panic_trapping_policyEEEmm
+ __ZNK19IO80211BufferCursor7_asTypeI29wl_roam_11kvr_nbr_rpt_resp_v1EEN7libkern11bounded_ptrIT_N9os_detail21panic_trapping_policyEEEmm
+ __ZNK19IO80211BufferCursor7_asTypeIjEEN7libkern11bounded_ptrIT_N9os_detail21panic_trapping_policyEEEmm
+ __ZThn40_N32AppleBCMWLANNeighborCacheManager18isChannelSpecValidER18AppleChannelSpec_t
+ __ZThn40_NK16IO80211BSSBeacon26retrieveRnrBssidSameSsid6GEPhj
+ __ZThn48_N28AppleBCMWLANBusInterfacePCIe16notifyDriverFailEv
+ __ZThn80_N21IO80211InfraInterface26setInfraSpecificFrameStatsEP22apple80211_stat_reportP31apple80211_infra_specific_stats
+ __ZThn80_N23IO80211VirtualInterface26setInfraSpecificFrameStatsEP22apple80211_stat_reportP31apple80211_infra_specific_stats
+ __ZZN16AppleBCMWLANCore13setRESET_CHIPEP24apple80211_reset_commandE7allowWD
+ __ZZN16AppleBCMWLANCore13setRESET_CHIPEP24apple80211_reset_commandE7checked
+ ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2524
+ ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1049
+ ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.656
+ ____ZN16AppleBCMWLANCore13setupFirmwareEPK21AppleBCMWLANChipImage_block_invoke
+ __block_descriptor_tmp.1045
+ __block_descriptor_tmp.1052
+ __block_descriptor_tmp.1054
+ __block_descriptor_tmp.1055
+ __block_descriptor_tmp.1089
+ __block_descriptor_tmp.124
+ __block_descriptor_tmp.127
+ __block_descriptor_tmp.133
+ __block_descriptor_tmp.143
+ __block_descriptor_tmp.1619
+ __block_descriptor_tmp.1852
+ __block_descriptor_tmp.189
+ __block_descriptor_tmp.203
+ __block_descriptor_tmp.2147
+ __block_descriptor_tmp.235
+ __block_descriptor_tmp.252
+ __block_descriptor_tmp.2522
+ __block_descriptor_tmp.2526
+ __block_descriptor_tmp.2543
+ __block_descriptor_tmp.2577
+ __block_descriptor_tmp.292
+ __block_descriptor_tmp.2941
+ __block_descriptor_tmp.308
+ __block_descriptor_tmp.3491
+ __block_descriptor_tmp.356
+ __block_descriptor_tmp.3573
+ __block_descriptor_tmp.358
+ __block_descriptor_tmp.3585
+ __block_descriptor_tmp.3587
+ __block_descriptor_tmp.3590
+ __block_descriptor_tmp.3596
+ __block_descriptor_tmp.3615
+ __block_descriptor_tmp.50
+ __block_descriptor_tmp.503
+ __block_descriptor_tmp.545
+ __block_descriptor_tmp.552
+ __block_descriptor_tmp.654
+ __block_descriptor_tmp.656
+ __block_descriptor_tmp.659
+ __block_descriptor_tmp.673
+ __block_descriptor_tmp.678
+ __block_descriptor_tmp.688
+ __block_descriptor_tmp.689
+ __block_descriptor_tmp.697
+ __block_descriptor_tmp.699
+ __block_descriptor_tmp.797
+ __block_descriptor_tmp.804
+ __block_descriptor_tmp.805
+ __block_descriptor_tmp.814
+ __block_literal_global.2545
+ __block_literal_global.2579
- _IOMallocZero
- __Block_byref_object_copy_.191
- __Block_byref_object_copy_.288
- __Block_byref_object_dispose_.192
- __Block_byref_object_dispose_.289
- __ZN15AppleBCMWLANLQM22getRxDurationBroadcastEv
- __ZN15AppleBCMWLANLQM22getRxDurationMulticastEv
- __ZN15AppleBCMWLANLQM28getInfraSpecificStatsVersionEv
- __ZN15AppleBCMWLANLQM28setInfraSpecificStatsVersionEj
- __ZN15AppleBCMWLANLQM36updateInfraMuticastBroadcastDurationEv
- __ZN16AppleBCMWLANCore8is4387C2Ev
- __ZN16AppleBCMWLANCore8is4388C0Ev
- __ZN26AppleBCMWLANTxPowerManager18dumpDynSARStatusV1EP13wl_dynsar_ioc
- __ZN26AppleBCMWLANTxPowerManager18dumpDynSARStatusV2EP13wl_dynsar_ioc
- __ZN27IO80211NeighborCacheManager13addHotChannelEP18AppleChannelSpec_t
- __ZNK16IO80211BSSBeacon33retrieveColocatedRnrBssidSameSsidEPhj
- __ZNK16IO80211BSSBeacon36retrieveNonColocatedRnrBssidSameSsidEPhj
- __ZThn40_NK16IO80211BSSBeacon33retrieveColocatedRnrBssidSameSsidEPhj
- __ZThn40_NK16IO80211BSSBeacon36retrieveNonColocatedRnrBssidSameSsidEPhj
- ___ZN16AppleBCMWLANCore18SetPowerState_ImplEj_block_invoke.2490
- ___ZN28AppleBCMWLANBusInterfacePCIe10Start_ImplEP9IOService_block_invoke.1045
- ___ZN28AppleBCMWLANBusInterfacePCIe18SetPowerState_ImplEj_block_invoke.652
- __block_descriptor_tmp.1041
- __block_descriptor_tmp.1048
- __block_descriptor_tmp.1050
- __block_descriptor_tmp.1051
- __block_descriptor_tmp.1088
- __block_descriptor_tmp.121
- __block_descriptor_tmp.123
- __block_descriptor_tmp.129
- __block_descriptor_tmp.139
- __block_descriptor_tmp.1586
- __block_descriptor_tmp.1819
- __block_descriptor_tmp.187
- __block_descriptor_tmp.201
- __block_descriptor_tmp.2114
- __block_descriptor_tmp.231
- __block_descriptor_tmp.2488
- __block_descriptor_tmp.2492
- __block_descriptor_tmp.250
- __block_descriptor_tmp.2509
- __block_descriptor_tmp.2541
- __block_descriptor_tmp.2869
- __block_descriptor_tmp.290
- __block_descriptor_tmp.304
- __block_descriptor_tmp.3455
- __block_descriptor_tmp.352
- __block_descriptor_tmp.3537
- __block_descriptor_tmp.354
- __block_descriptor_tmp.3549
- __block_descriptor_tmp.3551
- __block_descriptor_tmp.3554
- __block_descriptor_tmp.3560
- __block_descriptor_tmp.3579
- __block_descriptor_tmp.49
- __block_descriptor_tmp.499
- __block_descriptor_tmp.541
- __block_descriptor_tmp.548
- __block_descriptor_tmp.650
- __block_descriptor_tmp.655
- __block_descriptor_tmp.669
- __block_descriptor_tmp.674
- __block_descriptor_tmp.681
- __block_descriptor_tmp.684
- __block_descriptor_tmp.693
- __block_descriptor_tmp.695
- __block_descriptor_tmp.796
- __block_descriptor_tmp.800
- __block_descriptor_tmp.801
- __block_descriptor_tmp.810
- __block_literal_global.2543
CStrings:
+ "\"AppleBCMWLANV3_driverkit-1160.11\""
+ "%c [dk] %s@%d: %s LQM-WiFi-Roam-kvr: kvr Report unknown type\n"
+ "%c [dk] %s@%d: LQM-WiFi-Roam-kvr: dms_req: token=%u \n"
+ "%c [dk] %s@%d: LQM-WiFi-Roam-kvr: dms_rsp: token=%u \n"
+ "%c [dk] %s@%d: LQM-WiFi-Roam-kvr: kvrPayloadBcnRptReq: operating_class=%u requesting_channel_number=%u bcn_mode=%u bssid_hi=%u bssid_lo=%u duration=%u channel_num=%u bcm_chanspec=0x%x \n"
+ "%c [dk] %s@%d: LQM-WiFi-Roam-kvr: kvrPayloadBcnRptRsp:  index_of_AP_in_report=%u num_aps=%u meas_mode=%u bssid_hi=%u bssid_lo=%u ssid_match=%u bcm_chanspec=0x%x rssi=%d snr=%d \n"
+ "%c [dk] %s@%d: LQM-WiFi-Roam-kvr: nbr_report_req: token=%u \n"
+ "%c [dk] %s@%d: LQM-WiFi-Roam-kvr: nbr_report_rsp:  channel_num=%u bcm_chanspec=0x%x \n"
+ "%c [dk] %s@%d: LQM-WiFi-Roam-kvr:Type: %d\n"
+ "%c [dk] %s@%d: Payload too large %ld"
+ "/AppleInternal/Library/BuildRoots/ce7a2ab7-ccb4-11ee-8860-1e1d6dc629d0/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS23.4.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
+ "AdjustBusy(-1), busystate %u, fAdjustBusyCnt %u\n"
+ "AppleBCMWLANV3_driverkit-1160.11"
+ "BCMWLAN Firmware Rx Stall - V3"
+ "BCMWLAN Firmware Rx Stall V3 - No Unicast Data after RTS/CTS"
+ "Feb 16 2024 20:56:36"
+ "RC1 Coex Stats4: Mode=%u, Request=%u RC1Duration=%uus RC1DutyCycle=%u RC1MaxDuration=%u WlanCritCnt=%u WlanCritDur=%u WlanCritMaxDur=%u WlanCritEvtBitmap=0x%x WlanCritMaxEvtType=%u DataStall=%u RC1DenyDS=%u RC1DenyDurDS=%u SucRR=%u\n"
+ "RC1 Coex Stats4: StuckCnt=%u [%llums]\n"
+ "RC1 Coex Stats5: Mode=%u, Request=%u RC1Duration=%uus RC1DutyCycle=%u RC1MaxDuration=%u WlanCritCnt=%u WlanCritDur=%u WlanCritMaxDur=%u,WlanCritEvtBitmap=0x%x WlanCritMaxEvtType=%u DataStall=%u RC1DenyDS=%u RC1DenyDurDS=%u SucRR=%u\n"
+ "RC1 Coex Stats5: NewRequest=%u NewRC1Duration=%uus NewRC1DutyCycle=%u NewRC1MaxDuration=%u rc1_msg73_cnt=%u rc1_last_msg73_pl[0]=%u rc1_last_msg73_pl[1]=%u rc1_last_msg73_pl[2]=0x%x rc1_last_msg73_pl[3]=%u rc1_last_msg73_pl[4]=%u StuckCnt=%u [%llums]\n"
+ "Reason code=%u"
+ "Tag kvr Report"
+ "[dk] %s@%d:%s LQM-WiFi-Roam-kvr: kvr Report unknown type\n"
+ "[dk] %s@%d:Aborting scan while previous abort is not completed. return busy.\n"
+ "[dk] %s@%d:AdjustBusy(-1), busystate %u, fAdjustBusyCnt %u\n"
+ "[dk] %s@%d:For current session updated fRxDurMulticast %d, fRxDurBroadcast %d \n"
+ "[dk] %s@%d:HC currentTime %llu is less than resetTime %llu\n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: Invalid kvrCursor IO80211BufferCursor\n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: NULL payload\n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: Unhandled WLC_FBT_ODS_REQ. Phase 2\n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: Unhandled WLC_FBT_ODS_RESP. Phase 2\n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: dms_req: token=%u \n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: dms_rsp: token=%u \n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: kvrPayloadBcnRptReq: operating_class=%u requesting_channel_number=%u bcn_mode=%u bssid_hi=%u bssid_lo=%u duration=%u channel_num=%u bcm_chanspec=0x%x \n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: kvrPayloadBcnRptRsp:  index_of_AP_in_report=%u num_aps=%u meas_mode=%u bssid_hi=%u bssid_lo=%u ssid_match=%u bcm_chanspec=0x%x rssi=%d snr=%d \n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: nbr_report_req: token=%u \n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: nbr_report_rsp:  channel_num=%u bcm_chanspec=0x%x \n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: not enough space for the kvr type payoad. length is %ld\n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: not enough space for the wl_roam_11kvr_bcn_rpt_req_v1 payload. length is %ld\n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: not enough space for the wl_roam_11kvr_bcn_rpt_resp_v1 payload. length is %ld\n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: not enough space for the wl_roam_11kvr_dms_req_v1 payload. length is %ld\n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: not enough space for the wl_roam_11kvr_dms_resp_v1 payload. length is %ld\n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: not enough space for the wl_roam_11kvr_nbr_rpt_req_v1 payload. length is %ld\n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr: not enough space for the wl_roam_11kvr_nbr_rpt_resp_v1 payload. length is %ld\n"
+ "[dk] %s@%d:LQM-WiFi-Roam-kvr:Type: %d\n"
+ "[dk] %s@%d:Not Seting link up waiting for way done, isJoining<%d> EncryptionMode<%d>\n"
+ "[dk] %s@%d:Payload too large %ld"
+ "[dk] %s@%d:Rx Stall Reason Code %s- NumPkts Considered=%u, NumPkts Dropped=%u, Alert Threshold=%u\n"
+ "[dk] %s@%d:busystate %u, fAdjustBusyCnt %u\n"
+ "[dk] %s@%d:ivars->getPrimaryInterfaceId->setInfraSpecificFrameStats failed\n"
+ "[dk] %s@%d:parseEventLogRecordKvrReport failed\n"
+ "[dk] %s@%d:sizeof(rc1CoexStatsV4) %ld payload->getLength() %d\n"
+ "[dk] %s@%d:sizeof(rc1CoexStatsV4) %ld rc1CoexStatsV4.len() %d\n"
+ "[dk] %s@%d:sizeof(rc1CoexStatsV5) %ld payload->getLength() %d\n"
+ "[dk] %s@%d:sizeof(rc1CoexStatsV5) %ld rc1CoexStatsV5.len() %d\n"
+ "[dk] %s@%d:sizeof(wlc_rc1cx_status_v4_t) %lu payload->getLength() %lu\n"
+ "[dk] %s@%d:sizeof(wlc_rc1cx_status_v4_t) %lu rc1CoexStats.len() %d\n"
+ "[dk] %s@%d:sizeof(wlc_rc1cx_status_v5_t) %lu payload->getLength() %lu\n"
+ "[dk] %s@%d:sizeof(wlc_rc1cx_status_v5_t) %lu rc1CoexStats.len() %d\n"
+ "busystate %u, fAdjustBusyCnt %u\n"
+ "handleRxStallReasons"
+ "notifyDriverFail"
+ "parseEventLogRecordKvrReport"
+ "triggerCoreCapture"
+ "updateRC1CoexStatsReportV4"
+ "updateRC1CoexStatsReportV5"
+ "wifioff.wd"
- "\"AppleBCMWLANV3_driverkit-1153.8.3.1\""
- "/AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/DriverKit.platform/Developer/SDKs/DriverKit.iPhoneOS23.3.Internal.sdk/System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/PrivateHeaders/IO80211Util.h"
- "AppleBCMWLANV3_driverkit-1153.8.3.1"
- "Dec 20 2023 22:11:10"
- "[WiFiTimeSync!] RX PTMTimestamp invalid: fw_ns=%lld now_ns=%lld ts_ticks=%lld now_ticks=%lld lastPowerOnTicks=%lld isPowerOn()=%d. triggering WD\n"
- "[dk] %s@%d:%s:%d: Length check fail:\n"
- "[dk] %s@%d:Rx Stall Reason Code %s- NumPkts Considered=%d, NumPkts Dropped=%d, Alert Threshold=%d\n"
- "[dk] %s@%d:Set link state before 4 way\n"
- "[dk] %s@%d:Updated fRxDurMulticast %d, fRxDurBroadcast %d \n"
- "dumpDynSARStatusV1"
- "dumpDynSARStatusV2"

```
