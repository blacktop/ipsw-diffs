## nesessionmanager

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled"))

 		(require-not (global-name "com.apple.research.adtcd"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (system-attribute developer-mode))
 	)

 	(literal "/usr/sbin/pppd")
 )
 
+(deny socket-ioctl)
+(allow socket-ioctl
+	(ioctl-command
+		CTLIOCGINFO
+		SIOCAIFADDR
+		SIOCAIFAGENTID
+		SIOCDIFADDR
+		SIOCDIFAGENTID
+		SIOCGCONNINFO
+		SIOCGIFADDR
+		SIOCGIFAGENTDATA
+		SIOCGIFCONSTRAINED
+		SIOCGIFDELEGATE
+		SIOCGIFEXPENSIVE
+		SIOCGIFFLAGS
+		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
+		SIOCGIFMEDIA
+		SIOCGIFMTU
+		SIOCGIFTYPE
+		SIOCGIFULTRACONSTRAINED
+		SIOCSIFISVPN
+		SIOCSIFMTU)
+)
+
+(deny syscall-unix)
+(allow syscall-unix
+	(syscall-number
+		SYS_exit
+		SYS_fork
+		SYS_read
+		SYS_write
+		SYS_open
+		SYS_close
+		SYS_wait4
+		SYS_link
+		SYS_unlink
+		SYS_chdir
+		SYS_fchdir
+		SYS_chmod
+		SYS_chown
+		SYS_getfsstat
+		SYS_getpid
+		SYS_getuid
+		SYS_geteuid
+		SYS_recvmsg
+		SYS_sendmsg
+		SYS_recvfrom
+		SYS_accept
+		SYS_getpeername
+		SYS_getsockname
+		SYS_access
+		SYS_chflags
+		SYS_fchflags
+		SYS_sync
+		SYS_kill
+		SYS_crossarch_trap
+		SYS_getppid
+		SYS_dup
+		SYS_pipe
+		SYS_getegid
+		SYS_sigaction
+		SYS_getgid
+		SYS_sigprocmask
+		SYS_sigpending
+		SYS_sigaltstack
+		SYS_ioctl
+		SYS_symlink
+		SYS_readlink
+		SYS_execve
+		SYS_umask
+		SYS_msync
+		SYS_munmap
+		SYS_mprotect
+		SYS_madvise
+		SYS_mincore
+		SYS_getgroups
+		SYS_getdtablesize
+		SYS_dup2
+		SYS_fcntl
+		SYS_select
+		SYS_fsync
+		SYS_socket
+		SYS_connect
+		SYS_getpriority
+		SYS_bind
+		SYS_setsockopt
+		SYS_listen
+		SYS_sigsuspend
+		SYS_gettimeofday
+		SYS_getrusage
+		SYS_getsockopt
+		SYS_readv
+		SYS_writev
+		SYS_fchown
+		SYS_fchmod
+		SYS_rename
+		SYS_flock
+		SYS_sendto
+		SYS_shutdown
+		SYS_socketpair
+		SYS_mkdir
+		SYS_rmdir
+		SYS_utimes
+		SYS_pread
+		SYS_pwrite
+		SYS_statfs
+		SYS_fstatfs
+		SYS_quotactl
+		SYS_csops
+		SYS_csops_audittoken
+		SYS_kdebug_typefilter
+		SYS_kdebug_trace_string
+		SYS_kdebug_trace64
+		SYS_kdebug_trace
+		SYS_seteuid
+		SYS_sigreturn
+		SYS_stat
+		SYS_fstat
+		SYS_lstat
+		SYS_pathconf
+		SYS_fpathconf
+		SYS_getrlimit
+		SYS_setrlimit
+		SYS_mmap
+		SYS_lseek
+		SYS_truncate
+		SYS_ftruncate
+		SYS_sysctl
+		SYS_mlock
+		SYS_munlock
+		SYS_getumask
+		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
+		SYS_getattrlist
+		SYS_setattrlist
+		SYS_fgetattrlist
+		SYS_fsetattrlist
+		SYS_getxattr
+		SYS_fgetxattr
+		SYS_setxattr
+		SYS_fsetxattr
+		SYS_removexattr
+		SYS_fremovexattr
+		SYS_listxattr
+		SYS_flistxattr
+		SYS_fsctl
+		SYS_posix_spawn
+		SYS_ffsctl
+		SYS_shm_open
+		SYS_shm_unlink
+		SYS_sem_open
+		SYS_sem_close
+		SYS_sem_unlink
+		SYS_sysctlbyname
+		SYS_stat_extended
+		SYS_lstat_extended
+		SYS_fstat_extended
+		SYS_chmod_extended
+		SYS_fchmod_extended
+		SYS_access_extended
+		SYS_gettid
+		SYS_mkdir_extended
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
+		SYS_aio_suspend
+		SYS_iopolicysys
+		SYS_process_policy
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
+		SYS_getauid
+		SYS_bsdthread_create
+		SYS_bsdthread_terminate
+		SYS_kqueue
+		SYS_kevent
+		SYS_lchown
+		SYS_bsdthread_register
+		SYS_workq_open
+		SYS_workq_kernreturn
+		SYS_kevent64
+		SYS_thread_selfid
+		SYS_kevent_qos
+		SYS_kevent_id
+		SYS___mac_syscall
+		SYS_pselect
+		SYS_pselect_nocancel
+		SYS_read_nocancel
+		SYS_write_nocancel
+		SYS_open_nocancel
+		SYS_close_nocancel
+		SYS_wait4_nocancel
+		SYS_recvmsg_nocancel
+		SYS_sendmsg_nocancel
+		SYS_recvfrom_nocancel
+		SYS_accept_nocancel
+		SYS_msync_nocancel
+		SYS_fcntl_nocancel
+		SYS_select_nocancel
+		SYS_fsync_nocancel
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
+		SYS_guarded_open_np
+		SYS_guarded_close_np
+		SYS_guarded_kqueue_np
+		SYS_change_fdguard_np
+		SYS_proc_rlimit_control
+		SYS_connectx
+		SYS_getattrlistbulk
+		SYS_clonefileat
+		SYS_openat
+		SYS_openat_nocancel
+		SYS_renameat
+		SYS_faccessat
+		SYS_fchmodat
+		SYS_fchownat
+		SYS_fstatat
+		SYS_fstatat64
+		SYS_unlinkat
+		SYS_mkdirat
+		SYS_bsdthread_ctl
+		SYS_thread_selfusage
+		SYS_csrctl
+		SYS_guarded_open_dprotected_np
+		SYS_guarded_write_np
+		SYS_guarded_pwrite_np
+		SYS_guarded_writev_np
+		SYS_renameatx_np
+		SYS_mremap_encrypted
+		SYS_persona
+		SYS_mach_eventlink_signal_wait_until
+		SYS_work_interval_ctl
+		SYS_getentropy
+		SYS_necp_open
+		SYS_necp_client_action
+		SYS___nexus_set_opt
+		SYS___channel_open
+		SYS___channel_get_info
+		SYS___channel_sync
+		SYS_ulock_wait
+		SYS_ulock_wake
+		SYS_fclonefileat
+		SYS_terminate_with_payload
+		SYS_abort_with_payload
+		SYS_necp_session_open
+		SYS_necp_session_action
+		SYS_setattrlistat
+		SYS_os_fault_with_payload
+		SYS_kqueue_workloop_ctl
+		SYS_memorystatus_available_memory
+		SYS_objc_bp_assist_cfg_np
+		SYS_shared_region_map_and_slide_2_np
+		SYS_task_read_for_pid
+		SYS_preadv
+		SYS_pwritev
+		SYS_preadv_nocancel
+		SYS_pwritev_nocancel
+		SYS_ulock_wait2
+		SYS_proc_info_extended_id
+		SYS_map_with_linking_np)
+)
+
 (deny syscall-mach)
 (allow syscall-mach
 	(machtrap-number

 		MSC_mk_timer_arm_leeway)
 )
 
+(deny syscall-mig
+	(require-all
+		(require-not (kernel-mig-routine
+			host_info
+			host_get_io_master
+			host_get_clock_service
+			host_processors
+			host_get_special_port
+			host_set_special_port
+			clock_get_time
+			mach_exception_raise
+			mach_exception_raise_state
+			mach_exception_raise_state_identity
+			io_object_conforms_to
+			io_iterator_next
+			io_registry_create_iterator
+			io_registry_iterator_exit_entry
+			io_registry_entry_from_path
+			io_registry_entry_get_name
+			io_registry_entry_get_parent_iterator
+			io_service_close
+			io_registry_entry_create_iterator
+			io_iterator_is_valid
+			io_service_add_notification
+			io_service_add_interest_notification
+			io_service_open_extended
+			io_connect_unmap_memory_from_task
+			io_connect_method
+			io_connect_async_method
+			io_service_add_interest_notification_64
+			io_service_add_notification_ool_64
+			io_service_set_authorization_id
+			io_server_version
+			io_registry_entry_get_properties_bin
+			io_service_get_matching_service_bin
+			io_registry_entry_get_properties_bin_buf
+			io_registry_entry_get_property_bin_buf
+			mach_port_deallocate
+			mach_port_get_refs
+			mach_port_mod_refs
+			mach_port_request_notification
+			mach_port_insert_right
+			mach_port_extract_right
+			mach_port_get_attributes_from_user
+			mach_port_set_attributes
+			mach_port_allocate_qos
+			mach_port_get_context_from_user
+			mach_port_kobject_description_from_user
+			mach_port_is_connection_for_service
+			mach_port_get_service_port_info
+			mach_ports_register
+			mach_ports_lookup
+			task_info_from_user
+			task_resume
+			task_get_special_port_from_user
+			task_set_special_port
+			thread_create_from_user
+			semaphore_create
+			semaphore_destroy
+			task_policy_set
+			task_set_exc_guard_behavior
+			task_create_identity_token
+			thread_policy
+			vm_remap_external
+			mach_vm_region_info_64
+			vm_region_64
+			mach_make_memory_entry_64
+			vm_purgable_control
+			vm_reallocate
+			mach_vm_copy
+			mach_vm_msync
+			mach_vm_behavior_set
+			mach_vm_map_external
+			mach_vm_machine_attribute
+			mach_vm_remap_external
+			mach_vm_region
+			_mach_make_memory_entry
+			mach_vm_purgable_control
+			mach_vm_range_create
+			mach_vm_reallocate
+			mach_memory_entry_purgable_control
+			mach_memory_entry_ownership
+			mach_voucher_attr_command
+			task_restartable_ranges_register
+			task_restartable_ranges_synchronize))
+		(require-any
+			(kernel-mig-routine mach_vm_region_recurse)
+			(require-all
+				(require-not (kernel-mig-routine
+					host_info
+					host_get_clock_service
+					mach_exception_raise
+					mach_exception_raise_state
+					mach_exception_raise_state_identity
+					mach_port_get_context_from_user))
+				(require-not (kernel-mig-routine vm_remap_external))
+				(require-not (kernel-mig-routine task_restartable_ranges_register))
+				(require-not (kernel-mig-routine task_restartable_ranges_synchronize))
+				(require-not (kernel-mig-routine mach_vm_reallocate))
+				(require-not (kernel-mig-routine semaphore_create))
+				(require-not (kernel-mig-routine task_info_from_user))
+				(require-not (kernel-mig-routine io_service_open_extended))
+				(require-not (kernel-mig-routine vm_reallocate))
+			)
+		)
+	)
+)
+
 (deny sysctl*
 	(require-all
 		(sysctl-name "vm.debug_range_enabled")
```
