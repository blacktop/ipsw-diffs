## CompanionWakeSettings

> `/System/Library/NanoPreferenceBundles/General/CompanionWakeSettings.bundle/CompanionWakeSettings`

```diff

-1112.0.187.0.0
-  __TEXT.__text: 0x7d90
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_stubs: 0xf40
-  __TEXT.__objc_methlist: 0x46c
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x9fb
-  __TEXT.__oslogstring: 0x223
-  __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__objc_methname: 0x10af
-  __TEXT.__objc_classname: 0x144
-  __TEXT.__objc_methtype: 0x36e
-  __TEXT.__unwind_info: 0x200
-  __DATA_CONST.__auth_got: 0x1c0
+1112.1.27.0.0
+  __TEXT.__text: 0x2de8
+  __TEXT.__auth_stubs: 0x2d0
+  __TEXT.__objc_stubs: 0xa20
+  __TEXT.__objc_methlist: 0x28c
+  __TEXT.__const: 0x50
+  __TEXT.__gcc_except_tab: 0x18
+  __TEXT.__cstring: 0x49a
+  __TEXT.__objc_methname: 0xb91
+  __TEXT.__oslogstring: 0x17c
+  __TEXT.__objc_classname: 0xef
+  __TEXT.__objc_methtype: 0x285
+  __TEXT.__unwind_info: 0x13c
+  __DATA_CONST.__auth_got: 0x178
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0xe18
-  __DATA_CONST.__cfstring: 0x640
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__const: 0xc8
+  __DATA_CONST.__cfstring: 0x500
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0xd20
-  __DATA.__objc_selrefs: 0x470
-  __DATA.__objc_classrefs: 0xc0
-  __DATA.__objc_superrefs: 0x38
-  __DATA.__objc_ivar: 0x78
-  __DATA.__objc_data: 0x230
+  __DATA_CONST.__objc_intobj: 0x78
+  __DATA.__objc_const: 0x978
+  __DATA.__objc_selrefs: 0x2f0
+  __DATA.__objc_classrefs: 0x88
+  __DATA.__objc_superrefs: 0x20
+  __DATA.__objc_ivar: 0x4c
+  __DATA.__objc_data: 0x140
   __DATA.__data: 0x120
-  __DATA.__bss: 0x5c8
+  __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DCC190D4-8CA0-31A2-9113-D1B6CAE79297
-  Functions: 297
-  Symbols:   212
-  CStrings:  485
+  UUID: 30AB4EDC-48C8-377E-9478-6C9A517B5DA8
+  Functions: 59
+  Symbols:   90
+  CStrings:  286
 
Symbols:
+ _OBJC_CLASS_$_CSLPRFReturnToAppSettings
+ _OBJC_CLASS_$_CSLPRFReturnToAppSettingsModel
+ _cslprf_sessions_log
- _CFPreferencesGetAppBooleanValue
- _CSLSBannerLookScreenDwellTimeout
- _CSLSBulletinAlertAfterSleepGestureLingerTimeout
- _CSLSDisableViewOnWakePreferenceKey
- _CSLSIdleScreenOffExtendedTimeout
- _CSLSOnWakeTimeoutPreferenceKey
- _CSLSViewOnWakeFirstUpdateTimeout
- _CSLSViewOnWakePreferencesDomain
- _CSLSViewOnWakeUpdateDefaultTimeout
- _CSLSViewOnWakeUpdateDefaultTimeoutObsolete
- _CSLSWakeToQuickLookTimeOut
- _CSLSWakeToViewMissedBundleAlertTimeOut
- _NSStringFromClass
- _OBJC_CLASS_$_BSDescriptionBuilder
- _OBJC_CLASS_$_BSEqualsBuilder
- _OBJC_CLASS_$_BSHashBuilder
- _OBJC_CLASS_$_CSLSConcurrentObserverStore
- _OBJC_CLASS_$_CSLSReturnToAppSettings
- _OBJC_CLASS_$_CSLSReturnToAppSettingsModel
- _OBJC_CLASS_$_NRPairedDeviceRegistry
- _OBJC_CLASS_$_NSPointerArray
- _OBJC_CLASS_$_NSUUID
- _OBJC_METACLASS_$_CSLSConcurrentObserverStore
- _OBJC_METACLASS_$_CSLSReturnToAppSettings
- _OBJC_METACLASS_$_CSLSReturnToAppSettingsModel
- __Block_object_dispose
- __NSConcreteGlobalBlock
- _csl_accessibility_log
- _csl_action_metrics_log
- _csl_alerts_log
- _csl_analytics_log
- _csl_app_event_log
- _csl_app_sessions_log
- _csl_app_switcher_log
- _csl_application_install_log
- _csl_ariadne_log
- _csl_background_refresh_log
- _csl_backlight_log
- _csl_battery_log
- _csl_bb_log
- _csl_bb_pipeline_log
- _csl_bedtime_log
- _csl_brightness_log
- _csl_budget_log
- _csl_button_log
- _csl_cache_delete_log
- _csl_clock_log
- _csl_connection_status_log
- _csl_control_center_log
- _csl_crown_log
- _csl_data_migration_log
- _csl_demo_mode_log
- _csl_depth_mode_log
- _csl_detents_log
- _csl_developer_log
- _csl_diagnostics_log
- _csl_dnd_log
- _csl_dock_log
- _csl_duet_metering_log
- _csl_eclipse_log
- _csl_eco_mode_log
- _csl_flipbook_log
- _csl_fluidui_log
- _csl_gesture_log
- _csl_haptic_log
- _csl_hid_log
- _csl_icon_field_log
- _csl_icon_log
- _csl_idle_navigation_log
- _csl_lesson_log
- _csl_low_power_mode_cellular_log
- _csl_midnight_timer_log
- _csl_migration_app_log
- _csl_notification_alerting_log
- _csl_notification_center_log
- _csl_notification_management_log
- _csl_now_playing_log
- _csl_owd_log
- _csl_passcode_log
- _csl_power_log
- _csl_preboard_log
- _csl_prelaunch_log
- _csl_process_assertions_log
- _csl_qlll_log
- _csl_responder_log
- _csl_scene_alerts_log
- _csl_scene_presentation_log
- _csl_schedule_log
- _csl_school_mode_log
- _csl_screenshot_log
- _csl_scroll_center_log
- _csl_sessions_log
- _csl_settings_log
- _csl_shutdown_log
- _csl_snapshot_log
- _csl_startup_log
- _csl_state_capture_log
- _csl_statusbar_log
- _csl_sting_log
- _csl_systemstate_log
- _csl_testing_log
- _csl_thermal_log
- _csl_timer_log
- _csl_trace_log
- _csl_transaction_log
- _csl_transition_log
- _csl_ui_log
- _csl_uitrigger_log
- _csl_usage_metering_log
- _csl_user_idle_log
- _csl_view_service_log
- _csl_wake_gesture_log
- _csl_watchkit_log
- _csl_waterlock_log
- _csl_widget_log
- _csl_workspace_log
- _csl_xpc_barrier_log
- _objc_enumerationMutation
- _objc_opt_respondsToSelector
- _objc_retain
- _objc_retain_x3
- _objc_unsafeClaimAutoreleasedReturnValue
- _os_log_create
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
CStrings:
+ "@\"CSLPRFReturnToAppSettingsModel\""
+ "T@\"CSLPRFReturnToAppSettingsModel\",W,N,V_returnToAppSettingsModel"
- "\x11"
- "\x14"
- "27120128-3A0E-492A-8BBC-C57A70E362CA"
- "@\"CSLSConcurrentObserverStore\""
- "@\"CSLSReturnToAppSettingsModel\""
- "@\"NSMutableDictionary\""
- "@\"NSPointerArray\""
- "@24@0:8@16"
- "AllowReturnToAppUntilCrownPress"
- "AlwaysReturnToAppInSession"
- "B8@?0"
- "CSLSConcurrentObserverStore"
- "CSLSReturnToAppSettings"
- "CSLSReturnToAppSettingsModel"
- "OnWakeTimeoutSeconds"
- "ReturnToAppSettings"
- "ReturnToAppTimeout"
- "SessionCapable"
- "T@\"CSLSReturnToAppSettingsModel\",W,N,V_returnToAppSettingsModel"
- "T@\"NSPointerArray\",&,N,V_observers"
- "TB,N,V_alwaysReturnToAppInSession"
- "TB,N,V_sessionCapable"
- "TB,R,N,V_hasCustomReturnToAppTimeout"
- "TQ,R,N"
- "Td,N"
- "T{os_unfair_lock_s=I},N,V_observersLock"
- "__canControlReturnToAppUntilCrownPress = %{BOOL}u, allowReturnToAppUntilCrownPress = %{BOOL}u"
- "_alwaysReturnToAppInSession"
- "_hasCustomReturnToAppTimeout"
- "_hasCustomReturnToAppTimeout = %{BOOL}u"
- "_lock"
- "_npsDomainAccessor"
- "_npsManager"
- "_observers"
- "_observersLock"
- "_returnToAppSettingsByBundleID"
- "_returnToAppTimeout"
- "_sessionCapable"
- "_withLock:"
- "accessibility"
- "action_metrics"
- "addObserver:"
- "addPointer:"
- "alerts"
- "allObjects"
- "analytics"
- "app_event"
- "app_sessions"
- "app_switcher"
- "appendBool:"
- "appendBool:counterpart:"
- "appendBool:withName:"
- "appendDouble:"
- "appendDouble:counterpart:"
- "appendFloat:withName:"
- "application_install"
- "ariadne"
- "background_refresh"
- "backlight"
- "battery"
- "bb"
- "bb_pipeline"
- "bedtime"
- "brightness"
- "budget"
- "build"
- "builder"
- "builderWithObject:"
- "builderWithObject:ofExpectedClass:"
- "button"
- "cache_delete"
- "clock"
- "com.apple.Carousel"
- "com.apple.Carousel.notifications"
- "com.apple.nano"
- "compact"
- "connection_status"
- "control_center"
- "countByEnumeratingWithState:objects:count:"
- "crown"
- "d"
- "d16@0:8"
- "d8@?0"
- "data_migration"
- "demo_mode"
- "depth_mode"
- "detents"
- "developer"
- "diagnostics"
- "dictionary"
- "dictionaryWithCapacity:"
- "dnd"
- "dock"
- "duet_metering"
- "eclipse"
- "eco_mode"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObserversWithBlock:"
- "flipbook"
- "fluidui"
- "gesture"
- "getActivePairedDevice"
- "haptic"
- "hid"
- "icon"
- "icon_field"
- "idle_navigation"
- "initWithDictionary:"
- "initWithServiceName:"
- "initWithUUIDString:"
- "isEqual"
- "lesson"
- "low_power_mode_cellular"
- "midnight_timer"
- "migration_app"
- "notification_alerting"
- "notification_center"
- "notification_management"
- "now_playing"
- "objectForKey:"
- "observers"
- "observersLock"
- "owd"
- "passcode"
- "performSelectorOnMainThread:withObject:waitUntilDone:"
- "performSelectorOnMainThreadWithRespondingObservers:object:waitUntilDone:"
- "pointerAtIndex:"
- "power"
- "preboard"
- "prelaunch"
- "process_assertions"
- "qlll"
- "reloadAppSettings"
- "removeObserver:"
- "replacePointerAtIndex:withPointer:"
- "responder"
- "returnToAppSettingsToDictionary:"
- "scene_alerts"
- "scene_presentation"
- "schedule"
- "school_mode"
- "screenshot"
- "scroll_center"
- "sessions"
- "setObject:forKey:"
- "setObservers:"
- "setObserversLock:"
- "setSessionCapable:"
- "setting returnToAppTimeout to %d"
- "settings"
- "settingsChanged:forBundleID:"
- "sharedInstance"
- "shutdown"
- "snapshot"
- "startup"
- "state_capture"
- "statusbar"
- "sting"
- "supportsCapability:"
- "synchronize"
- "systemstate"
- "testing"
- "thermal"
- "timer"
- "toDictionary"
- "trace"
- "transaction"
- "transition"
- "ui"
- "uitrigger"
- "usage_metering"
- "user_idle"
- "v16@?0@\"<CSLSReturnToAppSettingsObserver>\"8"
- "v16@?0@8"
- "v20@0:8{os_unfair_lock_s=I}16"
- "v24@0:8@?16"
- "v24@0:8d16"
- "v32@?0@\"NSString\"8@\"CSLSReturnToAppSettings\"16^B24"
- "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
- "v36@0:8:16@24B32"
- "viewOnWakeDisabled"
- "view_service"
- "wake_gesture"
- "watchkit"
- "waterlock"
- "weakObjectsPointerArray"
- "widget"
- "workspace"
- "xpc_barrier"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```
