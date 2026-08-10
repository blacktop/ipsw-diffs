## com.apple.photos.PCCService

> Group: ⬆️ Updated

```diff

 
 (allow default)
 
-(deny file-ioctl
-	(with no-report)
-	(process-attribute is-autoboxed)
-)
+(deny file-ioctl)
 
-(deny generic-issue-extension
-	(with no-report)
-	(process-attribute is-autoboxed)
-)
+(deny generic-issue-extension)
 
-(deny iokit-issue-extension
-	(with no-report)
-	(process-attribute is-autoboxed)
-)
+(deny iokit-issue-extension)
 
-(deny iokit-open-user-client
-	(process-attribute is-autoboxed)
-)
+(deny iokit-open-user-client)
 (allow iokit-open-user-client
-	(require-all
-		(process-attribute is-autoboxed)
-		(require-any
-			(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
-			(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
-			(iokit-registry-entry-class "AppleKeyStoreUserClient")
-		)
+	(require-any
+		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
+		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 	)
 )
 
-(deny iokit-set-properties
-	(with no-report)
-	(process-attribute is-autoboxed)
+(deny iokit-open-service)
+(allow iokit-open-service
+	(iokit-registry-entry-class "AppleKeyStore")
 )
 
-(deny ipc*
-	(with no-report)
-	(process-attribute is-autoboxed)
-)
+(deny iokit-set-properties)
 
-(deny ipc-posix-shm-read-data
-	(process-attribute is-autoboxed)
-)
+(deny ipc*)
+
+(deny ipc-posix-shm-read-data)
 (allow ipc-posix-shm-read-data
-	(require-all
-		(process-attribute is-autoboxed)
-		(require-any
-			(ipc-posix-name "apple.cfprefs.system.daemonv1")
-			(ipc-posix-name "apple.cfprefs.user.daemonv1")
-			(ipc-posix-name "apple.shm.notification_center")
-		)
+	(require-any
+		(ipc-posix-name "apple.cfprefs.system.daemonv1")
+		(ipc-posix-name "apple.cfprefs.user.daemonv1")
+		(ipc-posix-name "apple.shm.notification_center")
 	)
 )
 
-(deny job-creation
-	(with no-report)
-	(process-attribute is-autoboxed)
-)
+(deny job-creation)
 
-(deny mach-issue-extension
-	(with no-report)
-	(process-attribute is-autoboxed)
-)
+(deny mach-issue-extension)
 
 (deny mach-lookup
 	(require-all
+		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.biome.access.system"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.TapToRadarKit.service"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.privatecloudcompute"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))

 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.TapToRadarKit.service"))
+		(require-not (system-attribute developer-mode))
+	)
+)
+
+(deny process-exec*)
+
+(deny socket-ioctl)
+
+(deny syscall-unix)
+(allow syscall-unix
+	(syscall-number
+		SYS_exit
+		SYS_read
+		SYS_write
+		SYS_open
+		SYS_close
+		SYS_getfsstat
+		SYS_getpid
+		SYS_getuid
+		SYS_geteuid
+		SYS_sendmsg
+		SYS_access
+		SYS_crossarch_trap
+		SYS_dup
+		SYS_getegid
+		SYS_sigaction
+		SYS_getgid
+		SYS_sigprocmask
+		SYS_sigpending
+		SYS_sigaltstack
+		SYS_ioctl
+		SYS_readlink
+		SYS_umask
+		SYS_munmap
+		SYS_mprotect
+		SYS_madvise
+		SYS_dup2
+		SYS_fcntl
+		SYS_socket
+		SYS_connect
+		SYS_sigsuspend
+		SYS_gettimeofday
+		SYS_readv
+		SYS_writev
+		SYS_fchmod
+		SYS_rename
+		SYS_flock
+		SYS_sendto
+		SYS_mkdir
+		SYS_pread
+		SYS_pwrite
+		SYS_statfs
+		SYS_fstatfs
+		SYS_csops
+		SYS_csops_audittoken
+		SYS_kdebug_typefilter
+		SYS_kdebug_trace_string
+		SYS_kdebug_trace64
+		SYS_kdebug_trace
+		SYS_sigreturn
+		SYS_stat
+		SYS_fstat
+		SYS_lstat
+		SYS_pathconf
+		SYS_getrlimit
+		SYS_setrlimit
+		SYS_mmap
+		SYS_lseek
+		SYS_ftruncate
+		SYS_sysctl
+		SYS_getumask
+		SYS_getattrlist
+		SYS_getxattr
+		SYS_listxattr
+		SYS_fsctl
+		SYS_shm_open
+		SYS_sysctlbyname
+		SYS_stat_extended
+		SYS_lstat_extended
+		SYS_fstat_extended
+		SYS_gettid
+		SYS_mkdir_extended
+		SYS_shared_region_check_np
+		SYS_psynch_rw_longrdlock
+		SYS_psynch_rw_yieldwrlock
+		SYS_psynch_rw_downgrade
+		SYS_psynch_rw_upgrade
+		SYS_psynch_mutexwait
+		SYS_psynch_mutexdrop
+		SYS_psynch_rw_rdlock
+		SYS_psynch_rw_wrlock
+		SYS_psynch_rw_unlock
+		SYS_psynch_rw_unlock2
+		SYS_issetugid
+		SYS___pthread_kill
+		SYS___pthread_sigmask
+		SYS___sigwait
+		SYS___disable_threadsignal
+		SYS___pthread_markcancel
+		SYS___pthread_canceled
+		SYS___semwait_signal
+		SYS_proc_info
+		SYS_stat64
+		SYS_fstat64
+		SYS_lstat64
+		SYS_stat64_extended
+		SYS_lstat64_extended
+		SYS_fstat64_extended
+		SYS_getdirentries64
+		SYS_statfs64
+		SYS_fstatfs64
+		SYS_getfsstat64
+		SYS___pthread_chdir
+		SYS___pthread_fchdir
+		SYS_bsdthread_create
+		SYS_bsdthread_terminate
+		SYS_kevent
+		SYS_bsdthread_register
+		SYS_workq_open
+		SYS_workq_kernreturn
+		SYS_kevent64
+		SYS_thread_selfid
+		SYS_kevent_qos
+		SYS_kevent_id
+		SYS___mac_syscall
+		SYS_read_nocancel
+		SYS_write_nocancel
+		SYS_open_nocancel
+		SYS_close_nocancel
+		SYS_sendmsg_nocancel
+		SYS_fcntl_nocancel
+		SYS_connect_nocancel
+		SYS_sigsuspend_nocancel
+		SYS_readv_nocancel
+		SYS_writev_nocancel
+		SYS_sendto_nocancel
+		SYS_pread_nocancel
+		SYS_pwrite_nocancel
+		SYS___sigwait_nocancel
+		SYS___semwait_signal_nocancel
+		SYS_fsgetpath
+		SYS_fileport_makeport
+		SYS_fileport_makefd
+		SYS_memorystatus_control
+		SYS_guarded_close_np
+		SYS_proc_rlimit_control
+		SYS_clonefileat
+		SYS_openat
+		SYS_faccessat
+		SYS_fstatat
+		SYS_fstatat64
+		SYS_mkdirat
+		SYS_bsdthread_ctl
+		SYS_guarded_write_np
+		SYS_guarded_pwrite_np
+		SYS_guarded_writev_np
+		SYS_persona
+		SYS_getentropy
+		SYS_ulock_wait
+		SYS_ulock_wake
+		SYS_terminate_with_payload
+		SYS_abort_with_payload
+		SYS_os_fault_with_payload
+		SYS_memorystatus_available_memory
+		SYS_preadv
+		SYS_pwritev
+		SYS_preadv_nocancel
+		SYS_pwritev_nocancel
+		SYS_ulock_wait2
+		SYS_map_with_linking_np)
+)
+
+(deny syscall-mach)
+(allow syscall-mach
+	(machtrap-number
+		MSC__kernelrpc_mach_vm_allocate_trap
+		MSC__kernelrpc_mach_vm_deallocate_trap
+		MSC_task_dyld_process_info_notify_get
+		MSC__kernelrpc_mach_vm_protect_trap
+		MSC__kernelrpc_mach_vm_map_trap
+		MSC__kernelrpc_mach_port_allocate_trap
+		MSC__kernelrpc_mach_port_deallocate_trap
+		MSC__kernelrpc_mach_port_mod_refs_trap
+		MSC__kernelrpc_mach_port_insert_right_trap
+		MSC__kernelrpc_mach_port_construct_trap
+		MSC__kernelrpc_mach_port_destruct_trap
+		MSC_mach_reply_port
+		MSC_thread_self_trap
+		MSC_task_self_trap
+		MSC_host_self_trap
+		MSC_semaphore_signal_trap
+		MSC_semaphore_wait_trap
+		MSC_semaphore_timedwait_trap
+		MSC__kernelrpc_mach_port_guard_trap
+		MSC_mach_generate_activity_id
+		MSC_mach_msg2_trap
+		MSC_thread_get_special_reply_port
+		MSC_syscall_thread_switch
+		MSC_host_create_mach_voucher_trap
+		MSC__kernelrpc_mach_port_type_trap
+		MSC__kernelrpc_mach_port_request_notification_trap
+		MSC_mach_timebase_info_trap)
+)
+
+(deny syscall-mig
+	(require-all
+		(require-not (kernel-mig-routine
+			host_info
+			host_get_io_master
+			host_get_clock_service
+			host_get_special_port
+			clock_get_time
+			mach_exception_raise
+			mach_exception_raise_state
+			mach_exception_raise_state_identity
+			io_registry_entry_from_path
+			io_service_open_extended
+			io_connect_method
+			io_service_add_interest_notification_64
+			io_server_version
+			io_service_get_matching_service_bin
+			mach_port_deallocate
+			mach_port_get_refs
+			mach_port_request_notification
+			mach_port_set_attributes
+			mach_port_get_context_from_user
+			mach_port_is_connection_for_service
+			task_threads_from_user
+			mach_ports_lookup
+			task_info_from_user
+			task_get_special_port_from_user
+			task_set_special_port
+			semaphore_create
+			thread_terminate
+			thread_suspend
+			thread_resume
+			thread_policy_set
+			vm_remap_external
+			vm_reallocate
+			mach_vm_copy
+			mach_vm_map_external
+			mach_vm_remap_external
+			mach_vm_region
+			_mach_make_memory_entry
+			mach_vm_page_range_query
+			mach_vm_range_create
+			mach_vm_reallocate
+			mach_memory_entry_ownership
+			mach_voucher_attr_command
+			task_restartable_ranges_register
+			task_restartable_ranges_synchronize))
 		(require-any
-			(process-attribute is-autoboxed)
+			(kernel-mig-routine mach_vm_region_recurse)
+			(kernel-mig-routine task_set_exc_guard_behavior)
 			(require-all
-				(system-attribute developer-mode)
-				(process-attribute is-autoboxed)
-				(require-not (global-name "com.apple.dt.testmanagerd.uiprocess"))
+				(require-not (kernel-mig-routine
+					host_info
+					host_get_clock_service
+					mach_exception_raise
+					mach_exception_raise_state
+					mach_exception_raise_state_identity
+					mach_port_get_context_from_user))
+				(require-not (kernel-mig-routine mach_vm_range_create))
+				(require-not (kernel-mig-routine vm_remap_external))
+				(require-not (kernel-mig-routine task_restartable_ranges_register))
+				(require-not (kernel-mig-routine task_restartable_ranges_synchronize))
+				(require-not (kernel-mig-routine mach_vm_reallocate))
+				(require-not (kernel-mig-routine semaphore_create))
+				(require-not (kernel-mig-routine task_info_from_user))
+				(require-not (kernel-mig-routine io_service_open_extended))
+				(require-not (kernel-mig-routine vm_reallocate))
 			)
 		)
 	)
 )
 
-(deny process-exec*
-	(with no-report)
-	(process-attribute is-autoboxed)
-)
-
 (deny sysctl*
 	(require-all
-		(process-attribute is-autoboxed)
 		(sysctl-name "vm.debug_range_enabled")
 		(require-not (sysctl-name "kern.wq_limit_cooperative_threads"))
 		(require-not (system-attribute developer-mode))
 	)
 )
 
-(deny system-fsctl
-	(process-attribute is-autoboxed)
+(deny system-fcntl)
+(allow system-fcntl
+	(fcntl-command
+		F_GETFD
+		F_SETFD
+		F_GETFL
+		F_GETPATH
+		F_GETPROTECTIONCLASS
+		F_DUPFD_CLOEXEC
+		F_ADDFILESIGS_RETURN
+		F_CHECK_LV)
 )
+
+(deny system-fsctl)
 (allow system-fsctl
-	(require-all
-		(process-attribute is-autoboxed)
-		(fsctl-command FSIOC_CAS_BSDFLAGS)
-	)
+	(fsctl-command FSIOC_CAS_BSDFLAGS)
 )
 
 (deny system-kas-info)
+
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
+(deny system-mac-syscall
+	(require-any
+		(require-not (mac-policy-name "AMFI"))
+		(require-not (mac-syscall-number 90))
+	)
+)
+
+(deny system-memorystatus-control)
+(allow system-memorystatus-control
+	(memorystatus-control-command MEMORYSTATUS_CMD_INCREASE_JETSAM_TASK_LIMIT)
+)
+
+(deny system-necp-client-action)
+
+(allow process-exec-update-label)
```
