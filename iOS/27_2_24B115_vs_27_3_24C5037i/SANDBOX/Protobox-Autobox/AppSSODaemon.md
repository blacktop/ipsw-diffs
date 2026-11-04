## AppSSODaemon

> Group: ⬆️ Updated

```diff

 		SYS___sigwait_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
+		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
-			(require-not (mac-syscall-number 4 6 7))
+			(require-not (mac-syscall-number 6 7))
+			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number (_IO "" 5)))
 			(require-not (mac-syscall-number 67))
 			(require-not (mac-syscall-number 2))
```
