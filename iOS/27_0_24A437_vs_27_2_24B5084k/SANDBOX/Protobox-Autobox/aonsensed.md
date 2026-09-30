## aonsensed

> Group: ⬆️ Updated

```diff

 		(require-not (xpc-service-name "com.apple.aonsensed.camera-xpc"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.AppleDeviceQueryService"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (system-attribute developer-mode))
 	)

 		SYS_fsync
 		SYS_socket
 		SYS_connect
+		SYS_getpriority
 		SYS_bind
 		SYS_setsockopt
 		SYS_sigsuspend

 		SYS___sigwait_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
+		SYS_fileport_makeport
 		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_open_np

 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
