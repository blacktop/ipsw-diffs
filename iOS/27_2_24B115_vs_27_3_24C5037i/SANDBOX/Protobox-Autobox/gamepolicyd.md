## gamepolicyd

> Group: ⬆️ Updated

```diff

 		SYS_setrlimit
 		SYS_mmap
 		SYS_lseek
+		SYS_ftruncate
 		SYS_sysctl
 		SYS_getumask
 		SYS_getattrlist

 
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
