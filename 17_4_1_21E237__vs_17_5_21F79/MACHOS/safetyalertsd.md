## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-45.0.8.0.0
-  __TEXT.__text: 0x7e498
-  __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_stubs: 0x2020
+45.0.15.0.1
+  __TEXT.__text: 0x910a8
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__objc_stubs: 0x2320
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x2c0
-  __TEXT.__const: 0x4d59
-  __TEXT.__gcc_except_tab: 0x36c4
-  __TEXT.__oslogstring: 0x1ea00
-  __TEXT.__cstring: 0x3c69
-  __TEXT.__objc_methname: 0x2578
-  __TEXT.__objc_classname: 0x173
-  __TEXT.__objc_methtype: 0x103f
-  __TEXT.__unwind_info: 0x216c
+  __TEXT.__objc_methlist: 0x2f0
+  __TEXT.__const: 0x7a31
+  __TEXT.__gcc_except_tab: 0x3f24
+  __TEXT.__oslogstring: 0x22991
+  __TEXT.__cstring: 0x3ef1
+  __TEXT.__objc_methname: 0x291c
+  __TEXT.__objc_classname: 0x1ae
+  __TEXT.__objc_methtype: 0x111e
+  __TEXT.__unwind_info: 0x2894
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x628
-  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__auth_got: 0x668
+  __DATA_CONST.__got: 0x2e0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4a38
-  __DATA_CONST.__cfstring: 0x4120
-  __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__const: 0x6518
+  __DATA_CONST.__cfstring: 0x4480
+  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x1a8
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x1650
-  __DATA.__objc_selrefs: 0x8c0
-  __DATA.__objc_ivar: 0x4c
-  __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x380
-  __DATA.__common: 0x10
-  __DATA.__bss: 0x438
+  __DATA_CONST.__objc_classrefs: 0x1f0
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_intobj: 0x18
+  __DATA.__objc_const: 0x1808
+  __DATA.__objc_selrefs: 0x980
+  __DATA.__objc_ivar: 0x54
+  __DATA.__objc_data: 0x230
+  __DATA.__data: 0x3d8
+  __DATA.__common: 0x20
+  __DATA.__bss: 0x488
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/PushKit.framework/PushKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 85E7076D-7F4D-3C01-ACAC-7C3FC14E526F
-  Functions: 1961
-  Symbols:   336
-  CStrings:  3127
+  UUID: 7312E755-FA38-3426-BF76-549286985CE9
+  Functions: 2529
+  Symbols:   359
+  CStrings:  3412
 
Symbols:
+ _CC_SHA224
+ _CFDataCreate
+ _OBJC_CLASS_$_CBController
+ _OBJC_CLASS_$_MCProfileConnection
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_RTPeopleDiscoveryServiceConfiguration
+ _OBJC_CLASS_$_UNMutableNotificationContent
+ _OBJC_CLASS_$_UNNotificationIcon
+ _OBJC_CLASS_$_UNNotificationRequest
+ _OBJC_CLASS_$_UNNotificationSound
+ _OBJC_CLASS_$_UNUserNotificationCenter
+ _SecKeyCreateWithData
+ _SecKeyVerifySignature
+ __CTServerConnectionGetCellBroadcastSettingForAlertType
+ __ZNK14SAPlatformInfo20isAOPSupportedDeviceEv
+ _kSecAttrKeyClass
+ _kSecAttrKeyClassPublic
+ _kSecAttrKeySizeInBits
+ _kSecAttrKeyType
+ _kSecAttrKeyTypeEC
+ _kSecKeyAlgorithmECDSASignatureDigestRFC4754
+ _objc_release_x20
+ _objc_retain_x20
+ _objc_retain_x8
+ _strtol
- _OBJC_CLASS_$_BluetoothManager
- __ZN14SAPlatformInfo20isAOPSupportedDeviceEv
- __ZNSt3__19to_stringEd
CStrings:
+ "@\"UNUserNotificationCenter\""
+ "AlertMessageID"
+ "BLEAlertData"
+ "BleUIDKeyString"
+ "CODEBOOK_DOWNLOAD_PERIOD_SECONDS"
+ "CODEBOOK_DOWNLOAD_TIMEOUT_SECONDS"
+ "J%d"
+ "JPN"
+ "M"
+ "Quake"
+ "SAEWBLEConfig_v2"
+ "SAUnUserNotificationProxy"
+ "Safety Alerts Test"
+ "SafetyAlertsLivability"
+ "UNUserNotificationCenterDelegate"
+ "UN_USER_NOTIFICATION_TEST_ENABLED"
+ "_notificationCenter"
+ "addNotificationRequest:withCompletionHandler:"
+ "bleAdvertisementTimePrecisionInMSec"
+ "bleDataVersion"
+ "ble_received"
+ "bluetoothState"
+ "bytes"
+ "cellularQualityAverage"
+ "codebook.json"
+ "codebookDownloadPeriodSeconds"
+ "codebookFileName"
+ "com.apple.safetyalerts.aa"
+ "compatibilityVersion"
+ "content"
+ "contentVersion"
+ "defaultSound"
+ "displayBLEAlert"
+ "emergency-20"
+ "fetchCurrentPeopleDensity:"
+ "getControllerInfoWithCompletion:"
+ "iconNamed:"
+ "initWithBundleIdentifier:queue:"
+ "initWithRestorationIdentifier:"
+ "initWithServiceLevel:storageDuration:observationInterval:densityCallbackConfiguration:"
+ "isBLERelaySupported_v2"
+ "isSafetyDataSubmissionAllowed"
+ "key"
+ "latencyRelativeToOriginator"
+ "latencyRelativeToSWave"
+ "localizedUserNotificationStringForKey:arguments:"
+ "manifestVersionNumber"
+ "motionHarvestOnly"
+ "motionHarvestOnlyInCountry"
+ "postNotification:withSilence:"
+ "publicKeys"
+ "requestWithIdentifier:content:trigger:destinations:"
+ "saMotionHarvestAllowed"
+ "safetyalertsblem"
+ "safetyalertsdble"
+ "safetyalertsrm"
+ "security"
+ "setBody:"
+ "setCategoryIdentifier:"
+ "setIcon:"
+ "setSound:"
+ "setThreadIdentifier:"
+ "setTitle:"
+ "setWantsNotificationResponsesDelivered"
+ "setWithObjects:"
+ "sharedConnection"
+ "silentDisplayAlert"
+ "startMonitoringForPeopleDiscovery:handler:"
+ "stopMonitoringForPeopleDiscoveryWithHandler:"
+ "threadIdentifier"
+ "userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:"
+ "userNotificationCenter:openSettingsForNotification:"
+ "userNotificationCenter:willPresentNotification:withCompletionHandler:"
+ "v24@?0@\"CBControllerInfo\"8@\"NSError\"16"
+ "v24@?0@\"RTPeopleDensity\"8@\"NSError\"16"
+ "v32@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24"
+ "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24@?<v@?Q>32"
+ "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotificationResponse\"24@?<v@?>32"
+ "wifiQualityAverage"
+ "{\"msg%{public}.0s\":\"#SALBAssetConfig,can't read bleAdvertisementTimePrecisionInMSec\"}"
+ "{\"msg%{public}.0s\":\"#SALBAssetConfig,can't read bleDataVersion\"}"
+ "{\"msg%{public}.0s\":\"#SALBAssetConfig,can't read displayBLEAlert\"}"
+ "{\"msg%{public}.0s\":\"#SALBAssetConfig,readBleConfigFromDefaults\", \"isBLERelaySupported\":%{private}hhd, \"advertiseEvaluationIntervalSeconds\":%{private}d, \"discoveryEvaluationIntervalSeconds\":%{private}d, \"advertiseDurationSeconds\":%{private}d, \"minDeviceDensityCount\":%{private}d, \"minTimeBetweenPeopleDensityQuery\":%{private}d, \"percent\":%{private}d, \"minBatteryLevelForBLEActivity\":%{private}d, \"bleCBAdvertiseRate\":%{private}d, \"bleCBScanRate\":%{private}d, \"bleCBScanRateScreenOff\":%{private}d, \"bleDataVersion\":%{private}d, \"displayBLEAlert\":%{private}d, \"bleAdvertisementTimePrecisionInMSec\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#SALBAssetConfig,readBleConfigFromFailSafe\", \"isBLERelaySupported\":%{private}hhd, \"advertiseEvaluationIntervalSeconds\":%{private}d, \"discoveryEvaluationIntervalSeconds\":%{private}d, \"advertiseDurationSeconds\":%{private}d, \"minBatteryLevelForBLEActivity\":%{private}d, \"minDeviceDensityCount\":%{private}d, \"minTimeBetweenPeopleDensityQuery\":%{private}d, \"bleCBScanRate\":%{private}d, \"CBScanRateBackground\":%{private}d, \"bleCBAdvertiseRate\":%{private}d, \"bleDataVersion\":%{private}d, \"displayBLEAlert\":%{private}d, \"bleAdvertisementTimePrecisionInMSec\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#SALBAssetConfig,readBleConfigFromFile\", \"isBLERelaySupported\":%{private}hhd, \"advertiseEvaluationIntervalSeconds\":%{private}d, \"discoveryEvaluationIntervalSeconds\":%{private}d, \"advertiseDurationSeconds\":%{private}d, \"minBatteryLevelForBLEActivity\":%{private}d, \"minDeviceDensityCount\":%{private}d, \"minTimeBetweenPeopleDensityQuery\":%{private}d, \"bleCBScanRate\":%{private}d, \"bleCBScanRateScreenOff\":%{private}d, \"bleCBAdvertiseRate\":%{private}d, \"bleDataVersion\":%{private}d, \"displayBLEAlert\":%{private}d, \"bleAdvertisementTimePrecisionInMSec\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#aa,downloadCodebook,codebook downloaded\"}"
+ "{\"msg%{public}.0s\":\"#aa,downloadCodebook,downloader not ready\"}"
+ "{\"msg%{public}.0s\":\"#aa,downloadCodebook,downloading public keys codebook\", \"srcUrl\":%{private, location:escape_only}s, \"dstPath\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#aa,downloadCodebook,empty codebook file name\"}"
+ "{\"msg%{public}.0s\":\"#aa,downloadCodebook,empty codebook file or url path\"}"
+ "{\"msg%{public}.0s\":\"#aa,downloadCodebook,failed to download\"}"
+ "{\"msg%{public}.0s\":\"#aa,downloadCodebook,not supported\"}"
+ "{\"msg%{public}.0s\":\"#aa,downloadCodebook,pull cname unavailable\"}"
+ "{\"msg%{public}.0s\":\"#aa,generateHashOfData,dataRef nil\"}"
+ "{\"msg%{public}.0s\":\"#aa,generateHashOfData,empty input\"}"
+ "{\"msg%{public}.0s\":\"#aa,generateHashOfData,failed to generate SHA224\"}"
+ "{\"msg%{public}.0s\":\"#aa,initialized\"}"
+ "{\"msg%{public}.0s\":\"#aa,isSignatureValidInternal\", \"isValid\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#aa,isSignatureValidInternal\", \"signature\":%{private, location:escape_only}@, \"dataHash\":%{private, location:escape_only}@, \"publicKeyData\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#aa,isSignatureValidInternal,attributes nil\"}"
+ "{\"msg%{public}.0s\":\"#aa,isSignatureValidInternal,dataHash nil\"}"
+ "{\"msg%{public}.0s\":\"#aa,isSignatureValidInternal,error in create publicKeyRef\", \"error\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#aa,isSignatureValidInternal,error in verify signature\", \"error\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#aa,isSignatureValidInternal,nil input\"}"
+ "{\"msg%{public}.0s\":\"#aa,isSignatureValidInternal,publicKeyRef nil\"}"
+ "{\"msg%{public}.0s\":\"#aa,isSignatureValidUsingCodebook,cfData input nil\"}"
+ "{\"msg%{public}.0s\":\"#aa,isSignatureValidUsingCodebook,fCodebook nil\"}"
+ "{\"msg%{public}.0s\":\"#aa,isSignatureValidUsingCodebook,input empty\"}"
+ "{\"msg%{public}.0s\":\"#aa,isSignatureValidUsingCodebook,not supported\"}"
+ "{\"msg%{public}.0s\":\"#aa,loadCodebook\", \"filePath\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#aa,loadCodebook,codebook dict empty\", \"filePath\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#aa,loadCodebook,empty file path\"}"
+ "{\"msg%{public}.0s\":\"#aa,loadCodebook,error converting to dict\", \"error\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#aa,loadCodebook,invalid codeBook\"}"
+ "{\"msg%{public}.0s\":\"#aa,loadCodebook,invalid path\", \"filePath\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#aa,loadCodebook,not supported\"}"
+ "{\"msg%{public}.0s\":\"#aa,loadCodebook,path not derived\", \"filePath\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#aa,loadCodebook,read failed\", \"filePath\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#aa,onXpcActivityTriggered\"}"
+ "{\"msg%{public}.0s\":\"#aa,processXpcActivity\"}"
+ "{\"msg%{public}.0s\":\"#aa,processXpcActivity,activity is nil\"}"
+ "{\"msg%{public}.0s\":\"#aa,processXpcActivity,checkin\"}"
+ "{\"msg%{public}.0s\":\"#aa,processXpcActivity,failed to set state\"}"
+ "{\"msg%{public}.0s\":\"#aa,processXpcActivity,run\"}"
+ "{\"msg%{public}.0s\":\"#aa,processXpcActivity,unexpected xpcActivity\"}"
+ "{\"msg%{public}.0s\":\"#aa,released\"}"
+ "{\"msg%{public}.0s\":\"#aa,setupXpcActivity\", \"downloadPeriodSeconds\":\"%{private}0.1f\"}"
+ "{\"msg%{public}.0s\":\"#aa,setupXpcActivity\"}"
+ "{\"msg%{public}.0s\":\"#aa,setupXpcActivity,cannot create xpcDictionary\"}"
+ "{\"msg%{public}.0s\":\"#aa,setupXpcActivity,init failed\"}"
+ "{\"msg%{public}.0s\":\"#aa,setupXpcActivity,invalid download period\"}"
+ "{\"msg%{public}.0s\":\"#aa,setupXpcActivity,not supported\"}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,SAAlertDisplay\"}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,displayProdBleAlert,invalid telephony\"}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,displayProdBleAlert,not a prod alert\"}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,displayProdBleAlert,test alert not to be displayed\"}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,displayProdBleAlert,to display\", \"en\":%{public, location:escape_only}s, \"sp\":%{public, location:escape_only}s, \"bleMsgTypes\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,displayTestBleAlert,invalid telephony\"}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,displayTestBleAlert,not internal install\"}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,displayTestBleAlert,to display\", \"en\":%{public, location:escape_only}s, \"sp\":%{public, location:escape_only}s, \"bleMsgTypes\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,handleBleAlert\"}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,handleBleAlert,invalid parser or displayAlert\"}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,parseAlertInformation isInternalTestAlert\"}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,parseAlertInformation isLivabilityAlert\"}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,parseAlertInformation isLiveAppleAlert or isLiveAppleUpdateAlert\"}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,parseAlertInformation isLiveAppleTestAlert\"}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,parseAlertInformation isQEOrDevTest\"}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,parseAlertInformation\", \"bleMsgTypes\":%{private}d, \"bleSenderType\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,test kAlertTypeInvalid\"}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,test kTestInternalAlertForNoDisplay\"}"
+ "{\"msg%{public}.0s\":\"#alertdisplay,test kTestInternalQEOrDevNoDisplay\"}"
+ "{\"msg%{public}.0s\":\"#alerthandler,handleBleAlert,display blocked by MA\"}"
+ "{\"msg%{public}.0s\":\"#alerthandler,handleBleAlert,duplicateAlert\"}"
+ "{\"msg%{public}.0s\":\"#ar,onSettingsChanged\"}"
+ "{\"msg%{public}.0s\":\"#asset,scheduleXPCActivity\", \"duration\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#assetConfig,log\", \"pullpc\":%{private}d, \"appc\":%{private}d, \"efficacyParticipationPercentage\":%{private}d, \"wowControls\":%{private}d, \"pullCname\":%{private, location:escape_only}s, \"efficacyManifestFileName\":%{private, location:escape_only}s, \"codebookFileName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#bleUtility,getBleAdvertisementTimePrecision\", \"bleAdvertisementTimePrecisionInMSec\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#bleUtility,getBleAlertVersion\", \"bleDataVersion\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#bleUtility,getCBAdvertiseRate\", \"bleCBAdvertiseRate\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#blecore,isBLEAlertRelayDevice,BLE relay possible\"}"
+ "{\"msg%{public}.0s\":\"#blecore,isBLERelaySupported\", \"isBLERelaySupported\":%{public}d, \"isSALivabilityEnabled\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#blecore,onBLEAlertReceived\", \"res\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#blecore,onBLEAlertReceived\"}"
+ "{\"msg%{public}.0s\":\"#blecore,onBLEAlertReceived,Signature invalid\"}"
+ "{\"msg%{public}.0s\":\"#blecore,onBLEAlertReceivedCb\"}"
+ "{\"msg%{public}.0s\":\"#blecore,onCurrentPeopleDensityReceivedCb\"}"
+ "{\"msg%{public}.0s\":\"#blecore,onCurrentPeopleDensityReceivedCb,lastEvent,\", \"startTimestamp\":\"%{private}0.2f\", \"densityScore\":\"%{private}0.2f\", \"scanDuration\":\"%{private}0.2f\"}"
+ "{\"msg%{public}.0s\":\"#blecore,onInitCompleted\"}"
+ "{\"msg%{public}.0s\":\"#blecore,processBleIgneousAlert\"}"
+ "{\"msg%{public}.0s\":\"#blecore,processBleIgneousAlert,BLEAlertRelay not supported\"}"
+ "{\"msg%{public}.0s\":\"#blecore,processBleIgneousAlert,Not a BLEAlertRelay device\"}"
+ "{\"msg%{public}.0s\":\"#blecore,processBleIgneousAlert,forward blocked\"}"
+ "{\"msg%{public}.0s\":\"#blecore,processBleIgneousAlert,transport error\"}"
+ "{\"msg%{public}.0s\":\"#blecore,requestCurrentPeopleDensity failed\"}"
+ "{\"msg%{public}.0s\":\"#blecore,requestCurrentPeopleDensity\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,decodeAlertToBLEPacket\", \"alertData\":%{private, location:escape_only}s, \"regionCode\":%{private, location:escape_only}s, \"Sender\":%{private}d, \"alertUIDHash\":%{private, location:escape_only}s, \"eventType\":%{private}d, \"Msgtypes\":%{private}d, \"alertType\":%{private}d, \"bleAlertInfo.sentTime\":%{private}llu, \"ExpirationLen\":%{private}d, \"ExpirationNum\":%{private}d, \"GeoCodeType\":%{private}d, \"GeoShapeType\":%{private}d, \"GeoCode\":%{private}llu, \"Magnitude\":%{private}d, \"epi_latitude\":%{private}d, \"epi_longitude\":%{private}d, \"MMI\":%{private}d, \"Radius\":%{private}d, \"bleAdvertiseTime\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#bletransport,decodeAlertToBLEPacket\", \"igneousAlertInformation.uid\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#bletransport,decodeAlertToBLEPacket\", \"offset\":%{private}d, \"alertData\":%{private, location:escape_only}s, \"length:alert.length\":%{private}llu}"
+ "{\"msg%{public}.0s\":\"#bletransport,decodeAlertToBLEPacket\", \"source\":%{private, location:escape_only}s, \"uid\":%{private, location:escape_only}s, \"regionCode\":%{private, location:escape_only}s, \"ingress_to_server_ts\":\"%{private}0.3f\", \"egress_from_source_ts\":\"%{private}0.3f\", \"event_origin_ts\":\"%{private}0.3f\", \"effective\":\"%{private}0.3f\", \"expires\":\"%{private}0.3f\", \"event_update_number\":\"%{private}0.3f\", \"epi_latitude\":\"%{private}0.3f\", \"epi_longitude\":\"%{private}0.3f\", \"magnitude\":\"%{private}0.3f\", \"depth\":\"%{private}0.3f\", \"mmiLat\":\"%{private}0.3f\", \"mmiLon\":\"%{private}0.3f\", \"mmiLevel\":\"%{private}0.3f\", \"bleAdvertiseTime\":\"%{private}0.3f\", \"radiusOfApplicableRegion\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#bletransport,decodeAlertToBLEPacket,invalid UID\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,decodeAlertToBLEPacket,invalid data\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,preparePDUAndSignatureForValidation,invalid data\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,preparePDUAndSignatureForValidation,invalid signature\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,readIndexDataAndSignature,\", \"Signature\":%{public, location:escape_only}s, \"alertData\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#bletransport,readIndexDataAndSignature,\", \"encodedDataLen\":%{public}d, \"index\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#bletransport,readIndexDataAndSignature,\", \"encodedDataLen\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#bletransport,readIndexDataAndSignature,can't read data\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,readIndexDataAndSignature,can't read signature\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,readIndexDataAndSignature,invalid data payload.\", \"encodedDataLen\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#bletransport,readIndexDataAndSignature,invalid data\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,readIndexDataAndSignature,invalid signature.\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,startAdvertisingIgneousAlert cb\", \"Error\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#bletransport,startAdvertisingIgneousAlert cb\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,startAdvertisingIgneousAlert fAdvertiser invalid\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,startAdvertisingIgneousAlert fAdvertiser release\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,startAdvertisingIgneousAlert invalid BLE info\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,startAdvertisingIgneousAlert\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,startAdvertisingIgneousAlert,can not convert data to Bin\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,startAdvertisingIgneousAlert,fDispatchQueue invalid\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,subscribeForBLEDiscoveryCb\", \"safetyAlertsAlertData.length\":%{public}llu, \"safetyAlertsSignature.length\":%{public}llu}"
+ "{\"msg%{public}.0s\":\"#bletransport,subscribeForBLEDiscoveryCb,PDU decode failed\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,subscribeForBLEDiscoveryCb,authenticated\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,subscribeForBLEDiscoveryCb,fOnBLEAlertCb failed\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,subscribeForBLEDiscoveryCb,fOnBLEAlertCb\"}"
+ "{\"msg%{public}.0s\":\"#bletransport,subscribeForBLEDiscoveryCb,invalid PDU or Sign\"}"
+ "{\"msg%{public}.0s\":\"#bm\", \"wifiCCA\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#bm,onCurrentPeopleDensityRecievedCb\", \"fRSSIHistogram\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#bm,onCurrentPeopleDensityRecievedCb\", \"now\":%{private}llu, \"startTimestamp\":\"%{private}0.2f\", \"densityScore\":\"%{private}0.2f\", \"scanDuration\":\"%{private}0.2f\", \"endTimestamp\":\"%{private}0.2f\"}"
+ "{\"msg%{public}.0s\":\"#bm,onCurrentPeopleDensityRecievedCb\"}"
+ "{\"msg%{public}.0s\":\"#bm,onInitCompleted\"}"
+ "{\"msg%{public}.0s\":\"#chsel,addCountryConfig\", \"success\":%{public}hhd, \"country\":%{public, location:escape_only}@, \"config\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#chsel,addCountryConfig,d null\"}"
+ "{\"msg%{public}.0s\":\"#chsel,addCountryConfig,invalidArgs\"}"
+ "{\"msg%{public}.0s\":\"#chsel,addCountryConfig,isoList null\"}"
+ "{\"msg%{public}.0s\":\"#chsel,getIgneousStateParameters,state\", \"isEnabled\":%{private}hhd, \"inSupportedCountry\":%{private}hhd, \"isInMagnetMode\":%{private}hhd, \"isUserOptedIn\":%{private}hhd, \"inCoverageRegion\":%{private}hhd, \"isInCountry\":%{private}hhd, \"emergencyAlert\":%{private}hhd, \"motionHarvestPref\":%{private}hhd, \"motionHarvestOnlyInCountry\":%{private}hhd, \"motionHarvestAvailable\":%{private}hhd, \"improveSafety\":%{private}hhd, \"isMotionHarvestAllowed\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#chsel,onMotionHarvestOnlySupportChanged\", \"asset config value\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#chsel,onMotionHarvestOnlySupportChanged\", \"isSupported\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#cob,empty valid public\"}"
+ "{\"msg%{public}.0s\":\"#cob,invalid codebook dict\"}"
+ "{\"msg%{public}.0s\":\"#cob,invalid public key obj\"}"
+ "{\"msg%{public}.0s\":\"#cob,isValid,empty public keys\"}"
+ "{\"msg%{public}.0s\":\"#cob,isValid,out of range\", \"effective\":\"%{private}0.1f\", \"expires\":\"%{private}0.1f\", \"now\":\"%{private}0.1f\"}"
+ "{\"msg%{public}.0s\":\"#cob,isValid,parse failed\"}"
+ "{\"msg%{public}.0s\":\"#cob,log\", \"uid\":%{private, location:escape_only}s, \"contentVersion\":%{private}d, \"compatibilityVersion\":%{private}d, \"numKeys\":%{private}d, \"effective\":\"%{private}.1f\", \"expires\":\"%{private}.1f\", \"parseSuccessful\":%{private}hhd, \"isValid\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#cob,parse failed\", \"field\":%{private, location:escape_only}s, \"codebookDictionary\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#cob,parse failed\", \"field\":%{private, location:escape_only}s, \"publicKeyDictionary\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#commonUtils,convertDictionaryToString\", \"error\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#commonUtils,convertDictionaryToString,dict nil\"}"
+ "{\"msg%{public}.0s\":\"#commonUtils,convertDictionaryToString,str nil\"}"
+ "{\"msg%{public}.0s\":\"#commonUtils,convertHexToChar,error\"}"
+ "{\"msg%{public}.0s\":\"#commonUtils,convertHexToChar,invalid len\", \"len\":%{private}d, \"hex.size()\":%{private}llu}"
+ "{\"msg%{public}.0s\":\"#commonUtils,convertStringToDictionary\", \"error\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#commonUtils,convertStringToDictionary\", \"key\":%{private, location:escape_only}@, \"value\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#commonUtils,convertStringToDictionary,empty string\"}"
+ "{\"msg%{public}.0s\":\"#commonUtils,convertStringToDictionary,null data\"}"
+ "{\"msg%{public}.0s\":\"#commonUtils,isValidHexString,\", \"d\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#commonUtils,isValidHexString,\", \"hexStr\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#commonUtils,isValidHexString,emptry string\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,SACoreRoutineProd,failed,invalid UniqueId\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,Test,getCurrentPeopleDensity\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,Test,startMonitoringForPeopleDensity\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,Test,stopMonitoringForPeopleDensity\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,getCurrentPeopleDensity\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,getCurrentPeopleDensity,done\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,getCurrentPeopleDensity,invalid fRoutineManager\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onCurrentPeopleDensityReceived\", \"Error\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onCurrentPeopleDensityReceived\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onCurrentPeopleDensityReceived,adding density\", \"startTimestamp\":\"%{private}0.2f\", \"scanDuration\":\"%{private}0.2f\", \"densityScore\":\"%{private}0.2f\", \"endTimestamp\":\"%{private}0.2f\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onCurrentPeopleDensityReceived,event nil\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onCurrentPeopleDensityReceived,invalid event values\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onCurrentPeopleDensityReceived,rssiHist\", \"rssi\":%{private}d, \"numDevices\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onCurrentPeopleDensityReceived,rssiHist,invalid Type\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onPeopleDensityReceived\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onPeopleDensityReceived,adding density\", \"startTimestamp\":\"%{private}0.2f\", \"endTimestamp\":\"%{private}0.2f\", \"scanDuration\":\"%{private}0.2f\", \"densityScore\":\"%{private}0.2f\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onPeopleDensityReceived,event out of bound,skipping\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onPeopleDensityReceived,fetch completed\", \"densityLen\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onPeopleDensityReceived,invalid start time,skipping\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onPeopleDensityReceived,received update\", \"Error\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onPeopleDensityReceived,received update,\", \"count\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onPeopleDensityReceived,received update,no densityEvents\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onPeopleDensityReceived,rssiHist\", \"rssi\":%{private}d, \"numDevices\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,onPeopleDensityReceived,rssiHist,invalid Type\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,startMonitoringForPeopleDensity\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,startMonitoringForPeopleDensity,invalid instance\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,startMonitoringForPeopleDiscovery,\", \"Error\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,stopMonitoringForPeopleDensity\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,stopMonitoringForPeopleDensity,\", \"Error\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,stopMonitoringForPeopleDensity,invalid instance\"}"
+ "{\"msg%{public}.0s\":\"#ctsa,com.apple.CTTelephonyCenter\", \"eDel\":%{public}d, \"eDelAvl\":%{public}d, \"saAvl\":%{public}d, \"saEmergencyAvl\":%{public}d, \"saMotionHarvestPref\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#ctsa,displayIgneousBleAlert invalid data\"}"
+ "{\"msg%{public}.0s\":\"#ctsa,displayIgneousBleAlert sent successfully \"}"
+ "{\"msg%{public}.0s\":\"#ctsa,displayIgneousBleAlert\", \"rootDict\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#ctsa,displayIgneousBleAlert,infoDict invalid\"}"
+ "{\"msg%{public}.0s\":\"#ctsa,displayIgneousBleAlert,infoDictList invalid\"}"
+ "{\"msg%{public}.0s\":\"#ctsa,displayIgneousBleAlert,item1 invalid\"}"
+ "{\"msg%{public}.0s\":\"#ctsa,displayIgneousBleAlert,item2 invalid\"}"
+ "{\"msg%{public}.0s\":\"#ctsa,onMotionHarvestPref error\"}"
+ "{\"msg%{public}.0s\":\"#ctsa,onMotionHarvestPref\", \"opt out\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#ctsa,onMotionHarvestPref,not phone\"}"
+ "{\"msg%{public}.0s\":\"#ctsa,processIgneousAlert,Send to Ble\"}"
+ "{\"msg%{public}.0s\":\"#daemon,#warning,isIgneousAlert,invalid parser\"}"
+ "{\"msg%{public}.0s\":\"#daemon,#warning,processIgneousAlert,invalid parser\"}"
+ "{\"msg%{public}.0s\":\"#daemon,USGSAlert stale Alert\"}"
+ "{\"msg%{public}.0s\":\"#daemon,kAlertLivability fails precheck\"}"
+ "{\"msg%{public}.0s\":\"#daemon,kAlertLivability isStaleAlert fails\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onMotionHarvestWeaTrigger,fail to call motion SPI\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onMotionHarvestWeaTrigger,invalid messageID\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onMotionHarvestWeaTrigger,not ETWS\", \"alertMessageID\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#daemon,onMotionHarvestWeaTrigger,not allowed\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onMotionHarvestWeaTrigger,triggered harvest\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onMotionHarvestWeaTrigger,uid null\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onMotionHarvestWeaTrigger,weaReceivedDict null\"}"
+ "{\"msg%{public}.0s\":\"#daemonInterfaceProd,igneousEnablementStateInfo\", \"inCoverageRegion\":%{private}hhd, \"inSupportedCountry\":%{private}hhd, \"isInMagnetMode\":%{private}hhd, \"isUserOptedIn\":%{private}hhd, \"isEnabled\":%{private}hhd, \"isEmergencyAlertEnabled\":%{private}hhd, \"isMotionHarvestAllowed\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#evtTrk,updateIgneousReceived done\"}"
+ "{\"msg%{public}.0s\":\"#evtTrk,updateIgneousReceived\", \"bleUID\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#evtTrk,updateIgneousReceived\", \"decodedAlertData.uid.c_str()\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#evtTrk,updateIgneousReceived\", \"hexUID\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#evtTrk,updateIgneousReceived\", \"metaValueStr.c_str()\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#evtTrk,updateIgneousReceived,PDU decode failed\"}"
+ "{\"msg%{public}.0s\":\"#evtTrk,updateIgneousReceived,invalid UID\"}"
+ "{\"msg%{public}.0s\":\"#iap,SAIgneousAlertParser\", \"bleUID\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#iap,bleReceived\", \"lastBleReceivedTs\":\"%{public}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#iap,isDuplicateBleAlertReceived\", \"uid\":%{private, location:escape_only}s, \"lastBleReceivedTs\":\"%{public}0.3f\", \"curTime\":\"%{public}0.3f\", \"ThresholdTimeBetweenAlerts\":\"%{public}0.3f\", \"FollowUpMessageValidTime\":\"%{public}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#iap,isDuplicateBleAlertReceived\"}"
+ "{\"msg%{public}.0s\":\"#iap,isIgneousAlertReceivedForBle,bleUid Invalid\"}"
+ "{\"msg%{public}.0s\":\"#iap,isIgneousAlertReceivedForBle,dictionary Invalid\"}"
+ "{\"msg%{public}.0s\":\"#iap,isStaleAlert\", \"nowSeconds\":\"%{public}0.3f\", \"egressTime\":\"%{public}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#iap,isStaleAlert,stale alert received\"}"
+ "{\"msg%{public}.0s\":\"#iap,parseIgneousAlert\", \"alertSignatureLen\":%{private}llu, \"bleAlertDataLen\":%{private}llu}"
+ "{\"msg%{public}.0s\":\"#iap,parseIgneousAlert,authenticated\"}"
+ "{\"msg%{public}.0s\":\"#notif,\", \"str\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#notif,addNotificationRequest failed\", \"threadId\":%{private, location:escape_only}@, \"inUNError\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#notif,warning,cantCreateDisplayStr\"}"
+ "{\"msg%{public}.0s\":\"#notif,warning,emptyContent\"}"
+ "{\"msg%{public}.0s\":\"#pk,isExpired\", \"effective\":\"%{private}0.1f\", \"expires\":\"%{private}0.1f\", \"now\":\"%{private}0.1f\"}"
+ "{\"msg%{public}.0s\":\"#pk,isValid,out of range\", \"effective\":\"%{private}0.1f\", \"expires\":\"%{private}0.1f\", \"now\":\"%{private}0.1f\"}"
+ "{\"msg%{public}.0s\":\"#pk,isValid,parse not successfull\"}"
+ "{\"msg%{public}.0s\":\"#pk,key dataRef nil\"}"
+ "{\"msg%{public}.0s\":\"#pk,log\", \"key\":%{private, location:escape_only}@, \"effective\":\"%{private}.1f\", \"expires\":\"%{private}.1f\", \"parseSuccessful\":%{private}hhd, \"isValid\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#raii,destroy,clear\"}"
+ "{\"msg%{public}.0s\":\"#raii,init\"}"
+ "{\"msg%{public}.0s\":\"#raii,init,load\"}"
+ "{\"msg%{public}.0s\":\"#raii,released\"}"
+ "{\"msg%{public}.0s\":\"#rm,onInitCompleted\"}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,wifiQualityWithinWindow,size one\", \"quality\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saBiomeProd,wifiQualityWithinWindow,size two\", \"quality\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saCoreTelephony,onMotionHarvestWeaTrigger,alert does not have any info,ignoring.\"}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,#warning,findAllEventsWithin,outOfRangeArgs\", \"history\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,#warning,findAllEventsWithin,skipping,notReady\", \"history\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,#warning,findFirstEventAfter,InvalidArgs\", \"history\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,#warning,findFirstEventAfter,skipping,notReady\", \"history\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,findFirstEventAfterInternal\", \"debugName\":%{private, location:escape_only}s, \"time\":\"%{private}.2f\", \"fStartTimeSeconds\":\"%{private}.2f\", \"fEndTimeSeconds\":\"%{private}.2f\"}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,findLatestEventBeforeInternal\", \"debugName\":%{private, location:escape_only}s, \"time\":\"%{private}.2f\", \"fStartTimeSeconds\":\"%{private}.2f\", \"fEndTimeSeconds\":\"%{private}.2f\"}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,findLatestValueBefore\", \"filePath\":%{private, location:escape_only}s, \"debugName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,insert\", \"filePath\":%{private, location:escape_only}s, \"debugName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,isFoundInternal\", \"debugName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,load\", \"filePath\":%{private, location:escape_only}s, \"debugName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,save\", \"filePath\":%{private, location:escape_only}s, \"debugName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,update\", \"filePath\":%{private, location:escape_only}s, \"debugName\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd\", \"fIsBluetoothStateCached\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,BTController failed:\", \"inError\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,cb\", \"fIsBluetoothStateCached\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,isBluetoothEnabled invalid controller\"}"
+ "{\"msg%{public}.0s\":\"#saSettingsProd,settings updated\"}"
+ "{\"msg%{public}.0s\":\"#saanalytics,igneous received\", \"id\":%{private, location:escape_only}s, \"alertTextID\":%{private}lu, \"alertOriginationTime\":\"%{public}0.1f\", \"saReceivedTime\":\"%{public}0.1f\", \"insidePolygon\":%{private}d, \"saReceivedBeforeWEA\":%{public}d, \"latencyToEqOriginMilliSec\":\"%{public}0.2f\", \"salatencyOriginatorMilliSec\":\"%{public}0.2f\", \"salatencyServerMilliSec\":\"%{public}0.2f\", \"distanceToEpicenter\":\"%{private}0.2f\", \"latencyRelativeToSWave\":\"%{private}0.2f\", \"MMI\":\"%{private}0.2f\", \"magnitude\":\"%{private}0.2f\", \"isTestAlert\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#saanalytics,isBLERelay is not supported\"}"
+ "{\"msg%{public}.0s\":\"#saanalytics,onSettingsChanged\"}"
+ "{\"msg%{public}.0s\":\"blecore,onBLEAlertReceived,stale alert\"}"
+ "{}"
- "ASSET_DOWNLOAD_INTERVAL_WHEN_NO_ASSET"
- "BLERelayData"
- "IgneousBLERelay"
- "SAEWBLEConfig"
- "USCA"
- "WeaEnrichmentLivability"
- "copy"
- "enabled"
- "requestBLEDensityScanWindowTime"
- "saEnabledStateDefaultsWrite"
- "setObject:forKey:"
- "{\"msg%{public}.0s\":\" \", \" \":%{private}d}"
- "{\"msg%{public}.0s\":\" g=\", \" \":%{private}d}"
- "{\"msg%{public}.0s\":\"#SALBAssetConfig,readBleConfigFromDefaults\", \"isBLERelaySupported\":%{private}hhd, \"advertiseEvaluationIntervalSeconds\":%{private}d, \"discoveryEvaluationIntervalSeconds\":%{private}d, \"advertiseDurationSeconds\":%{private}d, \"minDeviceDensityCount\":%{private}d, \"minTimeBetweenPeopleDensityQuery\":%{private}d, \"percent\":%{private}d, \"minBatteryLevelForBLEActivity\":%{private}d, \"bleCBAdvertiseRate\":%{private}d, \"bleCBScanRate\":%{private}d, \"bleCBScanRateScreenOff\":%{private}d}"
- "{\"msg%{public}.0s\":\"#SALBAssetConfig,readBleConfigFromFailSafe\", \"isBLERelaySupported\":%{private}hhd, \"advertiseEvaluationIntervalSeconds\":%{private}d, \"discoveryEvaluationIntervalSeconds\":%{private}d, \"advertiseDurationSeconds\":%{private}d, \"minBatteryLevelForBLEActivity\":%{private}d, \"minDeviceDensityCount\":%{private}d, \"minTimeBetweenPeopleDensityQuery\":%{private}d, \"bleCBScanRate\":%{private}d, \"CBScanRateBackground\":%{private}d, \"bleCBAdvertiseRate\":%{private}d}"
- "{\"msg%{public}.0s\":\"#SALBAssetConfig,readBleConfigFromFile\", \"isBLERelaySupported\":%{private}hhd, \"advertiseEvaluationIntervalSeconds\":%{private}d, \"discoveryEvaluationIntervalSeconds\":%{private}d, \"advertiseDurationSeconds\":%{private}d, \"minBatteryLevelForBLEActivity\":%{private}d, \"minDeviceDensityCount\":%{private}d, \"minTimeBetweenPeopleDensityQuery\":%{private}d, \"bleCBScanRate\":%{private}d, \"bleCBScanRateScreenOff\":%{private}d, \"bleCBAdvertiseRate\":%{private}d}"
- "{\"msg%{public}.0s\":\"#ar,onSettingsChangeCb\"}"
- "{\"msg%{public}.0s\":\"#assetConfig,log\", \"pullpc\":%{private}d, \"appc\":%{private}d, \"efficacyParticipationPercentage\":%{private}d, \"wowControls\":%{private}d, \"pullCname\":%{private, location:escape_only}s, \"efficacyManifestFileName\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#blecore,isBLERelaySupported\", \"isBLERelaySupported\":%{public}d, \"isBLERelayFFEnabled\":%{public}d}"
- "{\"msg%{public}.0s\":\"#blecore,onPeopleDensityCb\", \"count\":%{private}lu}"
- "{\"msg%{public}.0s\":\"#blecore,onPeopleDensityReceivedCb,lastEvent,\", \"startTimestamp\":\"%{private}0.2f\", \"endTimestamp\":\"%{private}0.2f\", \"densityScore\":\"%{private}0.2f\", \"scanDuration\":\"%{private}0.2f\"}"
- "{\"msg%{public}.0s\":\"#blecore,onPeopleDensityReceivedCb1\"}"
- "{\"msg%{public}.0s\":\"#blecore,onPeopleDensityReceivedCb2\"}"
- "{\"msg%{public}.0s\":\"#blecore,requestBLEDensity failed\"}"
- "{\"msg%{public}.0s\":\"#blecore,requestBLEDensity\"}"
- "{\"msg%{public}.0s\":\"#blecore,sendIgneousAlertOverBLE\"}"
- "{\"msg%{public}.0s\":\"#blecore,sendIgneousAlertOverBLE,Not a BLEAlertRelay device\"}"
- "{\"msg%{public}.0s\":\"#blecore,sendIgneousAlertOverBLE,transport error\"}"
- "{\"msg%{public}.0s\":\"#bletransport,decodeAlertToBLEPacket\", \"alertData\":%{private, location:escape_only}s, \"regionCode\":%{private, location:escape_only}s, \"alertUIDHash\":%{private, location:escape_only}s, \"bleAlertInfo.sentTime\":\"%{private}0.3f\", \"Msgtypes\":%{private}d, \"alertType\":%{private}d, \"ExpirationLen\":%{private}d, \"ExpirationNum\":%{private}d, \"Geo\":%{private}d, \"MMI\":%{private}d, \"bleAlertInfo.geoCode\":%{private}llu, \"bleAlertInfo.Magnitude\":%{private}d, \"epi_latitude\":%{private}d, \"epi_longitude\":%{private}d, \"BLEAdvertiseTime\":%{private}d}"
- "{\"msg%{public}.0s\":\"#bletransport,decodeAlertToBLEPacket\", \"offset\":%{private}d, \"bleAlertData.geoCode.s\":%{private, location:escape_only}s, \"buf\":%{private, location:escape_only}s, \"bleAlertData.geoCode.longInt\":%{private}llu}"
- "{\"msg%{public}.0s\":\"#bletransport,decodeAlertToBLEPacket\", \"signature\":%{private, location:escape_only}s, \"alertData\":%{private, location:escape_only}s, \"length:alert.length\":%{private}llu}"
- "{\"msg%{public}.0s\":\"#bletransport,decodeAlertToBLEPacket,received packet exceeds allowed size\"}"
- "{\"msg%{public}.0s\":\"#bletransport,encodeAlertToBLEPacket\", \"Msgtypes\":%{private}d, \"alertType\":%{private}d, \"msgTypeAlertType\":%{private}d, \"expirationIntervalLength\":%{private}d, \"expirationIntervalNumber\":%{private}d, \"expLenNum\":%{private}d, \"geoCodeType\":%{private}d, \"MMI\":%{private}d, \"geoTypeMMI\":%{private}d, \"bleAlertInfo.geoCode.longInt\":%{private}llu, \"bleAlertInfo.geoCode.s\":%{private, location:escape_only}s, \"offset\":%{private}d}"
- "{\"msg%{public}.0s\":\"#bletransport,encodeAlertToBLEPacket\", \"bleAlertInfo.regionCode.size()\":%{private}llu, \"bleAlertInfo.regionCode\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#bletransport,encodeAlertToBLEPacket\", \"bleAlertInfo.sTime.f\":\"%{private}3f\", \"bigneousAlertInformation.originTime\":\"%{private}3f\", \"ios Seconds until today\":\"%{private}3f\"}"
- "{\"msg%{public}.0s\":\"#bletransport,encodeAlertToBLEPacket\", \"buffer\":%{private, location:escape_only}s, \"bleAlertInfo.regionCode\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#bletransport,encodeAlertToBLEPacket\", \"buffer\":%{private, location:escape_only}s, \"regionCode\":%{private, location:escape_only}s, \"alertUIDHash\":%{private, location:escape_only}s, \"bleAlertInfo.sentTime\":\"%{private}0.3f\", \"Msgtypes\":%{private}d, \"alertType\":%{private}d, \"ExpirationLen\":%{private}d, \"ExpirationNum\":%{private}d, \"Geo\":%{private}d, \"MMI\":%{private}d, \"bleAlertInfo.geoCode\":%{private}llu, \"bleAlertInfo.Magnitude\":%{private}d, \"epi_latitude\":%{private}d, \"epi_longitude\":%{private}d, \"BLEAdvertiseTime\":%{private}d}"
- "{\"msg%{public}.0s\":\"#bletransport,encodeAlertToBLEPacket\", \"d\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#bletransport,fDispatchQueue invalid\"}"
- "{\"msg%{public}.0s\":\"#bletransport,getBleUIDFromAlertInformation\", \"bleUID\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#bletransport,getBleUIDFromAlertInformation\", \"hashString\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#bletransport,getCBAdvertiseRate\", \"bleCBAdvertiseRate\":%{private}d}"
- "{\"msg%{public}.0s\":\"#bletransport,getNumberOfSecondsOfWholeDaysUntilToday\", \"totalSecondsUntilToday\":%{private}d, \"nowUTC\":\"%{private}3f\"}"
- "{\"msg%{public}.0s\":\"#bletransport,sendIgneousAlertOverBLE cb\", \"Error\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#bletransport,sendIgneousAlertOverBLE cb\"}"
- "{\"msg%{public}.0s\":\"#bletransport,sendIgneousAlertOverBLE fAdvertiser invalid\"}"
- "{\"msg%{public}.0s\":\"#bletransport,sendIgneousAlertOverBLE fAdvertiser release\"}"
- "{\"msg%{public}.0s\":\"#bletransport,sendIgneousAlertOverBLE\"}"
- "{\"msg%{public}.0s\":\"#bm,init,unable to create settings\"}"
- "{\"msg%{public}.0s\":\"#chsel,createdSelector\", \"allowedListDone\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#chsel,getIgneousStateParameters,defaultRead,state\", \"isEnabled\":%{private}hhd, \"igenousStateInformation.isEnabled\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#chsel,getIgneousStateParameters,state\", \"isEnabled\":%{private}hhd, \"inSupportedCountry\":%{private}hhd, \"isInMagnetMode\":%{private}hhd, \"isUserOptedIn\":%{private}hhd, \"inCoverageRegion\":%{private}hhd, \"isInCountry\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#coreRoutine,getPeopleDensity,adding density\", \"startTimestamp\":\"%{private}0.2f\", \"endTimestamp\":\"%{private}0.2f\", \"scanDuration\":\"%{private}0.2f\", \"densityScore\":\"%{private}0.2f\"}"
- "{\"msg%{public}.0s\":\"#coreRoutine,getPeopleDensity,event out of bound,skipping\"}"
- "{\"msg%{public}.0s\":\"#coreRoutine,getPeopleDensity,fetch completed\", \"densityLen\":%{public}lu}"
- "{\"msg%{public}.0s\":\"#coreRoutine,getPeopleDensity,invalid start time,skipping\"}"
- "{\"msg%{public}.0s\":\"#coreRoutine,getPeopleDensity,received update\", \"Error\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#coreRoutine,getPeopleDensity,received update,\", \"count\":%{public}d}"
- "{\"msg%{public}.0s\":\"#coreRoutine,getPeopleDensity,received update,no densityEvents\"}"
- "{\"msg%{public}.0s\":\"#coreRoutine,getPeopleDensity,rssiHist\", \"rssi\":%{private}d, \"numDevices\":%{private}d}"
- "{\"msg%{public}.0s\":\"#coreRoutine,getPeopleDensity,rssiHist,invalid Type\"}"
- "{\"msg%{public}.0s\":\"#ctsa,Alert for production environment\", \"pKey\":%{private, location:escape_only}s, \"AlertKey\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#ctsa,Alert for production environment\"}"
- "{\"msg%{public}.0s\":\"#ctsa,com.apple.CTTelephonyCenter\", \"eDel\":%{public}d, \"eDelAvl\":%{public}d, \"saAvl\":%{public}d, \"saEmergencyAvl\":%{public}d}"
- "{\"msg%{public}.0s\":\"#ctsa,doesAlertPassesProductionCheck\", \"InternalInstall\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"#ctsa,doesAlertPassesProductionCheck,invalid dictionary\"}"
- "{\"msg%{public}.0s\":\"#ctsa,doesAlertPassesProductionCheck,not in prod\"}"
- "{\"msg%{public}.0s\":\"#ctsa,onFirstUnlock\"}"
- "{\"msg%{public}.0s\":\"#ctsa,processIgneousAlert1\"}"
- "{\"msg%{public}.0s\":\"#ctsa,processIgneousAlert2\"}"
- "{\"msg%{public}.0s\":\"#ctsa,ref prodId nil\"}"
- "{\"msg%{public}.0s\":\"#daemon,#warning,isIgneousAlert,invalidProxy\"}"
- "{\"msg%{public}.0s\":\"#daemon,#warning,processIgneousAlert,invalidProxy\"}"
- "{\"msg%{public}.0s\":\"#daemon,onBLEAlertReceived\"}"
- "{\"msg%{public}.0s\":\"#daemon,onBLEAlertReceptionCB\"}"
- "{\"msg%{public}.0s\":\"#daemonInterfaceProd,igneousEnablementStateInfo\", \"inCoverageRegion\":%{private}hhd, \"inSupportedCountry\":%{private}hhd, \"isInMagnetMode\":%{private}hhd, \"isUserOptedIn\":%{private}hhd, \"isEnabled\":%{private}hhd, \"isEmergencyAlertEnabled\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#iap,doesIgneousAlertPassPrecheck\", \"nowSeconds\":\"%{public}0.3f\", \"originTime\":\"%{public}0.3f\"}"
- "{\"msg%{public}.0s\":\"#iap,doesIgneousAlertPassPrecheck,stale alert received\"}"
- "{\"msg%{public}.0s\":\"#iap,doesIgneousLivabilityAlertPassPrecheck\", \"nowSeconds\":\"%{public}0.3f\", \"originTime\":\"%{public}0.3f\"}"
- "{\"msg%{public}.0s\":\"#iap,doesIgneousLivabilityAlertPassPrecheck,stale alert received\"}"
- "{\"msg%{public}.0s\":\"#saEventHistory,findLatestEventBefore\", \"time\":\"%{private}.2f\", \"fStartTimeSeconds\":\"%{private}.2f\", \"fEndTimeSeconds\":\"%{private}.2f\"}"
- "{\"msg%{public}.0s\":\"#saEventHistory,load\", \"filePath\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#saEventHistory,metaDataDict\", \"key\":%{private, location:escape_only}@, \"value\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#saEventHistory,metaValueToString\", \"error\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#saEventHistory,stringToMetaValue\", \"error\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#saEventHistory,stringToMetaValue\", \"key\":%{private, location:escape_only}@, \"value\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#saEventHistory,stringToMetaValue,empty string\"}"
- "{\"msg%{public}.0s\":\"#saEventHistory,stringToMetaValue,null data\"}"
- "{\"msg%{public}.0s\":\"#saSettingsProd\", \"isBluetoothEnabled\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,initialized,cannot initialize bleManager\"}"
- "{\"msg%{public}.0s\":\"#saSettingsProd,isBluetoothEnabled,bleManager is nil\"}"
- "{\"msg%{public}.0s\":\"#saanalytics,igneous received\", \"id\":%{private, location:escape_only}s, \"alertTextID\":%{private}lu, \"alertOriginationTime\":\"%{public}0.1f\", \"saReceivedTime\":\"%{public}0.1f\", \"insidePolygon\":%{private}d, \"saReceivedBeforeWEA\":%{public}d, \"salatencyOriginatorMilliSec\":\"%{public}0.2f\", \"salatencyServerMilliSec\":\"%{public}0.2f\", \"distanceToEpicenter\":\"%{private}0.2f\", \"MMI\":\"%{private}0.2f\", \"magnitude\":\"%{private}0.2f\", \"isTestAlert\":%{private}hhd}"

```
