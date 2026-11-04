## com.apple.StreamingUnzipService

> Group: ⬆️ Updated

```diff

 		SYS_pread_nocancel
 		SYS___sigwait_nocancel
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
```
