## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

-30.48.2.1.2
-  __TEXT.__text: 0x1e674c
+30.51.1.1.1
+  __TEXT.__text: 0x1e779c
   __TEXT.__auth_stubs: 0x2ad0
-  __TEXT.__objc_stubs: 0x16e00
-  __TEXT.__objc_methlist: 0xb504
+  __TEXT.__objc_stubs: 0x16c40
+  __TEXT.__objc_methlist: 0xb55c
   __TEXT.__const: 0x3d40
-  __TEXT.__gcc_except_tab: 0x47f8
-  __TEXT.__cstring: 0x3ec13
-  __TEXT.__objc_classname: 0xa2a
-  __TEXT.__objc_methname: 0x2273e
-  __TEXT.__objc_methtype: 0x31b0
+  __TEXT.__gcc_except_tab: 0x4800
+  __TEXT.__cstring: 0x3f293
+  __TEXT.__objc_classname: 0xa21
+  __TEXT.__objc_methname: 0x226f5
+  __TEXT.__objc_methtype: 0x320e
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__oslogstring: 0x83ca
   __TEXT.__ustring: 0x10

   __TEXT.__swift5_capture: 0x193c
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x5440
+  __TEXT.__unwind_info: 0x5430
   __TEXT.__eh_frame: 0x2070
   __DATA_CONST.__auth_got: 0x1578
-  __DATA_CONST.__got: 0xc40
+  __DATA_CONST.__got: 0xc30
   __DATA_CONST.__auth_ptr: 0x570
-  __DATA_CONST.__const: 0xa760
-  __DATA_CONST.__cfstring: 0x9400
+  __DATA_CONST.__const: 0xa7a8
+  __DATA_CONST.__cfstring: 0x9420
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x188
+  __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_intobj: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x2f0
   __DATA_CONST.__objc_dictobj: 0x500
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x19b58
-  __DATA.__objc_selrefs: 0x75b0
-  __DATA.__objc_ivar: 0x140c
+  __DATA.__objc_const: 0x19d18
+  __DATA.__objc_selrefs: 0x7568
+  __DATA.__objc_ivar: 0x1438
   __DATA.__objc_data: 0x2a08
   __DATA.__data: 0x4218
-  __DATA.__bss: 0x6ab0
+  __DATA.__bss: 0x6ac0
   __DATA.__common: 0x380
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6528BE67-EACD-39D4-A1B4-EC928A334A29
-  Functions: 8985
-  Symbols:   1226
-  CStrings:  14040
+  UUID: D6F0E203-C57A-35CA-8571-93DB4A2E2A72
+  Functions: 9014
+  Symbols:   1224
+  CStrings:  14069
 
Symbols:
- _OBJC_CLASS_$_ISIcon
- _OBJC_CLASS_$_ISImageDescriptor
CStrings:
+ "### AASensorService Activate failed: %{error}"
+ "%s no longer nearby: %@"
+ "-[AASensorServiceDaemon _aaControllerEnsureStarted]"
+ "-[AASensorServiceDaemon _aaControllerEnsureStarted]_block_invoke"
+ "-[AASensorServiceDaemon _aaControllerEnsureStarted]_block_invoke_2"
+ "-[AASensorServiceDaemon _activate]"
+ "-[AASensorServiceDaemon _invalidate]"
+ "-[AAServicesXPCConnection sensorServiceActivate:completion:]"
+ "-[AAServicesXPCConnection sensorServiceActivate:completion:]_block_invoke"
+ "-[AAServicesXPCConnection sensorServiceReportSensorInfo:]"
+ "-[AASleepDetectionManager _sendMediaRemoteCommand:startRewindMediaTimer:]_block_invoke_2"
+ "-[AASleepDetectionManager _sendSleepDetectionFailureMetric:]"
+ "-[AASleepDetectionManager _sendSleepDetectionMediaMetricWithMediaPaused:rewoundMediaInSeconds:mediaStreamingAfterRewinding:]"
+ "-[AASleepDetectionManager _sendSleepDetectionUserResumedMedia:]"
+ "-[AASleepDetectionManager _sendSleepDuration]"
+ "-[BTSmartRoutingDaemon _lowestBatteryForDeviceWithAddress:]"
+ "-[BTSmartRoutingDaemon _startWxDiscoveryForWorkoutTimer:]"
+ "-[BTSmartRoutingDaemon _startWxDiscoveryForWorkoutTimer:]_block_invoke"
+ "-[BTSmartRoutingDaemon _startWxDiscoveryForWorkout]"
+ "@\"AASensorService\""
+ "AASensorServiceDaemon"
+ "Active AASensorService clients count: %d\n"
+ "BTAddress"
+ "Battery info lookup failed. No battery found for device with identifier: %@"
+ "DRServerIsATV"
+ "Found lowest battery: %@"
+ "Not routed to default route, return!"
+ "Reporting SensorInfo: %@"
+ "SR is not enabled on this device"
+ "Starting Wx discovery for workout"
+ "Stem click gesture notification received, wx %@ cmd %@"
+ "T@\"AASensorService\",&,N,V_sensorService"
+ "TB,N,V_DRServerIsATV"
+ "Temp Override status has changed -> cancelling stem click transaction timer"
+ "The media is still streaming after rewinding media is completed sending a pause command"
+ "Unable to find icon type for default product ID: %lu. Using SF Symbol"
+ "UserResumedAfterSleepDetected"
+ "Workout Wx discovery timer running"
+ "Wx discovery in progress"
+ "WxDiscoveryAfterWorkoutStartTimer: Start timer with delay %us"
+ "WxDiscoveryAfterWorkoutStartTimer: timer expires"
+ "_DRServerIsATV"
+ "_activatedSensorServiceSet"
+ "_currentAudioDevice is nil returning from _sendSleepDetectionFailureMetric"
+ "_currentAudioDevice is nil returning from _sendSleepDetectionMediaMetricWithMediaPaused"
+ "_currentAudioDevice is nil returning from _sendSleepDetectionUserResumedMedia"
+ "_currentAudioDevice is nil returning from _sendSleepDuration"
+ "_firstConnectedTime"
+ "_firstStemClick"
+ "_firstStemClickTime"
+ "_iconTypeForProductID:"
+ "_lastStemClickBTAddr"
+ "_lowestBatteryForDeviceWithAddress:"
+ "_ovadDataDict"
+ "_reportSensorInfo:"
+ "_sendMediaRemoteCommand MRMediaRemoteCommandSeekToPlaybackPosition previouslyIsPlaying %d newIsPlaying %d"
+ "_sendSleepDetectionMediaMetricWithMediaPaused:rewoundMediaInSeconds:mediaStreamingAfterRewinding:"
+ "_sendSleepDuration"
+ "_sensorDataUpdated:"
+ "_sensorService"
+ "_sleepDetectedConfidenceLevel is zero returning from _sendSleepDetectionFailureMetric"
+ "_sleepDetectedConfidenceLevel is zero returning from _sendSleepDetectionMediaMetricWithMediaPaused"
+ "_sleepDetectedConfidenceLevel is zero returning from _sendSleepDetectionUserResumedMedia"
+ "_startWxDiscoveryForWorkout"
+ "_startWxDiscoveryForWorkoutTimer:"
+ "_wxWorkoutDiscoveryTimer"
+ "firstClickAfterConnect"
+ "iconWithUTI:"
+ "mediaStreamingAfterRewinding"
+ "payloadData"
+ "proximityPairingPayloadWithData:"
+ "reportSensorInfo:"
+ "sensorService"
+ "sensorServiceActivate:completion:"
+ "sensorServiceReportSensorInfo:"
+ "setDRServerIsATV:"
+ "setSensorService:"
+ "sharedAASensorServiceDaemon"
+ "tempOverride"
+ "v24@0:8@\"AASensorInfo\"16"
+ "v32@0:8@\"AASensorService\"16@?<v@?@\"NSError\">24"
+ "v32@0:8B16@20B28"
- "%@-icon-%.0f.png"
- "("
- "+[AANotificationIconGenerator _writeIcon:withDescriptor:toURL:]"
- "+[AANotificationIconGenerator generateIcon:withDescriptor:tempFileName:]"
- "+[AANotificationIconGenerator generateNotificationIconForProductID:]"
- "-[AANearbyDeviceManagerDaemon _loadAADevicesConfigFromPairedDeviceForDevice:]"
- "-[BTSmartRoutingDaemon _lowestBatteryLevelForDeviceWithAddress:]"
- "AADeviceBatteryInfo no longer nearby: %@"
- "AANearbyDevice loading configs from paired device: %@"
- "AANotificationIconGenerator"
- "Attempting to write icon to %@"
- "B32@0:8q16@24"
- "Battery being shown on SR banner comes from SR map"
- "Battery being shown on SR banner comes from nearbydevice map"
- "Failed to generate SF Symbol based icon, using default"
- "Failed to write icon to %@"
- "Found lower battery level: %@"
- "Stem click gesture notification received, cmd %@"
- "T@\"AABattery\",R,C,N"
- "T@\"NSMutableDictionary\",C,N"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathComponent:isDirectory:"
- "Unable to access the Library directory."
- "Unable to create folder for icons: %@."
- "Unable to find icon type for default product ID: %lu"
- "Using existing icon from: %@"
- "_batteryForType:"
- "_batteryMap"
- "_deviceBatteryInfoUpdated:"
- "_imageTypeForProductID:"
- "_loadAADevicesConfigFromPairedDeviceForDevice:"
- "_lowestBatteryLevelForDeviceWithAddress:"
- "_sendSleepDetectionMediaMetricWithMediaPaused:rewoundMediaInSeconds:"
- "_setBatteryInMap:forType:"
- "_startWxDiscoveryForWorkoutStart"
- "_updateBatteryOfType:withDeviceBatteryInfo:"
- "_userNotificationImageDescriptor"
- "_writeIcon:withDescriptor:toURL:"
- "airpods-user-notification-%@-"
- "batteryMap"
- "com.apple.audioaccessoryd.notificationicons"
- "generateIcon:withDescriptor:tempFileName:"
- "generateNotificationIconForProductID:"
- "iconAtPath:"
- "imageForDescriptor:"
- "initWithSize:scale:"
- "initWithType:"
- "placeholder"
- "prepareImageForDescriptor:"
- "scale"
- "setBatteryMap:"
- "size"
- "updateWithDeviceBatteryInfo:"
- "updateWithPairedDeviceConfig:"
- "writeToURL:"

```
