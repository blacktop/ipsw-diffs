## CoreMotionAlgorithms

> `/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms`

```diff

-2886.1.7.0.0
-  __TEXT.__text: 0x20ed18
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_methlist: 0x628
-  __TEXT.__const: 0x47b2
-  __TEXT.__cstring: 0xf563
-  __TEXT.__gcc_except_tab: 0x38fc
-  __TEXT.__oslogstring: 0x181c
-  __TEXT.__unwind_info: 0x6b1c
+2890.0.8.0.5
+  __TEXT.__text: 0x214b18
+  __TEXT.__auth_stubs: 0xce0
+  __TEXT.__objc_methlist: 0x688
+  __TEXT.__const: 0x4882
+  __TEXT.__cstring: 0xf916
+  __TEXT.__gcc_except_tab: 0x3978
+  __TEXT.__oslogstring: 0x1b86
+  __TEXT.__unwind_info: 0x6c70
   __TEXT.__eh_frame: 0x644
-  __TEXT.__objc_classname: 0x159
-  __TEXT.__objc_methname: 0x191d
-  __TEXT.__objc_methtype: 0x21be
-  __TEXT.__objc_stubs: 0xfa0
+  __TEXT.__objc_classname: 0x15a
+  __TEXT.__objc_methname: 0x1b97
+  __TEXT.__objc_methtype: 0x2566
+  __TEXT.__objc_stubs: 0x1100
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x3c0
+  __DATA_CONST.__const: 0x3e0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf30
-  __DATA_CONST.__objc_selrefs: 0x570
-  __AUTH_CONST.__const: 0x9570
-  __AUTH_CONST.__cfstring: 0x340
+  __DATA_CONST.__objc_const: 0x1000
+  __DATA_CONST.__objc_selrefs: 0x5c8
+  __AUTH_CONST.__const: 0x96a0
+  __AUTH_CONST.__cfstring: 0x3a0
   __AUTH_CONST.__objc_const: 0x2d0
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x678
+  __AUTH_CONST.__auth_got: 0x680
   __AUTH.__objc_data: 0x320
   __AUTH.__data: 0x8
   __DATA.__objc_classrefs: 0x78
   __DATA.__objc_superrefs: 0x18
-  __DATA.__objc_ivar: 0x120
-  __DATA.__data: 0x778
+  __DATA.__objc_ivar: 0x134
+  __DATA.__data: 0x798
   __DATA.__common: 0x110
-  __DATA.__bss: 0x13d8
+  __DATA.__bss: 0x13e8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9329
-  Symbols:   267
-  CStrings:  3568
+  Functions: 9427
+  Symbols:   268
+  CStrings:  3627
 
Symbols:
+ _kdebug_trace
CStrings:
+ "CMAPrecisionFindingManager,timestamp,%{public}f,horizontalAngle,%{public}f,horizontalAngleUncertainty,%{public}f,positionX,%{public}f,positionY,%{public}f,positionZ,%{public}f,velocityX,%{public}f,velocityY,%{public}f,isConverged,%{public}d,revokeReason,%{public}d,verticalState,%{public}d"
+ "CMPrecisionFindingPositionEstimator::fVerticalState,timestamp,%{public}f,horizontalDistance,%{public}f,verticalDistance,%{public}f,relativeAltitude,%{public}f,fractionAboveThreshold,%{public}f,likelihoodAboveThreshold,%{public}f,isConverged,%{public}d,isAboveBelow,%{public}d,isAboveBelowMessageShowing,%{public}d,wasInMediumRange,%{public}d,wasLevelChanged,%{public}d,timeElapsedSinceAboveBelowFractionHigh,%{public}f,isAboveBelowFractionConsistentlyHigh,%{public}d,distanceChangeSinceAboveBelowFractionHigh,%{public}f,isDistanceChangedEnoughForAboveBelowMessage,%{public}d,timeElapsedSinceAboveBelowMessageShown,%{public}f,aboveBelowMessageShownLongerThanThreshold,%{public}d,elevationChangeSinceAboveBelowMessageShown,%{public}f,isChangingLevelWhileAboveBelowMessageShowing,%{public}d,wasAboveBelowMessageShown,%{public}d"
+ "LogAriadneSignposts"
+ "MaxEstimatedDeltaHeightOverSession"
+ "MaxPercentParticlesAboveHeightThreshold"
+ "T@\"NSNumber\",&,N,V_maxEstimatedDeltaHeightOverSession"
+ "T@\"NSNumber\",&,N,V_maxPercentParticlesAboveHeightThreshold"
+ "T@\"NSNumber\",N,V_horizontalAngleUncertaintyNumber"
+ "_horizontalAngleUncertaintyNumber"
+ "_maxEstimatedDeltaHeightOverSession"
+ "_maxEstimatedHeight"
+ "_maxPercentParticlesAboveHeightThreshold"
+ "_minEstimatedHeight"
+ "accelPeakThreshold"
+ "allMaxNormTimestamps"
+ "allMaxNormValues"
+ "boolForKey:"
+ "companionAopTs"
+ "doubleValue"
+ "enableMode"
+ "feedEstimatedHeight:"
+ "feedFractionAboveThreshold:"
+ "firstTimestampMAPDecision"
+ "fractionAboveThreshold"
+ "horizontalAngleUncertainty"
+ "horizontalAngleUncertaintyNumber"
+ "horizontalAngleUncertaintyUnfiltered"
+ "horizontalDistance"
+ "isAboveBelow"
+ "isAboveBelowMessageShowing"
+ "isFreeFallDetectedEpoch"
+ "isMAPDetected"
+ "isMAPFPDecided"
+ "kappaPeakDetectorMapMagTimestamps"
+ "kappaPeakDetectorMapResult"
+ "lastTimestampMAPDecision"
+ "likelihoodAboveThreshold"
+ "magnitudePercentileThreshold"
+ "magnitudePeriodicityLowerPercentile"
+ "magnitudePeriodicityUpperPercentile"
+ "martyTriggerPathBitmap"
+ "maxEstimatedDeltaHeightOverSession"
+ "maxNormTimestamp"
+ "maxNormValue"
+ "maxPercentParticlesAboveHeightThreshold"
+ "minNumPeaks"
+ "numDeescalationMAP"
+ "peakMagnitudePercentileDiff"
+ "peakSeparation"
+ "peakTimeDeltaPercentileDiff"
+ "peakToPeakMinimumSeparation"
+ "peakToPeakSeparationThreshold"
+ "precisionFindingVerticalState"
+ "setHorizontalAngleUncertaintyNumber:"
+ "setMaxEstimatedDeltaHeightOverSession:"
+ "setMaxPercentParticlesAboveHeightThreshold:"
+ "shouldDeescalateBecauseOfMAPFPCondition"
+ "standardUserDefaults"
+ "timePercentileDiffThreshold"
+ "timePeriodicityLowerPercentile"
+ "timePeriodicityUpperPercentile"
+ "verticalDistance"
+ "{CMPrecisionFindingPositionEstimator=\"fPosition\"{CMAPositionType=\"timestamp\"d\"distance\"f\"horizontalAngle\"f\"horizontalAngleUncertainty\"f\"isConverged\"B\"revokeReason\"i\"isDistanceValid\"B}\"fParticleFilterState\"{CMFindingParticleFilterState=\"timestamp\"d\"horizontalAngleUncertaintyUnfiltered\"f\"stateEstimate\"{array<float, 5UL>=\"__elems_\"[5f]}}\"fVerticalState\"{CMAVerticalState=\"timestamp\"d\"horizontalDistance\"f\"verticalDistance\"f\"relativeAltitude\"f\"fractionAboveThreshold\"f\"likelihoodAboveThreshold\"f\"isConverged\"B\"isAboveBelow\"B\"isAboveBelowMessageShowing\"B}\"fVelocityEstimator\"{CMPrecisionFindingVelocityEstimator=\"fDownsampler\"{CMDownsampler<double>=\"_vptr$CMDownsampler\"^^?\"fMinimumToleratedDt\"d\"fLastTimestamp\"d}\"fPlanarVelocity\"{CMVector<float, 2UL>=\"elements\"[2f]}\"fNoise\"{CMVector<float, 2UL>=\"elements\"[2f]}\"fSensorBuffers\"{CMAOPFFTSensorBuffers=\"fBuffers\"{Buffers=\"inertialRotationRateX\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"inertialRotationRateY\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"inertialRotationRateZ\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"userRotationRateX\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"userRotationRateY\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"userRotationRateZ\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"inertialAccelX\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"inertialAccelY\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"inertialAccelZ\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"userAccelX\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"userAccelY\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"userAccelZ\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"attitude\"{CMFixedSizeQueue<CMOQuaternion, 256UL>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[16c]\"fStorage\"{CMQueueStorage<CMOQuaternion, 256UL>=\"buffer\"[4080c]}}\"fTimestamp\"Q\"timestampDelta\"{CMFixedSizeQueue<unsigned short, 127UL>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[2c]\"fStorage\"{CMQueueStorage<unsigned short, 127UL>=\"buffer\"[252c]}}}\"fCountDeviceMotionForPDRFeatures\"Q\"fCountDeviceMotionForPDRFeaturesFast\"Q\"fTNB\"{TNB=\"userAccelInerLPF\"{CMVector<float, 3UL>=\"elements\"[3f]}\"userAccelInerLPFPrev\"{CMVector<float, 3UL>=\"elements\"[3f]}\"tangent\"{CMVector<float, 3UL>=\"elements\"[3f]}\"binormal\"{CMVector<float, 3UL>=\"elements\"[3f]}\"isValid\"B\"dotVector\"{CMVector<float, 2UL>=\"elements\"[2f]}\"dotVectorFiltered\"{CMVector<float, 2UL>=\"elements\"[2f]}\"dotFilter\"[2{CLButterworthFilter<float, 2UL>=\"fPrimed\"Q\"fOffset\"Q\"fData\"[5f]\"fCoefficients\"[9f]}]}}\"fSpeedEstimator\"{CMPDRSpeedEstimator=\"fSpeed\"f\"fSpeedUnc\"f}\"fDOTEstimator\"{CMAPrecisionFindingDOTEstimator=\"fBodyYAxis\"{CMVector<float, 3UL>=\"elements\"[3f]}\"fIsWristCrownInitialized\"B\"fWristCrownConfig\"{CMAWatchOrientationStruct=\"timestamp\"d\"wrist\"i\"crown\"i}}\"fIsDOTAvailable\"B}\"fRangeHandler\"{CMFindingRangeHandler=\"fFirstSampleAccepted\"B\"fRangeBuffer\"{CMFixedSizeRunningBuffer<float, 10UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 10UL>=\"buffer\"[36c]}}\"fRangeTimeBuffer\"{CMFixedSizeRunningBuffer<double, 10UL>=\"fIsStaleStatistics\"B\"fMean\"d\"fVariance\"d\"fNorm\"d\"fSamples\"{CMQueue<double>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[8c]}\"fStorage\"{CMQueueStorage<double, 10UL>=\"buffer\"[72c]}}\"fRangeIsValidBuffer\"{CMFixedSizeRunningBuffer<bool, 10UL>=\"fIsStaleStatistics\"B\"fMean\"B\"fVariance\"B\"fNorm\"B\"fSamples\"{CMQueue<bool>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[1c]}\"fStorage\"{CMQueueStorage<bool, 10UL>=\"buffer\"[9c]}}\"fFirstOrderRangeFilter\"{FirstOrderFilter<float>=\"fNumSamples\"i\"fAlpha\"f\"fFiltered\"f}\"fSustainedLowRangeObserved\"B\"fLowRangeCount\"I}\"fParticleFilter\"{CMFindingParticleFilter=\"fRangeMeasurement\"{RangeMeasurement=\"range\"f\"rangeShift\"f}\"fVelocityMeasurement\"{VelocityEstimation=\"velocity\"{CMVector<float, 2UL>=\"elements\"[2f]}\"noise\"{CMVector<float, 2UL>=\"elements\"[2f]}}\"fSpeedMeasurenment\"f\"fParticleFilter\"{CMParticleFilter<5UL>=\"fParticles\"{vector<std::array<float, 5>, std::allocator<std::array<float, 5>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::array<float, 5> *, std::allocator<std::array<float, 5>>>=\"__value_\"^v}}\"fWeights\"{vector<double, std::allocator<double>>=\"__begin_\"^d\"__end_\"^d\"__end_cap_\"{__compressed_pair<double *, std::allocator<double>>=\"__value_\"^d}}\"fNumParticles\"Q}\"fParticles\"^v\"fWeights\"^v\"fNumParticles\"Q\"fWasMeasurementApplied\"B\"fCurrentState\"{array<float, 5UL>=\"__elems_\"[5f]}\"fAngularDeviation\"f\"fTimestamp\"d\"fCurrentAccel\"{CMVector<float, 2UL>=\"elements\"[2f]}\"fBatchedDv\"{CMVector<float, 2UL>=\"elements\"[2f]}\"fBatchedDt\"f\"fPreviousAltitude\"f\"fCurrentAltitude\"f\"fFirstAltitude\"B\"fMeasurementCount\"Q\"fEstimatedAbsoluteVerticalRange\"f\"fEstimatedHorizontalRange\"f\"fEstimatedTotalRange\"f\"fAboveBelowFraction\"f\"fAboveBelowLikelihood\"f}\"fFirstArcShown\"B\"fActivityBuffer\"{CMFixedSizeRunningBuffer<unsigned int, 4UL>=\"fIsStaleStatistics\"B\"fMean\"I\"fVariance\"I\"fNorm\"I\"fSamples\"{CMQueue<unsigned int>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<unsigned int, 4UL>=\"buffer\"[12c]}}\"fActivityTimeBuffer\"{CMFixedSizeRunningBuffer<unsigned int, 4UL>=\"fIsStaleStatistics\"B\"fMean\"I\"fVariance\"I\"fNorm\"I\"fSamples\"{CMQueue<unsigned int>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<unsigned int, 4UL>=\"buffer\"[12c]}}\"fWristCrownConfig\"{CMAWatchOrientationStruct=\"timestamp\"d\"wrist\"i\"crown\"i}\"fWasPhoneMoving\"B\"fIsWristCrownInitialized\"B\"fIsFilterInitialized\"B\"fNumParticles\"Q\"fEnableRevokeDelayTimer\"B\"fHighUncertaintyTimeStamp\"d\"fRangeAtArcRevoke\"f\"fPreviousVelocityTimeStamp\"d\"fAcceptedRange\"{optional<CMARangeType>=\"\"(?=\"__null_state_\"c\"__val_\"{CMARangeType=\"timestamp\"d\"range\"d\"rangeError\"d\"rssi\"d\"cycleIndex\"S})\"__engaged_\"B}\"fRangeKalmanFilter\"{CMAPrecisionFindingRangeKF=\"fState\"d\"fP\"d\"fTimestampLastUpdate\"d\"fIsInitialized\"B}\"fPreviousRawRange\"d\"fPreviousRawRangeTimestamp\"d\"fBaseAltitude\"f\"fCurrentAltitude\"f\"fWasFirstAltitudeReceived\"B\"fWasInMediumRange\"B\"fWasLevelChanged\"B\"fAboveBelowFractionTimeStamp\"d\"fAboveBelowFirstMessageTimeStamp\"d\"fIsAboveBelowMeassageShowing\"B\"fWasAboveBelowMessageShown\"B\"fMaxDistanceWhenAboveBelowFractionHigh\"f\"fMinDistanceWhenAboveBelowFractionHigh\"f\"fElevationWhenAboveBelowFractionHigh\"f\"fIsAboveBelowFractionHigh\"B\"fLoggingDownsampler\"{CMDownsampler<double>=\"_vptr$CMDownsampler\"^^?\"fMinimumToleratedDt\"d\"fLastTimestamp\"d}}"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xe1"
- "CMAPrecisionFindingManager,timestamp,%{public}f,horizontalAngle,%{public}f,horizontalAngleAccuracy,%{public}f,positionX,%{public}f,positionY,%{public}f,velocityX,%{public}f,velocityY,%{public}f,isConverged,%{public}d,revokeReason,%{public}d"
- "horizontalAngleAccuracyUnfiltered"
- "{CMPrecisionFindingPositionEstimator=\"fPosition\"{CMAPositionType=\"timestamp\"d\"distance\"f\"horizontalAngle\"f\"horizontalAngleAccuracy\"f\"isConverged\"B\"revokeReason\"i\"isDistanceValid\"B}\"fParticleFilterState\"{CMFindingParticleFilterState=\"timestamp\"d\"horizontalAngleAccuracyUnfiltered\"f\"stateEstimate\"{array<float, 4UL>=\"__elems_\"[4f]}}\"fVelocityEstimator\"{CMPrecisionFindingVelocityEstimator=\"fDownsampler\"{CMDownsampler<double>=\"_vptr$CMDownsampler\"^^?\"fMinimumToleratedDt\"d\"fLastTimestamp\"d}\"fPlanarVelocity\"{CMVector<float, 2UL>=\"elements\"[2f]}\"fNoise\"{CMVector<float, 2UL>=\"elements\"[2f]}\"fSensorBuffers\"{CMAOPFFTSensorBuffers=\"fBuffers\"{Buffers=\"inertialRotationRateX\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"inertialRotationRateY\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"inertialRotationRateZ\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"userRotationRateX\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"userRotationRateY\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"userRotationRateZ\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"inertialAccelX\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"inertialAccelY\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"inertialAccelZ\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"userAccelX\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"userAccelY\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"userAccelZ\"{CMFixedSizeRunningBuffer<float, 256UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 256UL>=\"buffer\"[1020c]}}\"attitude\"{CMFixedSizeQueue<CMOQuaternion, 256UL>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[16c]\"fStorage\"{CMQueueStorage<CMOQuaternion, 256UL>=\"buffer\"[4080c]}}\"fTimestamp\"Q\"timestampDelta\"{CMFixedSizeQueue<unsigned short, 127UL>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[2c]\"fStorage\"{CMQueueStorage<unsigned short, 127UL>=\"buffer\"[252c]}}}\"fCountDeviceMotionForPDRFeatures\"Q\"fCountDeviceMotionForPDRFeaturesFast\"Q\"fTNB\"{TNB=\"userAccelInerLPF\"{CMVector<float, 3UL>=\"elements\"[3f]}\"userAccelInerLPFPrev\"{CMVector<float, 3UL>=\"elements\"[3f]}\"tangent\"{CMVector<float, 3UL>=\"elements\"[3f]}\"binormal\"{CMVector<float, 3UL>=\"elements\"[3f]}\"isValid\"B\"dotVector\"{CMVector<float, 2UL>=\"elements\"[2f]}\"dotVectorFiltered\"{CMVector<float, 2UL>=\"elements\"[2f]}\"dotFilter\"[2{CLButterworthFilter<float, 2UL>=\"fPrimed\"Q\"fOffset\"Q\"fData\"[5f]\"fCoefficients\"[9f]}]}}\"fSpeedEstimator\"{CMPDRSpeedEstimator=\"fSpeed\"f\"fSpeedUnc\"f}\"fDOTEstimator\"{CMAPrecisionFindingDOTEstimator=\"fBodyYAxis\"{CMVector<float, 3UL>=\"elements\"[3f]}\"fIsWristCrownInitialized\"B\"fWristCrownConfig\"{CMAWatchOrientationStruct=\"timestamp\"d\"wrist\"i\"crown\"i}}\"fIsDOTAvailable\"B}\"fParticleFilter\"{CMFindingParticleFilter=\"fRangeMeasurement\"{RangeMeasurement=\"range\"f\"rangeShift\"f}\"fVelocityMeasurement\"{VelocityEstimation=\"velocity\"{CMVector<float, 2UL>=\"elements\"[2f]}\"noise\"{CMVector<float, 2UL>=\"elements\"[2f]}}\"fSpeedMeasurenment\"f\"fParticleFilter\"{CMParticleFilter<4UL>=\"fParticles\"{vector<std::array<float, 4>, std::allocator<std::array<float, 4>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::array<float, 4> *, std::allocator<std::array<float, 4>>>=\"__value_\"^v}}\"fWeights\"{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__end_cap_\"{__compressed_pair<float *, std::allocator<float>>=\"__value_\"^f}}\"fNumParticles\"Q}\"fParticles\"^v\"fWeights\"^v\"fNumParticles\"Q\"fWasMeasurementApplied\"B\"fCurrentState\"{array<float, 4UL>=\"__elems_\"[4f]}\"fAngularDeviation\"f\"fTimestamp\"d\"fCurrentAccel\"{CMVector<float, 2UL>=\"elements\"[2f]}\"fBatchedDv\"{CMVector<float, 2UL>=\"elements\"[2f]}\"fBatchedDt\"f\"fMeasurementCount\"Q\"fEstimatedRangeFromParticles\"f}\"fFirstSampleAccepted\"B\"fFirstArcShown\"B\"fRangeBuffer\"{CMFixedSizeRunningBuffer<float, 10UL>=\"fIsStaleStatistics\"B\"fMean\"f\"fVariance\"f\"fNorm\"f\"fSamples\"{CMQueue<float>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<float, 10UL>=\"buffer\"[36c]}}\"fRangeTimeBuffer\"{CMFixedSizeRunningBuffer<double, 10UL>=\"fIsStaleStatistics\"B\"fMean\"d\"fVariance\"d\"fNorm\"d\"fSamples\"{CMQueue<double>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[8c]}\"fStorage\"{CMQueueStorage<double, 10UL>=\"buffer\"[72c]}}\"fRangeIsValidBuffer\"{CMFixedSizeRunningBuffer<bool, 10UL>=\"fIsStaleStatistics\"B\"fMean\"B\"fVariance\"B\"fNorm\"B\"fSamples\"{CMQueue<bool>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[1c]}\"fStorage\"{CMQueueStorage<bool, 10UL>=\"buffer\"[9c]}}\"fActivityBuffer\"{CMFixedSizeRunningBuffer<unsigned int, 4UL>=\"fIsStaleStatistics\"B\"fMean\"I\"fVariance\"I\"fNorm\"I\"fSamples\"{CMQueue<unsigned int>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<unsigned int, 4UL>=\"buffer\"[12c]}}\"fActivityTimeBuffer\"{CMFixedSizeRunningBuffer<unsigned int, 4UL>=\"fIsStaleStatistics\"B\"fMean\"I\"fVariance\"I\"fNorm\"I\"fSamples\"{CMQueue<unsigned int>=\"fHeadAndSize\"{?=\"fHead\"S\"fSize\"S}\"fCapacity\"I\"fBuffer\"[4c]}\"fStorage\"{CMQueueStorage<unsigned int, 4UL>=\"buffer\"[12c]}}\"fWristCrownConfig\"{CMAWatchOrientationStruct=\"timestamp\"d\"wrist\"i\"crown\"i}\"fWasPhoneMoving\"B\"fIsWristCrownInitialized\"B\"fIsFilterInitialized\"B\"fNumParticles\"Q\"fAngleUncertaintyFilter\"{FirstOrderFilter<float>=\"fNumSamples\"i\"fAlpha\"f\"fFiltered\"f}\"fFirstOrderRangeFilter\"{FirstOrderFilter<float>=\"fNumSamples\"i\"fAlpha\"f\"fFiltered\"f}\"fSustainedLowRangeObserved\"B\"fLowRangeCount\"I\"fPreviousRange\"f\"fPreviousRangeTimeStamp\"d\"fLowAccuracyTimeStamp\"d\"fRangeWhenArcRevokedDueToHighUncertainty\"f\"fPreviousVelocityTimeStamp\"d\"fAcceptedRange\"{optional<CMARangeType>=\"\"(?=\"__null_state_\"c\"__val_\"{CMARangeType=\"timestamp\"d\"range\"d\"rangeError\"d\"rssi\"d\"cycleIndex\"S})\"__engaged_\"B}}"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0q"

```
