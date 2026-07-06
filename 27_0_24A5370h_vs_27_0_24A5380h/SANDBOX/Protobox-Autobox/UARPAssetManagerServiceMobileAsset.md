## UARPAssetManagerServiceMobileAsset

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
```
