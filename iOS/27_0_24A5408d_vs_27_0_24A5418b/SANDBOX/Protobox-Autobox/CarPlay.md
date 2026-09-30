## CarPlay

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.carkit.reconnectiontime.service"))
 		(require-not (global-name "com.apple.coreduetd.knowledge"))
 		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.tailspind"))
 		(require-not (global-name "com.apple.assistant.uibridge-service"))
 		(require-not (require-any
 			(global-name "com.apple.assistant.request-dispatcher.uibridge-service")
```
