## ptpd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))
+		(require-not (global-name "com.apple.coremedia.mediaparserd.formatreader.xpc"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.assetimagegenerator.xpc"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
 		(require-not (global-name "com.apple.lsd.mapdb"))

 		mach_voucher_attr_command
 		UNDNotificationCreated_rpc
 		task_restartable_ranges_register
-		task_restartable_ranges_synchronize)
+		task_restartable_ranges_synchronize
+		mach_eventlink_create)
 )
 
 (deny sysctl*
```
