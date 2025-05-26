## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-63.0.1.0.0
-  __TEXT.__text: 0x2c9e88
-  __TEXT.__auth_stubs: 0x1730
-  __TEXT.__objc_stubs: 0x78c0
-  __TEXT.__init_offsets: 0xdc
-  __TEXT.__objc_methlist: 0x73b0
-  __TEXT.__gcc_except_tab: 0xa128
-  __TEXT.__cstring: 0x16594
-  __TEXT.__oslogstring: 0xa2f8
-  __TEXT.__objc_classname: 0xf58
-  __TEXT.__objc_methname: 0xa00a
-  __TEXT.__objc_methtype: 0x4b35
-  __TEXT.__const: 0x6fd8
-  __TEXT.__unwind_info: 0xa308
-  __TEXT.__eh_frame: 0x644
-  __DATA_CONST.__auth_got: 0xbb0
+77.0.0.0.0
+  __TEXT.__text: 0x2dedb4
+  __TEXT.__auth_stubs: 0x1770
+  __TEXT.__objc_stubs: 0x7c20
+  __TEXT.__init_offsets: 0xec
+  __TEXT.__objc_methlist: 0x7508
+  __TEXT.__gcc_except_tab: 0xa88c
+  __TEXT.__cstring: 0x16cd6
+  __TEXT.__oslogstring: 0xb118
+  __TEXT.__objc_classname: 0xf6a
+  __TEXT.__objc_methname: 0xa37c
+  __TEXT.__objc_methtype: 0x5208
+  __TEXT.__const: 0x72a8
+  __TEXT.__unwind_info: 0xa860
+  __TEXT.__eh_frame: 0x6bc
+  __DATA_CONST.__auth_got: 0xbd0
   __DATA_CONST.__got: 0x288
-  __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x17028
-  __DATA_CONST.__cfstring: 0x48c0
-  __DATA_CONST.__objc_classlist: 0x448
+  __DATA_CONST.__auth_ptr: 0x40
+  __DATA_CONST.__const: 0x18288
+  __DATA_CONST.__cfstring: 0x4b00
+  __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x16b0
-  __DATA_CONST.__objc_arraydata: 0x140
+  __DATA_CONST.__objc_arraydata: 0x180
   __DATA_CONST.__objc_dictobj: 0x190
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0xfb68
-  __DATA.__objc_selrefs: 0x2668
+  __DATA.__objc_const: 0xfe98
+  __DATA.__objc_selrefs: 0x2738
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x578
-  __DATA.__objc_superrefs: 0x3e0
-  __DATA.__objc_ivar: 0x7ac
-  __DATA.__objc_data: 0x2ad0
+  __DATA.__objc_classrefs: 0x580
+  __DATA.__objc_superrefs: 0x3e8
+  __DATA.__objc_ivar: 0x7f8
+  __DATA.__objc_data: 0x2b20
   __DATA.__data: 0x1f30
-  __DATA.__bss: 0x30b8
+  __DATA.__bss: 0x3118
   __DATA.__common: 0xb94
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13464
-  Symbols:   525
-  CStrings:  7449
+  Functions: 13784
+  Symbols:   529
+  CStrings:  7613
 
Symbols:
+ __ZN2PB6ReaderC1EPKhm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
+ __ZNSt3__16__sortIRNS_6__lessIffEEPfEEvT0_S5_T_
+ __ZNSt3__16__sortIRNS_6__lessIyyEEPyEEvT0_S5_T_
CStrings:
+ "\x03\x16\x12\x81\x13\x13\xf0!\xf0#3"
+ "\x12B\x11%\x11"
+ "-[CSAnomalyEventService sendMartyCompanionTrigger:]"
+ "-[CSAnomalyEventService startRecording]"
+ "-[CSAnomalyEventService triggered:]"
+ "-[CSKappaDetectionService sendForceTriggerProtobuf:]"
+ "-[CSKappaDetectionService setRecording:withUUID:]"
+ "-[CSKappaDetectionService start]"
+ "/Library/Caches/com.apple.xbs/Sources/CoreSafety/SafetyAlgorithms/CSAnomalyEventService.mm"
+ "1P %d 3P %d"
+ "@100@0:8Q16C24f28f32C36S40c44c48c52c56c60Q64[3 ]72C80C84S88Q92"
+ "CSArmedClients"
+ "CSMartyTokenCount"
+ "CSMartyTokenCountDefault"
+ "CSMartyTokenReplenishPeriod"
+ "CSMartyTokenReplenishTimestamp"
+ "ForceDeescalateMAP"
+ "KappaFeaturesAlgPeakDetectorMAP"
+ "T^{TriggerSample=CCSIQffcccccQ[3 ]CCSQ},R,N"
+ "Ti,N,V_enableMode"
+ "Ti,N,V_kappaArmedSeconds"
+ "Ti,N,V_martyArmedSeconds"
+ "UUID cannot be nil"
+ "Using new protobuf companion trigger session UUID %{public}s %{public}@"
+ "[MAP] config-1,%d"
+ "[MAP] config-1,%f,config-2,%llu,config-3,%d,config-4,%llu,config-5,%f,config-6,%f,config-7,%f,config-8,%f,config-9,%llu,config-10,%f"
+ "[MAP] reset"
+ "[MAP] summary,A,%{public}d,B,%{public}llu,config-1,%{public}f,config-2,%{public}llu,config-3,%{public}d,config-4,%{public}llu,config-5,%{public}f,config-6,%{public}f,config-7,%{public}f,config-8,%{public}f,config-9,%{public}llu,config-10,%{public}f,debug-1,%{public}d,debug-2,%{public}llu,debug-3,%{public}f,debug-4,%{public}llu,debug-5,%{public}llu,debug-6,%{public}d\n"
+ "[SC] AlgBlock summary,A,%{public}llu,B,%{public}llu,C,%{public}d,D,%{public}d,E,%{public}d,F,%{public}d,G,%{public}d,H,%{public}d,I,%{public}d,J,%{public}d,K,%{public}d,L,%{public}d,M,%{public}d,config-1,%{public}f,config-2,%{public}f,config-3,%{public}d,config-4,%{public}d,config-5,%{public}d,config-6,%{public}f,config-7,%{public}f,config-8,%{public}f,config-9,%{public}f,config-10,%{public}d,config-11,%{public}d,config-12,%{public}f,config-13,%{public}d,config-14,%{public}d,config-15,%{public}f,config-16,%{public}f,config-17,%{public}d,config-18,%{public}d,config-19,%{public}f,config-20,%{public}d,config-21,%{public}d,debug-1a,%{public}d,debug-1b,%{public}d,debug-1c,%{public}d,debug-1d,%{public}d,debug-1e,%{public}d,debug-1f,%{public}d,debug-1g,%{public}d,debug-1h,%{public}d,debug-1i,%{public}d,debug-1j,%{public}d,debug-1k,%{public}d,debug-1l,%{public}llu,debug-1m,%{public}d,debug-1n,%{public}d,debug-1o,%{public}d,debug-2a,%{public}d,debug-2b,%{public}d,debug-2c,%{public}d,debug-2d,%{public}d,debug-3a,%{public}d,debug-3b,%{public}f,debug-3c,%{public}f,debug-3d,%{public}d,debug-4a,%{public}d,debug-4b,%{public}d,debug-4c,%{public}f,debug-4d,%{public}d,debug-4e,%{public}llu,debug-5a,%{public}d,debug-5b,%{public}d,debug-6a,%{public}f,debug-6b,%{public}f,debug-6c,%{public}f,debug-6d,%{public}f,debug-7a,%{public}d,debug-7b,%{public}d,debug-7c,%{public}d,debug-8a,%{public}d,debug-8b,%{public}d,debug-9a,%{public}d,debug-9b,%{public}d,debug-9c,%{public}d,debug-10a,%{public}d,debug-10b,%{public}d,debug-10c,%{public}d,debug-11a,%{public}d,debug-12a,%{public}d,debug-12b,%{public}d,debug-12c,%{public}llu,debug-12d,%{public}llu\n"
+ "[SC] force %d %d %d %d %d is %d %d %d %d %d %d %d %d %d %d %d %d %d"
+ "^{TriggerSample=CCSIQffcccccQ[3 ]CCSQ}16@0:8"
+ "_convertToKappa"
+ "_enableMode"
+ "_kappaArmedSeconds"
+ "_kappaCompanion"
+ "_kappaCompanionTrigger"
+ "_kappaCompanionUUID"
+ "_martyArmedSeconds"
+ "_martyCompanion"
+ "_martyCompanionTrigger"
+ "_martyCompanionUUID"
+ "_sessionActive"
+ "_sessionNum"
+ "_stopMartyCollection"
+ "_stopMartyDetection"
+ "abortSession"
+ "aborting session"
+ "accelPeakThreshold"
+ "acquiring kappa token"
+ "acquiring marty token"
+ "allMaxNormTimestamps"
+ "allMaxNormValues"
+ "clients %d %d %d"
+ "companionAopTs"
+ "companionEnableMode"
+ "companionKappaArmedSeconds"
+ "companionKappaDeviceType"
+ "companionKappaTokenCount"
+ "companionMartyArmedSeconds"
+ "companionMartyDeviceType"
+ "companionMartyTokenCount"
+ "const T &CMQueue<unsigned long long>::operator[](const size_t) const [T = unsigned long long]"
+ "converting a marty session into a kappa one"
+ "decel"
+ "device cannot collect data"
+ "deviceHardware"
+ "deviceModel"
+ "enableMode"
+ "error %{public}@"
+ "failed to get armed clients state"
+ "feed sorted samples type %d"
+ "finish session %d"
+ "finishSession"
+ "firstOrThirdPartyEnabled"
+ "firstTimestampMAPDecision"
+ "forcefully restarting the session; any recordings will be discarded"
+ "fractionAboveThreshold"
+ "horizontalAngleUncertainty"
+ "horizontalAngleUncertaintyUnfiltered"
+ "horizontalDistance"
+ "hsm is nil"
+ "ignoring post driving kappa trigger in action"
+ "impact"
+ "initWithTimestamp:meta:decel:impact:path:armedSec:motionHint:gpsHint:basebandHint:wifiHint:btHint:lastValidImuTimestamp:vehicleProbabilityLongTermMean:martyPath:enableMode:martyArmedSec:companionAopTs:"
+ "invalid kappa device type detected"
+ "invalid path %d/%d for enable mode %d"
+ "invalid trigger"
+ "isAboveBelow"
+ "isAboveBelowMessageShowing"
+ "isFreeFallDetectedEpoch"
+ "isIdle"
+ "isIn(_idle)"
+ "isIn(_reading)"
+ "isMAPDetected"
+ "isMAPFPDecided"
+ "kappaArmedSeconds"
+ "kappaPeakDetectorMapMagTimestamps"
+ "kappaPeakDetectorMapResult"
+ "kappaTokenCount"
+ "kappaTriggerPathBitmap"
+ "lastTimestampMAPDecision"
+ "lastValidImuTimestamp"
+ "likelihoodAboveThreshold"
+ "magnitudePercentileThreshold"
+ "magnitudePeriodicityLowerPercentile"
+ "magnitudePeriodicityUpperPercentile"
+ "martyArmedSeconds"
+ "martyDeviceType"
+ "martyPath"
+ "martyTokenCount"
+ "martyTriggerPathBitmap"
+ "maxNormTimestamp"
+ "maxNormValue"
+ "minNumPeaks"
+ "no marty companion"
+ "not authorized for collection"
+ "numDeescalationMAP"
+ "peakMagnitudePercentileDiff"
+ "peakSeparation"
+ "peakTimeDeltaPercentileDiff"
+ "peakToPeakMinimumSeparation"
+ "peakToPeakSeparationThreshold"
+ "precisionFindingVerticalState"
+ "receiveCompanionUUID:"
+ "receiveDeviceInfoProtobuf:"
+ "receiveForceTriggerProtobuf:"
+ "receiveMartyCompanionTrigger:"
+ "receiveMartyDeviceInfo:"
+ "receiveMartyUUID:"
+ "received kappa device info %{private}d %{private}s %{private}d %{private}d %{private}d %{private}d %{private}d %{private}d %{private}d"
+ "receiving kappa companion uuid %{public}s"
+ "receiving kappa device info %{private}d %{private}s %{private}d %{private}d %{private}d %{private}d %{private}d %{private}d %{private}d"
+ "receiving kappa trigger info %{private}d %{private}d %{private}d %{private}d %{private}llu %{private}f %{private}f %{private}d %{private}d %{private}d %{private}d %{private}d %{private}llu %{private}f %{private}f %{private}f %{private}d %{private}d%{private}d %{private}llu"
+ "receiving marty companion uuid %{public}s"
+ "receiving marty device info %{private}d %{private}s %{private}d %{private}d %{private}d %{private}d %{private}d %{private}d %{private}d"
+ "receiving marty trigger info %{private}d %{private}d %{private}d %{private}d %{private}llu %{private}f %{private}f %{private}d %{private}d %{private}d %{private}d %{private}d %{private}llu %{private}f %{private}f %{private}f %{private}d %{private}d%{private}d %{private}llu"
+ "recording details can only be set in idle"
+ "recording details may only be set in idle"
+ "restartSession can only happen in reading"
+ "restartSessionInternal"
+ "rmsSN"
+ "sendCompanionUUID:"
+ "sendDeviceInfo:"
+ "sendDeviceInfoProtobuf"
+ "sendForceTriggerProtobuf:"
+ "sendMartyCompanionTrigger:"
+ "sendMartyDeviceInfo"
+ "sendMartyUUID:"
+ "sendUUID:"
+ "sending kappa companion uuid %{public}s"
+ "sending kappa device info %{private}d %{private}s %{private}d %{private}d %{private}d %{private}d %{private}d %{private}d %{private}d"
+ "sending kappa trigger info %{private}d %{private}d %{private}d %{private}d %{private}llu %{private}f %{private}f %{private}d %{private}d %{private}d %{private}d %{private}d %{private}llu %{private}f %{private}f %{private}f %{private}d %{private}d%{private}d %{private}llu"
+ "sending marty companion uuid %{public}s"
+ "sending marty device info %{private}d %{private}s %{private}d %{private}d %{private}d %{private}d %{private}d %{private}d %{private}d"
+ "sending marty trigger info %{private}d %{private}d %{private}d %{private}d %{private}llu %{private}f %{private}f %{private}d %{private}d %{private}d %{private}d %{private}d %{private}llu %{private}f %{private}f %{private}f %{private}d %{private}d%{private}d %{private}llu"
+ "set recording state %d %d %d %d"
+ "setEnableMode:"
+ "setKappaArmedSeconds:"
+ "setMartyArmedSeconds:"
+ "setRecording"
+ "setRecording:withUUID:"
+ "setUploader:"
+ "shouldDeescalateBecauseOfMAPFPCondition"
+ "starting session %d type=%d"
+ "stopping collection"
+ "stopping detection"
+ "timePercentileDiffThreshold"
+ "timePeriodicityLowerPercentile"
+ "timePeriodicityUpperPercentile"
+ "trigger path %d marty path %d enabledMode %d"
+ "unhandled message %d"
+ "v152@0:8{KappaSessionDetails=fCiiiiiiiifiiiiiiiiiiiiiiiBiQQQ}16"
+ "vehicleProbabilityLongTermMean"
+ "verticalDistance"
+ "{\"msg%{public}.0s\":\"UUID cannot be nil\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"hsm is nil\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"invalid trigger\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"recording details can only be set in idle\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"restartSession can only happen in reading\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{KappaSessionDetails=\"serverConfigVersion\"f\"trigger_bitmap\"C\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"coarseLat\"i\"coarseLong\"i\"sunElevation\"f\"signalEnvironment\"i\"gpsCount\"i\"numDeescalationStatic\"i\"numDeescalationMoving\"i\"numDeescalationSteps\"i\"numDeescalationQuiescence\"i\"numDeescalationAutocorrelation\"i\"numDeescalationTriggerCluster\"i\"numDeescalationSkiingBaroAndAudio\"i\"numDeescalationSkiLift\"i\"numDeescalationUsha\"i\"numDeescalationAOI\"i\"numDeescalationTwoLevel\"i\"numDeescalationDistToRoad\"i\"numDeescalationMAP\"i\"latchedHighSpeedCrash\"B\"numSevereCrashes\"i\"severeCrashAOPTimestamp\"Q\"algsEndTimestamp\"Q\"crashTimestamp\"Q}"
+ "{TriggerSample=\"meta\"C\"path\"C\"armedSec\"S\"rmsSN\"I\"timestamp\"Q\"decel\"f\"impact\"f\"motionHint\"c\"gpsHint\"c\"basebandHint\"c\"wifiHint\"c\"btHint\"c\"lastValidImuTimestamp\"Q\"vehicleProbabilityLongTermMean\"[3 ]\"martyPath\"C\"enableMode\"C\"martyArmedSec\"S\"companionAopTs\"Q}"
+ "{unique_ptr<const KappaCompanion::CompanionDeviceInfo, std::default_delete<const KappaCompanion::CompanionDeviceInfo>>=\"__ptr_\"{__compressed_pair<const KappaCompanion::CompanionDeviceInfo *, std::default_delete<const KappaCompanion::CompanionDeviceInfo>>=\"__value_\"^{CompanionDeviceInfo}}}"
+ "{unique_ptr<const KappaCompanion::CompanionTrigger, std::default_delete<const KappaCompanion::CompanionTrigger>>=\"__ptr_\"{__compressed_pair<const KappaCompanion::CompanionTrigger *, std::default_delete<const KappaCompanion::CompanionTrigger>>=\"__value_\"^{CompanionTrigger}}}"
+ "{unique_ptr<const KappaCompanion::CompanionUUID, std::default_delete<const KappaCompanion::CompanionUUID>>=\"__ptr_\"{__compressed_pair<const KappaCompanion::CompanionUUID *, std::default_delete<const KappaCompanion::CompanionUUID>>=\"__value_\"^{CompanionUUID}}}"
+ "{unique_ptr<const MartyCompanion::CompanionDeviceInfo, std::default_delete<const MartyCompanion::CompanionDeviceInfo>>=\"__ptr_\"{__compressed_pair<const MartyCompanion::CompanionDeviceInfo *, std::default_delete<const MartyCompanion::CompanionDeviceInfo>>=\"__value_\"^{CompanionDeviceInfo}}}"
+ "{unique_ptr<const MartyCompanion::CompanionTrigger, std::default_delete<const MartyCompanion::CompanionTrigger>>=\"__ptr_\"{__compressed_pair<const MartyCompanion::CompanionTrigger *, std::default_delete<const MartyCompanion::CompanionTrigger>>=\"__value_\"^{CompanionTrigger}}}"
+ "{unique_ptr<const MartyCompanion::CompanionUUID, std::default_delete<const MartyCompanion::CompanionUUID>>=\"__ptr_\"{__compressed_pair<const MartyCompanion::CompanionUUID *, std::default_delete<const MartyCompanion::CompanionUUID>>=\"__value_\"^{CompanionUUID}}}"
- "\t\x12\x81\x13\x13\xf0!\xf0#\x13"
- "\x11\x16\x11"
- "%{public}@ %{public}@"
- "-[CSKappaDetectionService startRecording]"
- "@80@0:8Q16C24f28f32C36S40c44c48c52c56c60Q64[3 ]72"
- "T^{TriggerSample=CCSIQffcccccQ[3 ]},R,N"
- "[SC] AlgBlock summary,A,%{public}llu,B,%{public}llu,C,%{public}d,D,%{public}d,E,%{public}d,F,%{public}d,G,%{public}d,H,%{public}d,I,%{public}d,J,%{public}d,K,%{public}d,L,%{public}d,config-1,%{public}f,config-2,%{public}f,config-3,%{public}d,config-4,%{public}d,config-5,%{public}d,config-6,%{public}f,config-7,%{public}f,config-8,%{public}f,config-9,%{public}f,config-10,%{public}d,config-11,%{public}d,config-12,%{public}f,config-13,%{public}d,config-14,%{public}d,config-15,%{public}f,config-16,%{public}f,config-17,%{public}d,config-18,%{public}d,config-19,%{public}f,config-20,%{public}d,config-21,%{public}d,debug-1a,%{public}d,debug-1b,%{public}d,debug-1c,%{public}d,debug-1d,%{public}d,debug-1e,%{public}d,debug-1f,%{public}d,debug-1g,%{public}d,debug-1h,%{public}d,debug-1i,%{public}d,debug-1j,%{public}d,debug-1k,%{public}d,debug-1l,%{public}llu,debug-1m,%{public}d,debug-1n,%{public}d,debug-2a,%{public}d,debug-2b,%{public}d,debug-2c,%{public}d,debug-2d,%{public}d,debug-3a,%{public}d,debug-3b,%{public}f,debug-3c,%{public}f,debug-3d,%{public}d,debug-4a,%{public}d,debug-4b,%{public}d,debug-4c,%{public}f,debug-4d,%{public}d,debug-4e,%{public}llu,debug-5a,%{public}d,debug-5b,%{public}d,debug-6a,%{public}f,debug-6b,%{public}f,debug-6c,%{public}f,debug-6d,%{public}f,debug-7a,%{public}d,debug-7b,%{public}d,debug-7c,%{public}d,debug-8a,%{public}d,debug-8b,%{public}d,debug-9a,%{public}d,debug-9b,%{public}d,debug-9c,%{public}d,debug-10a,%{public}d,debug-10b,%{public}d,debug-10c,%{public}d,debug-11a,%{public}d\n"
- "[SC] force %d %d %d %d %d is %d %d %d %d %d %d %d %d %d %d %d %d"
- "^{TriggerSample=CCSIQffcccccQ[3 ]}16@0:8"
- "_mslRecording is nil, recording was forcefully stopped"
- "acquire token %d"
- "armedSecond"
- "cannot start when a recording is in progress"
- "device is not authorized for data collection"
- "horizontalAngleAccuracy"
- "horizontalAngleAccuracyUnfiltered"
- "ignoring post driving trigger in action"
- "initWithTimestamp:meta:decel:impact:path:armedSec:motionHint:gpsHint:basebandHint:wifiHint:btHint:lastValidImuTimestamp:vehicleProbabilityLongTermMean:"
- "recording not started"
- "scanning %{public}@"
- "specified key not present %{public}@ %{public}@ using-top level"
- "token count %d"
- "tokenCount"
- "using config %{public}@"
- "using top level dictionary"
- "v152@0:8{KappaSessionDetails=fCiiiiiiiifiiiiiiiiiiiiiiBiQQQ}16"
- "{\"msg%{public}.0s\":\"cannot start when a recording is already in progress\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "{KappaSessionDetails=\"serverConfigVersion\"f\"trigger_bitmap\"C\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"coarseLat\"i\"coarseLong\"i\"sunElevation\"f\"signalEnvironment\"i\"gpsCount\"i\"numDeescalationStatic\"i\"numDeescalationMoving\"i\"numDeescalationSteps\"i\"numDeescalationQuiescence\"i\"numDeescalationAutocorrelation\"i\"numDeescalationTriggerCluster\"i\"numDeescalationSkiingBaroAndAudio\"i\"numDeescalationSkiLift\"i\"numDeescalationUsha\"i\"numDeescalationAOI\"i\"numDeescalationTwoLevel\"i\"numDeescalationDistToRoad\"i\"latchedHighSpeedCrash\"B\"numSevereCrashes\"i\"severeCrashAOPTimestamp\"Q\"algsEndTimestamp\"Q\"crashTimestamp\"Q}"
- "{TriggerSample=\"meta\"C\"path\"C\"armedSec\"S\"rmsSN\"I\"timestamp\"Q\"decel\"f\"impact\"f\"motionHint\"c\"gpsHint\"c\"basebandHint\"c\"wifiHint\"c\"btHint\"c\"lastValidImuTimestamp\"Q\"vehicleProbabilityLongTermMean\"[3 ]}"

```
