## com.apple.CallKit.CallDirectory

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.ciphermld"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))

 		SYS_change_fdguard_np
 		SYS_proc_rlimit_control
 		SYS_openat
+		SYS_renameat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat
```
