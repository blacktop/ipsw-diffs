## CoreMotion

> `/System/Library/Frameworks/CoreMotion.framework/CoreMotion`

```diff

-2956.0.7.0.0
-  __TEXT.__text: 0x3430f0
-  __TEXT.__auth_stubs: 0x2a00
-  __TEXT.__objc_methlist: 0xb664
-  __TEXT.__const: 0xa398
+2960.0.47.0.3
+  __TEXT.__text: 0x351dd0
+  __TEXT.__auth_stubs: 0x29f0
+  __TEXT.__objc_methlist: 0xbf6c
+  __TEXT.__const: 0xa448
   __TEXT.__swift5_typeref: 0x257
   __TEXT.__swift5_reflstr: 0x2e
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__constg_swiftt: 0xb8
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__cstring: 0x3ecae
-  __TEXT.__oslogstring: 0x25ce3
+  __TEXT.__cstring: 0x3fb44
+  __TEXT.__oslogstring: 0x28135
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x10
-  __TEXT.__gcc_except_tab: 0xb078
-  __TEXT.__unwind_info: 0xaaf8
-  __TEXT.__eh_frame: 0x1d0
+  __TEXT.__swift_as_entry: 0x18
+  __TEXT.__swift_as_ret: 0x18
+  __TEXT.__gcc_except_tab: 0xb438
+  __TEXT.__unwind_info: 0xa688
+  __TEXT.__eh_frame: 0x1c8
   __TEXT.__objc_classname: 0x18ae
-  __TEXT.__objc_methname: 0x19416
-  __TEXT.__objc_methtype: 0x867c
-  __TEXT.__objc_stubs: 0xd040
-  __DATA_CONST.__got: 0x790
+  __TEXT.__objc_methname: 0x1959e
+  __TEXT.__objc_methtype: 0x87d5
+  __TEXT.__objc_stubs: 0xd120
+  __DATA_CONST.__got: 0x798
   __DATA_CONST.__const: 0x3720
   __DATA_CONST.__objc_classlist: 0x7f0
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c60
+  __DATA_CONST.__objc_selrefs: 0x4ce0
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x6f8
   __DATA_CONST.__objc_arraydata: 0x250
-  __AUTH_CONST.__auth_got: 0x1518
-  __AUTH_CONST.__auth_ptr: 0xc0
-  __AUTH_CONST.__const: 0x129b8
-  __AUTH_CONST.__cfstring: 0x11780
-  __AUTH_CONST.__objc_const: 0x1bca0
+  __AUTH_CONST.__auth_got: 0x1510
+  __AUTH_CONST.__auth_ptr: 0xf0
+  __AUTH_CONST.__const: 0x12bc8
+  __AUTH_CONST.__cfstring: 0x12260
+  __AUTH_CONST.__objc_const: 0x1ae08
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0xaf0
   __AUTH.__data: 0x210
-  __DATA.__objc_ivar: 0x1580
+  __DATA.__objc_ivar: 0x15ac
   __DATA.__data: 0xe68
-  __DATA.__bss: 0x480
-  __DATA.__common: 0x158
-  __DATA_DIRTY.__objc_ivar: 0x150
+  __DATA.__bss: 0x470
+  __DATA.__common: 0x100
+  __DATA_DIRTY.__objc_ivar: 0x154
   __DATA_DIRTY.__objc_data: 0x4470
-  __DATA_DIRTY.__data: 0x108
-  __DATA_DIRTY.__bss: 0xed8
+  __DATA_DIRTY.__data: 0x138
   __DATA_DIRTY.__common: 0x68
+  __DATA_DIRTY.__bss: 0xf58
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 11480
-  Symbols:   1722
-  CStrings:  14804
+  Functions: 11188
+  Symbols:   1735
+  CStrings:  15044
 
Symbols:
+ _BTAccessoryManagerGetPrimaryBudSide
+ _BTDeviceGetAddressString
+ _BTDeviceGetName
+ _BTLocalDeviceAddCallbacks
+ _BTLocalDeviceGetConnectedDevices
+ _BTLocalDeviceGetDefault
+ _BTLocalDeviceRemoveCallbacks
+ _CLInternalGetPinnedLocationAuthorizationState
+ _CLInternalSetPinnedLocationAuthorization
+ _IOHIDDeviceCreate
+ _IOHIDDeviceSetReport
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
+ __ZNSt3__117bad_function_callD0Ev
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ _objc_retain_x9
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_initStructMetadataWithLayoutString
- _BTDeviceAddressFromString
- _BTDeviceFromAddress
- __ZNSt3__16__sortIRNS_6__lessIffEEPfEEvT0_S5_T_
- __ZNSt9exceptionD2Ev
- __ZTISt9exception
- _acos
- _objc_retain_x10
- _swift_arrayDestroy
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_initStructMetadata
CStrings:
+ "#Warning Messaging connection %{private}p interrupted!"
+ "#Warning Messaging connection %{private}p invalidated!"
+ "#Warning Streaming server connection %{private}p.%{private}p interrupted!"
+ "#Warning Streaming server connection %{private}p.%{private}p invalidated!"
+ "-[CMMediaSession _feedActiveAudioRouteChangedEvent]"
+ "-[CMMediaSession _feedAdaptiveLatencyJitterBufferLevel]"
+ "-[CMMediaSession _feedLidAngle:]"
+ "-[CMMediaSession _startHeadTracking]_block_invoke"
+ "-[CMMediaSession feedPoseAnchorWithAttitude:position:lidAngleDeg:numberOfDetectedFaces:timestampUs:]"
+ "04:55:45"
+ "@\"CMDeviceOrientationManager\""
+ "@\"CMHeadphoneActivityManager\""
+ "@104@0:8{?={?=dddd}{?=ddd}dddd}16"
+ "@112@0:8{?={?=dddd}{?=ddd}dddd}16d104"
+ "@120@0:8{?={?=dddd}{?=fff}{?=fff}{?=fff}iBBBfBBi}16{?=f{?=fff}}104"
+ "@128@0:8{?={?=dddd}{?=fff}{?=fff}{?=fff}iBBBfBBi}16{?=f{?=fff}}104d120"
+ "@64@0:8d16d24d32d40q48d56"
+ "AbsoluteAltitude: %f, Accuracy: %f, Precision %f, FilteredPressure %f, statusInfo: %ld, timestamp :%f"
+ "B24@0:8^{Sample=d{?={?=dddd}{?=fff}{?=fff}{?=fff}iBBBfBBi}{?=f{?=fff}}BIC{Status=S}f}16"
+ "C20@0:8C16"
+ "C24@0:8^{CLLocationCoordinate2D=dd}16"
+ "CL: CLInternalGetPinnedLocationAuthorizationState"
+ "CL: CLInternalSetPinnedLocationAuthorization"
+ "CLAccessoryMonitor"
+ "CLAccessoryNotifier::CLAccessoryNotifier(const char *, int, int, int)"
+ "CMOQuaternion CMRelDMFwdPredictor::getPredictedDeltaRotation(uint64_t &)"
+ "CMPose,q.x,%f,q.y,%f,q.z,%f,q.w,%f,translation.x,%f,translation.y,%f,translation.z,%f,consumedAuxTimestamp,%f,receivedAuxTimestamp,%f,machAbsTimestamp,%f,presentationTimestamp,%f,timestamp,%f"
+ "Cancelling the streaming server connection %{private}p.%{private}p"
+ "CorrespondencePoseResidualThreshold"
+ "Error received on the streaming client connection %{private}p"
+ "Feb 16 2025"
+ "IOReturn CLIoHidInterface::Device::sendIOHIDDeviceReport(const uint8_t *, size_t)"
+ "Streaming request sent on streaming listener %{private}p.%{private}p"
+ "Td,R,N,V_filteredPressure"
+ "TempestPreferenceRenderingOverheadSeconds"
+ "T{?=fff},R,N"
+ "[AccessoryDeviceMotion] USB Mode change during %{public}@. Skipping..."
+ "[AccessoryDeviceMotion] USB Mode change during Spatial Audio. Resetting..."
+ "[AccessoryDeviceMotion] USB Mode change during Streaming. Resetting..."
+ "[AccessoryMonitor] DM Session,duration,%{public}d,mean_temperature,%{public}d,min_temperature,%{public}d,max_temperature,%{public}d,bias_temperature,%{public}d"
+ "[AccessoryMonitor] Sending analytics: \n%{private}@"
+ "[AccessoryMonitor] Setting update interval to %{public}f, reportInterval %{public}@"
+ "[AccessoryMonitor] Unrecognized update interval notification %{public}d"
+ "[AccessoryMonitor] Unsupported version of DM session %{public}d"
+ "[AccessoryMonitor] event type %{public}d, seq %{public}u, payload bytes %{public}.*P"
+ "[AccessoryMonitor] invalid message: empty message %{public}p (%zd)"
+ "[AccessoryMonitor] invalid message: length (%{public}zd) is smaller than header (%{public}zd)"
+ "[AccessoryMonitor] invalid message: length (%{public}zd) is smaller than reported message size (%{public}d)"
+ "[AccessoryMonitor] invalid message: mismatched version (local:%{public}d remote:%{public}d), dropping"
+ "[AccessoryMonitor] invalid message: unknown type (%{public}d), dropping"
+ "[AccessoryMonitor] onAccessoryStatusUpdate - Accessory ping sent."
+ "[AccessoryMonitor] onAccessoryStatusUpdate error. No service ref."
+ "[AccessoryMonitor] unexpected event type %{public}u"
+ "[AccessoryNotifier] %{public}s subscribes to AudioAccessoryInterface"
+ "[AccessoryNotifier] Service removed for usage page %{public}d usage %{public}d"
+ "[AccessoryNotifier] onAccessoryStatusUpdate - Failed to ping"
+ "[AccessoryNotifier] onNewHidService error! BT Address mismatched for usage pair (%{public}d, %{public}d). Expecting %{private}llx, got %{private}llx"
+ "[AccessoryNotifier] onNewHidService. New service %{private}p for usage pair (%{public}d, %{public}d) with BT address %{private}llx"
+ "[AccessoryNotifier] setCustomProperty error. No service ref."
+ "[AccessoryNotifier] setCustomProperty error. Size %zu not allowed."
+ "[AccessoryNotifier] setCustomProperty failed - %{public}x"
+ "[AccessoryNotifier] setCustomProperty succeeded."
+ "[CLAccessoryNotifier] Usage pair (%{public}d, %{public}d) received kActiveDeviceUpdated. Update BT address to %{private}llx"
+ "[CLAccessoryNotifier] getConfig failed for usage pair (%{public}d, %{public}d). No valid service"
+ "[CLAccessoryNotifier] getConfig,hardwareModel,%{public}d,side,%{public}d,SN,%{private}s"
+ "[CLAudioAccessoryInterface] Client %p subscribes"
+ "[CLAudioAccessoryInterface] Failed to get jitter buffer level because BT device does not exist"
+ "[CLAudioAccessoryInterface] Failed to get jitter buffer level. Invalid BT AccessoryManager"
+ "[CLAudioAccessoryInterface] Failed to register BT local device event callback.  Status %{public}d"
+ "[CLAudioAccessoryInterface] Local device unavailable. Status %{public}d"
+ "[CLAudioAccessoryInterface] Notify client %p with event %u"
+ "[CLAudioAccessoryInterface] Received BT_LOCAL_DEVICE_CONNECTION_STATUS_CHANGED"
+ "[CLAudioAccessoryInterface] Received jitter buffer level %{public}d"
+ "[CLAudioAccessoryInterface] Selected device with BT address %{private}s"
+ "[CLAudioAccessoryInterface] Sending kActivitDeviceUpdated to client %p"
+ "[CLAudioAccessoryInterface] USB connection mode change"
+ "[CLAudioAccessoryInterface] Unexpected JBL change for product 0x%{public}x"
+ "[CLAudioAccessoryInterface] Warning! Selecting invalid BT address %{private}s"
+ "[CLAudioAccessoryInterface] accessoryEventHandler failed. Invalid BT AccessoryManager"
+ "[CLAudioAccessoryInterface] getBTAddress failed. Can't get BT address string from BT Device."
+ "[CLAudioAccessoryInterface] getBTAddress failed. Invalid BT Device."
+ "[CLAudioAccessoryInterface] getBTAddress returned %{private}llu from address %{private}s"
+ "[CLAudioAccessoryInterface] in ear status - invalid BT AccessoryManager"
+ "[CLAudioAccessoryInterface] refreshBTDevice - Failed to get the product ID. Error: %{public}d"
+ "[CLAudioAccessoryInterface] refreshBTDevice failed. Devices not found"
+ "[CLAudioAccessoryInterface] refreshBTDevice failed. Invalid BT AccessoryManager"
+ "[CLAudioAccessoryInterface] refreshBTDevice failed. Invalid BT Local Device"
+ "[CLAudioAccessoryInterface] refreshBTDevice failed. Invalid BT Session"
+ "[CLAudioAccessoryInterface] refreshBTDevice. Active device %{private}s side changed, %{public}d"
+ "[CLAudioAccessoryInterface] refreshBTDevice. Active device %{private}s unchanged."
+ "[CLAudioAccessoryInterface] refreshBTDevice. Current active device %{public}p not available"
+ "[CLAudioAccessoryInterface] refreshBTDevice. Current active device changed to %{public}p,addr,%{private}s,PID,0x%{public}x,side,%{public}d"
+ "[CLAudioAccessoryInterface] refreshBTDevice. First InEar device selected"
+ "[CLAudioAccessoryInterface] refreshBTDevice. Matched device found"
+ "[CLAudioAccessoryInterface] refreshBTDevice. Name,%{private}s, Address,%{private}s, inear,%{public}d,%{public}d"
+ "[CLAudioAccessoryInterface] refreshBTDevice. No matched device. Use the first listed device."
+ "[CLAudioAccessoryInterface] update TimeSync failed due to invalid BT AccessoryManager"
+ "[CLIoHidInterface] createIOHIDDevice failed - AOP service doesn't exist"
+ "[CLIoHidInterface] createIOHIDDevice failed - can't create HID device"
+ "[CLIoHidInterface] createIOHIDDevice failed - can't find the grandparent of the service"
+ "[CLIoHidInterface] createIOHIDDevice failed - can't find the parent of the service"
+ "[CLIoHidInterface] createIOHIDDevice failed - can't open the HID device"
+ "[CLIoHidInterface] createIOHIDDevice failed - null service ref"
+ "[CLIoHidInterface] sendIOHIDDeviceReport failed - can't create HID Device"
+ "[CMAnchorMotionCorrespondence] Calling anchor correspondence."
+ "[CMAnchorMotionCorrespondence] Entering the first burst condition"
+ "[CMAnchorMotionCorrespondence] Resetting for large correspondence gap: dtSeconds %f fLastAnchorCorrespondenceUpdateUs is %llu."
+ "[CMAnchorMotionCorrespondence] fFirstBurst is set to false."
+ "[CMAnchorMotionCorrespondence] threshold is set to %.2f"
+ "[CMHeadToHeadsetAttitudeEstimator] AngleToDefault: %f."
+ "[CMMediaSession] %{public}@"
+ "[CMMediaSession] Active audio route changed, reloading JBL"
+ "[CMMediaSession] Correspondence threshold new: %{public}f old: %{public}f"
+ "[CMMediaSession] Current JBL: %{public}u"
+ "[CMMediaSession] Face Yaw: %f, Pitch: %f, Roll: %f, User HorizontalAngle: %f, VerticalAngle: %f"
+ "[CMMediaSession] Failed to feed JBL value, retrying in %{public}.1f sec"
+ "[CMMediaSession] Failed to feed JBL value, using default value for prediction"
+ "[CMMediaSession] Ignore anchor since distance: %{public}.1f cm is under the %{public}.1f cm threshold."
+ "[CMMediaSession] Ignoring _feedAccessoryConfig call that occurred after _stop was called."
+ "[CMMediaSession] Ignoring _feedAccessoryDeviceMotion call that occurred after _stop was called."
+ "[CMMediaSession] Ignoring _feedAccessoryInEarStatus call that occurred after _stop was called."
+ "[CMMediaSession] Ignoring _feedActiveAudioRouteChangedEvent call that occurred after _stop was called."
+ "[CMMediaSession] Ignoring _feedAdaptiveLatencyJitterBufferLevel call that occurred after _stop was called."
+ "[CMMediaSession] Ignoring _feedDisplayCount call that occurred after _stop was called."
+ "[CMMediaSession] Ignoring _feedFaceKitData call that occurred after _stop was called."
+ "[CMMediaSession] Ignoring _feedLidAngle call that occurred after _stop was called."
+ "[CMMediaSession] Ignoring _feedPoseAnchor call that occurred after _stop was called."
+ "[CMMediaSession] Ignoring _feedPredictorEstimates call that occurred after _stop was called."
+ "[CMMediaSession] Ignoring _feedScreenUnlockedEvent call that occurred after _stop was called."
+ "[CMMediaSession] Ignoring _feedSourceDeviceIMU call that occurred after _stop was called."
+ "[CMMediaSession] Ignoring feedPoseAnchorWithAttitude call that occurred after _stop was called."
+ "[CMMediaSession] Previous Source Activity: %{public}s, Current Source Activity: %{public}s"
+ "[CMMediaSession] Stem gravity angle: %{public}f, Stem faceY angle: %{public}f, FaceY gravity angle: %{public}f."
+ "[CMMediaSession] renderingOverheadSeconds new: %{public}.3f old: %{public}.3f"
+ "[CMMediaSession] renderingOverheadSeconds should usually be positive and less than 1 sec"
+ "[CMMediaSession][Cam %{public}u] Received %{public}lu faces of %{public}d detected faces"
+ "[CMMediaSession][HeadsetActivity] Activity encountered an error: %{public}@"
+ "[CMMediaSession][HeadsetActivity] Device disconnected. Resetting headphone activity type to unknown."
+ "[CMMediaSession][HeadsetActivity] Headphone other moving started."
+ "[CMMediaSession][HeadsetActivity] Headset entered other moving. Source already static. Case 2-5."
+ "[CMMediaSession][HeadsetActivity] Headset entered ped. Source is already static. Case 1-5."
+ "[CMMediaSession][HeadsetActivity] Headset entered pedestrian. Source is already pedestrian. Case 5-5."
+ "[CMMediaSession][HeadsetActivity] Headset entered pedestrian. Source is already pedestrian. Case 6-5."
+ "[CMMediaSession][HeadsetActivity] Headset entered static. Source is already static. Case 3-5."
+ "[CMMediaSession][HeadsetActivity] Headset entered walking. Source is already walking. Case 4-5."
+ "[CMMediaSession][HeadsetActivity] Headset entered walking. Source is already walking. Case 7-5."
+ "[CMMediaSession][HeadsetActivity] Headset exited static. Source is don't care. Case 3-7 and 3-8."
+ "[CMMediaSession][HeadsetActivity] Headset exiting other moving. Source don't care. Case 2-7 and 2-8."
+ "[CMMediaSession][HeadsetActivity] Headset exiting pedestrian. Source is don't care. Case 1-7 and 1-8."
+ "[CMMediaSession][HeadsetActivity] Headset exiting pedestrian. Source is don't care. Case 5-7 and 5-8."
+ "[CMMediaSession][HeadsetActivity] Headset exiting pedestrian. Source is don't care. Case 6-7 and 6-8."
+ "[CMMediaSession][HeadsetActivity] Headset exiting walking. Source is don't care. Case 4-7 and 4-8."
+ "[CMMediaSession][HeadsetActivity] Headset exiting walking. Source is don't care. Case 7-7 and 7-8."
+ "[CMMediaSession][HeadsetActivity] Headset other moving stopped."
+ "[CMMediaSession][HeadsetActivity] Headset pedestrian started."
+ "[CMMediaSession][HeadsetActivity] Headset pedestrian stopped."
+ "[CMMediaSession][HeadsetActivity] Headset running started."
+ "[CMMediaSession][HeadsetActivity] Headset running stopped."
+ "[CMMediaSession][HeadsetActivity] Headset static started."
+ "[CMMediaSession][HeadsetActivity] Headset static stopped."
+ "[CMMediaSession][HeadsetActivity] Headset walking started."
+ "[CMMediaSession][HeadsetActivity] Headset walking stopped."
+ "[CMMediaSession][HeadsetActivity] No activity returned!"
+ "[CMMediaSession][HeadsetActivity] Previous Headphone Activity: %s, Current headphone activity: %s"
+ "[CMMediaSession][HeadsetActivity] Source entered pedestrian. Headset is already pedestrian. Case 5-1."
+ "[CMMediaSession][HeadsetActivity] Source entered pedestrian. Headset is already pedestrian. Case 6-1."
+ "[CMMediaSession][HeadsetActivity] Source entered static. Headset is other moving. Case 2-1."
+ "[CMMediaSession][HeadsetActivity] Source entered static. Headset is pedestrian. Case 1-1."
+ "[CMMediaSession][HeadsetActivity] Source entered static. Headset is static. Case 3-1."
+ "[CMMediaSession][HeadsetActivity] Source entered walking. Headset is already walking. Case 4-1."
+ "[CMMediaSession][HeadsetActivity] Source entered walking. Headset is already walking. Case 7-1."
+ "[CMMediaSession][HeadsetActivity] Source entering walking."
+ "[CMMediaSession][HeadsetActivity] Source exiting pedestrian. Headset don't care. Case 5-3 and 5-4."
+ "[CMMediaSession][HeadsetActivity] Source exiting pedestrian. Headset don't care. Case 6-3 and 6-4."
+ "[CMMediaSession][HeadsetActivity] Source exiting static. Headset don't care. Case 1-3 and 1-4."
+ "[CMMediaSession][HeadsetActivity] Source exiting static. Headset don't care. Case 2-3 and 2-4."
+ "[CMMediaSession][HeadsetActivity] Source exiting static. Headset don't care. Case 3-3 and 3-4."
+ "[CMMediaSession][HeadsetActivity] Source exiting walking."
+ "[CMMediaSession][HeadsetActivity] Source exiting walking. Headset don't care. Case 4-3 and 4-4."
+ "[CMMediaSession][HeadsetActivity] Source exiting walking. Headset don't care. Case 7-3 and 7-4."
+ "[CMMediaSession][HeadsetActivity] Status encountered an error: %{public}@"
+ "[CMMediaSession][HeadsetActivity] Stopping headphone activity updates"
+ "[CMRelDMFwdPredictor] angular acceleration gain = [%{public}.1f, %{public}.1f, %{public}.1f]"
+ "[CMRelDMFwdPredictor] high angular acceleration variance detected: %{public}.2f"
+ "[CMRelDMFwdPredictor] prediction interval = %{public}.3f, requested interval = %{public}.3f"
+ "[CMRelDMFwdPredictor] suppress prediction = %{public}d"
+ "[HeadphoneUsage] Invalid BT AccessoryManager"
+ "[RelDMService][feedAnchor] Bypass anchor correspondence %d:"
+ "[RelDMService][feedAnchor] Number of faces:  %d:, overwrite anchor correspondence ?: %d"
+ "_accessoryMonitorDispatcher"
+ "_correspondenceThresholdDegrees"
+ "_deviceOrientationManager"
+ "_feedActiveAudioRouteChangedEvent"
+ "_filteredPressure"
+ "_headphoneActivityManager"
+ "_headphoneActivityQueue"
+ "_lastCAFwdPredictorError"
+ "_lastListenerOrientationGenerationTimestampSeconds"
+ "_lastPresentationTimestamp"
+ "_orientationCounter"
+ "_previousHeadphoneMotionActivityType"
+ "_renderingOverheadSeconds"
+ "_selectDeviceWithBTAddress:"
+ "averageTemperature"
+ "avgAnchorCorrectionAngleDeg"
+ "avgAnchorCorrectionPitchAngleDeg"
+ "avgAnchorCorrectionYawAngleDeg"
+ "avgAngleBetweenHeadRotationAxisAndGravity"
+ "avgAngleBetweenStemAndFaceY"
+ "avgAngleBetweenStemAndGravity"
+ "avgAngleFromDefaultHeadToHeadsetDeg"
+ "avgDistanceFromCamera"
+ "avgDistanceToCamera"
+ "avgFaceposeConfidence"
+ "avgFwdPredictorErrorDeg"
+ "avgHorizontalAngleInCameraFrame"
+ "avgPitchAngleInFaceFrame"
+ "avgRollAngleInFaceFrame"
+ "avgVerticalAngleInCameraFrame"
+ "avgYawAngleInFaceFrame"
+ "biasTemperature"
+ "bool CLAccessoryNotifier::getConfig(Config *)"
+ "bool CLAccessoryNotifier::setCustomProperty(uint8_t, const uint8_t *, size_t)"
+ "bool CLAudioAccessoryInterface::selectDeviceWithBTAddress(NSString *)"
+ "bool CLIoHidInterface::Device::createIOHIDDevice()"
+ "com.apple.CoreMotion.AudioAccessory.Temperatures"
+ "deltaAverageTemperature"
+ "deltaMaxTemperature"
+ "deltaMinTemperature"
+ "deltaVXYUnconditionalPlanarWithAudioThreshold"
+ "deltaVXYUnconditionalPlanarWithoutAudioThreshold"
+ "deltaVXYUnconditionalRolloverWithAudioThreshold"
+ "deltaVXYUnconditionalRolloverWithoutAudioThreshold"
+ "displayPoseState"
+ "fMagnetometerBiasEstimateVariance"
+ "fPresentationTimestamp"
+ "feedPoseAnchorWithAttitude:position:lidAngleDeg:numberOfDetectedFaces:timestampUs:"
+ "filteredPressure"
+ "float CMHeadToHeadsetAttitudeEstimator::getAngleBetweenEstimateAndDefault() const"
+ "getPinnedLocationAuthorizationState:"
+ "getPinnedLocationAuthorizationStateWithReplyBlock:"
+ "headsetActivityOtherDuration"
+ "headsetActivityPedestrianDuration"
+ "headsetActivityPedestrianWhenSessionSrcActivityPedestrian"
+ "headsetActivityRunningDuration"
+ "headsetActivityStationaryDuration"
+ "headsetActivityWalkingDuration"
+ "headsetActivityWalkingWhenSrcActivityWalking"
+ "i32@0:8r^{ListenerOrientation={CMOQuaternion=[4f]}{CMOQuaternion=[4f]}QQBB}16^@24"
+ "initWithAltitude:accuracy:precision:filteredPressure:status:timestamp:"
+ "isPitchStable"
+ "kCMAbsoluteAltitudeCodingKeyFilteredPressure"
+ "kCMDeviceMotionCodingKeyMagnetometerBiasEstimateVarianceX"
+ "kCMDeviceMotionCodingKeyMagnetometerBiasEstimateVarianceY"
+ "kCMDeviceMotionCodingKeyMagnetometerBiasEstimateVarianceZ"
+ "kCMPoseCodingKeyPresentationTimestamp"
+ "magnetometerBiasEstimateVariance"
+ "maxAnchorCorrectionAngleDeg"
+ "maxAnchorCorrectionPitchAngleDeg"
+ "maxAnchorCorrectionYawAngleDeg"
+ "maxDistanceToCamera"
+ "maxFaceposeConfidence"
+ "maxFwdPredictorErrorDeg"
+ "maxHorizontalAngleInCameraFrame"
+ "maxMean"
+ "maxNumberOfFaceDetectedDuringSession"
+ "maxPitchAngleInFaceFrame"
+ "maxRollAngleInFaceFrame"
+ "maxTemperature"
+ "maxVerticalAngleInCameraFrame"
+ "maxYawAngleInFaceFrame"
+ "meanN"
+ "minAnchorCorrectionAngleDeg"
+ "minAnchorCorrectionPitchAngleDeg"
+ "minAnchorCorrectionYawAngleDeg"
+ "minDistanceToCamera"
+ "minFaceposeConfidence"
+ "minFwdPredictorErrorDeg"
+ "minHorizontalAngleInCameraFrame"
+ "minMean"
+ "minPitchAngleInFaceFrame"
+ "minRollAngleInFaceFrame"
+ "minTemperature"
+ "minVerticalAngleInCameraFrame"
+ "minYawAngleInFaceFrame"
+ "mobilityCalibrationMessage"
+ "normalGammaCalibrationBin"
+ "numberOfBTZ"
+ "numberOfDetectedFaces"
+ "numberOfDeviceOrientationChange"
+ "percentHeadsetActivityOther"
+ "percentHeadsetActivityPedestrian"
+ "percentHeadsetActivityRunning"
+ "percentHeadsetActivityStationary"
+ "percentHeadsetActivityWalking"
+ "percentageOfActuallyRejectedAnchors"
+ "percentageOfCameraRequestMultipleFaceDetected"
+ "percentageOfCameraRequestNoFaceDetected"
+ "percentageOfHeadsetActivityPedestrianWhenSessionSrcActivityPedestrian"
+ "percentageOfHeadsetActivityWalkingWhenSrcActivityWalking"
+ "percentageOfPotentiallyRejectedAnchors"
+ "percentageOfSessionSrcActivityStationaryAndHeadsetActivityOtherMoving"
+ "percentageOfSessionSrcActivityStationaryAndHeadsetActivityPedestrian"
+ "percentageOfSessionSrcActivityStationaryAndHeadsetActivityStationary"
+ "percentageOfSrcActivityPedestrianWhenHeadsetActivityPedestrian"
+ "percentageOfSrcActivityWalkingWhenHeadsetActivityWalking"
+ "presentationTimestamp"
+ "productID"
+ "quaternionWithoutPrediction"
+ "rm_number_of_detected_faces"
+ "setAltitudeData:accuracy:precision:filteredPressure:status:"
+ "setPinnedLocationAuthorization:"
+ "setPinnedLocationAuthorization:replyBlock:"
+ "shouldStartStreamingDataToReceiver returned on streaming server connection %{private}p.%{private}p: %s"
+ "slowRollZgTimeThreshold"
+ "speedLB"
+ "speedUB"
+ "srcActivityPedestrianWhenHeadsetActivityPedestrian"
+ "srcActivityStationaryAndHeadsetActivityOtherMovingDuration"
+ "srcActivityStationaryAndHeadsetActivityPedestrianDuration"
+ "srcActivityStationaryAndHeadsetActivityStationaryDuration"
+ "srcActivityWalking"
+ "srcActivityWalkingWhenHeadsetActivityWalking"
+ "static void CLAccessoryNotifier::onServiceRemoval(void *)"
+ "uint16_t CLAudioAccessoryInterface::getAdaptiveLatencyJitterBufferLevel()"
+ "uint64_t CLAudioAccessoryInterface::getBTAddress() const"
+ "updateN"
+ "v120@0:8{?={?=dddd}{?=fff}{?=fff}{?=fff}iBBBfBBi}16{?=f{?=fff}}104"
+ "v24@0:8@?<v@?@\"NSError\"{CLLocationCoordinate2D=dd}B>16"
+ "v24@0:8^{Sample=d{?={?=dddd}{?=fff}{?=fff}{?=fff}iBBBfBBi}{?=f{?=fff}}BIC{Status=S}f}16"
+ "v24@0:8r^{Sample=d{?={?=dddd}{?=fff}{?=fff}{?=fff}iBBBfBBi}{?=f{?=fff}}BIC{Status=S}f}16"
+ "v24@?0@\"CMDeviceOrientation\"8@\"NSError\"16"
+ "v24@?0@\"CMMotionActivity\"8@\"NSError\"16"
+ "v28@0:8C16@?20"
+ "v28@0:8C16@?<v@?@\"NSError\">20"
+ "v36@0:8r^{Sample=d{?=dii{?=dddd}{?=fff}fffffI{?=fff}{?=fff}{?=fff}fIifi}}16^{?=fBBid}24f32"
+ "v36@?0@\"NSError\"8{CLLocationCoordinate2D=dd}16B32"
+ "v56@0:8d16d24d32d40q48"
+ "v76@0:8{?=dddd}16{CMVector<float, 3UL>=[3f]}48f60i64Q68"
+ "varianceN"
+ "virtual CFTimeInterval CLAccessoryMonitor::minimumUpdateIntervalChanged(int, const CFTimeInterval &)"
+ "virtual void CLAccessoryDeviceMotion::onAudioAccessoryInterfaceCallback(CLAudioAccessoryInterface::Event)"
+ "virtual void CLAccessoryMonitor::onEventData(void *, void *, IOHIDEventRef)"
+ "virtual void CLAccessoryMonitor::onServiceConnection()"
+ "virtual void CLAccessoryNotifier::onAudioAccessoryInterfaceCallback(CLAudioAccessoryInterface::Event)"
+ "void CLAccessoryMonitor::onMonitorEvent(const uint8_t *const, const size_t, const CFTimeInterval)"
+ "void CLAccessoryMonitor::onMonitorEvent(const uint8_t *const, const size_t, const CFTimeInterval)_block_invoke"
+ "void CLAudioAccessoryInterface::localDeviceEventHandler(BTLocalDeviceEvent)"
+ "void CLAudioAccessoryInterface::notifyClients(Event)"
+ "void CLAudioAccessoryInterface::subscribe(AudioAccessoryInterfaceCallback, void *)"
+ "void CLAudioAccessoryInterface::subscribe(AudioAccessoryInterfaceCallback, void *)_block_invoke"
+ "void CMAnchorMotionCorrespondence::anchorCorrespondence(const CMOQuaternion &, const uint64_t)"
+ "void CMAnchorMotionCorrespondence::setPoseResidualThreshold(float)"
+ "void CMAudioPerceptualFilter::feed(const CMVector3d &, const CMOQuaternion &, uint64_t, uint64_t)"
+ "void CMRelDMFwdPredictor::checkSuppressionConditions(const CMRelDM::IMUData &, const CMOQuaternion &, uint64_t)"
+ "void CMRelDMService::feedAnchor(const CMOQuaternion &, const CMVector3d &, float, int32_t, const uint64_t)"
+ "{\"msg%{public}.0s\":\"CLInternalGetPinnedLocationAuthorizationState\", \"event\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"CLInternalSetPinnedLocationAuthorization\", \"event\":%{public, location:escape_only}s}"
+ "{?=fff}16@0:8"
+ "{CAFwdPredictorError=\"timestamp\"Q\"errorRad\"f}"
- "#Warning Connection interrupted!"
- "#Warning Connection invalidated!"
- "#Warning Streaming connection interrupted!"
- "#Warning Streaming connection invalidated!"
- "%02x:%02x:%02x:%02x:%02x:%02x"
- "-[CMMediaSession feedPoseAnchorWithAttitude:position:lidAngleDeg:timestampUs:]"
- "16:38:16"
- "@104@0:8{?={?=dddd}{?=ddd}ddd}16d96"
- "@108@0:8{?={?=dddd}{?=fff}{?=fff}{?=fff}iBBBfBBi}16{?=f}104"
- "@116@0:8{?={?=dddd}{?=fff}{?=fff}{?=fff}iBBBfBBi}16{?=f}104d108"
- "@56@0:8d16d24d32q40d48"
- "@96@0:8{?={?=dddd}{?=ddd}ddd}16"
- "AbsoluteAltitude: %f, Accuracy: %f, Precision %f, statusInfo: %ld, timestamp :%f"
- "B24@0:8^{Sample=d{?={?=dddd}{?=fff}{?=fff}{?=fff}iBBBfBBi}{?=f}BIC{Status=S}f}16"
- "BTHeadphones%d,%d"
- "CMOQuaternion CMRelDMFwdPredictor::getPredictedRelAttitude(uint64_t &) const"
- "CMOQuaternion CMRelDMFwdPredictor::predictKinematics(const CFTimeInterval) const"
- "CMPose,q.x,%f,q.y,%f,q.z,%f,q.w,%f,translation.x,%f,translation.y,%f,translation.z,%f,consumedAuxTimestamp,%f,receivedAuxTimestamp,%f,machAbsTimestamp,%f,timestamp,%f"
- "CMRelDMFwdPredictor::OmegaState CMRelDMFwdPredictor::medianVector3d(const CMFixedSizeQueue<OmegaState, kQBufferLen - 1> &, const size_t) const"
- "Cancelling the streaming connection"
- "Error received on the streaming connection"
- "Fatal error"
- "History buffer is empty, can't predict"
- "Insufficient space allocated to copy string contents"
- "Jan 31 2025"
- "Streaming request sent"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Time interval between feeds is %{public}lf, max value is %{public}f"
- "Timestamp %{public}llu not long enough since previous %{public}llu. Skipping this sample."
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "[AccessoryDeviceMotion] Received unsupported event %{private}d from AudioAccessoryInterface"
- "[AccessoryNotifier] BT address of the active audio route : %{private}llx"
- "[AccessoryNotifier] Duplicate service with the same BT address %{private}llx for usage page %{public}d usage %{public}d"
- "[AccessoryNotifier] Failed to get an updated BT address"
- "[AccessoryNotifier] JBL is unavailable because BT accessory is not connected"
- "[AccessoryNotifier] Resetting active audio route"
- "[AccessoryNotifier] Selecting active audio route for BT Address %{private}@"
- "[AccessoryNotifier] The active audio route is AirPods (3rd generation)"
- "[AccessoryNotifier] The active audio route is AirPods Max"
- "[AccessoryNotifier] The active audio route is AirPods Pro"
- "[AccessoryNotifier] The active audio route is AirPods Pro (2nd generation)"
- "[AccessoryNotifier] The active audio route is B453"
- "[AccessoryNotifier] The active audio route is B768E"
- "[AccessoryNotifier] The active audio route is B768M"
- "[AccessoryNotifier] The active audio route is Beats Fit Pro"
- "[AccessoryNotifier] The active audio route is unknown"
- "[AccessoryNotifier] The current active route is identical to the requsting device %{private}@"
- "[AccessoryNotifier] Warning! Invalid input BT address %{private}@"
- "[AccessoryNotifier] Warning! Spatial Audio is not supported for BT address %{private}@ with modelID %{private}@"
- "[AccessoryNotifier] onNewHidService for service %{private}p. Updating BT address from %{private}llx to %{private}llx"
- "[AccessoryNotifier] selectActiveAudioRoute retry #%{public}d"
- "[CLAudioAccessoryInterface] BT address of the current device is %{private}s"
- "[CLAudioAccessoryInterface] BT_ACCESSORY_SETTINGS_CHANGED device:%{private}p"
- "[CLAudioAccessoryInterface] clear the BT address"
- "[CLAudioAccessoryInterface] in ear status - invalid BT address %{private}s"
- "[CLAudioAccessoryInterface] isSpatialAudioSupported - Failed to convert %{private}s into a valid BT address"
- "[CLAudioAccessoryInterface] isSpatialAudioSupported - Failed to get the device handle with BT address %{private}s"
- "[CLAudioAccessoryInterface] isSpatialAudioSupported - not supported for device %{private}s"
- "[CLAudioAccessoryInterface] refresh device handle - Failed to convert %{private}s into a valid BT address. Error: %{public}d"
- "[CLAudioAccessoryInterface] refresh device handle - Failed to get the device handle with BT address %{private}s. Error: %{public}d"
- "[CLAudioAccessoryInterface] refresh device handle - Failed to get the product ID. Error: %{public}d"
- "[CLAudioAccessoryInterface] refresh device handle - invalid BT address %{private}s"
- "[CLAudioAccessoryInterface] refresh device handle - invalid BT session"
- "[CLAudioAccessoryInterface] update TimeSync failed due to invalid BT address %{private}s"
- "[CMAnchorMotionCorrespondence] After pose update fPredictedRelativeAttitude %f %f %f %f."
- "[CMAnchorMotionCorrespondence] Anchor sensor states %d to %d."
- "[CMAnchorMotionCorrespondence] Before pose update fPredictedRelativeAttitude %f %f %f %f."
- "[CMAnchorMotionCorrespondence] dtSeconds %f, Anchor sensor state probably changed from 0 to %d."
- "[CMMediaSession] %{private}s"
- "[CMMediaSession] Failed to feed initial JBL value"
- "[CMMediaSession] Failed to feed initial JBL value, retrying in %{public}.1f sec"
- "[CMMediaSession] Initial JBL: %{public}d"
- "[CMMediaSession] Not starting jitterBufferLevelMonitor for clientMode %d"
- "[CMMediaSession] Start jitterBufferLevelMonitor because clientMode changed to %d"
- "[CMMediaSession] Stop jitterBufferLevelMonitor because clientMode changed to %d"
- "[CMMediaSession][Cam %{public}lu] Received %{public}lu faces"
- "[CMRelDMFwdPredictor] Index out of range of relative w buffer"
- "[CMRelDMFwdPredictor] dt is less than %{public}f."
- "[predictionIntervalMicrosecondsValue isKindOfClass:[NSNumber class]]"
- "_predictionIntervalMicroseconds"
- "_selectActiveAudioRouteForAccelerometerWithBTAddress:modelID:"
- "_selectActiveAudioRouteForGyroWithBTAddress:modelID:"
- "_selectActiveAudioRouteForHeartRateWithBTAddress:modelID:"
- "_selectActiveAudioRouteForMagnetometerWithBTAddress:modelID:"
- "_selectActiveAudioRouteForPPGWithBTAddress:modelID:"
- "_selectActiveAudioRouteWithBTAddress:modelID:"
- "_startedJitterBufferLevelPolling"
- "bool CLAccessoryNotifier::selectActiveAudioRoute(NSString *, NSString *)"
- "bool CLAccessoryNotifier::selectActiveAudioRoute(NSString *, NSString *)_block_invoke"
- "bool CLAudioAccessoryInterface::isSpatialAudioSupported(uint64_t) const"
- "const T &CMQueue<CMRelDMFwdPredictor::AttitudeState>::operator[](const size_t) const [T = CMRelDMFwdPredictor::AttitudeState]"
- "const T &CMQueue<CMRelDMFwdPredictor::OmegaState>::operator[](const size_t) const [T = CMRelDMFwdPredictor::OmegaState]"
- "feedPoseAnchorWithAttitude:position:lidAngleDeg:timestampUs:"
- "i32@0:8r^{ListenerOrientation={CMOQuaternion=[4f]}QQBB}16^@24"
- "initWithAltitude:accuracy:precision:status:timestamp:"
- "invalid Collection: less than 'count' elements in collection"
- "setAltitudeData:accuracy:precision:status:"
- "shouldStartStreamingDataToReceiver returned : %s"
- "uint16_t CLAccessoryNotifier::getAdaptiveLatencyJitterBufferLevel() const"
- "uint16_t CLAudioAccessoryInterface::getAdaptiveLatencyJitterBufferLevel() const"
- "v108@0:8{?={?=dddd}{?=fff}{?=fff}{?=fff}iBBBfBBi}16{?=f}104"
- "v24@0:8^{Sample=d{?={?=dddd}{?=fff}{?=fff}{?=fff}iBBBfBBi}{?=f}BIC{Status=S}f}16"
- "v24@0:8r^{Sample=d{?={?=dddd}{?=fff}{?=fff}{?=fff}iBBBfBBi}{?=f}BIC{Status=S}f}16"
- "v36@0:8r^{Sample=d{?=dii{?=dddd}{?=fff}fffffI{?=fff}{?=fff}{?=fff}fIif}}16^{?=fBBid}24f32"
- "v48@0:8d16d24d32q40"
- "v72@0:8{?=dddd}16{CMVector<float, 3UL>=[3f]}48f60Q64"
- "void CLAccessoryDeviceMotion::onAudioAccessoryInterfaceCallback(CLAudioAccessoryInterface::Event)"
- "void CLAudioAccessoryInterface::setBTAddress(uint64_t)"
- "void CMAnchorMotionCorrespondence::anchorCorrespondence(const CMOQuaternion &, const float)"
- "void CMAnchorMotionCorrespondence::propagatePredictedRelativeAttitude(const CMVector3d &, const CMVector3d &, double)"
- "void CMAudioPerceptualFilter::feed(const CMVector3d &, uint64_t, uint64_t)"
- "void CMRelDMFwdPredictor::feed(const CMOQuaternion &, const CMOQuaternion &, const uint64_t)"
- "void CMRelDMService::feedAnchor(const CMOQuaternion &, const CMVector3d &, float, const uint64_t)"

```
