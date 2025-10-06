## wifid

> `/usr/sbin/wifid`

```diff

-1664.2.0.0.0
-  __TEXT.__text: 0x17e1ac
+1675.21.3.1.0
+  __TEXT.__text: 0x17e274
   __TEXT.__auth_stubs: 0x2550
-  __TEXT.__objc_stubs: 0x10b40
-  __TEXT.__objc_methlist: 0x4ff4
-  __TEXT.__objc_methname: 0x16151
+  __TEXT.__objc_stubs: 0x10ae0
+  __TEXT.__objc_methlist: 0x4f54
+  __TEXT.__objc_methname: 0x1605f
   __TEXT.__objc_classname: 0x7ab
-  __TEXT.__objc_methtype: 0x2be4
+  __TEXT.__objc_methtype: 0x2b9f
   __TEXT.__const: 0x8c0
-  __TEXT.__gcc_except_tab: 0x17f4
-  __TEXT.__cstring: 0x636a3
+  __TEXT.__gcc_except_tab: 0x182c
+  __TEXT.__cstring: 0x63a91
   __TEXT.__ustring: 0x4c2
   __TEXT.__oslogstring: 0x245
   __TEXT.__dlopen_cstrs: 0x1a5
-  __TEXT.__unwind_info: 0x3320
+  __TEXT.__unwind_info: 0x3338
   __DATA_CONST.__auth_got: 0x12b8
   __DATA_CONST.__got: 0xfd0
   __DATA_CONST.__auth_ptr: 0x138
-  __DATA_CONST.__const: 0x6878
-  __DATA_CONST.__cfstring: 0x1b9e0
+  __DATA_CONST.__const: 0x68a8
+  __DATA_CONST.__cfstring: 0x1ba60
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x698
+  __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_intobj: 0xbd0
   __DATA_CONST.__objc_arraydata: 0x378
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0xd5c0
-  __DATA.__objc_selrefs: 0x4db0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x6a8
-  __DATA.__objc_superrefs: 0x1a0
-  __DATA.__objc_ivar: 0x8c8
+  __DATA.__objc_const: 0xd500
+  __DATA.__objc_selrefs: 0x4d48
+  __DATA.__objc_ivar: 0x8b8
   __DATA.__objc_data: 0x1180
-  __DATA.__data: 0x1040
+  __DATA.__data: 0x1048
   __DATA.__bss: 0x7e0
   __DATA.__common: 0x5c
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 1F95B994-F7C5-30AB-9B73-E10C69266E2A
-  Functions: 5248
-  Symbols:   1280
-  CStrings:  18311
+  UUID: 8B1F7321-92E6-3F7A-AE97-4C44880BF170
+  Functions: 5240
+  Symbols:   1278
+  CStrings:  18318
 
Symbols:
- _OBJC_CLASS_$_CWFSensingParameters
- _OBJC_CLASS_$_WAUtil
CStrings:
+ "%@: isHidden=%d, isEAP=%d, isSAE=%d, isWPA=%d, isWEP=%d, WAPI=%d, type=%d, enabled=%@, saveData=%@, responsiveness=%@ (%@) isHome=%@, isForceFixed=%d, transitionDisabledFlags=%@, foundNanIe=%d, isPH=%d, isPublicAirPlayNetwork=%d, is6EDisabled=%d, hs20=%d, channel=%d"
+ "%s: AWDL enableCount:%d"
+ "%s: AWDL inActiveDuration:%d"
+ "%s: AWDL totalDuration:%d"
+ "%s: Network with the same %s %@ found at index %ld"
+ "%s: Removed known BSS from index %ld"
+ "%s: SSID transition arbitrator is running, ignore duplicated steering request"
+ "%s: Starting cloud sync engine after AJ retry"
+ "%s: Starting cloud sync engine after exceeding %ds waiting for auto-join attempt"
+ "%s: WiFiRoam : AP environment downgraded from TriBandMultiAP to MultiAp due to 6Emode"
+ "%s: WiFiRoam : AP environment downgraded from TriBandSingleAP to DualBandSingleAp due to 6Emode"
+ "%s: currently no networking app is in the foreground"
+ "%s: error %d, state %d\n"
+ "%s: network with domain name %@ not found"
+ "%s: null request"
+ "%s: wifiAmbiguousSSIDs is null"
+ "-[WiFiBatteryManager requestPowerResource:withDetails:]"
+ "AP_MODE_MOVETOIOS_MIGRATION"
+ "AWDL_STATS_AWDL_STATS_ENABLE_COUNT"
+ "AWDL_STATS_STATS_INACTIVITY_DURATION"
+ "AWDL_STATS_TOTAL_DURATION"
+ "AssertMacros: %s, %s file: %s, line: %d, value: %lld\n"
+ "Association failed"
+ "BSP_CoexMode"
+ "BSP_LQM_AvgMuteMS"
+ "BSP_LQM_ErrorPercentage"
+ "BSP_LQM_IsP2PActive"
+ "BSP_LQM_IsScanActive"
+ "BSP_LQM_MaxConsecutiveFails"
+ "BSP_LQM_MaxMuteMS"
+ "BSP_LQM_MutePercentage"
+ "BSP_LQM_Overflowed"
+ "BSP_LQM_RejectOrFailPercentageOfTriggers"
+ "BSP_LQM_SampleDurationMS"
+ "BSP_LQM_TimeToTST"
+ "BSP_LQM_TimeoutPercentageOfTriggers"
+ "BSP_LQM_TriggerCount"
+ "DeviceUnlocked"
+ "FindMatchingHS20Network"
+ "Gave up waiting for EAPOLControlCopyStateAndStatus. Bailing"
+ "HPSetup"
+ "MIGRATION: %s Starting SoftAp on 2.4GHz (RegulatoryRestricted: %d, Infra6G: %d, InfraBWHigherThan80MHz:%d Infra5G_DFS:%d AWDLRealTimeMode:%d)"
+ "MIGRATION: Selecting 2.4G infra channel :%d "
+ "MIGRATION: Selecting 2G  channel :%d\n"
+ "MIGRATION: Selecting 5G  channel :%d  AwdlActive: %d"
+ "MIGRATION: Selecting 5G infra channel :%d "
+ "MIGRATION:%s Client name : %@ "
+ "MIGRATION:%s Request  Dict : %@ "
+ "MIGRATION:%s: END print request  dictionary %@ and hostAPDict: %@"
+ "MIGRATION:%s: SoftAP failed to start"
+ "N/A"
+ "Preferences SpringBoard Carousel WiFiPickerExtens Setup budd sharingd demod BundledIntentHandler SiriViewService assistantd assistant_service Siri SettingsIntentExtension NanoSettings PineBoard TVSettings SoundBoard RealityControlCenter mobilewifitool WirelessStress coreautomationd wifiutil NanoWiFiViewService ATKWiFiFramework WiFiViewService hQT XCTestInternalAngel HPSetup AirPlaySenderUIApp TVSetup"
+ "SUCCESS"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "TB,?,N"
+ "TB,?,N,GisNetworkProvider"
+ "TB,?,N,GisNetworkProvider,VnetworkProvider"
+ "TB,?,N,GisNexusProvider"
+ "TB,?,N,GisSpecificUseOnly"
+ "TB,?,N,GisSpecificUseOnly,VspecificUseOnly"
+ "WiFiDeviceManagerSetAmbiguousSSIDs"
+ "WiFiDeviceManagerStartAutoJoinAndReply_block_invoke_2"
+ "WiFiManager-1675.21.3.1 Feb 17 2024 00:27:52"
+ "WiFiManager-1675.21.3.1 Feb 17 2024 00:28:21"
+ "WiFiNetworkIs6EModeOff"
+ "__WiFiDeviceManagerPostAutoJoinNotificationWithMetric"
+ "__WiFiDeviceManagerSelectPHChannel"
+ "__WiFiManagerLockStateUpdate_block_invoke"
+ "__WiFiManagerLockStateUpdate_block_invoke_3"
+ "__WiFiManagerResetCarPlayMode"
+ "autoJoinParameters"
+ "domain name"
+ "enableCount"
+ "inActiveDuration"
+ "matd"
+ "requestPowerResource:withDetails:"
+ "setScanningState:client:neighborBSS:otherBSS:withChannelInfoList:withRequest:forInterface:"
+ "totalDuration"
+ "updateIsBSPActive:"
+ "updateWithBspOverflowed:IsBSPActive:BspTimeToTST:BspSampleDurationMS:IsScanActiveBSP:IsP2PActiveBSP:BspTriggerCount:BspMutePercentage:BspMaxMuteMS:BspAvgMuteMS:BspErrorPercentage:BspTimeOutPercentageOfTriggers:BspRejectOrFailPercentageOfTriggers:bspMaxConsecutiveFails:supportsLinkRecommendation:forInterface:"
- " AWDL link went down. Check if we have correct country code"
- "%@: isHidden=%d, isEAP=%d, isSAE=%d, isWPA=%d, isWEP=%d, WAPI=%d, type=%d, enabled=%@, saveData=%@, responsiveness=%@ (%@) isHome=%@, isForceFixed=%d, transitionDisabledFlags=%@, foundNanIe=%d, isPH=%d, isPublicAirPlayNetwork=%d, hs20=%d"
- "%s: Determine fresh locale since AWDL ended"
- "%s: Didn't get two WiFiSoftErrorStatsRecords with chipCounter properties to delta."
- "%s: Error: failed to create AWDL end locale check timer"
- "%s: Invalid Params"
- "%s: Removed known BSS from index %ld: %@"
- "%s: currently in non-networking app %@"
- "+[WiFiSoftErrorContext populateBtCoexCounterDeltaWithCountersFromRecord1:andRecord2:]"
- "+[WiFiSoftErrorContext populateWiFiChipCounterDeltaWithChipCountersFromRecord1:andChipCountersFromRecord2:]"
- "+[WiFiSoftErrorContext populateWiFiFrameCountersWithRecord1Counters:andRecord2Counters:]"
- "-[WiFiBatteryManager requestPowerResource::]"
- "@\"WAMessageAWD\""
- "AssertMacros: %s, %s file: %s, line: %d, value: %ld\n"
- "MMBTCS_antennaOwnership2BT"
- "MMBTCS_antennaOwnership2WLAN"
- "MMBTCS_enbledStateOff"
- "MMBTCS_enbledStateOn"
- "MMBTCS_hybridStateOff"
- "MMBTCS_hybridStateOn"
- "MMBTCS_tdmStateOff"
- "MMBTCS_tdmStateOn"
- "MMCC_frameCounters"
- "MMCC_mcastWPA2Counters"
- "MMCC_rxGeneralStats"
- "MMCC_rxMACCounterStats"
- "MMCC_rxMACErrorStats"
- "MMCC_rxPhyErrors"
- "MMCC_txErrorStats"
- "MMCC_txGeneralStats"
- "MMCC_ucastWPA2Counters"
- "MMFCS_rxControl"
- "MMFCS_rxData"
- "MMFCS_rxManagement"
- "MMFCS_txControl"
- "MMFCS_txData"
- "MMFCS_txManagement"
- "Preferences SpringBoard Carousel WiFiPickerExtens Setup budd sharingd demod BundledIntentHandler SiriViewService assistantd assistant_service Siri SettingsIntentExtension NanoSettings PineBoard TVSettings SoundBoard RealityControlCenter mobilewifitool WirelessStress coreautomationd wifiutil NanoWiFiViewService ATKWiFiFramework WiFiViewService hQT XCTestInternalAngel HPSetup"
- "T@\"WAMessageAWD\",&,N,V_btCoexStats"
- "T@\"WAMessageAWD\",&,N,V_chipCounters"
- "T@\"WAMessageAWD\",&,N,V_frameCounters"
- "TB,N,GisNetworkProvider"
- "TB,N,GisNetworkProvider,VnetworkProvider"
- "TB,N,GisNexusProvider"
- "TB,N,GisSpecificUseOnly"
- "TB,N,GisSpecificUseOnly,VspecificUseOnly"
- "T{?=Q^v},N,V_requestDetails"
- "WiFiManager-1664.2 Dec 21 2023 00:07:19"
- "WiFiManager-1664.2 Dec 21 2023 00:07:52"
- "__WiFiDeviceManagerPostAutoJoinNotification"
- "__WiFiManagerAwdlEndCheckLocaleCallback"
- "__WiFiManagerAwdlLinkEventCallback"
- "__WiFiManagerLockStateUpdate_block_invoke_2"
- "_btCoexStats"
- "_chipCounters"
- "_frameCounters"
- "_requestDetails"
- "btCoexStats"
- "chipCounters"
- "frameCounters"
- "getCopyOfMessage:withNumericalValuesSubstractedByValuesInMessage:"
- "populateBtCoexCounterDeltaWithCountersFromRecord1:andRecord2:"
- "populateWiFiChipCounterDeltaWithChipCountersFromRecord1:andChipCountersFromRecord2:"
- "populateWiFiFrameCountersWithRecord1Counters:andRecord2Counters:"
- "requestDetails"
- "requestPowerResource::"
- "setBtCoexStats:"
- "setChipCounters:"
- "setComment:"
- "setFrameCounters:"
- "setRequestDetails:"
- "setScanningState:client:neighborBSS:otherBSS:withChannelInfoList:forInterface:"
- "setScheduleDailyAt:"
- "setSubMessageValue:"
- "setSubmitMetric:"
- "v32@0:8{?=Q^v}16"
- "{?=\"type\"Q\"refcon\"^v}"
- "{?=Q^v}16@0:8"

```
