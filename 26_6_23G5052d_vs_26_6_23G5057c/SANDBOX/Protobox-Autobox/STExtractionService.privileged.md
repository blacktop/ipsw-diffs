## STExtractionService.privileged

> Group: ⬆️ Updated

```diff

 		SYS_sigprocmask
 		SYS_sigpending
 		SYS_sigaltstack
+		SYS_symlink
 		SYS_readlink
 		SYS_umask
 		SYS_mprotect

 		SYS_open_dprotected_np
 		SYS_openat_dprotected_np
 		SYS_fsetattrlist
+		SYS_flistxattr
 		SYS_fsctl
 		SYS_sysctlbyname
 		SYS_gettid

 		F_SETFL
 		F_NOCACHE
 		F_GETPATH
+		F_GETPROTECTIONCLASS
+		F_SETPROTECTIONCLASS
+		F_SINGLE_WRITER
 		F_ADDFILESIGS_RETURN
 		F_CHECK_LV
 		F_PUNCHHOLE
```
