## ResolverService

> Group: ⬆️ Updated

```diff

 			SYS_exit
 			SYS_read
 			SYS_open
+			SYS_close
 			SYS_getfsstat
 			SYS_getpid
 			SYS_getuid

 			SYS_sigaltstack
 			SYS_readlink
 			SYS_umask
+			SYS_munmap
 			SYS_mprotect
 			SYS_dup2
 			SYS_fcntl

 
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
