## NotesAccountNotificationPlugin

> `/System/Library/Accounts/Notification/NotesAccountNotificationPlugin.bundle/NotesAccountNotificationPlugin`

```diff

-2654.11.0.0.0
+2656.0.0.0.0
   __TEXT.__text: 0x7bf8
   __TEXT.__auth_stubs: 0x760
   __TEXT.__objc_methlist: 0x218

   __TEXT.__objc_methtype: 0x248
   __TEXT.__objc_stubs: 0xea0
   __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x2b0
+  __DATA_CONST.__const: 0x2f8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 172
-  Symbols:   179
-  CStrings:  187
+  Symbols:   188
+  CStrings:  0
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
- "CLASS_$_ATXAnchorModelPredictionSchedulerGuardedData"
- "S_$__ATXInspectionServer"
- "TACLASS_$_ATXCorrelationMatrixGuardedData"
- "_OBJC_CLASS_$_ATXAppClipSettingsUpdateSource"
- "_OBJC_CLASS_$_ATXAppClipUsageDuetContextUpdateListener"
- "_OBJC_CLASS_$_ATXAppClipUsageDuetDataProvider"
- "_OBJC_CLASS_$_ATXAppClipsFeedback"
- "_OBJC_CLASS_$_ATXAppDirectoryOrderingProvider"
- "_OBJC_CLASS_$_ATXAppDirectoryServer"
- "_OBJC_CLASS_$_ATXAppFeaturizer"
- "_OBJC_CLASS_$_ATXAppIntentMonitor"
- "_OBJC_CLASS_$_ATXAppLaunchLogger"
- "_OBJC_CLASS_$_ATXAppLaunchMicroLocation"
- "_OBJC_CLASS_$_ATXAppLaunchMicroLocationGuardedData"
- "_OBJC_CLASS_$_ATXAppPredictionBlacklist"
- "_OBJC_CLASS_$_ATXAudioConnectedAnchor"
- "_OBJC_CLASS_$_ATXAudioConnectedMMExpert"
- "_OBJC_CLASS_$_ATXAudioDisconnectedAnchor"
- "_OBJC_CLASS_$_ATXAudioDisconnectedMMExpert"
- "_OBJC_CLASS_$_ATXBBNotificationManager"
- "_OBJC_CLASS_$_ATXBTConnectedMMExpert"
- "_OBJC_CLASS_$_ATXBTDisconnectedMMExpert"
- "_OBJC_CLASS_$_ATXBackgroundSaver"
- "_OBJC_CLASS_$_ATXBackgroundSaverGuardedData"
- "_OBJC_CLASS_$_ATXBackupFileManager"
- "_OBJC_CLASS_$_ATXBackupService"
- "_OBJC_CLASS_$_ATXBlendingLayerSessionLogger"
- "_OBJC_CLASS_$_ATXBluetoothConnectedAnchor"
- "_OBJC_CLASS_$_ATXBluetoothDisconnectedAnchor"
- "_OBJC_CLASS_$_ATXCDNDownloaderTriggerManager"
- "_OBJC_CLASS_$_ATXCarPlayConnectedAnchor"
- "_OBJC_CLASS_$_ATXCarPlayConnectedMMExpert"
- "_OBJC_CLASS_$_ATXCarPlayDisconnectedAnchor"
- "_OBJC_CLASS_$_ATXCarPlayDisconnectedMMExpert"
- "_OBJC_CLASS_$_ATXChargerConnectedAnchor"
- "_OBJC_CLASS_$_ATXClientModelSuggestionReceiver"
- "_OBJC_CLASS_$_ATXClientModelSuggestionRouter"
- "_OBJC_CLASS_$_ATXCloudStorageSettingsListener"
- "_OBJC_CLASS_$_ATXContextSourcesGuardedData"
- "_OBJC_CLASS_$_ATXCurrentABGroupDetails"
- "_OBJC_CLASS_$_ATXDigitalHealthBlacklist"
- "_OBJC_CLASS_$_ATXDigitalHealthBlacklistGuardedData"
- "_OBJC_CLASS_$_ATXDuetCallbackGuardedData"
- "_OBJC_CLASS_$_ATXDuetDataProvider"
- "_OBJC_CLASS_$_ATXDuetGuardedRootOfAppData"
- "_OBJC_CLASS_$_ATXDuetKnowledgeStoreManager"
- "_OBJC_CLASS_$_ATXFeaturizedInfoSuggestion"
- "_OBJC_CLASS_$_ATXFileUtil"
- "_OBJC_CLASS_$_ATXGlobalAppScorePredictor"
- "_OBJC_CLASS_$_ATXGlobalAppScoresUtil"
- "_OBJC_CLASS_$_ATXGlobalSmartSuppression"
- "_OBJC_CLASS_$_ATXGuardedActionBlacklist"
- "_OBJC_CLASS_$_ATXGuardedAppBlacklist"
- "_OBJC_CLASS_$_ATXGuardedHistData"
- "_OBJC_CLASS_$_ATXHeroAppFeedback"
- "_OBJC_CLASS_$_ATXHeroAppManager"
- "_OBJC_CLASS_$_ATXHeuristicActionProducer"
- "_OBJC_CLASS_$_ATXHistogramBundleIdTable"
- "_OBJC_CLASS_$_ATXHistogramData"
- "_OBJC_CLASS_$_ATXHistogramTable"
- "_OBJC_CLASS_$_ATXHomeScreenSuggestionSender"
- "_OBJC_CLASS_$_ATXHomeScreenWidgetFeedback"
- "_OBJC_CLASS_$_ATXIdleTimeEndAnchor"
- "_OBJC_CLASS_$_ATXIdleTimeEndMMExpert"
- "_OBJC_CLASS_$_ATXInfoSuggestionCriterionRegistry"
- "_OBJC_CLASS_$_ATXInfoSuggestionServer"
- "_OBJC_CLASS_$_ATXInformationEngine"
- "_OBJC_CLASS_$_ATXInformationEngineGuardedData"
- "_OBJC_CLASS_$_ATXInformationFeatureSet"
- "_OBJC_CLASS_$_ATXInformationFeatureSetBuilder"
- "_OBJC_CLASS_$_ATXInformationFeatureWeights"
- "_OBJC_CLASS_$_ATXInformationFeaturizer"
- "_OBJC_CLASS_$_ATXInformationFilter"
- "_OBJC_CLASS_$_ATXInformationFilterGuardedData"
- "_OBJC_CLASS_$_ATXInformationProbabilisticRanker"
- "_OBJC_CLASS_$_ATXIntentMetadataCache"
- "_OBJC_CLASS_$_ATXIntentMetadataCacheInvalidationMonitor"
- "_OBJC_CLASS_$_ATXIntentMetadataCacheKey"
- "_OBJC_CLASS_$_ATXInternalAppRegistrationNotification"
- "_OBJC_CLASS_$_ATXInternalAppsInstallStartNotification"
- "_OBJC_CLASS_$_ATXInternalOffloadAppsNotification"
- "_OBJC_CLASS_$_ATXLockscreenBlacklist"
- "_OBJC_CLASS_$_ATXLockscreenBlacklistData"
- "_OBJC_CLASS_$_ATXMLActionProducer"
- "_OBJC_CLASS_$_ATXMMAppPredictionExpert"
- "_OBJC_CLASS_$_ATXMagicalMomentsAppPredictor"
- "_OBJC_CLASS_$_ATXMagicalMomentsUpdateMonitor"
- "_OBJC_CLASS_$_ATXManagedConfigurationUpdateSource"
- "_OBJC_CLASS_$_ATXMediaApplications"
- "_OBJC_CLASS_$_ATXNotificationsDedupeTracker"
- "_OBJC_CLASS_$_ATXNotificationsLoggingServer"
- "_OBJC_CLASS_$_ATXNudgeRegistrar"
- "_OBJC_CLASS_$_ATXPredictionContextBuilder"
- "_OBJC_CLASS_$_ATXPrivacyReset"
- "_OBJC_CLASS_$_ATXScoredInfoSuggestion"
- "_OBJC_CLASS_$_ATXScreenUnlockUpdateSource"
- "_OBJC_CLASS_$_ATXServer"
- "_OBJC_CLASS_$_ATXStackState"
- "_OBJC_CLASS_$_ATXStackStateTracker"
- "_OBJC_CLASS_$_ATXStackStateTrackerInternalState"
- "_OBJC_CLASS_$_ATXSuggestionDeduplicator"
- "_OBJC_CLASS_$_ATXSuggestionPreprocessor"
- "_OBJC_CLASS_$_ATXTimeBucketedRateLimiter"
- "_OBJC_CLASS_$_ATXTimeUtil"
- "_OBJC_CLASS_$_ATXTimelineAbuseControlConfig"
- "_OBJC_CLASS_$_ATXTimelineRelevance"
- "_OBJC_CLASS_$_ATXTimelineRelevanceFilter"
- "_OBJC_CLASS_$_ATXUpdatePredictionsLogger"
- "_OBJC_CLASS_$_ATXUpdatePredictionsManager"
- "_OBJC_CLASS_$_ATXUpdatePredictionsSources"
- "_OBJC_CLASS_$_ATXUtils"
- "_OBJC_CLASS_$_ATXWebClipDataStore"
- "_OBJC_CLASS_$_ATXWifiStateMonitor"
- "_OBJC_CLASS_$__ATXAggregateLogger"
- "_OBJC_CLASS_$__ATXAppDailyDose"
- "_OBJC_CLASS_$__ATXAppDailyDoseCurrentStore"
- "_OBJC_CLASS_$__ATXAppInfo"
- "_OBJC_CLASS_$__ATXAppInfoManager"
- "_OBJC_CLASS_$__ATXAppInstallMonitor"
- "_OBJC_CLASS_$__ATXAppLaunchCategoricalHistogram"
- "_OBJC_CLASS_$__ATXAppLaunchCategoricalHistogramWithPersistentBackup"
- "_OBJC_CLASS_$__ATXAppLaunchGuardedCDContext"
- "_OBJC_CLASS_$__ATXAppLaunchGuardedHistory"
- "_OBJC_CLASS_$__ATXAppLaunchHistogram"
- "_OBJC_CLASS_$__ATXNeuralNetwork"
- "_OBJC_CLASS_$__ATXScoreInterpreter"
- "_OBJC_CLASS_$__ATXScoreInterpreterCtx"
- "_OBJC_CLASS_$__ATXScoreTypes"
- "_OBJC_METACLASS_$_ATXAWDUtils"
- "_OBJC_METACLASS_$_ATXActionBlendingUpdater"
- "_OBJC_METACLASS_$_ATXActionCacheBuilder"
- "_OBJC_METACLASS_$_ATXActionCacheReader"
- "_OBJC_METACLASS_$_ATXActionFeedback"
- "_OBJC_METACLASS_$_ATXActionFeedbackWeights"
- "_OBJC_METACLASS_$_ATXActionLOIBoost"
- "_OBJC_METACLASS_$_ATXActionPredictionContainer"
- "_OBJC_METACLASS_$_ATXActionPredictions"
- "_OBJC_METACLASS_$_ATXActionPredictionsHelpers"
- "_OBJC_METACLASS_$_ATXActionResolution"
- "_OBJC_METACLASS_$_ATXActionResult"
- "_OBJC_METACLASS_$_ATXActionStatistics"
- "_OBJC_METACLASS_$_ATXActionValuation"
- "_OBJC_METACLASS_$_ATXAmbientLightMonitor"
- "_OBJC_METACLASS_$_ATXAppBlendingUpdater"
- "_OBJC_METACLASS_$_ATXAppPredictionFeedbackItem"
- "_OBJC_METACLASS_$_ATXAppPredictorFeedback"
- "_OBJC_METACLASS_$_ATXAppPredictorPredictionChunks"
- "_OBJC_METACLASS_$_ATXBehavioralPredictionsFeatureCache"
- "_OBJC_METACLASS_$_ATXBehavioralPredictionsFeatureCacheGuardedData"
- "_OBJC_METACLASS_$_ATXBiomePredictionContextStream"
- "_OBJC_METACLASS_$_ATXBlendedLocalAndGlobalScores"
- "_OBJC_METACLASS_$_ATXBoostObject"
- "_OBJC_METACLASS_$_ATXClientModelPredictionReasons"
- "_OBJC_METACLASS_$_ATXDeviceStateMonitor"
- "_OBJC_METACLASS_$_ATXDirichletDistribution"
- "_OBJC_METACLASS_$_ATXDisplayCacheLockscreenFilter"
- "_OBJC_METACLASS_$_ATXFallbackActionsFeedback"
- "_OBJC_METACLASS_$_ATXGroupHistogram"
- "_OBJC_METACLASS_$_ATXGroupHistogramEntry"
- "_OBJC_METACLASS_$_ATXGuardedActionPredictionContainerData"
- "_OBJC_METACLASS_$_ATXLocationToLaunchCorrelation"
- "_OBJC_METACLASS_$_ATXMPBCacheAgeAtCacheRefreshTracker"
- "_OBJC_METACLASS_$_ATXMagicalMomentsAppPredictorFeedback"
- "_OBJC_METACLASS_$_ATXMediaActionPrediction"
- "_OBJC_METACLASS_$_ATXMinimalSlotResolutionParameters"
- "_OBJC_METACLASS_$_ATXPBPredictionAmbientLightContext"
- "_OBJC_METACLASS_$_ATXPBPredictionContext"
- "_OBJC_METACLASS_$_ATXPBPredictionDeviceStateContext"
- "_OBJC_METACLASS_$_ATXPBPredictionLocationMotionContext"
- "_OBJC_METACLASS_$_ATXPBPredictionTimeContext"
- "_OBJC_METACLASS_$_ATXPBPredictionUserContext"
- "_OBJC_METACLASS_$_ATXPredictionAmbientLightContext"
- "_OBJC_METACLASS_$_ATXPredictionContext"
- "_OBJC_METACLASS_$_ATXPredictionContextDomain"
- "_OBJC_METACLASS_$_ATXPredictionDeviceStateContext"
- "_OBJC_METACLASS_$_ATXPredictionLocationMotionContext"
- "_OBJC_METACLASS_$_ATXPredictionTimeContext"
- "_OBJC_METACLASS_$_ATXPredictionUserContext"
- "_OBJC_METACLASS_$_ATXPrivacyPreservingLocationHash"
- "_OBJC_METACLASS_$_ATXProactiveSuggestionBuilder"
- "_OBJC_METACLASS_$_ATXScoreDict"
- "_OBJC_METACLASS_$_ATXScoreInterpreterCache"
- "_OBJC_METACLASS_$_ATXScoreInterpreterFromAssetBuilder"
- "_OBJC_METACLASS_$_ATXSlotResolution"
- "_OBJC_METACLASS_$_ATXSlotResolutionParametersStatistics"
- "asons"
- "ing"

```
