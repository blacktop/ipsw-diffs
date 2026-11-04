## com.apple.dt.instruments.dtsecurity

> Group: ⬆️ Updated

```diff

 		SYS___sigwait_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
+		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_close_np
 		SYS_proc_rlimit_control

 			(sysctl-name "kperf.timer.action")
 			(sysctl-name "kperf.timer.period")
 		))
+		(require-not (sysctl-name "kperf.blessed_pid"))
 		(require-not (sysctl-name "vm.debug_range_enabled"))
 		(require-not (require-any
 			(sysctl-name "kpc.actionid")

 
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
```
