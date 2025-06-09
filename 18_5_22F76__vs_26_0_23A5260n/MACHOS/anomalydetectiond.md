## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-125.0.17.0.0
-  __TEXT.__text: 0x32ee4c
-  __TEXT.__auth_stubs: 0x1660
-  __TEXT.__objc_stubs: 0x9180
-  __TEXT.__objc_methlist: 0x8c50
-  __TEXT.__gcc_except_tab: 0x10cec
-  __TEXT.__const: 0x8db6
-  __TEXT.__cstring: 0x199e0
-  __TEXT.__oslogstring: 0xfe21
-  __TEXT.__objc_classname: 0x10d9
-  __TEXT.__objc_methtype: 0x63b5
-  __TEXT.__objc_methname: 0xbea0
+143.0.0.0.0
+  __TEXT.__text: 0x34d690
+  __TEXT.__auth_stubs: 0x1670
+  __TEXT.__objc_stubs: 0x90e0
+  __TEXT.__objc_methlist: 0x8c28
+  __TEXT.__gcc_except_tab: 0x10fcc
+  __TEXT.__const: 0x9246
+  __TEXT.__cstring: 0x1a216
+  __TEXT.__oslogstring: 0xfe12
+  __TEXT.__objc_classname: 0x10a6
+  __TEXT.__objc_methtype: 0x5ce4
+  __TEXT.__objc_methname: 0xbe19
   __TEXT.__ustring: 0x10ae
-  __TEXT.__unwind_info: 0xb7b8
+  __TEXT.__unwind_info: 0xbdd0
   __TEXT.__eh_frame: 0x590
-  __DATA_CONST.__auth_got: 0xb48
-  __DATA_CONST.__got: 0x590
-  __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x22408
-  __DATA_CONST.__cfstring: 0x6100
-  __DATA_CONST.__objc_classlist: 0x4c8
+  __DATA_CONST.__auth_got: 0xb50
+  __DATA_CONST.__got: 0x5a0
+  __DATA_CONST.__auth_ptr: 0x30
+  __DATA_CONST.__const: 0x22d00
+  __DATA_CONST.__cfstring: 0x6380
+  __DATA_CONST.__objc_classlist: 0x4c0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x130
+  __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x448
-  __DATA_CONST.__objc_intobj: 0x1818
+  __DATA_CONST.__objc_superrefs: 0x440
+  __DATA_CONST.__objc_intobj: 0x1950
   __DATA_CONST.__objc_arraydata: 0x240
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x320
-  __DATA.__objc_const: 0x105a8
-  __DATA.__objc_selrefs: 0x2f80
-  __DATA.__objc_ivar: 0x964
-  __DATA.__objc_data: 0x2fd0
-  __DATA.__data: 0x2070
+  __DATA_CONST.__objc_doubleobj: 0x10
+  __DATA.__objc_const: 0xff48
+  __DATA.__objc_selrefs: 0x2f58
+  __DATA.__objc_ivar: 0x934
+  __DATA.__objc_data: 0x2f80
+  __DATA.__data: 0x2010
   __DATA.__bss: 0x230
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
-  - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
-  - /System/Library/PrivateFrameworks/BiomeDSL.framework/BiomeDSL
-  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
-  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
+  - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/HID.framework/HID

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SOS.framework/SOS
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1D68CD9C-8AAC-32AB-9278-901E537328AA
-  Functions: 15305
-  Symbols:   561
-  CStrings:  9525
+  UUID: 0A952C44-38AC-3F32-A457-04AC56F5E591
+  Functions: 15872
+  Symbols:   565
+  CStrings:  9666
 
Symbols:
+ _IOPMAssertionCreateWithProperties
+ _IOPMAssertionRelease
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_UAFAssetSetManager
+ __ZNSt12out_of_rangeD1Ev
+ __ZTISt12out_of_range
+ __ZTVSt12out_of_range
+ _objc_autoreleasePoolPop
- _BiomeLibrary
- _CPPowerAssertionCreate
- _OBJC_CLASS_$_BMBiomeScheduler
- _OBJC_CLASS_$_BMStreams
CStrings:
+ "/System/Library/Frameworks/SafetyKit.framework"
+ "AOI - Bad input in test dict"
+ "AOI ident %@ (%f, %f) mode %d expect %d near %d, pass %d"
+ "AOIs.json"
+ "AnomalydetectiondPLEvent"
+ "AssertName"
+ "AssertType"
+ "Attempting to release power assertion when there is none, ref count %d"
+ "B28@0:8@16B24"
+ "CSKappaConnectionTestSensorAccessQuery"
+ "Creating power assertion failed"
+ "Error parsing %@: %@"
+ "Error reading file: %@"
+ "FEEDBACK_ASSISTANT_NOTIFICATION"
+ "File not found %@"
+ "Kappa Detection"
+ "Malformatted AOI json, element not number %@"
+ "Malformatted AOI json, row not list %@"
+ "Malformatted AOI json, row with wrong count %@"
+ "Malformatted AOI json, top level %@"
+ "Opening Fastpaths"
+ "Power assertion ref count should have been 0 but is to %d"
+ "Power assertion ref decreased to %d"
+ "Power assertion ref increased to %d for %@"
+ "PreventUserIdleSystemSleep"
+ "SensorAccess"
+ "Sorted %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u"
+ "Successfully created new power assertion for %@"
+ "Successfully released power assertion"
+ "TIA"
+ "TimeoutAction"
+ "TimeoutActionRelease"
+ "TimeoutSeconds"
+ "UAFUsages"
+ "[de-AOI] No assetSet"
+ "[de-AOI] invalid coordinate"
+ "[de-AOI] loadAOIs returned nullptr"
+ "[de-AOI] mode,%u,hardcoded,%d,OTA %d %d %d %d"
+ "[de-AOI] summary,A,%{public}llu,B,%{public}u,mode,%{public}u,debug-1a,%{public}u,"
+ "[de-AOI] usages %@"
+ "_assertionDescription"
+ "_assertionName"
+ "aFDeviceMotionConfig"
+ "aFHeartRate"
+ "accelBiasEstimate"
+ "accelRotationRate"
+ "accessoryBatchedPPG"
+ "accessoryInEarDetection"
+ "anomalydetectiondPLRecordType"
+ "assetNamed:"
+ "audioAFDeviceMotion"
+ "batchedPPGData"
+ "blankDacOffset"
+ "blankDark"
+ "blankLight"
+ "blankTIA"
+ "blankiLED"
+ "boolForKey:withFallback:"
+ "bundleWithPath:"
+ "cMPedEntry"
+ "cMPedometerStep"
+ "cVIMUMeasurement"
+ "collectSensorControlTelemetry"
+ "com.apple.anomalydetectiond.kappa.aoi.test"
+ "com.apple.aonsense"
+ "com.apple.aonsense.safety.country"
+ "com.apple.aonsense.safety.generic"
+ "companionStepCountElevation"
+ "configId"
+ "configMask"
+ "consecutiveEpochs"
+ "courseFusion"
+ "covUT"
+ "dacOffset"
+ "dark"
+ "deterministicAlgoDecisionBool"
+ "dictionary"
+ "doGyroPropagate"
+ "elevationBatchProcessingTimestamps"
+ "ended"
+ "est"
+ "eventTimeNS"
+ "expected"
+ "fGyroXLatestGyroValleyIntegratedValueLeftZCToMaxima"
+ "fGyroXLatestGyroValleyValueRps"
+ "fGyroXNumPeaksInLast5sCount"
+ "fGyroXNumValleysInLast2s"
+ "fScreenTiltAngle2sLast"
+ "fWristAngleToHorizontal2sFirst"
+ "fWristAngleToHorizontal2sFirstToLast"
+ "fWristAngleToHorizontal2sLast"
+ "failure"
+ "firmwareVersion"
+ "flagBitfield"
+ "flickFPDetectorFeatures"
+ "flickGyroMaxima"
+ "flickLPFDM6Data"
+ "flickMaxima"
+ "frameType"
+ "gPSCalibrationBin"
+ "gravVarianceSum"
+ "gravityXG"
+ "gravityYG"
+ "gravityZG"
+ "gyroBiasEstimate"
+ "gyroController"
+ "gyroScaleEstimate"
+ "gyroX"
+ "gyroY"
+ "gyroZ"
+ "hardwareVersion"
+ "heartRateSourceDevice"
+ "horizontalRotation"
+ "hrSensorLocation"
+ "iLED"
+ "imuComboPacket"
+ "integratedValueLeftZCToMaxima"
+ "integratedValueLeftZCToRightHalf"
+ "integratedValueLeftZCToRightZC"
+ "isArmedForKappa"
+ "isCandidate"
+ "isCourseStable"
+ "isCourseValid"
+ "isDOTBiasChangePossible"
+ "isFiller"
+ "isIEDEnabled"
+ "isPeak"
+ "isStablePoseFiltered"
+ "isVirtualTransport"
+ "isZUPT"
+ "kalmanGain"
+ "key '%@' has non-string value: %@"
+ "lastUpdateTime"
+ "light"
+ "localizedStringForKey:value:table:"
+ "manufacturer"
+ "measurementNoise"
+ "movingGpsBlockoutWindow"
+ "navigationListener:didUpdateNoCellCoverage:"
+ "navigationListener:didUpdateNoCellCoverageInfo:"
+ "notHorizontalRotation"
+ "numSamplesInAverage"
+ "omegaXRps"
+ "omegaYRps"
+ "omegaZRps"
+ "os_transaction_object is not nil"
+ "payloadsInBatch"
+ "pedestrianClass"
+ "powerlogActivity timestamp,%f,reason,%d,state,%d"
+ "powerlogActivity:event:isActive:"
+ "ptsSmoothedRoute"
+ "radiusOfCurvatureFiltered"
+ "reportId"
+ "retrieveAssetSet:usages:"
+ "samplingFrequency"
+ "scanError"
+ "sharedManager"
+ "softwareVersion"
+ "sourceTimestampToCFAbsoluteTime"
+ "sourceTimestampToMachContinuous"
+ "started"
+ "streamingHeartRateDataWatch"
+ "streamingHighFrequencyHeartRateDataWatch"
+ "stringDictionaryForKey:"
+ "taskType"
+ "temperatureFiltered"
+ "testAOIReceived"
+ "testIdentifier"
+ "testSensorAccessQuery"
+ "testSensorAccessQuery received"
+ "timeIntervalSince1970"
+ "timestampLeftHalfCrossingUs"
+ "timestampLeftZeroCrossingUs"
+ "timestampRel"
+ "timestampRightHalfCrossingUs"
+ "timestampRightZeroCrossingUs"
+ "ts0CalCount"
+ "ts0CalnA"
+ "ts0Dark0"
+ "ts0Dark1"
+ "ts0Light"
+ "ts0PdVf"
+ "ts0RxGain"
+ "ts1CalCount"
+ "ts1CalnA"
+ "ts1Dark0"
+ "ts1Dark1"
+ "ts1Light"
+ "ts1PdVf"
+ "ts1RxGain"
+ "tx0CurrentuA"
+ "tx1CurrentuA"
+ "updateCount"
+ "v32@0:8@\"GEONavigationListener\"16@\"GEONavigationListenerNoCellCoverageInfo\"24"
+ "v32@0:8d16i24B28"
+ "v32@?0{unique_ptr<CLConnection, CLConnectionDeleter>=^{CLConnection}}8{shared_ptr<CLConnectionMessage>=^{CLConnectionMessage}^{__shared_weak_count}}16"
+ "workoutRecorderAccessoryDeviceMotionConfig"
+ "workoutRecorderAudioAccessoryDeviceMotion"
+ "workoutRecorderHeartRateAccessory"
+ "workoutRecorderHeartRateSourceDevice"
+ "workoutRecorderHighFrequencyHeartRateWatch"
+ "yawDelta"
+ "{unique_ptr<AnomalySessionDetails, std::default_delete<AnomalySessionDetails>>=\"__ptr_\"^{AnomalySessionDetails}}"
+ "{unique_ptr<CLConnectionServer, std::default_delete<CLConnectionServer>>=\"__ptr_\"^{CLConnectionServer}}"
+ "{unique_ptr<CLKappaAlgFlowController, std::default_delete<CLKappaAlgFlowController>>=\"__ptr_\"^{CLKappaAlgFlowController}}"
+ "{unique_ptr<MartySessionDetails, std::default_delete<MartySessionDetails>>=\"__ptr_\"^{MartySessionDetails}}"
+ "{unique_ptr<MartySessionInfo, std::default_delete<MartySessionInfo>>=\"__ptr_\"^{MartySessionInfo}}"
+ "{unique_ptr<MartyUserInfo, std::default_delete<MartyUserInfo>>=\"__ptr_\"^{MartyUserInfo}}"
+ "{unique_ptr<const MartyCompanion::CompanionDeviceInfo, std::default_delete<const MartyCompanion::CompanionDeviceInfo>>=\"__ptr_\"^{CompanionDeviceInfo}}"
+ "{unique_ptr<const MartyCompanion::CompanionTrigger, std::default_delete<const MartyCompanion::CompanionTrigger>>=\"__ptr_\"^{CompanionTrigger}}"
+ "{unique_ptr<const MartyCompanion::CompanionUUID, std::default_delete<const MartyCompanion::CompanionUUID>>=\"__ptr_\"^{CompanionUUID}}"
- "-[CSKappaDetectionService feedSignificantUserInteraction:]"
- "-[CSMartyDetectionService feedSignificantUserInteraction:]"
- "2!"
- "@\"BPSSink\""
- "@28@0:8Q16C24"
- "APWakeReason"
- "App %s %{public}s at %{public}.1f = %{public}llu"
- "Attempting to release power assertion when there is none"
- "CSKappaCoreAnalyticsDispatchQueue"
- "CSPowerDispatchQueue"
- "CSPowerIBProtocol"
- "CSSignificantUserInteraction"
- "CSSignificantUserInteraction is null"
- "DSLPublisher"
- "Device"
- "KappaEvent"
- "No powerlogging sessionType set before session finished"
- "No powerlogging sessionType set before trigger found"
- "Power assertion failed"
- "Power assertion failed, no CPPowerAssertionCreate"
- "SUI %llu %u\n"
- "Screen unlock at %{public}.1f = %{public}llu"
- "ScreenLocked"
- "Sorted %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u"
- "TC,R,N,V_type"
- "Your iPhone detected a possible crash earlier. If you're willing to answer a few questions about the event, your answers can improve crash detection."
- "[de-AOI] missing feature mode case"
- "[de-AOI] mode,%u,hardcoded,%d,OTA-general,%d,OTA-specific,%d"
- "[de-AOI] summary,A,%{public}llu,B,%{public}u,mode,%{public}u,debug-1a,%{public}u,debug-2a,%{public}zu"
- "_activeReasons"
- "_assertString"
- "_assertionReference"
- "_biomeAppLaunchSink"
- "_biomeUnlockSink"
- "_kappaCompanion"
- "_kappaCompanionTrigger"
- "_kappaCompanionUUID"
- "_type"
- "addAOIs"
- "appLaunch"
- "bundleID"
- "cancel"
- "clearAllPowerloggingInfo"
- "clearPowerloggingInfo"
- "clearPowerloggingInfo:"
- "closed"
- "com.apple.anomalydetectiond.AppLaunch"
- "com.apple.anomalydetectiond.Unlock"
- "createPowerAssertion ref %d"
- "double release of power assertion"
- "eventBody"
- "eventBody.starting"
- "feedSignificantUserInteraction:"
- "filterWithKeyPath:value:"
- "initWithIdentifier:targetQueue:waking:"
- "initWithTimestamp:type:"
- "isStarting"
- "launched"
- "none"
- "os_transaction_object not nil before power assertion"
- "powerlogActivity reason:%d"
- "powerlogActivity:state:"
- "publisher"
- "reasonEndTimestamp"
- "reasonStartTimestamp"
- "recordSignificantUserInteraction:"
- "ref count is not zero but there is no power assertion"
- "releasePowerAssertion ref %d"
- "sendPowerlogMetrics"
- "sendPowerlogMetrics:start:end:"
- "sinkWithCompletion:receiveInput:"
- "subscribeOn:"
- "v16@?0@\"BMStoreEvent\"8"
- "v16@?0@\"BPSCompletion\"8"
- "v24@0:8@\"CSSignificantUserInteraction\"16"
- "v32@?0{unique_ptr<CLConnection, CLConnectionDeleter>={__compressed_pair<CLConnection *, CLConnectionDeleter>=^{CLConnection}}}8{shared_ptr<CLConnectionMessage>=^{CLConnectionMessage}^{__shared_weak_count}}16"
- "{\"msg%{public}.0s\":\"CSSignificantUserInteraction is null\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "{unique_ptr<AnomalySessionDetails, std::default_delete<AnomalySessionDetails>>=\"__ptr_\"{__compressed_pair<AnomalySessionDetails *, std::default_delete<AnomalySessionDetails>>=\"__value_\"^{AnomalySessionDetails}}}"
- "{unique_ptr<CLConnectionServer, std::default_delete<CLConnectionServer>>=\"__ptr_\"{__compressed_pair<CLConnectionServer *, std::default_delete<CLConnectionServer>>=\"__value_\"^{CLConnectionServer}}}"
- "{unique_ptr<CLKappaAlgFlowController, std::default_delete<CLKappaAlgFlowController>>=\"__ptr_\"{__compressed_pair<CLKappaAlgFlowController *, std::default_delete<CLKappaAlgFlowController>>=\"__value_\"^{CLKappaAlgFlowController}}}"
- "{unique_ptr<MartySessionDetails, std::default_delete<MartySessionDetails>>=\"__ptr_\"{__compressed_pair<MartySessionDetails *, std::default_delete<MartySessionDetails>>=\"__value_\"^{MartySessionDetails}}}"
- "{unique_ptr<MartySessionInfo, std::default_delete<MartySessionInfo>>=\"__ptr_\"{__compressed_pair<MartySessionInfo *, std::default_delete<MartySessionInfo>>=\"__value_\"^{MartySessionInfo}}}"
- "{unique_ptr<MartyUserInfo, std::default_delete<MartyUserInfo>>=\"__ptr_\"{__compressed_pair<MartyUserInfo *, std::default_delete<MartyUserInfo>>=\"__value_\"^{MartyUserInfo}}}"
- "{unique_ptr<const KappaCompanion::CompanionDeviceInfo, std::default_delete<const KappaCompanion::CompanionDeviceInfo>>=\"__ptr_\"{__compressed_pair<const KappaCompanion::CompanionDeviceInfo *, std::default_delete<const KappaCompanion::CompanionDeviceInfo>>=\"__value_\"^{CompanionDeviceInfo}}}"
- "{unique_ptr<const KappaCompanion::CompanionTrigger, std::default_delete<const KappaCompanion::CompanionTrigger>>=\"__ptr_\"{__compressed_pair<const KappaCompanion::CompanionTrigger *, std::default_delete<const KappaCompanion::CompanionTrigger>>=\"__value_\"^{CompanionTrigger}}}"
- "{unique_ptr<const KappaCompanion::CompanionUUID, std::default_delete<const KappaCompanion::CompanionUUID>>=\"__ptr_\"{__compressed_pair<const KappaCompanion::CompanionUUID *, std::default_delete<const KappaCompanion::CompanionUUID>>=\"__value_\"^{CompanionUUID}}}"
- "{unique_ptr<const MartyCompanion::CompanionDeviceInfo, std::default_delete<const MartyCompanion::CompanionDeviceInfo>>=\"__ptr_\"{__compressed_pair<const MartyCompanion::CompanionDeviceInfo *, std::default_delete<const MartyCompanion::CompanionDeviceInfo>>=\"__value_\"^{CompanionDeviceInfo}}}"
- "{unique_ptr<const MartyCompanion::CompanionTrigger, std::default_delete<const MartyCompanion::CompanionTrigger>>=\"__ptr_\"{__compressed_pair<const MartyCompanion::CompanionTrigger *, std::default_delete<const MartyCompanion::CompanionTrigger>>=\"__value_\"^{CompanionTrigger}}}"
- "{unique_ptr<const MartyCompanion::CompanionUUID, std::default_delete<const MartyCompanion::CompanionUUID>>=\"__ptr_\"{__compressed_pair<const MartyCompanion::CompanionUUID *, std::default_delete<const MartyCompanion::CompanionUUID>>=\"__value_\"^{CompanionUUID}}}"

```
