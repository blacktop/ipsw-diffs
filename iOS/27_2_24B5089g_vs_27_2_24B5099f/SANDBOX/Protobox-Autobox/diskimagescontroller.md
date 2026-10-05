## diskimagescontroller

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (require-any
+			(global-name "com.apple.amberd")
 			(global-name "com.apple.diskimagesiod.ram.xpc")
 			(global-name "com.apple.diskimagesiod.spb.xpc")
 			(global-name "com.apple.diskimagesiod.xpc")
 		))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
