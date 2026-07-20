## SUCoreHelperService

> Group: ⬆️ Updated

```diff

 
 (deny generic-issue-extension)
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 	)
 )
 
+(deny iokit-open-user-client)
+
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny job-creation)
+(allow ipc-sysv-shm)
+
+(deny isp-command-send)
+
+(deny mach-host-special-port-set)
 
 (deny mach-issue-extension)
 
-(deny mach-lookup)
+(deny process-codesigning)
 
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
+(deny socket-ioctl)
+
+(deny syscall-unix
+	(require-all
+		(require-not (syscall-number
+			SYS_exit
+			SYS_read
+			SYS_open
+			SYS_getfsstat
+			SYS_getpid
+			SYS_getuid
+			SYS_geteuid
+			SYS_sendmsg
+			SYS_crossarch_trap
+			SYS_dup
+			SYS_getegid
+			SYS_sigaction
+			SYS_getgid
+			SYS_sigprocmask
+			SYS_sigpending
+			SYS_sigaltstack
+			SYS_readlink
+			SYS_umask
+			SYS_mprotect
+			SYS_fcntl
+			SYS_fsync
+			SYS_sigsuspend
+			SYS_readv
+			SYS_sendto
+			SYS_mkdir
+			SYS_pread
+			SYS_kdebug_typefilter
+			SYS_kdebug_trace_string
+			SYS_kdebug_trace64
+			SYS_kdebug_trace
+			SYS_sigreturn
+			SYS_pathconf
+			SYS_lseek
+			SYS_sysctl
+			SYS_getumask
+			SYS_fsctl
+			SYS_sysctlbyname
+			SYS_gettid
+			SYS_mkdir_extended
+			SYS_shared_region_check_np
+			SYS_psynch_rw_longrdlock
+			SYS_psynch_rw_yieldwrlock
+			SYS_psynch_rw_downgrade
+			SYS_psynch_rw_upgrade
+			SYS_psynch_mutexwait
+			SYS_psynch_mutexdrop
+			SYS_psynch_rw_rdlock
+			SYS_psynch_rw_wrlock
+			SYS_psynch_rw_unlock
+			SYS_psynch_rw_unlock2
+			SYS_issetugid
+			SYS___pthread_kill
+			SYS___pthread_sigmask
+			SYS___sigwait
+			SYS___pthread_markcancel
+			SYS___pthread_canceled
+			SYS_proc_info
+			SYS_getdirentries64
+			SYS_getfsstat64
+			SYS___pthread_chdir
+			SYS___pthread_fchdir
+			SYS_thread_selfid
+			SYS___mac_syscall
+			SYS_read_nocancel
+			SYS_sendmsg_nocancel
+			SYS_fcntl_nocancel
+			SYS_sigsuspend_nocancel
+			SYS_readv_nocancel
+			SYS_sendto_nocancel
+			SYS_pread_nocancel
+			SYS___sigwait_nocancel
+			SYS_fsgetpath
+			SYS_memorystatus_control
+			SYS_guarded_open_np
+			SYS_openat
+			SYS_fstatat
+			SYS_fstatat64
+			SYS_mkdirat
+			SYS_persona
+			SYS_terminate_with_payload
+			SYS_abort_with_payload
+			SYS_os_fault_with_payload
+			SYS_memorystatus_available_memory
+			SYS_preadv
+			SYS_preadv_nocancel
+			SYS_map_with_linking_np))
+		(require-any
+			(require-all
+				(require-not (syscall-number
+					SYS_exit
+					SYS_getpid
+					SYS_getuid
+					SYS_geteuid
+					SYS_getegid
+					SYS_getgid
+					SYS_mprotect
+					SYS_kdebug_typefilter
+					SYS_kdebug_trace_string
+					SYS_kdebug_trace64
+					SYS_kdebug_trace
+					SYS_sysctl
+					SYS_getumask
+					SYS_sysctlbyname
+					SYS_gettid
+					SYS_issetugid
+					SYS_fsgetpath
+					SYS_abort_with_payload
+					SYS_os_fault_with_payload
+					SYS_memorystatus_available_memory))
+				(require-not (syscall-number
+					SYS_open
+					SYS_crossarch_trap
+					SYS_dup
+					SYS_umask
+					SYS_fcntl
+					SYS_pread
+					SYS_fsctl
+					SYS_shared_region_check_np
+					SYS_proc_info
+					SYS_thread_selfid
+					SYS___mac_syscall
+					SYS_fcntl_nocancel
+					SYS_pread_nocancel
+					SYS_memorystatus_control
+					SYS_openat
+					SYS_fstatat
+					SYS_fstatat64
+					SYS_terminate_with_payload))
+				(require-not (syscall-number SYS_getfsstat64))
+				(require-not (syscall-number SYS_map_with_linking_np))
+				(require-not (syscall-number SYS_getfsstat))
+			)
+			(syscall-number SYS_getrlimit)
+			(syscall-number SYS_setrlimit)
+		)
+	)
+)
+
+(deny syscall-mach)
+(allow syscall-mach
+	(machtrap-number
+		MSC__kernelrpc_mach_vm_allocate_trap
+		MSC__kernelrpc_mach_vm_purgable_control_trap
+		MSC__kernelrpc_mach_vm_deallocate_trap
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
+		MSC_swtch_pri
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
+		host_get_io_master
+		host_get_clock_service
+		host_get_special_port
+		clock_get_time
+		mach_exception_raise
+		mach_exception_raise_state
+		mach_exception_raise_state_identity
+		io_service_open_extended
+		io_server_version
+		io_service_get_matching_service_bin
+		io_registry_entry_get_property_bin_buf
+		mach_port_request_notification
+		mach_port_set_attributes
+		mach_port_get_context_from_user
+		mach_port_is_connection_for_service
+		task_info_from_user
+		task_get_special_port_from_user
+		task_set_special_port
+		semaphore_create
+		semaphore_destroy
+		task_set_exc_guard_behavior
+		vm_remap_external
+		vm_reallocate
+		mach_vm_copy
+		mach_vm_map_external
+		mach_vm_region_recurse
+		_mach_make_memory_entry
+		mach_vm_range_create
+		mach_vm_reallocate
+		mach_memory_entry_ownership
+		mach_voucher_attr_command
+		task_restartable_ranges_register
+		task_restartable_ranges_synchronize)
+)
+
 (deny sysctl*
 	(require-all
 		(sysctl-name "vm.debug_range_enabled")

 	)
 )
 
+(deny system-fcntl)
+(allow system-fcntl
+	(fcntl-command
+		F_GETFL
+		F_GETPATH
+		F_GETPROTECTIONCLASS
+		F_OFD_GETLK
+		F_ADDFILESIGS_RETURN
+		F_CHECK_LV)
+)
+
 (deny system-fsctl)
 (allow system-fsctl
 	(fsctl-command FSIOC_CAS_BSDFLAGS)

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
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
 (allow process-exec-update-label)
```
