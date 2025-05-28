## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-83.0.5.0.0
-  __TEXT.__text: 0x2de2ec
+92.0.1.0.1
+  __TEXT.__text: 0x2e90f0
   __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_stubs: 0x80e0
-  __TEXT.__objc_methlist: 0x7860
-  __TEXT.__objc_methname: 0xa9a6
-  __TEXT.__cstring: 0x170a8
-  __TEXT.__objc_classname: 0xfb0
-  __TEXT.__objc_methtype: 0x559a
-  __TEXT.__const: 0x73a7
-  __TEXT.__gcc_except_tab: 0xb540
-  __TEXT.__oslogstring: 0xb8d4
-  __TEXT.__unwind_info: 0xac98
+  __TEXT.__objc_stubs: 0x8160
+  __TEXT.__objc_methlist: 0x7908
+  __TEXT.__objc_methname: 0xaa4a
+  __TEXT.__cstring: 0x17398
+  __TEXT.__objc_classname: 0xfc2
+  __TEXT.__objc_methtype: 0x54c3
+  __TEXT.__const: 0x74b7
+  __TEXT.__gcc_except_tab: 0xb4ec
+  __TEXT.__oslogstring: 0xb9ec
+  __TEXT.__unwind_info: 0xad7c
   __TEXT.__eh_frame: 0x6a8
   __DATA_CONST.__auth_got: 0xb50
-  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__got: 0x400
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x1cbd8
-  __DATA_CONST.__cfstring: 0x5060
-  __DATA_CONST.__objc_classlist: 0x460
+  __DATA_CONST.__const: 0x1c740
+  __DATA_CONST.__cfstring: 0x5140
+  __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_classrefs: 0x598
+  __DATA_CONST.__objc_superrefs: 0x3f0
   __DATA_CONST.__objc_intobj: 0x16e0
   __DATA_CONST.__objc_arraydata: 0x1a0
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x1b8
-  __DATA.__objc_const: 0x10610
-  __DATA.__objc_selrefs: 0x2838
-  __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x590
-  __DATA.__objc_superrefs: 0x3e8
-  __DATA.__objc_ivar: 0x8a0
-  __DATA.__objc_data: 0x2bc0
+  __DATA.__objc_const: 0x10848
+  __DATA.__objc_selrefs: 0x2868
+  __DATA.__objc_ivar: 0x8b0
+  __DATA.__objc_data: 0x2c10
   __DATA.__data: 0x1fc0
   __DATA.__bss: 0x218
   __DATA.__common: 0x8

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14157
-  Symbols:   508
-  CStrings:  7780
+  Functions: 14317
+  Symbols:   509
+  CStrings:  7844
 
Symbols:
+ __ZNSt3__119piecewise_constructE
CStrings:
+ "\x16\x12\x11E\x11"
+ "\x17"
+ "\x184"
+ "%u HzSamples %llu"
+ "-[CSAnomalyEventService onCompanionConnectionStatusUpdate:cftime:]"
+ "@146@0:8Q16C24f28f32C36S40c44c48c52c56c60Q64[3 ]72C80C84S88Q92 100 102 104C106C110*114f122f126C130B134S138C142"
+ "@28@0:8Q16i24"
+ "@32@0:8Q16S24C28"
+ "@64@0:8@16@24Q32Q40d48@56"
+ "CSCompanionStatus"
+ "CSCompanionStatus status=%d t=%llu"
+ "CSSPUSafetyHertzSample"
+ "HertzFp"
+ "No _aop to tell about companion"
+ "Sorted %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u"
+ "T@\"NSString\",?,R,C"
+ "T@?,C,N,V_companionStatusHandler"
+ "TQ,V_registrationPeriodInSeconds"
+ "T^{?=QSC},R,N"
+ "T^{?=Qi},R,N"
+ "T^{TriggerSample=CCSIQffcccccQ[3 ]CCSQC[16c]ffCCBS   C},R,N"
+ "^{?=QSC}16@0:8"
+ "^{?=Qi}16@0:8"
+ "^{TriggerSample=CCSIQffcccccQ[3 ]CCSQC[16c]ffCCBS   C}16@0:8"
+ "_aop != nullptr"
+ "_apTriggerTimestamp"
+ "_companionStatusHandler"
+ "_registrationPeriodInSeconds"
+ "accessoryHeartRate"
+ "accessoryPPG"
+ "accessorySleepStateConfidenceEpoch"
+ "accessorySleepStateUpdate"
+ "altimeter"
+ "altitudeAngleConfidence"
+ "apTriggerTimestamp"
+ "azimuthAngleConfidence"
+ "code"
+ "companionStatusHandler"
+ "companionStatusHandler is nil"
+ "currentAudioWindowMeanFirstTrigger"
+ "currentWindowMean"
+ "dark0"
+ "dark1"
+ "dark2"
+ "dark3"
+ "dramDurationMs"
+ "frameNum"
+ "historical loudness stats %f / %f / %f / %i"
+ "igneousPath"
+ "initWithSpoolerFolder:serverConfiguration:registrationPeriodInSeconds:retentionPeriodInSeconds:outOfBandMetadataTimeout:defaultsKeyPostfix:"
+ "initWithTimestamp:code:"
+ "initWithTimestamp:dramDurationMs:vehicularFlags:"
+ "initWithTimestamp:meta:decel:impact:path:armedSec:motionHint:gpsHint:basebandHint:wifiHint:btHint:lastValidImuTimestamp:vehicleProbabilityLongTermMean:martyPath:enableMode:martyArmedSec:companionAopTs:maxMeanTenMinPreTrigger:lastCompleted15sWindowMean:currentWindowMean:numMaxEnvelopes:igneousPath:igneousGUID:martyImpactMagnitude:martyRotationMagnitude:overrideMode:martyIsBicycle:martyArmedSecBicycle:locallyArmed:"
+ "lastAuxTimeStampMicroSeconds"
+ "lastCompleted15sWindowMean"
+ "lastCompletedAudio15sWindowMeanFirstTrigger"
+ "lastRingSensorTimeStampMicroSeconds"
+ "ledCurrent"
+ "light0"
+ "light1"
+ "locallyArmed"
+ "locallyArmedBitmap"
+ "maxAudioMeanTenMinPreFirstTrigger"
+ "maxMeanTenMinPreTrigger"
+ "mismatch between report and nsdata sizes %d %d"
+ "numAudioMaxEnvelopesFirstTrigger"
+ "numMaxEnvelopes"
+ "onCompanionConnectionStatusUpdate %d"
+ "onCompanionConnectionStatusUpdate:cftime:"
+ "overrideArmedBitmap"
+ "overrideMode"
+ "pencilFusionReplayResult"
+ "positionConfidence"
+ "qSP"
+ "recordCompanionStatus:"
+ "recordSafetyHertzSample:"
+ "registrationPeriodInSeconds"
+ "rxGain"
+ "safetyCompanionStatus"
+ "safetyHertzSample"
+ "setCompanionStatusHandler:"
+ "setRegistrationPeriodInSeconds:"
+ "temperatureGyro"
+ "temperatureGyroBias"
+ "timeStampMicroSeconds"
+ "trigger %{public}llu path %{public}d size %{public}d metrics %{public}f,%{public}f,%{public}f,%{public}d"
+ "triggered: trigger path %d marty path %d igneous path %d enabledMode %d overrideMode %d locallyArmed %d"
+ "v20@?0d8i16"
+ "v24@0:8@\"CSCompanionStatus\"16"
+ "v24@0:8@\"CSSPUSafetyHertzSample\"16"
+ "{\"msg%{public}.0s\":\"No _aop to tell about companion\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{?=\"timestamp\"Q\"code\"i}"
+ "{?=\"timestamp\"Q\"dramDurationMs\"S\"vehicularFlags\"C}"
+ "{TriggerSample=\"meta\"C\"path\"C\"armedSec\"S\"rmsSN\"I\"timestamp\"Q\"decel\"f\"impact\"f\"motionHint\"c\"gpsHint\"c\"basebandHint\"c\"wifiHint\"c\"btHint\"c\"lastValidImuTimestamp\"Q\"vehicleProbabilityLongTermMean\"[3 ]\"martyPath\"C\"enableMode\"C\"martyArmedSec\"S\"companionAopTs\"Q\"igneousPath\"C\"igneousGUID\"[16c]\"martyImpactMagnitude\"f\"martyRotationMagnitude\"f\"locallyArmed\"C\"overrideMode\"C\"martyIsBicycle\"B\"martyArmedSecBicycle\"S\"maxMeanTenMinPreTrigger\" \"lastCompleted15sWindowMean\" \"currentWindowMean\" \"numMaxEnvelopes\"C}"
- "\x16"
- "\x16\x12\x11%\x11"
- "\x18$"
- "%u DOT, sn = %llu, %u %u"
- "-[CSKappaDetectionService feedDirectionOfTravel:]"
- "-[CSMartyDetectionService feedDirectionOfTravel:]"
- "@120@0:8Q16f24f28f32f36f40f44f48f52I56f60f64f68f72f76Q80Q88Q96[3[3f]]104[3[3f]]112"
- "@132@0:8Q16C24f28f32C36S40c44c48c52c56c60Q64[3 ]72C80C84S88Q92C100*104f112f116C120B124S128"
- "@56@0:8@16@24Q32d40@48"
- "CSSPUDirectionOfTravel"
- "CSSPUDirectionOfTravel is null"
- "DotFp"
- "Sorted %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u, %u"
- "T^{DOTSample=QffffffffIffffIQQQ[3[3f]][3[3f]]},R,N"
- "T^{TriggerSample=CCSIQffcccccQ[3 ]CCSQC[16c]ffCBS},R,N"
- "^{DOTSample=QffffffffIffffIQQQ[3[3f]][3[3f]]}16@0:8"
- "^{TriggerSample=CCSIQffcccccQ[3 ]CCSQC[16c]ffCBS}16@0:8"
- "absoluteTimestamp"
- "directionOfTravel %llu %u %u\n"
- "feedDirectionOfTravel:"
- "initWithSpoolerFolder:serverConfiguration:retentionPeriodInSeconds:outOfBandMetadataTimeout:defaultsKeyPostfix:"
- "initWithTimestamp:combinedX:combinedY:combinedZ:combinedUnc:inertialApproachX:inertialApproachY:inertialApproachZ:inertialApproachUnc:inerAccelCount:sagittalApproachX:sagittalApproachY:sagittalApproachZ:sagittalApproachUnc:sagittalCount:previousTimestamp:previousTimeAccel:previousTimeSag:sagittalApproach:inerAccelApproach:"
- "initWithTimestamp:meta:decel:impact:path:armedSec:motionHint:gpsHint:basebandHint:wifiHint:btHint:lastValidImuTimestamp:vehicleProbabilityLongTermMean:martyPath:enableMode:martyArmedSec:companionAopTs:igneousPath:igneousGUID:martyImpactMagnitude:martyRotationMagnitude:overrideMode:martyIsBicycle:martyArmedSecBicycle:"
- "not authorized for collection"
- "recordDirectionOfTravel:"
- "trigger path %d marty path %d igneous path %d enabledMode %d"
- "v24@0:8@\"CSSPUDirectionOfTravel\"16"
- "{\"msg%{public}.0s\":\"CSSPUDirectionOfTravel is null\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "{DOTSample=\"timestamp\"Q\"combinedX\"f\"combinedY\"f\"combinedZ\"f\"combinedUnc\"f\"inertialApproachX\"f\"inertialApproachY\"f\"inertialApproachZ\"f\"inertialApproachUnc\"f\"inerAccelCount\"I\"sagittalApproachX\"f\"sagittalApproachY\"f\"sagittalApproachZ\"f\"sagittalApproachUnc\"f\"sagittalCount\"I\"previousTimestamp\"Q\"previousTimeAccel\"Q\"previousTimeSag\"Q\"sagittalApproach\"[3[3f]]\"inerAccelApproach\"[3[3f]]}"
- "{TriggerSample=\"meta\"C\"path\"C\"armedSec\"S\"rmsSN\"I\"timestamp\"Q\"decel\"f\"impact\"f\"motionHint\"c\"gpsHint\"c\"basebandHint\"c\"wifiHint\"c\"btHint\"c\"lastValidImuTimestamp\"Q\"vehicleProbabilityLongTermMean\"[3 ]\"martyPath\"C\"enableMode\"C\"martyArmedSec\"S\"companionAopTs\"Q\"igneousPath\"C\"igneousGUID\"[16c]\"martyImpactMagnitude\"f\"martyRotationMagnitude\"f\"overrideMode\"C\"martyIsBicycle\"B\"martyArmedSecBicycle\"S}"

```
