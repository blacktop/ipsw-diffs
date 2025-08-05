## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`

```diff

-220.0.0.0.0
-  __TEXT.__text: 0x16b60
+222.0.3.0.0
+  __TEXT.__text: 0x18034
   __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0x1ed0
-  __TEXT.__const: 0x140
-  __TEXT.__cstring: 0x1435
-  __TEXT.__gcc_except_tab: 0x5f8
-  __TEXT.__oslogstring: 0x18d7
-  __TEXT.__unwind_info: 0x888
-  __TEXT.__objc_classname: 0x41c
-  __TEXT.__objc_methname: 0x37e1
-  __TEXT.__objc_methtype: 0xab8
-  __TEXT.__objc_stubs: 0x27e0
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x7d8
-  __DATA_CONST.__objc_classlist: 0xd0
-  __DATA_CONST.__objc_protolist: 0x70
+  __TEXT.__objc_methlist: 0x2018
+  __TEXT.__const: 0x150
+  __TEXT.__cstring: 0x1701
+  __TEXT.__gcc_except_tab: 0x628
+  __TEXT.__oslogstring: 0x19df
+  __TEXT.__unwind_info: 0x8e0
+  __TEXT.__objc_classname: 0x455
+  __TEXT.__objc_methname: 0x3da6
+  __TEXT.__objc_methtype: 0xbb5
+  __TEXT.__objc_stubs: 0x2c40
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x828
+  __DATA_CONST.__objc_classlist: 0xd8
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf00
+  __DATA_CONST.__objc_selrefs: 0x1068
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x2f8
-  __AUTH_CONST.__const: 0x760
-  __AUTH_CONST.__cfstring: 0x1120
-  __AUTH_CONST.__objc_const: 0x2c70
-  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__const: 0x7a0
+  __AUTH_CONST.__cfstring: 0x1340
+  __AUTH_CONST.__objc_const: 0x2e88
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x194
-  __DATA.__data: 0x540
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x1a8
+  __DATA.__data: 0x5a0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x640
-  __DATA_DIRTY.__bss: 0x88
+  __DATA_DIRTY.__bss: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C49DB961-3091-3AA3-91FE-64D25F530E1C
-  Functions: 814
-  Symbols:   2721
-  CStrings:  1234
+  UUID: F755E707-80EB-37FA-9700-02DDE8440BC2
+  Functions: 846
+  Symbols:   2857
+  CStrings:  1338
 
Symbols:
+ +[_OSIBLMAnalyticsHandler currentBatteryLevel]
+ +[_OSINotificationManager sharedInstance]
+ +[_OSINotificationManager sharedInstance].cold.1
+ -[_OSIAutoLPMManager evaluateAutoLPMDisengagement]
+ -[_OSIBLMAnalyticsHandler recordIBLMFirstUserNotificationResponse:]
+ -[_OSIBLMAnalyticsHandler recordIBLMFirstUserNotificationTrigger:]
+ -[_OSIBLManager engagementThreshold]
+ -[_OSIBLManager firstTimeNotificationState]
+ -[_OSIBLManager handleFirstTimeNotification]
+ -[_OSIBLManager setEngagementThreshold:]
+ -[_OSIBLManager setFirstTimeNotificationState:]
+ -[_OSIBLManager setTrialIBLMDrainPredictionThreshold:]
+ -[_OSIBLManager trialIBLMDrainPredictionThreshold]
+ -[_OSINotificationManager .cxx_destruct]
+ -[_OSINotificationManager init]
+ -[_OSINotificationManager log]
+ -[_OSINotificationManager notificationRequestWith:content:]
+ -[_OSINotificationManager postIBLMFirstTimeNotification]
+ -[_OSINotificationManager postNotificationWith:content:]
+ -[_OSINotificationManager setLog:]
+ -[_OSINotificationManager setUnCenter:]
+ -[_OSINotificationManager unCenter]
+ -[_OSINotificationManager userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:]
+ GCC_except_table4
+ GCC_except_table5
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_UNMutableNotificationContent
+ _OBJC_CLASS_$_UNNotificationIcon
+ _OBJC_CLASS_$_UNNotificationRequest
+ _OBJC_CLASS_$_UNUserNotificationCenter
+ _OBJC_CLASS_$__OSINotificationManager
+ _OBJC_IVAR_$__OSIBLManager._engagementThreshold
+ _OBJC_IVAR_$__OSIBLManager._firstTimeNotificationState
+ _OBJC_IVAR_$__OSIBLManager._trialIBLMDrainPredictionThreshold
+ _OBJC_IVAR_$__OSINotificationManager._log
+ _OBJC_IVAR_$__OSINotificationManager._unCenter
+ _OBJC_METACLASS_$__OSINotificationManager
+ _UNNotificationDefaultActionIdentifier
+ _UNNotificationDismissActionIdentifier
+ __OBJC_$_CLASS_METHODS__OSINotificationManager
+ __OBJC_$_INSTANCE_METHODS__OSINotificationManager
+ __OBJC_$_INSTANCE_VARIABLES__OSINotificationManager
+ __OBJC_$_PROP_LIST__OSINotificationManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UNUserNotificationCenterDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UNUserNotificationCenterDelegate
+ __OBJC_$_PROTOCOL_REFS_UNUserNotificationCenterDelegate
+ __OBJC_CLASS_PROTOCOLS_$__OSINotificationManager
+ __OBJC_CLASS_RO_$__OSINotificationManager
+ __OBJC_LABEL_PROTOCOL_$_UNUserNotificationCenterDelegate
+ __OBJC_METACLASS_RO_$__OSINotificationManager
+ __OBJC_PROTOCOL_$_UNUserNotificationCenterDelegate
+ ___21-[_OSIBLManager init]_block_invoke.79
+ ___21-[_OSIBLManager init]_block_invoke_2.81
+ ___21-[_OSIBLManager init]_block_invoke_3
+ ___22-[_OSIBLManager start]_block_invoke.103
+ ___22-[_OSIBLManager start]_block_invoke.106
+ ___27-[_OSIAutoLPMManager start]_block_invoke.31
+ ___27-[_OSIAutoLPMManager start]_block_invoke_2.32
+ ___27-[_OSIAutoLPMManager start]_block_invoke_3
+ ___27-[_OSIAutoLPMManager start]_block_invoke_4
+ ___33-[_OSIBLMState monitorForAutoLPM]_block_invoke_4
+ ___41+[_OSINotificationManager sharedInstance]_block_invoke
+ ___41-[_OSIBLManager updateTrialOSIParameters]_block_invoke.91
+ ___54-[_OSIBLMAnalyticsHandler historicalDrainDataForDate:]_block_invoke.101
+ ___56-[_OSINotificationManager postNotificationWith:content:]_block_invoke
+ ___56-[_OSINotificationManager postNotificationWith:content:]_block_invoke.cold.1
+ ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke.105
+ ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke.106
+ ___66-[_OSIBLMAnalyticsHandler recordIBLMFirstUserNotificationTrigger:]_block_invoke
+ ___67-[_OSIBLMAnalyticsHandler recordIBLMFirstUserNotificationResponse:]_block_invoke
+ ___block_descriptor_32_e8_v12?0i8l
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8lw32l8
+ ___block_literal_global.118
+ ___block_literal_global.85
+ ___kCFBooleanTrue
+ _kIBLMDefaultsPresentedFirstUserNotification
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$actionIdentifier
+ _objc_msgSend$addNotificationRequest:withCompletionHandler:
+ _objc_msgSend$batteryPercentageKey
+ _objc_msgSend$body
+ _objc_msgSend$bundleWithURL:
+ _objc_msgSend$currentBatteryLevel
+ _objc_msgSend$evaluateAutoLPMDisengagement
+ _objc_msgSend$handleFirstTimeNotification
+ _objc_msgSend$iconNamed:
+ _objc_msgSend$initFileURLWithPath:
+ _objc_msgSend$initWithBundleIdentifier:
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$notificationRequestWith:content:
+ _objc_msgSend$postIBLMFirstTimeNotification
+ _objc_msgSend$recordIBLMFirstUserNotificationResponse:
+ _objc_msgSend$recordIBLMFirstUserNotificationTrigger:
+ _objc_msgSend$requestWithIdentifier:content:trigger:
+ _objc_msgSend$setBody:
+ _objc_msgSend$setCategoryIdentifier:
+ _objc_msgSend$setContext:
+ _objc_msgSend$setDefaultActionURL:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setDestinations:
+ _objc_msgSend$setExpirationDate:
+ _objc_msgSend$setIcon:
+ _objc_msgSend$setQueue:
+ _objc_msgSend$setShouldHideDate:
+ _objc_msgSend$setShouldIgnoreDoNotDisturb:
+ _objc_msgSend$setShouldIgnoreDowntime:
+ _objc_msgSend$setShouldPreventNotificationDismissalAfterDefaultAction:
+ _objc_msgSend$setShouldSuppressScreenLightUp:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$setWantsNotificationResponsesDelivered
+ _objc_msgSend$title
- ___21-[_OSIBLManager init]_block_invoke.73
- ___21-[_OSIBLManager init]_block_invoke_2.75
- ___22-[_OSIBLManager start]_block_invoke.92
- ___22-[_OSIBLManager start]_block_invoke.95
- ___27-[_OSIAutoLPMManager start]_block_invoke.23
- ___27-[_OSIAutoLPMManager start]_block_invoke_2.24
- ___41-[_OSIBLManager updateTrialOSIParameters]_block_invoke.80
- ___54-[_OSIBLMAnalyticsHandler historicalDrainDataForDate:]_block_invoke.92
- ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke.96
- ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke.97
- ___block_literal_global.109
CStrings:
+ "/System/Library/UserNotifications/Bundles/com.apple.osintelligence.notifications.bundle"
+ "@\"NSNumber\""
+ "@\"UNUserNotificationCenter\""
+ "ADAPTIVE_POWER_FIRST_TIME_BODY"
+ "ADAPTIVE_POWER_FIRST_TIME_TITLE"
+ "Content title : %@, Body %@"
+ "IBLM-FirstTime"
+ "IBLM_EngagementPredictionThreshold"
+ "Localizable-IBLM"
+ "Posted notification with error: %@"
+ "Posting First time notification"
+ "Prev12Next12Drain Prediction Confidence: %lf Engagement Threshold: %f"
+ "SELF.%@.value == %@ OR SELF.%@.value == %@ OR SELF.%@.value == %@ OR SELF.%@.value == %@"
+ "Sending IBLM User Notification CA event: %@"
+ "T@\"NSNumber\",&,N,V_firstTimeNotificationState"
+ "T@\"UNUserNotificationCenter\",&,N,V_unCenter"
+ "Td,N,V_engagementThreshold"
+ "Td,N,V_trialIBLMDrainPredictionThreshold"
+ "Trial: %@:%f"
+ "UNUserNotificationCenterDelegate"
+ "URLWithString:"
+ "_OSINotificationManager"
+ "_engagementThreshold"
+ "_firstTimeNotificationState"
+ "_trialIBLMDrainPredictionThreshold"
+ "_unCenter"
+ "actionIdentifier"
+ "addNotificationRequest:withCompletionHandler:"
+ "autoLPMDisengaged"
+ "autoLPMDisengagedTime"
+ "battery-rcl"
+ "batteryPercentageKey"
+ "body"
+ "bundleWithURL:"
+ "com.apple.osi.iblm.firstUserNotification"
+ "com.apple.osintelligence.iblm.autoLPMpluggedInState"
+ "com.apple.osintelligence.iblm.userNotificationResponse"
+ "com.apple.osintelligence.notifications"
+ "currentBatteryLevel"
+ "engagementThreshold"
+ "evaluateAutoLPMDisengagement"
+ "firstTimeIBLMCategory"
+ "firstTimeNotificationState"
+ "handleFirstTimeNotification"
+ "iconNamed:"
+ "initFileURLWithPath:"
+ "initWithBundleIdentifier:"
+ "localizedStringForKey:value:table:"
+ "notification request coming in for %@: %@"
+ "notificationRequestWith:content:"
+ "notificationResponse"
+ "notificationTrigger"
+ "notifications"
+ "postIBLMFirstTimeNotification"
+ "postNotificationWith:content:"
+ "presentedFirstUserNotification"
+ "recordIBLMFirstUserNotificationResponse:"
+ "recordIBLMFirstUserNotificationTrigger:"
+ "requestWithIdentifier:content:trigger:"
+ "setBody:"
+ "setCategoryIdentifier:"
+ "setDefaultActionURL:"
+ "setDelegate:"
+ "setDestinations:"
+ "setEngagementThreshold:"
+ "setExpirationDate:"
+ "setFirstTimeNotificationState:"
+ "setIcon:"
+ "setShouldHideDate:"
+ "setShouldIgnoreDoNotDisturb:"
+ "setShouldIgnoreDowntime:"
+ "setShouldPreventNotificationDismissalAfterDefaultAction:"
+ "setShouldSuppressScreenLightUp:"
+ "setTitle:"
+ "setTrialIBLMDrainPredictionThreshold:"
+ "setUnCenter:"
+ "setWantsNotificationResponsesDelivered"
+ "settings-navigation://com.apple.Settings.Battery/POWER_MODE_SPECIFIER_IDENTIFIER"
+ "title"
+ "trialIBLMDrainPredictionThreshold"
+ "unCenter"
+ "userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:"
+ "userNotificationCenter:openSettingsForNotification:"
+ "userNotificationCenter:willPresentNotification:withCompletionHandler:"
+ "v32@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24"
+ "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24@?<v@?Q>32"
+ "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotificationResponse\"24@?<v@?>32"
+ "v40@0:8@16@24@?32"
- "SELF.%@.value = %@"

```
