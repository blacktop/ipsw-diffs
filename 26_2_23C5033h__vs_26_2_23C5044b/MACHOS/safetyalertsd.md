## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-64.0.38.0.0
-  __TEXT.__text: 0xf3094
+64.0.39.0.0
+  __TEXT.__text: 0xf5900
   __TEXT.__auth_stubs: 0xfe0
   __TEXT.__objc_stubs: 0x30a0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xadc
   __TEXT.__const: 0x9dde
-  __TEXT.__gcc_except_tab: 0xecbc
-  __TEXT.__cstring: 0x5b2e
-  __TEXT.__oslogstring: 0x3cbe3
+  __TEXT.__gcc_except_tab: 0xeff0
+  __TEXT.__cstring: 0x5bef
+  __TEXT.__oslogstring: 0x3dac3
   __TEXT.__objc_classname: 0x1ea
   __TEXT.__objc_methname: 0x39b7
   __TEXT.__objc_methtype: 0x1a87
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x41c8
+  __TEXT.__unwind_info: 0x41f0
   __DATA_CONST.__auth_got: 0x800
   __DATA_CONST.__got: 0x580
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x8560
-  __DATA_CONST.__cfstring: 0x6100
+  __DATA_CONST.__const: 0x8570
+  __DATA_CONST.__cfstring: 0x61c0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x438
-  __DATA.__bss: 0x508
+  __DATA.__bss: 0x510
   __DATA.__common: 0x128
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 233E6295-9A5D-3B86-A347-7344800D2998
-  Functions: 3457
+  UUID: FF2BB73C-E7D2-32AC-AB9E-AEAB238759D0
+  Functions: 3467
   Symbols:   448
-  CStrings:  4880
+  CStrings:  4926
 
CStrings:
+ "DITHERING_CHANNEL_REFRESH_PERIOD"
+ "SAFETY_ALERTS_IMMINENT_THREAT_ALERT"
+ "apnsTopicCleanupList_v1"
+ "com.apple.aps.ardea.safetyalert"
+ "com.apple.aps.gypstw.safetyalert"
+ "com.apple.aps.mantistw.safetyalert"
+ "{\"msg%{public}.0s\":\"#chNg,#getDitheringChannelAndTopicForOtherAlerts,dithering other alert first time selecting channel\", \"subscribedChannelName\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#chNg,#getDitheringChannelAndTopicForOtherAlerts,dithering other alert\", \"subscribedChannelName\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#chNg,#getLastSubscribedChannelNameForTopic\", \"topicName\":%{private, location:escape_only}s, \"Current Channel count\":%{private}ld}"
+ "{\"msg%{public}.0s\":\"#channel,unsubcribeForgottenChannels\"}"
+ "{\"msg%{public}.0s\":\"#channel,unsubcribeForgottenChannels,\", \"topic\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#chsel,fOtherAlertsDitheredChannels cleared by time\"}"
+ "{\"msg%{public}.0s\":\"#chsel,onUserSettingsChanged\", \"fOtherAlertsDitheredChannels\":%{public}ld}"
+ "{\"msg%{public}.0s\":\"#chsel,onUserSettingsChanged\", \"improveAlertState\":%{public}hhd, \"fImproveAlertDeliveryState\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#chsel,updateChannelListBasedOnType,fOtherAlertsDitheredChannels\", \"fLastDitheringChannelUpdated_s\":\"%{private}3f\", \"fOtherAlertsDitheredChannels size\":%{private}ld}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readAPNSTopicCleanupListAsset empty\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readAPNSTopicCleanupListAsset not a string\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readAPNSTopicCleanupListAsset topic not an array\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readAPNSTopicCleanupListAsset\", \"apnsTopicList\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readAPNSTopicCleanupListAsset\", \"config\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readAPNSTopicCleanupListAsset\", \"t\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readAPNSTopicCleanupListAsset\", \"topic\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readAPNSTopicCleanupListAsset,configIsNil\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readAPNSTopicCleanupListAsset,main dict nil\"}"
+ "{\"msg%{public}.0s\":\"#daemon,#warning,onSafetyAlertReceived,Imminent Threat Switch Disabled\"}"
+ "{\"msg%{public}.0s\":\"#eff,isIgneousCapable,biomeStatus\", \"startSeconds\":\"%{private}0.1f\", \"endSeconds\":\"%{private}0.1f\", \"nwCellularStatus\":%{private, location:escape_only}s, \"nwWifiStatus\":%{private, location:escape_only}s, \"isEQSwitchEnabled\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#eff,isSaCapable,biomeStatus\", \"startSeconds\":\"%{private}0.1f\", \"endSeconds\":\"%{private}0.1f\", \"subStatus\":%{private, location:escape_only}s, \"nwCellularStatus\":%{private, location:escape_only}s, \"nwWifiStatus\":%{private, location:escape_only}s, \"isSASwitchEnabled\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#notif,postGeneralAlertRichNotification\", \"regionSpanMeters\":\"%{public}0.1f\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk empty dictionary\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk subDictionary or state invalid\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk\", \"AlwayPlaySound\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk\", \"EQ\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk\", \"ImprovedAlert\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk\", \"OtherAlerts\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk\", \"aboutPrivacy\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk\", \"emptyScreen\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk\", \"key\":%{public, location:escape_only}@, \"value\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,getUserPrefSwitchVisibilityFromDisk\", \"mainSwitch\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,onLocationAuthorized\", \"isAuthorized\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefLSOff_UseWithCaution\", \"alwaysPlaySoundState\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefLSOff_UseWithCaution\", \"earthquakeAlertsState\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefLSOff_UseWithCaution\", \"improvedAlertDeliveryState\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,writeUserPrefLSOff_UseWithCaution\", \"otherAlertsState\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#chNg,#getDitheringChannelAndTopicForOtherAlerts,dithering other alert\", \"encodedChannelName\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#eff,isIgneousCapable,biomeStatus\", \"startSeconds\":\"%{private}0.1f\", \"endSeconds\":\"%{private}0.1f\", \"subStatus\":%{private, location:escape_only}s, \"nwCellularStatus\":%{private, location:escape_only}s, \"nwWifiStatus\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#eff,isSaCapable,biomeStatus\", \"startSeconds\":\"%{private}0.1f\", \"endSeconds\":\"%{private}0.1f\", \"subStatus\":%{private, location:escape_only}s, \"nwCellularStatus\":%{private, location:escape_only}s, \"nwWifiStatus\":%{private, location:escape_only}s}"

```
