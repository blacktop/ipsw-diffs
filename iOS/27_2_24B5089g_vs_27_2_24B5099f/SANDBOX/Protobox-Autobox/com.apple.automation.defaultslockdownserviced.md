## com.apple.automation.defaultslockdownserviced

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.aggregated"))
```
