## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-65.0.1.0.0
-  __TEXT.__text: 0xf5900
-  __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__objc_stubs: 0x30a0
+65.0.2.0.0
+  __TEXT.__text: 0xf8180
+  __TEXT.__auth_stubs: 0x1020
+  __TEXT.__objc_stubs: 0x3120
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xadc
+  __TEXT.__objc_methlist: 0xb04
   __TEXT.__const: 0x9dde
-  __TEXT.__gcc_except_tab: 0xeff0
-  __TEXT.__cstring: 0x5bef
-  __TEXT.__oslogstring: 0x3dac3
+  __TEXT.__gcc_except_tab: 0xf288
+  __TEXT.__cstring: 0x5cc0
+  __TEXT.__oslogstring: 0x3ebb4
   __TEXT.__objc_classname: 0x1ea
-  __TEXT.__objc_methname: 0x39b7
-  __TEXT.__objc_methtype: 0x1a87
+  __TEXT.__objc_methname: 0x3a52
+  __TEXT.__objc_methtype: 0x1b29
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x41f0
-  __DATA_CONST.__auth_got: 0x800
+  __TEXT.__unwind_info: 0x42a8
+  __DATA_CONST.__auth_got: 0x820
   __DATA_CONST.__got: 0x580
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x8570
-  __DATA_CONST.__cfstring: 0x61c0
+  __DATA_CONST.__const: 0x85c8
+  __DATA_CONST.__cfstring: 0x62e0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA.__objc_const: 0x1190
-  __DATA.__objc_selrefs: 0x10a0
-  __DATA.__objc_ivar: 0x80
+  __DATA.__objc_const: 0x11d0
+  __DATA.__objc_selrefs: 0x10c0
+  __DATA.__objc_ivar: 0x88
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x438
-  __DATA.__bss: 0x510
+  __DATA.__bss: 0x518
   __DATA.__common: 0x128
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F8115325-15DB-309C-AB64-E710C41AD214
-  Functions: 3467
-  Symbols:   448
-  CStrings:  4926
+  UUID: CB854778-8AE8-337F-8867-9B9273045B94
+  Functions: 3484
+  Symbols:   452
+  CStrings:  4997
 
Symbols:
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
CStrings:
+ "%s_%@"
+ "MAX_MAP_RESOLUTION"
+ "NOTIFICATIONS_SHOULD_STACK"
+ "SA_NOTIFICATIONS_SPACING_INTERVAL"
+ "_generalAlertQueue"
+ "_generalAlertStagingTimer"
+ "com.apple.safetyalerts.generalAlertStagingTimer"
+ "maxMapResolution"
+ "metadata"
+ "notifications"
+ "processGeneralSafetyAlertsArray:withMetadata:"
+ "processNextQueuedAlert"
+ "processSingleAlert:withMetadata:"
+ "shouldStack"
+ "spacingIntervalSeconds"
+ "startStagingTimerIfNeeded"
+ "stopStagingTimer"
+ "{\"msg%{public}.0s\":\"#assetConfig,getMaxMapResolutionKm\"}"
+ "{\"msg%{public}.0s\":\"#assetConfig,getNotificationsShouldStack\"}"
+ "{\"msg%{public}.0s\":\"#assetConfig,getSANotificationsSpacingInterval\"}"
+ "{\"msg%{public}.0s\":\"#channel,cleaned_up_general_alert_staging\"}"
+ "{\"msg%{public}.0s\":\"#channel,enqueued_single_general_alert\", \"queue_size\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#channel,failed_to_create_staging_timer\"}"
+ "{\"msg%{public}.0s\":\"#channel,initialized_general_alert_staging\"}"
+ "{\"msg%{public}.0s\":\"#channel,no_alerts_to_stage\"}"
+ "{\"msg%{public}.0s\":\"#channel,only_one_alert_in_queue_no_timer_needed\"}"
+ "{\"msg%{public}.0s\":\"#channel,processNextQueuedAlert,queue_empty\"}"
+ "{\"msg%{public}.0s\":\"#channel,processing_first_queued_alert_immediately\"}"
+ "{\"msg%{public}.0s\":\"#channel,processing_general_safety_alerts_array\", \"alerts_count\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#channel,processing_igneous_alert_immediate\"}"
+ "{\"msg%{public}.0s\":\"#channel,processing_queued_general_alert\", \"remaining_queue_size\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#channel,processing_single_alert\"}"
+ "{\"msg%{public}.0s\":\"#channel,processing_single_general_safety_alert\"}"
+ "{\"msg%{public}.0s\":\"#channel,queued_general_safety_alert\", \"alert_index\":%{private}d, \"queue_size\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#channel,sending_single_general_alert_immediately\"}"
+ "{\"msg%{public}.0s\":\"#channel,staging_timer_already_running\"}"
+ "{\"msg%{public}.0s\":\"#channel,started_staging_timer_for_remaining_alerts\", \"remaining_alerts\":%{public}d, \"interval_seconds\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#channel,starting_array_processing\", \"total_queued\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#channel,stopped_staging_timer\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getMaxMapResolutionKm\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getMaxMapResolutionKm,clamped_max\", \"original\":%{public}d, \"clamped\":%{public}d, \"max_limit\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getMaxMapResolutionKm,clamped_min\", \"original\":%{public}d, \"clamped\":%{public}d, \"min_limit\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getMaxMapResolutionKm,final_result\", \"result\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getMaxMapResolutionKm,mobile_asset_or_default\", \"original_value\":%{public}d, \"from_mobile_asset\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getMaxMapResolutionKm,user_defaults\", \"original_value\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getNotificationsShouldStack\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getNotificationsShouldStack,mobile_asset_or_default\", \"value\":%{public}hhd, \"from_mobile_asset\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getNotificationsShouldStack,user_defaults\", \"value\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getSANotificationsSpacingInterval\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getSANotificationsSpacingInterval,clamped_max\", \"original\":%{public}d, \"clamped\":%{public}d, \"max_limit\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getSANotificationsSpacingInterval,clamped_min\", \"original\":%{public}d, \"clamped\":%{public}d, \"min_limit\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getSANotificationsSpacingInterval,final_result\", \"result\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getSANotificationsSpacingInterval,mobile_asset_or_default\", \"original_value\":%{public}d, \"from_mobile_asset\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,getSANotificationsSpacingInterval,user_defaults\", \"original_value\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readNotificationsAsset\", \"asset\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readNotificationsAsset\", \"maxMapResolution\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readNotificationsAsset\", \"notificationsShouldStack\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readNotificationsAsset\", \"saNotificationsSpacingInterval\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readNotificationsAsset,configIsNil\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readNotificationsAsset,main dict nil\"}"
+ "{\"msg%{public}.0s\":\"#countryAssetConfig,readNotificationsAsset,notificationsConfig nil\"}"
+ "{\"msg%{public}.0s\":\"#notif,postGeneralAlertRichNotification,applying_min_resolution\", \"original_span\":\"%{public}0.1f\", \"min_resolution_km\":\"%{public}0.1f\", \"final_span\":\"%{public}0.1f\"}"
+ "{\"msg%{public}.0s\":\"#notif,postIgneousRichNotification,applying_min_resolution\", \"original_span\":\"%{public}0.1f\", \"min_resolution_km\":\"%{public}0.1f\", \"final_span\":\"%{public}0.1f\"}"
+ "{\"msg%{public}.0s\":\"#notif,using_grouped_thread\", \"threadId\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#notif,using_unique_thread\", \"threadId\":%{private, location:escape_only}@}"
+ "{unique_ptr<SATimer, std::default_delete<SATimer>>=\"\"{?=\"__ptr_\"^{SATimer}}}"
+ "{vector<NSDictionary *, std::allocator<NSDictionary *>>=\"__begin_\"^@\"__end_\"^@\"\"{?=\"__cap_\"^@}}"
- "d24@0:8d16"
- "findOptimalZoomLevelForRegionSpan:"
- "{\"msg%{public}.0s\":\"#channel,processing_alert\", \"alert_index\":%{private}d, \"is_last_alert\":%{public}hhd, \"alert_keys_count\":%{private}d}"
- "{\"msg%{public}.0s\":\"#channel,processing_single_alert_or_other_data\"}"
- "{\"msg%{public}.0s\":\"#channel,userInfoDict\", \"key\":%{private, location:escape_only}@, \"value\":%{private, location:escape_only}@}"

```
