## mapinspectord

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.mapinspectord"))
 		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.mapinspectord"))
 		(require-not (xpc-service-name "com.apple.mapinspectord"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.diagnosticd"))
```
