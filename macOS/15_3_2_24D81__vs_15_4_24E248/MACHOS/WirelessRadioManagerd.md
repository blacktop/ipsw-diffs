## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

-1635.2.0.0.0
-  __TEXT.__text: 0x80a64
+1675.19.0.0.0
+  __TEXT.__text: 0x7ecc0
   __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_stubs: 0x11d20
-  __TEXT.__objc_methlist: 0x971c
+  __TEXT.__objc_stubs: 0x11c00
+  __TEXT.__objc_methlist: 0x9b4c
   __TEXT.__gcc_except_tab: 0x42c
-  __TEXT.__const: 0x2ac4
-  __TEXT.__cstring: 0x2a41b
-  __TEXT.__objc_methname: 0x1fa97
+  __TEXT.__const: 0x2af4
+  __TEXT.__cstring: 0x293a0
+  __TEXT.__objc_methname: 0x1fb23
   __TEXT.__objc_classname: 0x68f
   __TEXT.__objc_methtype: 0x4682
   __TEXT.__dlopen_cstrs: 0x43
   __TEXT.__oslogstring: 0x44
-  __TEXT.__unwind_info: 0x14b8
+  __TEXT.__unwind_info: 0x13f0
   __DATA_CONST.__auth_got: 0x640
   __DATA_CONST.__got: 0x4c8
-  __DATA_CONST.__const: 0x1fd0
-  __DATA_CONST.__cfstring: 0x17b80
+  __DATA_CONST.__const: 0x1fb0
+  __DATA_CONST.__cfstring: 0x17940
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x17f0
   __DATA_CONST.__objc_arrayobj: 0x510
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0xf6c0
-  __DATA.__objc_selrefs: 0x5bd8
-  __DATA.__objc_ivar: 0x116c
+  __DATA.__objc_const: 0xede0
+  __DATA.__objc_selrefs: 0x5d20
+  __DATA.__objc_ivar: 0x1168
   __DATA.__objc_data: 0x1680
   __DATA.__data: 0x278
   __DATA.__bss: 0x254

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E319FC2F-0E60-3EEA-8183-2C6D8530C5F9
-  Functions: 3432
+  UUID: 91AFB2B1-06AD-3844-A63E-4D7FBBE346A5
+  Functions: 3399
   Symbols:   351
-  CStrings:  12007
+  CStrings:  11960
 
CStrings:
+ "2G wifi policy table found matched cell issue band: %s"
+ "5G wifi policy table found matched cell issue band: %s"
+ "6G wifi policy table found matched cell issue band: %s"
+ "BB25A AntMapping_1:Updating antenna map params to cellular modem"
+ "BB25A: platformID not defined to configure CellTxAntIdx over the bus"
+ "BTAntennaSelection_ configureBTAntennaSelection: BT power state = %d, "
+ "BTAntennaSelection_ disable BT pencil coex mitigation config"
+ "BTAntennaSelection_ enable BT pencil coex mitigation config"
+ "BTAntennaSelection_ sending parameters to thread"
+ "HFAFHDebug_ Coex Issue array count 5G: %lu"
+ "HPCellular (handleBTPowerStateChange): HPCellularActive = (%d), set BT AFH map to (%@)."
+ "HPCellular (handleCellularNetworkUpdate): HPCellularActive = (%d), set BT AFH map to (%@)."
+ "HPCellular (updateGPSRadioActiveState): HPCellularActive = (%d), set BT AFH map to (%@)."
+ "^{?=idddd[5@]B}60@0:8i16d20d28d36d44^I52"
+ "combineWifiChannelList:withChannelList:inAllowedChannelSet:"
+ "handleWiFiStatusUpdateEvent:isFWReset:"
+ "initWiFiStatetoBT"
+ "isFalseTDDIssueBand:cellDlLowFreq:cellDlHighFreq:cellUlLowFreq:cellUlHighFreq:"
+ "notifyBBVoIPState:::::"
+ "search_2GWifi_IssueBandForCellBandInfoType:cellDlLowFreq:cellDlHighFreq:cellUlLowFreq:cellUlHighFreq:matchedIssuBand:"
+ "search_5GWifi_IssueBandForCellBandInfoType:cellDlLowFreq:cellDlHighFreq:cellUlLowFreq:cellUlHighFreq:matchedIssuBand:"
+ "search_WifiEnh_IssueBandForCellBandInfoType:cellDlLowFreq:cellDlHighFreq:cellUlLowFreq:cellUlHighFreq:matchedIssuBand:"
+ "setAggregatedConditionIdConfig:"
+ "setChannelsToEnablerFemModeWiFiEnh:enable5G:enable6G:"
+ "updateAntennaPreference:"
+ "v28@0:8B16B20B24"
+ "v40@0:8C16C20C24C28@32"
+ "wlan.debug.module-instance=aruba"
+ "wlan.debug.module-instance=garden"
+ "wlan.debug.module-instance=kos"
- "@\"WCM_BSPMonitor\""
- "AggdRemoval_ Since Aggd related keys ave been disabled on the server side, we will stop submitting metrics to Aggd. (handleErrorReport)"
- "BT Crashed or init - resending WiFi states"
- "CellularMwsTxAllBands"
- "CellularWatchFcmBcmAntennaPref"
- "Check if band is eligible for WatchAntennaPreference on bandinfoType(0x%x) downlink(%lf ~ %lf) uplink(%lf ~ %lf) "
- "CoreWiFi"
- "DisableOCL_WiFiEnh 2G Part: pIssueBandMatched: pIssueBand->_bandInfoType(%d) & bandInfoType(%d) && pIssueBand->_downlinkLowFreq(%lf) <= cellDlLowFreq(%lf) && pIssueBand->_downlinkHighFreq(%lf) >= cellDlHighFreq(%lf) && pIssueBand->_uplinkLowFreq(%lf) <= cellUlLowFreq(%lf) && pIssueBand->_uplinkHighFreq(%lf) >= cellUlHighFreq(%lf)"
- "DisableOCL_WiFiEnh 5G Part: pIssueBandMatched_5GHz: pIssueBand_5GHz->_bandInfoType(%d) & bandInfoType(%d) && pIssueBand_5GHz->_downlinkLowFreq(%lf) <= cellDlLowFreq(%lf) && pIssueBand_5GHz->_downlinkHighFreq(%lf) >= cellDlHighFreq(%lf) && pIssueBand_5GHz->_uplinkLowFreq(%lf) <= cellUlLowFreq(%lf) && pIssueBand_5GHz->_uplinkHighFreq(%lf) >= cellUlHighFreq(%lf)"
- "DisableOCL_WiFiEnh Enh Part: pIssueBandMatched_Enh: pIssueBand_Enh->_bandInfoType(%d) & bandInfoType(%d) && pIssueBand_Enh->_downlinkLowFreq(%lf) <= cellDlLowFreq(%lf) && pIssueBand_Enh->_downlinkHighFreq(%lf) >= cellDlHighFreq(%lf) && pIssueBand_Enh->_uplinkLowFreq(%lf) <= cellUlLowFreq(%lf) && pIssueBand_Enh->_uplinkHighFreq(%lf) >= cellUlHighFreq(%lf)"
- "Failed to send message to BT about AWDL Active State"
- "Failed to send message to BT about NAN Active State"
- "Figaro5GTDD"
- "HPCellular (handleBTPowerStateChange): Bool flag self.hpCellNeed2SetBTAFH = (%d), Fixed AFH self.btPreferredChannelMapHPCellularActive = (%@)."
- "HPCellular (handleCellularNetworkUpdate): Bool flag self.hpCellNeed2SetBTAFH = (%d), Fixed AFH self.btPreferredChannelMapHPCellularActive = (%@)."
- "HPCellular (updateGPSRadioActiveState): Bool flag self.hpCellNeed2SetBTAFH = (%d), Fixed AFH self.btPreferredChannelMapHPCellularActive = (%@)."
- "KeepBTAwake"
- "PolicyManager: WiFi 5G rates recovered and no AoS link, allow AoS 5GHz"
- "PolicyManager: handleLow5GRate %d"
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
- "WCM_WiFiCellCoexIssue(%p) has invalid _issueType(%d) in watchAntPreference %d"
- "WatchAntennaPref need to apply rules for %s"
- "WatchAntennaPreference for this band Yes or No %d"
- "WiFiEnh_: thisIssueBand does not match any of the predefined ranges defined in WCM_WiFiCellCoexIssueBand enum."
- "YYDebug_ Unknown WiFi band for WiFi antenna selection"
- "YYDebug_ configureBTAntennaSelection: BT power state = %d, "
- "YYDebug_ disable BT pencil coex mitigation config"
- "YYDebug_ enable BT pencil coex mitigation config"
- "_bspMonitor"
- "bspMonitor"
- "enableLegacyCoexFeature"
- "handleErrorReport:"
- "handleWiFiNANChange"
- "handleWiFiStatusUpdateEvent:"
- "i52@0:8i16d20d28d36d44"
- "initControllerPolicy:"
- "kWCMBTAWDLActive"
- "kWCMBTNANActive"
- "notifyBBVoIPState::::"
- "reportWiFiError"
- "setBspMonitor:"
- "setChannelsToEnablerFemModeWiFiEnh:enable5G:enable6G:setDefaultForall:"
- "thisIssueBand does not match any of the predefined ranges defined in WCM_WiFiCellCoexIssueBand enum."
- "updateAWDLActive:"
- "updateAwakeMode:"
- "updateNANActive:"
- "v32@0:8B16B20B24B28"
- "v32@0:8C16C20C24C28"
- "watchAntennaPrefEnabledInPolicy:cellDlHighFreq:cellUlLowFreq:cellUlHighFreq:watchAntPref:"
- "watchAntennaPreferenceEnableCheckBandCombination:cellDlLowFreq:cellDlHighFreq:cellUlLowFreq:cellUlHighFreq:"

```
