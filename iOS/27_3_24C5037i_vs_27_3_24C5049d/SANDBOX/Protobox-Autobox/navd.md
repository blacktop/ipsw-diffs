## navd

> Group: ⬆️ Updated

```diff

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
-				(require-not (require-any
-					(global-name "P.-")
-					(global-name "P.S")
-				))
-				(require-not (global-name "P.o"))
+				(require-not (global-name "com.apple.AccessoryServices"))
 				(require-not (system-attribute developer-mode))
 			)
 			(require-all
 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
-				(require-not (require-any
-					(global-name "P.-")
-					(global-name "P.S")
-				))
-				(require-not (global-name "P.o"))
+				(require-not (global-name "com.apple.AccessoryServices"))
 				(require-not (system-attribute developer-mode))
 			)
 		)
```
