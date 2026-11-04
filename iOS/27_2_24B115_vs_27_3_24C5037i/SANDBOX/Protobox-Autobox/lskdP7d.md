## lskdP7d

> Group: ⬆️ Updated

```diff

 		SYS_setrlimit
 		SYS_mmap
 		SYS_lseek
+		SYS_ftruncate
 		SYS_sysctl
 		SYS_getumask
 		SYS_getattrlist

 	(fcntl-command
 		F_SETFD
 		F_GETFL
+		F_SETLKW
 		F_GETPATH
 		F_SETPROTECTIONCLASS
 		F_DUPFD_CLOEXEC

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
```
