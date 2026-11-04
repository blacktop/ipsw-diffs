## videocodecd

> Group: ⬆️ Updated

```diff

 		SYS_munmap
 		SYS_mprotect
 		SYS_madvise
+		SYS_getpgrp
 		SYS_fcntl
 		SYS_setpriority
 		SYS_socket

 		SYS_psynch_rw_unlock
 		SYS_psynch_rw_unlock2
 		SYS_psynch_cvclrprepost
+		SYS_iopolicysys
 		SYS_process_policy
 		SYS_issetugid
 		SYS___pthread_kill

 
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
