## ActionPredictionHeuristicsInternal

> `/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/Versions/A/ActionPredictionHeuristicsInternal`

```diff

-584.9.0.0.0
-  __TEXT.__text: 0x432a8
+588.11.0.0.0
+  __TEXT.__text: 0x43580
   __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_methlist: 0x25ec
+  __TEXT.__objc_methlist: 0x2954
   __TEXT.__const: 0x328
-  __TEXT.__cstring: 0x30fd
-  __TEXT.__gcc_except_tab: 0xe1c
+  __TEXT.__cstring: 0x3105
+  __TEXT.__gcc_except_tab: 0xe18
   __TEXT.__oslogstring: 0x68e1
   __TEXT.__dlopen_cstrs: 0x1a0
-  __TEXT.__unwind_info: 0xdd0
+  __TEXT.__unwind_info: 0xe20
   __TEXT.__objc_classname: 0xc7c
   __TEXT.__objc_methname: 0x7737
   __TEXT.__objc_methtype: 0x1150
   __TEXT.__objc_stubs: 0x6a40
   __DATA_CONST.__got: 0x860
-  __DATA_CONST.__const: 0x410
+  __DATA_CONST.__const: 0x430
   __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d10
+  __DATA_CONST.__objc_selrefs: 0x1da0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x228
   __DATA_CONST.__objc_arraydata: 0x120
   __AUTH_CONST.__auth_got: 0x388
-  __AUTH_CONST.__const: 0x1180
+  __AUTH_CONST.__const: 0x11a0
   __AUTH_CONST.__cfstring: 0x3400
-  __AUTH_CONST.__objc_const: 0x9fc8
+  __AUTH_CONST.__objc_const: 0x9968
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0x1ef0
   __DATA.__objc_ivar: 0x2e4
   __DATA.__data: 0x380
-  __DATA.__bss: 0x368
+  __DATA.__bss: 0x378
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation

   - /System/Library/PrivateFrameworks/VoiceShortcutClient.framework/Versions/A/VoiceShortcutClient
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0F32D0A4-B7C8-3C7E-828F-A6429C364F29
-  Functions: 1107
-  Symbols:   3691
-  CStrings:  2722
+  UUID: 5B2FC923-4B37-39D1-AEFA-EDF0FC0BD71F
+  Functions: 1175
+  Symbols:   3761
+  CStrings:  2723
 
Symbols:
+ +[ATXContextHeuristicSuggestionProducer _mediaWithName:type:adamIdentifier:umcIdentifier:predictionReasons:localizedReason:score:expirationDate:].cold.1
+ +[ATXEventTravelTimeDataSourceInternal sharedInstance].cold.1
+ +[ATXHeuristicAirportCity cityForAirport:language:].cold.1
+ +[ATXHeuristicDevice sharedAlarmManager].cold.1
+ +[ATXHeuristicResultCache sharedInstance].cold.1
+ +[ATXIntentToAppBundleIdCache sharedInstance].cold.1
+ +[ATXWalletDataSourceSharedData sharedInstance].cold.1
+ -[ATXContextFlightEventSuggestionProducer suggestionForFlightCheckInWithReason:score:].cold.1
+ -[ATXContextFlightEventSuggestionProducer suggestionForFlightCheckInWithReason:score:].cold.2
+ -[ATXContextFlightEventSuggestionProducer suggestionForFlightInformationWithReason:score:date:].cold.1
+ -[ATXHeuristicCacheExpirationEntry initWithHeuristic:cache:].cold.1
+ -[ATXHeuristicCacheExpirationEntry initWithHeuristic:cache:].cold.2
+ -[ATXHeuristicCacheNotificationExpirer initDarwin:].cold.1
+ -[ATXHeuristicCacheNotificationExpirer initLocal:].cold.1
+ -[ATXHeuristicCacheTimeExpirer initWithFireDate:].cold.1
+ -[ATXHeuristicDataSourcesServer initWithDevice:].cold.1
+ -[ATXHeuristicDevice _calendarVisibilityManager].cold.1
+ -[ATXHeuristicNowPlaying initWithPersistenceIdentifier:].cold.1
+ ATXHeuristicDataSourcesInterface.cold.1
+ __112-[ATXUserAppPreferenceDataSource preferredAppForIntentName:andParameterCombination:skipAppSchemaCheck:callback:]_block_invoke.23
+ __112-[ATXUserAppPreferenceDataSource preferredAppForIntentName:andParameterCombination:skipAppSchemaCheck:callback:]_block_invoke.23.cold.1
+ __112-[ATXUserAppPreferenceDataSource preferredAppForIntentName:andParameterCombination:skipAppSchemaCheck:callback:]_block_invoke.25
+ __159-[ATXEventTravelTimeDataSourceInternal travelTimeInfoForEventID:location:expectedArrivalDate:transportType:localOnlyAfterFirstUpdate:heuristicDevice:callback:]_block_invoke.41
+ __159-[ATXEventTravelTimeDataSourceInternal travelTimeInfoForEventID:location:expectedArrivalDate:transportType:localOnlyAfterFirstUpdate:heuristicDevice:callback:]_block_invoke.41.cold.1
+ __31-[ATXHeuristicResultCache init]_block_invoke.198
+ __31-[ATXHeuristicResultCache init]_block_invoke.198.cold.1
+ __31-[ATXHeuristicResultCache init]_block_invoke.200
+ __31-[ATXHeuristicResultCache init]_block_invoke.200.cold.1
+ __46-[ATXHeuristicCacheNotificationExpirer _start]_block_invoke.82
+ __51-[ATXHeuristicResultCache _observeUserFocusChanges]_block_invoke.208
+ __52-[ATXInformationHeuristicRefreshBiomeTrigger _start]_block_invoke.195
+ __54-[ATXHeuristicResultCache isFocusModeActiveWithError:]_block_invoke.213
+ __56-[ATXHeuristicNowPlaying initWithPersistenceIdentifier:]_block_invoke.28
+ __57-[ATXHeuristicReturnCall heuristicResultWithEnvironment:]_block_invoke.35
+ __58-[ATXHeuristicRecentEvent heuristicResultWithEnvironment:]_block_invoke.18
+ __60-[ATXHeuristicUpcomingEvent heuristicResultWithEnvironment:]_block_invoke.21
+ __60-[ATXInformationHeuristicRefreshNotitifcationTrigger _start]_block_invoke.105
+ __63-[ATXAlarmsDataSource alarmsFromDate:toDate:completionHandler:]_block_invoke.16
+ __63-[ATXAlarmsDataSource alarmsFromDate:toDate:completionHandler:]_block_invoke.19
+ __63-[ATXAlarmsDataSource alarmsFromDate:toDate:completionHandler:]_block_invoke.19.cold.1
+ __74-[ATXSetAlarmTimeOfDayDataSource _recentIntentDonationsForBundleId:limit:]_block_invoke.11
+ __74-[ATXSetAlarmTimeOfDayDataSource _recentIntentDonationsForBundleId:limit:]_block_invoke.11.cold.1
+ __74-[ATXSetAlarmTimeOfDayDataSource _recentIntentDonationsForBundleId:limit:]_block_invoke.13
+ __78-[ATXCalendarEventsDataSource calendarEventsFromStartDate:toEndDate:callback:]_block_invoke.25
+ __80-[ATXIntentToAppBundleIdCache _slowlyFetchBundleIdsForIntent:completionHandler:]_block_invoke.17
+ __82-[ATXBestContactHandleForServiceDataSource bestHandleForContact:service:callback:]_block_invoke.42
+ __92+[ATXHeuristicFlightEventUtilities fetchDestinationPlacemarkForFlightEvent:heuristicDevice:]_block_invoke.201
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
+ __block_literal_global.207
+ __block_literal_global.30
- GCC_except_table12
- __112-[ATXUserAppPreferenceDataSource preferredAppForIntentName:andParameterCombination:skipAppSchemaCheck:callback:]_block_invoke.17
- __112-[ATXUserAppPreferenceDataSource preferredAppForIntentName:andParameterCombination:skipAppSchemaCheck:callback:]_block_invoke.17.cold.1
- __112-[ATXUserAppPreferenceDataSource preferredAppForIntentName:andParameterCombination:skipAppSchemaCheck:callback:]_block_invoke.19
- __159-[ATXEventTravelTimeDataSourceInternal travelTimeInfoForEventID:location:expectedArrivalDate:transportType:localOnlyAfterFirstUpdate:heuristicDevice:callback:]_block_invoke.29
- __159-[ATXEventTravelTimeDataSourceInternal travelTimeInfoForEventID:location:expectedArrivalDate:transportType:localOnlyAfterFirstUpdate:heuristicDevice:callback:]_block_invoke.35.cold.1
- __31-[ATXHeuristicResultCache init]_block_invoke.192
- __31-[ATXHeuristicResultCache init]_block_invoke.192.cold.1
- __31-[ATXHeuristicResultCache init]_block_invoke.194
- __31-[ATXHeuristicResultCache init]_block_invoke.194.cold.1
- __46-[ATXHeuristicCacheNotificationExpirer _start]_block_invoke.76
- __51-[ATXHeuristicResultCache _observeUserFocusChanges]_block_invoke.202
- __52-[ATXInformationHeuristicRefreshBiomeTrigger _start]_block_invoke.189
- __54-[ATXHeuristicResultCache isFocusModeActiveWithError:]_block_invoke.207
- __56-[ATXHeuristicNowPlaying initWithPersistenceIdentifier:]_block_invoke.22
- __57-[ATXHeuristicReturnCall heuristicResultWithEnvironment:]_block_invoke.29
- __58-[ATXHeuristicRecentEvent heuristicResultWithEnvironment:]_block_invoke.12
- __60-[ATXHeuristicUpcomingEvent heuristicResultWithEnvironment:]_block_invoke.15
- __60-[ATXInformationHeuristicRefreshNotitifcationTrigger _start]_block_invoke.99
- __63-[ATXAlarmsDataSource alarmsFromDate:toDate:completionHandler:]_block_invoke.10
- __63-[ATXAlarmsDataSource alarmsFromDate:toDate:completionHandler:]_block_invoke.13
- __63-[ATXAlarmsDataSource alarmsFromDate:toDate:completionHandler:]_block_invoke.13.cold.1
- __74-[ATXSetAlarmTimeOfDayDataSource _recentIntentDonationsForBundleId:limit:]_block_invoke.5
- __74-[ATXSetAlarmTimeOfDayDataSource _recentIntentDonationsForBundleId:limit:]_block_invoke.5.cold.1
- __74-[ATXSetAlarmTimeOfDayDataSource _recentIntentDonationsForBundleId:limit:]_block_invoke.7
- __78-[ATXCalendarEventsDataSource calendarEventsFromStartDate:toEndDate:callback:]_block_invoke.19
- __80-[ATXIntentToAppBundleIdCache _slowlyFetchBundleIdsForIntent:completionHandler:]_block_invoke.11
- __82-[ATXBestContactHandleForServiceDataSource bestHandleForContact:service:callback:]_block_invoke.36
- __92+[ATXHeuristicFlightEventUtilities fetchDestinationPlacemarkForFlightEvent:heuristicDevice:]_block_invoke.192
- __block_literal_global.14
- __block_literal_global.201
- __block_literal_global.24
CStrings:
+ "carPlay"

```
