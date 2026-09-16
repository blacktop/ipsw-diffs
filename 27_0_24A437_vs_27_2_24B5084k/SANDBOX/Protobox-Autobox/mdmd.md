## mdmd

> Group: ⬆️ Updated

```diff

 
 (deny ipc-posix-sem-open)
 (allow ipc-posix-sem-open
-	(ipc-posix-name "purplebuddy.sentinel")
+	(require-any
+		(ipc-posix-name "dmc_isCurrentUserConfigured")
+		(ipc-posix-name "purplebuddy.sentinel")
+	)
 )
 
 (deny ipc-posix-shm-read-data)

 		SYS_sysctl
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_setattrlist
 		SYS_fgetattrlist

 		SYS_clonefileat
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
