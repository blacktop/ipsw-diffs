## ProactiveSuggestionClientModel

> `/System/Library/PrivateFrameworks/ProactiveSuggestionClientModel.framework/Versions/A/ProactiveSuggestionClientModel`

```diff

-584.9.0.0.0
-  __TEXT.__text: 0x760d0
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0x7230
+588.11.0.0.0
+  __TEXT.__text: 0x75b98
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_methlist: 0x776c
   __TEXT.__const: 0x1a0
-  __TEXT.__cstring: 0x4892
+  __TEXT.__cstring: 0x489a
   __TEXT.__oslogstring: 0x5895
   __TEXT.__gcc_except_tab: 0x60c
-  __TEXT.__unwind_info: 0x1ba8
+  __TEXT.__unwind_info: 0x1b80
   __TEXT.__objc_classname: 0x1443
   __TEXT.__objc_methname: 0xfc26
   __TEXT.__objc_methtype: 0x2240

   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b40
+  __DATA_CONST.__objc_selrefs: 0x2bd0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x398
   __DATA_CONST.__objc_arraydata: 0x198
-  __AUTH_CONST.__auth_got: 0x2a8
-  __AUTH_CONST.__const: 0x1670
+  __AUTH_CONST.__auth_got: 0x2a0
+  __AUTH_CONST.__const: 0x1690
   __AUTH_CONST.__cfstring: 0x4b00
-  __AUTH_CONST.__objc_const: 0x14328
+  __AUTH_CONST.__objc_const: 0x13a50
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x2760
   __DATA.__objc_ivar: 0x91c
   __DATA.__data: 0xa28
-  __DATA.__bss: 0x2c0
+  __DATA.__bss: 0x2d0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5A715D70-5ED9-370F-AA38-6429242BEB02
-  Functions: 3153
-  Symbols:   6942
-  CStrings:  4178
+  UUID: 49CAEE61-B8CA-3611-953C-2EE9D74753DA
+  Functions: 3228
+  Symbols:   7062
+  CStrings:  4179
 
Symbols:
+ +[ATXInfoSuggestionFeedbackClient sharedInstance].cold.1
+ +[ATXInfoTimelineDonationClient sharedInstance].cold.1
+ +[ATXProactiveSuggestionClientModel clientModelTypeFromClientModelId:].cold.1
+ ATXPBHomeScreenCachedSuggestionReadFrom.cold.1
+ ATXPBHomeScreenCachedSuggestionReadFrom.cold.2
+ ATXPBHomeScreenCachedSuggestionReadFrom.cold.3
+ ATXPBHomeScreenCachedSuggestionReadFrom.cold.4
+ ATXPBHomeScreenCachedSuggestionReadFrom.cold.5
+ ATXPBProactiveSuggestionUISpecificationReadFrom.cold.1
+ ATXPBSuggestionLayoutListReadFrom.cold.1
+ ATXPBSuggestionLayoutReadFrom.cold.1
+ ATXPBSuggestionLayoutReadFrom.cold.2
+ ATXPBSuggestionLayoutReadFrom.cold.3
+ ATXPBSuggestionLayoutReadFrom.cold.4
+ ATXPBSuggestionLayoutReadFrom.cold.5
+ ATXPBSuggestionLayoutReadFrom.cold.6
+ ATXPBSuggestionLayoutReadFrom.cold.7
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ __101-[ATXUIFeedbackMetricsComputer _computeResultForConsumerSubType:query:publisher:resultSpecification:]_block_invoke.18
+ __101-[ATXUIFeedbackMetricsComputer _computeResultForConsumerSubType:query:publisher:resultSpecification:]_block_invoke.18.cold.1
+ __101-[ATXUIFeedbackMetricsComputer _computeResultForConsumerSubType:query:publisher:resultSpecification:]_block_invoke.21
+ __132-[ATXProactiveSuggestionGroupedUIFeedbackQuery enumerateGroupedUIFeedbackResultsWithBlock:completionBlock:uiFeedbackPublisherChain:]_block_invoke.28
+ __148-[ATXUniversalRealTimeSuggestionRequestCoordinator delegateUpdatedSuggestionsForClientModelId:suggestionRequest:response:clientModelsPendingUpdate:]_block_invoke.38
+ __38-[ATXInfoTimelineDonationClient _init]_block_invoke.8
+ __40-[ATXInfoSuggestionFeedbackClient _init]_block_invoke.8
+ __47-[ATXHomeScreenCachedSuggestions protoForBiome]_block_invoke.64
+ __51-[ATXScoreNormalizationDriver modelScoreHarvesting]_block_invoke.68
+ __54-[ATXBiomeBlendingModelStream publisherFromStartTime:]_block_invoke.24
+ __64-[ATXProactiveSuggestionUIFeedbackPublisher uiFeedbackPublisher]_block_invoke.11
+ __64-[ATXUniversalBiomeUIStream genericEventPublisherFromStartTime:]_block_invoke.23
+ __64-[ATXUniversalBlendingLayerServer coalescedBlendingLayerRefresh]_block_invoke.39
+ __67-[ATXHomeScreenCachedSuggestions allSuggestionsInCachedSuggestions]_block_invoke.14
+ __70-[ATXUniversalBlendingLayerServer listener:shouldAcceptNewConnection:]_block_invoke.49
+ __70-[ATXUniversalBlendingLayerServer listener:shouldAcceptNewConnection:]_block_invoke.49.cold.1
+ __72-[ATXProactiveSuggestionClientModel listener:shouldAcceptNewConnection:]_block_invoke.190
+ __72-[ATXProactiveSuggestionClientModel listener:shouldAcceptNewConnection:]_block_invoke.190.cold.1
+ __77-[ATXTrendPlot initWithStartDate:endDate:granularity:binInitialDataProvider:]_block_invoke.48
+ __82-[ATXShortcutsEditorGroupedUIFeedbackPublisher shortcutsEditorUIFeedbackPublisher]_block_invoke.67
+ __89-[ATXProactiveSuggestionFeedbackMetricsLogger(UIFeedback) logMetricsWithUIFeedbackQuery:]_block_invoke.11
+ __91-[ATXUniversalRealTimeSuggestionRequestCoordinator clientModelUpdatesForSuggestionRequest:]_block_invoke.15
+ __91-[ATXUniversalRealTimeSuggestionRequestCoordinator clientModelUpdatesForSuggestionRequest:]_block_invoke.18
+ __91-[ATXUniversalRealTimeSuggestionRequestCoordinator clientModelUpdatesForSuggestionRequest:]_block_invoke.18.cold.1
+ __91-[ATXUniversalRealTimeSuggestionRequestCoordinator clientModelUpdatesForSuggestionRequest:]_block_invoke.20
+ __91-[ATXUniversalRealTimeSuggestionRequestCoordinator clientModelUpdatesForSuggestionRequest:]_block_invoke.20.cold.1
+ __91-[ATXUniversalRealTimeSuggestionRequestCoordinator clientModelUpdatesForSuggestionRequest:]_block_invoke.23
+ __92-[ATXProactiveSuggestionUIFeedbackPublisher uiFeedbackSessionPublisherWithCorrelateHandler:]_block_invoke.22
+ __93-[ATXProactiveSuggestionUIFeedbackQuery enumerateUIFeedbackResultsWithBlock:completionBlock:]_block_invoke.15
+ __94-[ATXShadowMetricsComputer computeResultAsTrendPlotFromStartDate:toEndDate:resultGranularity:]_block_invoke.13
+ __94-[ATXShadowMetricsComputer computeResultAsTrendPlotFromStartDate:toEndDate:resultGranularity:]_block_invoke.13.cold.1
+ __94-[ATXShadowMetricsComputer computeResultAsTrendPlotFromStartDate:toEndDate:resultGranularity:]_block_invoke.15
+ __94-[ATXShadowMetricsComputer computeResultAsTrendPlotFromStartDate:toEndDate:resultGranularity:]_block_invoke.18
+ __97-[ATXUIFeedbackMetricsComputer _computeResultForClientModel:query:publisher:resultSpecification:]_block_invoke.13
+ __97-[ATXUIFeedbackMetricsComputer _computeResultForClientModel:query:publisher:resultSpecification:]_block_invoke.13.cold.1
+ __97-[ATXUIFeedbackMetricsComputer _computeResultForClientModel:query:publisher:resultSpecification:]_block_invoke.15
+ __97-[ATXUniversalRealTimeSuggestionRequestCoordinator remoteAsyncDelegateForClientModel:completion:]_block_invoke.45
+ __97-[ATXUniversalRealTimeSuggestionRequestCoordinator remoteAsyncDelegateForClientModel:completion:]_block_invoke.47
+ __97-[ATXUniversalRealTimeSuggestionRequestCoordinator remoteAsyncDelegateForClientModel:completion:]_block_invoke_2.48
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
+ __block_literal_global.189
+ __block_literal_global.192
+ __block_literal_global.24
+ __block_literal_global.34
+ __block_literal_global.37
+ __block_literal_global.48
+ __block_literal_global.57
+ __block_literal_global.93
- __101-[ATXUIFeedbackMetricsComputer _computeResultForConsumerSubType:query:publisher:resultSpecification:]_block_invoke.12
- __101-[ATXUIFeedbackMetricsComputer _computeResultForConsumerSubType:query:publisher:resultSpecification:]_block_invoke.12.cold.1
- __101-[ATXUIFeedbackMetricsComputer _computeResultForConsumerSubType:query:publisher:resultSpecification:]_block_invoke.15
- __132-[ATXProactiveSuggestionGroupedUIFeedbackQuery enumerateGroupedUIFeedbackResultsWithBlock:completionBlock:uiFeedbackPublisherChain:]_block_invoke.22
- __148-[ATXUniversalRealTimeSuggestionRequestCoordinator delegateUpdatedSuggestionsForClientModelId:suggestionRequest:response:clientModelsPendingUpdate:]_block_invoke.32
- __38-[ATXInfoTimelineDonationClient _init]_block_invoke.4
- __40-[ATXInfoSuggestionFeedbackClient _init]_block_invoke.4
- __47-[ATXHomeScreenCachedSuggestions protoForBiome]_block_invoke.58
- __51-[ATXScoreNormalizationDriver modelScoreHarvesting]_block_invoke.62
- __54-[ATXBiomeBlendingModelStream publisherFromStartTime:]_block_invoke.18
- __64-[ATXProactiveSuggestionUIFeedbackPublisher uiFeedbackPublisher]_block_invoke.5
- __64-[ATXUniversalBiomeUIStream genericEventPublisherFromStartTime:]_block_invoke.17
- __64-[ATXUniversalBlendingLayerServer coalescedBlendingLayerRefresh]_block_invoke.33
- __67-[ATXHomeScreenCachedSuggestions allSuggestionsInCachedSuggestions]_block_invoke.8
- __70-[ATXUniversalBlendingLayerServer listener:shouldAcceptNewConnection:]_block_invoke.43
- __70-[ATXUniversalBlendingLayerServer listener:shouldAcceptNewConnection:]_block_invoke.43.cold.1
- __72-[ATXProactiveSuggestionClientModel listener:shouldAcceptNewConnection:]_block_invoke.184
- __72-[ATXProactiveSuggestionClientModel listener:shouldAcceptNewConnection:]_block_invoke.184.cold.1
- __77-[ATXTrendPlot initWithStartDate:endDate:granularity:binInitialDataProvider:]_block_invoke.42
- __82-[ATXShortcutsEditorGroupedUIFeedbackPublisher shortcutsEditorUIFeedbackPublisher]_block_invoke.61
- __89-[ATXProactiveSuggestionFeedbackMetricsLogger(UIFeedback) logMetricsWithUIFeedbackQuery:]_block_invoke.5
- __91-[ATXUniversalRealTimeSuggestionRequestCoordinator clientModelUpdatesForSuggestionRequest:]_block_invoke.12
- __91-[ATXUniversalRealTimeSuggestionRequestCoordinator clientModelUpdatesForSuggestionRequest:]_block_invoke.12.cold.1
- __91-[ATXUniversalRealTimeSuggestionRequestCoordinator clientModelUpdatesForSuggestionRequest:]_block_invoke.14
- __91-[ATXUniversalRealTimeSuggestionRequestCoordinator clientModelUpdatesForSuggestionRequest:]_block_invoke.14.cold.1
- __91-[ATXUniversalRealTimeSuggestionRequestCoordinator clientModelUpdatesForSuggestionRequest:]_block_invoke.17
- __91-[ATXUniversalRealTimeSuggestionRequestCoordinator clientModelUpdatesForSuggestionRequest:]_block_invoke.9
- __92-[ATXProactiveSuggestionUIFeedbackPublisher uiFeedbackSessionPublisherWithCorrelateHandler:]_block_invoke.16
- __93-[ATXProactiveSuggestionUIFeedbackQuery enumerateUIFeedbackResultsWithBlock:completionBlock:]_block_invoke.9
- __94-[ATXShadowMetricsComputer computeResultAsTrendPlotFromStartDate:toEndDate:resultGranularity:]_block_invoke.12
- __94-[ATXShadowMetricsComputer computeResultAsTrendPlotFromStartDate:toEndDate:resultGranularity:]_block_invoke.7
- __94-[ATXShadowMetricsComputer computeResultAsTrendPlotFromStartDate:toEndDate:resultGranularity:]_block_invoke.7.cold.1
- __94-[ATXShadowMetricsComputer computeResultAsTrendPlotFromStartDate:toEndDate:resultGranularity:]_block_invoke.9
- __97-[ATXUIFeedbackMetricsComputer _computeResultForClientModel:query:publisher:resultSpecification:]_block_invoke.7
- __97-[ATXUIFeedbackMetricsComputer _computeResultForClientModel:query:publisher:resultSpecification:]_block_invoke.7.cold.1
- __97-[ATXUIFeedbackMetricsComputer _computeResultForClientModel:query:publisher:resultSpecification:]_block_invoke.9
- __97-[ATXUniversalRealTimeSuggestionRequestCoordinator remoteAsyncDelegateForClientModel:completion:]_block_invoke.39
- __97-[ATXUniversalRealTimeSuggestionRequestCoordinator remoteAsyncDelegateForClientModel:completion:]_block_invoke.41
- __97-[ATXUniversalRealTimeSuggestionRequestCoordinator remoteAsyncDelegateForClientModel:completion:]_block_invoke_2.42
- __block_literal_global.14
- __block_literal_global.177
- __block_literal_global.18
- __block_literal_global.186
- __block_literal_global.19
- __block_literal_global.22
- __block_literal_global.3
- __block_literal_global.36
- __block_literal_global.45
- __block_literal_global.6
- __block_literal_global.87
- __block_literal_global.9
- _fmod
CStrings:
+ "carPlay"

```
