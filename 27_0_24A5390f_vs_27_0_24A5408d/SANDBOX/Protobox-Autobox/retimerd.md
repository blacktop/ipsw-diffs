## retimerd

> Group: ⬆️ Updated

```diff

 		SYS_select
 		SYS_fsync
 		SYS_socket
+		SYS_connect
 		SYS_getpriority
 		SYS_sigsuspend
 		SYS_gettimeofday

 		SYS_fcntl_nocancel
 		SYS_select_nocancel
 		SYS_fsync_nocancel
+		SYS_connect_nocancel
 		SYS_sigsuspend_nocancel
 		SYS_readv_nocancel
 		SYS_writev_nocancel

 			_mach_make_memory_entry
 			mach_vm_range_create
 			mach_vm_reallocate
+			mach_memory_entry_ownership
 			mach_voucher_attr_command
 			task_restartable_ranges_register
 			task_restartable_ranges_synchronize))

 
 (deny system-fcntl)
 (allow system-fcntl
-	(fcntl-command F_GETFL F_GETPATH F_ADDFILESIGS_RETURN F_CHECK_LV)
+	(fcntl-command F_SETFD F_GETFL F_GETPATH F_ADDFILESIGS_RETURN F_CHECK_LV)
 )
 
 (deny system-fsctl)
```
