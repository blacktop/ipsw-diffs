## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-62.0.0.0.0
-  __TEXT.__text: 0xaad20
+64.0.2.0.0
+  __TEXT.__text: 0xaaccc
   __TEXT.__auth_stubs: 0xea0
   __TEXT.__objc_stubs: 0x2360
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x2f0
-  __TEXT.__const: 0x843f
-  __TEXT.__gcc_except_tab: 0xa350
-  __TEXT.__cstring: 0x4339
-  __TEXT.__oslogstring: 0x25108
+  __TEXT.__const: 0x8427
+  __TEXT.__gcc_except_tab: 0xa2f4
+  __TEXT.__cstring: 0x4351
+  __TEXT.__oslogstring: 0x25136
   __TEXT.__objc_classname: 0x1b7
   __TEXT.__objc_methname: 0x28c7
   __TEXT.__objc_methtype: 0x111e

   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x3d8
-  __DATA.__bss: 0x5a0
+  __DATA.__bss: 0x598
   __DATA.__common: 0x48
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2733
+  Functions: 2735
   Symbols:   392
-  CStrings:  3036
+  CStrings:  3037
 
CStrings:
+ "BLE:APPLE SAFETY ALERTS LIVABILITY TEST:"
+ "bleAlertUID"
+ "{\"msg%!{(MISSING)public}.0s\":\"#SALBAssetConfig,readBleConfigFromDefaults\", \"isBLERelaySupported\":%!{(MISSING)private}hhd, \"advertiseEvaluationIntervalSeconds\":%!{(MISSING)private}d, \"discoveryEvaluationIntervalSeconds\":%!{(MISSING)private}d, \"advertiseDurationSeconds\":%!{(MISSING)private}d, \"minDeviceDensityCount\":%!{(MISSING)private}d, \"minTimeBetweenPeopleDensityQuery\":%!{(MISSING)private}d, \"percent\":%!{(MISSING)private}d, \"minBatteryLevelForBLEActivity\":%!{(MISSING)private}d, \"bleCBAdvertiseRate\":%!{(MISSING)private}d, \"bleCBScanRate\":%!{(MISSING)private}d, \"bleCBScanRateScreenOff\":%!{(MISSING)private}d, \"bleDataVersion\":%!{(MISSING)private}d, \"bleAdvertisementTimePrecisionInMSec\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#SALBAssetConfig,readBleConfigFromFailSafe\", \"isBLERelaySupported\":%!{(MISSING)private}hhd, \"advertiseEvaluationIntervalSeconds\":%!{(MISSING)private}d, \"discoveryEvaluationIntervalSeconds\":%!{(MISSING)private}d, \"advertiseDurationSeconds\":%!{(MISSING)private}d, \"minBatteryLevelForBLEActivity\":%!{(MISSING)private}d, \"minDeviceDensityCount\":%!{(MISSING)private}d, \"minTimeBetweenPeopleDensityQuery\":%!{(MISSING)private}d, \"bleCBScanRate\":%!{(MISSING)private}d, \"CBScanRateBackground\":%!{(MISSING)private}d, \"bleCBAdvertiseRate\":%!{(MISSING)private}d, \"bleDataVersion\":%!{(MISSING)private}d, \"bleAdvertisementTimePrecisionInMSec\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#SALBAssetConfig,readBleConfigFromFile\", \"isBLERelaySupported\":%!{(MISSING)private}hhd, \"advertiseEvaluationIntervalSeconds\":%!{(MISSING)private}d, \"discoveryEvaluationIntervalSeconds\":%!{(MISSING)private}d, \"advertiseDurationSeconds\":%!{(MISSING)private}d, \"minBatteryLevelForBLEActivity\":%!{(MISSING)private}d, \"minDeviceDensityCount\":%!{(MISSING)private}d, \"minTimeBetweenPeopleDensityQuery\":%!{(MISSING)private}d, \"bleCBScanRate\":%!{(MISSING)private}d, \"bleCBScanRateScreenOff\":%!{(MISSING)private}d, \"bleCBAdvertiseRate\":%!{(MISSING)private}d, \"bleDataVersion\":%!{(MISSING)private}d, \"bleAdvertisementTimePrecisionInMSec\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid  advertiserTime\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid originTime\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAdvertiserTime\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#brm,onBleAlertReceived\", \"nowSeconds\":\"%!{(MISSING)public}0.7f\", \"igneousAlertInformation.bleAdvertiseTime\":\"%!{(MISSING)public}0.7f\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#iap,parseIgneousAlert\", \"source\":%!{(MISSING)private, location:escape_only}@, \"uid\":%!{(MISSING)private, location:escape_only}@, \"ingress_to_server_ts\":%!{(MISSING)private, location:escape_only}@, \"egress_from_source_ts\":%!{(MISSING)private, location:escape_only}@, \"event_origin_ts\":%!{(MISSING)private, location:escape_only}@, \"effective\":%!{(MISSING)private, location:escape_only}@, \"expires\":%!{(MISSING)private, location:escape_only}@, \"event_update_number\":%!{(MISSING)private, location:escape_only}@, \"epi_latitude\":%!{(MISSING)private, location:escape_only}@, \"epi_longitude\":%!{(MISSING)private, location:escape_only}@, \"magnitude\":%!{(MISSING)private, location:escape_only}@, \"depth\":%!{(MISSING)private, location:escape_only}@}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#iap,parseIgneousAlert\", \"source\":%!{(MISSING)private, location:escape_only}s, \"uid\":%!{(MISSING)private, location:escape_only}s, \"alertSignature\":%!{(MISSING)private, location:escape_only}s, \"bleAlertData\":%!{(MISSING)private, location:escape_only}s, \"bleAlertUID\":%!{(MISSING)private, location:escape_only}s, \"ingress_to_server_ts\":\"%!{(MISSING)private}0.3f\", \"egress_from_source_ts\":\"%!{(MISSING)private}0.3f\", \"event_origin_ts\":\"%!{(MISSING)private}0.3f\", \"effective\":\"%!{(MISSING)private}0.3f\", \"expires\":\"%!{(MISSING)private}0.3f\", \"event_update_number\":\"%!{(MISSING)private}0.3f\", \"epi_latitude\":\"%!{(MISSING)private}0.3f\", \"epi_longitude\":\"%!{(MISSING)private}0.3f\", \"magnitude\":\"%!{(MISSING)private}0.3f\", \"depth\":\"%!{(MISSING)private}0.3f\", \"mmiSize\":%!{(MISSING)private}llu, \"mmiLat\":\"%!{(MISSING)private}0.3f\", \"mmiLon\":\"%!{(MISSING)private}0.3f\", \"mmiLevel\":\"%!{(MISSING)private}0.3f\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"brm,submitMetrics\", \"isBleAdvertiser\":%!{(MISSING)private}hhd, \"wasSAReceived\":%!{(MISSING)private}hhd, \"batteryChargeLevel\":%!{(MISSING)private}d, \"bleRelayFanOutSetting\":%!{(MISSING)private}d, \"meanNumNearbyDevices\":%!{(MISSING)private}d, \"bleRelayAdvertiseDuration\":%!{(MISSING)private}d, \"alertIndex\":%!{(MISSING)private}d, \"bleReceivedRSSI\":%!{(MISSING)private}d, \"bleReceivedRSSIBucketed\":%!{(MISSING)private}d, \"bleLatencyRelativeToSATime\":\"%!{(MISSING)private}0.2f\", \"latencyRelativeToBleAdvertiseTime\":\"%!{(MISSING)private}0.2f\", \"latencyRelativeToOriginatorTime\":\"%!{(MISSING)private}0.2f\", \"alertUID\":%!{(MISSING)private, location:escape_only}s, \"bleAlertUID\":%!{(MISSING)private, location:escape_only}s, \"deviceRole\":%!{(MISSING)private, location:escape_only}s, \"pushInterface\":%!{(MISSING)private, location:escape_only}s, \"source\":%!{(MISSING)private, location:escape_only}s}"
- "DisplayAlert"
- "displayBLEAlert"
- "{\"msg%!{(MISSING)public}.0s\":\"#SALBAssetConfig,can't read displayBLEAlert\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#SALBAssetConfig,readBleConfigFromDefaults\", \"isBLERelaySupported\":%!{(MISSING)private}hhd, \"advertiseEvaluationIntervalSeconds\":%!{(MISSING)private}d, \"discoveryEvaluationIntervalSeconds\":%!{(MISSING)private}d, \"advertiseDurationSeconds\":%!{(MISSING)private}d, \"minDeviceDensityCount\":%!{(MISSING)private}d, \"minTimeBetweenPeopleDensityQuery\":%!{(MISSING)private}d, \"percent\":%!{(MISSING)private}d, \"minBatteryLevelForBLEActivity\":%!{(MISSING)private}d, \"bleCBAdvertiseRate\":%!{(MISSING)private}d, \"bleCBScanRate\":%!{(MISSING)private}d, \"bleCBScanRateScreenOff\":%!{(MISSING)private}d, \"bleDataVersion\":%!{(MISSING)private}d, \"displayBLEAlert\":%!{(MISSING)private}d, \"bleAdvertisementTimePrecisionInMSec\":%!{(MISSING)private}d}"
- "{\"msg%!{(MISSING)public}.0s\":\"#SALBAssetConfig,readBleConfigFromFailSafe\", \"isBLERelaySupported\":%!{(MISSING)private}hhd, \"advertiseEvaluationIntervalSeconds\":%!{(MISSING)private}d, \"discoveryEvaluationIntervalSeconds\":%!{(MISSING)private}d, \"advertiseDurationSeconds\":%!{(MISSING)private}d, \"minBatteryLevelForBLEActivity\":%!{(MISSING)private}d, \"minDeviceDensityCount\":%!{(MISSING)private}d, \"minTimeBetweenPeopleDensityQuery\":%!{(MISSING)private}d, \"bleCBScanRate\":%!{(MISSING)private}d, \"CBScanRateBackground\":%!{(MISSING)private}d, \"bleCBAdvertiseRate\":%!{(MISSING)private}d, \"bleDataVersion\":%!{(MISSING)private}d, \"displayBLEAlert\":%!{(MISSING)private}d, \"bleAdvertisementTimePrecisionInMSec\":%!{(MISSING)private}d}"
- "{\"msg%!{(MISSING)public}.0s\":\"#SALBAssetConfig,readBleConfigFromFile\", \"isBLERelaySupported\":%!{(MISSING)private}hhd, \"advertiseEvaluationIntervalSeconds\":%!{(MISSING)private}d, \"discoveryEvaluationIntervalSeconds\":%!{(MISSING)private}d, \"advertiseDurationSeconds\":%!{(MISSING)private}d, \"minBatteryLevelForBLEActivity\":%!{(MISSING)private}d, \"minDeviceDensityCount\":%!{(MISSING)private}d, \"minTimeBetweenPeopleDensityQuery\":%!{(MISSING)private}d, \"bleCBScanRate\":%!{(MISSING)private}d, \"bleCBScanRateScreenOff\":%!{(MISSING)private}d, \"bleCBAdvertiseRate\":%!{(MISSING)private}d, \"bleDataVersion\":%!{(MISSING)private}d, \"displayBLEAlert\":%!{(MISSING)private}d, \"bleAdvertisementTimePrecisionInMSec\":%!{(MISSING)private}d}"
- "{\"msg%!{(MISSING)public}.0s\":\"#alerthandler,handleBleAlert,display blocked by MA\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid  res byte 2\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#iap,parseIgneousAlert\", \"source\":%!{(MISSING)private, location:escape_only}@, \"uid\":%!{(MISSING)private, location:escape_only}@, \"ingress_to_server_ts\":%!{(MISSING)private, location:escape_only}@, \"egress_from_source_ts\":%!{(MISSING)private, location:escape_only}@, \"event_origin_ts\":%!{(MISSING)private, location:escape_only}@, \"effective\":%!{(MISSING)private, location:escape_only}@, \"expires\":%!{(MISSING)private, location:escape_only}@, \"event_update_number\":%!{(MISSING)private, location:escape_only}@, \"epi_latitude\":%!{(MISSING)private, location:escape_only}@, \"epi_longitude\":%!{(MISSING)private, location:escape_only}@, \"magnitude\":%!{(MISSING)private, location:escape_only}@, \"depth\":%!{(MISSING)private, location:escape_only}@, \"display\":%!{(MISSING)private, location:escape_only}@}"
- "{\"msg%!{(MISSING)public}.0s\":\"#iap,parseIgneousAlert\", \"source\":%!{(MISSING)private, location:escape_only}s, \"uid\":%!{(MISSING)private, location:escape_only}s, \"alertSignature\":%!{(MISSING)private, location:escape_only}s, \"bleAlertData\":%!{(MISSING)private, location:escape_only}s, \"bleAlertUID\":%!{(MISSING)private, location:escape_only}s, \"ingress_to_server_ts\":\"%!{(MISSING)private}0.3f\", \"egress_from_source_ts\":\"%!{(MISSING)private}0.3f\", \"event_origin_ts\":\"%!{(MISSING)private}0.3f\", \"effective\":\"%!{(MISSING)private}0.3f\", \"expires\":\"%!{(MISSING)private}0.3f\", \"event_update_number\":\"%!{(MISSING)private}0.3f\", \"epi_latitude\":\"%!{(MISSING)private}0.3f\", \"epi_longitude\":\"%!{(MISSING)private}0.3f\", \"magnitude\":\"%!{(MISSING)private}0.3f\", \"depth\":\"%!{(MISSING)private}0.3f\", \"mmiSize\":%!{(MISSING)private}llu, \"mmiLat\":\"%!{(MISSING)private}0.3f\", \"mmiLon\":\"%!{(MISSING)private}0.3f\", \"mmiLevel\":\"%!{(MISSING)private}0.3f\", \"Display\":%!{(MISSING)private}d}"
- "{\"msg%!{(MISSING)public}.0s\":\"brm,submitMetrics\", \"isBleAdvertiser\":%!{(MISSING)private}hhd, \"wasSAReceived\":%!{(MISSING)private}hhd, \"batteryChargeLevel\":%!{(MISSING)private}d, \"bleRelayFanOutSetting\":%!{(MISSING)private}d, \"meanNumNearbyDevices\":%!{(MISSING)private}d, \"bleRelayAdvertiseDuration\":%!{(MISSING)private}d, \"alertIndex\":%!{(MISSING)private}d, \"bleReceivedRSSI\":%!{(MISSING)private}d, \"bleReceivedRSSIBucketed\":%!{(MISSING)private}d, \"bleLatencyRelativeToSATime\":\"%!{(MISSING)private}0.2f\", \"latencyRelativeToBleAdvertiseTime\":\"%!{(MISSING)private}0.2f\", \"latencyRelativeToOriginatorTime\":\"%!{(MISSING)private}0.2f\", \"alertUID\":%!{(MISSING)private, location:escape_only}s, \"deviceRole\":%!{(MISSING)private, location:escape_only}s, \"pushInterface\":%!{(MISSING)private, location:escape_only}s, \"source\":%!{(MISSING)private, location:escape_only}s}"

```
