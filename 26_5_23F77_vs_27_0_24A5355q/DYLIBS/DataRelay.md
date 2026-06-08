## DataRelay

> `/System/Library/PrivateFrameworks/DataRelay.framework/DataRelay`

```diff

-35.14.0.0.0
-  __TEXT.__text: 0x159c
-  __TEXT.__auth_stubs: 0x1c0
-  __TEXT.__objc_methlist: 0x2f8
+40.28.1.1.2
+  __TEXT.__text: 0x150c
+  __TEXT.__objc_methlist: 0x3a0
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__cstring: 0x4eb
-  __TEXT.__unwind_info: 0xd8
-  __TEXT.__objc_classname: 0x4f
-  __TEXT.__objc_methname: 0xa2b
-  __TEXT.__objc_methtype: 0x6bb
-  __TEXT.__objc_stubs: 0x280
-  __DATA_CONST.__got: 0x30
+  __TEXT.__cstring: 0x4ee
+  __TEXT.__unwind_info: 0xd0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x208
+  __DATA_CONST.__objc_selrefs: 0x278
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0xa0
-  __AUTH_CONST.__objc_const: 0x360
+  __AUTH_CONST.__objc_const: 0x3d0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x190

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E9EC7E62-CEA2-3F6D-99C7-31FBEC7967E4
+  UUID: 5A06B812-457B-32CF-9D61-114D9C441F64
   Functions: 45
-  Symbols:   193
-  CStrings:  175
+  Symbols:   194
+  CStrings:  42
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x8
- _objc_autoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
Functions:
~ -[DataRelayServiceClient description] : 84 -> 68
~ -[DataRelayServiceClient init] : 108 -> 100
~ -[DataRelayServiceClient activateWithCompletion:] : 160 -> 152
~ ___49-[DataRelayServiceClient activateWithCompletion:]_block_invoke : 268 -> 264
~ -[DataRelayServiceClient _activate] : 368 -> 360
~ -[DataRelayServiceClient _ensureXPCStarted] : 436 -> 432
~ -[DataRelayServiceClient _interrupted] : 204 -> 200
~ ___36-[DataRelayServiceClient invalidate]_block_invoke : 280 -> 276
~ -[DataRelayServiceClient _invalidated] : 332 -> 328
~ -[DataRelayServiceClient sensorDataAvailable:dataTypes:completion:] : 272 -> 276
~ ___67-[DataRelayServiceClient sensorDataAvailable:dataTypes:completion:]_block_invoke : 612 -> 600
~ -[DataRelayServiceClient sensorDataUnavailable:dataTypes:completion:] : 272 -> 276
~ ___69-[DataRelayServiceClient sensorDataUnavailable:dataTypes:completion:]_block_invoke : 612 -> 600
~ -[DataRelayServiceClient setDispatchQueue:] : 64 -> 12
~ ___67-[DataRelayServiceClient sensorDataAvailable:dataTypes:completion:]_block_invoke.cold.1 : 216 -> 208
~ ___69-[DataRelayServiceClient sensorDataUnavailable:dataTypes:completion:]_block_invoke.cold.1 : 216 -> 208
CStrings:
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@?"
- "@?16@0:8"
- "AAServicesXPCDaemonInterface"
- "B"
- "B16@0:8"
- "NSCoding"
- "NSSecureCoding"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dispatchQueue"
- "T@?,C,N,V_interruptionHandler"
- "T@?,C,N,V_invalidationHandler"
- "TB,R"
- "_activate"
- "_activateCalled"
- "_activateCompletion"
- "_dispatchQueue"
- "_ensureXPCStarted"
- "_interrupted"
- "_interruptionHandler"
- "_invalidateCalled"
- "_invalidateDone"
- "_invalidated"
- "_invalidationHandler"
- "_reportError:"
- "_setQueue:"
- "_xpcCnx"
- "activateWithCompletion:"
- "activeHRMSessionChanged:hrmState:completion:"
- "addObject:"
- "areHeadphonesNearbyAndEligibleToPlay:completion:"
- "array"
- "assetManagerShowDownloadNotificationForBTAddress:completionHandler:"
- "audioRoutingControlActivate:completion:"
- "audioSessionControlActivate:completion:"
- "audioSessionControlUpdate:"
- "componentsJoinedByString:"
- "description"
- "deviceManagerActivate:completion:"
- "deviceManagerFetchAADeviceBatteryInfoForAddress:deviceHandler:"
- "deviceManagerFetchAADeviceBatteryInfoForIdentifier:deviceHandler:"
- "deviceManagerFetchAccessoryFeatureFlagConfiguration:"
- "deviceManagerFetchAudioAccessoryDeviceForBTAddress:deviceHandler:"
- "deviceManagerFetchAudioAccessoryDeviceForIdentifier:deviceHandler:"
- "deviceManagerFetchPairedAudioAccessoryDevices:"
- "deviceManagerSendDeviceConfig:identifier:completion:"
- "deviceManagerUpdate:completion:"
- "dispatchQueue"
- "encodeWithCoder:"
- "getConversationAwarenessStateForDeviceAddress:btAddress:completion:"
- "getSleepStateForDeviceAddress:btAddress:completion:"
- "headphoneActivityProviderActivate:completion:"
- "informDRClientSensorDataAvailable:dataTypes:completion:"
- "informDRClientSensorDataUnavailable:dataTypes:completion:"
- "init"
- "initWithCoder:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "interruptionHandler"
- "invalidate"
- "invalidationHandler"
- "isTemporaryPairingConnectionAllowed:"
- "prewarmAudioAccessoriesForFitnessWorkout:"
- "proxCardUserActionOnHeadphone:btAddress:withAction:completion:"
- "remoteObjectProxyWithErrorHandler:"
- "resume"
- "sensorDataAvailable:dataTypes:completion:"
- "sensorDataUnavailable:dataTypes:completion:"
- "sensorServiceActivate:completion:"
- "sensorServiceSendPTEvent:value:completion:"
- "set3PDeviceInEarState:inEarStatePrimary:inEarStateSecondary:"
- "set3PDeviceProperty:property:value:"
- "setDispatchQueue:"
- "setHijackBlockingMode:mode:completion:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setMuteAction:auditToken:bundleIdentifier:"
- "setRemoteObjectInterface:"
- "supportsSecureCoding"
- "systemStateMonitorActivate:completion:"
- "systemStateMonitorFetchHealthKitDataWriteAllowedForDevice:completionHandler:"
- "systemStateMonitorFetchPairedHRMDevices:"
- "systemStateMonitorReportActiveHRMDeviceChanged:withSREnabled:"
- "systemStateMonitorReportSiriHijackEligibilityChanged:"
- "systemStateMonitorShowFitEducationNotificationForIdentifier:completionHandler:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"AAAudioRoutingControl\"16"
- "v24@0:8@\"AAAudioSessionControl\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v28@0:8@\"AudioAccessoryDevice\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"AA3PDeviceRoutingControl\"16i24i28"
- "v32@0:8@\"AAAudioRoutingControl\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"AAAudioRoutingControl\"16@?<v@?C@\"NSError\">24"
- "v32@0:8@\"AAAudioSessionControl\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"AADeviceManager\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"AAHeadphoneActivityProvider\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"AASensorService\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"AASystemStateMonitor\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"AADeviceBatteryInfo\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"AudioAccessoryDevice\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?c>24"
- "v32@0:8@16@?24"
- "v32@0:8@16i24i28"
- "v36@0:8@\"AAAudioRoutingControl\"16B24@?<v@?@\"NSError\">28"
- "v36@0:8@\"NSString\"16C24@?<v@?@\"NSError\">28"
- "v36@0:8@16B24@?28"
- "v36@0:8@16C24@?28"
- "v40@0:8@\"AA3PDeviceRoutingControl\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@\"AADeviceConfig\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"AAHeadphoneActivityProvider\"16@\"NSString\"24@?<v@?C@\"NSDate\"@\"NSError\">32"
- "v40@0:8@\"AAHeadphoneActivityProvider\"16@\"NSString\"24@?<v@?C@\"NSError\">32"
- "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v44@0:8@\"AAUSBSupportedDeviceManager\"16@\"NSString\"24C32@?<v@?@\"NSDictionary\"@\"NSError\">36"
- "v44@0:8@16@24C32@?36"
- "v60@0:8i16{?=[8I]}20@\"NSString\"52"
- "v60@0:8i16{?=[8I]}20@52"

```
