## distnoted

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
