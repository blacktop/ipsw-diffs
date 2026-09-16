## sharereportingd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.cloudd"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		SYS_stat
 		SYS_fstat
 		SYS_lstat
+		SYS_pathconf
 		SYS_getrlimit
 		SYS_setrlimit
 		SYS_mmap

 		SYS_preadv_nocancel
 		SYS_pwritev_nocancel
 		SYS_ulock_wait2
+		SYS_proc_info_extended_id
 		SYS_map_with_linking_np)
 )
 
```
