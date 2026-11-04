## CommandAndControl

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.accessibility.AXSpringBoardServer"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.sysdiagnose.service.xpc"))
+		(require-not (global-name "com.apple.dt.automationmode.reader"))
 		(require-not (global-name "com.apple.feedbackd.centralized-feedback"))
 		(require-not (global-name "com.apple.DragUI.druid.destination"))
 		(require-not (require-any

 		SYS_fsetxattr
 		SYS_listxattr
 		SYS_fsctl
+		SYS_posix_spawn
 		SYS_ffsctl
 		SYS_shm_open
 		SYS_sem_open

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 5))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(with-filter (mac-policy-name "vnguard")
+	(deny system-mac-syscall
+		(require-not (mac-syscall-number 1))
 	)
 )
 (deny system-mac-syscall
```
