## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`

```diff

-148.100.2.0.0
-  __TEXT.__text: 0x7804
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0xc90
-  __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x6a4
-  __TEXT.__gcc_except_tab: 0x320
-  __TEXT.__oslogstring: 0x941
-  __TEXT.__unwind_info: 0x388
-  __TEXT.__objc_classname: 0x240
-  __TEXT.__objc_methname: 0x16ff
-  __TEXT.__objc_methtype: 0x550
-  __TEXT.__objc_stubs: 0x10c0
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x310
-  __DATA_CONST.__objc_classlist: 0x68
-  __DATA_CONST.__objc_protolist: 0x40
+198.0.0.0.1
+  __TEXT.__text: 0x14bf4
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_methlist: 0x1d70
+  __TEXT.__const: 0x128
+  __TEXT.__cstring: 0x12e2
+  __TEXT.__gcc_except_tab: 0x5cc
+  __TEXT.__oslogstring: 0x1585
+  __TEXT.__unwind_info: 0x800
+  __TEXT.__objc_classname: 0x41d
+  __TEXT.__objc_methname: 0x330c
+  __TEXT.__objc_methtype: 0xa8a
+  __TEXT.__objc_stubs: 0x2500
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__const: 0x760
+  __DATA_CONST.__objc_classlist: 0xd0
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b8
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x1c8
-  __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x720
-  __AUTH_CONST.__objc_const: 0x1350
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x88
-  __DATA.__data: 0x300
-  __DATA_DIRTY.__objc_data: 0x320
-  __DATA_DIRTY.__bss: 0x8
+  __DATA_CONST.__objc_selrefs: 0xde8
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0xa0
+  __AUTH_CONST.__auth_got: 0x2d0
+  __AUTH_CONST.__const: 0x720
+  __AUTH_CONST.__cfstring: 0xf80
+  __AUTH_CONST.__objc_const: 0x2b20
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x178
+  __DATA.__data: 0x540
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__objc_data: 0x640
+  __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
+  - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
+  - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
+  - /System/Library/PrivateFrameworks/LowPowerMode.framework/LowPowerMode
+  - /System/Library/PrivateFrameworks/PerformanceControlKit.framework/PerformanceControlKit
+  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
+  - /System/Library/PrivateFrameworks/Trial.framework/Trial
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 509B3899-8CA8-3676-8E68-C27855ADC20F
-  Functions: 303
-  Symbols:   1079
-  CStrings:  538
+  UUID: A41601C8-67F0-3C78-8F73-1AB7D3D32C02
+  Functions: 763
+  Symbols:   2568
+  CStrings:  1137
 
Symbols:
+ +[OSIUtilities isiPhone]
+ +[OSIUtilities midnightDateFrom:]
+ +[_OSBatteryTimeTillDischargeOutput supportsSecureCoding]
+ +[_OSDayDrainResult supportsSecureCoding]
+ +[_OSIAutoLPMManager sharedInstance]
+ +[_OSIAutoLPMManager sharedInstance].cold.1
+ +[_OSIBLMAnalyticsHandler sharedInstance]
+ +[_OSIBLMAnalyticsHandler sharedInstance].cold.1
+ +[_OSIBLMState isIBLMDefaultOn]
+ +[_OSIBLMState isIBLMSupported]
+ +[_OSIBLMState loadCurrentIBLMState]
+ +[_OSIBLMState loadNumberForPreferenceKey:]
+ +[_OSIBLMState saveCurrentIBLMState:]
+ +[_OSIBLMState saveNumber:forKey:]
+ +[_OSIBLMState sharedInstance]
+ +[_OSIBLMState sharedInstance].cold.1
+ +[_OSIBLMState sharedLog]
+ +[_OSIBLManager sharedInstance]
+ +[_OSIBLManager sharedInstance].cold.1
+ +[_OSIBLMitigation supportsSecureCoding]
+ +[_OSIBatteryLifeManager sharedInstance]
+ +[_OSIBatteryLifeManager sharedInstance].cold.1
+ +[_OSICLPCInterface hasPerformanceControlService]
+ +[_OSICLPCInterface sharedInstance]
+ +[_OSICLPCInterface sharedInstance].cold.1
+ +[_OSICLPCInterface supportsPerformanceControl]
+ +[_OSITimeSeriesUtilities resampleTimeSeries:withFrequency:]
+ +[_OSLastLockPredictorMetadata supportsSecureCoding]
+ +[_OSLastLockPredictorOutput supportsSecureCoding]
+ -[_OSBatteryDrainPredictor highBatteryDrainComparedtoHourlyAggregate]
+ -[_OSBatteryDrainPredictor highBatteryDrainComparedtoHourlyAggregate].cold.1
+ -[_OSBatteryDrainPredictor lastBatteryLevelDate]
+ -[_OSBatteryDrainPredictor lastBatteryLevelValue]
+ -[_OSBatteryPredictor batteryLifeMitigationWithError:]
+ -[_OSBatteryPredictor client:setIBLMState:]
+ -[_OSBatteryPredictor highDayDrainAroundCurrentDateWithError:]
+ -[_OSBatteryPredictor overrideAllMitigations:]
+ -[_OSBatteryPredictor overrideCLPCMitigations:]
+ -[_OSBatteryPredictor recommendsAutoLPMWithError:]
+ -[_OSBatteryPredictor typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withError:]
+ -[_OSBatteryTimeTillDischargeOutput description]
+ -[_OSBatteryTimeTillDischargeOutput encodeWithCoder:]
+ -[_OSBatteryTimeTillDischargeOutput initWithCoder:]
+ -[_OSBatteryTimeTillDischargeOutput predictedDischargeTime]
+ -[_OSBatteryTimeTillDischargeOutput setPredictedDischargeTime:]
+ -[_OSChargingPredictor timeUntilNextChargeSessionOfMinDuration:fromSOC:WithError:]
+ -[_OSDayDrainResult confidence]
+ -[_OSDayDrainResult copyWithZone:]
+ -[_OSDayDrainResult description]
+ -[_OSDayDrainResult encodeWithCoder:]
+ -[_OSDayDrainResult initWithCoder:]
+ -[_OSDayDrainResult initWithIsHighDrain:confidence:]
+ -[_OSDayDrainResult isHighDrain]
+ -[_OSDayDrainResult setConfidence:]
+ -[_OSDayDrainResult setIsHighDrain:]
+ -[_OSIAutoLPMManager .cxx_destruct]
+ -[_OSIAutoLPMManager context]
+ -[_OSIAutoLPMManager defaults]
+ -[_OSIAutoLPMManager didEnableAutoLPM]
+ -[_OSIAutoLPMManager disengageAutoLPM]
+ -[_OSIAutoLPMManager disengageAutoLPM].cold.1
+ -[_OSIAutoLPMManager engageAutoLPM]
+ -[_OSIAutoLPMManager engageAutoLPM].cold.1
+ -[_OSIAutoLPMManager evaluateAutoLPMEngagement]
+ -[_OSIAutoLPMManager init]
+ -[_OSIAutoLPMManager isPluggedIn]
+ -[_OSIAutoLPMManager log]
+ -[_OSIAutoLPMManager queue]
+ -[_OSIAutoLPMManager setContext:]
+ -[_OSIAutoLPMManager setDefaults:]
+ -[_OSIAutoLPMManager setDidEnableAutoLPM:]
+ -[_OSIAutoLPMManager setLog:]
+ -[_OSIAutoLPMManager setQueue:]
+ -[_OSIAutoLPMManager start]
+ -[_OSIBLMAnalyticsHandler .cxx_destruct]
+ -[_OSIBLMAnalyticsHandler cancelTask]
+ -[_OSIBLMAnalyticsHandler cancelTask].cold.1
+ -[_OSIBLMAnalyticsHandler dateFormatter]
+ -[_OSIBLMAnalyticsHandler dateFormatter].cold.1
+ -[_OSIBLMAnalyticsHandler defaults]
+ -[_OSIBLMAnalyticsHandler extractAndReportMetrics]
+ -[_OSIBLMAnalyticsHandler featureEngagementMetricsFromDrainData:engagementData:]
+ -[_OSIBLMAnalyticsHandler historicalDrainDataForDate:]
+ -[_OSIBLMAnalyticsHandler historicalEngagementDataForDate:]
+ -[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]
+ -[_OSIBLMAnalyticsHandler init]
+ -[_OSIBLMAnalyticsHandler log]
+ -[_OSIBLMAnalyticsHandler ppsIDForSubsystem:category:]
+ -[_OSIBLMAnalyticsHandler ppsIDForSubsystem:category:].cold.1
+ -[_OSIBLMAnalyticsHandler queue]
+ -[_OSIBLMAnalyticsHandler recordAnalyticsFeatureState:]
+ -[_OSIBLMAnalyticsHandler recordAutoLPMState:]
+ -[_OSIBLMAnalyticsHandler recordFeatureState:]
+ -[_OSIBLMAnalyticsHandler recordFeatureState:].cold.1
+ -[_OSIBLMAnalyticsHandler recordMitigationUpdateTo:fromPrevious:]
+ -[_OSIBLMAnalyticsHandler reportDailyFeatureState]
+ -[_OSIBLMAnalyticsHandler sendDataToPPS:subsystem:category:]
+ -[_OSIBLMAnalyticsHandler sendDataToPPS:subsystem:category:].cold.1
+ -[_OSIBLMAnalyticsHandler sendDataToPPS:subsystem:category:].cold.2
+ -[_OSIBLMAnalyticsHandler setDefaults:]
+ -[_OSIBLMAnalyticsHandler setLog:]
+ -[_OSIBLMAnalyticsHandler setQueue:]
+ -[_OSIBLMAnalyticsHandler setSubsystemToPPSID:]
+ -[_OSIBLMAnalyticsHandler start]
+ -[_OSIBLMAnalyticsHandler stop]
+ -[_OSIBLMAnalyticsHandler submitTask]
+ -[_OSIBLMAnalyticsHandler submitTask].cold.1
+ -[_OSIBLMAnalyticsHandler subsystemToPPSID]
+ -[_OSIBLMState .cxx_destruct]
+ -[_OSIBLMState autoLPMEngagement]
+ -[_OSIBLMState client:setIBLMState:]
+ -[_OSIBLMState context]
+ -[_OSIBLMState isIBLMCurrentlyEnabled]
+ -[_OSIBLMState monitorForAutoLPM]
+ -[_OSIBLMState queue]
+ -[_OSIBLMState setAutoLPMEngagement:]
+ -[_OSIBLMState setContext:]
+ -[_OSIBLMState setQueue:]
+ -[_OSIBLMState willEnableAutoLPM]
+ -[_OSIBLManager .cxx_destruct]
+ -[_OSIBLManager cameraViewfinder:viewfinderSessionDidBegin:]
+ -[_OSIBLManager cameraViewfinder:viewfinderSessionDidEnd:]
+ -[_OSIBLManager cancelTask]
+ -[_OSIBLManager cancelTask].cold.1
+ -[_OSIBLManager consoleModeNotificationHandler]
+ -[_OSIBLManager consoleModeNotifyToken]
+ -[_OSIBLManager context]
+ -[_OSIBLManager currentFeatureState]
+ -[_OSIBLManager currentMitigationWithError:]
+ -[_OSIBLManager currentMitigation]
+ -[_OSIBLManager defaults]
+ -[_OSIBLManager evaluate]
+ -[_OSIBLManager featureStatusQueue]
+ -[_OSIBLManager handleCLPCTestOverride:]
+ -[_OSIBLManager handleFeatureDisabled]
+ -[_OSIBLManager handleFeatureEnabled]
+ -[_OSIBLManager handleTestOverride:]
+ -[_OSIBLManager init]
+ -[_OSIBLManager isConsoleModeActive]
+ -[_OSIBLManager isIBLMCurrentlyEnabled]
+ -[_OSIBLManager isLPMEnabled]
+ -[_OSIBLManager isPluggedIn]
+ -[_OSIBLManager lastEvaluateDate]
+ -[_OSIBLManager lastMitigationChangeDate]
+ -[_OSIBLManager log]
+ -[_OSIBLManager mitigationWithLevel:]
+ -[_OSIBLManager notifyMitigationChange:]
+ -[_OSIBLManager notifyTestToken]
+ -[_OSIBLManager notifyToken]
+ -[_OSIBLManager overrideAllMitigations:]
+ -[_OSIBLManager overrideCLPCMitigations:]
+ -[_OSIBLManager predictMitigationLevelWithError:]
+ -[_OSIBLManager predictMitigationLevelWithError:].cold.1
+ -[_OSIBLManager queryAndUpdateCurrentConsoleModeState]
+ -[_OSIBLManager queryAndUpdateCurrentConsoleModeState].cold.1
+ -[_OSIBLManager queue]
+ -[_OSIBLManager resetMitigation]
+ -[_OSIBLManager setConsoleModeNotifyToken:]
+ -[_OSIBLManager setContext:]
+ -[_OSIBLManager setCurrentFeatureState:]
+ -[_OSIBLManager setCurrentMitigation:]
+ -[_OSIBLManager setDefaults:]
+ -[_OSIBLManager setFeatureStatusQueue:]
+ -[_OSIBLManager setIsConsoleModeActive:]
+ -[_OSIBLManager setLastEvaluateDate:]
+ -[_OSIBLManager setLastMitigationChangeDate:]
+ -[_OSIBLManager setLog:]
+ -[_OSIBLManager setNotifyTestToken:]
+ -[_OSIBLManager setNotifyToken:]
+ -[_OSIBLManager setQueue:]
+ -[_OSIBLManager setTrialClient:]
+ -[_OSIBLManager setTrialFeatureEnabled:]
+ -[_OSIBLManager setTrialMitigationsEnabled:]
+ -[_OSIBLManager setTrialPerformanceMitigationEnabled:]
+ -[_OSIBLManager setViewFinder:]
+ -[_OSIBLManager setViewfinderIsActive:]
+ -[_OSIBLManager shouldOverrideMitigations]
+ -[_OSIBLManager start]
+ -[_OSIBLManager submitTask]
+ -[_OSIBLManager submitTask].cold.1
+ -[_OSIBLManager testOverridenMitigation]
+ -[_OSIBLManager trialClient]
+ -[_OSIBLManager trialFeatureEnabled]
+ -[_OSIBLManager trialMitigationsEnabled]
+ -[_OSIBLManager trialPerformanceMitigationEnabled]
+ -[_OSIBLManager updateFeatureState:withError:]
+ -[_OSIBLManager updateMitigationTo:]
+ -[_OSIBLManager updateTrialParameters]
+ -[_OSIBLManager viewFinder]
+ -[_OSIBLManager viewfinderIsActive]
+ -[_OSIBLMitigation .cxx_destruct]
+ -[_OSIBLMitigation confidence]
+ -[_OSIBLMitigation copyWithZone:]
+ -[_OSIBLMitigation decisionMakerString]
+ -[_OSIBLMitigation decisionMaker]
+ -[_OSIBLMitigation description]
+ -[_OSIBLMitigation encodeWithCoder:]
+ -[_OSIBLMitigation initWithCoder:]
+ -[_OSIBLMitigation initWithLevel:decisionMaker:decisionMakerString:confidence:]
+ -[_OSIBLMitigation level]
+ -[_OSIBLMitigation setConfidence:]
+ -[_OSIBLMitigation setDecisionMaker:]
+ -[_OSIBLMitigation setDecisionMakerString:]
+ -[_OSIBLMitigation setLevel:]
+ -[_OSIBatteryLifeManager .cxx_destruct]
+ -[_OSIBatteryLifeManager clientToHandler]
+ -[_OSIBatteryLifeManager init]
+ -[_OSIBatteryLifeManager log]
+ -[_OSIBatteryLifeManager mitigationWithError:]
+ -[_OSIBatteryLifeManager notifyTestToken]
+ -[_OSIBatteryLifeManager notifyToken]
+ -[_OSIBatteryLifeManager overrideAllMitigations:]
+ -[_OSIBatteryLifeManager overrideCLPCMitigations:]
+ -[_OSIBatteryLifeManager queue]
+ -[_OSIBatteryLifeManager registerForDrainLevelPredictionForClient:withithUpdateHandler:]
+ -[_OSIBatteryLifeManager setClientToHandler:]
+ -[_OSIBatteryLifeManager setLog:]
+ -[_OSIBatteryLifeManager setNotifyTestToken:]
+ -[_OSIBatteryLifeManager setNotifyToken:]
+ -[_OSIBatteryLifeManager setQueue:]
+ -[_OSICLPCInterface .cxx_destruct]
+ -[_OSICLPCInterface clpcClient]
+ -[_OSICLPCInterface init]
+ -[_OSICLPCInterface log]
+ -[_OSICLPCInterface queue]
+ -[_OSICLPCInterface setClpcClient:]
+ -[_OSICLPCInterface setLog:]
+ -[_OSICLPCInterface setQueue:]
+ -[_OSICLPCInterface start]
+ -[_OSICLPCInterface start].cold.1
+ -[_OSICLPCInterface updatePerformanceControlWithMitigation:]
+ -[_OSLastLockPredictionClient .cxx_destruct]
+ -[_OSLastLockPredictionClient activityHistoryDiagnosisWithHandler:]
+ -[_OSLastLockPredictionClient activityHistoryDiagnosis]
+ -[_OSLastLockPredictionClient connection]
+ -[_OSLastLockPredictionClient dealloc]
+ -[_OSLastLockPredictionClient deviceUsageDiagnosisWithHandler:]
+ -[_OSLastLockPredictionClient deviceUsageDiagnosis]
+ -[_OSLastLockPredictionClient fixModelOutput:]
+ -[_OSLastLockPredictionClient fixModelOutput:withHandler:]
+ -[_OSLastLockPredictionClient handleInterruption]
+ -[_OSLastLockPredictionClient handleInterruption].cold.1
+ -[_OSLastLockPredictionClient hasEnoughActivityHistoryWithHandler:]
+ -[_OSLastLockPredictionClient hasEnoughActivityHistory]
+ -[_OSLastLockPredictionClient initConnection]
+ -[_OSLastLockPredictionClient init]
+ -[_OSLastLockPredictionClient lastLockPredictionResultAtDate:withTimeSinceActive:withError:]
+ -[_OSLastLockPredictionClient lastLockPredictionResultAtDate:withTimeSinceActive:withHandler:]
+ -[_OSLastLockPredictionClient lastLockPredictionResultWithError:]
+ -[_OSLastLockPredictionClient lastLockPredictionResultWithHandler:]
+ -[_OSLastLockPredictionClient lock]
+ -[_OSLastLockPredictionClient modelDescriptionWithHandler:]
+ -[_OSLastLockPredictionClient modelDescription]
+ -[_OSLastLockPredictionClient modelMetadataWithHandler:]
+ -[_OSLastLockPredictionClient modelMetadata]
+ -[_OSLastLockPredictionClient overrideRecommendedRequeryTimeTo:]
+ -[_OSLastLockPredictionClient overrideRecommendedRequeryTimeTo:withHandler:]
+ -[_OSLastLockPredictionClient recommendedRequeryTimeWithHandler:]
+ -[_OSLastLockPredictionClient recommendedRequeryTime]
+ -[_OSLastLockPredictionClient restoreLastLockModelWithHandler:]
+ -[_OSLastLockPredictionClient restoreLastLockModel]
+ -[_OSLastLockPredictionClient restoreRecommendedRequeryTimeWithHandler:]
+ -[_OSLastLockPredictionClient restoreRecommendedRequeryTime]
+ -[_OSLastLockPredictionClient setConnection:]
+ -[_OSLastLockPredictionClient setLock:]
+ -[_OSLastLockPredictionClient unfixModelOutputWithHandler:]
+ -[_OSLastLockPredictionClient unfixModelOutput]
+ -[_OSLastLockPredictionClient validConnection]
+ -[_OSLastLockPredictorMetadata .cxx_destruct]
+ -[_OSLastLockPredictorMetadata confidenceThresholdRelaxed]
+ -[_OSLastLockPredictorMetadata confidenceThresholdStrict]
+ -[_OSLastLockPredictorMetadata description]
+ -[_OSLastLockPredictorMetadata encodeWithCoder:]
+ -[_OSLastLockPredictorMetadata initWithCoder:]
+ -[_OSLastLockPredictorMetadata initWithProtocolConformer:]
+ -[_OSLastLockPredictorMetadata longThreshold]
+ -[_OSLastLockPredictorMetadata modelVersion]
+ -[_OSLastLockPredictorMetadata predictorType]
+ -[_OSLastLockPredictorMetadata queryingMechanism]
+ -[_OSLastLockPredictorMetadata recommendedRequeryTime]
+ -[_OSLastLockPredictorMetadata requireEnoughHistory]
+ -[_OSLastLockPredictorMetadata setConfidenceThresholdRelaxed:]
+ -[_OSLastLockPredictorMetadata setConfidenceThresholdStrict:]
+ -[_OSLastLockPredictorMetadata setLongThreshold:]
+ -[_OSLastLockPredictorMetadata setModelVersion:]
+ -[_OSLastLockPredictorMetadata setPredictorType:]
+ -[_OSLastLockPredictorMetadata setQueryingMechanism:]
+ -[_OSLastLockPredictorMetadata setRecommendedRequeryTime:]
+ -[_OSLastLockPredictorMetadata setRequireEnoughHistory:]
+ -[_OSLastLockPredictorOutput confidenceLevelString]
+ -[_OSLastLockPredictorOutput confidenceLevel]
+ -[_OSLastLockPredictorOutput confidenceValueString]
+ -[_OSLastLockPredictorOutput confidenceValue]
+ -[_OSLastLockPredictorOutput description]
+ -[_OSLastLockPredictorOutput encodeWithCoder:]
+ -[_OSLastLockPredictorOutput initInvalidOutput]
+ -[_OSLastLockPredictorOutput initWithCoder:]
+ -[_OSLastLockPredictorOutput initWithConfidenceLevel:andConfidenceValue:andPredictedDuration:andReason:]
+ -[_OSLastLockPredictorOutput initWithConfidenceValue:andRelaxedThreshold:andStrictThreshold:andPredictedDuration:andReason:]
+ -[_OSLastLockPredictorOutput outputReasonString]
+ -[_OSLastLockPredictorOutput outputReason]
+ -[_OSLastLockPredictorOutput predictedDurationString]
+ -[_OSLastLockPredictorOutput predictedDuration]
+ -[_OSLastLockPredictorOutput setConfidenceLevel:]
+ -[_OSLastLockPredictorOutput setConfidenceValue:]
+ -[_OSLastLockPredictorOutput setOutputReason:]
+ -[_OSLastLockPredictorOutput setPredictedDuration:]
+ GCC_except_table13
+ GCC_except_table16
+ GCC_except_table19
+ GCC_except_table2
+ GCC_except_table22
+ GCC_except_table23
+ GCC_except_table27
+ GCC_except_table30
+ GCC_except_table33
+ GCC_except_table36
+ GCC_except_table39
+ GCC_except_table42
+ GCC_except_table45
+ GCC_except_table8
+ _AnalyticsSendEventLazy
+ _CFPreferencesCopyValue
+ _CFPreferencesSetValue
+ _CFPreferencesSynchronize
+ _IOObjectRelease
+ _IOServiceGetMatchingService
+ _IOServiceMatching
+ _MGGetProductType
+ _MGGetStringAnswer
+ _OBJC_CLASS_$_BGRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_CLPCPolicyInterface
+ _OBJC_CLASS_$_FigCameraViewfinder
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$_TRIClient
+ _OBJC_CLASS_$__CDClientContext
+ _OBJC_CLASS_$__CDContextQueries
+ _OBJC_CLASS_$__CDContextualChangeRegistration
+ _OBJC_CLASS_$__CDContextualPredicate
+ _OBJC_CLASS_$__OSBatteryTimeTillDischargeOutput
+ _OBJC_CLASS_$__OSDayDrainResult
+ _OBJC_CLASS_$__OSIAutoLPMManager
+ _OBJC_CLASS_$__OSIBLMAnalyticsHandler
+ _OBJC_CLASS_$__OSIBLMState
+ _OBJC_CLASS_$__OSIBLManager
+ _OBJC_CLASS_$__OSIBLMitigation
+ _OBJC_CLASS_$__OSIBatteryLifeManager
+ _OBJC_CLASS_$__OSICLPCInterface
+ _OBJC_CLASS_$__OSITimeSeriesUtilities
+ _OBJC_CLASS_$__OSLastLockPredictionClient
+ _OBJC_CLASS_$__OSLastLockPredictorMetadata
+ _OBJC_CLASS_$__OSLastLockPredictorOutput
+ _OBJC_CLASS_$__PMLowPowerMode
+ _OBJC_IVAR_$__OSBatteryTimeTillDischargeOutput._predictedDischargeTime
+ _OBJC_IVAR_$__OSDayDrainResult._confidence
+ _OBJC_IVAR_$__OSDayDrainResult._isHighDrain
+ _OBJC_IVAR_$__OSIAutoLPMManager._context
+ _OBJC_IVAR_$__OSIAutoLPMManager._defaults
+ _OBJC_IVAR_$__OSIAutoLPMManager._didEnableAutoLPM
+ _OBJC_IVAR_$__OSIAutoLPMManager._log
+ _OBJC_IVAR_$__OSIAutoLPMManager._queue
+ _OBJC_IVAR_$__OSIBLMAnalyticsHandler._defaults
+ _OBJC_IVAR_$__OSIBLMAnalyticsHandler._log
+ _OBJC_IVAR_$__OSIBLMAnalyticsHandler._queue
+ _OBJC_IVAR_$__OSIBLMAnalyticsHandler._subsystemToPPSID
+ _OBJC_IVAR_$__OSIBLMState._autoLPMEngagement
+ _OBJC_IVAR_$__OSIBLMState._context
+ _OBJC_IVAR_$__OSIBLMState._queue
+ _OBJC_IVAR_$__OSIBLManager._consoleModeNotifyToken
+ _OBJC_IVAR_$__OSIBLManager._context
+ _OBJC_IVAR_$__OSIBLManager._currentFeatureState
+ _OBJC_IVAR_$__OSIBLManager._currentMitigation
+ _OBJC_IVAR_$__OSIBLManager._defaults
+ _OBJC_IVAR_$__OSIBLManager._featureStatusQueue
+ _OBJC_IVAR_$__OSIBLManager._isConsoleModeActive
+ _OBJC_IVAR_$__OSIBLManager._lastEvaluateDate
+ _OBJC_IVAR_$__OSIBLManager._lastMitigationChangeDate
+ _OBJC_IVAR_$__OSIBLManager._log
+ _OBJC_IVAR_$__OSIBLManager._notifyTestToken
+ _OBJC_IVAR_$__OSIBLManager._notifyToken
+ _OBJC_IVAR_$__OSIBLManager._queue
+ _OBJC_IVAR_$__OSIBLManager._trialClient
+ _OBJC_IVAR_$__OSIBLManager._trialFeatureEnabled
+ _OBJC_IVAR_$__OSIBLManager._trialMitigationsEnabled
+ _OBJC_IVAR_$__OSIBLManager._trialPerformanceMitigationEnabled
+ _OBJC_IVAR_$__OSIBLManager._viewFinder
+ _OBJC_IVAR_$__OSIBLManager._viewfinderIsActive
+ _OBJC_IVAR_$__OSIBLMitigation._confidence
+ _OBJC_IVAR_$__OSIBLMitigation._decisionMaker
+ _OBJC_IVAR_$__OSIBLMitigation._decisionMakerString
+ _OBJC_IVAR_$__OSIBLMitigation._level
+ _OBJC_IVAR_$__OSIBatteryLifeManager._clientToHandler
+ _OBJC_IVAR_$__OSIBatteryLifeManager._log
+ _OBJC_IVAR_$__OSIBatteryLifeManager._notifyTestToken
+ _OBJC_IVAR_$__OSIBatteryLifeManager._notifyToken
+ _OBJC_IVAR_$__OSIBatteryLifeManager._queue
+ _OBJC_IVAR_$__OSICLPCInterface._clpcClient
+ _OBJC_IVAR_$__OSICLPCInterface._log
+ _OBJC_IVAR_$__OSICLPCInterface._queue
+ _OBJC_IVAR_$__OSLastLockPredictionClient._connection
+ _OBJC_IVAR_$__OSLastLockPredictionClient._lock
+ _OBJC_IVAR_$__OSLastLockPredictorMetadata.confidenceThresholdRelaxed
+ _OBJC_IVAR_$__OSLastLockPredictorMetadata.confidenceThresholdStrict
+ _OBJC_IVAR_$__OSLastLockPredictorMetadata.longThreshold
+ _OBJC_IVAR_$__OSLastLockPredictorMetadata.modelVersion
+ _OBJC_IVAR_$__OSLastLockPredictorMetadata.predictorType
+ _OBJC_IVAR_$__OSLastLockPredictorMetadata.queryingMechanism
+ _OBJC_IVAR_$__OSLastLockPredictorMetadata.recommendedRequeryTime
+ _OBJC_IVAR_$__OSLastLockPredictorMetadata.requireEnoughHistory
+ _OBJC_IVAR_$__OSLastLockPredictorOutput._confidenceLevel
+ _OBJC_IVAR_$__OSLastLockPredictorOutput._confidenceValue
+ _OBJC_IVAR_$__OSLastLockPredictorOutput._outputReason
+ _OBJC_IVAR_$__OSLastLockPredictorOutput._predictedDuration
+ _OBJC_METACLASS_$__OSBatteryTimeTillDischargeOutput
+ _OBJC_METACLASS_$__OSDayDrainResult
+ _OBJC_METACLASS_$__OSIAutoLPMManager
+ _OBJC_METACLASS_$__OSIBLMAnalyticsHandler
+ _OBJC_METACLASS_$__OSIBLMState
+ _OBJC_METACLASS_$__OSIBLManager
+ _OBJC_METACLASS_$__OSIBLMitigation
+ _OBJC_METACLASS_$__OSIBatteryLifeManager
+ _OBJC_METACLASS_$__OSICLPCInterface
+ _OBJC_METACLASS_$__OSITimeSeriesUtilities
+ _OBJC_METACLASS_$__OSLastLockPredictionClient
+ _OBJC_METACLASS_$__OSLastLockPredictorMetadata
+ _OBJC_METACLASS_$__OSLastLockPredictorOutput
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _PPSCreateTelemetryIdentifier
+ _PPSSendTelemetry
+ __OBJC_$_CLASS_METHODS__OSBatteryTimeTillDischargeOutput
+ __OBJC_$_CLASS_METHODS__OSDayDrainResult
+ __OBJC_$_CLASS_METHODS__OSIAutoLPMManager
+ __OBJC_$_CLASS_METHODS__OSIBLMAnalyticsHandler
+ __OBJC_$_CLASS_METHODS__OSIBLMState
+ __OBJC_$_CLASS_METHODS__OSIBLManager
+ __OBJC_$_CLASS_METHODS__OSIBLMitigation
+ __OBJC_$_CLASS_METHODS__OSIBatteryLifeManager
+ __OBJC_$_CLASS_METHODS__OSICLPCInterface
+ __OBJC_$_CLASS_METHODS__OSITimeSeriesUtilities
+ __OBJC_$_CLASS_METHODS__OSLastLockPredictorMetadata
+ __OBJC_$_CLASS_METHODS__OSLastLockPredictorOutput
+ __OBJC_$_CLASS_PROP_LIST__OSBatteryTimeTillDischargeOutput
+ __OBJC_$_CLASS_PROP_LIST__OSDayDrainResult
+ __OBJC_$_CLASS_PROP_LIST__OSIBLMitigation
+ __OBJC_$_CLASS_PROP_LIST__OSLastLockPredictorMetadata
+ __OBJC_$_CLASS_PROP_LIST__OSLastLockPredictorOutput
+ __OBJC_$_INSTANCE_METHODS__OSBatteryTimeTillDischargeOutput
+ __OBJC_$_INSTANCE_METHODS__OSDayDrainResult
+ __OBJC_$_INSTANCE_METHODS__OSIAutoLPMManager
+ __OBJC_$_INSTANCE_METHODS__OSIBLMAnalyticsHandler
+ __OBJC_$_INSTANCE_METHODS__OSIBLMState
+ __OBJC_$_INSTANCE_METHODS__OSIBLManager
+ __OBJC_$_INSTANCE_METHODS__OSIBLMitigation
+ __OBJC_$_INSTANCE_METHODS__OSIBatteryLifeManager
+ __OBJC_$_INSTANCE_METHODS__OSICLPCInterface
+ __OBJC_$_INSTANCE_METHODS__OSLastLockPredictionClient
+ __OBJC_$_INSTANCE_METHODS__OSLastLockPredictorMetadata
+ __OBJC_$_INSTANCE_METHODS__OSLastLockPredictorOutput
+ __OBJC_$_INSTANCE_VARIABLES__OSBatteryTimeTillDischargeOutput
+ __OBJC_$_INSTANCE_VARIABLES__OSDayDrainResult
+ __OBJC_$_INSTANCE_VARIABLES__OSIAutoLPMManager
+ __OBJC_$_INSTANCE_VARIABLES__OSIBLMAnalyticsHandler
+ __OBJC_$_INSTANCE_VARIABLES__OSIBLMState
+ __OBJC_$_INSTANCE_VARIABLES__OSIBLManager
+ __OBJC_$_INSTANCE_VARIABLES__OSIBLMitigation
+ __OBJC_$_INSTANCE_VARIABLES__OSIBatteryLifeManager
+ __OBJC_$_INSTANCE_VARIABLES__OSICLPCInterface
+ __OBJC_$_INSTANCE_VARIABLES__OSLastLockPredictionClient
+ __OBJC_$_INSTANCE_VARIABLES__OSLastLockPredictorMetadata
+ __OBJC_$_INSTANCE_VARIABLES__OSLastLockPredictorOutput
+ __OBJC_$_PROP_LIST__OSBatteryTimeTillDischargeOutput
+ __OBJC_$_PROP_LIST__OSDayDrainResult
+ __OBJC_$_PROP_LIST__OSIAutoLPMManager
+ __OBJC_$_PROP_LIST__OSIBLMAnalyticsHandler
+ __OBJC_$_PROP_LIST__OSIBLMState
+ __OBJC_$_PROP_LIST__OSIBLManager
+ __OBJC_$_PROP_LIST__OSIBLMitigation
+ __OBJC_$_PROP_LIST__OSIBatteryLifeManager
+ __OBJC_$_PROP_LIST__OSICLPCInterface
+ __OBJC_$_PROP_LIST__OSLastLockPredictionClient
+ __OBJC_$_PROP_LIST__OSLastLockPredictorMetadata
+ __OBJC_$_PROP_LIST__OSLastLockPredictorMetadataProtocol
+ __OBJC_$_PROP_LIST__OSLastLockPredictorOutput
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FigCameraViewfinderDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FigCameraViewfinderDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FigCameraViewfinderSessionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__OSLastLockPredictionProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__OSLastLockPredictionProtocol_Private
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__OSLastLockPredictorMetadataProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FigCameraViewfinderDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FigCameraViewfinderSessionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES__OSLastLockPredictionProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES__OSLastLockPredictionProtocol_Private
+ __OBJC_$_PROTOCOL_METHOD_TYPES__OSLastLockPredictorMetadataProtocol
+ __OBJC_$_PROTOCOL_REFS_FigCameraViewfinderDelegate
+ __OBJC_$_PROTOCOL_REFS_FigCameraViewfinderSessionDelegate
+ __OBJC_$_PROTOCOL_REFS__OSLastLockPredictionProtocol
+ __OBJC_$_PROTOCOL_REFS__OSLastLockPredictionProtocol_Private
+ __OBJC_$_PROTOCOL_REFS__OSLastLockPredictorMetadataProtocol
+ __OBJC_CLASS_PROTOCOLS_$__OSBatteryTimeTillDischargeOutput
+ __OBJC_CLASS_PROTOCOLS_$__OSDayDrainResult
+ __OBJC_CLASS_PROTOCOLS_$__OSIBLManager
+ __OBJC_CLASS_PROTOCOLS_$__OSIBLMitigation
+ __OBJC_CLASS_PROTOCOLS_$__OSLastLockPredictionClient
+ __OBJC_CLASS_PROTOCOLS_$__OSLastLockPredictorMetadata
+ __OBJC_CLASS_PROTOCOLS_$__OSLastLockPredictorOutput
+ __OBJC_CLASS_RO_$__OSBatteryTimeTillDischargeOutput
+ __OBJC_CLASS_RO_$__OSDayDrainResult
+ __OBJC_CLASS_RO_$__OSIAutoLPMManager
+ __OBJC_CLASS_RO_$__OSIBLMAnalyticsHandler
+ __OBJC_CLASS_RO_$__OSIBLMState
+ __OBJC_CLASS_RO_$__OSIBLManager
+ __OBJC_CLASS_RO_$__OSIBLMitigation
+ __OBJC_CLASS_RO_$__OSIBatteryLifeManager
+ __OBJC_CLASS_RO_$__OSICLPCInterface
+ __OBJC_CLASS_RO_$__OSITimeSeriesUtilities
+ __OBJC_CLASS_RO_$__OSLastLockPredictionClient
+ __OBJC_CLASS_RO_$__OSLastLockPredictorMetadata
+ __OBJC_CLASS_RO_$__OSLastLockPredictorOutput
+ __OBJC_LABEL_PROTOCOL_$_FigCameraViewfinderDelegate
+ __OBJC_LABEL_PROTOCOL_$_FigCameraViewfinderSessionDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$__OSLastLockPredictionProtocol
+ __OBJC_LABEL_PROTOCOL_$__OSLastLockPredictionProtocol_Private
+ __OBJC_LABEL_PROTOCOL_$__OSLastLockPredictorMetadataProtocol
+ __OBJC_METACLASS_RO_$__OSBatteryTimeTillDischargeOutput
+ __OBJC_METACLASS_RO_$__OSDayDrainResult
+ __OBJC_METACLASS_RO_$__OSIAutoLPMManager
+ __OBJC_METACLASS_RO_$__OSIBLMAnalyticsHandler
+ __OBJC_METACLASS_RO_$__OSIBLMState
+ __OBJC_METACLASS_RO_$__OSIBLManager
+ __OBJC_METACLASS_RO_$__OSIBLMitigation
+ __OBJC_METACLASS_RO_$__OSIBatteryLifeManager
+ __OBJC_METACLASS_RO_$__OSICLPCInterface
+ __OBJC_METACLASS_RO_$__OSITimeSeriesUtilities
+ __OBJC_METACLASS_RO_$__OSLastLockPredictionClient
+ __OBJC_METACLASS_RO_$__OSLastLockPredictorMetadata
+ __OBJC_METACLASS_RO_$__OSLastLockPredictorOutput
+ __OBJC_PROTOCOL_$_FigCameraViewfinderDelegate
+ __OBJC_PROTOCOL_$_FigCameraViewfinderSessionDelegate
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$__OSLastLockPredictionProtocol
+ __OBJC_PROTOCOL_$__OSLastLockPredictionProtocol_Private
+ __OBJC_PROTOCOL_$__OSLastLockPredictorMetadataProtocol
+ __OBJC_PROTOCOL_REFERENCE_$__OSLastLockPredictionProtocol_Private
+ ___21-[_OSIBLManager init]_block_invoke
+ ___21-[_OSIBLManager init]_block_invoke.53
+ ___21-[_OSIBLManager init]_block_invoke_2
+ ___21-[_OSIBLManager init]_block_invoke_2.56
+ ___22-[_OSIBLManager start]_block_invoke
+ ___22-[_OSIBLManager start]_block_invoke_2
+ ___22-[_OSIBLManager start]_block_invoke_2.cold.1
+ ___27-[_OSBatteryPredictor init]_block_invoke.72
+ ___27-[_OSBatteryPredictor init]_block_invoke.72.cold.1
+ ___27-[_OSIAutoLPMManager start]_block_invoke
+ ___27-[_OSIAutoLPMManager start]_block_invoke.23
+ ___27-[_OSIAutoLPMManager start]_block_invoke_2
+ ___27-[_OSIAutoLPMManager start]_block_invoke_2.24
+ ___27-[_OSIAutoLPMManager start]_block_invoke_2.cold.1
+ ___30+[_OSIBLMState sharedInstance]_block_invoke
+ ___30-[_OSIBatteryLifeManager init]_block_invoke
+ ___30-[_OSIBatteryLifeManager init]_block_invoke.4
+ ___30-[_OSIBatteryLifeManager init]_block_invoke.cold.1
+ ___31+[_OSIBLManager sharedInstance]_block_invoke
+ ___31-[_OSIBLMAnalyticsHandler init]_block_invoke
+ ___31-[_OSIBLMAnalyticsHandler init]_block_invoke_2
+ ___33-[_OSIBLMState monitorForAutoLPM]_block_invoke
+ ___33-[_OSIBLMState monitorForAutoLPM]_block_invoke_2
+ ___33-[_OSIBLMState monitorForAutoLPM]_block_invoke_3
+ ___33-[_OSIBLMState willEnableAutoLPM]_block_invoke
+ ___35+[_OSICLPCInterface sharedInstance]_block_invoke
+ ___36+[_OSIAutoLPMManager sharedInstance]_block_invoke
+ ___38-[_OSChargingPredictor initConnection]_block_invoke.58
+ ___38-[_OSChargingPredictor initConnection]_block_invoke.58.cold.1
+ ___38-[_OSIBLManager updateTrialParameters]_block_invoke
+ ___38-[_OSIBLManager updateTrialParameters]_block_invoke.62
+ ___39-[_OSChargingPredictor fixModelOutput:]_block_invoke.66
+ ___39-[_OSIBLManager isIBLMCurrentlyEnabled]_block_invoke
+ ___40+[_OSIBatteryLifeManager sharedInstance]_block_invoke
+ ___40-[_OSChargingPredictor unfixModelOutput]_block_invoke.68
+ ___40-[_OSIBLMAnalyticsHandler dateFormatter]_block_invoke
+ ___41+[_OSIBLMAnalyticsHandler sharedInstance]_block_invoke
+ ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke
+ ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke.91
+ ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke.91.cold.1
+ ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke.91.cold.2
+ ___43-[_OSBatteryPredictor client:setIBLMState:]_block_invoke.cold.1
+ ___44-[_OSLastLockPredictionClient modelMetadata]_block_invoke
+ ___44-[_OSLastLockPredictionClient modelMetadata]_block_invoke.84
+ ___44-[_OSLastLockPredictionClient modelMetadata]_block_invoke.cold.1
+ ___45-[_OSLastLockPredictionClient initConnection]_block_invoke
+ ___45-[_OSLastLockPredictionClient initConnection]_block_invoke.72
+ ___45-[_OSLastLockPredictionClient initConnection]_block_invoke.cold.1
+ ___46-[_OSBatteryPredictor overrideAllMitigations:]_block_invoke
+ ___46-[_OSBatteryPredictor overrideAllMitigations:]_block_invoke.89
+ ___46-[_OSBatteryPredictor overrideAllMitigations:]_block_invoke.89.cold.1
+ ___46-[_OSBatteryPredictor overrideAllMitigations:]_block_invoke.cold.1
+ ___46-[_OSIBLMAnalyticsHandler recordAutoLPMState:]_block_invoke
+ ___46-[_OSIBLManager updateFeatureState:withError:]_block_invoke
+ ___46-[_OSIBLManager updateFeatureState:withError:]_block_invoke.cold.1
+ ___46-[_OSLastLockPredictionClient fixModelOutput:]_block_invoke
+ ___46-[_OSLastLockPredictionClient fixModelOutput:]_block_invoke.103
+ ___46-[_OSLastLockPredictionClient fixModelOutput:]_block_invoke.cold.1
+ ___47-[_OSBatteryPredictor overrideCLPCMitigations:]_block_invoke
+ ___47-[_OSBatteryPredictor overrideCLPCMitigations:]_block_invoke.90
+ ___47-[_OSBatteryPredictor overrideCLPCMitigations:]_block_invoke.90.cold.1
+ ___47-[_OSBatteryPredictor overrideCLPCMitigations:]_block_invoke.cold.1
+ ___47-[_OSLastLockPredictionClient modelDescription]_block_invoke
+ ___47-[_OSLastLockPredictionClient modelDescription]_block_invoke.80
+ ___47-[_OSLastLockPredictionClient modelDescription]_block_invoke.cold.1
+ ___47-[_OSLastLockPredictionClient unfixModelOutput]_block_invoke
+ ___47-[_OSLastLockPredictionClient unfixModelOutput]_block_invoke.106
+ ___47-[_OSLastLockPredictionClient unfixModelOutput]_block_invoke.cold.1
+ ___48-[_OSBatteryDrainPredictor lastBatteryLevelDate]_block_invoke
+ ___48-[_OSBatteryDrainPredictor lastBatteryLevelDate]_block_invoke.58
+ ___48-[_OSBatteryDrainPredictor lastBatteryLevelDate]_block_invoke.cold.1
+ ___49-[_OSBatteryDrainPredictor lastBatteryLevelValue]_block_invoke
+ ___49-[_OSBatteryDrainPredictor lastBatteryLevelValue]_block_invoke.59
+ ___49-[_OSBatteryDrainPredictor lastBatteryLevelValue]_block_invoke.cold.1
+ ___50-[_OSBatteryPredictor recommendsAutoLPMWithError:]_block_invoke
+ ___50-[_OSBatteryPredictor recommendsAutoLPMWithError:]_block_invoke.93
+ ___50-[_OSBatteryPredictor recommendsAutoLPMWithError:]_block_invoke.93.cold.1
+ ___50-[_OSBatteryPredictor recommendsAutoLPMWithError:]_block_invoke.cold.1
+ ___50-[_OSIBLMAnalyticsHandler extractAndReportMetrics]_block_invoke
+ ___51-[_OSLastLockPredictionClient deviceUsageDiagnosis]_block_invoke
+ ___51-[_OSLastLockPredictionClient deviceUsageDiagnosis]_block_invoke.95
+ ___51-[_OSLastLockPredictionClient deviceUsageDiagnosis]_block_invoke.cold.1
+ ___51-[_OSLastLockPredictionClient restoreLastLockModel]_block_invoke
+ ___51-[_OSLastLockPredictionClient restoreLastLockModel]_block_invoke.115
+ ___51-[_OSLastLockPredictionClient restoreLastLockModel]_block_invoke.cold.1
+ ___53-[_OSLastLockPredictionClient recommendedRequeryTime]_block_invoke
+ ___53-[_OSLastLockPredictionClient recommendedRequeryTime]_block_invoke.76
+ ___53-[_OSLastLockPredictionClient recommendedRequeryTime]_block_invoke.cold.1
+ ___54-[_OSBatteryPredictor batteryLifeMitigationWithError:]_block_invoke
+ ___54-[_OSBatteryPredictor batteryLifeMitigationWithError:]_block_invoke.87
+ ___54-[_OSBatteryPredictor batteryLifeMitigationWithError:]_block_invoke.87.cold.1
+ ___54-[_OSBatteryPredictor batteryLifeMitigationWithError:]_block_invoke.cold.1
+ ___54-[_OSIBLMAnalyticsHandler historicalDrainDataForDate:]_block_invoke
+ ___54-[_OSIBLMAnalyticsHandler historicalDrainDataForDate:]_block_invoke.89
+ ___54-[_OSIBLMAnalyticsHandler historicalDrainDataForDate:]_block_invoke.cold.1
+ ___55-[_OSLastLockPredictionClient activityHistoryDiagnosis]_block_invoke
+ ___55-[_OSLastLockPredictionClient activityHistoryDiagnosis]_block_invoke.92
+ ___55-[_OSLastLockPredictionClient activityHistoryDiagnosis]_block_invoke.cold.1
+ ___55-[_OSLastLockPredictionClient hasEnoughActivityHistory]_block_invoke
+ ___55-[_OSLastLockPredictionClient hasEnoughActivityHistory]_block_invoke.88
+ ___55-[_OSLastLockPredictionClient hasEnoughActivityHistory]_block_invoke.cold.1
+ ___56-[_OSLastLockPredictionClient modelMetadataWithHandler:]_block_invoke
+ ___56-[_OSLastLockPredictionClient modelMetadataWithHandler:]_block_invoke.cold.1
+ ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke
+ ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke.93
+ ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke.94
+ ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke.cold.1
+ ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke_2
+ ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke_2.cold.1
+ ___58-[_OSLastLockPredictionClient fixModelOutput:withHandler:]_block_invoke
+ ___58-[_OSLastLockPredictionClient fixModelOutput:withHandler:]_block_invoke.cold.1
+ ___59-[_OSIBLMAnalyticsHandler historicalEngagementDataForDate:]_block_invoke
+ ___59-[_OSLastLockPredictionClient modelDescriptionWithHandler:]_block_invoke
+ ___59-[_OSLastLockPredictionClient modelDescriptionWithHandler:]_block_invoke.cold.1
+ ___59-[_OSLastLockPredictionClient unfixModelOutputWithHandler:]_block_invoke
+ ___59-[_OSLastLockPredictionClient unfixModelOutputWithHandler:]_block_invoke.cold.1
+ ___60-[_OSICLPCInterface updatePerformanceControlWithMitigation:]_block_invoke
+ ___60-[_OSICLPCInterface updatePerformanceControlWithMitigation:]_block_invoke.cold.1
+ ___60-[_OSICLPCInterface updatePerformanceControlWithMitigation:]_block_invoke.cold.2
+ ___60-[_OSLastLockPredictionClient restoreRecommendedRequeryTime]_block_invoke
+ ___60-[_OSLastLockPredictionClient restoreRecommendedRequeryTime]_block_invoke.112
+ ___60-[_OSLastLockPredictionClient restoreRecommendedRequeryTime]_block_invoke.cold.1
+ ___62-[_OSBatteryPredictor highDayDrainAroundCurrentDateWithError:]_block_invoke
+ ___62-[_OSBatteryPredictor highDayDrainAroundCurrentDateWithError:]_block_invoke.85
+ ___62-[_OSBatteryPredictor highDayDrainAroundCurrentDateWithError:]_block_invoke.85.cold.1
+ ___62-[_OSBatteryPredictor highDayDrainAroundCurrentDateWithError:]_block_invoke.cold.1
+ ___63-[_OSLastLockPredictionClient deviceUsageDiagnosisWithHandler:]_block_invoke
+ ___63-[_OSLastLockPredictionClient deviceUsageDiagnosisWithHandler:]_block_invoke.cold.1
+ ___63-[_OSLastLockPredictionClient restoreLastLockModelWithHandler:]_block_invoke
+ ___63-[_OSLastLockPredictionClient restoreLastLockModelWithHandler:]_block_invoke.cold.1
+ ___64-[_OSLastLockPredictionClient overrideRecommendedRequeryTimeTo:]_block_invoke
+ ___64-[_OSLastLockPredictionClient overrideRecommendedRequeryTimeTo:]_block_invoke.109
+ ___64-[_OSLastLockPredictionClient overrideRecommendedRequeryTimeTo:]_block_invoke.cold.1
+ ___65-[_OSChargingPredictor chargePredictionOutputOfScheme:withError:]_block_invoke.62
+ ___65-[_OSChargingPredictor chargePredictionOutputOfScheme:withError:]_block_invoke.62.cold.1
+ ___65-[_OSIBLMAnalyticsHandler recordMitigationUpdateTo:fromPrevious:]_block_invoke
+ ___65-[_OSLastLockPredictionClient lastLockPredictionResultWithError:]_block_invoke
+ ___65-[_OSLastLockPredictionClient lastLockPredictionResultWithError:]_block_invoke.98
+ ___65-[_OSLastLockPredictionClient lastLockPredictionResultWithError:]_block_invoke.cold.1
+ ___65-[_OSLastLockPredictionClient recommendedRequeryTimeWithHandler:]_block_invoke
+ ___65-[_OSLastLockPredictionClient recommendedRequeryTimeWithHandler:]_block_invoke.cold.1
+ ___67-[_OSLastLockPredictionClient activityHistoryDiagnosisWithHandler:]_block_invoke
+ ___67-[_OSLastLockPredictionClient activityHistoryDiagnosisWithHandler:]_block_invoke.cold.1
+ ___67-[_OSLastLockPredictionClient hasEnoughActivityHistoryWithHandler:]_block_invoke
+ ___67-[_OSLastLockPredictionClient hasEnoughActivityHistoryWithHandler:]_block_invoke.cold.1
+ ___67-[_OSLastLockPredictionClient lastLockPredictionResultWithHandler:]_block_invoke
+ ___67-[_OSLastLockPredictionClient lastLockPredictionResultWithHandler:]_block_invoke.cold.1
+ ___72-[_OSLastLockPredictionClient restoreRecommendedRequeryTimeWithHandler:]_block_invoke
+ ___72-[_OSLastLockPredictionClient restoreRecommendedRequeryTimeWithHandler:]_block_invoke.cold.1
+ ___76-[_OSLastLockPredictionClient overrideRecommendedRequeryTimeTo:withHandler:]_block_invoke
+ ___76-[_OSLastLockPredictionClient overrideRecommendedRequeryTimeTo:withHandler:]_block_invoke.cold.1
+ ___82-[_OSChargingPredictor timeUntilNextChargeSessionOfMinDuration:fromSOC:WithError:]_block_invoke
+ ___82-[_OSChargingPredictor timeUntilNextChargeSessionOfMinDuration:fromSOC:WithError:]_block_invoke.64
+ ___82-[_OSChargingPredictor timeUntilNextChargeSessionOfMinDuration:fromSOC:WithError:]_block_invoke.64.cold.1
+ ___82-[_OSChargingPredictor timeUntilNextChargeSessionOfMinDuration:fromSOC:WithError:]_block_invoke.cold.1
+ ___92-[_OSLastLockPredictionClient lastLockPredictionResultAtDate:withTimeSinceActive:withError:]_block_invoke
+ ___92-[_OSLastLockPredictionClient lastLockPredictionResultAtDate:withTimeSinceActive:withError:]_block_invoke.100
+ ___92-[_OSLastLockPredictionClient lastLockPredictionResultAtDate:withTimeSinceActive:withError:]_block_invoke.cold.1
+ ___94-[_OSBatteryPredictor typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withError:]_block_invoke
+ ___94-[_OSBatteryPredictor typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withError:]_block_invoke.83
+ ___94-[_OSBatteryPredictor typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withError:]_block_invoke.83.cold.1
+ ___94-[_OSBatteryPredictor typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withError:]_block_invoke.cold.1
+ ___94-[_OSLastLockPredictionClient lastLockPredictionResultAtDate:withTimeSinceActive:withHandler:]_block_invoke
+ ___94-[_OSLastLockPredictionClient lastLockPredictionResultAtDate:withTimeSinceActive:withHandler:]_block_invoke.cold.1
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e38_v16?0"_OSLastLockPredictorMetadata"8lr32l8
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e31_v16?0"BGRepeatingSystemTask"8ls32l8
+ ___block_descriptor_40_e8_32s_e35_v24?0"NSString"8"NSDictionary"16ls32l8
+ ___block_descriptor_40_e8_32s_e50_v32?0"NSString"8?<v?"_OSIBLMitigation">16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32s_e8_v12?0i8ls32l8
+ ___block_descriptor_40_e8_32w_e38_v16?0"<TRINamespaceUpdateProtocol>"8lw32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32r40r_e48_v24?0"_OSLastLockPredictorOutput"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_64_e8_32r40r48r56r_e22_v16?0"BMStoreEvent"8lr32l8r40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40r48r_e20_v20?0B8"NSError"12ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40r48r_e30_v24?0"NSNumber"8"NSError"16ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40r48r_e38_v24?0"_OSIBLMitigation"8"NSError"16ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40r48r_e39_v24?0"_OSDayDrainResult"8"NSError"16ls32l8r40l8r48l8
+ ___block_descriptor_72_e8_32s40r48r56r64r_e22_v16?0"BMStoreEvent"8lr40l8r48l8r56l8r64l8s32l8
+ ___block_literal_global.102
+ ___block_literal_global.105
+ ___block_literal_global.106
+ ___block_literal_global.108
+ ___block_literal_global.111
+ ___block_literal_global.119
+ ___block_literal_global.121
+ ___block_literal_global.125
+ ___block_literal_global.127
+ ___block_literal_global.131
+ ___block_literal_global.79
+ ___block_literal_global.83
+ ___block_literal_global.87
+ ___block_literal_global.91
+ ___block_literal_global.94
+ ___block_literal_global.97
+ ___kCFBooleanFalse
+ __os_feature_enabled_impl
+ _dateFormatter.formatter
+ _dateFormatter.onceToken
+ _dispatch_async
+ _dispatch_get_global_queue
+ _dispatch_once
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_create
+ _dispatch_sync
+ _gLastLockPredictionClientLog
+ _kCFPreferencesAnyHost
+ _kCFPreferencesAnyUser
+ _kIBLMChangeNotification
+ _kIBLMDefaultsDomain
+ _kIOMainPortDefault
+ _kInvalidPredictedLastLockDuration
+ _kPMLPMSourceIBLM
+ _monitorForAutoLPM.onceToken
+ _notify_get_state
+ _notify_post
+ _notify_register_check
+ _notify_register_dispatch
+ _notify_set_state
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_getProperty
+ _objc_msgSend$PluggedIn
+ _objc_msgSend$activityHistoryDiagnosisWithHandler:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addUpdateHandlerForNamespaceName:usingBlock:
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$batteryExternalConnectedKey
+ _objc_msgSend$batteryLifeMitigationWithError:
+ _objc_msgSend$batteryLifeMitigationWithHandler:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$boolValue
+ _objc_msgSend$booleanValue
+ _objc_msgSend$cameraViewfinder
+ _objc_msgSend$cancelTask
+ _objc_msgSend$cancelTaskRequestWithIdentifier:error:
+ _objc_msgSend$client:setIBLMState:
+ _objc_msgSend$client:setIBLMState:withHandler:
+ _objc_msgSend$clientToHandler
+ _objc_msgSend$clientWithIdentifier:
+ _objc_msgSend$consoleModeNotificationHandler
+ _objc_msgSend$context
+ _objc_msgSend$createClient:
+ _objc_msgSend$date
+ _objc_msgSend$dateFormatter
+ _objc_msgSend$dateFromString:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$debugDescription
+ _objc_msgSend$decisionMaker
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$defaults
+ _objc_msgSend$dictionary
+ _objc_msgSend$didEnableAutoLPM
+ _objc_msgSend$disengageAutoLPM
+ _objc_msgSend$doubleValue
+ _objc_msgSend$engageAutoLPM
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$evaluate
+ _objc_msgSend$evaluateAutoLPMEngagement
+ _objc_msgSend$extractAndReportMetrics
+ _objc_msgSend$featureEngagementMetricsFromDrainData:engagementData:
+ _objc_msgSend$getValue:size:
+ _objc_msgSend$handleCLPCTestOverride:
+ _objc_msgSend$handleFeatureDisabled
+ _objc_msgSend$handleFeatureEnabled
+ _objc_msgSend$handleTestOverride:
+ _objc_msgSend$hasEnoughActivityHistoryWithHandler:
+ _objc_msgSend$hasPerformanceControlService
+ _objc_msgSend$highDayDrainAroundCurrentDateWithError:
+ _objc_msgSend$highDayDrainAroundCurrentDateWithHandler:
+ _objc_msgSend$historicalClassification
+ _objc_msgSend$historicalDrainDataForDate:
+ _objc_msgSend$historicalEngagementDataForDate:
+ _objc_msgSend$historicalPluggedInDataForDate:
+ _objc_msgSend$hour
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithIsHighDrain:confidence:
+ _objc_msgSend$initWithLevel:decisionMaker:decisionMakerString:confidence:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$integerValue
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isHighDrain
+ _objc_msgSend$isIBLMCurrentlyEnabled
+ _objc_msgSend$isIBLMDefaultOn
+ _objc_msgSend$isIBLMSupported
+ _objc_msgSend$isLPMEnabled
+ _objc_msgSend$isPluggedIn
+ _objc_msgSend$keyPathForBatteryLevel
+ _objc_msgSend$keyPathForBatteryStateDataDictionary
+ _objc_msgSend$keyPathForLowPowerModeStatus
+ _objc_msgSend$keyPathForPluginStatus
+ _objc_msgSend$lastBatteryLevelDate
+ _objc_msgSend$lastBatteryLevelValue
+ _objc_msgSend$lastLockPredictionResultAtDate:withTimeSinceActive:withHandler:
+ _objc_msgSend$lastLockPredictionResultWithHandler:
+ _objc_msgSend$level
+ _objc_msgSend$levelForFactor:withNamespaceName:
+ _objc_msgSend$loadCurrentIBLMState
+ _objc_msgSend$loadNumberForPreferenceKey:
+ _objc_msgSend$localWakingRegistrationWithIdentifier:contextualPredicate:clientIdentifier:callback:
+ _objc_msgSend$midnightDateFrom:
+ _objc_msgSend$minute
+ _objc_msgSend$mitigationWithError:
+ _objc_msgSend$mitigationWithLevel:
+ _objc_msgSend$notifyMitigationChange:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$overrideAllMitigations:
+ _objc_msgSend$overrideAllMitigations:withHandler:
+ _objc_msgSend$overrideCLPCMitigations:
+ _objc_msgSend$overrideCLPCMitigations:withHandler:
+ _objc_msgSend$overrideRecommendedRequeryTimeTo:withHandler:
+ _objc_msgSend$ppsIDForSubsystem:category:
+ _objc_msgSend$predicateForChangeAtKeyPath:
+ _objc_msgSend$predicateForKeyPath:withFormat:
+ _objc_msgSend$predictMitigationLevelWithError:
+ _objc_msgSend$predictor
+ _objc_msgSend$publisher
+ _objc_msgSend$queryAndUpdateCurrentConsoleModeState
+ _objc_msgSend$queue
+ _objc_msgSend$recommendedRequeryTime
+ _objc_msgSend$recommendedRequeryTimeWithHandler:
+ _objc_msgSend$recommendsAutoLPMWithError:
+ _objc_msgSend$recommendsAutoLPMWithHandler:
+ _objc_msgSend$recordAnalyticsFeatureState:
+ _objc_msgSend$recordAutoLPMState:
+ _objc_msgSend$recordFeatureState:
+ _objc_msgSend$recordMitigationUpdateTo:fromPrevious:
+ _objc_msgSend$registerCallback:
+ _objc_msgSend$registerForTaskWithIdentifier:usingQueue:launchHandler:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$reportDailyFeatureState
+ _objc_msgSend$resetMitigation
+ _objc_msgSend$restoreLastLockModelWithHandler:
+ _objc_msgSend$restoreRecommendedRequeryTimeWithHandler:
+ _objc_msgSend$saveCurrentIBLMState:
+ _objc_msgSend$saveNumber:forKey:
+ _objc_msgSend$sendDataToPPS:subsystem:category:
+ _objc_msgSend$setAutoLPMEngagement:
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setDateStyle:
+ _objc_msgSend$setDecisionMakerString:
+ _objc_msgSend$setDelegate:queue:
+ _objc_msgSend$setDidEnableAutoLPM:
+ _objc_msgSend$setExpirationHandler:
+ _objc_msgSend$setIntelligentBatteryLifeMode:options:error:
+ _objc_msgSend$setInterval:
+ _objc_msgSend$setLevel:
+ _objc_msgSend$setMinDurationBetweenInstances:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setPowerMode:fromSource:
+ _objc_msgSend$setPriority:
+ _objc_msgSend$setRequiresExternalPower:
+ _objc_msgSend$setTaskCompleted
+ _objc_msgSend$setTimeStyle:
+ _objc_msgSend$setTimeZone:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$sharedLog
+ _objc_msgSend$sharedScheduler
+ _objc_msgSend$shouldOverrideMitigations
+ _objc_msgSend$start
+ _objc_msgSend$startWithOptions:
+ _objc_msgSend$starting
+ _objc_msgSend$stop
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$submitTask
+ _objc_msgSend$submitTaskRequest:error:
+ _objc_msgSend$supportsPerformanceControl
+ _objc_msgSend$systemTimeZone
+ _objc_msgSend$testOverridenMitigation
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$timeUntilNextChargeSessionOfMinDuration:fromSOC:withHandler:
+ _objc_msgSend$timestamp
+ _objc_msgSend$typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withError:
+ _objc_msgSend$typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withHandler:
+ _objc_msgSend$updateMitigationTo:
+ _objc_msgSend$updatePerformanceControlWithMitigation:
+ _objc_msgSend$updateTrialParameters
+ _objc_msgSend$userContext
+ _objc_msgSend$value:withObjCType:
+ _objc_release_x1
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainBlock
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_setProperty_atomic
+ _os_transaction_create
+ _sharedInstance.instance
+ _sharedInstance.onceToken
- GCC_except_table20
- ___27-[_OSBatteryPredictor init]_block_invoke.49
- ___27-[_OSBatteryPredictor init]_block_invoke.49.cold.1
- ___38-[_OSChargingPredictor initConnection]_block_invoke.55
- ___38-[_OSChargingPredictor initConnection]_block_invoke.55.cold.1
- ___39-[_OSChargingPredictor fixModelOutput:]_block_invoke.61
- ___40-[_OSChargingPredictor unfixModelOutput]_block_invoke.63
- ___65-[_OSChargingPredictor chargePredictionOutputOfScheme:withError:]_block_invoke.59
- ___65-[_OSChargingPredictor chargePredictionOutputOfScheme:withError:]_block_invoke.59.cold.1
CStrings:
+ "!"
+ "### Last Lock Predictor\n- Model Type: %@\n- How to Query: %@\n- Requery Time: %.2f minutes\n- Definition of Long Inactivity: >%.2f hours\n- Confidence Spectrum: 0 --- low --- %.2f --- medium --- %.2f --- high --- 1"
+ "%@-%@"
+ "<_OSBatteryTimeTillDischargeOutput: Predicted discharge time %lf>"
+ "<_OSDayDrainResult: Is High Drain %d, confidence %lf>"
+ "<_OSIBLMitigation: Level %ld, Decision maker %@>"
+ "@\"<CLPCPolicyAccess>\""
+ "@\"<_CDLocalContext>\""
+ "@\"FigCameraViewfinder\""
+ "@\"NSDate\""
+ "@\"NSDictionary\"8@?0"
+ "@\"NSMutableDictionary\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSUserDefaults\""
+ "@\"TRIClient\""
+ "@\"_OSIBLMitigation\""
+ "@24@0:8^{_NSZone=}16"
+ "@28@0:8B16d20"
+ "@32@0:8@16@24"
+ "@32@0:8@16d24"
+ "@40@0:8@16d24^@32"
+ "@40@0:8Q16Q24^@32"
+ "@48@0:8q16q24@32d40"
+ "AppleCLPC"
+ "AutoLPMManager"
+ "AutoLPMManager initiating..."
+ "B24@0:8^@16"
+ "B32@0:8q16^@24"
+ "CLPCInterface"
+ "COREOS_PREDICTION_BATTERY"
+ "Canceling task %@"
+ "Connection to last lock predictor interrupted"
+ "Connection to last lock predictor invalidated"
+ "Console Mode Status is now %llu"
+ "Console Mode active"
+ "Creating PPS ID for %@"
+ "Current OSIBLMitigation %@"
+ "DecisionMaker"
+ "Device currently plugged in. Reseting IBLM mitigation"
+ "DeviceClass"
+ "Disengaged Auto LPM"
+ "Disengaging Auto LPM"
+ "Disengaging from IBLM mitigation for CLPC"
+ "Engaged Auto LPM"
+ "Engaging Auto LPM"
+ "Engaging into IBLM mitigation for CLPC"
+ "Error fetching changed OSIBLMitigation %@"
+ "Error getting battery stream in batteryLevelDurations: %s"
+ "Error getting biome battery events - %@"
+ "Error getting high drain prediction %@"
+ "Error in diagnosing the device usage frequency synchronously: %@"
+ "Error in diagnosing the device usage frequency: %@"
+ "Error in diagnosing user activity history synchronously: %@"
+ "Error in diagnosing user activity history: %@"
+ "Error in diagnosing user inactivity history synchronously: %@"
+ "Error in diagnosing user inactivity history: %@"
+ "Error in getting last lock activity prediction at date %@ with time since active %.2f: %@"
+ "Error in getting last lock prediction at date %@ with time since active %.2f synchronously: %@"
+ "Error in getting last lock prediction synchronously: %@"
+ "Error in getting last lock prediction: %@"
+ "Error in getting last lock predictor description synchronously: %@"
+ "Error in getting last lock predictor description: %@"
+ "Error in getting last lock predictor metadata synchronously: %@"
+ "Error in getting last lock predictor metadata: %@"
+ "Error in getting the recommended requery time for model synchronously: %@"
+ "Error in getting the recommended requery time: %@"
+ "Error in overriding the recommended requery time synchronously: %@"
+ "Error in overriding the recommended requery time: %@"
+ "Error in restoring the appropriate last lock predictor variant synchronously: %@"
+ "Error in restoring the appropriate last lock predictor variant: %@"
+ "Error in restoring the recommended requery time synchronously: %@"
+ "Error in restoring the recommended requery time: %@"
+ "Error setting up CLPC client"
+ "Error setting/clearing IBLM performance control mitigation %@"
+ "Error: No CLPC client"
+ "Error: Unsupported feature state %ld"
+ "Evaluating for Drain prediction"
+ "Expiration for %@"
+ "Failed to cancel task with error: %@"
+ "Failed to disengage Auto LPM"
+ "Failed to engaged Auto LPM"
+ "Failed to set state to %lu"
+ "Failed to submit task with error: %@"
+ "FeatureEngagementState"
+ "FeatureState"
+ "FigCameraViewfinderDelegate"
+ "FigCameraViewfinderSessionDelegate"
+ "For %lu intervals spanning from %@ to %@: \n found %lu lois and %lu visits \n associated %d intervals with lois"
+ "IBLM currently disabled. Skipping evaluation"
+ "IBLM falling back to default state %lu"
+ "IBLM is disabled by Trial. Skipping start"
+ "IBLM state from defaults is %lu"
+ "IBLM switch is disabled. Falling back to default LPM behavior"
+ "IBLM switch is disabled. Skipping Auto LPM"
+ "IBLMFeatureEngagement"
+ "IBLMFeatureState"
+ "IBLM_FeatureEnabled"
+ "IBLM_MitigationsEnabled"
+ "IBLM_PerformanceMitigationEnabled"
+ "IBLManager"
+ "Invalid PPS subsystem & category specified!"
+ "Is PluggedIn %ld "
+ "LPM is already enabled. Skipping Auto LPM"
+ "LPM on. Skipping evaluation for drain prediction"
+ "NSCopying"
+ "Nil payload. Nothing to send to PPS."
+ "No PPSTelemetryIdentifier provided!"
+ "OSIBLMState"
+ "OSIBLManager initiating..."
+ "OSIBatteryLifeManager"
+ "OSIPrediction"
+ "OSIntelligence"
+ "PluggedIn"
+ "Reporting %@ to PPS"
+ "Returning test overridden mitigation"
+ "SELF.%@.value = %@"
+ "SELF.%@.value == %@ OR SELF.%@.value == %@"
+ "Sending IBLM CA event: %@"
+ "Server error executing %@: %@"
+ "Set IBLM state to %lu from %@"
+ "Setting IBLM mitigation to %@"
+ "State updated to %ld from %ld"
+ "T@\"<CLPCPolicyAccess>\",&,V_clpcClient"
+ "T@\"<_CDLocalContext>\",&,N,V_context"
+ "T@\"FigCameraViewfinder\",&,N,V_viewFinder"
+ "T@\"NSDate\",&,N,V_lastEvaluateDate"
+ "T@\"NSDate\",&,N,V_lastMitigationChangeDate"
+ "T@\"NSMutableDictionary\",&,N,V_clientToHandler"
+ "T@\"NSMutableDictionary\",&,N,V_subsystemToPPSID"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_featureStatusQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSString\",&,N,V_decisionMakerString"
+ "T@\"NSUserDefaults\",&,N,V_defaults"
+ "T@\"TRIClient\",&,N,V_trialClient"
+ "T@\"_OSIBLMitigation\",&,V_currentMitigation"
+ "TB,N,V_autoLPMEngagement"
+ "TB,N,V_didEnableAutoLPM"
+ "TB,N,V_isConsoleModeActive"
+ "TB,N,V_isHighDrain"
+ "TB,N,V_trialFeatureEnabled"
+ "TB,N,V_trialMitigationsEnabled"
+ "TB,N,V_trialPerformanceMitigationEnabled"
+ "TB,N,V_viewfinderIsActive"
+ "Td,N,V_predictedDischargeTime"
+ "Td,N,VrecommendedRequeryTime"
+ "Test overrides in place. Skipping change in mitigations"
+ "Ti,N,V_consoleModeNotifyToken"
+ "Ti,N,V_notifyTestToken"
+ "Ti,N,V_notifyToken"
+ "Tq,N,V_currentFeatureState"
+ "Tq,N,V_decisionMaker"
+ "Tq,N,V_level"
+ "Trial overriding mitigation %ld"
+ "Trial: %@:%d"
+ "Unsupported featureState for analytics %ld"
+ "Updated IBLM Mitigation from %ld to %ld"
+ "Viewfinder camera active"
+ "[Last Lock Prediction] <Level: %@ | Value: %@ | Duration: %@ | Reason: %@>"
+ "^{PPSTelemetryIdentifier=}"
+ "^{PPSTelemetryIdentifier=}32@0:8@16@24"
+ "_OSBatteryTimeTillDischargeOutput"
+ "_OSDayDrainResult"
+ "_OSIAutoLPMManager"
+ "_OSIBLMAnalyticsHandler"
+ "_OSIBLMState"
+ "_OSIBLManager"
+ "_OSIBLMitigation"
+ "_OSIBatteryLifeManager"
+ "_OSICLPCInterface"
+ "_OSITimeSeriesUtilities"
+ "_OSLastLockPredictionClient"
+ "_OSLastLockPredictionProtocol"
+ "_OSLastLockPredictionProtocol_Private"
+ "_OSLastLockPredictorMetadata"
+ "_OSLastLockPredictorMetadataProtocol"
+ "_OSLastLockPredictorOutput"
+ "_autoLPMEngagement"
+ "_clientToHandler"
+ "_clpcClient"
+ "_consoleModeNotifyToken"
+ "_context"
+ "_currentFeatureState"
+ "_currentMitigation"
+ "_decisionMaker"
+ "_decisionMakerString"
+ "_defaults"
+ "_didEnableAutoLPM"
+ "_featureStatusQueue"
+ "_isConsoleModeActive"
+ "_isHighDrain"
+ "_lastEvaluateDate"
+ "_lastMitigationChangeDate"
+ "_level"
+ "_notifyTestToken"
+ "_notifyToken"
+ "_predictedDischargeTime"
+ "_queue"
+ "_subsystemToPPSID"
+ "_trialClient"
+ "_trialFeatureEnabled"
+ "_trialMitigationsEnabled"
+ "_trialPerformanceMitigationEnabled"
+ "_viewFinder"
+ "_viewfinderIsActive"
+ "activityHistoryDiagnosis"
+ "activityHistoryDiagnosisWithHandler:"
+ "addEntriesFromDictionary:"
+ "addUpdateHandlerForNamespaceName:usingBlock:"
+ "allocWithZone:"
+ "ambrosia"
+ "analyticsHandler"
+ "autoLPMEngagement"
+ "autoLPMState"
+ "batteryExternalConnectedKey"
+ "batteryLifeMitigationWithError:"
+ "batteryLifeMitigationWithHandler:"
+ "boolForKey:"
+ "boolValue"
+ "booleanValue"
+ "cameraViewfinder"
+ "cameraViewfinder:viewfinderSessionDidBegin:"
+ "cameraViewfinder:viewfinderSessionDidEnd:"
+ "cameraViewfinder:viewfinderSessionWillBegin:"
+ "cameraViewfinderSession:didCapturePhotoWithStatus:thumbnailData:timestamp:"
+ "cameraViewfinderSession:previewStreamDidCloseWithStatus:"
+ "cameraViewfinderSessionDidFinishMovieRecording:"
+ "cameraViewfinderSessionDidStartMovieRecording:"
+ "cameraViewfinderSessionPreviewStreamDidOpen:"
+ "cancelTask"
+ "cancelTaskRequestWithIdentifier:error:"
+ "client:setIBLMState:"
+ "client:setIBLMState:withHandler:"
+ "clientToHandler"
+ "clientWithIdentifier:"
+ "clpcClient"
+ "com.apple.OSIntelligence.lastlock"
+ "com.apple.osintelligence.OSIAutoLPMManager"
+ "com.apple.osintelligence.OSIBLManager"
+ "com.apple.osintelligence.OSIBLManager.featureStatus"
+ "com.apple.osintelligence.clpcinterface"
+ "com.apple.osintelligence.iblm"
+ "com.apple.osintelligence.iblm.AutoLPMState"
+ "com.apple.osintelligence.iblm.LPMState"
+ "com.apple.osintelligence.iblm.analytics"
+ "com.apple.osintelligence.iblm.analyticsHandler"
+ "com.apple.osintelligence.iblm.autoLPM"
+ "com.apple.osintelligence.iblm.autoLPMQuery"
+ "com.apple.osintelligence.iblm.batteryLifeManager"
+ "com.apple.osintelligence.iblm.contextstore-registration"
+ "com.apple.osintelligence.iblm.dailyAnalytics"
+ "com.apple.osintelligence.iblm.dailyMetrics"
+ "com.apple.osintelligence.iblm.evaluate"
+ "com.apple.osintelligence.iblm.historicalDrainDataForDate"
+ "com.apple.osintelligence.iblm.historicalPluggedInDataForDate"
+ "com.apple.osintelligence.iblm.mitigationchanged"
+ "com.apple.osintelligence.iblm.pluggedInState"
+ "com.apple.osintelligence.iblm.recordMitigationUpdate"
+ "com.apple.osintelligence.iblm.state"
+ "com.apple.osintelligence.iblmState.contextstore-registration"
+ "com.apple.system.console_mode_changed"
+ "consoleModeNotificationHandler"
+ "consoleModeNotifyToken"
+ "context"
+ "copyWithZone:"
+ "createClient:"
+ "currentFeatureState"
+ "currentMitigation"
+ "currentMitigationWithError:"
+ "d40@0:8d16q24^@32"
+ "dailyBatteryLevelConsumed"
+ "dailyChargeUp"
+ "dailyDrain"
+ "dailyEngagementCount"
+ "dailyEngagementDurationMins"
+ "dailyMinBatteryLevel"
+ "dailyPluggedInCount"
+ "dailyPluggedInTime"
+ "date"
+ "dateFormatter"
+ "dateFromString:"
+ "dateWithTimeIntervalSinceNow:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "decisionMaker"
+ "decisionMakerString"
+ "decodeObjectForKey:"
+ "defaults"
+ "dictionary"
+ "didEnableAutoLPM"
+ "didEngage"
+ "didEngageAutoLPM"
+ "disengageAutoLPM"
+ "doubleValue"
+ "engageAutoLPM"
+ "engagementFalseNegative"
+ "engagementFalsePositive"
+ "engagementTrueNegative"
+ "engagementTruePositive"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "evaluate"
+ "evaluateAutoLPMEngagement"
+ "extractAndReportMetrics"
+ "featureEngagementMetricsFromDrainData:engagementData:"
+ "featureStatusQueue"
+ "getValue:size:"
+ "handleCLPCTestOverride:"
+ "handleFeatureDisabled"
+ "handleFeatureEnabled"
+ "handleTestOverride:"
+ "hasEnoughActivityHistory"
+ "hasEnoughActivityHistoryWithHandler:"
+ "hasPerformanceControlService"
+ "highBatteryDrainComparedtoHourlyAggregate"
+ "highDayDrainAroundCurrentDateWithError:"
+ "highDayDrainAroundCurrentDateWithHandler:"
+ "historicalDrainDataForDate:"
+ "historicalEngagementDataForDate:"
+ "historicalIBLMEngagement"
+ "historicalPluggedInDataForDate:"
+ "hour"
+ "iPhone"
+ "initWithIdentifier:"
+ "initWithIsHighDrain:confidence:"
+ "initWithLevel:decisionMaker:decisionMakerString:confidence:"
+ "initWithSuiteName:"
+ "integerValue"
+ "isConsoleModeActive"
+ "isEqualToString:"
+ "isFeatureEnabled"
+ "isFeatureSupported"
+ "isHighDrain"
+ "isIBLMCurrentlyEnabled"
+ "isIBLMDefaultOn"
+ "isIBLMSupported"
+ "isLPMEnabled"
+ "isPluggedIn"
+ "isiPhone"
+ "kLastIBLMMitigationChangeDate"
+ "keyPathForBatteryLevel"
+ "keyPathForBatteryStateDataDictionary"
+ "keyPathForLowPowerModeStatus"
+ "keyPathForPluginStatus"
+ "lastBatteryLevelDate"
+ "lastBatteryLevelValue"
+ "lastEngagementDate"
+ "lastEvaluateDate"
+ "lastIBLMFeatureState"
+ "lastLock.predictionclient"
+ "lastLockPredictionResultAtDate:withTimeSinceActive:withError:"
+ "lastLockPredictionResultAtDate:withTimeSinceActive:withHandler:"
+ "lastLockPredictionResultWithError:"
+ "lastLockPredictionResultWithHandler:"
+ "lastMitigationChangeDate"
+ "lastMitigationLevel"
+ "level"
+ "levelForFactor:withNamespaceName:"
+ "loadCurrentIBLMState"
+ "loadNumberForPreferenceKey:"
+ "localWakingRegistrationWithIdentifier:contextualPredicate:clientIdentifier:callback:"
+ "midnightDateFrom:"
+ "minute"
+ "mitigationWithError:"
+ "mitigationWithLevel:"
+ "monitorForAutoLPM"
+ "notifyMitigationChange:"
+ "notifyTestToken"
+ "notifyToken"
+ "notify_get_state() failed with error %u"
+ "numberWithBool:"
+ "numberWithDouble:"
+ "numberWithInt:"
+ "numberWithUnsignedInteger:"
+ "objectForKey:"
+ "overrideAllMitigations:"
+ "overrideAllMitigations:withHandler:"
+ "overrideCLPCMitigations:"
+ "overrideCLPCMitigations:withHandler:"
+ "overrideRecommendedRequeryTimeTo:"
+ "overrideRecommendedRequeryTimeTo:withHandler:"
+ "ppsIDForSubsystem:category:"
+ "predicateForChangeAtKeyPath:"
+ "predicateForKeyPath:withFormat:"
+ "predictMitigationLevelWithError:"
+ "predictedDischargeTime"
+ "predictedTimeTillDischargeWithHandler:"
+ "publisher"
+ "queryAndUpdateCurrentConsoleModeState"
+ "queue"
+ "recommendedRequeryTime"
+ "recommendedRequeryTimeWithHandler:"
+ "recommendsAutoLPMWithError:"
+ "recommendsAutoLPMWithHandler:"
+ "recordAnalyticsFeatureState:"
+ "recordAutoLPMState:"
+ "recordFeatureState:"
+ "recordMitigationUpdateTo:fromPrevious:"
+ "registerCallback:"
+ "registerForDrainLevelPredictionForClient:withithUpdateHandler:"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "removeObjectForKey:"
+ "reportDailyFeatureState"
+ "resampleTimeSeries:withFrequency:"
+ "resetMitigation"
+ "restoreLastLockModel"
+ "restoreLastLockModelWithHandler:"
+ "restoreRecommendedRequeryTime"
+ "restoreRecommendedRequeryTimeWithHandler:"
+ "saveCurrentIBLMState:"
+ "saveNumber:forKey:"
+ "sendDataToPPS:subsystem:category:"
+ "setAutoLPMEngagement:"
+ "setBool:forKey:"
+ "setClientToHandler:"
+ "setClpcClient:"
+ "setConsoleModeNotifyToken:"
+ "setContext:"
+ "setCurrentFeatureState:"
+ "setCurrentMitigation:"
+ "setDateStyle:"
+ "setDecisionMaker:"
+ "setDecisionMakerString:"
+ "setDefaults:"
+ "setDelegate:queue:"
+ "setDidEnableAutoLPM:"
+ "setExpirationHandler:"
+ "setFeatureStatusQueue:"
+ "setIntelligentBatteryLifeMode:options:error:"
+ "setInterval:"
+ "setIsConsoleModeActive:"
+ "setIsHighDrain:"
+ "setLastEvaluateDate:"
+ "setLastMitigationChangeDate:"
+ "setLevel:"
+ "setMinDurationBetweenInstances:"
+ "setNotifyTestToken:"
+ "setNotifyToken:"
+ "setObject:forKey:"
+ "setPowerMode:fromSource:"
+ "setPredictedDischargeTime:"
+ "setPriority:"
+ "setQueue:"
+ "setRecommendedRequeryTime:"
+ "setRequiresExternalPower:"
+ "setSubsystemToPPSID:"
+ "setTaskCompleted"
+ "setTimeStyle:"
+ "setTimeZone:"
+ "setTrialClient:"
+ "setTrialFeatureEnabled:"
+ "setTrialMitigationsEnabled:"
+ "setTrialPerformanceMitigationEnabled:"
+ "setViewFinder:"
+ "setViewfinderIsActive:"
+ "sharedInstance"
+ "sharedLog"
+ "sharedScheduler"
+ "shouldOverrideMitigations"
+ "skipping highBatteryDrainComparedtoHourlyAggregate."
+ "start"
+ "startWithOptions:"
+ "starting"
+ "stop"
+ "stringFromDate:"
+ "submitTask"
+ "submitTaskRequest:error:"
+ "subsystemToPPSID"
+ "supportsPerformanceControl"
+ "systemTimeZone"
+ "testOverrideCLPCMitigationAlways"
+ "testOverrideMitigationAlways"
+ "testOverridenMitigation"
+ "timeIntervalSinceNow"
+ "timeUntilNextChargeSessionOfMinDuration:fromSOC:WithError:"
+ "timeUntilNextChargeSessionOfMinDuration:fromSOC:withHandler:"
+ "timestamp"
+ "trialClient"
+ "trialFeatureEnabled"
+ "trialMitigationsEnabled"
+ "trialPerformanceMitigationEnabled"
+ "typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withError:"
+ "typicalBatteryLevelWithReferenceDays:aggregatedOverTimeWidth:withHandler:"
+ "updateFeatureState:withError:"
+ "updateMitigationTo:"
+ "updatePerformanceControlWithMitigation:"
+ "updateTrialParameters"
+ "userContext"
+ "v12@?0i8"
+ "v16@?0@\"<TRINamespaceUpdateProtocol>\"8"
+ "v16@?0@\"BGRepeatingSystemTask\"8"
+ "v16@?0@\"_OSLastLockPredictorMetadata\"8"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@\"FigCameraViewfinderSession\"16"
+ "v24@0:8@?<v@?@\"_OSBatteryTimeTillDischargeOutput\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"_OSDayDrainResult\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"_OSIBLMitigation\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"_OSLastLockPredictorMetadata\">16"
+ "v24@0:8@?<v@?@\"_OSLastLockPredictorOutput\"@\"NSError\">16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v24@0:8Q16"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "v24@?0@\"NSString\"8@\"NSDictionary\"16"
+ "v24@?0@\"_OSDayDrainResult\"8@\"NSError\"16"
+ "v24@?0@\"_OSIBLMitigation\"8@\"NSError\"16"
+ "v24@?0@\"_OSLastLockPredictorOutput\"8@\"NSError\"16"
+ "v28@0:8@\"FigCameraViewfinderSession\"16i24"
+ "v28@0:8@16i24"
+ "v32@0:8@\"FigCameraViewfinder\"16@\"FigCameraViewfinderSession\"24"
+ "v32@0:8@\"_OSLastLockPredictorOutput\"16@?<v@?@\"NSString\">24"
+ "v32@0:8@16@24"
+ "v32@0:8@16q24"
+ "v32@0:8q16@?<v@?@\"NSError\">24"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "v32@?0@\"NSString\"8@?<v@?@\"_OSIBLMitigation\">16^B24"
+ "v40@0:8@\"NSDate\"16d24@?<v@?@\"_OSLastLockPredictorOutput\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16q24@?<v@?B@\"NSError\">32"
+ "v40@0:8@16@24@32"
+ "v40@0:8@16d24@?32"
+ "v40@0:8@16q24@?32"
+ "v40@0:8Q16Q24@?32"
+ "v40@0:8Q16Q24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8d16q24@?32"
+ "v40@0:8d16q24@?<v@?@\"NSNumber\"@\"NSError\">32"
+ "v60@0:8@\"FigCameraViewfinderSession\"16i24@\"NSData\"28{?=qiIq}36"
+ "v60@0:8@16i24@28{?=qiIq}36"
+ "value:withObjCType:"
+ "viewFinder"
+ "viewfinderIsActive"
+ "willEnableAutoLPM"
- "Error in diagnozing the device usage frequency synchronously: %@"
- "Error in diagnozing the device usage frequency: %@"
- "Error in diagnozing user inactivity history synchronously: %@"
- "Error in diagnozing user inactivity history: %@"
- "For %lu intervals spanning from %@ to %@: \n found %lu lois and %lu visits \n assosciated %d intervals with lois"

```
