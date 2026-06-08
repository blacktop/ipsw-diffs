## AudioAccessoryAssetManagement

> `/System/Library/PrivateFrameworks/AudioAccessoryAssetManagement.framework/AudioAccessoryAssetManagement`

```diff

-35.14.0.0.0
-  __TEXT.__text: 0x23ac
-  __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_methlist: 0x4d0
+40.28.1.1.2
+  __TEXT.__text: 0x22e8
+  __TEXT.__objc_methlist: 0x598
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0xcd3
-  __TEXT.__unwind_info: 0x140
-  __TEXT.__objc_classname: 0xf3
-  __TEXT.__objc_methname: 0x10cf
-  __TEXT.__objc_methtype: 0x904
-  __TEXT.__objc_stubs: 0x600
-  __DATA_CONST.__got: 0x90
+  __TEXT.__cstring: 0xcd8
+  __TEXT.__unwind_info: 0x128
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x390
+  __DATA_CONST.__objc_selrefs: 0x418
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x130
+  __DATA_CONST.__got: 0x90
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0x5e0
+  __AUTH_CONST.__objc_const: 0x668
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0x240
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D292927E-B8AB-3029-8B0D-CA501ADFE0B2
+  UUID: 5F51B0D1-38E1-3EDC-BC8A-8EF60AE75395
   Functions: 87
   Symbols:   360
-  CStrings:  300
+  CStrings:  79
 
Symbols:
+ ___block_literal_global.108
+ ___block_literal_global.113
+ ___block_literal_global.116
+ ___block_literal_global.278
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x21
+ _objc_retain_x8
- ___block_literal_global.180
- ___block_literal_global.42
- ___block_literal_global.47
- ___block_literal_global.50
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x24
CStrings:
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSLocale\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSXPCConnection\""
- "@\"RBSAssertion\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@?"
- "@?16@0:8"
- "AAServicesXPCClientInterface"
- "AAServicesXPCDaemonInterface"
- "AMTranslationAssetInfo"
- "AudioAccessoryAssetManagementXPCClientInterface"
- "AudioAccessoryAssetManagementXPCServiceInterface"
- "B"
- "B16@0:8"
- "C"
- "C16@0:8"
- "NSCoding"
- "NSSecureCoding"
- "T@\"NSLocale\",&,N,V_locale"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dispatchQueue"
- "T@\"NSString\",&,N,V_displayName"
- "T@?,C,N,V_interruptionHandler"
- "T@?,C,N,V_invalidationHandler"
- "T@?,C,N,V_translationAssetsInfoHandler"
- "TB,N,V_isSuggested"
- "TB,R"
- "TC,N,V_assetStatus"
- "_assetStatus"
- "_dispatchQueue"
- "_displayName"
- "_downloadTranslationAssetsPid"
- "_ensureAADXPCStarted"
- "_ensureXPCStarted"
- "_interrupted"
- "_interruptionHandler"
- "_invalidateCalled"
- "_invalidateDone"
- "_invalidateXPCServiceAssertion"
- "_invalidated"
- "_invalidationHandler"
- "_isSuggested"
- "_locale"
- "_processAssertion"
- "_setQueue:"
- "_takeXPCServiceAssertion"
- "_translationAssets"
- "_translationAssetsInfoHandler"
- "_xpcAADCnx"
- "_xpcCnx"
- "aaServicesRequireReset"
- "acquireWithError:"
- "activeHRMDeviceChanged:withSREnabled:"
- "activeHRMSessionChanged:hrmState:completion:"
- "areHeadphonesNearbyAndEligibleToPlay:completion:"
- "arrayWithObjects:count:"
- "assetManagerShowDownloadNotificationForBTAddress:completionHandler:"
- "assetStatus"
- "attributeWithDomain:name:"
- "audioRoutingControlActivate:completion:"
- "audioSessionControlActivate:completion:"
- "audioSessionControlUpdate:"
- "bundleIdentifier"
- "containsValueForKey:"
- "conversationAwarenessStateUpdated:forDeviceAddress:"
- "decodeBoolForKey:"
- "description"
- "deviceHeadGestureDetected:"
- "deviceManagerActivate:completion:"
- "deviceManagerFetchAADeviceBatteryInfoForAddress:deviceHandler:"
- "deviceManagerFetchAADeviceBatteryInfoForIdentifier:deviceHandler:"
- "deviceManagerFetchAccessoryFeatureFlagConfiguration:"
- "deviceManagerFetchAudioAccessoryDeviceForBTAddress:deviceHandler:"
- "deviceManagerFetchAudioAccessoryDeviceForIdentifier:deviceHandler:"
- "deviceManagerFetchPairedAudioAccessoryDevices:"
- "deviceManagerFoundBatteryInfo:"
- "deviceManagerFoundDevice:"
- "deviceManagerLostBatteryInfo:"
- "deviceManagerLostDevice:"
- "deviceManagerSendDeviceConfig:identifier:completion:"
- "deviceManagerUpdate:completion:"
- "dispatchQueue"
- "displayName"
- "downloadTranslationAssets:localeIdentifiers:useCellular:showDownloadCompleteNotification:bundleIdentifier:completion:"
- "downloadTranslationAssets:useCellular:completion:"
- "downloadTranslationAssets:useCellular:showDownloadCompleteNotification:completion:"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateObjectsUsingBlock:"
- "getConversationAwarenessStateForDeviceAddress:btAddress:completion:"
- "getSleepStateForDeviceAddress:btAddress:completion:"
- "getTranslationAssets"
- "getTranslationAssets:"
- "getTranslationAssets:error:"
- "getTranslationAssetsDownloadSize:completion:"
- "getTranslationAssetsDownloadSize:localeIdentifiers:completion:"
- "handleForIdentifier:error:"
- "headphoneActivityProviderActivate:completion:"
- "i"
- "identifierWithPid:"
- "informDRClientSensorDataAvailable:dataTypes:completion:"
- "informDRClientSensorDataUnavailable:dataTypes:completion:"
- "init"
- "initWithCoder:"
- "initWithExplanation:target:attributes:"
- "initWithMachServiceName:options:"
- "initWithObjects:"
- "initWithServiceName:"
- "interfaceWithProtocol:"
- "interruptionHandler"
- "invalidate"
- "invalidationHandler"
- "isSuggested"
- "isTemporaryPairingConnectionAllowed:"
- "isValid"
- "locale"
- "mainBundle"
- "pidOfDownloadTranslationAssetsXPCService:"
- "prewarmAudioAccessoriesForFitnessWorkout:"
- "proxCardUserActionOnHeadphone:btAddress:withAction:completion:"
- "remoteObjectInterface"
- "remoteObjectProxyWithErrorHandler:"
- "resume"
- "sensorServiceActivate:completion:"
- "sensorServiceReportSensorInfo:"
- "sensorServiceSendPTEvent:value:completion:"
- "set3PDeviceInEarState:inEarStatePrimary:inEarStateSecondary:"
- "set3PDeviceProperty:property:value:"
- "setAssetStatus:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setDispatchQueue:"
- "setDisplayName:"
- "setExportedInterface:"
- "setExportedObject:"
- "setHijackBlockingMode:mode:completion:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsSuggested:"
- "setLocale:"
- "setMuteAction:auditToken:bundleIdentifier:"
- "setRemoteObjectInterface:"
- "setTranslationAssetsInfoHandler:"
- "showDownloadLanguagesNotification:"
- "siriHijackEligibilityUpdated:"
- "sleepStateUpdated:sleepTimestamp:forDeviceAddress:"
- "stringWithFormat:"
- "supportsSecureCoding"
- "systemStateMonitorActivate:completion:"
- "systemStateMonitorFetchHealthKitDataWriteAllowedForDevice:completionHandler:"
- "systemStateMonitorFetchPairedHRMDevices:"
- "systemStateMonitorReportActiveHRMDeviceChanged:withSREnabled:"
- "systemStateMonitorReportSiriHijackEligibilityChanged:"
- "systemStateMonitorShowFitEducationNotificationForIdentifier:completionHandler:"
- "targetWithProcessIdentifier:"
- "translationAssetsInfoHandler"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8i16"
- "v24@0:8@\"AAAudioRoutingControl\"16"
- "v24@0:8@\"AAAudioSessionControl\"16"
- "v24@0:8@\"AADeviceBatteryInfo\"16"
- "v24@0:8@\"AASensorInfo\"16"
- "v24@0:8@\"AudioAccessoryAssetManagementClient\"16"
- "v24@0:8@\"AudioAccessoryDevice\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v28@0:8@\"AudioAccessoryDevice\"16B24"
- "v28@0:8@16B24"
- "v28@0:8C16@\"NSString\"20"
- "v28@0:8C16@20"
- "v32@0:8@\"AA3PDeviceRoutingControl\"16i24i28"
- "v32@0:8@\"AAAudioRoutingControl\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"AAAudioRoutingControl\"16@?<v@?C@\"NSError\">24"
- "v32@0:8@\"AAAudioSessionControl\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"AADeviceManager\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"AAHeadphoneActivityProvider\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"AASensorService\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"AASystemStateMonitor\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@\"NSError\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"AADeviceBatteryInfo\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"AudioAccessoryDevice\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?c>24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16i24i28"
- "v36@0:8@\"AAAudioRoutingControl\"16B24@?<v@?@\"NSError\">28"
- "v36@0:8@\"NSString\"16C24@?<v@?@\"NSError\">28"
- "v36@0:8@16B24@?28"
- "v36@0:8@16C24@?28"
- "v36@0:8C16@\"NSDate\"20@\"NSString\"28"
- "v36@0:8C16@20@28"
- "v40@0:8@\"AA3PDeviceRoutingControl\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@\"AADeviceConfig\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"AAHeadphoneActivityProvider\"16@\"NSString\"24@?<v@?C@\"NSDate\"@\"NSError\">32"
- "v40@0:8@\"AAHeadphoneActivityProvider\"16@\"NSString\"24@?<v@?C@\"NSError\">32"
- "v40@0:8@\"AudioAccessoryAssetManagementClient\"16@\"NSArray\"24@?<v@?@\"NSError\"Q>32"
- "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16B24B28@?32"
- "v40@0:8@16Q24@?32"
- "v44@0:8@\"AAUSBSupportedDeviceManager\"16@\"NSString\"24C32@?<v@?@\"NSDictionary\"@\"NSError\">36"
- "v44@0:8@16@24C32@?36"
- "v56@0:8@\"AudioAccessoryAssetManagementClient\"16@\"NSArray\"24B32B36@\"NSString\"40@?<v@?@\"NSError\">48"
- "v56@0:8@16@24B32B36@40@?48"
- "v60@0:8i16{?=[8I]}20@\"NSString\"52"
- "v60@0:8i16{?=[8I]}20@52"

```
