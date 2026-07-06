## CorePrescriptionService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.healthd.server"))
+		(require-not (global-name "com.apple.securityd"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
