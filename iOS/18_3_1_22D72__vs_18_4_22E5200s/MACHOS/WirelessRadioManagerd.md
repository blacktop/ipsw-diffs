## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

-1740.2.9.2.0
-  __TEXT.__text: 0x137558
-  __TEXT.__auth_stubs: 0x2170
-  __TEXT.__objc_stubs: 0x1bf40
+1740.3.8.0.0
+  __TEXT.__text: 0x1315dc
+  __TEXT.__auth_stubs: 0x2140
+  __TEXT.__objc_stubs: 0x1bc20
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xe25c
-  __TEXT.__objc_methname: 0x2b359
-  __TEXT.__cstring: 0x48aea
-  __TEXT.__objc_classname: 0xddc
-  __TEXT.__objc_methtype: 0x751c
-  __TEXT.__gcc_except_tab: 0x436c
-  __TEXT.__const: 0x1fa18
+  __TEXT.__objc_methlist: 0xe99c
+  __TEXT.__objc_methname: 0x2b487
+  __TEXT.__cstring: 0x478c6
+  __TEXT.__objc_classname: 0xddf
+  __TEXT.__objc_methtype: 0x754a
+  __TEXT.__gcc_except_tab: 0x4460
+  __TEXT.__const: 0x1b028
   __TEXT.__dlopen_cstrs: 0x376
   __TEXT.__oslogstring: 0x90
-  __TEXT.__unwind_info: 0x40d0
-  __DATA_CONST.__auth_got: 0x10d0
-  __DATA_CONST.__got: 0x6e8
+  __TEXT.__unwind_info: 0x3f30
+  __DATA_CONST.__auth_got: 0x10b8
+  __DATA_CONST.__got: 0x6f8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x4800
-  __DATA_CONST.__cfstring: 0x28d00
+  __DATA_CONST.__const: 0x4810
+  __DATA_CONST.__cfstring: 0x28720
   __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_intobj: 0x3378
-  __DATA_CONST.__objc_arraydata: 0xf500
-  __DATA_CONST.__objc_arrayobj: 0x6c18
-  __DATA_CONST.__objc_dictobj: 0x208
+  __DATA_CONST.__objc_arraydata: 0xf438
+  __DATA_CONST.__objc_arrayobj: 0x6a38
+  __DATA_CONST.__objc_dictobj: 0x2a8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x18548
-  __DATA.__objc_selrefs: 0x8138
-  __DATA.__objc_ivar: 0x18f0
+  __DATA.__objc_const: 0x17680
+  __DATA.__objc_selrefs: 0x83d0
+  __DATA.__objc_ivar: 0x18f4
   __DATA.__objc_data: 0x28a0
   __DATA.__data: 0x5c8
-  __DATA.__common: 0x168
-  __DATA.__bss: 0x470
+  __DATA.__common: 0x171
+  __DATA.__bss: 0x478
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6532
-  Symbols:   762
-  CStrings:  14006
+  Functions: 6445
+  Symbols:   759
+  CStrings:  13952
 
Symbols:
- _WiFiDeviceClientRegisterBSPEventCallback
- _close
- _open
CStrings:
+ "\x01Q"
+ "%s: getPrivateNetworkCapabilitiesForContext force mWrmCbrsMonitorRequired to true"
+ "-[WCM_BSPMonitorIOS handleWiFiStatusUpdateEvent:isFWReset:]_block_invoke"
+ "2G wifi policy table found matched cell issue band: %s"
+ "5G wifi policy table found matched cell issue band: %s"
+ "6G wifi policy table found matched cell issue band: %s"
+ "@40@0:8I16B20B24B28I32I36"
+ "BSP(%s): mBSPState=%d, mCountryCode=%@, mCountryCodeTimeStampUnixSec=%lld, WiFi(pwrState=0x%x, state=%d, channel=%d, bandForBT=0x%x, allowedBands=0x%x, isNanPhs=0x%x), BT(debugMode=%d, pwrState=0x%x, curBand=0x%x, ullaMode=%d, countryCode=%@, allowedBands=0x%x, targetBand=0x%x)"
+ "BTAntennaSelection_ configureBTAntennaSelection: BT power state = %d, "
+ "BTAntennaSelection_ disable BT pencil coex mitigation config"
+ "BTAntennaSelection_ enable BT pencil coex mitigation config"
+ "BTAntennaSelection_ sending parameters to thread"
+ "MWS_TIMER_GRANULARITY_MS"
+ "MWS_WIFI_CONDITION_CHANNEL_CONFIG"
+ "NonCallKitApp"
+ "RCU2 Controller - sendAntennaPreference Failure - preference set to %hu "
+ "RCU2 Controller - sendAntennaPreference Success - preference set to %hu"
+ "RCU2 Controller - sendAntennaPreference: %d"
+ "RCU2 Controller - setCellScanFreqTable: %@ "
+ "RCU2 Controller - updateCellScanFreqTable failed! "
+ "RCU2 Controller - updateCellScanFreqTable: %@ "
+ "WCMBSP:%s force disabling SibCoex Mode due to WiFi FW reset."
+ "WCMBSP:%s force enabling SibCoex Mode due to WiFi FW reset"
+ "WCMBSP:%s ignoring Wifi disassociated / disabled update due to isNanPhs state doesn't match: wifiState=%s, wifiChannel=%u, isNanPhs=%u"
+ "WCMBSP:%s powerState=0x%x isFWReset=0x%x"
+ "WLAN25ASupport"
+ "WiFiS: setting condition id %d for the following range of channels[%d, %d] in band 2g: %d 5g: %d 6g: %d"
+ "^{?=idddd[5@]B}60@0:8i16d20d28d36d44^I52"
+ "anyCallStateChange:"
+ "anyCallStateChange: mWrmCbrsMonitorRequired=%d, numberofSubscriptions=%lu, anyCallState=%d"
+ "cellScanFreqTableStr"
+ "combineWifiChannelList:withChannelList:inAllowedChannelSet:"
+ "createChannelConfigurationForConditionId:enable2G:enable5G:enable6G:wifi_channel_lower:wifi_channel_upper:"
+ "evaluateCbrsInDualSimMode done"
+ "evaluateCbrsInDualSimMode error: not in dual sim mode : numberofSubscriptions=%lu"
+ "handleWiFiStatusUpdateEvent:isFWReset:"
+ "isFalseTDDIssueBand:cellDlLowFreq:cellDlHighFreq:cellUlLowFreq:cellUlHighFreq:"
+ "isPrivateNetworkEvaluationNeeded mWrmCbrsMonitorRequired: %d"
+ "notifyBBVoIPState:::::"
+ "search_2GWifi_IssueBandForCellBandInfoType:cellDlLowFreq:cellDlHighFreq:cellUlLowFreq:cellUlHighFreq:matchedIssuBand:"
+ "search_5GWifi_IssueBandForCellBandInfoType:cellDlLowFreq:cellDlHighFreq:cellUlLowFreq:cellUlHighFreq:matchedIssuBand:"
+ "search_WifiEnh_IssueBandForCellBandInfoType:cellDlLowFreq:cellDlHighFreq:cellUlLowFreq:cellUlHighFreq:matchedIssuBand:"
+ "setAggregatedConditionIdConfig:"
+ "setCellScanFreqTable:"
+ "setChannelsToEnablerFemModeWiFiEnh:enable5G:enable6G:"
+ "updateAntennaPreference:"
+ "updateAnyCallState: callProvider %@ callState=%s"
+ "updateAnyCallState:providerIdentifier:"
+ "updateCellScanFreqTable"
+ "v28@0:8B16B20B24"
+ "v40@0:8C16C20C24C28@32"
+ "vendor:coex:preferredAntenna"
+ "vendor:coex:scanFreqTable"
- "%s (%d, 0x%x, %d)"
- "%s (0x%x, 0x%x)"
- "%s (0x%x, 0x%x, 0x%x, 0x%x, 0x%x, 0x%x)"
- "%s Unknown eventType %d"
- "-[WCM_BSPMonitorIOS handleWiFiStatusUpdateEvent:]_block_invoke"
- "-[WCM_BTControllerIOS handleBSPEvent:]"
- "-[WCM_WiFiServiceIOS bspBandSwitchRequest:targetBand:]_block_invoke"
- "-[WCM_WiFiServiceIOS bspGetBandSwitchStatus]_block_invoke"
- "-[WCM_WiFiServiceIOS bspGetChannelQualityInfo]_block_invoke"
- "-[WCM_WiFiServiceIOS bspNanPhsStateRequest]_block_invoke"
- "-[WCM_WiFiServiceIOS bspRegulatoryInfoRequest]_block_invoke"
- "-[WCM_WiFiServiceIOS bspSetCoexMode:wifiSupportedBands:btCurrentBand:btSupportedBands:setTimeToTSTOnly:timeToTST:]_block_invoke"
- "-[WCM_WiFiServiceIOS bspStatusRequest]_block_invoke"
- "-[WCM_WiFiServiceIOS bspUpdateBTStatus_powerState:frequencyBand:ullaMode:]_block_invoke"
- "/dev/btwake"
- "@\"WCM_BSPMonitor\""
- "AggdRemoval_ Since Aggd related keys ave been disabled on the server side, we will stop submitting metrics to Aggd. (handleErrorReport)"
- "BSP(%s): mBSPState=%d, mCountryCode=%@, mCountryCodeTimeStampUnixSec=%lld, WiFi(pwrState=0x%x, state=%d, channel=%d, bandForBT=0x%x, allowedBands=0x%x), BT(debugMode=%d, pwrState=0x%x, curBand=0x%x, ullaMode=%d, countryCode=%@, allowedBands=0x%x, targetBand=0x%x)"
- "BSP_BTSubband"
- "BSP_CoexMode"
- "BSP_Command"
- "BSP_CurrentBand"
- "BSP_EventParams"
- "BSP_EventType"
- "BSP_FailCount"
- "BSP_NanPhs_Band"
- "BSP_NanPhs_Channel"
- "BSP_NanPhs_isLinkDown"
- "BSP_RegulatoryInfo"
- "BSP_SIB_BTCurrentBand"
- "BSP_SIB_BTSupportedBands"
- "BSP_SIB_CmdParams"
- "BSP_SIB_CmdType"
- "BSP_SIB_Enable"
- "BSP_SIB_SetTimeToTSTOnly"
- "BSP_SIB_TimeToTST"
- "BSP_SIB_WiFiSupportedBands"
- "BSP_SuccessCount"
- "BSP_ULLAMode"
- "CellularMwsTxAllBands"
- "CellularWatchFcmBcmAntennaPref"
- "Check if band is eligible for WatchAntennaPreference on bandinfoType(0x%x) downlink(%lf ~ %lf) uplink(%lf ~ %lf) "
- "CoreWiFi"
- "DisableOCL_WiFiEnh 2G Part: pIssueBandMatched: pIssueBand->_bandInfoType(%d) & bandInfoType(%d) && pIssueBand->_downlinkLowFreq(%lf) <= cellDlLowFreq(%lf) && pIssueBand->_downlinkHighFreq(%lf) >= cellDlHighFreq(%lf) && pIssueBand->_uplinkLowFreq(%lf) <= cellUlLowFreq(%lf) && pIssueBand->_uplinkHighFreq(%lf) >= cellUlHighFreq(%lf)"
- "DisableOCL_WiFiEnh 5G Part: pIssueBandMatched_5GHz: pIssueBand_5GHz->_bandInfoType(%d) & bandInfoType(%d) && pIssueBand_5GHz->_downlinkLowFreq(%lf) <= cellDlLowFreq(%lf) && pIssueBand_5GHz->_downlinkHighFreq(%lf) >= cellDlHighFreq(%lf) && pIssueBand_5GHz->_uplinkLowFreq(%lf) <= cellUlLowFreq(%lf) && pIssueBand_5GHz->_uplinkHighFreq(%lf) >= cellUlHighFreq(%lf)"
- "DisableOCL_WiFiEnh Enh Part: pIssueBandMatched_Enh: pIssueBand_Enh->_bandInfoType(%d) & bandInfoType(%d) && pIssueBand_Enh->_downlinkLowFreq(%lf) <= cellDlLowFreq(%lf) && pIssueBand_Enh->_downlinkHighFreq(%lf) >= cellDlHighFreq(%lf) && pIssueBand_Enh->_uplinkLowFreq(%lf) <= cellUlLowFreq(%lf) && pIssueBand_Enh->_uplinkHighFreq(%lf) >= cellUlHighFreq(%lf)"
- "EnhancedCTService: updateCallState no change %s"
- "EnhancedCTService: updateCallState=%s, mWrmCbrsMonitorRequired=%d, numberofSubscriptions=%lu"
- "Failed to send message to BT about AWDL Active State"
- "Failed to send message to BT about NAN Active State"
- "Figaro5GTDD"
- "KeepBTAwake"
- "Keeping BT awake"
- "Letting BT go to sleep."
- "PolicyManager: WiFi 5G rates recovered and no AoS link, allow AoS 5GHz"
- "PolicyManager: handleLow5GRate %d"
- "Received BSPEvent msg: %@"
- "Sent message to BT about current AWDL Active State: %d"
- "Sent message to BT about current NAN Active State: %d"
- "T@\"WCM_BSPMonitor\",N,V_bspMonitor"
- "V2BtimapDebug_: pIssueBandMatched: pIssueBand->_bandInfoType(%d) & bandInfoType(%d) && pIssueBand->_downlinkLowFreq(%lf) <= cellDlLowFreq(%lf) && pIssueBand->_downlinkHighFreq(%lf) >= cellDlHighFreq(%lf) && pIssueBand->_uplinkLowFreq(%lf) <= cellUlLowFreq(%lf) && pIssueBand->_uplinkHighFreq(%lf) >= cellUlHighFreq(%lf)"
- "V2BtimapDebug_: pIssueBandMatched_5GHz: pIssueBand_5GHz->_bandInfoType(%d) & bandInfoType(%d) && pIssueBand_5GHz->_downlinkLowFreq(%lf) <= cellDlLowFreq(%lf) && pIssueBand_5GHz->_downlinkHighFreq(%lf) >= cellDlHighFreq(%lf) && pIssueBand_5GHz->_uplinkLowFreq(%lf) <= cellUlLowFreq(%lf) && pIssueBand_5GHz->_uplinkHighFreq(%lf) >= cellUlHighFreq(%lf)"
- "WCI2_V2: CC2UnitTest: pIssueBand->_bandInfoType(%d) & bandInfoType(%d) && pIssueBand->_downlinkLowFreq(%lf) <= cellDlLowFreq(%lf) && pIssueBand->_downlinkHighFreq(%lf) >= cellDlHighFreq(%lf) && pIssueBand->_uplinkLowFreq(%lf) <= cellUlLowFreq(%lf) && pIssueBand->_uplinkHighFreq(%lf) >= cellUlHighFreq(%lf), "
- "WCI2_V2: CC2UnitTest: pIssueBand_5GHz->_bandInfoType(%d) & bandInfoType(%d) && pIssueBand_5GHz->_downlinkLowFreq(%lf) <= cellDlLowFreq(%lf) && pIssueBand_5GHz->_downlinkHighFreq(%lf) >= cellDlHighFreq(%lf) && pIssueBand_5GHz->_uplinkLowFreq(%lf) <= cellUlLowFreq(%lf) && pIssueBand_5GHz->_uplinkHighFreq(%lf) >= cellUlHighFreq(%lf)"
- "WCI2_WiFiEnh2G5G 2G Part: pIssueBandMatched: pIssueBand->_bandInfoType(%d) & bandInfoType(%d) && pIssueBand->_downlinkLowFreq(%lf) <= cellDlLowFreq(%lf) && pIssueBand->_downlinkHighFreq(%lf) >= cellDlHighFreq(%lf) && pIssueBand->_uplinkLowFreq(%lf) <= cellUlLowFreq(%lf) && pIssueBand->_uplinkHighFreq(%lf) >= cellUlHighFreq(%lf)"
- "WCI2_WiFiEnh2G5G 5G Part: pIssueBandMatched_5GHz: pIssueBand_5GHz->_bandInfoType(%d) & bandInfoType(%d) && pIssueBand_5GHz->_downlinkLowFreq(%lf) <= cellDlLowFreq(%lf) && pIssueBand_5GHz->_downlinkHighFreq(%lf) >= cellDlHighFreq(%lf) && pIssueBand_5GHz->_uplinkLowFreq(%lf) <= cellUlLowFreq(%lf) && pIssueBand_5GHz->_uplinkHighFreq(%lf) >= cellUlHighFreq(%lf)"
- "WCI2_WiFiEnh2G5G Enh Part: pIssueBandMatched_Enh: pIssueBand_Enh->_bandInfoType(%d) & bandInfoType(%d) && pIssueBand_Enh->_downlinkLowFreq(%lf) <= cellDlLowFreq(%lf) && pIssueBand_Enh->_downlinkHighFreq(%lf) >= cellDlHighFreq(%lf) && pIssueBand_Enh->_uplinkLowFreq(%lf) <= cellUlLowFreq(%lf) && pIssueBand_Enh->_uplinkHighFreq(%lf) >= cellUlHighFreq(%lf)"
- "WCMBSP:%s ignoring late update wifiState=%s, wifiChannel=%u, isNanPhs=%u"
- "WCMBSP:%s powerState=0x%x"
- "WCM_WiFiCellCoexIssue(%p) has invalid _issueType(%d) in watchAntPreference %d"
- "WatchAntennaPref need to apply rules for %s"
- "WatchAntennaPreference for this band Yes or No %d"
- "WiFiEnh_: thisIssueBand does not match any of the predefined ranges defined in WCM_WiFiCellCoexIssueBand enum."
- "WiFiS: setting setting condition id %d for the following range of channels %d %d in band 2g: %d 5g: %d 6g: %d"
- "WifiGen9rFemConfig2gWifiOnly"
- "YYDebug_ Unknown WiFi band for WiFi antenna selection"
- "YYDebug_ configureBTAntennaSelection: BT power state = %d, "
- "YYDebug_ disable BT pencil coex mitigation config"
- "YYDebug_ enable BT pencil coex mitigation config"
- "_bspMonitor"
- "allowedServices"
- "bspMonitor"
- "callbackBSPEventCallback"
- "enableLegacyCoexFeature"
- "evaluateCbrsInDualSimMode error: not in dual sim mode"
- "handleBSPEvent:"
- "handleErrorReport:"
- "handleWiFiNANChange"
- "handleWiFiStatusUpdateEvent:"
- "i52@0:8i16d20d28d36d44"
- "isPrivateNetworkEvaluationNeeded: %d"
- "kWCMBTAWDLActive"
- "kWCMBTNANActive"
- "notifyBBVoIPState::::"
- "reportWiFiError"
- "setBspMonitor:"
- "setChannel:"
- "setChannelsToEnablerFemModeWiFiEnh:enable5G:enable6G:setDefaultForall:"
- "thisIssueBand does not match any of the predefined ranges defined in WCM_WiFiCellCoexIssueBand enum."
- "transportType"
- "updateAWDLActive:"
- "updateAwakeMode:"
- "updateCallState:"
- "updateNANActive:"
- "v32@0:8B16B20B24B28"
- "watchAntennaPrefEnabledInPolicy:cellDlHighFreq:cellUlLowFreq:cellUlHighFreq:watchAntPref:"
- "watchAntennaPreferenceEnableCheckBandCombination:cellDlLowFreq:cellDlHighFreq:cellUlLowFreq:cellUlHighFreq:"

```
