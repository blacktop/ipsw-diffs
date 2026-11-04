## analyticsagent

> Group: ⬆️ Updated

```diff

 			SYS_mprotect
 			SYS_dup2
 			SYS_fcntl
+			SYS_fsync
 			SYS_sigsuspend
 			SYS_readv
 			SYS_sendto
 			SYS_mkdir
+			SYS_rmdir
 			SYS_pread
 			SYS_kdebug_typefilter
 			SYS_kdebug_trace_string

 			SYS_lseek
 			SYS_sysctl
 			SYS_getumask
+			SYS_open_dprotected_np
+			SYS_openat_dprotected_np
 			SYS_fgetattrlist
+			SYS_listxattr
 			SYS_fsctl
 			SYS_sysctlbyname
 			SYS_gettid

 			SYS_psynch_rw_unlock
 			SYS_psynch_rw_unlock2
 			SYS_psynch_cvclrprepost
+			SYS_iopolicysys
 			SYS_issetugid
 			SYS___pthread_kill
 			SYS___pthread_sigmask

 			SYS_read_nocancel
 			SYS_sendmsg_nocancel
 			SYS_fcntl_nocancel
+			SYS_fsync_nocancel
 			SYS_sigsuspend_nocancel
 			SYS_readv_nocancel
 			SYS_sendto_nocancel

 			SYS_memorystatus_control
 			SYS_guarded_kqueue_np
 			SYS_openat
+			SYS_renameat
 			SYS_fstatat
 			SYS_fstatat64
 			SYS_mkdirat
+			SYS_guarded_open_dprotected_np
 			SYS_persona
 			SYS_terminate_with_payload
 			SYS_abort_with_payload

 		F_GETFD
 		F_SETFD
 		F_GETFL
+		F_NOCACHE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS

 
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
