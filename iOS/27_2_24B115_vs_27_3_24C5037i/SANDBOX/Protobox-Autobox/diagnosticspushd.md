## diagnosticspushd

> Group: ⬆️ Updated

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 

 		SYS_mprotect
 		SYS_madvise
 		SYS_fcntl
+		SYS_select
 		SYS_fsync
 		SYS_socket
 		SYS_connect

 		SYS_writev
 		SYS_rename
 		SYS_sendto
+		SYS_shutdown
 		SYS_mkdir
 		SYS_rmdir
 		SYS_pread

 		SYS_kevent_qos
 		SYS_kevent_id
 		SYS___mac_syscall
+		SYS_pselect
+		SYS_pselect_nocancel
 		SYS_read_nocancel
 		SYS_write_nocancel
 		SYS_open_nocancel

 		SYS_sendmsg_nocancel
 		SYS_recvfrom_nocancel
 		SYS_fcntl_nocancel
+		SYS_select_nocancel
 		SYS_fsync_nocancel
 		SYS_connect_nocancel
 		SYS_sigsuspend_nocancel

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_SETFD
 		F_GETFL
 		F_SETFL

 
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
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(with-filter (mac-policy-name "vnguard")
+	(deny system-mac-syscall
+		(require-not (mac-syscall-number 1))
 	)
 )
 (deny system-mac-syscall
```
