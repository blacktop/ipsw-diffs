## SeymourAppStoreService

> Group: ⬆️ Updated

```diff

 
 (deny generic-issue-extension)
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 	)
 )
 
+(deny iokit-open-user-client)
+
 (deny iokit-open-service)
 
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.symptom_diagnostics"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command

 			SYS_psynch_cvclrprepost
 			SYS_issetugid
 			SYS___pthread_kill
+			SYS___pthread_sigmask
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

 				(require-not (syscall-number SYS_map_with_linking_np))
 				(require-not (syscall-number SYS_getfsstat))
 			)
-			(syscall-number SYS___pthread_sigmask)
 			(syscall-number SYS_getrlimit)
 			(syscall-number SYS_setrlimit)
 		)
```
