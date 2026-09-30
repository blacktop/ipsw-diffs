## UARPAssetManagerServiceiCloud

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.logd"))
 		(require-any
 			(process-attribute is-autoboxed)
 			(require-all
```
