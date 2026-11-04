## ServicesAccountLinkingService

> Group: ⬆️ Updated

```diff

 			SYS_psynch_rw_wrlock
 			SYS_psynch_rw_unlock
 			SYS_psynch_cvclrprepost
+			SYS_iopolicysys
 			SYS_issetugid
 			SYS___pthread_kill
 			SYS___pthread_sigmask

 			SYS_guarded_open_np
 			SYS_change_fdguard_np
 			SYS_openat
+			SYS_renameat
 			SYS_fstatat
 			SYS_fstatat64
 			SYS_mkdirat

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
 		(mac-syscall-number 1)
```
