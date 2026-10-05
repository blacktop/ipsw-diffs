## HomeKitDaemon

> `FileSystem/System/Library/PrivateFrameworks/HomeKitDaemon.framework/HomeKitDaemon-IntelligentNotifications.loctable`

```diff

 en.INTELLIGENT_NOTIFICATION_USER_LEAVING_HOME = "%1$@ leaving %2$@"
 en.INTELLIGENT_NOTIFICATION_USER_LEFT = "%@ left"
 en.INTELLIGENT_NOTIFICATION_USER_LEFT_HOME = "%1$@ left %2$@"
-en.VIDEO_SUMMARIES_ADMIN_DOWNGRADE_LIMITED_BODY = "The iCloud+ plan for %1$@ includes video summaries for up to %2$ld cameras. You can manage video summaries in Home."
+en.VIDEO_SUMMARIES_ADMIN_DOWNGRADE_LIMITED_BODY.NSStringLocalizedFormatKey = "The iCloud+ plan for %1$@ includes video summaries for up to %2$#@cameraCount@. You can manage video summaries in Home."
+en.VIDEO_SUMMARIES_ADMIN_DOWNGRADE_LIMITED_BODY.cameraCount.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.VIDEO_SUMMARIES_ADMIN_DOWNGRADE_LIMITED_BODY.cameraCount.NSStringFormatValueTypeKey = "ld"
+en.VIDEO_SUMMARIES_ADMIN_DOWNGRADE_LIMITED_BODY.cameraCount.one = "%2$ld camera"
+en.VIDEO_SUMMARIES_ADMIN_DOWNGRADE_LIMITED_BODY.cameraCount.other = "%2$ld cameras"
 en.VIDEO_SUMMARIES_ADMIN_UNAVAILABLE_BODY = "The iCloud+ plan for %@ no longer includes video summaries."
 en.VIDEO_SUMMARIES_ADMIN_UNLIMITED_BODY = "The iCloud+ plan for %@ includes video summaries for all cameras. You can turn on video summaries in Home."
-en.VIDEO_SUMMARIES_ADMIN_UPGRADE_LIMITED_BODY = "The iCloud+ plan for %1$@ includes video summaries for up to %2$ld cameras. You can turn on video summaries in Home."
-en.VIDEO_SUMMARIES_AVAILABLE_LIMITED_BODY = "Your current iCloud+ plan includes video summaries for up to %ld cameras. You can turn on video summaries in Home."
+en.VIDEO_SUMMARIES_ADMIN_UPGRADE_LIMITED_BODY.NSStringLocalizedFormatKey = "The iCloud+ plan for %1$@ includes video summaries for up to %2$#@cameraCount@. You can turn on video summaries in Home."
+en.VIDEO_SUMMARIES_ADMIN_UPGRADE_LIMITED_BODY.cameraCount.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.VIDEO_SUMMARIES_ADMIN_UPGRADE_LIMITED_BODY.cameraCount.NSStringFormatValueTypeKey = "ld"
+en.VIDEO_SUMMARIES_ADMIN_UPGRADE_LIMITED_BODY.cameraCount.one = "%2$ld camera"
+en.VIDEO_SUMMARIES_ADMIN_UPGRADE_LIMITED_BODY.cameraCount.other = "%2$ld cameras"
+en.VIDEO_SUMMARIES_AVAILABLE_LIMITED_BODY.NSStringLocalizedFormatKey = "Your current iCloud+ plan includes video summaries for up to %#@cameraCount@. You can turn on video summaries in Home."
+en.VIDEO_SUMMARIES_AVAILABLE_LIMITED_BODY.cameraCount.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.VIDEO_SUMMARIES_AVAILABLE_LIMITED_BODY.cameraCount.NSStringFormatValueTypeKey = "ld"
+en.VIDEO_SUMMARIES_AVAILABLE_LIMITED_BODY.cameraCount.one = "%ld camera"
+en.VIDEO_SUMMARIES_AVAILABLE_LIMITED_BODY.cameraCount.other = "%ld cameras"
 en.VIDEO_SUMMARIES_AVAILABLE_TITLE = "Video Summaries Available"
 en.VIDEO_SUMMARIES_AVAILABLE_UNLIMITED_BODY = "Your current iCloud+ plan includes video summaries for all cameras. You can turn on video summaries in Home."
 en.VIDEO_SUMMARIES_UNAVAILABLE_BODY = "Your current iCloud+ plan does not include video summaries. You can manage your plan in Apple Account settings."

```
