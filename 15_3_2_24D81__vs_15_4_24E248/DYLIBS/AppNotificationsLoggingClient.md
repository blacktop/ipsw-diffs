## AppNotificationsLoggingClient

> `/System/Library/PrivateFrameworks/AppNotificationsLoggingClient.framework/Versions/A/AppNotificationsLoggingClient`

```diff

-584.9.0.0.0
-  __TEXT.__text: 0x4624
+588.11.0.0.0
+  __TEXT.__text: 0x4780
   __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_methlist: 0x250
-  __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x735
+  __TEXT.__objc_methlist: 0x300
+  __TEXT.__const: 0xc8
+  __TEXT.__cstring: 0x73d
   __TEXT.__oslogstring: 0x4bb
   __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__unwind_info: 0x160
+  __TEXT.__unwind_info: 0x168
   __TEXT.__objc_classname: 0x74
   __TEXT.__objc_methname: 0x85a
   __TEXT.__objc_methtype: 0x29d

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x100
-  __AUTH_CONST.__const: 0x720
+  __AUTH_CONST.__const: 0x740
   __AUTH_CONST.__cfstring: 0x840
-  __AUTH_CONST.__objc_const: 0x548
+  __AUTH_CONST.__objc_const: 0x410
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x30
   __DATA.__data: 0x128
-  __DATA.__bss: 0x2a0
+  __DATA.__bss: 0x2b0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/AppPredictionClient.framework/Versions/A/AppPredictionClient

   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/Versions/A/ProactiveSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 99B53E56-DAE3-3787-BE72-E8CB0A25CF1D
-  Functions: 181
-  Symbols:   476
-  CStrings:  339
+  UUID: AD9F284F-D5DD-3DE9-B763-8F651E257E13
+  Functions: 226
+  Symbols:   524
+  CStrings:  340
 
Symbols:
+ +[ATXNotificationsLoggingClient sharedInstance].cold.1
+ __37-[ATXNotificationsLoggingClient init]_block_invoke.67
+ __37-[ATXNotificationsLoggingClient init]_block_invoke.67.cold.1
+ __37-[ATXNotificationsLoggingClient init]_block_invoke.70
+ __66-[ATXNotificationsLoggingClient _processActiveSuggestionsRequests]_block_invoke.76
+ __66-[ATXNotificationsLoggingClient _processActiveSuggestionsRequests]_block_invoke.76.cold.1
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
+ __block_literal_global.69
+ __block_literal_global.72
+ __block_literal_global.88
+ __block_literal_global.90
+ __block_literal_global.93
- __37-[ATXNotificationsLoggingClient init]_block_invoke.61
- __37-[ATXNotificationsLoggingClient init]_block_invoke.61.cold.1
- __37-[ATXNotificationsLoggingClient init]_block_invoke.64
- __66-[ATXNotificationsLoggingClient _processActiveSuggestionsRequests]_block_invoke.70
- __66-[ATXNotificationsLoggingClient _processActiveSuggestionsRequests]_block_invoke.70.cold.1
- __block_literal_global.63
- __block_literal_global.66
- __block_literal_global.76
- __block_literal_global.78
- __block_literal_global.87
CStrings:
+ "carPlay"

```
