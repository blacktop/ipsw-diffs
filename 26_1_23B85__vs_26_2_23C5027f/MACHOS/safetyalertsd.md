## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-64.0.26.0.0
-  __TEXT.__text: 0xd707c
-  __TEXT.__auth_stubs: 0xfc0
-  __TEXT.__objc_stubs: 0x2ee0
+64.0.36.0.0
+  __TEXT.__text: 0xf0ce8
+  __TEXT.__auth_stubs: 0xfe0
+  __TEXT.__objc_stubs: 0x30a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xa8c
-  __TEXT.__const: 0x9848
-  __TEXT.__gcc_except_tab: 0xcafc
-  __TEXT.__cstring: 0x51e8
-  __TEXT.__oslogstring: 0x35c4d
+  __TEXT.__objc_methlist: 0xacc
+  __TEXT.__const: 0x9da0
+  __TEXT.__gcc_except_tab: 0xeb00
+  __TEXT.__cstring: 0x5b20
+  __TEXT.__oslogstring: 0x3be28
   __TEXT.__objc_classname: 0x1ea
-  __TEXT.__objc_methname: 0x37e4
-  __TEXT.__objc_methtype: 0x1990
+  __TEXT.__objc_methname: 0x3946
+  __TEXT.__objc_methtype: 0x1a2c
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x3d68
-  __DATA_CONST.__auth_got: 0x7f0
-  __DATA_CONST.__got: 0x4b8
+  __TEXT.__unwind_info: 0x4188
+  __DATA_CONST.__auth_got: 0x800
+  __DATA_CONST.__got: 0x580
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x8018
-  __DATA_CONST.__cfstring: 0x5860
+  __DATA_CONST.__const: 0x8560
+  __DATA_CONST.__cfstring: 0x60e0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__objc_intobj: 0x90
   __DATA.__objc_const: 0x1168
-  __DATA.__objc_selrefs: 0x1028
+  __DATA.__objc_selrefs: 0x1098
   __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0x280
-  __DATA.__data: 0x430
-  __DATA.__bss: 0x550
-  __DATA.__common: 0x48
+  __DATA.__data: 0x438
+  __DATA.__bss: 0x508
+  __DATA.__common: 0x120
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
+  - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4885007D-B8EE-39DF-957E-9DE2CD8864E4
-  Functions: 3251
-  Symbols:   421
-  CStrings:  4466
+  UUID: 0805B8D8-EEDC-3BE4-BEFA-A6C4F14CF32C
+  Functions: 3450
+  Symbols:   448
+  CStrings:  4850
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFGetTypeID
+ _OBJC_CLASS_$_NSBundle
+ __CFXPCCreateXPCObjectFromCFObject
+ _compression_stream_destroy
+ _compression_stream_init
+ _compression_stream_process
+ _kSAAboutPrivacy
+ _kSAAboutPrivacyDescription
+ _kSAAlwaysPlaySound
+ _kSAAlwaysPlaySoundDescription
+ _kSAEarthquakeAlert
+ _kSAEarthquakeAlertsDescription
+ _kSAEarthquakeAlertsDescriptionForWatch
+ _kSAEmptyScreen
+ _kSAEmptyScreenDescription
+ _kSAEnabledByDefault
+ _kSAImprovedAlertDelivery
+ _kSAImprovedAlertDeliveryDescription
+ _kSAOtherAlerts
+ _kSAOtherAlertsDescription
+ _kSAOtherAlertsDescriptionForWatch
+ _kSASafetyAlertsMainSwitchDescription
+ _kSASafetyAlertsMainSwitchName
+ _kSASwitchDescription
+ _kSASwitchHeading
+ _kSASwitchHeadingLabel
+ _kSASwitchLink
+ _kSASwitchName
+ _kSASwitchSupported
+ _kSAUserConfigurable
- _CFDictionaryGetValue
- __CTServerConnectionGetCellBroadcastConfig
- __CTServerConnectionGetCellBroadcastSettingForAlertType
- _objc_retain_x13
CStrings:
+ ""
+ "/System/Library/UserNotifications/Bundles/com.apple.safetyalerts.bundle"
+ "/System/Library/UserNotifications/Bundles/com.apple.safetyalerts.gen.bundle"
+ "ABOUT_PRIVACY_LINK"
+ "ABOUT_PRIVACY_SWITCH_STATE"
+ "ALWAYS_PLAY_SOUND_SWITCH_STATE"
+ "ALWAYS_PLAY_SOUND_SWITCH_VISIBLE"
+ "AboutPrivacy"
+ "AlwaysPlaySound"
+ "B40@0:8{vector<std::string, std::allocator<std::string>>=^v^v{?=^v}}16"
+ "Base64 decode failed"
+ "CellBroadcastSetting%@EnhancedDeliveryPref"
+ "CriticalSafetyAlertsMain"
+ "Decompression failed"
+ "EARTHQUAKE_ALERTS_SWITCH_STATE"
+ "EARTHQUAKE_ALERTS_SWITCH_VISIBLE"
+ "EARTHQUAKE_LEARN_MORE_LINK"
+ "EMPTY_SCREEN_SWITCH_STATE"
+ "Emergency"
+ "Empty base64 data"
+ "EmptyScreenSwitch"
+ "Federal Emergency Management System"
+ "ForceDisableEQDistributionOverCellular"
+ "ForceDisableGeneralSafetyAlertsDistributionOverCellular"
+ "IMPROVED_ALERT_DELIVERY_SWITCH_STATE"
+ "IMPROVED_ALERT_DELIVERY_SWITCH_VISIBLE"
+ "Imminent Threat Alert"
+ "ImprovedAlertDelivery"
+ "Invalid input data"
+ "MAIN_SWITCH_VISIBLE"
+ "OTHER_ALERTS_LEARN_MORE_LINK"
+ "OTHER_ALERTS_SWITCH_STATE"
+ "OTHER_ALERTS_SWITCH_VISIBLE"
+ "Other"
+ "OtherAlerts"
+ "RegionalSafetyAlertsDelivery_v1"
+ "SAFETY_ALERTS_EARTHQUAKE_ALERT_NEARBY"
+ "SAFETY_ALERTS_EARTHQUAKE_ALERT_TITLE"
+ "SAFETY_ALERTS_EARTHQUAKE_ALERT_UPDATE"
+ "SafetyAlertsSettingsDictionary"
+ "aboutPrivacyLink"
+ "aboutPrivacySwitchVisible"
+ "alerts"
+ "alwaysPlaySoundSwitchVisible"
+ "alwaysPlaySwitchState"
+ "apnsTopic"
+ "apnsTopicKey"
+ "bundleWithPath:"
+ "cacheTTLSeconds"
+ "calculateRegionSpanForGeometry:userLocation:"
+ "channelList"
+ "com.apple.SafetyAlerts.SADisplayed"
+ "com.apple.aps.buteo.safetyalert"
+ "com.apple.aps.gyps.safetyalert"
+ "com.apple.safetyalerts.gen"
+ "compressed_data"
+ "d24@0:8d16"
+ "d40@0:8^{SAGeometry=@B{Circle=ddd}i}16{CLLocationCoordinate2D=dd}24"
+ "decompressUserInfo:"
+ "dictionary"
+ "earthquakeLearnMoreLink"
+ "earthquakeSwitchState"
+ "earthquakeSwitchVisible"
+ "earthquake_alerts"
+ "emptyScreenSwitchVisible"
+ "featureSupportedRegion"
+ "findOptimalZoomLevelForRegionSpan:"
+ "genSafetyAlertsUIExtension"
+ "improvedAlertDeliveryEnabled"
+ "improvedAlertDeliverySwitchVisible"
+ "improvedAlertSwitchState"
+ "initWithBase64EncodedString:options:"
+ "instructions"
+ "isEarthquakeSwitchEnabled"
+ "isImminentThreatSwitchEnabled"
+ "isImprovedAlertDeliverySwitchEnabled"
+ "isSafetyAlertsSwitchStateUpdatedFromMA"
+ "localizedStringForKey:value:table:"
+ "mainSwitchVisible"
+ "mutableCopy"
+ "otherAlertsLearnMoreLink"
+ "otherAlertsSwitchState"
+ "otherAlertsSwitchVisible"
+ "payloadType"
+ "postGeneralAlertRichNotification:"
+ "readOldSwImprovedAlertDeliveryState"
+ "regionDefinition_v1"
+ "regionId"
+ "regionName"
+ "registerTopics:"
+ "removeObjectForKey:"
+ "saGetSafetyAlertsSettingsSpecifiers"
+ "saSetSafetyAlertsSettingsSpecifiers"
+ "sac3x.caf"
+ "safetyAlert"
+ "safetyAlertsSettings"
+ "setValue:forKey:"
+ "settings"
+ "settingsData"
+ "settingsPageVisited"
+ "settingsUpdate:isImprovedAlertStateEnabled:"
+ "synchronize"
+ "topicName"
+ "typeOfAlert"
+ "userSettingParams_v1"
+ "v12@?0i8"
+ "v36@?0i8{set<std::pair<std::string, std::string>, std::less<std::pair<std::string, std::string>>, std::allocator<std::pair<std::string, std::string>>>={__tree<std::pair<std::string, std::string>, std::less<std::pair<std::string, std::string>>, std::allocator<std::pair<std::string, std::string>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}12"
+ "{\"msg%{public}.0s\":\"#System,isBleDiscoveryAllowed\", \"isBLEDiscoveryDefaultOnSupported\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#ar,submitAdoptionRateMetrics\", \"isAmberAlertEnabled\":%{public}hhd, \"isEmergencyAlertEnabled\":%{public}hhd, \"isImprovedAlertDeliveryENabled\":%{public}hhd, \"isMagnetMode\":%{public}hhd, \"isPublicSafetyEnabled\":%{public}hhd, \"isSubscribed\":%{public}hhd, \"isTinkerWatch\":%{public}hhd, \"userInCoveredRegion\":%{private}hhd, \"maContentVersion\":%{public}d, \"maCompatibilityVersion\":%{public}d, \"isEarthquakeSwitchEnabled\":%{private}hhd, \"isImminentThreatSwitchEnabled\":%{private}hhd, \"isImprovedAlertDeliverySwitchEnabled\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#asset,#rba, geometryId not a dictionary\"}"
+ "{\"msg%{public}.0s\":\"#asset,#rba, region info not an array\"}"
+ "{\"msg%{public}.0s\":\"#asset,#rba, region not an array\"}"
+ "{\"msg%{public}.0s\":\"#asset,#rba, regionList not an array\"}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,\", \"rba\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,\", \"rba\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,\"}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,Object\", \"channelList\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,Object\", \"fAsset.typeOfAlert\":%{public}d, \"fAsset.topicName\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,Object\", \"geometryId\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,Object\", \"region\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,Object\", \"regionBasedAsset\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,Object\", \"regionDefinition\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,Object\", \"regionId\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,Object\", \"regionInfoList\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,Object\", \"regionName\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,RegionalSafetyAlertsDelivery_v1\"}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,d-Object\", \"d\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,loadRegionInformationFromDictionary\", \"d\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,log\", \"channel\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,log\", \"regionId\":%{private, location:escape_only}s, \"numberOfChannel\":%{private}ld}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,log\", \"regionInformation Size\":%{private}d, \"alertsDistributionInfo Size\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,log\", \"regionName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,log\", \"typeOfAlert\":%{private}d, \"regionList.size()\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,read region asset from file\"}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,region info not a dictionary\"}"
+ "{\"msg%{public}.0s\":\"#asset,#rba,regionDefinition_v1\"}"
+ "{\"msg%{public}.0s\":\"#blecore,areAllGatesOpenForAdvertiser\", \"isIgneousCapable\":%{private}hhd, \"isIgneousEnabled\":%{private}hhd, \"isEarthquakeAllowed\":%{private}hhd, \"isBluetoothEnabled\":%{private}hhd, \"isHWAllowed\":%{private}hhd, \"isLocationAuth\":%{private}hhd, \"isBLERelayFeatureEnabled\":%{private}hhd, \"isPhone\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#blecore,areAllGatesOpenForDiscovery\", \"isBluetoothEnabled\":%{private}hhd, \"isHWAllowed\":%{private}hhd, \"isLocationAuth\":%{private}hhd, \"isEarthquakeAllowed\":%{private}hhd, \"isBLERelayFeatureEnabled\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#blecore,onUserSettingsChanged\", \"eqSwitchState\":%{private}d, \"fIsEarthquakeSwitchEnabled\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#blecore,startAdvertisingIgneousAlert,earthquake switch is not enabled\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,onUserSettingsChanged\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,startAdvertisingIgneousAlert2\"}"
+ "{\"msg%{public}.0s\":\"#bm,onUserSettingsChanged\", \"isEnhancedDeliveryEnabled\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#brotli,decompressFromBase64_error\", \"error\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#brotli,decompressFromBase64_success\", \"base64_size\":%{private}d, \"compressed_size\":%{private}d, \"decompressed_size\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#brotli,decompression_error\", \"error\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#brotli,decompression_incomplete\", \"input_size\":%{private}d, \"final_status\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#brotli,decompression_success\", \"input_size\":%{private}d, \"output_size\":%{private}d, \"compression_ratio\":\"%{private}f\"}"
+ "{\"msg%{public}.0s\":\"#brotli,stream_finalize_error\", \"input_size\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#brotli,stream_init_failed\", \"status\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#brotli,stream_process_error\", \"input_size\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#ch,subscribeRequest\", \"channel\":%{private, location:escape_only}s, \"topic\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#ch,subscribeRequest,AlreadySubscribed\", \"channel\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#ch,subscribeRequest,invalid topic\"}"
+ "{\"msg%{public}.0s\":\"#chNg,#getDitheringChannelAndTopicForOtherAlerts,\", \"isRegistrationAllowed\":%{public}d, \"isRegionBasedChannelAllowed\":%{public}d, \"isCellularChannelAllowed\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#chNg,#getDitheringChannelAndTopicForOtherAlerts,UI switch is off, not registering\"}"
+ "{\"msg%{public}.0s\":\"#chNg,#getDitheringChannelAndTopicForOtherAlerts,dithering other alert\", \"channelNameAndTopic count\":%{public}ld}"
+ "{\"msg%{public}.0s\":\"#chNg,#getDitheringChannelAndTopicForOtherAlerts,dithering other alert\", \"encodedChannelName\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#chNg,#getDitheringChannelAndTopicForOtherAlerts,empty channel List\"}"
+ "{\"msg%{public}.0s\":\"#chNg,#getDitheringChannelAndTopicForOtherAlerts,not allowed to register channels\"}"
+ "{\"msg%{public}.0s\":\"#chNg,#getImprovedAlertDeliveryChannelsAndTopicForEarthquake\", \"isRegionBasedChannelAllowed\":%{public}d, \"isCellularChannelAllowed\":%{public}d, \"isRegistrationAllowed\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#chNg,#getImprovedAlertDeliveryChannelsAndTopicForEarthquake,not allowed to register other Alert wifi channels\"}"
+ "{\"msg%{public}.0s\":\"#chNg,#getImprovedAlertDeliveryChannelsAndTopicForEarthquake,other alert wifi\", \"channelNameAndTopic count\":%{public}ld}"
+ "{\"msg%{public}.0s\":\"#chNg,#getRBDChannelsListForAlertType\", \"eqChannels count\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#chNg,#getRBDChannelsListForAlertType\", \"otherAlertsDitheringChannels count\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#chNg,#getRBDChannelsListForAlertType\", \"otherAlertsWifiChannels count\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#chNg,#getRBDChannelsListForAlertType,location not in geometry\"}"
+ "{\"msg%{public}.0s\":\"#chNg,#getRBDChannelsListForAlertType,regionInfo not matching\"}"
+ "{\"msg%{public}.0s\":\"#chNg,#getWifiChannelAndTopicForOtherAlerts,\", \"isRegistrationAllowed\":%{public}d, \"isRegionBasedChannelAllowed\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#chNg,#getWifiChannelAndTopicForOtherAlerts,empty channel List\"}"
+ "{\"msg%{public}.0s\":\"#chNg,#getWifiChannelAndTopicForOtherAlerts,not allowed to register channels\"}"
+ "{\"msg%{public}.0s\":\"#chNg,#getWifiChannelAndTopicForOtherAlerts,not allowed to register other Alert wifi channels\", \"isRegionBasedChannelAllowed\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#chNg,#getWifiChannelAndTopicForOtherAlerts,other alert wifi\", \"channelNameAndTopic count\":%{public}ld, \"encodedChannelName\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#chNg,#getWifiChannelsAndTopicForEarthquake\", \"isRegionBasedChannelAllowed\":%{public}d, \"isRegistrationAllowed\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#chNg,#getWifiChannelsAndTopicForEarthquake,Eq\", \"channelNameAndTopic count\":%{public}ld, \"encodedChannelName\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#chNg,#getWifiChannelsAndTopicForEarthquake,empty channel List\"}"
+ "{\"msg%{public}.0s\":\"#chNg,#getWifiChannelsAndTopicForEarthquake,not allowed to register earthquake channels\", \"isRegionBasedChannelAllowed\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#chNg,#getWifiChannelsAndTopicForEarthquake,not allowed to register other Alert wifi channels\"}"
+ "{\"msg%{public}.0s\":\"#chNg,#updateRegionBasedDistributionChannels\", \"channelSet count\":%{public}ld}"
+ "{\"msg%{public}.0s\":\"#chNg,#updateRegionBasedDistributionChannels\", \"typeOfAlert\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#channel,Created SACloudChannelsInterface\", \"channelTopics size\":%{public}ld, \"channelTopics\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#channel,Created SACloudChannelsInterface\", \"topic\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#channel,Received push message\", \"message\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#channel,decompressUserInfo,JSON parse failed, returning nil\", \"error\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#channel,decompressUserInfo,decompressed\", \"decompressed_length\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#channel,decompressUserInfo,decompressed_alerts_array\", \"alerts_count\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#channel,decompressUserInfo,decompression failed, returning nil\"}"
+ "{\"msg%{public}.0s\":\"#channel,decompressUserInfo,expected array but got different type, returning nil\", \"object_class\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#channel,decompressUserInfo,failed to create NSData from string, returning nil\"}"
+ "{\"msg%{public}.0s\":\"#channel,decompressUserInfo,failed to create NSString from UTF8, returning nil\"}"
+ "{\"msg%{public}.0s\":\"#channel,decompressUserInfo,found compressed data\", \"base64_length\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#channel,decompressUserInfo,no compressed_data key, passing through\"}"
+ "{\"msg%{public}.0s\":\"#channel,decompressUserInfo,returning_result\", \"result_keys_count\":%{private}d, \"result\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#channel,decompressUserInfo,success\", \"json_class\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#channel,decompression returned nil, dropping message\"}"
+ "{\"msg%{public}.0s\":\"#channel,empty_alerts_array\"}"
+ "{\"msg%{public}.0s\":\"#channel,forwarding_last_alert\", \"last_alert_index\":%{private}d, \"total_alerts_skipped\":%{private}d, \"alert_keys_count\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#channel,last_alert_not_dict\", \"last_alert_index\":%{private}d, \"alert_class\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#channel,processing_alerts_array\", \"alerts_count\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#channel,processing_single_alert_or_other_data\"}"
+ "{\"msg%{public}.0s\":\"#chmgr,addChannel invalid channel proxy\"}"
+ "{\"msg%{public}.0s\":\"#chmgr,addChannel\", \"channelId\":%{private, location:escape_only}s, \"channelType\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#chmgr,addChannel\", \"fTopicList count\":%{private}d, \"topicList count\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#chmgr,onUserSettingsChanged\"}"
+ "{\"msg%{public}.0s\":\"#chmgr,removeChannel invalid channel proxy\"}"
+ "{\"msg%{public}.0s\":\"#chmgr,removeChannel\", \"channelId\":%{private, location:escape_only}s, \"channelType\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#chsel,getChannels,Dithering\", \"tileIdKey\":%{private}d, \"channelPrefix\":%{private, location:escape_only}s, \"channelId\":%{private, location:escape_only}s, \"channelType\":%{private}d, \"chanTopic\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#chsel,getChannels,Non-Dithering\", \"tileIdKey\":%{private}d, \"channelPrefix\":%{private, location:escape_only}s, \"channelId\":%{private, location:escape_only}s, \"channelType\":%{private}d, \"chanTopic\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#chsel,isEarthquakeAllowed,one of preconditions failed for ingneous\"}"
+ "{\"msg%{public}.0s\":\"#chsel,isEarthquakeAllowed,state\", \"isInCountry\":%{public}hhd, \"isCompanionMode\":%{public}hhd, \"isWatch\":%{public}hhd, \"isPhone\":%{public}hhd, \"inCoverageRegion\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#chsel,isEarthquakeAllowed,state\", \"registerIgneousOnWatch\":%{public}hhd, \"registerIgneousOnPhone\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#chsel,isFeatureEnabled,\", \"fIsImprovedAlertDeliverySwitchState,\":%{public}hhd, \"ffEnabled,\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#chsel,isSARegistrationAllowed,SA not supported on watch\"}"
+ "{\"msg%{public}.0s\":\"#chsel,isSARegistrationAllowed,precondition failed\"}"
+ "{\"msg%{public}.0s\":\"#chsel,isSARegistrationAllowed,state\", \"isSaRegisterPreCheckPass\":%{public}hhd, \"isInCountry\":%{public}hhd, \"requiresTelephony\":%{public}hhd, \"isTelephonySupported\":%{public}hhd, \"isParticipating\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#chsel,onUserSettingsChanged\"}"
+ "{\"msg%{public}.0s\":\"#chsel,runChannelUpdate, after RegionBasedDistribution\", \"fCurrentChannels Size\":%{public}ld}"
+ "{\"msg%{public}.0s\":\"#chsel,runChannelUpdate, after igneous\", \"fCurrentChannels Size\":%{public}ld}"
+ "{\"msg%{public}.0s\":\"#chsel,runChannelUpdate, after livability\", \"fCurrentChannels Size\":%{public}ld}"
+ "{\"msg%{public}.0s\":\"#chsel,updateChannelListBasedOnType,\", \"type\":%{private}d, \"channelSet count\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#chsel,updateChannelListBasedOnType,\", \"type\":%{private}d, \"fCurrentChannels count\":%{private}d, \"fEarthquakeWifiChannels count\":%{private}d, \"fIgneousChannels count\":%{private}d, \"fOtherAlertsWifiChannels count\":%{private}d, \"fOtherAlertsDitheredChannels count\":%{private}d, \"fEarthquakeLivabilityChannels count\":%{private}d, \"fOtherAlertLivabilityChannels count\":%{private}d, \"fSAChannels count\":%{private}d, \"fLivabilityChannels count\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#chsel,updateIgneousLivabilityChannels,livabilityChannel\", \"tileIdKey\":%{private}d, \"channelPrefix\":%{private, location:escape_only}s, \"channelId\":%{private, location:escape_only}s, \"channelType\":%{private}d, \"chanTopic\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readUserSettingsAsset,configIsNil\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readUserSettingsAsset,main dict nil\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readUserSettingsAsset,userSettings nil\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,setting log\", \"MainSwitchVisible\":%{private}hhd, \"earthquakeSwitchVisible\":%{private}hhd, \"earthquakeSwitchState\":%{private}hhd, \"earthquakeLearnMoreLink\":%{private, location:escape_only}s, \"otherAlertsLearnMoreLink\":%{private, location:escape_only}s, \"otherAlertsSwitchVisible\":%{private}hhd, \"otherAlertsSwitchState\":%{private}hhd, \"improvedAlertSwitchVisible\":%{private}hhd, \"improvedAlertSwitchState\":%{private}hhd, \"alwaysPlaySwitchVisible\":%{private}hhd, \"alwaysPlaySwitchState\":%{private}hhd, \"emptyScreenSwitchVisible\":%{private}hhd, \"aboutPrivacySwitchVisible\":%{private}hhd, \"aboutPrivacyLink\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#ctsa,SACoreTelephonyProd\", \"edSwitchState\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#ctsa,getEnhancedDeliverySwitchState,invalidType\", \"alertName\":%{public, location:escape_only}s, \"prefKey\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#ctsa,getEnhancedDeliverySwitchState,prefNotFound\", \"alertName\":%{public, location:escape_only}s, \"prefKey\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#ctsa,getEnhancedDeliverySwitchState,success\", \"alertName\":%{public, location:escape_only}s, \"prefKey\":%{public, location:escape_only}s, \"isEnabled\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#ctsa,getEnhancedDeliverySwitchState,success\", \"enhancedDeliveryPref\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#ctsa,onCarrierBundleChangedNotifFromCT for SA value nil\", \"slotID\":%{private}ld}"
+ "{\"msg%{public}.0s\":\"#ctsa,onCarrierBundleChangedNotifFromCT for SA\", \"isEQKillEnabled\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#ctsa,onCarrierBundleChangedNotifFromCT for SA\", \"isOtherAlertKillEnabled\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#ctsa,onCarrierBundleChangedNotifFromCT for SA\", \"killEQObject\":%{private, location:escape_only}@, \"killSAObject\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#ctsa,onCarrierBundleChangedNotifFromCT for SA\", \"slotID\":%{private}ld, \"val\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#ctsa,onCarrierBundleChangedNotifFromCT\", \"eqKillPresent\":%{public}hhd, \"saKillPresent\":%{public}hhd, \"fIsEQKillSwitchPresent[kSlot1]\":%{public}hhd, \"fIsEQKillSwitchPresent[kSlot2]\":%{public}hhd, \"fIsSAKillSwitchPresent[kSlot1]\":%{public}hhd, \"fIsSAKillSwitchPresent[kSlot2]\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#ctsa,onOperatorBundleChangedNotifFromCT for SA,failed\", \"error\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#ctsa,onOperatorBundleChangedNotifFromCT no carrier bundle SA\"}"
+ "{\"msg%{public}.0s\":\"#daemon,handleSettingsFromCompanion\", \"settingsDict\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#daemon,handleSettingsFromCompanion\"}"
+ "{\"msg%{public}.0s\":\"#daemon,handleSettingsFromCompanion,nil settingsDict\"}"
+ "{\"msg%{public}.0s\":\"#daemon,handleSettingsFromCompanion,notWatch\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onAlertReceived,push\", \"alert\":%{private, location:escape_only}s, \"IncomingInterface\":%{private, location:escape_only}@, \"alertInfo.fApnsTopic\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#daemon,onAlertRelayedFromCompanion,settingsPayload\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onCarrierSettingsChanged\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onChannelUpdate,afterCFUUpdate\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onChannelUpdate,beforeCFUUpdate\", \"isIASwitchVisible\":%{public}hhd, \"isIASwitchEnabled\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#daemon,onChannelUpdate,deferringCFUUpdate,locationOrCountryNotReady\", \"isCountryKnown\":%{public}hhd, \"isLocationValid\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#daemon,onCompanionNearbyChanged\", \"isNearby\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#daemon,onSafetyAlertReceived,fIncomingMessageInterface,cell\", \"interface\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#daemon,onSafetyAlertReceived,fIncomingMessageInterface,unknown\", \"interface\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#daemon,onSafetyAlertReceived,fIncomingMessageInterface,wifi\", \"interface\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#daemon,onSafetyAlertReceived,forwarding to GeneralSafetyAlertDisplay\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onUserSettingsChanged,afterCFUUpdate\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onUserSettingsChanged,beforeCFUUpdate\", \"isIASwitchVisible\":%{public}hhd, \"isIASwitchEnabled\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#daemon,onUserSettingsChanged,deferringCFUUpdate,locationOrCountryNotReady\", \"isCountryKnown\":%{public}hhd, \"isLocationValid\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#daemon,processIgneousAlert\", \"alertInfo.fApnsTopic\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#daemon,processIgneousAlert,send over BLE is disabled\"}"
+ "{\"msg%{public}.0s\":\"#daemon,pushSafetyAlertsSettingsToCompanion\"}"
+ "{\"msg%{public}.0s\":\"#daemon,pushSafetyAlertsSettingsToCompanion,notSupported\"}"
+ "{\"msg%{public}.0s\":\"#daemon,pushSafetyAlertsSettingsToCompanion,sending\", \"companionMessage\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#daemonInterfaceProd,set settingsPreference\", \"isEarthquakeAlertsEnabled\":%{public}d, \"isOtherAlertsEnabled\":%{public}d, \"isAlwaysPlaySoundEnabled\":%{public}d, \"isImprovedAlertDeliveryEnabled\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#daemonInterfaceProd,set settingsPreference\", \"message\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#daemonInterfaceProd,set settingsPreference\", \"settingsData\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#daemonInterfaceProd,settingsPageVisited\", \"message\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#daemonInterfaceProd,settingsPreference invalid tracker\"}"
+ "{\"msg%{public}.0s\":\"#daemonInterfaceProd,settingsPreference\", \"message\":%{private, location:escape_only}s, \"userSettings\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#daemonInterfaceProd,settingsPreference\", \"reply\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#dbg,#asset,getRegionBasedDistributionAssetData\"}"
+ "{\"msg%{public}.0s\":\"#gap,parse,invalid info entry\"}"
+ "{\"msg%{public}.0s\":\"#gap,parse,missingHash received\"}"
+ "{\"msg%{public}.0s\":\"#gap,parse,no valid info Array\"}"
+ "{\"msg%{public}.0s\":\"#gap,parse,no valid info entries\"}"
+ "{\"msg%{public}.0s\":\"#gap,parse,success\", \"uid\":%{private, location:escape_only}s, \"sessionId\":%{private, location:escape_only}s, \"status\":%{private}d, \"msgType\":%{private}d, \"urgency\":%{private}d, \"severity\":%{private}d, \"certainty\":%{private}d, \"infoEntriesCount\":%{private}d, \"cacheTTLSeconds\":%{private}d, \"hasGeometry\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#gap,parse,uid empty\"}"
+ "{\"msg%{public}.0s\":\"#gap,parse,uid nil\"}"
+ "{\"msg%{public}.0s\":\"#gsadisp,display\", \"uid\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#gsadisp,display,done\", \"uid\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#gsadisp,display,geometry available\"}"
+ "{\"msg%{public}.0s\":\"#gsadisp,display,invalid uid\"}"
+ "{\"msg%{public}.0s\":\"#gsadisp,display,no info entries\"}"
+ "{\"msg%{public}.0s\":\"#gsadisp,post\", \"uid\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#gsadisp,post,language fallback to first entry\"}"
+ "{\"msg%{public}.0s\":\"#gsadisp,post,no valid cmamLongText or cmamText found\"}"
+ "{\"msg%{public}.0s\":\"#gsadisp,post,no valid info entry found\"}"
+ "{\"msg%{public}.0s\":\"#gsadisp,post,sending to companion\"}"
+ "{\"msg%{public}.0s\":\"#gsadisp,post,sending to userNotification\", \"notifDetails\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#gsadisp,post,userNotification\"}"
+ "{\"msg%{public}.0s\":\"#gsadisp,post,userNotification,not supported platform\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,shouldCache,not enabled, exiting\"}"
+ "{\"msg%{public}.0s\":\"#notif,#warning,postGeneralAlertRichNotification,invalid regionSpanMeters\"}"
+ "{\"msg%{public}.0s\":\"#notif,#warning,postGeneralAlertRichNotification,invalidArgs\"}"
+ "{\"msg%{public}.0s\":\"#notif,calculateRegionSpanForGeometry\", \"maxDistanceFromUser\":\"%{private}0.1f\", \"regionSpanMeters\":\"%{private}0.1f\"}"
+ "{\"msg%{public}.0s\":\"#notif,calculateRegionSpanForGeometry,invalid geometry\"}"
+ "{\"msg%{public}.0s\":\"#notif,calculateRegionSpanForGeometry,no polygons\"}"
+ "{\"msg%{public}.0s\":\"#notif,postGeneralAlertRichNotification,contentInfo\", \"notifDetails\":%{sensitive, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#notif,postGeneralAlertRichNotification,invalidContent\", \"title\":%{private, location:escape_only}@, \"body\":%{private, location:escape_only}@, \"attribution\":%{private, location:escape_only}@, \"uid\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#notif,postGeneralAlertRichNotification,mapDisplay\", \"enabled\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#notif,postNotification,invalidContents\", \"title\":%{private, location:escape_only}@, \"body\":%{private, location:escape_only}@, \"toneFile\":%{private, location:escape_only}@, \"uid\":%{private, location:escape_only}@, \"alertInterface\":%{private, location:escape_only}@, \"isRelayed\":%{private, location:escape_only}@, \"level\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#notif,postSafetyAlertNotification\", \"d\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#notif,warning,typeInvalid\"}"
+ "{\"msg%{public}.0s\":\"#notif,warning,typeMissing\"}"
+ "{\"msg%{public}.0s\":\"#rm,onUserSettingsChanged\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,Asset not ready yet\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getAboutPrivacyLink\", \"aboutPrivacyLink MA\":%{public, location:escape_only}s, \"aboutPrivacyLink\":%{public, location:escape_only}s, \"preferenceValue\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getAlwaysPlayMADefaultValue\", \"alwaysPlaySwitchState\":%{public}hhd, \"alwayPlaySoundSwitchState\":%{public}hhd, \"preferenceValue\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getAlwaysPlaySoundSwitchState\", \"fIsAlwaysPlaySoundSwitchState\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getEarthquakeAlertSwitchState\", \"fIsEarthquakeAlertsSwitchState\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getEarthquakeLearnMoreLink\", \"earthquakeLearnMoreLink\":%{public, location:escape_only}s, \"preferenceValue\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getEarthquakeMADefaultValue\", \"earthquakeSwitchState MA\":%{public}hhd, \"earthquakeSwitchState\":%{public}hhd, \"preferenceValue\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getImprovedAlertDeliverySwitchState\", \"fIsImprovedAlertDeliverySwitchState\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getImprovedAlertMADefaultValue\", \"improvedAlertSwitchState MA\":%{public}hhd, \"iadSwitchState\":%{public}hhd, \"preferenceValue\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getOtherAlertsLearnMoreLink\", \"otherAlertsLearnMoreLink MA\":%{public, location:escape_only}s, \"OtherAlertLearnLink\":%{public, location:escape_only}s, \"preferenceValue\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getOtherAlertsMADefaultValue\", \"OtherAlertsSwitchState MA\":%{public}hhd, \"OtherAlertsSwitchState\":%{public}hhd, \"preferenceValue\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getOtherAlertsSwitchState\", \"fIsOtherAlertsSwitchState\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefStateFromDisk empty dictionary\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefStateFromDisk subDictionary or state invalid\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefStateFromDisk\", \"AlwayPlaySound\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefStateFromDisk\", \"EqStatus\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefStateFromDisk\", \"ImprovedAlert\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefStateFromDisk\", \"OtherAlerts\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefStateFromDisk\", \"key\":%{public, location:escape_only}@, \"value\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,isAboutPrivacySwitchVisible\", \"privacySwitchVisible\":%{public}hhd, \"privacySwitchVisible\":%{public}hhd, \"preferenceValue\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,isAlwaysPlaySwitchVisible\", \"alwayPlaySwitchVisible\":%{public}hhd, \"alwaysPlaySwitchVisible\":%{public}hhd, \"preferenceValue\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,isEarthquakeSwitchVisible\", \"earthquakeSwitchVisible MA\":%{public}hhd, \"earthquakeSwitchVisible\":%{public}hhd, \"preferenceValue\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,isEmptyScreenSwitchVisible\", \"emptyScreenSwitchVisible\":%{public}hhd, \"emptyScreenSwitchState\":%{public}hhd, \"preferenceValue\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,isImprovedAlertSwitchVisible\", \"improvedAlertSwitchVisible MA\":%{public}hhd, \"iadSwitchVisible\":%{public}hhd, \"preferenceValue\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,isMainSwitchVisibile\", \"MainSwitchVisible MA\":%{public}hhd, \"mainSwitchVisible\":%{public}hhd, \"preferenceValue\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,isOtherAlertsVisible\", \"otherAlertsSwitchVisible MA\":%{public}hhd, \"otherAlertsSwitchVisible\":%{public}hhd, \"preferenceValue\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,notifyUserSettingsUpdated updated\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,onAssetReceived\", \"taskData->reason\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,onAssetReceived\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,onAssetReceived,first run, copy old settings\", \"edState\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,onAssetReceived,first run, copy old settings\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,onCarrierSettingsChanged\", \"eqKillSwitchPresent\":%{public}d, \"fKillGridSubscription\":%{public}d, \"saKillSwitchPresent\":%{public}d, \"fKillDitheringSubscription\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,onCarrierSettingsChanged\", \"eqKillSwitchPresent\":%{public}d, \"fKillGridSubscription\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,onCarrierSettingsChanged\", \"saKillSwitchPresent\":%{public}d, \"fKillDitheringSubscription\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,onLocationChanged\", \"isNearby\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,onLocationChanged\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,onUserSettingsUpdated\", \"fIsImprovedAlertDeliverySwitchState\":%{private}d, \"improvedAlertDeliveryState\":%{private}d, \"fIsEarthquakeAlertsSwitchState\":%{private}d, \"eqState\":%{private}d, \"fIsOtherAlertsSwitchState\":%{private}d, \"otherAlertState\":%{private}d, \"fIsAlwaysPlaySoundSwitchState\":%{private}d, \"alwaysPlaySoundState\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,readUserPref no settings found\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,readUserPref\", \"saDetails\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,readUserPref\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,readUserPrefAndBroadcast main switch is disabled\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,readUserPrefAndBroadcast\", \"earthquakeAlertsState\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,readUserPrefAndBroadcast\", \"fIsAlwaysPlaySoundSwitchState\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,readUserPrefAndBroadcast\", \"fIsImprovedAlertDeliverySwitchState\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,readUserPrefAndBroadcast\", \"otherAlertsState\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,readUserPrefWithCallback\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,updateUserPref\", \"key\":%{public, location:escape_only}@, \"value\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,updateUserPref\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPref no settings data\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPref\", \"alwaysPlaySoundState\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPref\", \"earthquakeAlertsState\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPref\", \"improvedAlertDeliveryState\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPref\", \"otherAlertsState\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPref\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefFirstTime\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefFirstTime,data exist don't re-write default values.\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefWithMAValue\", \"mobileAssetSettingsConfig\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefWithMAValue\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefWithMAValue,first SA init\"}"
+ "{\"msg%{public}.0s\":\"#saanalytics,metric submitted\", \"forceSubmission\":%{public}d, \"isWEAReceived\":%{public}d, \"isSAReceived\":%{public}d, \"alertMetricVectorSize\":%{public}d, \"submissionTimerMapSize\":%{public}d, \"alertTextID\":%{private}ld, \"alertMetric->fInfo.fApnsTopic\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saanalytics,onUserSettingsChanged\"}"
+ "{\"msg%{public}.0s\":\"#uimetrics,SAUiDisplayMetricsEntry,postToAnalytics,values\", \"bleAlertID\":%{private, location:escape_only}@, \"isFirstUnlocked\":%{private, location:escape_only}@, \"isInLOI\":%{sensitive, location:escape_only}@, \"isLocked\":%{private, location:escape_only}@, \"transport\":%{private, location:escape_only}@, \"userTapped\":%{private, location:escape_only}@, \"postToTapLatency\":%{private, location:escape_only}@, \"serverToPostingLatency\":%{private, location:escape_only}@, \"tapToDisplayLatency\":%{private, location:escape_only}@, \"serverToTapLatency\":%{private, location:escape_only}@, \"isLockedDuringPosting\":%{private, location:escape_only}@, \"isLockedDuringSubmission\":%{private, location:escape_only}@, \"isRelayedAlert\":%{private, location:escape_only}@, \"level\":%{private, location:escape_only}@, \"alertType\":%{private}d, \"environmentId\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#uimetrics,setAlertType,invokedOnUninitializedObject\"}"
+ "{vector<std::string, std::allocator<std::string>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
- "Actualización de la alerta sísmica"
- "AppleSafetyAlertsAvailability"
- "EmergencyAlertsPref"
- "Enabled"
- "EnhancedDeliveryAvailability"
- "EnhancedDeliveryPref"
- "Sismo detectado cerca"
- "enhancedDeliveryPageVisited"
- "localAwarenessEnabled"
- "{\"msg%{public}.0s\":\"#System,isBleDiscoveryAllowed\", \"isBLEDiscoveryDefaultOnSupported\":%{private}hhd, \"isEmergencyAlertSwitchEnabled\":%{private}hhd, \"isEnhancedDeliverySwitchEnabled\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#ar,submitAdoptionRateMetrics\", \"isAmberAlertEnabled\":%{public}hhd, \"isEmergencyAlertEnabled\":%{public}hhd, \"isEnhancedDeliveryEnabled\":%{public}hhd, \"isMagnetMode\":%{public}hhd, \"isPublicSafetyEnabled\":%{public}hhd, \"isSubscribed\":%{public}hhd, \"isTinkerWatch\":%{public}hhd, \"userInCoveredRegion\":%{private}hhd, \"maContentVersion\":%{public}d, \"maCompatibilityVersion\":%{public}d}"
- "{\"msg%{public}.0s\":\"#blecore,areAllGatesOpenForAdvertiser\", \"isIgneousCapable\":%{private}hhd, \"isIgneousEnabled\":%{private}hhd, \"isIgneousAllowed\":%{private}hhd, \"isBluetoothEnabled\":%{private}hhd, \"isHWAllowed\":%{private}hhd, \"isLocationAuth\":%{private}hhd, \"isBLERelayFeatureEnabled\":%{private}hhd, \"isPhone\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#blecore,areAllGatesOpenForDiscovery\", \"isBluetoothEnabled\":%{private}hhd, \"isHWAllowed\":%{private}hhd, \"isLocationAuth\":%{private}hhd, \"isSwitchEnabled\":%{private}hhd, \"isBLERelayFeatureEnabled\":%{private}hhd, \"isEnhancedDeliverySwitchEnabled\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#blecore,onUserSettingsChanged\", \"discoveryAllowed\":%{private}d, \"fIsBleDiscoveryEnabled\":%{private}d}"
- "{\"msg%{public}.0s\":\"#bm,onEnhancedDeliveryStateChanged\", \"isEnhancedDeliveryEnabled\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#ch,AlreadySubscribed\", \"channel\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#ch,subscribe\"}"
- "{\"msg%{public}.0s\":\"#ch,subscribe,Alert\"}"
- "{\"msg%{public}.0s\":\"#ch,subscribe,invalid type\"}"
- "{\"msg%{public}.0s\":\"#ch,subscribeRequest\", \"channel\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#chmgr,addChannel\", \"channelId\":%{private, location:escape_only}s, \"channelType\":%{private}d}"
- "{\"msg%{public}.0s\":\"#chmgr,onEnhancedDeliveryEnabled,\", \"isEnabled,\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#chmgr,removeChannel\", \"channelId\":%{private, location:escape_only}s, \"channelType\":%{private}d}"
- "{\"msg%{public}.0s\":\"#chsel,getChannels,Dithering\", \"tileIdKey\":%{private}d, \"channelPrefix\":%{private, location:escape_only}s, \"channelId\":%{private, location:escape_only}s, \"channelType\":%{private}d}"
- "{\"msg%{public}.0s\":\"#chsel,getChannels,Non-Dithering\", \"tileIdKey\":%{private}d, \"channelPrefix\":%{private, location:escape_only}s, \"channelId\":%{private, location:escape_only}s, \"channelType\":%{private}d}"
- "{\"msg%{public}.0s\":\"#chsel,isFeatureEnabled,\", \"fIsEnhanceDeliverySwitchEnabled,\":%{public}hhd, \"ffEnabled,\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#chsel,onEnhancedDeliveryEnabled,\", \"isEnabled,\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#chsel,updateIgneousChannels,one of preconditions failed for ingneous\"}"
- "{\"msg%{public}.0s\":\"#chsel,updateIgneousChannels,state\", \"registerIgneousOnWatch\":%{public}hhd, \"registerIgneousOnPhone\":%{public}hhd, \"registerLivability\":%{public}hhd, \"isSAEWEnabled\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#chsel,updateIgneousLivabilityChannels,livabilityChannel\", \"tileIdKey\":%{private}d, \"channelPrefix\":%{private, location:escape_only}s, \"channelId\":%{private, location:escape_only}s, \"channelType\":%{private}d}"
- "{\"msg%{public}.0s\":\"#ctsa,GetCellBroadcastConfig error\"}"
- "{\"msg%{public}.0s\":\"#ctsa,com.apple.CTTelephonyCenter\", \"eDel\":%{public}d, \"eDelAvl\":%{public}d, \"saAvl\":%{public}d, \"saEmergencyAvl\":%{public}d, \"saMotionHarvestPref\":%{public}d}"
- "{\"msg%{public}.0s\":\"#ctsa,onEnhanceDeliveryStateChange,\", \"enhancedDeliveryState,\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#ctsa,onLocationChanged\", \"isEDRecentlyUpdated\":%{public}d, \"curTime\":\"%{public}0.3f\", \"fLastEDUpdateTime_s\":\"%{public}0.3f\"}"
- "{\"msg%{public}.0s\":\"#ctsa,onMotionHarvestPref\", \"toggle\":%{private, location:escape_only}@, \"didSucceed\":%{public}d, \"enabled\":%{public}d}"
- "{\"msg%{public}.0s\":\"#ctsa,onMotionHarvestPref\", \"toggle\":%{private, location:escape_only}@, \"errorCode\":%{public}d}"
- "{\"msg%{public}.0s\":\"#ctsa,onMotionHarvestPref\", \"toggles\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#ctsa,onMotionHarvestPref,none of the toggles exists\"}"
- "{\"msg%{public}.0s\":\"#ctsa,onMotionHarvestPref,not phone\"}"
- "{\"msg%{public}.0s\":\"#ctsa,onUserSettingsChanged\"}"
- "{\"msg%{public}.0s\":\"#daemon,onAlertReceived,push\", \"alert\":%{private, location:escape_only}s, \"IncomingInterface\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#daemon,onEnhancedDeliveryEnabled,\", \"enhancedDeliveryEnabled,\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#daemonInterfaceProd,enhancedDelivery\", \"message\":%{private, location:escape_only}s, \"isEnabled\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#daemonInterfaceProd,enhancedDeliveryPageVisited\", \"message\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#mapcache,shouldCache,not enabled exiting\"}"
- "{\"msg%{public}.0s\":\"#notif,warning,typeMissingOrInvalid\"}"
- "{\"msg%{public}.0s\":\"#rm,onEnhancedDeliveryEnabled\", \"isEnhancedDeliveryEnabled\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#saanalytics,metric submitted\", \"forceSubmission\":%{public}d, \"isWEAReceived\":%{public}d, \"isSAReceived\":%{public}d, \"alertMetricVectorSize\":%{public}d, \"submissionTimerMapSize\":%{public}d, \"alertTextID\":%{private}ld}"
- "{\"msg%{public}.0s\":\"#saanalytics,onEnhancedDeliveryEnabled\", \"isEnhancedDeliveryEnabled\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#uimetrics,SAUiDisplayMetricsEntry,postToAnalytics,values\", \"bleAlertID\":%{private, location:escape_only}@, \"isFirstUnlocked\":%{private, location:escape_only}@, \"isInLOI\":%{sensitive, location:escape_only}@, \"isLocked\":%{private, location:escape_only}@, \"transport\":%{private, location:escape_only}@, \"userTapped\":%{private, location:escape_only}@, \"postToTapLatency\":%{private, location:escape_only}@, \"serverToPostingLatency\":%{private, location:escape_only}@, \"tapToDisplayLatency\":%{private, location:escape_only}@, \"serverToTapLatency\":%{private, location:escape_only}@, \"isLockedDuringPosting\":%{private, location:escape_only}@, \"isLockedDuringSubmission\":%{private, location:escape_only}@, \"isRelayedAlert\":%{private, location:escape_only}@, \"level\":%{private, location:escape_only}@, \"environmentId\":%{private, location:escape_only}s}"
- "{vector<std::string, std::allocator<std::string>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"

```
