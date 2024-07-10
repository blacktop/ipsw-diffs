## CoreMotion

> `/System/Library/Frameworks/CoreMotion.framework/Versions/A/CoreMotion`

```diff

-2946.0.27.0.0
-  __TEXT.__text: 0x2b64cc
-  __TEXT.__auth_stubs: 0x2410
-  __TEXT.__objc_methlist: 0x8814
+2946.0.20.0.0
+  __TEXT.__text: 0x2b5a80
+  __TEXT.__auth_stubs: 0x2420
+  __TEXT.__objc_methlist: 0x8894
   __TEXT.__const: 0x7f80
   __TEXT.__swift5_typeref: 0x257
   __TEXT.__swift5_reflstr: 0x2e

   __TEXT.__constg_swiftt: 0xb8
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__cstring: 0x328d2
-  __TEXT.__oslogstring: 0x1c8b6
+  __TEXT.__cstring: 0x32593
+  __TEXT.__oslogstring: 0x1c73d
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x10
-  __TEXT.__gcc_except_tab: 0x88f0
+  __TEXT.__gcc_except_tab: 0x88f4
   __TEXT.__unwind_info: 0x8ce8
   __TEXT.__eh_frame: 0x1d0
   __TEXT.__objc_classname: 0x12a7
-  __TEXT.__objc_methname: 0x1385f
-  __TEXT.__objc_methtype: 0x6d36
-  __TEXT.__objc_stubs: 0x9c00
+  __TEXT.__objc_methname: 0x13ab8
+  __TEXT.__objc_methtype: 0x6d3c
+  __TEXT.__objc_stubs: 0x9c80
   __DATA_CONST.__got: 0x628
-  __DATA_CONST.__const: 0x1a18
+  __DATA_CONST.__const: 0x1a08
   __DATA_CONST.__objc_classlist: 0x618
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b98
+  __DATA_CONST.__objc_selrefs: 0x3be8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x540
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__auth_got: 0x1220
+  __AUTH_CONST.__auth_got: 0x1228
   __AUTH_CONST.__auth_ptr: 0xb8
-  __AUTH_CONST.__const: 0x10ed0
-  __AUTH_CONST.__cfstring: 0xdc40
-  __AUTH_CONST.__objc_const: 0x14cb0
+  __AUTH_CONST.__const: 0x10ea0
+  __AUTH_CONST.__cfstring: 0xda20
+  __AUTH_CONST.__objc_const: 0x14d80
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x13b0
   __AUTH.__data: 0x258
-  __DATA.__objc_ivar: 0x1134
+  __DATA.__objc_ivar: 0x1144
   __DATA.__data: 0xbd0
   __DATA.__bss: 0x1170
   __DATA.__common: 0x130

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9510
-  Symbols:   1511
-  CStrings:  6583
+  Functions: 9521
+  Symbols:   1510
+  CStrings:  6565
 
Symbols:
+ _objc_copyCppObjectAtomic
- _kCMMotionCuesEnterVehicularStateNotification
- _kCMMotionCuesExitVehicularStateNotification
CStrings:
+ "-[CMOdometryManager stopBackgroundUpdatesPrivate]"
+ "-[CMOdometryManagerInternal init]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Daemon/Core/CSI/CLMachThreadSupport.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Daemon/Motion/GyroBiasEstimator/CLGyroBiasFitter.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Daemon/Motion/GyroBiasEstimator/CLNonlinearGyroBiasFitter.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Daemon/Shared/Utilities/CLNotifierClientAdapter.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Daemon/Shared/Utilities/CLNotifierServiceAdapter.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Daemon/Shared/Utilities/CLPreferences.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/CoreMotion/Accessory/CMMediaSession.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/CoreMotion/Accessory/CMMotionContextSession.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/CoreMotion/Activity/CMMotionActivityManager.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/CoreMotion/Error/CMErrorUtils.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/CoreMotion/PedestrianFence/CMPedestrianFenceManager.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/CoreMotion/RMConnection/RMConnectionClient.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/CoreMotion/RMConnection/RMConnectionEndpoint.m"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/CoreMotion/Sensor/CMMotionManager.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/MotionSensorLogging/MSLWriterManager.cpp"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLCppContainer.h"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Logging/CLBinaryLog.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/CLMotionCore.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/DeviceMotion/CLSensorFusionServiceSPU.h"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/IO/CLIoHidFastPathDevice.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/IO/CLIoHidInterface.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/IO/CLIoHidUtils.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/IO/CLSPUHIDDriverInterface.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/MagicMount/CLSPUMagicMountInterface.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/Notifiers/CLAccessoryNotifier.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/Notifiers/CLDeviceMotion.mm"
+ "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/SensorCalibration/CLGyroCalibrationDatabase.mm"
+ "02:41:08"
+ "Jun 15 2024"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLGyroCalibrationDatabase_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLCppContainer.h:241:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLGyroCalibrationDatabase_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLCppContainer.h:250:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = char, Callback = (lambda at /AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLCppContainer.h:241:46)]"
+ "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = char, Callback = (lambda at /AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLCppContainer.h:250:46)]"
- "-[CMMediaSession feedPoseAnchorWithAttitude:position:lidAngleDeg:timestampUs:]"
- "-[CMOdometryManager setupBIO]_block_invoke"
- "-[CMOdometryManager startBackgroundUpdatesPrivateUsingReferenceFrame:toQueue:withHandler:]_block_invoke"
- "-[CMOdometryManager stopBackgroundUpdatesPrivate]_block_invoke"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Daemon/Core/CSI/CLMachThreadSupport.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Daemon/Motion/GyroBiasEstimator/CLGyroBiasFitter.cpp"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Daemon/Motion/GyroBiasEstimator/CLNonlinearGyroBiasFitter.cpp"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Daemon/Shared/Utilities/CLNotifierClientAdapter.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Daemon/Shared/Utilities/CLNotifierServiceAdapter.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Daemon/Shared/Utilities/CLPreferences.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/CoreMotion/Accessory/CMMediaSession.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/CoreMotion/Accessory/CMMotionContextSession.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/CoreMotion/Activity/CMMotionActivityManager.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/CoreMotion/Error/CMErrorUtils.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/CoreMotion/PedestrianFence/CMPedestrianFenceManager.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/CoreMotion/RMConnection/RMConnectionClient.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/CoreMotion/RMConnection/RMConnectionEndpoint.m"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/CoreMotion/Sensor/CMMotionManager.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Framework/MotionSensorLogging/MSLWriterManager.cpp"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLCppContainer.h"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Logging/CLBinaryLog.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/CLMotionCore.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/DeviceMotion/CLSensorFusionServiceSPU.h"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/IO/CLIoHidFastPathDevice.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/IO/CLIoHidInterface.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/IO/CLIoHidUtils.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/IO/CLSPUHIDDriverInterface.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/MagicMount/CLSPUMagicMountInterface.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/Notifiers/CLAccessoryNotifier.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/Notifiers/CLDeviceMotion.mm"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Motion/SensorCalibration/CLGyroCalibrationDatabase.mm"
- "00:06:24"
- "Jun 29 2024"
- "avgFaceposeLatencySec"
- "avgTimeToFirstFaceposeInCameraRequest"
- "com.apple.locationd.motioncues.vehicular.enter"
- "com.apple.locationd.motioncues.vehicular.exit"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLGyroCalibrationDatabase_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLCppContainer.h:241:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = CLGyroCalibrationDatabase_Type::NotificationData, Callback = (lambda at /AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLCppContainer.h:250:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = char, Callback = (lambda at /AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLCppContainer.h:241:46)]"
- "const Object_T *safeDecoder(CLCppContainer *, Callback) [Object_T = char, Callback = (lambda at /AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreLocationFramework/Shared/Intersilo/CLCppContainer.h:250:46)]"
- "maxFaceposeLatencySec"
- "maxTimeToFirstFaceposeInCameraRequest"
- "minTimeToFirstFaceposeInCameraRequest"
- "percentageOfCameraRequestDueToAuxAndSrcMotion"
- "percentageOfCameraRequestDueToAuxMotion"
- "percentageOfCameraRequestDueToMaxDutyCycleMoving"
- "percentageOfCameraRequestDueToMaxDutyCycleStatic"
- "percentageOfCameraRequestDueToSrcMotion"
- "percentageOfFaceposeAnchorInvalidDueToConfidence"
- "percentageOfFaceposeAnchorInvalidDueToFaceposeFailure"
- "percentageOfFaceposeAnchorValid"
- "timeToFirstFaceposeInSession"

```
