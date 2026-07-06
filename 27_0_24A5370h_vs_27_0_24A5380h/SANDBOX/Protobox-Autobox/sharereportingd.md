## sharereportingd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (system-attribute developer-mode))
 	)

 		SYS_getpid
 		SYS_getuid
 		SYS_geteuid
+		SYS_sendmsg
 		SYS_access
 		SYS_crossarch_trap
 		SYS_dup

 		SYS_gettimeofday
 		SYS_readv
 		SYS_writev
+		SYS_sendto
 		SYS_pread
 		SYS_pwrite
 		SYS_statfs

 		SYS_read_nocancel
 		SYS_write_nocancel
 		SYS_close_nocancel
+		SYS_sendmsg_nocancel
 		SYS_fcntl_nocancel
 		SYS_fsync_nocancel
 		SYS_sigsuspend_nocancel
 		SYS_readv_nocancel
 		SYS_writev_nocancel
+		SYS_sendto_nocancel
 		SYS_pread_nocancel
 		SYS_pwrite_nocancel
 		SYS___sigwait_nocancel

 			_mach_make_memory_entry
 			mach_vm_range_create
 			mach_vm_reallocate
+			mach_memory_entry_ownership
 			mach_voucher_attr_command
 			task_restartable_ranges_register
 			task_restartable_ranges_synchronize))

 					mach_exception_raise_state_identity
 					mach_port_get_context_from_user))
 				(require-not (kernel-mig-routine mach_vm_range_create))
+				(require-not (kernel-mig-routine vm_remap_external))
 				(require-not (kernel-mig-routine task_restartable_ranges_register))
 				(require-not (kernel-mig-routine task_restartable_ranges_synchronize))
-				(require-not (kernel-mig-routine semaphore_create))
 				(require-not (kernel-mig-routine mach_vm_reallocate))
+				(require-not (kernel-mig-routine semaphore_create))
 				(require-not (kernel-mig-routine task_info_from_user))
-				(require-not (kernel-mig-routine vm_remap_external))
 				(require-not (kernel-mig-routine io_service_open_extended))
 				(require-not (kernel-mig-routine vm_reallocate))
 			)

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_SETFD
 		F_GETFL
 		F_GETPATH
 		F_GETPROTECTIONCLASS
```
