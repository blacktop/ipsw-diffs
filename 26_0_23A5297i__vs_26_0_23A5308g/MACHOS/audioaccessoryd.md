## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

-30.54.2.1.1
-  __TEXT.__text: 0x1e88a8
+30.58.1.0.0
+  __TEXT.__text: 0x1e951c
   __TEXT.__auth_stubs: 0x2ad0
-  __TEXT.__objc_stubs: 0x16d60
-  __TEXT.__objc_methlist: 0xb5ec
+  __TEXT.__objc_stubs: 0x16e80
+  __TEXT.__objc_methlist: 0xb6c4
   __TEXT.__const: 0x39d0
-  __TEXT.__gcc_except_tab: 0x4970
-  __TEXT.__cstring: 0x3f6a3
-  __TEXT.__objc_classname: 0xa21
-  __TEXT.__objc_methname: 0x22925
+  __TEXT.__gcc_except_tab: 0x4a4c
+  __TEXT.__cstring: 0x3fad3
+  __TEXT.__objc_classname: 0xa1f
+  __TEXT.__objc_methname: 0x22a9d
   __TEXT.__objc_methtype: 0x3266
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__oslogstring: 0x83ca

   __TEXT.__swift5_capture: 0x193c
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x5498
+  __TEXT.__unwind_info: 0x54c8
   __TEXT.__eh_frame: 0x2070
   __DATA_CONST.__auth_got: 0x1578
   __DATA_CONST.__got: 0xc38
   __DATA_CONST.__auth_ptr: 0x570
-  __DATA_CONST.__const: 0xa7d0
-  __DATA_CONST.__cfstring: 0x9560
+  __DATA_CONST.__const: 0xa7d8
+  __DATA_CONST.__cfstring: 0x9540
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140

   __DATA_CONST.__objc_arraydata: 0x2f0
   __DATA_CONST.__objc_dictobj: 0x500
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x19da0
-  __DATA.__objc_selrefs: 0x75d0
-  __DATA.__objc_ivar: 0x1440
+  __DATA.__objc_const: 0x19e70
+  __DATA.__objc_selrefs: 0x7618
+  __DATA.__objc_ivar: 0x1454
   __DATA.__objc_data: 0x2a08
   __DATA.__data: 0x4218
   __DATA.__bss: 0x6ac0

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6BA96925-4728-3569-B516-0C9844CFE5F4
-  Functions: 9033
-  Symbols:   1224
-  CStrings:  14118
+  UUID: 4ECCC5EB-2455-3B90-AC61-4524A9312C2E
+  Functions: 9055
+  Symbols:   1225
+  CStrings:  14147
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
CStrings:
+ "### Show Asset Download notification %{error}"
+ "-[AABatteryMonitorDaemon _newDeviceWithIdentifier:]"
+ "-[AADeviceManagerDaemon _accessoryDevicePerformActions:withConfig:]"
+ "-[AAFeatureOnboarding _registerForSystemNotifications]_block_invoke"
+ "-[AALowBatteryAlertDaemon _clearUserDismissedChargingNotificationsWhileProcessNotRunning]_block_invoke"
+ "-[AALowBatteryAlertDaemon _clearUserDismissedChargingNotificationsWhileProcessNotRunning]_block_invoke_2"
+ "-[AAServicesXPCConnection assetManagerShowDownloadNotificationForBTAddress:completionHandler:]"
+ "-[AAServicesXPCConnection assetManagerShowDownloadNotificationForBTAddress:completionHandler:]_block_invoke"
+ "-[AASleepDetectionManager _stopMonitoringSourceMotion]"
+ "-[SRConnectionManager _isHeadphoneEligibleForTakingConnectionFromWatch:]"
+ "-[SRConnectionManager _isHeadphoneEligibleForTakingConnectionFromWatch:]_block_invoke"
+ "AADeviceBatteryInfo not crated, device not paired (identifier: %@)"
+ "Connected banner visible, trying again later"
+ "EvaluateNearbyDevicesForConnection connectedWx %d nearbyWx %d srDisDeviceCount %d nearbySource %d btState %s audioRoute %s tipiScore %s sourceSRcapable %s audioCategory %d callStarted %s OD %s"
+ "ForceDisconnectWatchCheck: NB %@"
+ "ForceDisconnectWatchCheck: isEligible %s"
+ "ForceDisconnectWatchCheck: isNearbySourceWatch %s foundMatchedSource %s WxLh %@ nbAddr %@"
+ "LR"
+ "Low battery banner UI conditions not met, screenActive: %s , screenLocked: %s, lowBatteryBanner: %s, proxCard: %s, srBanner: %s"
+ "NearbySourceDevice found: ID %@, Name '%@', audio score %d (%s)"
+ "NearbySourceDevice lost: ID %@, IDS %@, Name '%@'"
+ "NearbySourceDevice updated: ID %@, Name '%@', audio score %d (%s)"
+ "No device found"
+ "No identifier found"
+ "Platform not supported for Asset Download notification"
+ "Property cannot be toggled on a non-B498 headset"
+ "Stopping source motion monitoring"
+ "System is first unlocked"
+ "T@\"NSMutableDictionary\",&,N,V_devicesMap"
+ "TB,V_systemFirstUnlocked"
+ "User Notifications visible: %@"
+ "User Notifications with notificationId: %@ and deviceId: %@, not found in visible notifications, dismissing tracker"
+ "_actionsOnFirstUnlock"
+ "_addAssetManagerNotificationCategory"
+ "_cleanMonitoringSourceMotion"
+ "_enumerateAvailableDevicesWithBlock:"
+ "_newDeviceWithIdentifier:"
+ "_startMonitoringSourceMotion"
+ "_stopMonitoringSourceMotion"
+ "_systemFirstUnlocked"
+ "_updateNearbyWxCount"
+ "_wxConnectedCount"
+ "_wxNearbyCount"
+ "assetManagerShowDownloadNotificationForBTAddress:completionHandler:"
+ "availableDevicesCount"
+ "btAddress %@ nbNm %@ isNb %s ts1 %s ts2 %s fw %@ isCp %s sc %d nbInEar %s nbLh %@ fd %s nbSt %s"
+ "setDevicesMap:"
+ "setSystemFirstUnlocked:"
+ "systemFirstUnlocked"
+ "v24@?0@\"AudioAccessoryDevice\"8^B16"
- "-[AAServicesDaemon _reportActiveHRMDeviceUpdated:withSREnabled:]"
- "-[AAServicesXPCConnection systemStateMonitorReportActiveHRMDeviceChanged:withSREnabled:]"
- "-[AASleepDetectionManager _sourceMotionMonitoringEnsureStopped]"
- "-[BTSmartRoutingDaemon _systemStateUpdateRequired]"
- "<R"
- "Active HRM Device changed: %@"
- "Checking UI conditions for reporting low batteries screenActive: %s , screenLocked: %s, lowBatteryBanner: %s, proxCard: %s, srBanner: %s"
- "EvaluateNearbyDevicesForConnection srDisDeviceCount %d btState %s audioRoute %s tipiScore %s sourceSRcapable %s audioCategory %d callStarted %s OD %s"
- "GetIDSDeviceFromWxLastConnectedHost: comparing, Wx: %@, IDS: %@, Model: %u, name: %@"
- "NearbyInfo device found/updated: ID %@, Name '%@', audio score %d (%s)"
- "NearbyInfo device lost: ID %@, IDS %@, Name '%@'"
- "Report Active HRM device %@"
- "SPLITTER_BLOCKING_TITLE"
- "Setting Siri Hijack eligiblity"
- "UI conditions to show low battery banner not met, trying again later"
- "_nearbyHRMEnabledDevice"
- "_sourceMotionMonitoringEnsureStarted"
- "_sourceMotionMonitoringEnsureStopped"
- "activeHRMDeviceChanged:"
- "btAddress %@ nbNm %@ isNb %s ts1 %s ts2 %s fw %@ isCp %s sc %d nbIe %s nbLh %@"
- "srDisDevice identifier %@"

```
