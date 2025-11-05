## UserNotifications

> `/System/Library/Frameworks/UserNotifications.framework/Versions/A/UserNotifications`

```diff

-579.4.3.401.0
-  __TEXT.__text: 0x3228c
+579.5.24.0.0
+  __TEXT.__text: 0x32904
   __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_methlist: 0x2f44
-  __TEXT.__cstring: 0x31fa
+  __TEXT.__objc_methlist: 0x33f8
+  __TEXT.__cstring: 0x323a
   __TEXT.__const: 0xd0
   __TEXT.__oslogstring: 0x1f85
   __TEXT.__gcc_except_tab: 0x220
   __TEXT.__dlopen_cstrs: 0x8a
   __TEXT.__unwind_info: 0xc30
   __TEXT.__objc_classname: 0x8e5
-  __TEXT.__objc_methname: 0x90f7
-  __TEXT.__objc_methtype: 0x120d
-  __TEXT.__objc_stubs: 0x4e40
+  __TEXT.__objc_methname: 0x92f6
+  __TEXT.__objc_methtype: 0x1257
+  __TEXT.__objc_stubs: 0x4e60
   __DATA_CONST.__got: 0x390
   __DATA_CONST.__const: 0x318
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ac0
+  __DATA_CONST.__objc_selrefs: 0x1b68
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x118
   __AUTH_CONST.__auth_got: 0x268
   __AUTH_CONST.__const: 0xac0
-  __AUTH_CONST.__cfstring: 0x3280
-  __AUTH_CONST.__objc_const: 0x9dc8
+  __AUTH_CONST.__cfstring: 0x32a0
+  __AUTH_CONST.__objc_const: 0x95d8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x310
+  __DATA.__objc_ivar: 0x314
   __DATA.__data: 0x728
   __DATA.__bss: 0x78
   __DATA.__common: 0x38

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8AEE99DE-D865-33CB-94E1-A3451B260A97
-  Functions: 1250
-  Symbols:   3126
-  CStrings:  2522
+  UUID: AC19FBEC-30E6-3DFC-A26A-84A3824CC141
+  Functions: 1280
+  Symbols:   3161
+  CStrings:  2531
 
Symbols:
+ +[NSBundle(UserNotifications) userNotificationsBundleWithIdentifier:].cold.1
+ +[UNAttachmentUtilities _systemDirectoryURL].cold.1
+ +[UNNotificationSettings settingsWithAuthorizationStatus:soundSetting:badgeSetting:alertSetting:notificationCenterSetting:lockScreenSetting:carPlaySetting:remoteNotificationsSetting:announcementSetting:criticalAlertSetting:timeSensitiveSetting:scheduledDeliverySetting:directMessagesSetting:summarizationSetting:prioritizationSetting:alertStyle:showPreviewsSetting:groupingSetting:providesAppNotificationSettings:]
+ +[UNUserNotificationCenterDelegateConnectionListener sharedInstance].cold.1
+ +[UNUserNotificationCenterDelegateService serverInterface].cold.1
+ +[UNUserNotificationService clientInterface].cold.1
+ +[UNUserNotificationService serverInterface].cold.1
+ +[UNUserNotificationServiceConnection sharedInstance].cold.1
+ +[_UNNotificationServiceExtensionContext _extensionAuxiliaryHostProtocol].cold.1
+ +[_UNNotificationServiceExtensionContext _extensionAuxiliaryVendorProtocol].cold.1
+ -[UNCalendarNotificationTrigger _initWithDateComponents:repeats:].cold.1
+ -[UNCalendarNotificationTrigger nextTriggerDateAfterDate:withRequestedDate:].cold.1
+ -[UNCalendarNotificationTrigger nextTriggerDateAfterDate:withRequestedDate:].cold.2
+ -[UNLegacyNotificationTrigger _nextTriggerDateAfterDate:withRequestedDate:defaultTimeZone:].cold.1
+ -[UNLocationNotificationTrigger _initWithRegion:repeats:].cold.1
+ -[UNMutableNotificationSettings setPrioritizationSetting:]
+ -[UNNotificationRequest _initWithIdentifier:content:trigger:destinations:].cold.1
+ -[UNNotificationSettings initWithAuthorizationStatus:soundSetting:badgeSetting:alertSetting:notificationCenterSetting:lockScreenSetting:carPlaySetting:remoteNotificationsSetting:announcementSetting:criticalAlertSetting:timeSensitiveSetting:scheduledDeliverySetting:directMessagesSetting:summarizationSetting:prioritizationSetting:alertStyle:showPreviewsSetting:groupingSetting:providesAppNotificationSettings:]
+ -[UNNotificationSettings prioritizationSetting]
+ -[UNTimeIntervalNotificationTrigger _initWithTimeInterval:repeats:].cold.1
+ -[UNTimeIntervalNotificationTrigger _initWithTimeInterval:repeats:].cold.2
+ -[UNTimeIntervalNotificationTrigger nextTriggerDateAfterDate:withRequestedDate:].cold.1
+ -[UNTimeIntervalNotificationTrigger nextTriggerDateAfterDate:withRequestedDate:].cold.2
+ -[UNUserNotificationCenter initWithBundleIdentifier:queue:].cold.1
+ OBJC_IVAR_$_UNNotificationSettings._prioritizationSetting
+ UNBundle.cold.1
+ UNRegisterUserNotificationsLogging.cold.1
+ _UNCTopicSummaries
+ __53+[UNUserNotificationCenter currentNotificationCenter]_block_invoke.cold.1
+ __53+[UNUserNotificationCenter currentNotificationCenter]_block_invoke.cold.2
+ __53+[UNUserNotificationCenter currentNotificationCenter]_block_invoke.cold.3
+ __53+[UNUserNotificationCenter currentNotificationCenter]_block_invoke.cold.4
+ __53+[UNUserNotificationCenter currentNotificationCenter]_block_invoke.cold.5
+ _objc_msgSend$initWithAuthorizationStatus:soundSetting:badgeSetting:alertSetting:notificationCenterSetting:lockScreenSetting:carPlaySetting:remoteNotificationsSetting:announcementSetting:criticalAlertSetting:timeSensitiveSetting:scheduledDeliverySetting:directMessagesSetting:summarizationSetting:prioritizationSetting:alertStyle:showPreviewsSetting:groupingSetting:providesAppNotificationSettings:
+ _objc_msgSend$prioritizationSetting
- -[UNNotificationSettings initWithAuthorizationStatus:soundSetting:badgeSetting:alertSetting:notificationCenterSetting:lockScreenSetting:carPlaySetting:remoteNotificationsSetting:announcementSetting:criticalAlertSetting:timeSensitiveSetting:scheduledDeliverySetting:directMessagesSetting:summarizationSetting:alertStyle:showPreviewsSetting:groupingSetting:providesAppNotificationSettings:]
- _objc_msgSend$initWithAuthorizationStatus:soundSetting:badgeSetting:alertSetting:notificationCenterSetting:lockScreenSetting:carPlaySetting:remoteNotificationsSetting:announcementSetting:criticalAlertSetting:timeSensitiveSetting:scheduledDeliverySetting:directMessagesSetting:summarizationSetting:alertStyle:showPreviewsSetting:groupingSetting:providesAppNotificationSettings:
CStrings:
+ "<%@: %p; authorizationStatus: %@, notificationCenterSetting: %@, soundSetting: %@, badgeSetting: %@, lockScreenSetting: %@, carPlaySetting: %@, remoteNotifications: %@, announcementSetting: %@, criticalAlertSetting: %@, timeSensitiveSetting: %@, alertSetting: %@, scheduledDeliverySetting: %@, directMessagesSetting: %@, summarizationSetting: %@, prioritizationSetting: %@, showsPreviewsSetting: %@, alertStyle: %@, groupingSetting: %@ providesAppNotificationSettings: %@>"
+ "@164@0:8q16q24q32q40q48q56q64q72q80q88q96q104q112q120q128q136q144q152B160"
+ "TopicSummaries"
+ "Tq,R,V_prioritizationSetting"
+ "_prioritizationSetting"
+ "initWithAuthorizationStatus:soundSetting:badgeSetting:alertSetting:notificationCenterSetting:lockScreenSetting:carPlaySetting:remoteNotificationsSetting:announcementSetting:criticalAlertSetting:timeSensitiveSetting:scheduledDeliverySetting:directMessagesSetting:summarizationSetting:prioritizationSetting:alertStyle:showPreviewsSetting:groupingSetting:providesAppNotificationSettings:"
+ "prioritizationSetting"
+ "setPrioritizationSetting:"
+ "settingsWithAuthorizationStatus:soundSetting:badgeSetting:alertSetting:notificationCenterSetting:lockScreenSetting:carPlaySetting:remoteNotificationsSetting:announcementSetting:criticalAlertSetting:timeSensitiveSetting:scheduledDeliverySetting:directMessagesSetting:summarizationSetting:prioritizationSetting:alertStyle:showPreviewsSetting:groupingSetting:providesAppNotificationSettings:"
- "<%@: %p; authorizationStatus: %@, notificationCenterSetting: %@, soundSetting: %@, badgeSetting: %@, lockScreenSetting: %@, carPlaySetting: %@, remoteNotifications: %@, announcementSetting: %@, criticalAlertSetting: %@, timeSensitiveSetting: %@, alertSetting: %@, scheduledDeliverySetting: %@, directMessagesSetting: %@, summarizationSetting: %@, showsPreviewsSetting: %@, alertStyle: %@, groupingSetting: %@ providesAppNotificationSettings: %@>"
- "initWithAuthorizationStatus:soundSetting:badgeSetting:alertSetting:notificationCenterSetting:lockScreenSetting:carPlaySetting:remoteNotificationsSetting:announcementSetting:criticalAlertSetting:timeSensitiveSetting:scheduledDeliverySetting:directMessagesSetting:summarizationSetting:alertStyle:showPreviewsSetting:groupingSetting:providesAppNotificationSettings:"

```
