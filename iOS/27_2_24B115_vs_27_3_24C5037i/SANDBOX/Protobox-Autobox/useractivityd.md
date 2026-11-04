## useractivityd

> Group: ⬆️ Updated

```diff

 		SYS_exit
 		SYS_read
 		SYS_open
+		SYS_close
 		SYS_getfsstat
 		SYS_getpid
 		SYS_getuid

 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_renameat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat

 		SYS_guarded_open_dprotected_np
 		SYS_persona
 		SYS_getentropy
+		SYS_necp_open
+		SYS___channel_open
 		SYS_ulock_wait
 		SYS_ulock_wake
 		SYS_terminate_with_payload

 
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
