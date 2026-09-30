## ManagedAppsSubscriber

> Group: ⬆️ Updated

```diff

 		SYS_stat
 		SYS_fstat
 		SYS_lstat
+		SYS_pathconf
 		SYS_getrlimit
 		SYS_setrlimit
 		SYS_mmap

 	(deny system-mac-syscall
 		(require-all
 			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 67))
 			(require-not (mac-syscall-number 2))
 		)
```
