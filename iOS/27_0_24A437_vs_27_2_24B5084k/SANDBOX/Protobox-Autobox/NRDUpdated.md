## NRDUpdated

> Group: ⬆️ Updated

```diff

 		SYS_getpeername
 		SYS_getsockname
 		SYS_access
+		SYS_chflags
+		SYS_fchflags
 		SYS_kill
 		SYS_crossarch_trap
 		SYS_getppid

 		SYS_getsockopt
 		SYS_readv
 		SYS_writev
+		SYS_fchown
 		SYS_fchmod
 		SYS_rename
 		SYS_flock

 		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_fgetattrlist
+		SYS_fsetattrlist
 		SYS_getxattr
+		SYS_fgetxattr
 		SYS_setxattr
 		SYS_listxattr
+		SYS_flistxattr
 		SYS_fsctl
+		SYS_ffsctl
 		SYS_shm_open
 		SYS_shm_unlink
 		SYS_sem_open

 		SYS_stat_extended
 		SYS_lstat_extended
 		SYS_fstat_extended
+		SYS_fchmod_extended
 		SYS_gettid
 		SYS_mkdir_extended
 		SYS_shared_region_check_np

 		SYS_proc_rlimit_control
 		SYS_connectx
 		SYS_getattrlistbulk
+		SYS_clonefileat
 		SYS_openat
 		SYS_openat_nocancel
 		SYS_renameat

 		F_GETFL
 		F_SETFL
 		F_SETLKW
+		F_PREALLOCATE
+		F_NOCACHE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
 		F_DUPFD_CLOEXEC
 		F_SETNOSIGPIPE
 		F_GETNOSIGPIPE
+		F_SINGLE_WRITER
 		F_BARRIERFSYNC
 		F_OFD_SETLK
 		F_OFD_GETLK
```
