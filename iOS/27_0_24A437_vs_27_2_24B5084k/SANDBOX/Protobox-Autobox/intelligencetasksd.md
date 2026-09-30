## intelligencetasksd

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.linkd.registry"))
+		(require-not (global-name "com.apple.biome.compute.source"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.userprofiles"))
 		(require-not (global-name "com.apple.uservault"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
+		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (global-name "com.apple.spotlight.SearchAgent"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 			SYS_exit
 			SYS_read
 			SYS_open
+			SYS_close
 			SYS_getfsstat
 			SYS_getpid
 			SYS_getuid

 			SYS_sigaltstack
 			SYS_readlink
 			SYS_umask
+			SYS_munmap
 			SYS_mprotect
 			SYS_fcntl
 			SYS_sigsuspend
 			SYS_readv
+			SYS_flock
 			SYS_sendto
 			SYS_mkdir
 			SYS_pread

 			SYS_sigreturn
 			SYS_pathconf
 			SYS_lseek
+			SYS_ftruncate
 			SYS_sysctl
 			SYS_getumask
 			SYS_fsctl

 			SYS_pread_nocancel
 			SYS___sigwait_nocancel
 			SYS_fsgetpath
+			SYS_fileport_makeport
+			SYS_fileport_makefd
 			SYS_memorystatus_control
 			SYS_guarded_open_np
 			SYS_openat

 		MSC_task_dyld_process_info_notify_get
 		MSC__kernelrpc_mach_vm_protect_trap
 		MSC__kernelrpc_mach_vm_map_trap
+		MSC__kernelrpc_mach_port_allocate_trap
 		MSC__kernelrpc_mach_port_deallocate_trap
 		MSC__kernelrpc_mach_port_mod_refs_trap
 		MSC__kernelrpc_mach_port_insert_right_trap
+		MSC__kernelrpc_mach_port_insert_member_trap
 		MSC__kernelrpc_mach_port_construct_trap
 		MSC__kernelrpc_mach_port_destruct_trap
 		MSC_mach_reply_port

 		MSC_host_create_mach_voucher_trap
 		MSC__kernelrpc_mach_port_type_trap
 		MSC__kernelrpc_mach_port_request_notification_trap
-		MSC_mach_timebase_info_trap)
+		MSC_mach_timebase_info_trap
+		MSC_mk_timer_create)
 )
 
 (deny syscall-mig)
 (allow syscall-mig
 	(kernel-mig-routine
 		host_info
+		host_get_io_master
 		host_get_clock_service
 		host_request_notification
 		host_get_special_port

 		mach_exception_raise
 		mach_exception_raise_state
 		mach_exception_raise_state_identity
+		io_registry_entry_from_path
+		io_service_close
 		io_service_open_extended
+		io_connect_method
+		io_service_add_interest_notification_64
+		io_service_get_matching_service
+		io_server_version
+		io_service_get_matching_service_bin
+		mach_port_get_refs
 		mach_port_request_notification
 		mach_port_set_attributes
 		mach_port_get_context_from_user

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_GETFL
 		F_GETPATH
 		F_GETPROTECTIONCLASS
+		F_SETPROTECTIONCLASS
+		F_DUPFD_CLOEXEC
 		F_OFD_GETLK
 		F_OFD_SETLKWTIMEOUT
 		F_ADDFILESIGS_RETURN
```
