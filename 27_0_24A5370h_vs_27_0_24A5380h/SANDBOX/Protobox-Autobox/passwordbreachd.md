## passwordbreachd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.AutomaticSecurityUpgrade"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.AuthenticationServices.AutoFill"))
+		(require-not (global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.AutomaticSecurityUpgrade"))
+		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (system-attribute developer-mode))
 	)

 			SYS___pthread_kill
 			SYS___pthread_sigmask
 			SYS___sigwait
+			SYS___pthread_markcancel
+			SYS___pthread_canceled
 			SYS_proc_info
 			SYS_getdirentries64
 			SYS_getfsstat64
+			SYS___pthread_chdir
+			SYS___pthread_fchdir
 			SYS_thread_selfid
 			SYS___mac_syscall
 			SYS_pselect

 			SYS_map_with_linking_np))
 		(require-any
 			(require-all
-				(require-not (syscall-number SYS___pthread_kill))
 				(require-not (syscall-number
 					SYS_exit
 					SYS_getpid
```
