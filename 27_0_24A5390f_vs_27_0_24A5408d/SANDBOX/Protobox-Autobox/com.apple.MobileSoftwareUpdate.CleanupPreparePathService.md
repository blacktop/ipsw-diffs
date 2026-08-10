## com.apple.MobileSoftwareUpdate.CleanupPreparePathService

> Group: ⬆️ Updated

```diff

 		SYS_sysctl
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_setattrlist
 		SYS_fgetattrlist

 		SYS_unlinkat
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
```
