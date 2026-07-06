## diskimagescontroller

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.logd"))
 		(require-not (require-any
 			(global-name "com.apple.diskimagesiod.ram.xpc")
 			(global-name "com.apple.diskimagesiod.spb.xpc")
 			(global-name "com.apple.diskimagesiod.xpc")
 		))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (system-attribute developer-mode))

 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
-			(require-not (mac-syscall-number 86))
 			(require-not (mac-syscall-number 85))
+			(require-not (mac-syscall-number 86))
 			(require-not (mac-syscall-number 67))
 			(require-not (mac-syscall-number 2))
 		)
```
