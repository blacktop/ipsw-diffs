## ProductKitService

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
 (deny iokit-open-service)
 
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.daemonv1")
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")

 	)
 )
 
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
 		(require-not (global-name "com.apple.lsd.mapdb"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 
-(deny syscall-unix
-	(require-all
-		(require-not (syscall-number
-			SYS_exit
-			SYS_read
-			SYS_write
-			SYS_open
-			SYS_close
-			SYS_unlink
-			SYS_chmod
-			SYS_chown
-			SYS_getfsstat
-			SYS_getpid
-			SYS_getuid
-			SYS_geteuid
-			SYS_sendmsg
-			SYS_access
-			SYS_crossarch_trap
-			SYS_dup
-			SYS_getegid
-			SYS_sigaction
-			SYS_getgid
-			SYS_sigprocmask
-			SYS_sigpending
-			SYS_sigaltstack
-			SYS_ioctl
-			SYS_readlink
-			SYS_umask
-			SYS_munmap
-			SYS_mprotect
-			SYS_madvise
-			SYS_dup2
-			SYS_fcntl
-			SYS_fsync
-			SYS_socket
-			SYS_connect
-			SYS_sigsuspend
-			SYS_gettimeofday
-			SYS_readv
-			SYS_writev
-			SYS_fchown
-			SYS_fchmod
-			SYS_rename
-			SYS_sendto
-			SYS_mkdir
-			SYS_rmdir
-			SYS_pread
-			SYS_pwrite
-			SYS_statfs
-			SYS_fstatfs
-			SYS_csops
-			SYS_csops_audittoken
-			SYS_kdebug_typefilter
-			SYS_kdebug_trace_string
-			SYS_kdebug_trace64
-			SYS_kdebug_trace
-			SYS_sigreturn
-			SYS_stat
-			SYS_fstat
-			SYS_lstat
-			SYS_pathconf
-			SYS_getrlimit
-			SYS_setrlimit
-			SYS_mmap
-			SYS_lseek
-			SYS_ftruncate
-			SYS_sysctl
-			SYS_getumask
-			SYS_open_dprotected_np
-			SYS_openat_dprotected_np
-			SYS_getattrlist
-			SYS_fgetattrlist
-			SYS_fsetattrlist
-			SYS_fgetxattr
-			SYS_fsetxattr
-			SYS_flistxattr
-			SYS_fsctl
-			SYS_ffsctl
-			SYS_shm_open
-			SYS_sysctlbyname
-			SYS_stat_extended
-			SYS_lstat_extended
-			SYS_fstat_extended
-			SYS_chmod_extended
-			SYS_fchmod_extended
-			SYS_gettid
-			SYS_mkdir_extended
-			SYS_shared_region_check_np
-			SYS_psynch_rw_longrdlock
-			SYS_psynch_rw_yieldwrlock
-			SYS_psynch_rw_downgrade
-			SYS_psynch_rw_upgrade
-			SYS_psynch_mutexwait
-			SYS_psynch_mutexdrop
-			SYS_psynch_cvbroad
-			SYS_psynch_cvsignal
-			SYS_psynch_cvwait
-			SYS_psynch_rw_rdlock
-			SYS_psynch_rw_wrlock
-			SYS_psynch_rw_unlock
-			SYS_psynch_rw_unlock2
-			SYS_psynch_cvclrprepost
-			SYS_issetugid
-			SYS___pthread_kill
-			SYS___sigwait
-			SYS___disable_threadsignal
-			SYS___semwait_signal
-			SYS_proc_info
-			SYS_stat64
-			SYS_fstat64
-			SYS_lstat64
-			SYS_stat64_extended
-			SYS_lstat64_extended
-			SYS_fstat64_extended
-			SYS_getdirentries64
-			SYS_statfs64
-			SYS_fstatfs64
-			SYS_getfsstat64
-			SYS_bsdthread_create
-			SYS_bsdthread_terminate
-			SYS_kevent
-			SYS_bsdthread_register
-			SYS_workq_open
-			SYS_workq_kernreturn
-			SYS_kevent64
-			SYS_thread_selfid
-			SYS_kevent_qos
-			SYS_kevent_id
-			SYS___mac_syscall
-			SYS_read_nocancel
-			SYS_write_nocancel
-			SYS_open_nocancel
-			SYS_close_nocancel
-			SYS_sendmsg_nocancel
-			SYS_fcntl_nocancel
-			SYS_fsync_nocancel
-			SYS_connect_nocancel
-			SYS_sigsuspend_nocancel
-			SYS_readv_nocancel
-			SYS_writev_nocancel
-			SYS_sendto_nocancel
-			SYS_pread_nocancel
-			SYS_pwrite_nocancel
-			SYS___sigwait_nocancel
-			SYS___semwait_signal_nocancel
-			SYS_fsgetpath
-			SYS_fileport_makeport
-			SYS_fileport_makefd
-			SYS_memorystatus_control
-			SYS_guarded_close_np
-			SYS_proc_rlimit_control
-			SYS_getattrlistbulk
-			SYS_clonefileat
-			SYS_openat
-			SYS_fstatat
-			SYS_fstatat64
-			SYS_mkdirat
-			SYS_bsdthread_ctl
-			SYS_guarded_open_dprotected_np
-			SYS_guarded_write_np
-			SYS_guarded_pwrite_np
-			SYS_guarded_writev_np
-			SYS_persona
-			SYS_getentropy
-			SYS_ulock_wait
-			SYS_ulock_wake
-			SYS_terminate_with_payload
-			SYS_abort_with_payload
-			SYS_os_fault_with_payload
-			SYS_memorystatus_available_memory
-			SYS_preadv
-			SYS_pwritev
-			SYS_preadv_nocancel
-			SYS_pwritev_nocancel
-			SYS_ulock_wait2
-			SYS_map_with_linking_np))
-		(require-any
-			(require-all
-				(require-not (syscall-number SYS___pthread_kill))
-				(require-not (syscall-number
-					SYS_exit
-					SYS_getpid
-					SYS_getuid
-					SYS_geteuid
-					SYS_getegid
-					SYS_getgid
-					SYS_mprotect
-					SYS_kdebug_typefilter
-					SYS_kdebug_trace_string
-					SYS_kdebug_trace64
-					SYS_kdebug_trace
-					SYS_sysctl
-					SYS_getumask
-					SYS_sysctlbyname
-					SYS_gettid
-					SYS_issetugid
-					SYS_fsgetpath
-					SYS_abort_with_payload
-					SYS_os_fault_with_payload
-					SYS_memorystatus_available_memory))
-				(require-not (syscall-number
-					SYS_open
-					SYS_crossarch_trap
-					SYS_dup
-					SYS_umask
-					SYS_fcntl
-					SYS_pread
-					SYS_fsctl
-					SYS_shared_region_check_np
-					SYS_proc_info
-					SYS_thread_selfid
-					SYS___mac_syscall
-					SYS_fcntl_nocancel
-					SYS_pread_nocancel
-					SYS_memorystatus_control
-					SYS_openat
-					SYS_fstatat
-					SYS_fstatat64
-					SYS_terminate_with_payload))
-				(require-not (syscall-number SYS_getfsstat64))
-				(require-not (syscall-number SYS_map_with_linking_np))
-				(require-not (syscall-number SYS_getfsstat))
-			)
-			(syscall-number SYS___pthread_sigmask)
-		)
-	)
+(deny syscall-unix)
+(allow syscall-unix
+	(syscall-number
+		SYS_exit
+		SYS_read
+		SYS_write
+		SYS_open
+		SYS_close
+		SYS_unlink
+		SYS_chmod
+		SYS_chown
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
+		SYS_fsync
+		SYS_socket
+		SYS_connect
+		SYS_sigsuspend
+		SYS_gettimeofday
+		SYS_readv
+		SYS_writev
+		SYS_fchown
+		SYS_fchmod
+		SYS_rename
+		SYS_sendto
+		SYS_mkdir
+		SYS_rmdir
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
+		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
+		SYS_getattrlist
+		SYS_fgetattrlist
+		SYS_fsetattrlist
+		SYS_fgetxattr
+		SYS_fsetxattr
+		SYS_flistxattr
+		SYS_fsctl
+		SYS_ffsctl
+		SYS_shm_open
+		SYS_sysctlbyname
+		SYS_stat_extended
+		SYS_lstat_extended
+		SYS_fstat_extended
+		SYS_chmod_extended
+		SYS_fchmod_extended
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
+		SYS_guarded_close_np
+		SYS_proc_rlimit_control
+		SYS_getattrlistbulk
+		SYS_clonefileat
+		SYS_openat
+		SYS_fstatat
+		SYS_fstatat64
+		SYS_mkdirat
+		SYS_bsdthread_ctl
+		SYS_guarded_open_dprotected_np
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
 )
 
 (deny syscall-mach)

 		MSC_mk_timer_create)
 )
 
-(deny syscall-mig
-	(require-all
-		(require-not (kernel-mig-routine
-			host_info
-			host_get_clock_service
-			host_get_special_port
-			mach_exception_raise
-			mach_exception_raise_state
-			mach_exception_raise_state_identity
-			io_service_open_extended
-			mach_port_request_notification
-			mach_port_set_attributes
-			mach_port_get_context_from_user
-			mach_port_is_connection_for_service
-			mach_ports_lookup
-			task_info_from_user
-			task_get_special_port_from_user
-			task_set_special_port
-			semaphore_create
-			task_set_exc_guard_behavior
-			task_create_identity_token
-			vm_remap_external
-			vm_reallocate
-			mach_vm_copy
-			mach_vm_map_external
-			mach_vm_remap_external
-			_mach_make_memory_entry
-			mach_vm_range_create
-			mach_vm_reallocate
-			mach_memory_entry_ownership
-			mach_voucher_attr_command
-			task_restartable_ranges_register
-			task_restartable_ranges_synchronize))
-		(require-any
-			(kernel-mig-routine mach_vm_region_recurse)
-			(require-all
-				(require-not (kernel-mig-routine
-					host_info
-					host_get_clock_service
-					mach_exception_raise
-					mach_exception_raise_state
-					mach_exception_raise_state_identity
-					mach_port_get_context_from_user))
-				(require-not (kernel-mig-routine mach_vm_range_create))
-				(require-not (kernel-mig-routine vm_remap_external))
-				(require-not (kernel-mig-routine task_restartable_ranges_register))
-				(require-not (kernel-mig-routine task_restartable_ranges_synchronize))
-				(require-not (kernel-mig-routine mach_vm_reallocate))
-				(require-not (kernel-mig-routine semaphore_create))
-				(require-not (kernel-mig-routine task_info_from_user))
-				(require-not (kernel-mig-routine io_service_open_extended))
-				(require-not (kernel-mig-routine vm_reallocate))
-			)
-		)
-	)
+(deny syscall-mig)
+(allow syscall-mig
+	(kernel-mig-routine
+		host_info
+		host_get_clock_service
+		host_get_special_port
+		mach_exception_raise
+		mach_exception_raise_state
+		mach_exception_raise_state_identity
+		io_service_open_extended
+		mach_port_request_notification
+		mach_port_set_attributes
+		mach_port_get_context_from_user
+		mach_port_is_connection_for_service
+		mach_ports_lookup
+		task_info_from_user
+		task_get_special_port_from_user
+		task_set_special_port
+		semaphore_create
+		task_set_exc_guard_behavior
+		task_create_identity_token
+		vm_remap_external
+		vm_reallocate
+		mach_vm_copy
+		mach_vm_map_external
+		mach_vm_remap_external
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
```
