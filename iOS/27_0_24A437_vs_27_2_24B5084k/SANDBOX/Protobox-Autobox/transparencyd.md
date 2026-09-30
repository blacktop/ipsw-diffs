## transparencyd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))

 		SYS_fgetxattr
 		SYS_setxattr
 		SYS_listxattr
+		SYS_flistxattr
 		SYS_fsctl
 		SYS_posix_spawn
 		SYS_shm_open

 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
+		F_SINGLE_WRITER
 		F_BARRIERFSYNC
 		F_OFD_SETLK
 		F_OFD_GETLK
```
