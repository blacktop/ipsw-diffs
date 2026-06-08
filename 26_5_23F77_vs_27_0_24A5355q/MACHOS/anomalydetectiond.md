## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-152.0.2.0.0
-  __TEXT.__text: 0x34fb64
-  __TEXT.__auth_stubs: 0x16a0
+163.0.0.0.0
+  __TEXT.__text: 0x36a7b4
+  __TEXT.__auth_stubs: 0x18d0
   __TEXT.__objc_stubs: 0x9480
   __TEXT.__objc_methlist: 0x8d98
-  __TEXT.__gcc_except_tab: 0x11e80
-  __TEXT.__const: 0xf0de
-  __TEXT.__cstring: 0x1afb6
-  __TEXT.__oslogstring: 0x1113b
-  __TEXT.__objc_classname: 0x10ce
+  __TEXT.__gcc_except_tab: 0x1042c
+  __TEXT.__const: 0xfa8e
+  __TEXT.__cstring: 0x1c7b7
+  __TEXT.__oslogstring: 0x117d8
+  __TEXT.__objc_classname: 0x1070
   __TEXT.__objc_methtype: 0x5f66
   __TEXT.__objc_methname: 0xc218
   __TEXT.__ustring: 0x10ae
-  __TEXT.__unwind_info: 0xc3c8
-  __TEXT.__eh_frame: 0x590
-  __DATA_CONST.__auth_got: 0xb68
-  __DATA_CONST.__got: 0x5c0
-  __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x25558
-  __DATA_CONST.__cfstring: 0x6a20
+  __TEXT.__unwind_info: 0xc6f8
+  __TEXT.__eh_frame: 0x670
+  __DATA_CONST.__const: 0x27400
+  __DATA_CONST.__cfstring: 0x6a40
   __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x448
-  __DATA_CONST.__objc_intobj: 0x1968
+  __DATA_CONST.__objc_intobj: 0x1a88
   __DATA_CONST.__objc_arraydata: 0x240
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x320
   __DATA_CONST.__objc_doubleobj: 0x10
+  __DATA_CONST.__auth_got: 0xc80
+  __DATA_CONST.__got: 0x608
+  __DATA_CONST.__auth_ptr: 0x48
   __DATA.__objc_const: 0x10660
   __DATA.__objc_selrefs: 0x3050
   __DATA.__objc_ivar: 0x94c

   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreMotionFDNML.framework/CoreMotionFDNML
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/HID.framework/HID

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 99265ADF-AA89-36F8-8B58-96A4D2C24479
-  Functions: 16385
-  Symbols:   572
-  CStrings:  9950
+  UUID: 3B44A355-7F59-32E7-BD51-AFB61DE22F94
+  Functions: 17094
+  Symbols:   617
+  CStrings:  10271
 
Symbols:
+ __ZN27CLKappaDeescalatorAnomalyFM10kConfigKeyE
+ __ZN27CLKappaDeescalatorAnomalyFM13kForceBaseKeyE
+ __ZN27CLKappaDeescalatorAnomalyFM22kConfigurationDefaultsE
+ __ZN27CLKappaFeaturesAlgAnomalyFM19kAnomalyFMConfigKeyE
+ __ZN27CLKappaFeaturesAlgAnomalyFM22kConfigurationDefaultsE
+ __ZN6motion19AnomalyFMEmbeddings7predictERKNSt3__13mapINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_2fm9ArrayDataENS1_4lessIS8_EENS6_INS1_4pairIKS8_SA_EEEEEENS1_8functionIFvNS1_10shared_ptrIKNS9_16PredictionResultEEEEEE
+ __ZN6motion19AnomalyFMEmbeddingsC1EPU28objcproto17OS_dispatch_queue8NSObject
+ __ZN6motion2fm6Client28sendModelManagerRequestAsyncERKNS0_19ModelManagerRequestENSt3__112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEENS5_8functionIFvNS5_10shared_ptrIKNS0_20ModelManagerResponseEEEEEE
+ __ZN6motion2fm6ClientC1EPU28objcproto17OS_dispatch_queue8NSObject
+ __ZN6motion2fm6ClientD1Ev
+ __ZNK6motion2fm9ArrayData11NumElementsEv
+ __ZNKSt3__16locale9use_facetERNS0_2idE
+ __ZNKSt3__18ios_base6getlocEv
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEf
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEi
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEj
+ __ZNSt3__118condition_variable10notify_oneEv
+ __ZNSt3__118condition_variable4waitERNS_11unique_lockINS_5mutexEEE
+ __ZNSt3__118condition_variableD1Ev
+ __ZNSt3__15ctypeIcE2idE
+ __ZNSt3__15mutex4lockEv
+ __ZNSt3__15mutex6unlockEv
+ __ZNSt3__15mutexD1Ev
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16localeD1Ev
+ __ZNSt3__18ios_base33__set_badbit_and_consider_rethrowEv
+ __ZNSt3__18ios_base4initEPv
+ __ZNSt3__18ios_base5clearEj
+ __ZNSt3__19basic_iosIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
+ __ZTTNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ _memset
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x10
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x9
CStrings:
+ ", "
+ "..."
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreSafety/SafetyAlgorithms/CLKappaFeaturesAlgAnomalyFM.mm"
+ "AnomalyFM"
+ "AnomalyFM_model"
+ "["
+ "[%s] Array '%s': type=%d shape=[%s], num_elements=%llu"
+ "[%s] Error encountered when running transit model %s"
+ "[%s] Raw bytes (uint8_t): [%s]"
+ "[%s] Typed values (float): [%s]"
+ "[%s] Typed values prediction %llu %f"
+ "[%s] all epochs were below threshold, deescalate inert: %d %d"
+ "[%s] all epochs were below threshold, deescalate: %d %d"
+ "[%s] an error was encountered running the mode, returning nop model %d adaptor %d"
+ "[%s] base model error: %s"
+ "[%s] deescalator active: %d %d: model found presence of crash"
+ "[%s] dump adapter input': [%s]"
+ "[%s] resetConfiguration"
+ "[%s] result_arrays size: %zu"
+ "[%s] returning decision nop"
+ "[%s] sending request %s"
+ "[%s] setConfig with enable,%d"
+ "[%s] skipping inference until all inputs present"
+ "[%s] summary,A,%{public}llu,B,%{public}u,mode,%{public}u,config-1,%{public}d,debug-1a,%{public}u,debug-1b,%{public}u,debug-1c,%{public}u,debug-1d,%{public}d,debug-1e,%{public}d"
+ "[AnomalyFM] summary,A,%{public}llu,B,%{public}f,config-1,%{public}d,config-2,%{public}f,config-3,%{public}d,debug-1a,%{public}u,debug-1b,%{public}u,debug-1c,%{public}u,debug-1d,%{public}u,debug-1e,%{public}d,debug-1f,%{public}d,debug-1g,%{public}f,debug-1h,%{public}f"
+ "[SC] AlgBlock summary,A,%{public}llu,B,%{public}llu,C,%{public}d,D,%{public}d,E,%{public}d,F,%{public}d,G,%{public}d,config-1,%{public}f,config-2,%{public}f,config-3,%{public}f,config-4,%{public}f,debug-1a,%{public}u,debug-1b,%{public}u,debug-1c,%{public}u,debug-2a,%{public}u,debug-2b,%{public}u,debug-2c,%{public}u,debug-2d,%{public}u,debug-2e,%{public}u,debug-2f,%{public}u,debug-2g,%{public}u,debug-2h,%{public}u,debug-2i,%{public}u,debug-2j,%{public}u,debug-2k,%{public}u,debug-2l,%{public}u,debug-2m,%{public}u,debug-2n,%{public}u,debug-2o,%{public}u,debug-2p,%{public}u,debug-2q,%{public}u,debug-2r,%{public}u,debug-2s,%{public}u"
+ "[SC] force %d %d %d %d %d is %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d"
+ "[Zg] summary,%{public}d,A,%{public}llu,B,%{public}hu,C,%{public}hu,D,%{public}f,E,%{public}f,F,%{public}f,G,%{public}f,H,%{public}f,I,%{public}hd,J,%{public}hu,K,%{public}d,L,%{public}d,M,%{public}d,N,%{public}llu,config-1,%{public}f,config-2,%{public}f\n"
+ "] "
+ "] missing config"
+ "accel0"
+ "accel1"
+ "accelNormYZ"
+ "accepted"
+ "accessoryHeadingFusionDMOutput"
+ "accessoryHeadingFusionVLInput"
+ "adaptiveMaxLow"
+ "adaptiveMinLow"
+ "adaptiveMinSecondPeak"
+ "adaptiveSecondPeakMeanMultiplier"
+ "angle"
+ "angleAccelMeasurement"
+ "angleDCPFilterOutput"
+ "angleDegrees"
+ "angleEstimatorState"
+ "angleGyroMeasurement"
+ "angleHES"
+ "anglePacket"
+ "anglePostMeas"
+ "angleProgress"
+ "angleRelGyroBiasMeasurement"
+ "angleUncertaintyPostMeas"
+ "arrivalMachAbsoluteTimestampMicroSeconds"
+ "arrivalMachContinuousTimestampMicroSeconds"
+ "arrivalTimestampMachAbsTimeMicroSeconds"
+ "arrivalTimestampMachContinuousTimeMicroSeconds"
+ "averageSteps"
+ "azimuthAngleToGravityAlignedViewConeCenterRad"
+ "bandpassNormYZ"
+ "bandpassX"
+ "bandpassY"
+ "bandpassZ"
+ "burstModeOnRequest"
+ "cameraFrameViewConeCenterDirectionX"
+ "cameraFrameViewConeCenterDirectionY"
+ "cameraFrameViewConeCenterDirectionZ"
+ "cannot call adaptor if not active"
+ "cannot call base model if not active"
+ "com.apple.fm.coremotion.anomalyfm"
+ "com.apple.fm.coremotion.anomalyfm.adaptor"
+ "com.coremotion.imufoundationmodel.ctl.queue"
+ "continuousFPLayer"
+ "continuousFPThreshold"
+ "continuousFPValue"
+ "cooldownDuration"
+ "covDiag"
+ "currentNegDurationX"
+ "currentNegDurationY"
+ "currentPosDurationX"
+ "currentPosDurationY"
+ "de-AnomalyFM"
+ "detected"
+ "detectedByPrimary"
+ "detectedBySecondary"
+ "detectionObjectValue"
+ "deviceAttitudeQuaternion"
+ "deviceAttitudeQuaternionW"
+ "deviceAttitudeQuaternionX"
+ "deviceAttitudeQuaternionY"
+ "deviceAttitudeQuaternionZ"
+ "dm6QI2B"
+ "dm9QNwu2B"
+ "dm9QNwu2I"
+ "doubleTapWindow"
+ "dumpAdaptorRow"
+ "durationS"
+ "ekAnchorBurstModeOnEvent"
+ "ekAnchorBurstModeSrcMotion"
+ "elevation"
+ "elevationAngleToGravityAlignedViewConeCenterRad"
+ "elevationChangeStd"
+ "elevationUncertainty"
+ "embeddings"
+ "endFloorIndex"
+ "excessiveXThreshold"
+ "fMyResult->fConfig.enabled"
+ "firstEndFX"
+ "firstEndFY"
+ "firstEndFZ"
+ "firstPeakLeftValley"
+ "firstPeakMagnitude"
+ "firstPeakProminence"
+ "firstPeakRightValley"
+ "firstPeakTimeUs"
+ "firstStartFX"
+ "firstStartFY"
+ "firstStartFZ"
+ "firstTapEndTimeUs"
+ "firstTapStartTimeUs"
+ "floorIndex"
+ "foldState"
+ "fpCooldownDuration"
+ "fpMitigationDisabled"
+ "g2gCalibration"
+ "gravityAlignedViewConeCenterDirectionX"
+ "gravityAlignedViewConeCenterDirectionY"
+ "gravityAlignedViewConeCenterDirectionZ"
+ "gravityAlignedViewConeHorizontalSpanAngleRad"
+ "gravityAlignedViewConeVerticalSpanAngleRad"
+ "gravityToBottomAngleDegrees"
+ "gripChangeFirstPeakY"
+ "gripChangeFirstPeakZ"
+ "gripChangeSecondPeakY"
+ "gripChangeSecondPeakZ"
+ "gripChangeYZRatioThreshold"
+ "gyroIMU0"
+ "gyroIMU1"
+ "gyroIMU1Interpolated"
+ "gyroIMU1Timestamp"
+ "gyroNormYZ"
+ "headingDeltaNwu2IRad"
+ "headphoneMotionActivity"
+ "hesState"
+ "highThreshold"
+ "historicalPressureMeasurement"
+ "historyWindowSamples"
+ "imuToImuContinuousTimestampMicroSeconds"
+ "imuToImuTimestampMicroSeconds"
+ "imu_input"
+ "inHandDoubleTap200HzInput"
+ "inHandDoubleTap800HzInput"
+ "inHandDoubleTapControlParams"
+ "inHandDoubleTapDetection"
+ "inHandDoubleTapMLInference"
+ "inHandDoubleTapSignals"
+ "inHandDoubleTapStats"
+ "inVisitRebasedMslp"
+ "inVisitStatus"
+ "initialFloorProbability"
+ "initialRecentHistoricalMeanSeaLevelPressure"
+ "innovation"
+ "invalid row"
+ "isAngleValid"
+ "isNIO"
+ "isNPDR"
+ "isQLeftImu2RightImuValid"
+ "isVelocityValid"
+ "kData4"
+ "lastAuxQBI"
+ "lastBurstModeOnRequestTimestampS"
+ "lastFeedTimestampS"
+ "lastMeasUpdateTimestampMicroSeconds"
+ "lastSrcStoppedTranslationTimestampS"
+ "lastVLInputTimestamp"
+ "loiEntryInfo"
+ "loiFloorMap"
+ "loiFloorTransitionModel"
+ "longestNegDurationXS"
+ "longestNegDurationYS"
+ "longestPosDurationXS"
+ "longestPosDurationYS"
+ "lowPassCutoffHz"
+ "lowThresholdAtDetection"
+ "lowpassNormYZ"
+ "lowpassX"
+ "lowpassY"
+ "lowpassZ"
+ "machAbsoluteTime"
+ "maxAbsBandpassX"
+ "maxBandpassYZNorm"
+ "maxFilteredAccelRange"
+ "maxNegDurationX"
+ "maxNegDurationY"
+ "maxPosDurationX"
+ "maxPosDurationY"
+ "maxSignalG"
+ "maxSingleTapDuration"
+ "meanElevationChange"
+ "meanSeaLevelPressure"
+ "meanTransitionTime"
+ "measurementValid"
+ "mechanicalAngleDegrees"
+ "medinaState"
+ "metsSource"
+ "minPeakTrackingDurationSamples"
+ "minSamplesBelowThreshold"
+ "observationTimestampMachAbsoluteTimeMicroSeconds"
+ "observationTimestampMachContinuousTimeMicroSeconds"
+ "occurrenceCount"
+ "omega0"
+ "omega1"
+ "oscillationAmplitudeThreshold"
+ "oscillationFrequencyThreshold"
+ "peakToLowMultiplier"
+ "phase"
+ "poseChangeThreshold"
+ "primaryBudDeviceAttitudeQuaternion"
+ "primaryFirstPeakMag"
+ "primaryFirstPeakTimeUs"
+ "primaryFirstTapEndTimeUs"
+ "primaryFirstTapStartTimeUs"
+ "primaryHighThreshold"
+ "primaryInitStabilitySec"
+ "primaryLowThreshold"
+ "primarySecondPeakMag"
+ "primarySecondPeakTimeUs"
+ "primarySecondTapEndTimeUs"
+ "primarySecondTapStartTimeUs"
+ "primarySecondTapThreshold"
+ "primaryState"
+ "prob200Hz"
+ "prob800Hz"
+ "progressValue"
+ "propertyA"
+ "propertyB"
+ "propertyBFrom"
+ "propertyBTo"
+ "propertyC"
+ "qBudPrimaryBudSecondary"
+ "qLeftImu2RightImuW"
+ "qLeftImu2RightImuX"
+ "qLeftImu2RightImuY"
+ "qLeftImu2RightImuZ"
+ "rawX"
+ "rawY"
+ "rawZ"
+ "rejectionLayer"
+ "relGyroBias"
+ "relGyroBiasPostMeas"
+ "relGyroBiasUncertaintyPostMeas"
+ "resourceId"
+ "rotation0"
+ "rotation1"
+ "rotationArbitraryToTrueNorth"
+ "rotationCameraToImu"
+ "rotationDM6InertialToImu"
+ "rotationImuToImu"
+ "row < kRowsInAdaptorInput"
+ "runAdaptor"
+ "runBaseModel"
+ "samplingRateHz"
+ "secondEndFX"
+ "secondEndFY"
+ "secondEndFZ"
+ "secondPeakLeftValley"
+ "secondPeakMagnitude"
+ "secondPeakProminence"
+ "secondPeakRightValley"
+ "secondPeakTimeUs"
+ "secondStartFX"
+ "secondStartFY"
+ "secondStartFZ"
+ "secondTapEndTimeUs"
+ "secondTapStartTimeUs"
+ "secondTapThresholdAtDetection"
+ "secondTapTriggerTimeout"
+ "secondaryFirstPeakMag"
+ "secondaryFirstPeakTimeUs"
+ "secondaryFirstTapEndTimeUs"
+ "secondaryFirstTapStartTimeUs"
+ "secondaryHighThreshold"
+ "secondaryInitStabilitySec"
+ "secondaryLowThreshold"
+ "secondarySMDisabled"
+ "secondarySecondPeakMag"
+ "secondarySecondPeakTimeUs"
+ "secondarySecondTapEndTimeUs"
+ "secondarySecondTapStartTimeUs"
+ "secondarySecondTapThreshold"
+ "secondaryState"
+ "sensorLocation"
+ "settlingEndTimeUs"
+ "settlingMean"
+ "settlingStartTimeUs"
+ "settlingStdDev"
+ "shouldDeescalateBecauseOfAnomalyFMCondition"
+ "stabilityAfterFirstTapSec"
+ "stabilityAfterSecondTapSec"
+ "stage"
+ "startFloorIndex"
+ "staticState"
+ "stepsStd"
+ "tempestHeadphoneMotionActivity"
+ "timeReference"
+ "timeSinceLastBurstModeOnRequestS"
+ "timeSinceLastSrcStoppedTranslationS"
+ "timestampMachAbsTimeMicroSeconds"
+ "timestampMachContinuousTimeMicroSeconds"
+ "timestampStartS"
+ "timestampStopS"
+ "transitionTimeStd"
+ "unfilteredEntityKitBoundingBoxDataList"
+ "valleyEndTimeUs"
+ "valleyMean"
+ "valleyStartTimeUs"
+ "valleyStdDev"
+ "velocityDegreesPerSecond"
+ "vlQNwu2Imu"
+ "vlSensorLocation"
+ "vlUnc"
+ "wallTime"
+ "xAxisDominanceThreshold"
+ "zg-M"
+ "{\"msg%{public}.0s\":\"cannot call adaptor if not active\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"cannot call base model if not active\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"invalid row\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "Acc100Fp"
- "Acc800Fp"
- "DmFp"
- "[SC] AlgBlock summary,A,%{public}llu,B,%{public}llu,C,%{public}d,D,%{public}d,E,%{public}d,F,%{public}d,G,%{public}d,config-1,%{public}f,config-2,%{public}f,config-3,%{public}f,config-4,%{public}f,debug-1a,%{public}u,debug-1b,%{public}u,debug-1c,%{public}u,debug-2a,%{public}u,debug-2b,%{public}u,debug-2c,%{public}u,debug-2d,%{public}u,debug-2e,%{public}u,debug-2f,%{public}u,debug-2g,%{public}u,debug-2h,%{public}u,debug-2i,%{public}u,debug-2j,%{public}u,debug-2k,%{public}u,debug-2l,%{public}u,debug-2m,%{public}u,debug-2n,%{public}u,debug-2o,%{public}u,debug-2p,%{public}u,debug-2q,%{public}u,debug-2r,%{public}u"
- "[SC] force %d %d %d %d %d is %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d"
- "[Zg] summary,%{public}d,A,%{public}llu,B,%{public}hu,C,%{public}hu,D,%{public}f,E,%{public}f,F,%{public}f,G,%{public}f,H,%{public}f,I,%{public}hd,J,%{public}hu,K,%{public}d,L,%{public}d,M,%{public}d,config-1,%{public}f,config-2,%{public}f\n"

```
