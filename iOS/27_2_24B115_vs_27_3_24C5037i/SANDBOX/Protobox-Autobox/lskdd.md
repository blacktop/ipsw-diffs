## lskdd

> Group: ⬆️ Updated

```diff

 		SYS_getumask
 		SYS_getattrlist
 		SYS_fsctl
+		SYS_posix_spawn
 		SYS_shm_open
 		SYS_sem_open
 		SYS_sem_close

 
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
