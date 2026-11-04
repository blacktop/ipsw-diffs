## installd

> Group: ⬆️ Updated

```diff

 		SYS_mkdir
 		SYS_rmdir
 		SYS_pread
+		SYS_pwrite
 		SYS_statfs
 		SYS_fstatfs
 		SYS_csops

 		SYS_kevent_id
 		SYS___mac_syscall
 		SYS_read_nocancel
+		SYS_write_nocancel
 		SYS_open_nocancel
 		SYS_sendmsg_nocancel
 		SYS_fcntl_nocancel
 		SYS_fsync_nocancel
 		SYS_sigsuspend_nocancel
 		SYS_readv_nocancel
+		SYS_writev_nocancel
 		SYS_sendto_nocancel
 		SYS_pread_nocancel
+		SYS_pwrite_nocancel
 		SYS___sigwait_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath

 		SYS_mkdirat
 		SYS_bsdthread_ctl
 		SYS_guarded_open_dprotected_np
+		SYS_guarded_write_np
+		SYS_guarded_pwrite_np
+		SYS_guarded_writev_np
 		SYS_renameatx_np
 		SYS_persona
 		SYS_getentropy

 		SYS_memorystatus_available_memory
 		SYS_objc_bp_assist_cfg_np
 		SYS_preadv
+		SYS_pwritev
 		SYS_preadv_nocancel
+		SYS_pwritev_nocancel
 		SYS_ulock_wait2
 		SYS_proc_info_extended_id
 		SYS_map_with_linking_np)

 
 (deny system-kas-info)
 
-(with-filter (mac-policy-name "Sandbox")
-	(deny system-mac-syscall
-		(require-all
-			(require-not (mac-syscall-number 80))
-			(require-not (mac-syscall-number 6))
-			(require-not (mac-syscall-number 4))
-			(require-not (mac-syscall-number 67))
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
