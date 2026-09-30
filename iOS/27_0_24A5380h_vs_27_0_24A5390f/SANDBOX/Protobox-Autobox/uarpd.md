## uarpd

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
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.TapToRadarKit.service"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.corespeech.corespeechservices"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (xpc-service-name "com.apple.corespeech.xpc"))
-		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.FileCoordination"))
+		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (system-attribute developer-mode))
 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command CTLIOCGINFO SIOCGCONNINFO)

 			SYS_exit
 			SYS_read
 			SYS_open
+			SYS_close
 			SYS_fchdir
 			SYS_getfsstat
 			SYS_getpid

 			SYS_symlink
 			SYS_readlink
 			SYS_umask
+			SYS_munmap
 			SYS_mprotect
 			SYS_dup2
 			SYS_fcntl

 			SYS_guarded_kqueue_np
 			SYS_change_fdguard_np
 			SYS_openat
+			SYS_renameat
 			SYS_faccessat
 			SYS_fstatat
 			SYS_fstatat64
```
