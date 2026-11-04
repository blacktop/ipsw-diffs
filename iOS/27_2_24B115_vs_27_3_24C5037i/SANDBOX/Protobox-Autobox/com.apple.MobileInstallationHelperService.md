## com.apple.MobileInstallationHelperService

> Group: ⬆️ Updated

```diff

 		SYS_pread_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
+		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_close_np
 		SYS_guarded_kqueue_np

 
 (deny system-kas-info)
 
-(with-filter (mac-policy-name "Sandbox")
-	(deny system-mac-syscall
-		(require-all
-			(require-not (mac-syscall-number 80))
-			(require-not (mac-syscall-number 7))
-			(require-not (mac-syscall-number 6))
-			(require-not (mac-syscall-number 67))
-			(require-not (mac-syscall-number 5))
-			(require-not (mac-syscall-number 4))
-			(require-not (mac-syscall-number 2))
-		)
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
