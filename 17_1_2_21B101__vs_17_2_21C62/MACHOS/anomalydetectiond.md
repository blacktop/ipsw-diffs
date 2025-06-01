## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-77.0.0.0.0
-  __TEXT.__text: 0x2dedb4
+83.0.0.0.0
+  __TEXT.__text: 0x2df9a4
   __TEXT.__auth_stubs: 0x1770
-  __TEXT.__objc_stubs: 0x7c20
-  __TEXT.__init_offsets: 0xec
-  __TEXT.__objc_methlist: 0x7508
-  __TEXT.__gcc_except_tab: 0xa88c
-  __TEXT.__cstring: 0x16cd6
-  __TEXT.__oslogstring: 0xb118
-  __TEXT.__objc_classname: 0xf6a
-  __TEXT.__objc_methname: 0xa37c
-  __TEXT.__objc_methtype: 0x5208
-  __TEXT.__const: 0x72a8
-  __TEXT.__unwind_info: 0xa860
-  __TEXT.__eh_frame: 0x6bc
+  __TEXT.__objc_stubs: 0x7fc0
+  __TEXT.__init_offsets: 0xf8
+  __TEXT.__objc_methlist: 0x77f8
+  __TEXT.__gcc_except_tab: 0xb174
+  __TEXT.__cstring: 0x172bf
+  __TEXT.__oslogstring: 0xb5a2
+  __TEXT.__objc_classname: 0xfbb
+  __TEXT.__objc_methname: 0xa87c
+  __TEXT.__objc_methtype: 0x53f0
+  __TEXT.__const: 0x73b8
+  __TEXT.__unwind_info: 0xaba8
+  __TEXT.__eh_frame: 0x6d0
   __DATA_CONST.__auth_got: 0xbd0
   __DATA_CONST.__got: 0x288
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x18288
-  __DATA_CONST.__cfstring: 0x4b00
-  __DATA_CONST.__objc_classlist: 0x450
+  __DATA_CONST.__const: 0x18570
+  __DATA_CONST.__cfstring: 0x4f40
+  __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x120
+  __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x16b0
+  __DATA_CONST.__objc_intobj: 0x16e0
   __DATA_CONST.__objc_arraydata: 0x180
   __DATA_CONST.__objc_dictobj: 0x190
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0xfe98
-  __DATA.__objc_selrefs: 0x2738
+  __DATA.__objc_const: 0x105a0
+  __DATA.__objc_selrefs: 0x2808
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x580
+  __DATA.__objc_classrefs: 0x590
   __DATA.__objc_superrefs: 0x3e8
-  __DATA.__objc_ivar: 0x7f8
-  __DATA.__objc_data: 0x2b20
-  __DATA.__data: 0x1f30
-  __DATA.__bss: 0x3118
+  __DATA.__objc_ivar: 0x88c
+  __DATA.__objc_data: 0x2bc0
+  __DATA.__data: 0x1fc0
+  __DATA.__bss: 0x3190
   __DATA.__common: 0xb94
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E5D994E4-6DC4-3F63-913A-E1993513812F
-  Functions: 13784
+  UUID: BF08DCCE-65C6-3F6C-8F38-4F20FD052062
+  Functions: 14000
   Symbols:   529
-  CStrings:  8213
+  CStrings:  8381
 
CStrings:
+ "\x01\xf0\xa4\x11"
+ "\x03\x16\x12\x81\x13\x13\xf0!\xf0\"C"
+ "\x06"
+ "\a\x12\x12q2"
+ "\x12"
+ "\x16\x12\x11%\x11"
+ "\x18$"
+ "-[CSKappaDetectionService consumeSampleArray:]"
+ "-[CSMartyDetectionService feedAccel800:]"
+ "-[CSMartyDetectionService feedAccel:]"
+ "-[CSMartyDetectionService feedDeviceMotion:]"
+ "-[CSMartyDetectionService feedDirectionOfTravel:]"
+ "-[CSMartyDetectionService feedGPS:]"
+ "-[CSMartyDetectionService feedHgAccel:]"
+ "-[CSMartyDetectionService feedKappaTrigger:]"
+ "-[CSMartyDetectionService feedMag:]"
+ "-[CSMartyDetectionService feedPressure:]"
+ "-[CSMartyDetectionService feedRoads:]"
+ "-[CSMartyDetectionService feedSignificantUserInteraction:]"
+ "-[CSMartyDetectionService feedSortedSamples:]"
+ "-[CSMartyDetectionService feedSoundPressureLevel:]"
+ "-[CSMartyDetectionService feedSteps:]"
+ "-[CSMartyDetectionService sendCompanionTrigger:]"
+ "-[CSMartyDetectionService setRecording:withUUID:]"
+ "-[CSMartyDetectionService stop:]"
+ "-[CSMartyDetectionService triggered:]"
+ "/Library/Caches/com.apple.xbs/Sources/CoreSafety/SafetyAlgorithms/CSMartyDetectionService.mm"
+ "75ff2079-4a69-4622-af4d-5e561a6f7323"
+ "@\"CSCoreAnalyticsXPCManager\""
+ "@\"CSKappaCoreAnalytics\""
+ "@\"CSMartyDetectionService\""
+ "@112@0:8Q16C24f28f32C36S40c44c48c52c56c60Q64[3 ]72C80C84S88Q92C100*104"
+ "@28@0:8r*16C24"
+ "@32@0:8@?16@?24"
+ "@56@0:8@16@24@32@40@?48"
+ "@56@0:8@16@24Q32d40@48"
+ "@84@0:8Q16d24f32f36f40f44f48f52i56i60c64f68i72f76I80"
+ "At least one CoreAnalytics uploader failed to complete. Will retry later."
+ "B32@0:8d16@24"
+ "CAUnmanagedXPCActivity"
+ "CSCoreAnalyticsUtils"
+ "CSCoreAnalyticsXPCManager"
+ "CSFlowControllerProtocol"
+ "CSIgneousTokenCount"
+ "CSIgneousTokenCountDefault"
+ "CSIgneousTokenReplenishPeriod"
+ "CSIgneousTokenReplenishTimestamp"
+ "CSKappaCoreAnalytics"
+ "CSKappaCoreAnalyticsDispatchQueue"
+ "CSKappaCoreAnalyticsIBProtocol"
+ "CSKappaCoreAnalyticsLastSuccessfulUpload"
+ "CSMartyCoreAnalyticsLastSuccessfulUpload"
+ "CSMartyCoreAnalyticsUserInfo"
+ "CSMartyDetectionService"
+ "Configuring UserInfo with cadence %llu"
+ "CoreAnalytics Kappa upload failed"
+ "CoreAnalytics Marty upload failed"
+ "CoreAnalytics upload ran recently, skipping now."
+ "FC mode K"
+ "FC mode M"
+ "Failed to mark activity as CONTINUE. Current state is %{public}ld"
+ "Failed to mark activity as DEFER. Current state is %{public}ld"
+ "Failed to mark activity as DONE. Current state is %{public}ld"
+ "Igneous"
+ "IgneousDetectionService"
+ "Kappa handler executed successfully"
+ "Kappa handler executed with result: %d"
+ "KappaDetection"
+ "KappaShouldFeedAccessoryGPS"
+ "Marty"
+ "Marty handler executed successfully"
+ "MartyDetection"
+ "Missing config prefix for %d"
+ "Permissions"
+ "Platform"
+ "Running activity %s"
+ "SessionInfo:%@, ImproveSafety:%d"
+ "Start igneous monitoring: %{public}d %{public}@"
+ "T@\"NSString\",&,V_defaultsRegistrationDateKeyName"
+ "T@\"NSString\",&,V_defaultsSubjectAuthTokenKeyName"
+ "T@\"NSString\",&,V_defaultsSubjectIDKeyName"
+ "T@\"NSString\",R,N,V_postfix"
+ "T@\"NSString\",R,V_postfix"
+ "T@?,R,N"
+ "TS,N,V_armedSecMarty"
+ "T^{CSSPUGps_Struct=ffffffiiCQfifId},R,N"
+ "T^{TriggerSample=CCSIQffcccccQ[3 ]CCSQC[16c]},R,N"
+ "Unable to query AOP, _aop valid:%d, _userInfoStats valid:%d"
+ "Unexpected mode %u - all algorithms will be disabled"
+ "^{CSSPUGps_Struct=ffffffiiCQfifId}16@0:8"
+ "^{TriggerSample=CCSIQffcccccQ[3 ]CCSQC[16c]}16@0:8"
+ "_armedSecMarty"
+ "_cachedUploadedResults"
+ "_companionDeviceInfo"
+ "_companionTrigger"
+ "_defaultsRegistrationDateKeyName"
+ "_defaultsSubjectAuthTokenKeyName"
+ "_defaultsSubjectIDKeyName"
+ "_detectionEvent"
+ "_igneousUploader"
+ "_kappaHandler"
+ "_martyAuthorizedToCollect"
+ "_martyDetectionService"
+ "_martyHandler"
+ "_postfix"
+ "_sendAndResetSessionInfoToCoreAnalytics"
+ "_sessionInfoStats"
+ "_shouldFeedAccessoryGPS"
+ "_stopClientCollection"
+ "_stopClientDetection"
+ "_updateArmingTimes"
+ "_userInfoStats"
+ "_userInfoUploadCadence"
+ "_xpcIntervalInSecs"
+ "aborting marty detection service"
+ "absoluteTimestamp"
+ "acquiring igneous token"
+ "armedSecMarty"
+ "asymmetryProbability"
+ "cacheUserInfo"
+ "cannot collect recording for %d"
+ "clearCAStats"
+ "com.apple.MartySession"
+ "com.apple.MartyUserInfo"
+ "com.apple.anomalydetectiond.CSFolderMonitor%@.%@"
+ "configBaseKey:forFeatureMode:"
+ "configure to send after %llu seconds"
+ "converting session %d into a kappa one"
+ "defaultsRegistrationDateKeyName"
+ "defaultsSubjectAuthTokenKeyName"
+ "defaultsSubjectIDKeyName"
+ "fc2a58e3-5fef-42b8-89fc-a2e0bfe517b0"
+ "feedLocationManagerResults:"
+ "finishAnomalyEvent"
+ "forcefully aborting session"
+ "forcefully stopping the collection"
+ "hdsEndpointNameIgneous"
+ "igneous trigger path %d with guid %s"
+ "igneousCMPrototypingConfiguration"
+ "igneousGMConfiguration"
+ "igneousGUID"
+ "igneousOut"
+ "igneousStagingConfiguration"
+ "igneousTokenCount"
+ "ignoring gps accessory"
+ "ignoring gps accessory when btHint=0"
+ "ignoring gps when not in a session"
+ "initStateMachine"
+ "initWithFolder:fileExtension:queue:postfix:andAction:"
+ "initWithMartyUploadHandler:andKappaHandler:"
+ "initWithSpoolerFolder:serverConfiguration:retentionPeriodInSeconds:outOfBandMetadataTimeout:defaultsKeyPostfix:"
+ "initWithTimestamp:doubleTS:speedMS:speedAccuracyMS:courseDeg:courseAccuracyDeg:latitude:longitude:wayForm:roadClass:signalEnvironment:horizontalAccuracy:demNumContiguousFlatPoints:demConfidence:type:"
+ "initWithTimestamp:meta:decel:impact:path:armedSec:motionHint:gpsHint:basebandHint:wifiHint:btHint:lastValidImuTimestamp:vehicleProbabilityLongTermMean:martyPath:enableMode:martyArmedSec:companionAopTs:igneousPath:igneousGUID:"
+ "invalid path %d/%d/%d for enable mode %d"
+ "isKappaNotPostDriving %d isMarty %d isIgneous %d"
+ "isKappaTrigger:"
+ "isMartyTrigger:"
+ "marty not authorized to collect"
+ "martyDrivingTimeMotorcycle:%d, martyDrivingTimeCycle:%d"
+ "mobilitySmoothedGaitMetrics"
+ "multiple detection events cannot be recorded"
+ "no metadata type specified"
+ "not authorized to collect"
+ "numCrashesDetectedInSessionCycle"
+ "numCrashesDetectedInSessionMotorbike"
+ "numKappaTriggersAllSessions"
+ "numKappaTriggersAllSessions_companion"
+ "numMartySessionsCycle"
+ "numMartySessionsCycle_companion"
+ "numMartySessionsMotorbike"
+ "numMartySessionsMotorbike_companion"
+ "numTriggersAllSessionsCycle"
+ "numTriggersAllSessionsCycle_companion"
+ "numTriggersAllSessionsMotorbike"
+ "numTriggersAllSessionsMotorbike_companion"
+ "persistentConfigurationIgneous"
+ "phIcy6u36xhpEJarbZX0yOgE3ZQpW16R2MlII5OvgrUKeD7PdxOsfu3xEZDoApfc"
+ "postfix"
+ "receiveCompanionTrigger:"
+ "receiveDeviceInfo:"
+ "receiveUUID:"
+ "recording is nil"
+ "registerForCoreAnalyticsUserInfoWithExplicitCriteria"
+ "requestLocation:"
+ "resetSession Marty"
+ "sPy2s1bD7Fr9Tw3fPGqYFXeQwUhYuPNe04Wukh4SFENtnSocfhbMDEG9xty9Mq6f"
+ "secondsSinceReboot exceeds UserInfo cadence. Capping at cadence pd:%llu"
+ "sendCompanionTrigger:"
+ "sendDeviceInfo"
+ "set recording state %d %d"
+ "setArmedSecMarty:"
+ "setDefaultsRegistrationDateKeyName:"
+ "setDefaultsSubjectAuthTokenKeyName:"
+ "setDefaultsSubjectIDKeyName:"
+ "setNextFireDelay:"
+ "should feed accessory gps %d"
+ "shouldAttemptCoreAnalyticsUploadWithInterval:persistentKey:"
+ "startIgneousUploader"
+ "stop consuming samples"
+ "stop trigger timer"
+ "stopSession:"
+ "studiesServerUploaderSpoolerIgneous"
+ "subsequent detection events cannot take tokens or update metadata"
+ "timeIntervalSinceDate:"
+ "totalDrivingTimeCycle"
+ "totalDrivingTimeMotorcycle"
+ "totalKappaDrivingTime"
+ "trigger path %d marty path %d igneous path %d enabledMode %d"
+ "unmanaged xpc activity"
+ "updateMartyUserInfoWithInfo updated stats"
+ "updateMartyUserInfoWithInfo:"
+ "uploadUserInfoToCoreAnalyticsWithHandler:"
+ "uploadUserInfoWithHandler:"
+ "userInfoUploader"
+ "uuid is nil"
+ "v20@?0B8@\"NSDictionary\"12"
+ "v24@?0@\"NSDictionary\"8@?<v@?B@\"NSDictionary\">16"
+ "vehicleType"
+ "{\"msg%{public}.0s\":\"uuid is nil\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{CSSPUGps_Struct=\"speedMS\"f\"speedAccuracyMS\"f\"courseDeg\"f\"courseAccuracyDeg\"f\"latitude\"f\"longitude\"f\"wayForm\"i\"roadClass\"i\"signalEnvironment\"C\"timestamp\"Q\"horizontalAccuracy\"f\"demNumContiguousFlatPoints\"i\"demConfidence\"f\"type\"I\"doubleTS\"d}"
+ "{TriggerSample=\"meta\"C\"path\"C\"armedSec\"S\"rmsSN\"I\"timestamp\"Q\"decel\"f\"impact\"f\"motionHint\"c\"gpsHint\"c\"basebandHint\"c\"wifiHint\"c\"btHint\"c\"lastValidImuTimestamp\"Q\"vehicleProbabilityLongTermMean\"[3 ]\"martyPath\"C\"enableMode\"C\"martyArmedSec\"S\"companionAopTs\"Q\"igneousPath\"C\"igneousGUID\"[16c]}"
+ "{unique_ptr<MartySessionInfo, std::default_delete<MartySessionInfo>>=\"__ptr_\"{__compressed_pair<MartySessionInfo *, std::default_delete<MartySessionInfo>>=\"__value_\"^{MartySessionInfo}}}"
+ "{unique_ptr<MartyUserInfo, std::default_delete<MartyUserInfo>>=\"__ptr_\"{__compressed_pair<MartyUserInfo *, std::default_delete<MartyUserInfo>>=\"__value_\"^{MartyUserInfo}}}"
- "\x01\xf0\x95"
- "\x03\x16\x12\x81\x13\x13\xf0!\xf0#3"
- "\x12B\x11%\x11"
- "\x18"
- "-[CSAnomalyEventService sendMartyCompanionTrigger:]"
- "-[CSAnomalyEventService triggered:]"
- "-[CSKappaDetectionService feedPressureCalibration:]"
- "@\"CSCoreAnalytics\""
- "@\"CSCoreAnalyticsUserInfoConfiguration\""
- "@100@0:8Q16C24f28f32C36S40c44c48c52c56c60Q64[3 ]72C80C84S88Q92"
- "@48@0:8@16@24@32@?40"
- "@48@0:8@16@24Q32d40"
- "@80@0:8Q16d24f32f36f40f44f48f52i56i60c64f68i72f76"
- "AOIUpdateValues"
- "Active Kappa in progress. Defer sending UserInfo via XPC. defer:%d"
- "CAIndigenousXPCActivity"
- "CSCoreAnalytics"
- "CSCoreAnalyticsDispatchQueue"
- "CSCoreAnalyticsIBProtocol"
- "CSCoreAnalyticsUserInfoConfiguration"
- "CSPressureCalibration is null"
- "Configuring UserInfo with cadence %d"
- "Detection"
- "DisableKappaAOICheck"
- "Failed to mark activity as done. Current state is %{public}ld"
- "KappaEstimatesAlgAirbag"
- "KappaEstimatesAlgCrash"
- "KappaEstimatesAlgHighSpeedCrash"
- "KappaEstimatesAlgRolloverCrash"
- "KappaFeaturesAlgBaro"
- "KappaFeaturesAlgDataIntegrity"
- "KappaFeaturesAlgGPS"
- "KappaFeaturesAlgGravityAutoCorrelation"
- "KappaFeaturesAlgLackOfMotion"
- "KappaFeaturesAlgLocalAudio"
- "KappaFeaturesAlgPeakDetectorMAP"
- "KappaFeaturesAlgPulse"
- "KappaFeaturesAlgRemoteAudio"
- "KappaFeaturesAlgSpin"
- "KappaFeaturesAlgSteps"
- "KappaFeaturesAlgTriggerClusters"
- "KappaFeaturesAlgZg"
- "KappaInferencesAlgSevereCrash"
- "TQ,R,N,V_period"
- "T^{CSSPUGps_Struct=ffffffiiCQfifd},R,N"
- "T^{TriggerSample=CCSIQffcccccQ[3 ]CCSQ},R,N"
- "TwoLevelSensitivityConfig"
- "WaterProxyConfig"
- "^{CSSPUGps_Struct=ffffffiiCQfifd}16@0:8"
- "^{TriggerSample=CCSIQffcccccQ[3 ]CCSQ}16@0:8"
- "_martyCompanion"
- "_martyCompanionTrigger"
- "_martyCompanionUUID"
- "_period"
- "_sendConfig"
- "_stopMartyCollection"
- "_stopMartyDetection"
- "authorizedToCollectDataSanity"
- "can collect data but msl recording is nil"
- "com.apple.anomalydetectiond.CSFolderMonitor.%@"
- "configure to send after %d seconds"
- "converting a marty session into a kappa one"
- "feedPressureCalibration:"
- "indigenous xpc activity"
- "initWithFolder:fileExtension:queue:andAction:"
- "initWithPeriodInSeconds:"
- "initWithSpoolerFolder:serverConfiguration:retentionPeriodInSeconds:outOfBandMetadataTimeout:"
- "initWithTimestamp:doubleTS:speedMS:speedAccuracyMS:courseDeg:courseAccuracyDeg:latitude:longitude:wayForm:roadClass:signalEnvironment:horizontalAccuracy:demNumContiguousFlatPoints:demConfidence:"
- "initWithTimestamp:meta:decel:impact:path:armedSec:motionHint:gpsHint:basebandHint:wifiHint:btHint:lastValidImuTimestamp:vehicleProbabilityLongTermMean:martyPath:enableMode:martyArmedSec:companionAopTs:"
- "invalid path %d/%d for enable mode %d"
- "invalid trigger"
- "period"
- "receiveMartyCompanionTrigger:"
- "receiveMartyDeviceInfo:"
- "receiveMartyUUID:"
- "registerForCoreAnalyticsUserInfoWithConfiguration:"
- "secondsSinceReboot exceeds UserInfo cadence. Capping at cadence pd:%d"
- "sendDeviceInfo:"
- "sendMartyCompanionTrigger:"
- "sendMartyDeviceInfo"
- "sendMartyUUID:"
- "sendUUID:"
- "trigger path %d marty path %d enabledMode %d"
- "{\"msg%{public}.0s\":\"CSPressureCalibration is null\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"invalid trigger\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "{CSSPUGps_Struct=\"speedMS\"f\"speedAccuracyMS\"f\"courseDeg\"f\"courseAccuracyDeg\"f\"latitude\"f\"longitude\"f\"wayForm\"i\"roadClass\"i\"signalEnvironment\"C\"timestamp\"Q\"horizontalAccuracy\"f\"demNumContiguousFlatPoints\"i\"demConfidence\"f\"doubleTS\"d}"
- "{TriggerSample=\"meta\"C\"path\"C\"armedSec\"S\"rmsSN\"I\"timestamp\"Q\"decel\"f\"impact\"f\"motionHint\"c\"gpsHint\"c\"basebandHint\"c\"wifiHint\"c\"btHint\"c\"lastValidImuTimestamp\"Q\"vehicleProbabilityLongTermMean\"[3 ]\"martyPath\"C\"enableMode\"C\"martyArmedSec\"S\"companionAopTs\"Q}"

```
