## Photos

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
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.gamed"))
 		(require-not (global-name "com.apple.linkd.registry"))
+		(require-not (global-name "com.apple.itunescloud.music-subscription-status-service"))
 		(require-not (global-name "com.apple.healthd.server"))
 		(require-not (global-name "com.apple.systemstatus"))
 		(require-not (global-name "com.apple.contacts.donation.agent"))

 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
 		(require-not (global-name "com.apple.passd.in-app-payment"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (xpc-service-name "com.apple.CloudSharing.SPIHelper-iOS"))
+		(require-not (require-any
+			(xpc-service-name "com.google.keyboard.KeyboardExtension")
+			(xpc-service-name "com.sogou.sogouinput.basekeyboard")
+			(xpc-service-name "com.tencent.wetype.keyboard")
+		))
 		(require-not (global-name "com.apple.siri.analytics.assistant"))
 		(require-not (global-name "com.apple.visualintelligence.visual-action-prediction"))
 		(require-not (global-name "com.apple.asktod"))
 		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.sharingd.pairedcontactmanager"))
+		(require-not (local-name "com.apple.accessibility.gax.client"))
 		(require-not (require-any
 			(xpc-service-name "com.clusterdev.malayalam.keyboard")
 			(xpc-service-name "com.evoafuture.bettertalk.keyboard")

 			(xpc-service-name "com.willowvoice.ios.keyboard")
 		))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
+		(require-not (xpc-service-name "com.apple.CloudSharing.SPIHelper-iOS"))
 		(require-not (xpc-service-name "com.swiftkey.SwiftKeyApp.Keyboard"))
-		(require-not (require-any
-			(xpc-service-name "com.google.keyboard.KeyboardExtension")
-			(xpc-service-name "com.sogou.sogouinput.basekeyboard")
-			(xpc-service-name "com.tencent.wetype.keyboard")
-		))
 		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
 		(require-not (xpc-service-name "com.bytedance.ios.doubaoime.keyboardExtension"))
 		(require-not (system-attribute developer-mode))
 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
+(deny socket-ioctl)
+(allow socket-ioctl
+	(ioctl-command
+		CTLIOCGINFO
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
+(deny syscall-unix
+	(require-all
+		(require-not (syscall-number
+			SYS_exit
+			SYS_read
+			SYS_write
+			SYS_open
+			SYS_fchdir
+			SYS_getfsstat
+			SYS_getpid
+			SYS_getuid
+			SYS_geteuid
+			SYS_recvmsg
+			SYS_sendmsg
+			SYS_recvfrom
+			SYS_getsockname
+			SYS_crossarch_trap
+			SYS_dup
+			SYS_pipe
+			SYS_getegid
+			SYS_sigaction
+			SYS_getgid
+			SYS_sigprocmask
+			SYS_sigpending
+			SYS_sigaltstack
+			SYS_symlink
+			SYS_readlink
+			SYS_umask
+			SYS_msync
+			SYS_mprotect
+			SYS_mincore
+			SYS_getgroups
+			SYS_dup2
+			SYS_fcntl
+			SYS_select
+			SYS_listen
+			SYS_sigsuspend
+			SYS_getrusage
+			SYS_readv
+			SYS_writev
+			SYS_rename
+			SYS_sendto
+			SYS_shutdown
+			SYS_socketpair
+			SYS_mkdir
+			SYS_rmdir
+			SYS_gethostuuid
+			SYS_pread
+			SYS_pwrite
+			SYS_kdebug_typefilter
+			SYS_kdebug_trace_string
+			SYS_kdebug_trace64
+			SYS_kdebug_trace
+			SYS_sigreturn
+			SYS_thread_selfcounts
+			SYS_pathconf
+			SYS_fpathconf
+			SYS_lseek
+			SYS_sysctl
+			SYS_mlock
+			SYS_munlock
+			SYS_getumask
+			SYS_open_dprotected_np
+			SYS_openat_dprotected_np
+			SYS_setattrlist
+			SYS_fgetattrlist
+			SYS_fsetattrlist
+			SYS_fgetxattr
+			SYS_listxattr
+			SYS_flistxattr
+			SYS_fsctl
+			SYS_sysctlbyname
+			SYS_access_extended
+			SYS_gettid
+			SYS_mkdir_extended
+			SYS_shared_region_check_np
+			SYS_psynch_rw_longrdlock
+			SYS_psynch_rw_yieldwrlock
+			SYS_psynch_rw_downgrade
+			SYS_psynch_rw_upgrade
+			SYS_psynch_mutexwait
+			SYS_psynch_mutexdrop
+			SYS_psynch_cvbroad
+			SYS_psynch_cvsignal
+			SYS_psynch_cvwait
+			SYS_psynch_rw_rdlock
+			SYS_psynch_rw_wrlock
+			SYS_psynch_rw_unlock
+			SYS_psynch_rw_unlock2
+			SYS_psynch_cvclrprepost
+			SYS_iopolicysys
+			SYS_process_policy
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
+			SYS_kqueue
+			SYS_kevent
+			SYS_kevent64
+			SYS_thread_selfid
+			SYS_kevent_qos
+			SYS_kevent_id
+			SYS___mac_syscall
+			SYS_pselect
+			SYS_pselect_nocancel
+			SYS_read_nocancel
+			SYS_write_nocancel
+			SYS_recvmsg_nocancel
+			SYS_sendmsg_nocancel
+			SYS_recvfrom_nocancel
+			SYS_msync_nocancel
+			SYS_fcntl_nocancel
+			SYS_select_nocancel
+			SYS_sigsuspend_nocancel
+			SYS_readv_nocancel
+			SYS_writev_nocancel
+			SYS_sendto_nocancel
+			SYS_pread_nocancel
+			SYS_pwrite_nocancel
+			SYS___sigwait_nocancel
+			SYS_fsgetpath
+			SYS_fileport_makeport
+			SYS_fileport_makefd
+			SYS_memorystatus_control
+			SYS_guarded_open_np
+			SYS_guarded_kqueue_np
+			SYS_change_fdguard_np
+			SYS_openat
+			SYS_renameat
+			SYS_faccessat
+			SYS_fstatat
+			SYS_fstatat64
+			SYS_mkdirat
+			SYS_guarded_open_dprotected_np
+			SYS_guarded_write_np
+			SYS_guarded_pwrite_np
+			SYS_guarded_writev_np
+			SYS_renameatx_np
+			SYS_persona
+			SYS_mach_eventlink_signal
+			SYS_mach_eventlink_wait_until
+			SYS_mach_eventlink_signal_wait_until
+			SYS_work_interval_ctl
+			SYS_necp_open
+			SYS_necp_client_action
+			SYS___nexus_set_opt
+			SYS_terminate_with_payload
+			SYS_abort_with_payload
+			SYS_os_fault_with_payload
+			SYS_kqueue_workloop_ctl
+			SYS_memorystatus_available_memory
+			SYS_preadv
+			SYS_pwritev
+			SYS_preadv_nocancel
+			SYS_pwritev_nocancel
+			SYS_proc_info_extended_id
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
+		MSC_task_dyld_process_info_notify_get
+		MSC__kernelrpc_mach_vm_protect_trap
+		MSC__kernelrpc_mach_vm_map_trap
+		MSC__kernelrpc_mach_port_allocate_trap
+		MSC__kernelrpc_mach_port_deallocate_trap
+		MSC__kernelrpc_mach_port_mod_refs_trap
+		MSC__kernelrpc_mach_port_insert_right_trap
+		MSC__kernelrpc_mach_port_insert_member_trap
+		MSC__kernelrpc_mach_port_extract_member_trap
+		MSC__kernelrpc_mach_port_construct_trap
+		MSC__kernelrpc_mach_port_destruct_trap
+		MSC_mach_reply_port
+		MSC_thread_self_trap
+		MSC_task_self_trap
+		MSC_host_self_trap
+		MSC_semaphore_signal_trap
+		MSC_semaphore_wait_trap
+		MSC_semaphore_timedwait_trap
+		MSC__kernelrpc_mach_port_get_attributes_trap
+		MSC__kernelrpc_mach_port_guard_trap
+		MSC__kernelrpc_mach_port_unguard_trap
+		MSC_mach_generate_activity_id
+		MSC_task_name_for_pid
+		MSC_pid_for_task
+		MSC_mach_msg2_trap
+		MSC_thread_get_special_reply_port
+		MSC_swtch_pri
+		MSC_syscall_thread_switch
+		MSC_mach_vm_reclaim_update_kernel_accounting_trap
+		MSC_host_create_mach_voucher_trap
+		MSC__kernelrpc_mach_port_type_trap
+		MSC__kernelrpc_mach_port_request_notification_trap
+		MSC_mach_timebase_info_trap
+		MSC_mach_wait_until
+		MSC_mk_timer_create
+		MSC_mk_timer_destroy
+		MSC_mk_timer_arm
+		MSC_mk_timer_cancel
+		MSC_mk_timer_arm_leeway)
+)
+
+(deny syscall-mig)
+(allow syscall-mig
+	(kernel-mig-routine
+		host_info
+		host_get_io_master
+		host_get_clock_service
+		host_statistics_from_user
+		host_request_notification
+		host_statistics64_from_user
+		host_get_special_port
+		clock_get_time
+		mach_exception_raise
+		mach_exception_raise_state
+		mach_exception_raise_state_identity
+		io_object_conforms_to
+		io_iterator_next
+		io_registry_create_iterator
+		io_registry_entry_from_path
+		io_registry_entry_get_name
+		io_registry_entry_get_property_bytes
+		io_registry_entry_get_child_iterator
+		io_registry_entry_get_parent_iterator
+		io_service_close
+		io_connect_get_service
+		io_registry_get_root_entry
+		io_iterator_is_valid
+		io_service_open_extended
+		io_connect_map_memory_into_task
+		io_connect_unmap_memory_from_task
+		io_connect_method
+		io_connect_async_method
+		io_connect_set_notification_port_64
+		io_service_add_interest_notification_64
+		io_registry_entry_get_registry_entry_id
+		io_server_version
+		io_service_get_matching_service_bin
+		io_service_get_matching_services_bin
+		io_service_add_notification_bin_64
+		io_registry_entry_get_properties_bin_buf
+		io_registry_entry_get_property_bin_buf
+		mach_port_deallocate
+		mach_port_get_refs
+		mach_port_request_notification
+		mach_port_extract_right
+		mach_port_set_attributes
+		mach_port_get_context_from_user
+		task_threads_from_user
+		task_info_from_user
+		task_suspend
+		task_get_special_port_from_user
+		task_set_special_port
+		semaphore_create
+		semaphore_destroy
+		task_map_corpse_info_64
+		task_set_exc_guard_behavior
+		task_create_identity_token
+		thread_terminate
+		thread_get_state_to_user
+		thread_suspend
+		thread_resume
+		thread_info
+		thread_policy
+		thread_policy_set
+		thread_policy_get
+		vm_remap_external
+		vm_reallocate
+		mach_vm_read
+		mach_vm_copy
+		mach_vm_read_overwrite
+		mach_vm_map_external
+		mach_vm_remap_external
+		mach_vm_region_recurse
+		mach_vm_region
+		_mach_make_memory_entry
+		mach_vm_page_range_query
+		mach_vm_deferred_reclamation_buffer_allocate
+		mach_vm_deferred_reclamation_buffer_flush
+		mach_vm_range_create
+		mach_vm_deferred_reclamation_buffer_resize
+		mach_vm_reallocate
+		mach_memory_entry_ownership
+		mach_voucher_attr_command
+		task_restartable_ranges_register
+		task_restartable_ranges_synchronize
+		mach_eventlink_create
+		mach_eventlink_destroy
+		mach_eventlink_associate)
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
+		F_GETFD
+		F_GETFL
+		F_SETFL
+		F_GETLK
+		F_SETLKW
+		F_RDADVISE
+		F_RDAHEAD
+		F_NOCACHE
+		F_GETPATH
+		F_NODIRECT
+		F_GETPROTECTIONCLASS
+		F_SETPROTECTIONCLASS
+		F_DUPFD_CLOEXEC
+		F_SETNOSIGPIPE
+		F_BARRIERFSYNC
+		F_OFD_GETLK
+		F_OFD_SETLKWTIMEOUT
+		F_ADDFILESIGS_RETURN
+		F_CHECK_LV
+		F_PUNCHHOLE)
+)
+
 (deny system-fsctl)
 (allow system-fsctl
 	(fsctl-command

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 1)
+		(require-not (mac-policy-name "vnguard"))
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
+(allow system-necp-client-action
+	(necp-client-action
+		NECP_CLIENT_ACTION_ACQUIRE_AGENT_TOKEN
+		NECP_CLIENT_ACTION_ADD
+		NECP_CLIENT_ACTION_ADD_FLOW
+		NECP_CLIENT_ACTION_AGENT
+		NECP_CLIENT_ACTION_COPY_AGENT
+		NECP_CLIENT_ACTION_COPY_INTERFACE
+		NECP_CLIENT_ACTION_COPY_RESULT
+		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT_FINAL
+		NECP_CLIENT_ACTION_GET_SIGNED_CLIENT_ID
+		NECP_CLIENT_ACTION_MAP_SYSCTLS
+		NECP_CLIENT_ACTION_REMOVE
+		NECP_CLIENT_ACTION_REMOVE_FLOW
+		NECP_CLIENT_ACTION_UPDATE_CACHE)
+)
+
 (allow process-exec-update-label)
```
