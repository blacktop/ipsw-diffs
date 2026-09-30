## fseventsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (system-attribute developer-mode))
```
