## AudioAccessoryAssetManagement

> `/System/Library/PrivateFrameworks/AudioAccessoryAssetManagement.framework/AudioAccessoryAssetManagement`

```diff

-30.54.2.1.1
-  __TEXT.__text: 0x1894
+30.58.1.0.0
+  __TEXT.__text: 0x1e04
   __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_methlist: 0x24c
+  __TEXT.__objc_methlist: 0x42c
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x878
-  __TEXT.__unwind_info: 0xf0
-  __TEXT.__objc_classname: 0xb8
-  __TEXT.__objc_methname: 0x69f
-  __TEXT.__objc_methtype: 0x248
-  __TEXT.__objc_stubs: 0x440
+  __TEXT.__cstring: 0xac7
+  __TEXT.__unwind_info: 0x110
+  __TEXT.__objc_classname: 0xf2
+  __TEXT.__objc_methname: 0xd52
+  __TEXT.__objc_methtype: 0x6b4
+  __TEXT.__objc_stubs: 0x4a0
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x128
+  __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a8
-  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_selrefs: 0x2e0
+  __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x120
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0xc0
-  __AUTH_CONST.__objc_const: 0x408
-  __DATA.__objc_ivar: 0x30
-  __DATA.__data: 0x180
+  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__cfstring: 0xe0
+  __AUTH_CONST.__objc_const: 0x548
+  __DATA.__objc_ivar: 0x34
+  __DATA.__data: 0x240
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Translation.framework/Translation
+  - /System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7DF57352-BD27-3148-B4C2-6E24FB1A05C7
-  Functions: 62
-  Symbols:   271
-  CStrings:  162
+  UUID: F2CA3E13-20C9-3114-A6C0-AA8120474D88
+  Functions: 72
+  Symbols:   308
+  CStrings:  242
 
Symbols:
+ -[AudioAccessoryAssetManagementClient _ensureAADXPCStarted]
+ -[AudioAccessoryAssetManagementClient showDownloadLanguagesNotification:]
+ _OBJC_IVAR_$_AudioAccessoryAssetManagementClient._xpcAADCnx
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AAServicesXPCDaemonInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AAServicesXPCClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AAServicesXPCClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AAServicesXPCDaemonInterface
+ __OBJC_LABEL_PROTOCOL_$_AAServicesXPCClientInterface
+ __OBJC_LABEL_PROTOCOL_$_AAServicesXPCDaemonInterface
+ __OBJC_PROTOCOL_$_AAServicesXPCClientInterface
+ __OBJC_PROTOCOL_$_AAServicesXPCDaemonInterface
+ __OBJC_PROTOCOL_REFERENCE_$_AAServicesXPCClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_AAServicesXPCDaemonInterface
+ ___59-[AudioAccessoryAssetManagementClient _ensureAADXPCStarted]_block_invoke
+ ___59-[AudioAccessoryAssetManagementClient _ensureAADXPCStarted]_block_invoke_2
+ ___73-[AudioAccessoryAssetManagementClient showDownloadLanguagesNotification:]_block_invoke
+ ___73-[AudioAccessoryAssetManagementClient showDownloadLanguagesNotification:]_block_invoke.cold.1
+ ___73-[AudioAccessoryAssetManagementClient showDownloadLanguagesNotification:]_block_invoke_2
+ ___73-[AudioAccessoryAssetManagementClient showDownloadLanguagesNotification:]_block_invoke_2.cold.1
+ ___73-[AudioAccessoryAssetManagementClient showDownloadLanguagesNotification:]_block_invoke_3
+ ___73-[AudioAccessoryAssetManagementClient showDownloadLanguagesNotification:]_block_invoke_3.cold.1
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.130
+ ___block_literal_global.23
+ ___block_literal_global.26
+ _objc_msgSend$_ensureAADXPCStarted
+ _objc_msgSend$assetManagerShowDownloadNotificationForBTAddress:completionHandler:
+ _objc_msgSend$initWithMachServiceName:options:
- ___block_literal_global.47
CStrings:
+ "### ### Show download languages notification failed: %@, %@"
+ "### Show download languages notification failed"
+ "-[AudioAccessoryAssetManagementClient showDownloadLanguagesNotification:]_block_invoke"
+ "-[AudioAccessoryAssetManagementClient showDownloadLanguagesNotification:]_block_invoke_2"
+ "-[AudioAccessoryAssetManagementClient showDownloadLanguagesNotification:]_block_invoke_3"
+ "AAServicesXPCClientInterface"
+ "AAServicesXPCDaemonInterface"
+ "Show download languages notification returning with error %{error}"
+ "Show download languages notification with error: %{error}"
+ "_ensureAADXPCStarted"
+ "_xpcAADCnx"
+ "aaServicesRequireReset"
+ "activeHRMDeviceChanged:withSREnabled:"
+ "activeHRMSessionChanged:hrmState:completion:"
+ "areHeadphonesNearbyAndEligibleToPlay:completion:"
+ "assetManagerShowDownloadNotificationForBTAddress:completionHandler:"
+ "audioRoutingControlActivate:completion:"
+ "audioSessionControlActivate:completion:"
+ "audioSessionControlUpdate:"
+ "com.apple.AudioAccessoryServices"
+ "deviceHeadGestureDetected:"
+ "deviceManagerActivate:completion:"
+ "deviceManagerFetchAADeviceBatteryInfoForAddress:deviceHandler:"
+ "deviceManagerFetchAADeviceBatteryInfoForIdentifier:deviceHandler:"
+ "deviceManagerFetchAudioAccessoryDeviceForBTAddress:deviceHandler:"
+ "deviceManagerFetchPairedAudioAccessoryDevices:"
+ "deviceManagerFoundBatteryInfo:"
+ "deviceManagerFoundDevice:"
+ "deviceManagerLostBatteryInfo:"
+ "deviceManagerLostDevice:"
+ "deviceManagerSendDeviceConfig:identifier:completion:"
+ "deviceManagerUpdate:completion:"
+ "getting Show download languages notification WithCompletion"
+ "informDRClientSensorDataAvailable:dataTypes:completion:"
+ "informDRClientSensorDataUnavailable:dataTypes:completion:"
+ "initWithMachServiceName:options:"
+ "isTemporaryPairingConnectionAllowed:"
+ "prewarmAudioAccessoriesForFitnessWorkout:"
+ "proxCardUserActionOnHeadphone:btAddress:withAction:completion:"
+ "sensorServiceActivate:completion:"
+ "sensorServiceReportSensorInfo:"
+ "setHijackBlockingMode:mode:completion:"
+ "setMuteAction:auditToken:bundleIdentifier:"
+ "showDownloadLanguagesNotification:"
+ "siriHijackEligibilityUpdated:"
+ "systemStateMonitorActivate:completion:"
+ "systemStateMonitorFetchHealthKitDataWriteAllowedForDevice:completionHandler:"
+ "systemStateMonitorFetchPairedHRMDevices:"
+ "systemStateMonitorReportActiveHRMDeviceChanged:withSREnabled:"
+ "systemStateMonitorReportSiriHijackEligibilityChanged:"
+ "systemStateMonitorShowFitEducationNotificationForIdentifier:completionHandler:"
+ "v24@0:8@\"AAAudioRoutingControl\"16"
+ "v24@0:8@\"AAAudioSessionControl\"16"
+ "v24@0:8@\"AADeviceBatteryInfo\"16"
+ "v24@0:8@\"AASensorInfo\"16"
+ "v24@0:8@\"AudioAccessoryDevice\"16"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSDictionary\">16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v28@0:8@\"AudioAccessoryDevice\"16B24"
+ "v28@0:8@16B24"
+ "v32@0:8@\"AAAudioRoutingControl\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"AAAudioRoutingControl\"16@?<v@?C@\"NSError\">24"
+ "v32@0:8@\"AAAudioSessionControl\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"AADeviceManager\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"AASensorService\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"AASystemStateMonitor\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"AADeviceBatteryInfo\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"AudioAccessoryDevice\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?c>24"
+ "v36@0:8@\"AAAudioRoutingControl\"16B24@?<v@?@\"NSError\">28"
+ "v40@0:8@\"AADeviceConfig\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSError\">32"
+ "v40@0:8@16Q24@?32"
+ "v44@0:8@\"AAUSBSupportedDeviceManager\"16@\"NSString\"24C32@?<v@?@\"NSDictionary\"@\"NSError\">36"
+ "v44@0:8@16@24C32@?36"
+ "v60@0:8i16{?=[8I]}20@\"NSString\"52"
+ "v60@0:8i16{?=[8I]}20@52"

```
