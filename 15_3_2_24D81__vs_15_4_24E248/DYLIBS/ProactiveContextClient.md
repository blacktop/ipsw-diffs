## ProactiveContextClient

> `/System/Library/PrivateFrameworks/ProactiveContextClient.framework/Versions/A/ProactiveContextClient`

```diff

-584.9.0.0.0
-  __TEXT.__text: 0x2b700
+588.11.0.0.0
+  __TEXT.__text: 0x2baa8
   __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_methlist: 0x2274
+  __TEXT.__objc_methlist: 0x28e4
   __TEXT.__const: 0x420
-  __TEXT.__gcc_except_tab: 0x1020
-  __TEXT.__cstring: 0x208d
+  __TEXT.__gcc_except_tab: 0x101c
+  __TEXT.__cstring: 0x2095
   __TEXT.__oslogstring: 0x3793
   __TEXT.__dlopen_cstrs: 0x9f
-  __TEXT.__unwind_info: 0xe28
+  __TEXT.__unwind_info: 0xe40
   __TEXT.__objc_classname: 0x982
   __TEXT.__objc_methname: 0x5afc
   __TEXT.__objc_methtype: 0x1622

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1508
+  __DATA_CONST.__objc_selrefs: 0x15f8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x130
   __AUTH_CONST.__auth_got: 0x270
-  __AUTH_CONST.__const: 0x1840
+  __AUTH_CONST.__const: 0x1860
   __AUTH_CONST.__cfstring: 0x1ce0
-  __AUTH_CONST.__objc_const: 0xa680
+  __AUTH_CONST.__objc_const: 0x9ac8
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH.__objc_data: 0x15e0
   __DATA.__objc_ivar: 0x2cc
   __DATA.__data: 0x840
-  __DATA.__bss: 0x2f8
+  __DATA.__bss: 0x308
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation
   - /System/Library/Frameworks/CoreMotion.framework/Versions/A/CoreMotion

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 42207951-AE21-314D-8638-F8126A23EC79
-  Functions: 1139
-  Symbols:   3291
-  CStrings:  2007
+  UUID: 92C91799-16EB-3BE3-8BE0-AC0032D4C581
+  Functions: 1196
+  Symbols:   3354
+  CStrings:  2008
 
Symbols:
+ +[ATXMotionManagerWrapper hasMotionActivity].cold.1
+ +[ATXMotionManagerWrapper sharedInstance].cold.1
+ -[ATXLocationManager initWithGPS:routine:stateStore:now:modeGlobals:].cold.1
+ -[ATXLocationManager initWithGPS:routine:stateStore:now:modeGlobals:].cold.2
+ -[ATXLocationManager initWithGPS:routine:stateStore:now:modeGlobals:].cold.3
+ -[ATXLocationManagerGPSCoreLocation stateForRegion:withTimeout:].cold.1
+ -[ATXLocationManagerGPSCoreLocation updateLocationWithTimeout:requestPreciseLocation:].cold.1
+ -[ATXLocationManagerStateStoreOnDisk initWithPath:environment:locationParameters:].cold.1
+ -[ATXLocationManagerStateStoreOnDisk initWithPath:environment:locationParameters:].cold.2
+ -[ATXLocationManagerStateStoreOnDiskEnv callOnNextUnlock:].cold.1
+ -[ATXLocationOfInterest initWithUUID:visits:coordinate:type:city:].cold.1
+ -[ATXModeClassifier init].cold.2
+ -[ATXModeHeuristicClassifier initWithFeaturizers:minUpdateInterval:configuredModeService:].cold.2
+ __116-[ATXLocationManagerRoutineCR fetchNextPredictedLOIFromLocation:startDate:timeInterval:requireHighConfidence:reply:]_block_invoke.8
+ __39-[ATXUserFocusComputedMode currentMode]_block_invoke.16
+ __39-[ATXUserFocusInferredMode currentMode]_block_invoke.12
+ __42-[ATXModeBedtimeFeaturizer beginListening]_block_invoke.21
+ __42-[ATXModeRoutineFeaturizer beginListening]_block_invoke.21
+ __43-[ATXModeBedtimeFeaturizer provideFeatures]_block_invoke.12
+ __43-[ATXModeRoutineFeaturizer provideFeatures]_block_invoke.12
+ __43-[ATXUserFocusComputedMode currentModeUUID]_block_invoke.22
+ __44-[ATXModeAppLaunchFeaturizer beginListening]_block_invoke.25
+ __44-[ATXModeAppLaunchFeaturizer beginListening]_block_invoke.30
+ __44-[ATXUserFocusComputedMode currentModeEvent]_block_invoke.19
+ __44-[ATXUserFocusInferredMode currentModeEvent]_block_invoke.16
+ __45-[ATXUserFocusInferredMode previousModeEvent]_block_invoke.19
+ __46-[ATXLocationManager updatePredictedExitTimes]_block_invoke.101
+ __46-[ATXModeScreenShareFeaturizer beginListening]_block_invoke.21
+ __47-[ATXModeScreenShareFeaturizer provideFeatures]_block_invoke.12
+ __48-[ATXModeMicrolocationFeaturizer beginListening]_block_invoke.36
+ __49-[ATXModeGameControllerFeaturizer beginListening]_block_invoke.21
+ __49-[ATXModeMicrolocationFeaturizer provideFeatures]_block_invoke.25
+ __50-[ATXModeGameControllerFeaturizer provideFeatures]_block_invoke.12
+ __50-[ATXModeScreenRecordingFeaturizer beginListening]_block_invoke.21
+ __51-[ATXLocationManager fetchLOILocationOfType:reply:]_block_invoke.78
+ __51-[ATXModeScreenRecordingFeaturizer provideFeatures]_block_invoke.12
+ __51-[ATXUserFocusComputedMode currentModeSemanticType]_block_invoke.12
+ __53-[ATXUserFocusInferredMode lastTwoInferredModeEvents]_block_invoke.24
+ __54-[ATXModeDrivingFeaturizer _fetchMostRecentDNDWDEvent]_block_invoke.12
+ __55-[ATXModeAppLaunchFeaturizer _latestAppLaunchBundleIds]_block_invoke.13
+ __55-[ATXModeDuetHelper modeStreamFrom:to:ascending:limit:]_block_invoke.45
+ __56-[ATXLocationManager updatePredictedLocationsOfInterest]_block_invoke.100
+ __56-[ATXUserFocusInferredMode currentModeEventAtGivenTime:]_block_invoke.30
+ __57-[ATXModeDrivingFeaturizer _beginListeningForDNDWDEvents]_block_invoke.20
+ __57-[ATXUserFocusComputedMode currrentModeEventAtGivenTime:]_block_invoke.32
+ __59-[ATXLocationManager getCurrentRoutineModeWithCurrentDate:]_block_invoke.110
+ __60-[ATXLocationManagerRoutineCR fetchRoutineModeFromLocation:]_block_invoke.15
+ __60-[ATXLocationManagerRoutineCR fetchRoutineModeFromLocation:]_block_invoke.15.cold.1
+ __62-[ATXLocationManager getCurrentLocationWithCompletionHandler:]_block_invoke.63
+ __63-[ATXUserFocusComputedMode lastTwoUserFocusComputedStoreEvents]_block_invoke.29
+ __64-[ATXUserFocusInferredMode inferredModeEventWithSuggestionUUID:]_block_invoke.25
+ __66-[ATXLocationManager updateCurrentLocationOfInterestIfTimeElapsed]_block_invoke.84
+ __73-[ATXModeAnchorModelSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.23
+ __73-[ATXModeAnchorModelSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.26
+ __86-[ATXPOICategoryEventAggregator groupVisitsFromPublisher:startTimestamp:endTimestamp:]_block_invoke.11
+ __86-[ATXPOICategoryEventAggregator groupVisitsFromPublisher:startTimestamp:endTimestamp:]_block_invoke.13
+ __86-[ATXPOICategoryEventAggregator groupVisitsFromPublisher:startTimestamp:endTimestamp:]_block_invoke.20
+ __86-[ATXPOICategoryEventAggregator groupVisitsFromPublisher:startTimestamp:endTimestamp:]_block_invoke_2.17
+ __86-[ATXPOICategoryEventAggregator groupVisitsFromPublisher:startTimestamp:endTimestamp:]_block_invoke_2.17.cold.1
+ _____atxlog_handle_carPlay_widgets_block_invoke
+ ___atxlog_handle_carPlay_widgets
+ __atxlog_handle_action_prediction.cold.1
+ __atxlog_handle_anchor.cold.1
+ __atxlog_handle_app_install.cold.1
+ __atxlog_handle_app_library.cold.1
+ __atxlog_handle_app_prediction.cold.1
+ __atxlog_handle_backup.cold.1
+ __atxlog_handle_blending.cold.1
+ __atxlog_handle_blending_ecosystem.cold.1
+ __atxlog_handle_blending_internal_cache.cold.1
+ __atxlog_handle_carPlay_widgets.cold.1
+ __atxlog_handle_carPlay_widgets.log
+ __atxlog_handle_carPlay_widgets.onceToken
+ __atxlog_handle_context_heuristic.cold.1
+ __atxlog_handle_context_user_education_suggestions.cold.1
+ __atxlog_handle_contextual_actions.cold.1
+ __atxlog_handle_contextual_engine.cold.1
+ __atxlog_handle_dailyroutines.cold.1
+ __atxlog_handle_default.cold.1
+ __atxlog_handle_deletions.cold.1
+ __atxlog_handle_feedback.cold.1
+ __atxlog_handle_gi.cold.1
+ __atxlog_handle_hero.cold.1
+ __atxlog_handle_heuristic.cold.1
+ __atxlog_handle_home_screen.cold.1
+ __atxlog_handle_intents_helper.cold.1
+ __atxlog_handle_lock_screen.cold.1
+ __atxlog_handle_metrics.cold.1
+ __atxlog_handle_modes.cold.1
+ __atxlog_handle_notification_categorization.cold.1
+ __atxlog_handle_notification_management.cold.1
+ __atxlog_handle_notifications.cold.1
+ __atxlog_handle_pmm.cold.1
+ __atxlog_handle_relevance_model.cold.1
+ __atxlog_handle_relevant_shortcut.cold.1
+ __atxlog_handle_settings_actions.cold.1
+ __atxlog_handle_sleep_schedule.cold.1
+ __atxlog_handle_time_intelligence.cold.1
+ __atxlog_handle_timeline.cold.1
+ __atxlog_handle_trial_assets.cold.1
+ __atxlog_handle_ui.cold.1
+ __atxlog_handle_usage_insights.cold.1
+ __atxlog_handle_watch.cold.1
+ __atxlog_handle_xpc.cold.1
+ __atxlog_handle_zkw_hide.cold.1
+ __block_literal_global.125
+ __block_literal_global.16
+ __block_literal_global.18
+ __block_literal_global.19
+ __block_literal_global.30
+ __block_literal_global.31
+ __block_literal_global.33
+ __block_literal_global.85
+ __block_literal_global.87
- __116-[ATXLocationManagerRoutineCR fetchNextPredictedLOIFromLocation:startDate:timeInterval:requireHighConfidence:reply:]_block_invoke.4
- __39-[ATXUserFocusComputedMode currentMode]_block_invoke.10
- __39-[ATXUserFocusInferredMode currentMode]_block_invoke.6
- __42-[ATXModeBedtimeFeaturizer beginListening]_block_invoke.15
- __42-[ATXModeRoutineFeaturizer beginListening]_block_invoke.15
- __43-[ATXModeBedtimeFeaturizer provideFeatures]_block_invoke.6
- __43-[ATXModeRoutineFeaturizer provideFeatures]_block_invoke.6
- __43-[ATXUserFocusComputedMode currentModeUUID]_block_invoke.16
- __44-[ATXModeAppLaunchFeaturizer beginListening]_block_invoke.19
- __44-[ATXModeAppLaunchFeaturizer beginListening]_block_invoke.24
- __44-[ATXUserFocusComputedMode currentModeEvent]_block_invoke.13
- __44-[ATXUserFocusInferredMode currentModeEvent]_block_invoke.10
- __45-[ATXUserFocusInferredMode previousModeEvent]_block_invoke.13
- __46-[ATXLocationManager updatePredictedExitTimes]_block_invoke.95
- __46-[ATXModeScreenShareFeaturizer beginListening]_block_invoke.15
- __47-[ATXModeScreenShareFeaturizer provideFeatures]_block_invoke.6
- __48-[ATXModeMicrolocationFeaturizer beginListening]_block_invoke.30
- __49-[ATXModeGameControllerFeaturizer beginListening]_block_invoke.15
- __49-[ATXModeMicrolocationFeaturizer provideFeatures]_block_invoke.19
- __50-[ATXModeGameControllerFeaturizer provideFeatures]_block_invoke.6
- __50-[ATXModeScreenRecordingFeaturizer beginListening]_block_invoke.15
- __51-[ATXLocationManager fetchLOILocationOfType:reply:]_block_invoke.72
- __51-[ATXModeScreenRecordingFeaturizer provideFeatures]_block_invoke.6
- __51-[ATXUserFocusComputedMode currentModeSemanticType]_block_invoke.6
- __53-[ATXUserFocusInferredMode lastTwoInferredModeEvents]_block_invoke.18
- __54-[ATXModeDrivingFeaturizer _fetchMostRecentDNDWDEvent]_block_invoke.6
- __55-[ATXModeAppLaunchFeaturizer _latestAppLaunchBundleIds]_block_invoke.7
- __55-[ATXModeDuetHelper modeStreamFrom:to:ascending:limit:]_block_invoke.39
- __56-[ATXLocationManager updatePredictedLocationsOfInterest]_block_invoke.94
- __56-[ATXUserFocusInferredMode currentModeEventAtGivenTime:]_block_invoke.24
- __57-[ATXModeDrivingFeaturizer _beginListeningForDNDWDEvents]_block_invoke.14
- __57-[ATXUserFocusComputedMode currrentModeEventAtGivenTime:]_block_invoke.26
- __59-[ATXLocationManager getCurrentRoutineModeWithCurrentDate:]_block_invoke.104
- __60-[ATXLocationManagerRoutineCR fetchRoutineModeFromLocation:]_block_invoke.11
- __60-[ATXLocationManagerRoutineCR fetchRoutineModeFromLocation:]_block_invoke.11.cold.1
- __62-[ATXLocationManager getCurrentLocationWithCompletionHandler:]_block_invoke.57
- __63-[ATXUserFocusComputedMode lastTwoUserFocusComputedStoreEvents]_block_invoke.23
- __64-[ATXUserFocusInferredMode inferredModeEventWithSuggestionUUID:]_block_invoke.19
- __66-[ATXLocationManager updateCurrentLocationOfInterestIfTimeElapsed]_block_invoke.78
- __73-[ATXModeAnchorModelSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.18
- __73-[ATXModeAnchorModelSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.19
- __86-[ATXPOICategoryEventAggregator groupVisitsFromPublisher:startTimestamp:endTimestamp:]_block_invoke.14
- __86-[ATXPOICategoryEventAggregator groupVisitsFromPublisher:startTimestamp:endTimestamp:]_block_invoke.5
- __86-[ATXPOICategoryEventAggregator groupVisitsFromPublisher:startTimestamp:endTimestamp:]_block_invoke.7
- __86-[ATXPOICategoryEventAggregator groupVisitsFromPublisher:startTimestamp:endTimestamp:]_block_invoke_2.11
- __86-[ATXPOICategoryEventAggregator groupVisitsFromPublisher:startTimestamp:endTimestamp:]_block_invoke_2.11.cold.1
- __block_literal_global.12
- __block_literal_global.14
- __block_literal_global.24
- __block_literal_global.27
- __block_literal_global.79
- __block_literal_global.81
- __block_literal_global.9
CStrings:
+ "carPlay"

```
