## clocksyncd

> Group: ⬆️ Updated

```diff

 
 (deny mach-issue-extension)
 
-(deny mach-lookup)
+(deny mach-lookup
+	(require-all
+		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.locationd.synchronous"))
+		(require-not (global-name "com.apple.locationd.routine"))
+		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.FileCoordination"))
+		(require-not (system-attribute developer-mode))
+	)
+)
 
 (deny process-exec*)
 

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 90 96)
-		(require-not (mac-policy-name "AMFI"))
+(with-filter (mac-policy-name "AMFI")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 96))
+			(require-not (mac-syscall-number 90))
+		)
 	)
 )
 (deny system-mac-syscall
```
