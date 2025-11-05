## ProactiveMagicalMoments

> `/System/Library/PrivateFrameworks/ProactiveMagicalMoments.framework/Versions/A/ProactiveMagicalMoments`

```diff

-584.9.0.0.0
-  __TEXT.__text: 0x90e8
+588.11.0.0.0
+  __TEXT.__text: 0x92d8
   __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_methlist: 0x80c
+  __TEXT.__objc_methlist: 0x994
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0xae6
+  __TEXT.__cstring: 0xaee
   __TEXT.__oslogstring: 0xb42
   __TEXT.__gcc_except_tab: 0x158
-  __TEXT.__unwind_info: 0x2c8
+  __TEXT.__unwind_info: 0x2e0
   __TEXT.__objc_classname: 0x14a
   __TEXT.__objc_methname: 0x1c43
   __TEXT.__objc_methtype: 0x43f

   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x638
+  __DATA_CONST.__objc_selrefs: 0x6c0
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x210
-  __AUTH_CONST.__const: 0x820
+  __AUTH_CONST.__const: 0x840
   __AUTH_CONST.__cfstring: 0xb00
-  __AUTH_CONST.__objc_const: 0x13a8
+  __AUTH_CONST.__objc_const: 0x10f0
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x3c0
   __DATA.__objc_ivar: 0xa8
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x2c0
+  __DATA.__bss: 0x2d0
   - /System/Library/Frameworks/CallKit.framework/Versions/A/CallKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/Versions/A/CoreTelephony

   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/Versions/A/ProactiveSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9756EF39-36D6-3627-85E4-FE381396B8B5
-  Functions: 289
-  Symbols:   880
-  CStrings:  656
+  UUID: C45C5ADB-A5D8-38CE-B102-601752F88E64
+  Functions: 340
+  Symbols:   934
+  CStrings:  657
 
Symbols:
+ +[PMMContextHelper sharedInstance].cold.1
+ +[PMMMusicStateProcessor shared].cold.1
+ +[PMMPredictor sharedInstance].cold.1
+ -[PMMAudioDisconnectListener initWithHandler:].cold.1
+ -[PMMMusicStateProcessor lastPlayedInCarWithHandler:].cold.1
+ -[PMMMusicStateProcessor lastPlayedWithHandler:].cold.1
+ -[PMMPredictor _publishPredictionWithPredictedApplication:fromUnitTest:].cold.2
+ __44-[PMMPredictor handlePredictedApplications:]_block_invoke.67
+ __46-[PMMPredictor _handleNowPlayingInfoDidChange]_block_invoke.106
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
- __44-[PMMPredictor handlePredictedApplications:]_block_invoke.61
- __46-[PMMPredictor _handleNowPlayingInfoDidChange]_block_invoke.100
CStrings:
+ "carPlay"

```
