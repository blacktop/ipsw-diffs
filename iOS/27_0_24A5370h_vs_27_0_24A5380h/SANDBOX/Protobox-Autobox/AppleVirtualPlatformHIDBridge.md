## AppleVirtualPlatformHIDBridge

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.iohideventsystem"))
-		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.iohideventsystem"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
