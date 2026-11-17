## ScreenSharingServer

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (xpc-service-name "com.apple.accessibility.AccessibilityUIServer"))
+		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
```
