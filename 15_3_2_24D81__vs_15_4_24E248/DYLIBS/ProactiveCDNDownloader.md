## ProactiveCDNDownloader

> `/System/Library/PrivateFrameworks/ProactiveCDNDownloader.framework/Versions/A/ProactiveCDNDownloader`

```diff

-584.9.0.0.0
-  __TEXT.__text: 0x7488
+588.11.0.0.0
+  __TEXT.__text: 0x75b0
   __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0x560
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x4bb
+  __TEXT.__objc_methlist: 0x7c4
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x4c3
   __TEXT.__oslogstring: 0x484
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__unwind_info: 0x1c0
   __TEXT.__objc_classname: 0x116
   __TEXT.__objc_methname: 0x138c
   __TEXT.__objc_methtype: 0x787

   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f0
+  __DATA_CONST.__objc_selrefs: 0x610
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x2a8
-  __AUTH_CONST.__const: 0x7e0
+  __AUTH_CONST.__const: 0x800
   __AUTH_CONST.__cfstring: 0x200
-  __AUTH_CONST.__objc_const: 0x1038
+  __AUTH_CONST.__objc_const: 0xbc8
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x240
-  __DATA.__bss: 0x298
+  __DATA.__bss: 0x2a8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0F1C0816-2420-3808-A913-6D7AFA5784B8
-  Functions: 235
-  Symbols:   737
-  CStrings:  447
+  UUID: 1BE95371-91CB-3C60-9DDD-CECF81DA79FF
+  Functions: 279
+  Symbols:   785
+  CStrings:  448
 
Symbols:
+ -[ATXGEOTileLoader requestGEOTileDataForLocation:tileDataHandler:].cold.1
+ __62-[ATXProactiveCDNDownloader _heroDatasForLocation:completion:]_block_invoke.53
+ __62-[ATXProactiveCDNDownloader _heroDatasForLocation:completion:]_block_invoke.58
+ __77-[ATXGEOTileLoader requestGEOTileDataForLocation:tileLoader:tileDataHandler:]_block_invoke.19
+ __77-[ATXGEOTileLoader requestGEOTileDataForLocation:tileLoader:tileDataHandler:]_block_invoke.22
+ __77-[ATXGEOTileLoader requestGEOTileDataForLocation:tileLoader:tileDataHandler:]_block_invoke.22.cold.1
+ __85-[ATXProactiveCDNDownloader highConfidenceHeroDatasForCurrentLocationWithCompletion:]_block_invoke.35.cold.1
+ __85-[ATXProactiveCDNDownloader highConfidenceHeroDatasForCurrentLocationWithCompletion:]_block_invoke.38
+ __85-[ATXProactiveCDNDownloader highConfidenceHeroDatasForCurrentLocationWithCompletion:]_block_invoke.41
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
+ __block_literal_global.21
+ __block_literal_global.24
- __62-[ATXProactiveCDNDownloader _heroDatasForLocation:completion:]_block_invoke.47
- __62-[ATXProactiveCDNDownloader _heroDatasForLocation:completion:]_block_invoke.52
- __77-[ATXGEOTileLoader requestGEOTileDataForLocation:tileLoader:tileDataHandler:]_block_invoke.13
- __77-[ATXGEOTileLoader requestGEOTileDataForLocation:tileLoader:tileDataHandler:]_block_invoke.16
- __77-[ATXGEOTileLoader requestGEOTileDataForLocation:tileLoader:tileDataHandler:]_block_invoke.16.cold.1
- __85-[ATXProactiveCDNDownloader highConfidenceHeroDatasForCurrentLocationWithCompletion:]_block_invoke.26
- __85-[ATXProactiveCDNDownloader highConfidenceHeroDatasForCurrentLocationWithCompletion:]_block_invoke.29
- __85-[ATXProactiveCDNDownloader highConfidenceHeroDatasForCurrentLocationWithCompletion:]_block_invoke.29.cold.1
- __block_literal_global.15
- __block_literal_global.18
CStrings:
+ "carPlay"

```
