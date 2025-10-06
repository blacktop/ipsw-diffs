## CoreMotionAlgorithms

> `/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms`

```diff

-2890.12.17.0.4
-  __TEXT.__text: 0x222408
-  __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_methlist: 0x688
-  __TEXT.__const: 0x49b2
-  __TEXT.__cstring: 0xfc1b
-  __TEXT.__gcc_except_tab: 0x3978
-  __TEXT.__oslogstring: 0x1b86
-  __TEXT.__unwind_info: 0x6d40
-  __TEXT.__eh_frame: 0x644
-  __TEXT.__objc_classname: 0x15a
-  __TEXT.__objc_methname: 0x1b97
-  __TEXT.__objc_methtype: 0x2566
-  __TEXT.__objc_stubs: 0x1100
+2890.16.16.0.0
+  __TEXT.__text: 0x23af68
+  __TEXT.__auth_stubs: 0xdb0
+  __TEXT.__objc_methlist: 0x968
+  __TEXT.__const: 0x4c12
+  __TEXT.__cstring: 0x101c9
+  __TEXT.__gcc_except_tab: 0x3f5c
+  __TEXT.__oslogstring: 0x5c24
+  __TEXT.__ustring: 0xce
+  __TEXT.__unwind_info: 0x72e4
+  __TEXT.__eh_frame: 0x6a8
+  __TEXT.__objc_classname: 0x194
+  __TEXT.__objc_methname: 0x2549
+  __TEXT.__objc_methtype: 0x2823
+  __TEXT.__objc_stubs: 0x1880
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x3e0
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__const: 0x708
+  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1000
-  __DATA_CONST.__objc_selrefs: 0x5c8
-  __DATA_CONST.__objc_classrefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__const: 0x9970
-  __AUTH_CONST.__cfstring: 0x3a0
-  __AUTH_CONST.__objc_const: 0x2d0
-  __AUTH_CONST.__auth_got: 0x680
-  __AUTH.__objc_data: 0x320
+  __DATA_CONST.__objc_const: 0x1450
+  __DATA_CONST.__objc_selrefs: 0x7e0
+  __DATA_CONST.__objc_classrefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0x20
+  __AUTH_CONST.__const: 0x9cc0
+  __AUTH_CONST.__cfstring: 0xa20
+  __AUTH_CONST.__objc_const: 0x360
+  __AUTH_CONST.__auth_got: 0x6e8
+  __AUTH.__objc_data: 0x3c0
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x134
-  __DATA.__data: 0x7a8
+  __DATA.__got_weak: 0x8
+  __DATA.__objc_ivar: 0x17c
+  __DATA.__data: 0x818
+  __DATA.__bss: 0x1488
   __DATA.__common: 0x110
-  __DATA.__bss: 0x13e8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F90294E1-8AC5-3B22-86D6-B32DACCB83D1
-  Functions: 9590
-  Symbols:   268
-  CStrings:  3700
+  UUID: 206842CE-04CF-3AAA-8F3F-9D65DC2B00F9
+  Functions: 9933
+  Symbols:   288
+  CStrings:  4047
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_CMAPencilFusion
+ _OBJC_CLASS_$_CMAPencilFusionResult
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_METACLASS_$_CMAPencilFusion
+ _OBJC_METACLASS_$_CMAPencilFusionResult
+ __Block_object_assign
+ __ZNKSt9exception4whatEv
+ __ZNSt9exceptionD2Ev
+ __ZTISt9exception
+ ___cxa_rethrow
+ _dispatch_assert_queue$V2
+ _fmodf
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_copyWeak
+ _objc_initWeak
+ _objc_moveWeak
+ _objc_retain
+ _objc_setProperty_nonatomic_copy
CStrings:
+ "!0"
+ "%0"
+ "%zu: alpha <= 0, matrix ! positive definite"
+ "'0"
+ "16@0:8"
+ "@\"NSDictionary\"8@?0"
+ "@\"NSMutableArray\""
+ "@\"NSUserDefaults\""
+ "@24@0:8^{_NSZone=}16"
+ "@?"
+ "@?16@0:8"
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 231,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 237,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 78,invalid col %zu > %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 232,invalid element %zu <= %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 238,invalid element %zu <= %zu."
+ "Assertion failed: i0 < N-Ni+1 && j0 < N-Nj+1, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 302,indices exceed factored matrix size."
+ "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 84,invalid element %zu >= %zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 77,invalid row %zu > %zu."
+ "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 186,invalid row %zu > %zu."
+ "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 191,invalid row %zu > %zu."
+ "Axis"
+ "B32@0:8@16@?24"
+ "CMAPencilFusion"
+ "CMAPencilFusionResult"
+ "ContactCondition"
+ "D(%zu) <= 0 non-positive definite matrix!"
+ "D[%zu] <= 0, matrix ! positive definite"
+ "F"
+ "Flushing MSL"
+ "MSLEnabled"
+ "MaxAuxToRingSensorLatency"
+ "MaxAzimuth"
+ "MaxDeltaGyroBias"
+ "MaxGyroBias"
+ "MaxGyroBiasTemperature"
+ "MaxGyroNorm"
+ "MaxGyroShaftAxisNorm"
+ "MaxGyroTemperature"
+ "MaxPencilIMUSamplePeriod"
+ "MaxRingSensorSamplePeriod"
+ "MaxSourceIMUSamplePeriod"
+ "MaxTilt"
+ "MaxTimeBetweenGyroBiasUpdates"
+ "MaxUserAccelNorm"
+ "MeanAuxToRingSensorLatency"
+ "MeanAzimuth"
+ "MeanDeltaGyroBias"
+ "MeanGyroBias"
+ "MeanGyroBiasTemperature"
+ "MeanGyroNorm"
+ "MeanGyroShaftAxisNorm"
+ "MeanGyroTemperature"
+ "MeanPencilIMUSamplePeriod"
+ "MeanRingSensorSamplePeriod"
+ "MeanSourceIMUSamplePeriod"
+ "MeanTilt"
+ "MeanTimeBetweenGyroBiasUpdates"
+ "MeanUserAccelNorm"
+ "MinAuxToRingSensorLatency"
+ "MinAzimuth"
+ "MinDeltaGyroBias"
+ "MinGyroBias"
+ "MinGyroBiasTemperature"
+ "MinGyroNorm"
+ "MinGyroShaftAxisNorm"
+ "MinGyroTemperature"
+ "MinPencilIMUSamplePeriod"
+ "MinRingSensorSamplePeriod"
+ "MinSourceIMUSamplePeriod"
+ "MinTilt"
+ "MinTimeBetweenGyroBiasUpdates"
+ "MinUserAccelNorm"
+ "Missing real angles for timestamp %{public}.3f"
+ "NSCopying"
+ "PencilFusion"
+ "PreciseTipPositionLoggingEnabled"
+ "Pulled estimated angles, %{public}@"
+ "Pushing real angles, %{public}@"
+ "Q"
+ "Q16@0:8"
+ "Received real angles for timestamp %{public}.3f without corresponding estimation"
+ "T,N,V_position"
+ "T@\"CMAPencilFusionResult\",R,N"
+ "T@\"NSMutableArray\",&,N,V_estimations"
+ "T@\"NSNumber\",N,V_estimationUpdateIndex"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_handlerQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSUserDefaults\",&,N,V_defaults"
+ "T@?,C,N,V_handler"
+ "TB,N,GisRunning,V_running"
+ "TB,N,V_estimated"
+ "TB,N,V_mslEnabled"
+ "TB,N,V_preciseTipPositionLoggingEnabled"
+ "TB,N,V_verboseLoggingEnabled"
+ "TQ,N,V_currentEstimationUpdateIndex"
+ "Tf,N,V_altitudeAngle"
+ "Tf,N,V_azimuthAngle"
+ "Tf,N,V_rollAngle"
+ "VerboseLoggingEnabled"
+ "[BarrelRoll]:[CMABarrelRollMEKF]:[checkNIS] Measurement rejected by NIS check.t: %.6f s, NIS score: %.6f,  NIS Threshold: %.6f, r: %.6f %.6f %.6f"
+ "[BarrelRoll]:[CMABarrelRollMEKF]:[propagate] Requested propagation time: %llu us cannot be 1s ahead of the last state timestamp: %llu us. Rejecting request."
+ "[BarrelRoll]:[CMABarrelRollMEKF]:[ringMeasurementUpdate] Measurement timestamp: %llu us must match the state timestamp: %llu us"
+ "[BarrelRoll]:[CMABarrelRollService] Created CMABarrelRollService."
+ "[BarrelRoll]:[CMABarrelRollService]:[checkSessionStarted] BarrelRoll session start timestamp: %{public}llu microseconds, initialized during no-trust: %{public}d, numRingSensor: %{public}zu, numAuxDM6: %{public}zu, numSrcDM6: %{public}zu, wAuxNorm: %{public}f dps, wSrcNorm: %{public}f dps"
+ "[BarrelRoll]:[CMABarrelRollService]:[checkSessionStarted] Time elapsed between first consumed ring sensor and first ring sensor: %{public}llu microseconds."
+ "[BarrelRoll]:[CMABarrelRollService]:[checkSessionStarted] Time elapsed between first consumed ring sensor and session start: %{public}llu microseconds."
+ "[BarrelRoll]:[CMABarrelRollService]:[informStartPencilFusionUpdates] Called hidStartedPencilFusionUpdates when the start flag was already true. Latest src timestamp: %{public}llu us, HID start timestamp: %{public}llu"
+ "[BarrelRoll]:[CMABarrelRollService]:[informStartPencilFusionUpdates] HID started pencil fusion updates.  Latest src timestamp: %{public}llu us, fTimeStampHIDStartedPencilFusionUpdates: %{public}llu"
+ "[BarrelRoll]:[CMABarrelRollService]:[informStopPencilFusionUpdates] Called hidStoppedPencilFusionUpdates when the start flag was already false. Latest src timestamp: %{public}llu us, HID start timestamp: %{public}llu, HID stop timestamp: %{public}llu ."
+ "[BarrelRoll]:[CMABarrelRollService]:[informStopPencilFusionUpdates] HID stopped pencil fusion updates. Session duration: %{public}.1f s. Latest src timestamp: %{public}llu us, HID start timestamp: %{public}llu, HID stop timestamp: %{public}llu ."
+ "[BarrelRoll]:[CMABarrelRollService]:[periodicSysDiagnoseLog] { timestamp: %{public}llu us, trackingStatus: %{public}d, sinceLastLog: %{public}llu us, fSessionStarted: %{public}d, HID started flag: %{public}d , HID start timestamp: %{public}llu us, durationSinceSessionStart: %{public}.1f s, durationSinceHIDStart: %{public}.1f s }, { initialized during no-trust: %{public}d, }, { Latest estimate: timestamp: %{public}llu us, Q_SP: %{public}.3f %{public}.3f %{public}.3f %{public}.3f, roll: %{public}.1f deg, azimuth: %{public}.1f deg, altitude: %{public}.1f deg } { Ring: avgNumSamplesPerSecond: %{public}u, over: %{public}.1f s, num samples: %{public}d, sample period min/max/avg: %{public}.1f/%{public}.1f/%{public}.1f ms }, { Src : avgNumSamplesPerSecond: %{public}u, over: %{public}.1f s, num samples: %{public}d, sample period min/max/avg: %{public}.1f/%{public}.1f/%{public}.1f ms }, { Aux : avgNumSamplesPerSecond: %{public}u, over: %{public}.1f s, num samples: %{public}d, sample period min/max/avg: %{public}.1f/%{public}.1f/%{public}.1f ms }, { Latest timestamp ring / src / aux: %{public}llu us / %{public}llu us/ %{public}llu us }, { Aux-to-Ring Delay: %{public}.1f ms, Aux-to-Src Delay: %{public}.1f ms  }"
+ "[BarrelRoll]:[CMABarrelRollService]:[reset] Reset CMABarrelRollService."
+ "[BarrelRoll]:[CMABarrelRollService]:[setTrackingStatus] Status changed from: %{public}d to %{public}d, timestamp: %{public}llu us ."
+ "[BarrelRoll]:[CMABarrelRollService]:[updateAuxDM] Aux DM6 timestamps must be monotonically increasing. Input: %{public}llu us, previous: %{public}llu us."
+ "[BarrelRoll]:[CMABarrelRollService]:[updateAuxDM] Received first aux DM6 input, timestamp: %{public}llu us, wNorm: %{public}.3f dps, q_p_ip: %{public}.3f %{public}.3f %{public}.3f %{public}.3f"
+ "[BarrelRoll]:[CMABarrelRollService]:[updateAuxDM] Reset due to large aux DM6 timestamp gap. Time gap:%{public}u us, timestamp: %{public}llu us."
+ "[BarrelRoll]:[CMABarrelRollService]:[updateAuxDM] Reset due to unexpected zero Aux DM6 timestamp. Input: %{public}llu us, previous: %{public}llu us."
+ "[BarrelRoll]:[CMABarrelRollService]:[updateRingSensor] Consumed first ring sensor input, timestamp: %{public}llu us, touching: %{public}d, altitude: %{public}.3f deg, azimuth: %{public}.3f deg, wAuxNorm: %{public}.3f dps, wSrcNorm: %{public}.3f dps, numAuxDM6:%{public}zu, numSrcDM6:%{public}zu, feedRing: %{public}d"
+ "[BarrelRoll]:[CMABarrelRollService]:[updateRingSensor] Received first ring sensor input, timestamp: %{public}llu us, touching: %{public}d, altitude: %{public}.3f deg, azimuth: %{public}.3f deg, wAuxNorm: %{public}.3f dps, wSrcNorm: %{public}.3f dps, numAuxDM6:%{public}zu, numSrcDM6:%{public}zu, feedRing: %{public}d"
+ "[BarrelRoll]:[CMABarrelRollService]:[updateRingSensor] Reset due to large ring sensor timestamp gap. Time gap:%{public}u us, timestamp: %{public}llu us."
+ "[BarrelRoll]:[CMABarrelRollService]:[updateRingSensor] Reset due to unexpected zero ring sensor timestamp. Input: %{public}llu us, previous: %{public}llu us."
+ "[BarrelRoll]:[CMABarrelRollService]:[updateRingSensor] Ring sensor timestamps must be monotonically increasing. Input: %{public}llu us, previous: %{public}llu us."
+ "[BarrelRoll]:[CMABarrelRollService]:[updateSrcDM] Received first src DM6 input, timestamp: %{public}llu us, wNorm: %{public}.3f dps, q_s_is: %{public}.3f %{public}.3f %{public}.3f %{public}.3f"
+ "[BarrelRoll]:[CMABarrelRollService]:[updateSrcDM] Reset due to large gap between the latest source and aux sample. Aux is too far in the past, likely due to a gap.Latest src timestamp: %{public}llu us, latest aux timestamp: %{public}llu us, latest ring sensor timestamp: %{public}llu us, src-to-aux-delta:%{public}u us, threshold:%{public}u us."
+ "[BarrelRoll]:[CMABarrelRollService]:[updateSrcDM] Reset due to large gap between the latest source and ring sample. Ring is too far in the past, likely due to pencil being away from screen.Latest src timestamp: %{public}llu us, latest ring sensor timestamp: %{public}llu us, latest aux timestamp: %{public}llu us, src-to-ring-delta:%{public}u us, threshold:%{public}u us."
+ "[BarrelRoll]:[CMABarrelRollService]:[updateSrcDM] Reset due to unexpected zero Src DM6 timestamp. Input: %{public}llu us, previous: %{public}llu us."
+ "[BarrelRoll]:[CMABarrelRollService]:[updateSrcDM] Src DM6 timestamps must be monotonically increasing. Input: %{public}llu us, previous: %{public}llu us."
+ "[BarrelRoll]:[CMABarrelRollSession]:[updateSrcDM] Reset due to large Src DM6 timestamp gap. Time gap:%{public}u us, timestamp: %{public}llu us."
+ "[BarrelRoll]:[CMABarrelRoll]:[checkPencilDM6InitAnomaly] Detected cold start init anomaly. deltaFromSessionStartSeconds: %{public}.3f s, rollDeltaWillAndDidUpdateRad: %{public}.3f deg"
+ "[BarrelRoll]:[CMABarrelRoll]:[checkPersistentCorrectedVsCurrentRollDelta] Detected persistent large difference between corrected vs. current roll estimate. Timestamp: %{public}llu us, sustained duration: %{public}llu us durationSinceLastCurrentUpdate: %{public}llu us, rollDelta: %{public}.3f deg"
+ "[BarrelRoll]:[CMABarrelRoll]:[feedAuxDM] AuxDM timestamp must be greater than the last value. Input: %llu us, last: %llu us"
+ "[BarrelRoll]:[CMABarrelRoll]:[feedAuxDM] Expected exact source vs aux timestamp, not finding one should not have been possible. fBufAuxDM6TimestampMicroSeconds.back(): %llu, fBufSrcDM6TimestampMicroSeconds[indSrc]: %llu, indSrc: %lu"
+ "[BarrelRoll]:[CMABarrelRoll]:[feedRingSensor] Received initial ring sensor timestamp : %llu"
+ "[BarrelRoll]:[CMABarrelRoll]:[feedRingSensor] Received ring sensor trust state=True after initializing during no-trust, reinitializing. Ring sensor timestamp: %llu"
+ "[BarrelRoll]:[CMABarrelRoll]:[feedRingSensor] Ring sensor timestamp must be greater than the last value. Input: %llu us, last: %llu us"
+ "[BarrelRoll]:[CMABarrelRoll]:[feedRingSensor] Setting fBlockInitializationDueToHighDynamicMotion to %{public}d, timestamp: %{public}llu us, avgOmegaAuxNorm: %{public}.3f dps, avgUserAccelAuxNorm: %{public}.3f g, avgOmegaSrcNorm: %{public}.3f dps, avgUserAccelSrcNorm: %{public}.3f g, timeElapsedMicroSeconds: %{public}u"
+ "[BarrelRoll]:[CMABarrelRoll]:[feedRingSensor] Setting fBoolInitDuringNoTrust=True, latest ring sensor timestamp: %llu"
+ "[BarrelRoll]:[CMABarrelRoll]:[feedSrcDM] Performed soft reset on the first hover-or-out opportunity. Timestamp: %{public}llu us, durationFromSessionStartSeconds: %{public}.3f s"
+ "[BarrelRoll]:[CMABarrelRoll]:[feedSrcDM] SrcDM timestamp must be greater than the last value. Input: %llu us, last: %llu us"
+ "[BarrelRoll]:[CMABarrelRoll]:[feedSrcDM] Will perform soft reset on the first hover-or-out opportunity. Timestamp: %{public}llu us, durationFromSessionStartSeconds: %{public}.3f s,  rollDeltaWillAndDidUpdateRad: %{public}.3f deg"
+ "[BarrelRoll]:[CMABarrelRoll]:[feedSrcDM] aux timestamp: %llu us does not match the src timestamp: %llu"
+ "[BarrelRoll]:[CMABarrelRoll]:[getPastMEKFUpdateIndices] Unexpected index delta.lastAuxInd: %zu, firstAuxInd: %zu, lastSrcInd: %zu, firstSrcInd: %zu"
+ "[BarrelRoll]:[CMABarrelRoll]:[getPastMEKFUpdateIndices] Unexpected index order.lastAuxInd: %zu, firstAuxInd: %zu, lastSrcInd: %zu, firstSrcInd: %zu"
+ "[BarrelRoll]:[CMABarrelRoll]:[getPastMEKFUpdateIndices] Unexpected timestamp mismatch.indSrc: %zu, src: %llu, indAux: %zu, aux: %llu"
+ "[BarrelRoll]:[CMABarrelRoll]:[registerCorrectedUpdateCallbackFn] Registered corrected update callback."
+ "[BarrelRoll]:[CMABarrelRoll]:[reset] Reset CMABarrelRoll. Stats before reset: fBoolInitDuringNoTrust: %d, initializedDMYawAlignment:%d, last src timestamp %llu us, num src samples: %zu, last aux timestamp %llu us, num aux samples: %zu, last ring timestamp %llu us, num ring samples: %zu, fCurrentEstimateTimeMicroSeconds: %llu"
+ "[BarrelRoll]:[CMABarrelRoll]:[updateCurrentEstimate] Initial roll angle recorded: %.1f deg, timestamp: %llu us"
+ "[BarrelRoll]:[CMABarrelRoll]:[updateCurrentEstimate] Timestamp mismatch error. Latest aux timestamp: %llu us, corresponding src timestamp: %llu us"
+ "[BarrelRoll]:[CMABarrelRoll]:[updateDMInertialYaw] DM yaw alignment state changed from: %d to %d, latest ring sensor timestamp: %llu"
+ "[BarrelRoll]:[CMABarrelRoll]:[updateDMInertialYaw] Initialized DM yaw alignment state, latest ring sensor timestamp: %llu"
+ "[BarrelRoll]:[CMAMEstimator1DConstant]:[add] Adding last sample. Number of added inputs: %lu, initial allocation: %lu."
+ "[BarrelRoll]:[CMAMEstimator1DConstant]:[add] Number of added inputs: %lu exceeded the initial allocation: %lu . Will NOT add this sample."
+ "[BarrelRoll]:[CMAMEstimator1DConstant]:[normal_solve] Information matrix: %f below min valid value: %f. Will not proceed with this solve step."
+ "[BarrelRoll]:[CMAMEstimator1DConstant]:[solve] Called solve before adding any constraints. Aborting and returning false."
+ "[BarrelRoll]:[CMAMEstimator1DConstant]:[solve] Ill conditioned. Exiting solver."
+ "[BarrelRoll]:[CMAPencilDMYawAlignmentManager]:[feedMEKF] Exit soft reset. fDMYawAlignmentQ_IP_IS.angle: %.1f deg, fDMYawAlignmentMEKF angle: %.1f deg, timestamp: %llu"
+ "[BarrelRoll]:[CMAPencilDMYawAlignmentManager]:[reset] Resetting. Values before reset: fBoolInitializedDMYawAlignment: %d, fFirstDMYawAlignmentUpdateTimeMicroSeconds: %llu us, fLatestDMYawAlignmentUpdateTimeMicroSeconds: %llu us, fDMYawAlignmentAngle: %.1f deg, fBoolTrustPencilRingSensor: %d"
+ "[BarrelRoll]:[CMAPencilDMYawAlignmentManager]:[softReset] Enter soft reset. fDMYawAlignmentQ_IP_IS.angle: %{public}.1f deg, fDMYawAlignmentMEKF angle: %{public}.1f deg, timestamp: %{public}llu"
+ "[BarrelRoll]:[CMAPencilDMYawAlignmentManager]:[updateDMInertialYaw] Initialized DM north alignment, t: %.6f s, angle: %.6f deg"
+ "[BarrelRoll]:[CMAPencilDMYawAlignmentManager]:[updateDMInertialYaw] Reset median buffer. Large delta between new angle and median: %.1f deg, new angle: %.1f deg, old median: %.1f deg, timestamp: %llu"
+ "[BarrelRoll]:[CMAPencilDMYawAlignmentManager]:[updateDMInertialYaw] Starting north alignment. fBoolInitializedDMYawAlignment: %d, numMatchedSensorData: %zu, numRingSensor: %zu, numAuxDM: %zu, numSrcDM: %zu, first/last ring timestamp entry in buffer: %llu %llu us"
+ "[BarrelRoll]:[CMAPencilDMYawAlignmentManager]:[updateDMInertialYaw] Updated DM north alignment, t: %.6f s, new angle: %.6f deg, median angle: %.6f deg"
+ "[BarrelRoll]:[CMAPencilDMYawAlignmentMeasurement]:[CMAPencilDMYawAlignmentMeasurement] Failed measurement covariance Cholesky decomposition. f_eY_IS_xy: %.6f %.6f, f_eY_IP_xy: %.6f %.6f, ringMeasCovRad2: %.6f %.6f"
+ "[BarrelRoll]:[CMAPencilDMYawAlignmentSolver]:[iterate] Accept (lambda = %.6f)"
+ "[BarrelRoll]:[CMAPencilDMYawAlignmentSolver]:[iterate] Converged!"
+ "[BarrelRoll]:[CMAPencilDMYawAlignmentSolver]:[iterate] Max rollbacks exceeded, exiting!"
+ "[BarrelRoll]:[CMAPencilDMYawAlignmentSolver]:[iterate] Reject iterate request before initialization."
+ "[BarrelRoll]:[CMAPencilDMYawAlignmentSolver]:[iterate] Rollback (lambda = %.6f)"
+ "[BarrelRoll]:[CMAPencilFusion] Logging pencil tip position in full input precision in accordance with the associated user defaults setting."
+ "[BarrelRoll]:[CMAPencilFusion] Logging pencil tip position in quantized  precision in accordance with the associated user defaults setting."
+ "[BarrelRoll]:[CMAPencilFusion] Setting preciseTipPositionLoggingEnabled to %d"
+ "[BarrelRoll]:[CMAPencilRingSensorTrustModel]:[setTrustPencilBool] Changed fTrustPencilRingSensorBool from %d to %d, t: %.6f s"
+ "_altitudeAngle"
+ "_azimuthAngle"
+ "_barrelRollService"
+ "_currentEstimationUpdateIndex"
+ "_defaults"
+ "_estimated"
+ "_estimationUpdateIndex"
+ "_estimations"
+ "_handler"
+ "_handlerQueue"
+ "_mslEnabled"
+ "_position"
+ "_preciseTipPositionLoggingEnabled"
+ "_queue"
+ "_rollAngle"
+ "_running"
+ "_verboseLoggingEnabled"
+ "addObject:"
+ "allocWithZone:"
+ "avgRelOmegaRps"
+ "com.apple.CoreMotionAlgorithms.PencilFusion"
+ "com.apple.PencilUseSessionGyroMetrics"
+ "com.apple.PencilUseSessionLatencyMetrics"
+ "com.apple.PencilUseSessionSensorMetrics"
+ "copyWithZone:"
+ "currentEstimation"
+ "currentEstimationUpdateIndex"
+ "defaults"
+ "description"
+ "dictionaryWithObjects:forKeys:count:"
+ "estimations"
+ "firstRingSensorTimeStampMicroSeconds"
+ "flushMSL"
+ "getBytes:length:"
+ "handler"
+ "handlerQueue"
+ "lastObject"
+ "length"
+ "logHostDeviceMotionQuaternion:rotationRate:acceleration:timestamp:"
+ "logPencilDeviceMotionQuaternion:rotationRate:acceleration:gyroBias:temperatureGyroBias:temperatureGyro:status:sensorTime:timestamp:"
+ "logPencilFusionResult:"
+ "logTouchAltitudeAngle:altitudeAngleConfidence:azimuthAngle:azimuthAngleConfidence:position:positionConfidence:timestamp:"
+ "medianBufferNumSamples"
+ "medianNorthAlignmentEstimateRad"
+ "mslEnabled"
+ "newNorthAlignmentEstimateRad"
+ "numRingSensorSamples"
+ "numberWithFloat:"
+ "numberWithInt:"
+ "numberWithUnsignedLongLong:"
+ "pencilFusionDMYawAlignmentUpdate"
+ "pencilFusionRingSensorTrustModelUpdate"
+ "preciseTipPositionLoggingEnabled"
+ "queue"
+ "readUserDefaults"
+ "real"
+ "removeAllObjects"
+ "removeObject:"
+ "removeObjectAtIndex:"
+ "removeObserver:forKeyPath:"
+ "ringSensorTrustModelMode"
+ "running"
+ "sendPencilGyroBiasAxisStatistics:axis:"
+ "sendPencilSensorContactTypeStatistics:contactType:"
+ "sendPencilStatistics"
+ "sendPencilTimingStatistics:"
+ "setAltitudeAngle:"
+ "setAzimuthAngle:"
+ "setCurrentEstimationUpdateIndex:"
+ "setDefaults:"
+ "setEstimated:"
+ "setEstimationUpdateIndex:"
+ "setEstimations:"
+ "setHandler:"
+ "setHandlerQueue:"
+ "setMslEnabled:"
+ "setPosition:"
+ "setPreciseTipPositionLoggingEnabled:"
+ "setQueue:"
+ "setRollAngle:"
+ "setRunning:"
+ "setVerboseLoggingEnabled:"
+ "startPencilFusionUpdatesToQueue:withHandler:"
+ "startUserDefaults"
+ "stopPencilFusionUpdates"
+ "stopUserDefaults"
+ "timeElapsedSinceLastUpdateMicroSeconds"
+ "trustPencilRingSensorBool"
+ "updateEstimationsWithRealValuesWithQuaternion angles:[%{public}.1f, %{public}.1f, %{public}.1f] timestamp:%{public}.3f"
+ "updateEstimationsWithRealValuesWithQuaternion:timestamp:"
+ "updateHostDeviceMotionQuaternion: packet size %{public}zd != expected %{public}zd"
+ "updateHostDeviceMotionQuaternion: unknown data type"
+ "updateHostDeviceMotionQuaternion: unknown packet report ID"
+ "updateHostDeviceMotionQuaternion:[%{public}f, %{public}f, %{public}f, %{public}f] rotationRate:[%{public}f, %{public}f, %{public}f]  acceleration:[%{public}f, %{public}f, %{public}f] timestamp:%{public}f"
+ "updateHostDeviceMotionQuaternion:rotationRate:acceleration:timestamp:"
+ "updatePencilDeviceMotionPayload:"
+ "updatePencilDeviceMotionPayload:[%{public}f, %{public}f, %{public}f, %{public}f] rotationRate:[%{public}f, %{public}f, %{public}f]  acceleration:[%{public}f, %{public}f, %{public}f] gyroBias:[%{public}f, %{public}f, %{public}f] temperatureGyroBias:%{public}f temperatureGyro:%{public}f status:0x%{public}.4x timestamp:%{public}llu timestamp:%{public}f"
+ "updateTouchAltitudeAngle:%{public}.1f altitudeAngleConfidence:%{public}.2f azimuthAngle:%{public}.1f azimuthAngleConfidence:%{public}.2f position:[%{public}.1f, %{public}.1f, %{public}.1f] positionConfidence:%{public}.2f timestamp:%{public}f"
+ "updateTouchAltitudeAngle:altitudeAngleConfidence:azimuthAngle:azimuthAngleConfidence:position:positionConfidence:timestamp:"
+ "v108@0:8{?=}16324864c80c84S88Q92d100"
+ "v112@0:8{CMAPencilTimingStatistics=QQQQQQQQQQQQ}16"
+ "v20@0:8f16"
+ "v24@0:8@?16"
+ "v32@0:816"
+ "v40@0:8{CMOQuaternion=[4f]}16d32"
+ "v60@0:8f16f20f24f2832f48d52"
+ "v72@0:8{?=}163248d64"
+ "v80@0:8{CMAPencilSensorContactTypeStatistics=fffffffffffffff}16i76"
+ "v92@0:8{CMAPencilGyroBiasAxisStatistics=ffffffffffffQQQ}16i88"
+ "verboseLoggingEnabled"
+ "verboseLoggingEnabled: %{public}d, mslEnabled: %{public}d"
+ "{unique_ptr<CMABarrelRoll::CMABarrelRollService, std::default_delete<CMABarrelRoll::CMABarrelRollService>>=\"__ptr_\"{__compressed_pair<CMABarrelRoll::CMABarrelRollService *, std::default_delete<CMABarrelRoll::CMABarrelRollService>>=\"__value_\"^{CMABarrelRollService}}}"

```
