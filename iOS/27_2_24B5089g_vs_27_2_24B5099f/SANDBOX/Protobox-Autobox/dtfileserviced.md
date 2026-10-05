## dtfileserviced

> Group: ⬆️ Updated

```diff

 		SYS_setattrlist
 		SYS_fgetattrlist
 		SYS_fsetattrlist
+		SYS_poll
 		SYS_getxattr
 		SYS_fgetxattr
 		SYS_setxattr

 		SYS_sendto_nocancel
 		SYS_pread_nocancel
 		SYS_pwrite_nocancel
+		SYS_poll_nocancel
 		SYS___sigwait_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath

 		SYS_pwritev_nocancel
 		SYS_ulock_wait2
 		SYS_proc_info_extended_id
-		SYS_map_with_linking_np)
+		SYS_map_with_linking_np
+		SYS_mkfifoat)
 )
 
 (deny syscall-mach)
```
