## coreidvd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.networkscored"))
+		(require-not (global-name "com.apple.passd.cloud-store"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))

 		SYS_fstat
 		SYS_lstat
 		SYS_pathconf
+		SYS_fpathconf
 		SYS_getrlimit
 		SYS_setrlimit
 		SYS_mmap

 		SYS_setxattr
 		SYS_fsetxattr
 		SYS_listxattr
+		SYS_flistxattr
 		SYS_fsctl
 		SYS_shm_open
 		SYS_sem_open

 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
 		F_DUPFD_CLOEXEC
+		F_SINGLE_WRITER
 		F_BARRIERFSYNC
 		F_OFD_SETLK
 		F_OFD_GETLK
```
