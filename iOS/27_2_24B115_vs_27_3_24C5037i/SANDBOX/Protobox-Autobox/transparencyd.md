## transparencyd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.algosd"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.transparencyd.ids"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.logd.events"))

 		SYS___sigwait_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
+		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_open_np
 		SYS_guarded_close_np

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
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
