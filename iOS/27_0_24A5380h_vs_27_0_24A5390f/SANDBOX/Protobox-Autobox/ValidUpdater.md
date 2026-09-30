## ValidUpdater

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
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "/com.apple.trustd.metrics")
 		(ipc-posix-name "apple.cfprefs.daemonv1")

 	)
 )
 
-(deny ipc-posix-shm-write-create)
-(allow ipc-posix-shm-write-create
+(deny ipc-posix-shm-write*)
+(allow ipc-posix-shm-write*
 	(require-any
 		(ipc-posix-name "/com.apple.trustd.metrics")
 		(ipc-posix-name "com.apple.trustd.metrics")
 	)
 )
 
-(deny ipc-posix-shm-write-data)
-(allow ipc-posix-shm-write-data
-	(require-any
-		(ipc-posix-name "/com.apple.trustd.metrics")
-		(ipc-posix-name "com.apple.trustd.metrics")
-	)
-)
+(allow ipc-sysv-shm)
 
-(deny job-creation)
+(deny isp-command-send)
 
-(deny mach-issue-extension)
+(deny mach-host-special-port-set)
 
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.duetactivityscheduler"))

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

 			SYS_clonefileat
 			SYS_openat
 			SYS_openat_nocancel
+			SYS_renameat
 			SYS_fstatat
 			SYS_fstatat64
+			SYS_unlinkat
 			SYS_mkdirat
 			SYS_bsdthread_ctl
 			SYS_guarded_open_dprotected_np
```
