## skateboardcompaniond

> Group: ⬆️ Updated

```diff

 
 (allow default)
 
-(deny file-ioctl
-	(process-attribute is-autoboxed)
-)
+(deny file-ioctl)
 (allow file-ioctl
-	(require-all
-		(process-attribute is-autoboxed)
-		(ioctl-command (_IO "h" 4))
+	(ioctl-command (_IO "h" 4))
+)
+
+(deny generic-issue-extension)
+
+(deny iokit-get-properties)
+
+(deny iokit-open*)
+(allow iokit-open*
+	(require-any
+		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
+		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 	)
 )
 
-(deny generic-issue-extension
-	(with no-report)
-	(process-attribute is-autoboxed)
-)
+(deny iokit-open-user-client)
 
-(deny iokit-issue-extension
-	(with no-report)
-	(process-attribute is-autoboxed)
-)
+(deny iokit-open-service)
 
-(deny iokit-open-user-client
-	(process-attribute is-autoboxed)
-)
-(allow iokit-open-user-client
-	(require-all
-		(process-attribute is-autoboxed)
-		(require-any
-			(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
-			(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
-		)
+(deny iokit-set-properties)
+
+(deny ipc*)
+
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
+	(require-any
+		(ipc-posix-name "apple.cfprefs.system.daemonv1")
+		(ipc-posix-name "apple.cfprefs.user.daemonv1")
+		(ipc-posix-name "apple.shm.notification_center")
 	)
 )
 
-(deny iokit-set-properties
-	(with no-report)
-	(process-attribute is-autoboxed)
-)
+(allow ipc-sysv-shm)
 
-(deny ipc*
-	(with no-report)
-	(process-attribute is-autoboxed)
-)
+(deny isp-command-send)
 
-(deny ipc-posix-shm-read-data
-	(process-attribute is-autoboxed)
-)
-(allow ipc-posix-shm-read-data
-	(require-all
-		(process-attribute is-autoboxed)
-		(require-any
-			(ipc-posix-name "apple.cfprefs.system.daemonv1")
-			(ipc-posix-name "apple.cfprefs.user.daemonv1")
-			(ipc-posix-name "apple.shm.notification_center")
-		)
-	)
-)
-
-(deny job-creation
-	(with no-report)
-	(process-attribute is-autoboxed)
-)
+(deny mach-host-special-port-set)
 
 (deny mach-issue-extension
-	(with no-report)
-	(process-attribute is-autoboxed)
-)
-
-(deny mach-lookup
 	(require-all
+		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.diagnosticd"))

 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.logd"))
-		(require-any
-			(process-attribute is-autoboxed)
-			(require-all
-				(system-attribute developer-mode)
-				(process-attribute is-autoboxed)
-				(require-not (global-name "com.apple.dt.testmanagerd.uiprocess"))
-			)
-		)
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (system-attribute developer-mode))
 	)
 )
 
-(deny process-exec*
-	(with no-report)
-	(process-attribute is-autoboxed)
+(deny process-codesigning)
+
+(deny process-exec*)
+
+(allow process-exec-interpreter)
+
+(deny socket-ioctl)
+(allow socket-ioctl
+	(ioctl-command
+		SIOCGCONNINFO
+		SIOCGIFAGENTDATA
+		SIOCGIFCONSTRAINED
+		SIOCGIFDELEGATE
+		SIOCGIFEXPENSIVE
+		SIOCGIFFLAGS
+		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
+		SIOCGIFMTU
+		SIOCGIFULTRACONSTRAINED)
+)
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
+		SYS_recvmsg
+		SYS_sendmsg
+		SYS_recvfrom
+		SYS_getsockname
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
+		SYS_fcntl
+		SYS_socket
+		SYS_connect
+		SYS_bind
+		SYS_setsockopt
+		SYS_sigsuspend
+		SYS_gettimeofday
+		SYS_getsockopt
+		SYS_readv
+		SYS_writev
+		SYS_sendto
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
+		SYS_getrlimit
+		SYS_setrlimit
+		SYS_mmap
+		SYS_lseek
+		SYS_sysctl
+		SYS_getumask
+		SYS_getattrlist
+		SYS_fsctl
+		SYS_shm_open
+		SYS_sysctlbyname
+		SYS_stat_extended
+		SYS_lstat_extended
+		SYS_fstat_extended
+		SYS_gettid
+		SYS_shared_region_check_np
+		SYS_psynch_rw_longrdlock
+		SYS_psynch_rw_yieldwrlock
+		SYS_psynch_rw_downgrade
+		SYS_psynch_rw_upgrade
+		SYS_psynch_mutexwait
+		SYS_psynch_mutexdrop
+		SYS_psynch_cvbroad
+		SYS_psynch_cvsignal
+		SYS_psynch_cvwait
+		SYS_psynch_rw_rdlock
+		SYS_psynch_rw_wrlock
+		SYS_psynch_rw_unlock
+		SYS_psynch_rw_unlock2
+		SYS_psynch_cvclrprepost
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
+		SYS_recvmsg_nocancel
+		SYS_sendmsg_nocancel
+		SYS_recvfrom_nocancel
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
+		SYS_memorystatus_control
+		SYS_guarded_close_np
+		SYS_change_fdguard_np
+		SYS_proc_rlimit_control
+		SYS_connectx
+		SYS_openat
+		SYS_fstatat
+		SYS_fstatat64
+		SYS_bsdthread_ctl
+		SYS_guarded_write_np
+		SYS_guarded_pwrite_np
+		SYS_guarded_writev_np
+		SYS_persona
+		SYS_getentropy
+		SYS_necp_open
+		SYS_necp_client_action
+		SYS___channel_open
+		SYS___channel_get_info
+		SYS___channel_sync
+		SYS___channel_get_opt
+		SYS___channel_set_opt
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
+		MSC__kernelrpc_mach_port_deallocate_trap
+		MSC__kernelrpc_mach_port_mod_refs_trap
+		MSC__kernelrpc_mach_port_insert_right_trap
+		MSC__kernelrpc_mach_port_construct_trap
+		MSC__kernelrpc_mach_port_destruct_trap
+		MSC_mach_reply_port
+		MSC_task_self_trap
+		MSC_host_self_trap
+		MSC_semaphore_signal_trap
+		MSC_semaphore_wait_trap
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
+(deny syscall-mig)
+(allow syscall-mig
+	(kernel-mig-routine
+		host_info
+		host_get_clock_service
+		host_get_special_port
+		clock_get_time
+		mach_exception_raise
+		mach_exception_raise_state
+		mach_exception_raise_state_identity
+		io_service_open_extended
+		mach_port_request_notification
+		mach_port_set_attributes
+		mach_port_get_context_from_user
+		mach_port_is_connection_for_service
+		task_info_from_user
+		task_get_special_port_from_user
+		task_set_special_port
+		semaphore_create
+		task_set_exc_guard_behavior
+		vm_remap_external
+		vm_reallocate
+		mach_vm_map_external
+		mach_vm_region_recurse
+		_mach_make_memory_entry
+		mach_vm_range_create
+		mach_vm_reallocate
+		mach_memory_entry_ownership
+		mach_voucher_attr_command
+		task_restartable_ranges_register
+		task_restartable_ranges_synchronize)
 )
 
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
+	(fcntl-command F_SETFD F_GETFL F_GETPATH F_ADDFILESIGS_RETURN F_CHECK_LV)
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
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 90 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(deny system-mac-syscall
+	(require-any
+		(require-not (mac-policy-name "Sandbox"))
+		(require-not (mac-syscall-number 2))
+	)
+)
+
+(deny system-memorystatus-control)
+(allow system-memorystatus-control
+	(memorystatus-control-command MEMORYSTATUS_CMD_INCREASE_JETSAM_TASK_LIMIT)
+)
+
+(deny system-necp-client-action)
+(allow system-necp-client-action
+	(necp-client-action
+		NECP_CLIENT_ACTION_ADD
+		NECP_CLIENT_ACTION_ADD_FLOW
+		NECP_CLIENT_ACTION_AGENT
+		NECP_CLIENT_ACTION_COPY_AGENT
+		NECP_CLIENT_ACTION_COPY_INTERFACE
+		NECP_CLIENT_ACTION_COPY_RESULT
+		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT_FINAL
+		NECP_CLIENT_ACTION_REMOVE
+		NECP_CLIENT_ACTION_REMOVE_FLOW)
+)
+
+(allow process-exec-update-label)
```
