## appmanagedfeaturesd

> Group: ⬆️ Updated

```diff

 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.ManagedSettingsAgent"))
 		(require-not (global-name "com.apple.managedconfiguration.teslad"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.mobileactivationd"))

 		(require-not (global-name "com.apple.dmd"))
 		(require-not (global-name "com.apple.adid"))
 		(require-not (global-name "com.apple.icloud.findmydeviced"))
-		(require-not (global-name "com.apple.ManagedSettingsAgent"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 			SYS_umask
 			SYS_mprotect
 			SYS_fcntl
+			SYS_select
 			SYS_fsync
 			SYS_sigsuspend
 			SYS_readv
 			SYS_writev
 			SYS_rename
 			SYS_sendto
+			SYS_shutdown
 			SYS_mkdir
 			SYS_rmdir
 			SYS_pread

 			SYS_psynch_rw_unlock
 			SYS_psynch_rw_unlock2
 			SYS_psynch_cvclrprepost
+			SYS_iopolicysys
 			SYS_issetugid
 			SYS___pthread_kill
 			SYS___pthread_sigmask

 			SYS___pthread_fchdir
 			SYS_thread_selfid
 			SYS___mac_syscall
+			SYS_pselect
+			SYS_pselect_nocancel
 			SYS_read_nocancel
 			SYS_write_nocancel
 			SYS_recvmsg_nocancel
 			SYS_sendmsg_nocancel
 			SYS_recvfrom_nocancel
 			SYS_fcntl_nocancel
+			SYS_select_nocancel
 			SYS_fsync_nocancel
 			SYS_sigsuspend_nocancel
 			SYS_readv_nocancel

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_GETFL
 		F_SETFL
 		F_GETPATH

 
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
