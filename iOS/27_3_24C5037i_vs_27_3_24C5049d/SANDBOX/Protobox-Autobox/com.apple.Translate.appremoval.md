## com.apple.Translate.appremoval

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.translationd"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (system-attribute developer-mode))
 	)
```
