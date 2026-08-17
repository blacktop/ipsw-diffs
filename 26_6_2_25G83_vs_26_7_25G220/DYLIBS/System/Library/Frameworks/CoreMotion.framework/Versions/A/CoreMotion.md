## CoreMotion

> `/System/Library/Frameworks/CoreMotion.framework/Versions/A/CoreMotion`

```diff

 3077.0.4.0.0
-  __TEXT.__text: 0x2f16e4
+  __TEXT.__text: 0x301520
   __TEXT.__auth_stubs: 0x2470
-  __TEXT.__objc_methlist: 0x9894
-  __TEXT.__const: 0x9030
+  __TEXT.__objc_methlist: 0x9cbc
+  __TEXT.__const: 0x9360
   __TEXT.__swift5_typeref: 0x257
   __TEXT.__swift5_reflstr: 0x2e
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__constg_swiftt: 0xb8
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__oslogstring: 0x20a44
-  __TEXT.__cstring: 0x36d72
+  __TEXT.__oslogstring: 0x2357f
+  __TEXT.__cstring: 0x37bd0
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__gcc_except_tab: 0x926c
-  __TEXT.__unwind_info: 0x90b0
+  __TEXT.__gcc_except_tab: 0x9970
+  __TEXT.__unwind_info: 0x9408
   __TEXT.__eh_frame: 0x150
-  __TEXT.__objc_classname: 0x13f9
-  __TEXT.__objc_methname: 0x156c9
-  __TEXT.__objc_methtype: 0x6e4d
-  __TEXT.__objc_stubs: 0xa4c0
-  __DATA_CONST.__got: 0x6a0
-  __DATA_CONST.__const: 0x1c78
-  __DATA_CONST.__objc_classlist: 0x688
+  __TEXT.__objc_classname: 0x145b
+  __TEXT.__objc_methname: 0x1655f
+  __TEXT.__objc_methtype: 0x7197
+  __TEXT.__objc_stubs: 0xa740
+  __DATA_CONST.__got: 0x6b0
+  __DATA_CONST.__const: 0x1cf0
+  __DATA_CONST.__objc_classlist: 0x6a8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ff0
+  __DATA_CONST.__objc_selrefs: 0x4170
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x5b0
+  __DATA_CONST.__objc_superrefs: 0x5d0
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x1250
-  __AUTH_CONST.__const: 0x12980
-  __AUTH_CONST.__cfstring: 0xf1a0
-  __AUTH_CONST.__objc_const: 0x15478
+  __AUTH_CONST.__const: 0x12dd0
+  __AUTH_CONST.__cfstring: 0xf600
+  __AUTH_CONST.__objc_const: 0x15e08
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x870
+  __AUTH.__objc_data: 0x9b0
   __AUTH.__data: 0x200
-  __DATA.__objc_ivar: 0x1110
-  __DATA.__data: 0xb50
-  __DATA.__common: 0xa0
+  __DATA.__objc_ivar: 0x11c0
+  __DATA.__data: 0xb70
+  __DATA.__common: 0xc0
   __DATA_DIRTY.__objc_ivar: 0x15c
   __DATA_DIRTY.__objc_data: 0x38e0
   __DATA_DIRTY.__data: 0x128
   __DATA_DIRTY.__common: 0x48
-  __DATA_DIRTY.__bss: 0xd90
+  __DATA_DIRTY.__bss: 0xe40
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9928
-  Symbols:   1568
-  CStrings:  12836
+  Functions: 10126
+  Symbols:   1577
+  CStrings:  13113
 
Symbols:
+ _CMAccessoryVLLocalizationResultKey
+ _CMAccessoryVLSCSessionStateKey
+ _OBJC_CLASS_$_CMAccessoryDMVLFusion
+ _OBJC_CLASS_$_CMAccessoryHeadingFusionImpl
+ _OBJC_CLASS_$_CMAccessoryVLLocalizationResult
+ _OBJC_METACLASS_$_CMAccessoryDMVLFusion
+ _OBJC_METACLASS_$_CMAccessoryHeadingFusionImpl
+ _OBJC_METACLASS_$_CMAccessoryVLLocalizationResult
+ _kCMAudioAccessoryManagerMotionAlarmTimestampKey
CStrings:
+ "%{public}s calling setDisplayAngleHandler:%{public}p interval:%{public}f"
+ "-[CMAccessoryDMVLFusion feedDeviceMotion6:timestamp:]_block_invoke"
+ "-[CMMediaSession _checkEKAnchorScreenType:]"
+ "-[CMMediaSession _disallowEKAnchoredTrackingForNonVideoClients:clientMode:]"
+ "-[CMMediaSession _feedEntityKitData:timestamp:]"
+ "-[CMMediaSession convertToEntityKitDataPoC:numberOfTotalDetectedObjects:timestampMicroSeconds:]"
+ "-[CMMotionManager setDisplayAngleHandler:interval:]"
+ "@\"CMAccessoryDMVLFusion\""
+ "@\"CMAccessoryHeadingFusionImpl\""
+ "@32@0:8{?=fB}16d24"
+ "AngularFenceExit"
+ "B790DemoAssumeFixedLatency"
+ "B790DemoAssumeRightBud"
+ "B790DemoDetectScreenTypeLaptop"
+ "B790DemoDetectScreenTypeMonitor"
+ "B790DemoDetectScreenTypeSmartphone"
+ "B790DemoDetectScreenTypeTV"
+ "B790DemoDetectScreenTypeTablet"
+ "B790DemoManuallyCorrectImageGravityAlignment"
+ "B790DemoMinValidConfidence"
+ "B790DemoUseP1"
+ "CLAccessoryMotionAlarms"
+ "CLHomeHubServiceNotifier"
+ "CLHomeHubServiceNotifier.mm"
+ "CMAccessoryDMVLFusion"
+ "CMAccessoryHeadingFusionImpl"
+ "CMAccessoryVLLocalizationResult"
+ "CMAccessoryVLSCSessionState"
+ "CMDisplayAngle"
+ "CMDisplayAngleService.mm"
+ "CMProcessEntityKitData::CMProcessEntityKitData()"
+ "CMProcessEntityKitData::EntityKitDataPoC CMProcessEntityKitData::getSelectedAnchorFromInputList(const std::vector<EntityKitDataPoC> &, const CMOQuaternion &)"
+ "CMProcessEntityKitData::ProcessedEKAnchor CMProcessEntityKitData::feedEntityKitAnchor(const std::vector<EntityKitDataPoC> &, const uint64_t, const CMOQuaternion, const CorrespondenceData &)"
+ "DisplayAngle"
+ "FenceExit"
+ "Moving"
+ "Sit2Stand"
+ "T,N,V_positionCameraInImu"
+ "T,N,V_rotationCameraToImu"
+ "T,N,V_rotationImuToImu"
+ "TB,R,D,N,G_isAudioAccessoryMotionAlarmsAvailable"
+ "TB,R,N,GisAngleStable,V_angleStable"
+ "TB,R,N,GisDisplayAngleAvailable"
+ "Td,D,N,S_setAudioAccessoryMotionAlarmsUpdateInterval:"
+ "Td,N,V_timestamp"
+ "Tf,N,V_headingAccuracy"
+ "Tf,N,V_headingOffset"
+ "Tf,N,V_referenceFrameDeltaYawFromArbitraryToTrueNorth"
+ "Tf,R,N,V_angleDegrees"
+ "Ti,N,V_sensorLocation"
+ "Timestamp"
+ "T{?=[4]},N,V_transform"
+ "T{?=[6[6f]]},N,V_covariance"
+ "WakeGesture"
+ "[AccessoryMotionAlarms] Invalid payload"
+ "[AccessoryMotionAlarms] Moving,%{public}@,sensorTime,%{public}llu"
+ "[AccessoryMotionAlarms] Reconfig timer started"
+ "[AccessoryMotionAlarms] Reconfig timer stopped"
+ "[AccessoryMotionAlarms] Reconfiguring alarms"
+ "[AccessoryMotionAlarms] Setting update interval to %{public}f"
+ "[AccessoryMotionAlarms] Skipping reconfig since update interval is 0"
+ "[AccessoryMotionAlarms] Unrecognized update interval notification %{public}d"
+ "[AccessoryMotionAlarms] config AngularFenceExitAlarm, angleThreshold %{public}f, repeated %{public}u"
+ "[AccessoryMotionAlarms] config FenceExitAlarm, radius %{public}f, repeated %{public}u"
+ "[AccessoryMotionAlarms] config MovingAlarm, timeout %{public}u, repeated %{public}u"
+ "[AccessoryMotionAlarms] config Sit2StandAlarm, timeout %{public}u, repeated %{public}u"
+ "[AccessoryMotionAlarms] configAngularFenceExitAlarm failed"
+ "[AccessoryMotionAlarms] configFenceExitAlarm failed"
+ "[AccessoryMotionAlarms] configMovingAlarm failed"
+ "[AccessoryMotionAlarms] configSit2StandAlarm failed"
+ "[AccessoryMotionAlarms] payload,{%{private}.*P}"
+ "[CLHomeHubServiceNotifier] %{public}s : Bump detected, timestamp=%{public}lf, now=%{public}lf"
+ "[CLHomeHubServiceNotifier] %{public}s : angle=%{public}f, isAngleStable=%{public}d, timestamp=%{public}lf, now=%{public}lf"
+ "[CLHomeHubServiceNotifier] Bad report,type,%{public}d,size,%{public}lu"
+ "[CLHomeHubServiceNotifier] Empty payload, returning"
+ "[CLHomeHubServiceNotifier] Event ref invalid"
+ "[CLHomeHubServiceNotifier] Failed to send EnableBumpEvents command"
+ "[CLHomeHubServiceNotifier] Failed to send EnableDisplayAngle command"
+ "[CMAccessoryDMVLFusion] feedDeviceMotion6"
+ "[CMAccessoryHeadingFusion]  Timestamp is in the future, timestamp, %llu, previousTimestamp, %llu"
+ "[CMAccessoryHeadingFusion] DM heading: %f"
+ "[CMMediaSession] Ignoring tracking scheme choice kEKAnchored due to connected external displays, number of displays:  %{public}d. Falling back to kIMUOnly."
+ "[CMMediaSession] Update _primaryBudSide from:%{public}d to %{public}d"
+ "[CMMediaSession][CMProcessEntityKitData][EntityKit] Available N: %zu bounding boxes from EK, timestamp: %{public}.6f, _scheme: %{public}d"
+ "[CMMediaSession][CMProcessEntityKitData][EntityKit] CMMediaSession received information for %d bounding boxes from EK, budSide: %{public}d, primaryBudSide: %{public}d, timestamp: %{public}.6f"
+ "[CMMediaSession][CMProcessEntityKitData][EntityKit] CMMediaSession received information for %d bounding boxes from EK, timestamp: %{public}.6f, _scheme: %d"
+ "[CMMediaSession][CMProcessEntityKitData][EntityKit] Saved EntityKit anchor to MSL."
+ "[CMMediaSession][EntityKit] Disallow kEKAnchored for non-kVideo clients: %{public}d"
+ "[CMMediaSession][EntityKit] Error -- Default H2H transformation for model %{public}d to B788 values for B790, defaultHeadsetOrientation: %{public}.6f %{public}.6f %{public}.6f %{public}.6f"
+ "[CMMediaSession][EntityKit][DEMO] EK anchor related options: _B790DemoUseP1: %{public}d, _B790DemoAssumeRightBud: %{public}d, _B790DemoAssumeFixedLatency: %{public}d, _B790DemoManuallyCorrectImageGravityAlignment: %{public}d, _B790DemoDetectScreenType Laptop: %{public}d Monitor: %{public}d, Smartphone: %{public}d, Tablet: %{public}d, TV: %{public}d ."
+ "[CMMediaSession][_feedEntityKitData][EntityKit] Anchor latency: %{public}.3f ms, anchorTimestampMicroSeconds: %{public}llu, mach continuous vs. absolute offset: %{public}d"
+ "[CMMediaSession][_feedEntityKitData][EntityKit] Backwards timestamp, ignoring input. _lastEKAnchorGTBTimestampUs: %{public}llu, detection confidence: %{public}.3f, class: %{public}d, timestampMicroSeconds: %{public}llu, gtbTimestampUS: %{public}llu."
+ "[CMMediaSession][_feedEntityKitData][EntityKit] CMMediaSession _primaryBudSide is not set. Ignoring anchor. Timestamp: %{public}.6f"
+ "[CMMediaSession][_feedEntityKitData][EntityKit] CMMediaSession is set to assume Right bud, but active bud side differs. Ignoring anchor. Timestamp: %{public}.6f"
+ "[CMMediaSession][_feedEntityKitData][EntityKit] Reached the max %d num inputs limit, ignoring input. _lastEKAnchorGTBTimestampUs: %{public}llu, detection confidence: %{public}.3f, class: %{public}d, timestampMicroSeconds: %{public}llu, gtbTimestampUS: %{public}llu."
+ "[CMMediaSession][convertToEntityKitDataPoC][EntityKit] Warning: Mismatch between originalBudSide: %{public}u and budSide: %{public}u , _B790DemoAssumeRightBud: %{public}d, timestamp: %{public}llu"
+ "[CMProcessEntityKitData][EntityKit] Called feedEntityKitAnchor with input list of %{public}zu items, q_bf: %{public}.3f %{public}.3f %{public}.3f %{public}.3f timestamp: %{public}llu."
+ "[CMProcessEntityKitData][EntityKit] Change fUseP1 from: %d to: %d."
+ "[CMProcessEntityKitData][EntityKit] Constructed CMProcessEntityKitData."
+ "[CMProcessEntityKitData][EntityKit] Correspondence FSM state reset to waiting for first valid anchor due to motion, timestamp: %{public}llu"
+ "[CMProcessEntityKitData][EntityKit] Correspondence logic motion state changed from %{public}d to %{public}d, timestamp: %{public}llu, srcInMovingState: %{public}d, recentPedestrian: %{public}d, recentSitStand: %{public}d, isSrcMoving: %{public}d"
+ "[CMProcessEntityKitData][EntityKit] CorrespondenceFSMState was kWaitingFirstAnchor, selected ind: %{public}u from %{public}zu anchors using min yaw criteria."
+ "[CMProcessEntityKitData][EntityKit] Detected primary bud side changed from: %{public}u to: %{public}u since last valid anchor, timestamp: %{public}llu"
+ "[CMProcessEntityKitData][EntityKit] Initialized based on looking at screen on start. "
+ "[CMProcessEntityKitData][EntityKit] ProcessedEKAnchor: detectionConfidence: %{public}.3f, class: %{public}d, timestampMicroSeconds: %{public}llu, gtbTimestampUS: %{public}llu, numberOfTotalDetectedObjects: %{public}d, expected vs received boresight: %{public}.1f deg"
+ "[CMProcessEntityKitData][EntityKit] Received first EK anchor, timestamp: %{public}llu"
+ "[CMProcessEntityKitData][EntityKit] Received new EK anchor, time elapsed since last anchor: %{public}.2f s, timestamp: %{public}llu"
+ "[CMProcessEntityKitData][EntityKit] Reject EK anchor due to backwards timestamp. Last timestamp:%{public}llu, new timestamp: %{public}llu, detectionConfidence: %{public}.3f, class: %{public}d, gtbTimestampUS: %{public}llu"
+ "[CMProcessEntityKitData][EntityKit] Reject EK anchor due to invalid bud side value that is set to kUnknownBudSide. detectionConfidence: %{public}.3f, class: %{public}d, timestampMicroSeconds: %{public}llu, gtbTimestampUS: %{public}llu"
+ "[CMProcessEntityKitData][EntityKit] Reject EK anchor due to low detection confidence: %{public}.3f, threshold:%{public}.3f, class: %{public}d, timestampMicroSeconds: %{public}llu, gtbTimestampUS: %{public}llu"
+ "[CMProcessEntityKitData][EntityKit] Selected ind: %{public}u from %{public}zu anchors using findIndexWithBestFitToLastAnchor."
+ "[CMProcessEntityKitData][EntityKit] Set looking at screen on start values."
+ "[CMProcessEntityKitData][EntityKit] fManuallyCorrectImageGravityAlignment changed from: %{public}d to: %{public}d."
+ "[CMProcessEntityKitData][EntityKit] fMinValidConfidence changed from: %.3f to %.3f"
+ "[CMProcessEntityKitData][EntityKit] feedEntityKitAnchor returns False due to correspondence logic motion level."
+ "[CMProcessEntityKitData][EntityKit] feedEntityKitAnchor returns False due to empty input anchors list."
+ "[CMProcessEntityKitData][EntityKit] feedEntityKitAnchor returns False due to not being able to find a selected anchor with the chosen criteria."
+ "[CMProcessEntityKitData][EntityKit] feedEntityKitAnchor returns False due to unexpected backwards timestamp, previous: %{public}llu, new: %{public}llu"
+ "[CMProcessEntityKitData][EntityKit] feedEntityKitAnchor returns False due to unexpectedly large number of entries:%{public}zu in the input list."
+ "[CMProcessEntityKitData][EntityKit] feedEntityKitAnchor returns False due to zero screened input anchors left."
+ "[CMProcessEntityKitData][EntityKit] updateHeadsetActivityPedestrian , timestamp: %{public}llu"
+ "[CMProcessEntityKitData][EntityKit] useP1: %d value is the same as current fUseP1. No change."
+ "[CMRelDMSensorFusionMekf][entityKitAnchorMeasurementUpdate][EntityKit] Converged to anchor, fLastConvergedToAnchorTimestamp: %{public}llu, timestamp: %{public}llu."
+ "[CMRelDMSensorFusionMekf][entityKitAnchorMeasurementUpdate][EntityKit] NOT-Converged to anchor, fLastConvergedToAnchorTimestamp: %{public}llu, timestamp: %{public}llu."
+ "[CMRelDMSensorFusionMekf][entityKitAnchorMeasurementUpdate][EntityKit] Updated EKF state via EntityKit, timestamp: %{public}llu."
+ "[CMRelDMSensorFusionMekf][feedEntityKitAnchor][EntityKit] Consumed EK Anchor. anchorTime=%{public}llu"
+ "[CMRelDMSensorFusionMekf][feedEntityKitAnchor][EntityKit] Failed hasValidStateAtAnchorTime, anchor rejected. anchorTime=%{public}llu"
+ "[CMRelDMSensorFusionMekf][feedEntityKitAnchor][EntityKit] Initialize with anchor. anchorTime=%{public}llu"
+ "[RelDMService][EntityKit] Detected extend BTZ due to EK anchor."
+ "[RelDMService][EntityKit] FaceKit anchor is ignored since tracking scheme is kEKAnchored. Timestamp: %{public}llu ."
+ "[RelDMService][feedEntityKitAnchor][EntityKit] Anchor data is far ahead of IMU: anchor, %{public}llu, auxIMU, %{public}llu"
+ "[RelDMService][feedEntityKitAnchor][EntityKit] Anchor is ignored due to uncorrelated src motion, timestamp: %{public}llu"
+ "[RelDMService][feedEntityKitAnchor][EntityKit] Correspondence check: Extend BTZ and do NOT consume anchor due to large delta between expected vs received boresight: %{public}.1f deg"
+ "[RelDMService][feedEntityKitAnchor][EntityKit] Entering 2-IMU with EK anchored tracking."
+ "[RelDMService][feedEntityKitAnchor][EntityKit] Failed correspondence check due to large delta between expected vs received boresight: %{public}.1f deg, auxAvgOmegaShort: %{public}.2f dps,  auxAvgOmegaLong: %{public}.2f dps, auxMovingDuration: %{public}.1f s, canExtendBTZ: %{public}d"
+ "[RelDMService][feedEntityKitAnchor][EntityKit] Processing valid EK anchor, detectionConfidence: %{public}.3f, class: %{public}d, timestampMicroSeconds: %{public}llu, gtbTimestampUS: %{public}llu"
+ "[RelDMService][feedEntityKitAnchor][EntityKit] Tracking will be re-enabled from receiving EntityKit anchor."
+ "[RelDMService][feedEntityKitAnchor][EntityKit] anchor is NOT-VALID, timestamp: %llu"
+ "[RelDMService][feedEntityKitAnchor][EntityKit] anchor is VALID, timestamp: %llu"
+ "[RelDMService][feedEntityKitAnchor][EntityKit] fBodyFace is not set, anchor IGNORED, timestamp: %{public}llu"
+ "[RelDMService][feedEntityKitAnchor][EntityKit] tracking scheme:%d is not kEKAnchored, anchor IGNORED, timestamp: %{public}llu"
+ "[RelativeDeviceMotion][CMProcessEntityKitData][EntityKit] Ignoring EK anchor due to unexpected detection class, detection confidence: %{public}.3f, class: %{public}d, timestampMicroSeconds: %{public}llu, gtbTimestampUS: %{public}llu."
+ "[RelativeDeviceMotion][CMProcessEntityKitData][EntityKit] Processing EK anchor detection confidence: %{public}.3f, class: %{public}d, timestampMicroSeconds: %{public}llu, gtbTimestampUS: %{public}llu."
+ "[RelativeDeviceMotion][CMProcessEntityKitData][EntityKit] Unexpected detection class: %{public}d"
+ "_B790DemoAssumeFixedLatency"
+ "_B790DemoAssumeRightBud"
+ "_B790DemoDetectScreenTypeLaptop"
+ "_B790DemoDetectScreenTypeMonitor"
+ "_B790DemoDetectScreenTypeSmartphone"
+ "_B790DemoDetectScreenTypeTV"
+ "_B790DemoDetectScreenTypeTablet"
+ "_B790DemoManuallyCorrectImageGravityAlignment"
+ "_B790DemoUseP1"
+ "_angleDegrees"
+ "_angleStable"
+ "_audioAccessoryMotionAlarmsAvailable"
+ "_audioAccessoryMotionAlarmsUpdateInterval"
+ "_checkEKAnchorScreenType:"
+ "_covariance"
+ "_disallowEKAnchoredTrackingForNonVideoClients:clientMode:"
+ "_ekAnchorInputsList"
+ "_feedEntityKitData:timestamp:"
+ "_headingAccuracy"
+ "_headingOffset"
+ "_impl"
+ "_isAudioAccessoryMotionAlarmsAvailable"
+ "_isAudioAccessoryMotionAlarmsAvailablePrivate"
+ "_lastEKAnchorGTBTimestampUs"
+ "_positionCameraInImu"
+ "_primaryBudSide"
+ "_rotationCameraToImu"
+ "_rotationImuToImu"
+ "_sensorLocation"
+ "_setAudioAccessoryMotionAlarmsUpdateInterval:"
+ "_setAudioAccessoryMotionAlarmsUpdateIntervalPrivate:"
+ "_shouldStopMotionAlarms"
+ "_startAudioAccessoryMotionAlarmsAngularFenceExitAlarmUpdatesPrivateToQueue:withAngleThreshold:withRepeat:withHandler:"
+ "_startAudioAccessoryMotionAlarmsAngularFenceExitAlarmUpdatesToQueue:withAngleThreshold:withRepeat:withHandler:"
+ "_startAudioAccessoryMotionAlarmsFenceExitAlarmUpdatesPrivateToQueue:withRadius:withRepeat:withHandler:"
+ "_startAudioAccessoryMotionAlarmsFenceExitAlarmUpdatesToQueue:withRadius:withRepeat:withHandler:"
+ "_startAudioAccessoryMotionAlarmsMovingAlarmUpdatesPrivateToQueue:withTimeout:withRepeat:withHandler:"
+ "_startAudioAccessoryMotionAlarmsMovingAlarmUpdatesToQueue:withTimeout:withRepeat:withHandler:"
+ "_startAudioAccessoryMotionAlarmsSit2StandAlarmUpdatesPrivateToQueue:withTimeout:withRepeat:withHandler:"
+ "_startAudioAccessoryMotionAlarmsSit2StandAlarmUpdatesToQueue:withTimeout:withRepeat:withHandler:"
+ "_stopAudioAccessoryMotionAlarmsAngularFenceExitAlarmUpdates"
+ "_stopAudioAccessoryMotionAlarmsAngularFenceExitAlarmUpdatesPrivate"
+ "_stopAudioAccessoryMotionAlarmsFenceExitAlarmUpdates"
+ "_stopAudioAccessoryMotionAlarmsFenceExitAlarmUpdatesPrivate"
+ "_stopAudioAccessoryMotionAlarmsMovingAlarmUpdates"
+ "_stopAudioAccessoryMotionAlarmsMovingAlarmUpdatesPrivate"
+ "_stopAudioAccessoryMotionAlarmsSit2StandAlarmUpdates"
+ "_stopAudioAccessoryMotionAlarmsSit2StandAlarmUpdatesPrivate"
+ "_transform"
+ "angle %f, isStable: %d @ %f"
+ "angleDegrees"
+ "angleStable"
+ "com.apple.CoreMotion.CMAccessoryDMVLFusion"
+ "convertToEntityKitDataPoC:numberOfTotalDetectedObjects:timestampMicroSeconds:"
+ "displayAngleAvailable"
+ "fAccessoryDMVLFusion"
+ "fAudioAccessoryMotionAlarmsAngularFenceExitAlarmHandler"
+ "fAudioAccessoryMotionAlarmsAngularFenceExitAlarmQueue"
+ "fAudioAccessoryMotionAlarmsAvailable"
+ "fAudioAccessoryMotionAlarmsDispatcher"
+ "fAudioAccessoryMotionAlarmsFenceExitAlarmHandler"
+ "fAudioAccessoryMotionAlarmsFenceExitAlarmQueue"
+ "fAudioAccessoryMotionAlarmsMovingAlarmHandler"
+ "fAudioAccessoryMotionAlarmsMovingAlarmQueue"
+ "fAudioAccessoryMotionAlarmsSit2StandAlarmHandler"
+ "fAudioAccessoryMotionAlarmsSit2StandAlarmQueue"
+ "fAudioAccessoryMotionAlarmsUpdateInterval"
+ "fDisplayAngleService"
+ "fHidDriverInterface"
+ "feedDeviceMotion6:timestamp:"
+ "headingOffset"
+ "initWithDisplayAngle:timestamp:"
+ "isAngleStable"
+ "isDisplayAngleAvailable"
+ "onAudioAccessoryMotionAlarms:"
+ "onDisplayAngleChange"
+ "onIoHidEventBounce"
+ "positionCameraInImu"
+ "reConfigure"
+ "reopenHIDDriverInterface"
+ "reset"
+ "rotationCameraToImu"
+ "rotationImuToImu"
+ "setCovariance:"
+ "setDisplayAngleHandler:interval:"
+ "setHeadingAccuracy:"
+ "setHeadingOffset:"
+ "setPositionCameraInImu:"
+ "setRotationCameraToImu:"
+ "setRotationImuToImu:"
+ "setSensorLocation:"
+ "setTransform:"
+ "target"
+ "timestamp: %.2f, sensorLocation: %d, confidence: %.2f, transform:\n  [%f, %f, %f, %f]\n  [%f, %f, %f, %f]\n  [%f, %f, %f, %f]\n  [%f, %f, %f, %f]"
+ "v144@0:8{?=[4]}16"
+ "v160@0:8{?=[6[6f]]}16"
+ "v24@0:8r^{MotionAlarmReport=CQId}16"
+ "v32@0:8r^{?={?=dddd}{?=fff}{?=fff}{?=fff}iBBBfBBi}16d24"
+ "v44@0:8@16@24B32@?36"
+ "v48@0:816"
+ "virtual CFTimeInterval CLAccessoryMotionAlarms::minimumUpdateIntervalChanged(int, const CFTimeInterval &)"
+ "virtual void CLAccessoryMotionAlarms::onEventData(void *, void *, IOHIDEventRef)"
+ "virtual void CLHomeHubServiceNotifier::visitBumpEvent(const CMHomeHubReport::BumpEvent &)"
+ "virtual void CLHomeHubServiceNotifier::visitDisplayAngleState(const DisplayAngleState &)"
+ "void CLAccessoryMotionAlarms::configAngularFenceExitAlarm(const float, const bool)"
+ "void CLAccessoryMotionAlarms::configFenceExitAlarm(float, bool)"
+ "void CLAccessoryMotionAlarms::configMovingAlarm(uint32_t, bool)"
+ "void CLAccessoryMotionAlarms::configSit2StandAlarm(uint32_t, bool)"
+ "void CLAccessoryMotionAlarms::reconfigAlarms()"
+ "void CLAccessoryMotionAlarms::startReconfigTimer()"
+ "void CLAccessoryMotionAlarms::stopReconfigTimer()"
+ "void CLHomeHubServiceNotifier::onIoHidEvent(IOHIDEventRef)"
+ "void CLHomeHubServiceNotifier::setBumpEventsEnabled(bool)"
+ "void CLHomeHubServiceNotifier::setDisplayAngleEnabled(bool)"
+ "void CMAccessoryHeadingFusion::feedDeviceMotionAttitude(const CMOQuaternion &, uint64_t, uint8_t)"
+ "void CMProcessEntityKitData::initEKAnchorCorrespondenceValues(uint64_t, const CMOQuaternion &, const CMOQuaternion &)"
+ "void CMProcessEntityKitData::screenEKAnchorInputsList(const std::vector<EntityKitDataPoC> &)"
+ "void CMProcessEntityKitData::setMinValidConfidence(const float)"
+ "void CMProcessEntityKitData::setUseP1(const bool)"
+ "void CMProcessEntityKitData::updateHeadsetActivityPedestrian(const uint64_t)"
+ "void CMProcessEntityKitData::updateManuallyCorrectImageGravityAlignment(const bool)"
+ "void CMProcessEntityKitData::updateMotionLevel()"
+ "void CMRelDMSensorFusionMekf::entityKitAnchorMeasurementUpdate(const State &, const AnchorData &, bool, uint64_t)"
+ "void CMRelDMSensorFusionMekf::feedEntityKitAnchor(const CMVector3d &, const CMVector3d &, const float, const uint64_t)"
+ "void CMRelDMService::feedEntityKitAnchor(const std::vector<CMProcessEntityKitData::EntityKitDataPoC> &, uint64_t)"
+ "{?=\"columns\"[4]}"
+ "{?=\"v\"[6[6f]]}"
+ "{?=[4]}16@0:8"
+ "{?=[6[6f]]}16@0:8"
+ "{EntityKitDataPoC=fffffiiiQQI{CMOQuaternion=[4f]}{CMVector<float, 3UL>=[3f]}}36@0:8@16I24Q28"
+ "{unique_ptr<CMAccessoryHeadingFusion, std::default_delete<CMAccessoryHeadingFusion>>=\"\"{?=\"__ptr_\"^{CMAccessoryHeadingFusion}}}"
+ "{unique_ptr<CMDisplayAngleService, std::default_delete<CMDisplayAngleService>>=\"\"{?=\"__ptr_\"^{CMDisplayAngleService}}}"
+ "{vector<CMProcessEntityKitData::EntityKitDataPoC, std::allocator<CMProcessEntityKitData::EntityKitDataPoC>>=\"__begin_\"^{EntityKitDataPoC}\"__end_\"^{EntityKitDataPoC}\"\"{?=\"__cap_\"^{EntityKitDataPoC}}}"
```
