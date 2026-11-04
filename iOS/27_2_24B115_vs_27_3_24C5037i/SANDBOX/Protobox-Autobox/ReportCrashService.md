## ReportCrashService

> Group: ⬆️ Updated

```diff

 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
 		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
 	)
 )
 

 		SYS_shutdown
 		SYS_socketpair
 		SYS_mkdir
+		SYS_rmdir
 		SYS_pread
 		SYS_pwrite
 		SYS_statfs

 		SYS_fstatat64
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_csrctl
 		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np

 		mach_vm_remap_new_external
 		mach_vm_deferred_reclamation_buffer_flush
 		mach_vm_range_create
+		mach_vm_deferred_reclamation_buffer_query
 		mach_vm_reallocate
 		mach_memory_entry_ownership
 		mach_voucher_extract_all_attr_recipes

 		F_SETFD
 		F_GETFL
 		F_SETFL
+		F_RDADVISE
 		F_NOCACHE
 		F_GETPATH
 		F_GETPROTECTIONCLASS

 
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
