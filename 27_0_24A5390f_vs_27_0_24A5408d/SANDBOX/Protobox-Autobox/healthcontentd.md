## healthcontentd

> Group: ⬆️ Updated

```diff

 			SYS_kdebug_trace
 			SYS_sigreturn
 			SYS_pathconf
+			SYS_mmap
 			SYS_lseek
 			SYS_ftruncate
 			SYS_sysctl

 			SYS_guarded_kqueue_np
 			SYS_change_fdguard_np
 			SYS_openat
+			SYS_renameat
 			SYS_fstatat
 			SYS_fstatat64
 			SYS_mkdirat

 
 (deny system-fsctl)
 (allow system-fsctl
-	(fsctl-command APFSIOC_GET_CLONE_INFO FSIOC_CAS_BSDFLAGS)
+	(fsctl-command
+		APFSIOC_GET_CLONE_INFO
+		APFSIOC_GET_PURGEABLE_FILE_FLAGS
+		APFSIOC_PURGEABLE_GET_FILE_INFO
+		FSIOC_CAS_BSDFLAGS)
 )
 
 (deny system-kas-info)
```
