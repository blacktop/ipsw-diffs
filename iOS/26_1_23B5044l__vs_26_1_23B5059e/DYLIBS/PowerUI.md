## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI`

```diff

-696.40.4.0.0
-  __TEXT.__text: 0xc22cc
+696.40.6.0.0
+  __TEXT.__text: 0xc3f78
   __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_methlist: 0x1b6b4
-  __TEXT.__const: 0x538
-  __TEXT.__cstring: 0xe111
-  __TEXT.__oslogstring: 0xbf0a
-  __TEXT.__gcc_except_tab: 0x125c
-  __TEXT.__unwind_info: 0x1ce0
-  __TEXT.__objc_classname: 0xb55
-  __TEXT.__objc_methname: 0x3e22d
-  __TEXT.__objc_methtype: 0x40f1
-  __TEXT.__objc_stubs: 0xca40
-  __DATA_CONST.__got: 0x4f8
-  __DATA_CONST.__const: 0x14c8
-  __DATA_CONST.__objc_classlist: 0x2f8
+  __TEXT.__objc_methlist: 0x1b8f4
+  __TEXT.__const: 0x540
+  __TEXT.__cstring: 0xe56b
+  __TEXT.__oslogstring: 0xc31f
+  __TEXT.__gcc_except_tab: 0x1290
+  __TEXT.__unwind_info: 0x1d50
+  __TEXT.__objc_classname: 0xb97
+  __TEXT.__objc_methname: 0x3e58b
+  __TEXT.__objc_methtype: 0x4108
+  __TEXT.__objc_stubs: 0xcbe0
+  __DATA_CONST.__got: 0x508
+  __DATA_CONST.__const: 0x14f8
+  __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5408
+  __DATA_CONST.__objc_selrefs: 0x54b8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2d0
+  __DATA_CONST.__objc_superrefs: 0x2e0
   __DATA_CONST.__objc_arraydata: 0x6fb8
   __AUTH_CONST.__auth_got: 0x588
-  __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0xbdc0
-  __AUTH_CONST.__objc_const: 0x36420
+  __AUTH_CONST.__const: 0x680
+  __AUTH_CONST.__cfstring: 0xc0c0
+  __AUTH_CONST.__objc_const: 0x36ef0
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_arrayobj: 0x3a8
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__objc_doubleobj: 0xd0
-  __AUTH.__objc_data: 0x1400
-  __DATA.__objc_ivar: 0x3c24
+  __AUTH.__objc_data: 0x14a0
+  __DATA.__objc_ivar: 0x3c50
   __DATA.__data: 0x6c8
   __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0x1a0
+  __DATA_DIRTY.__bss: 0x1c0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 87A50C1A-ABDE-368A-8DC6-103348890F80
-  Functions: 9789
-  Symbols:   26859
-  CStrings:  8895
+  UUID: CD39136B-2CEB-3159-ADE9-59C3E9B80992
+  Functions: 9843
+  Symbols:   27032
+  CStrings:  9003
 
Symbols:
+ +[PowerUIIBLMNotificationManager sharedInstance]
+ +[PowerUIIBLMNotificationManager sharedInstance].cold.1
+ +[PowerUINotificationManager chargingAdviceNotificationContent]
+ +[PowerUINotificationManager chargingAdviceNotificationRequest]
+ +[PowerUINotificationManager lowRuntimeNotificationContent]
+ +[PowerUINotificationManager lowRuntimeNotificationRequest]
+ +[PowerUIRuntimeAwarenessNotifier sharedInstance]
+ +[PowerUIRuntimeAwarenessNotifier sharedInstance].cold.1
+ -[PowerUIIBLMNotificationManager .cxx_destruct]
+ -[PowerUIIBLMNotificationManager displayIBLMEngagedNotification]
+ -[PowerUIIBLMNotificationManager init]
+ -[PowerUIIBLMNotificationManager log]
+ -[PowerUIIBLMNotificationManager notifyToken]
+ -[PowerUIIBLMNotificationManager queue]
+ -[PowerUIIBLMNotificationManager recordIBLMFirstUserNotificationResponse:]
+ -[PowerUIIBLMNotificationManager setLog:]
+ -[PowerUIIBLMNotificationManager setNotifyToken:]
+ -[PowerUIIBLMNotificationManager setQueue:]
+ -[PowerUIIBLMNotificationManager setUnCenter:]
+ -[PowerUIIBLMNotificationManager unCenter]
+ -[PowerUIIBLMNotificationManager userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:]
+ -[PowerUINotificationManager postChargingAdviceNotification]
+ -[PowerUINotificationManager postLowRuntimeNotification]
+ -[PowerUIRuntimeAwarenessNotifier .cxx_destruct]
+ -[PowerUIRuntimeAwarenessNotifier batteryPredictor]
+ -[PowerUIRuntimeAwarenessNotifier checkBatteryLevelAndPostNotificationIfNeeded]
+ -[PowerUIRuntimeAwarenessNotifier context]
+ -[PowerUIRuntimeAwarenessNotifier init]
+ -[PowerUIRuntimeAwarenessNotifier lastChargingAdviceNotificationDate]
+ -[PowerUIRuntimeAwarenessNotifier lastSeenBatteryLevel]
+ -[PowerUIRuntimeAwarenessNotifier locationMonitor]
+ -[PowerUIRuntimeAwarenessNotifier log]
+ -[PowerUIRuntimeAwarenessNotifier monitor:maySuggestNewFullChargeDeadline:]
+ -[PowerUIRuntimeAwarenessNotifier monitorMayInvalidateDEoCCache:]
+ -[PowerUIRuntimeAwarenessNotifier queue]
+ -[PowerUIRuntimeAwarenessNotifier setBatteryPredictor:]
+ -[PowerUIRuntimeAwarenessNotifier setContext:]
+ -[PowerUIRuntimeAwarenessNotifier setLastChargingAdviceNotificationDate:]
+ -[PowerUIRuntimeAwarenessNotifier setLastSeenBatteryLevel:]
+ -[PowerUIRuntimeAwarenessNotifier setLocationMonitor:]
+ -[PowerUIRuntimeAwarenessNotifier setLog:]
+ -[PowerUIRuntimeAwarenessNotifier setQueue:]
+ -[PowerUIRuntimeAwarenessNotifier shouldAdviseToCharge]
+ -[PowerUIRuntimeAwarenessNotifier shouldThrottleChargingAdviceNotification]
+ -[PowerUIRuntimeAwarenessNotifier startAllMonitoring]
+ -[PowerUIRuntimeAwarenessNotifier stopAllMonitoring]
+ _OBJC_CLASS_$_PowerUIIBLMNotificationManager
+ _OBJC_CLASS_$_PowerUIRuntimeAwarenessNotifier
+ _OBJC_IVAR_$_PowerUIIBLMNotificationManager._log
+ _OBJC_IVAR_$_PowerUIIBLMNotificationManager._notifyToken
+ _OBJC_IVAR_$_PowerUIIBLMNotificationManager._queue
+ _OBJC_IVAR_$_PowerUIIBLMNotificationManager._unCenter
+ _OBJC_IVAR_$_PowerUIRuntimeAwarenessNotifier._batteryPredictor
+ _OBJC_IVAR_$_PowerUIRuntimeAwarenessNotifier._context
+ _OBJC_IVAR_$_PowerUIRuntimeAwarenessNotifier._lastChargingAdviceNotificationDate
+ _OBJC_IVAR_$_PowerUIRuntimeAwarenessNotifier._lastSeenBatteryLevel
+ _OBJC_IVAR_$_PowerUIRuntimeAwarenessNotifier._locationMonitor
+ _OBJC_IVAR_$_PowerUIRuntimeAwarenessNotifier._log
+ _OBJC_IVAR_$_PowerUIRuntimeAwarenessNotifier._queue
+ _OBJC_METACLASS_$_PowerUIIBLMNotificationManager
+ _OBJC_METACLASS_$_PowerUIRuntimeAwarenessNotifier
+ __OBJC_$_CLASS_METHODS_PowerUIIBLMNotificationManager
+ __OBJC_$_CLASS_METHODS_PowerUIRuntimeAwarenessNotifier
+ __OBJC_$_INSTANCE_METHODS_PowerUIIBLMNotificationManager
+ __OBJC_$_INSTANCE_METHODS_PowerUIRuntimeAwarenessNotifier
+ __OBJC_$_INSTANCE_VARIABLES_PowerUIIBLMNotificationManager
+ __OBJC_$_INSTANCE_VARIABLES_PowerUIRuntimeAwarenessNotifier
+ __OBJC_$_PROP_LIST_PowerUIIBLMNotificationManager
+ __OBJC_$_PROP_LIST_PowerUIRuntimeAwarenessNotifier
+ __OBJC_CLASS_PROTOCOLS_$_PowerUIIBLMNotificationManager
+ __OBJC_CLASS_PROTOCOLS_$_PowerUIRuntimeAwarenessNotifier
+ __OBJC_CLASS_RO_$_PowerUIIBLMNotificationManager
+ __OBJC_CLASS_RO_$_PowerUIRuntimeAwarenessNotifier
+ __OBJC_METACLASS_RO_$_PowerUIIBLMNotificationManager
+ __OBJC_METACLASS_RO_$_PowerUIRuntimeAwarenessNotifier
+ ___39-[PowerUIRuntimeAwarenessNotifier init]_block_invoke
+ ___39-[PowerUIRuntimeAwarenessNotifier init]_block_invoke.25
+ ___39-[PowerUIRuntimeAwarenessNotifier init]_block_invoke_2
+ ___48+[PowerUIIBLMNotificationManager sharedInstance]_block_invoke
+ ___49+[PowerUIRuntimeAwarenessNotifier sharedInstance]_block_invoke
+ ___64-[PowerUIIBLMNotificationManager displayIBLMEngagedNotification]_block_invoke
+ ___64-[PowerUIIBLMNotificationManager displayIBLMEngagedNotification]_block_invoke.cold.1
+ ___74-[PowerUIIBLMNotificationManager recordIBLMFirstUserNotificationResponse:]_block_invoke
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
+ _kIBLMNotification
+ _objc_msgSend$body
+ _objc_msgSend$chargingAdviceNotificationContent
+ _objc_msgSend$chargingAdviceNotificationRequest
+ _objc_msgSend$checkBatteryLevelAndPostNotificationIfNeeded
+ _objc_msgSend$lowRuntimeNotificationContent
+ _objc_msgSend$lowRuntimeNotificationRequest
+ _objc_msgSend$postChargingAdviceNotification
+ _objc_msgSend$postLowRuntimeNotification
+ _objc_msgSend$recordIBLMFirstUserNotificationResponse:
+ _objc_msgSend$setSecond:
+ _objc_msgSend$shouldAdviseToCharge
+ _objc_msgSend$shouldThrottleChargingAdviceNotification
+ _objc_msgSend$timeToEmpty
CStrings:
+ "(SELF.%@.value.rawExternalConnected = %@)"
+ "/System/Library/UserNotifications/Bundles/com.apple.osintelligence.notifications.bundle"
+ "@\"_OSBatteryPredictor\""
+ "ADAPTIVE_POWER_FIRST_TIME_BODY"
+ "ADAPTIVE_POWER_FIRST_TIME_TITLE"
+ "Allowing internal charging advice notification - last sent %f hours ago"
+ "Battery level changed to exactly %d%%"
+ "Content title : %@, Body %@"
+ "Current battery level: %ld%%, last seen: %ld%%"
+ "Device runtime is critically low. Consider charging soon."
+ "Failed to post IBLM notification with identifier %@: %@"
+ "IBLM notification response received: %@"
+ "IBLM-Engaged"
+ "Invalid TTE prediction: %f"
+ "Localizable-IBLM"
+ "No previous TTE notification recorded, allowing internal notification"
+ "Not showing internal charging advice during nighttime hours (current hour: %ld)"
+ "Posted internal charging advice notification, next eligible in 16 hours"
+ "Posting First time IBLM notification"
+ "PowerUIIBLMNotificationManager"
+ "PowerUIIBLMNotificationManager initialized with bundle identifier: %@"
+ "PowerUIRuntimeAwarenessNotifier"
+ "RuntimeAwarenessNotifier initiating..."
+ "Sending IBLM User Notification CA event: %@"
+ "Successfully posted IBLM notification with identifier: %@"
+ "T@\"NSDate\",&,N,V_lastChargingAdviceNotificationDate"
+ "T@\"PowerUILocationSignalMonitor\",&,N,V_locationMonitor"
+ "T@\"_OSBatteryPredictor\",&,N,V_batteryPredictor"
+ "TTE %f hours, %f hours until 9 PM - no charge needed"
+ "TTE %f hours, but %f hours until 9 PM - suggesting charge"
+ "Throttling internal charging advice notification - last sent %f hours ago, threshold is %f hours"
+ "Tq,N,V_lastSeenBatteryLevel"
+ "Triggering LRN check"
+ "Unlikely in known charge location: %@"
+ "Your device may run out of power before 11 pm. Consider charging now."
+ "[Internal] Charging Advice"
+ "[Internal] Low Runtime Warning"
+ "_batteryPredictor"
+ "_lastChargingAdviceNotificationDate"
+ "_lastSeenBatteryLevel"
+ "_locationMonitor"
+ "batteryPredictor"
+ "body"
+ "chargeRec"
+ "chargingAdviceCategory"
+ "chargingAdviceNotificationContent"
+ "chargingAdviceNotificationRequest"
+ "chargingAdviceRequest"
+ "checkBatteryLevelAndPostNotificationIfNeeded"
+ "com.apple.osi.iblm.engagedNotification"
+ "com.apple.osintelligence.iblm.userNotificationResponse"
+ "com.apple.osintelligence.notifications"
+ "com.apple.powerui.iblm"
+ "com.apple.powerui.iblmnotificationmanager.queue"
+ "com.apple.powerui.runtimeAwareness"
+ "com.apple.powerui.runtimeAwareness.run"
+ "com.apple.powerui.runtimeAwarenessNotifications"
+ "com.apple.powerui.runtimeAwarenessNotifier"
+ "com.apple.powerui.runtimeawarenessqueue"
+ "displayIBLMEngagedNotification"
+ "firstTimeIBLMCategory"
+ "lastChargingAdviceNotificationDate"
+ "lastSeenBatteryLevel"
+ "locationMonitor"
+ "lowRuntimeCategory"
+ "lowRuntimeNotificationContent"
+ "lowRuntimeNotificationRequest"
+ "lowRuntimeRequest"
+ "notificationResponse"
+ "postChargingAdviceNotification"
+ "postLowRuntimeNotification"
+ "recordIBLMFirstUserNotificationResponse:"
+ "runtimeAwarenessNotifications"
+ "runtimeWarning"
+ "setBatteryPredictor:"
+ "setLastChargingAdviceNotificationDate:"
+ "setLastSeenBatteryLevel:"
+ "setLocationMonitor:"
+ "setSecond:"
+ "settings-navigation://com.apple.Settings.Battery/POWER_MODE_SPECIFIER_IDENTIFIER"
+ "shouldAdviseToCharge"
+ "shouldThrottleChargingAdviceNotification"
+ "timeToEmpty"

```
