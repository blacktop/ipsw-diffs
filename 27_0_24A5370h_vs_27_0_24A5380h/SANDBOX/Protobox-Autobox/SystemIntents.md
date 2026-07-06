## SystemIntents

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.CarPlayApp.service"))
-		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
-		(require-not (global-name "com.apple.dasd.end-prewarm"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.pluginkit.pkd"))
-		(require-not (global-name "com.apple.hangtracerd"))
-		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.backboard.display.services"))
-		(require-not (global-name "com.apple.gpumemd.source"))
-		(require-not (global-name "com.apple.inputservice.keyboardui"))
-		(require-not (global-name "com.apple.hangtracermonitor"))
-		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
-		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.springboard.services"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.accessibility.gax.backboard"))
-		(require-not (global-name "com.apple.backboard.hid.services"))
-		(require-not (global-name "com.apple.inputanalyticsd"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.iohideventsystem"))
-		(require-not (global-name "com.apple.PowerManagement.control"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
 		(require-not (global-name "com.apple.TextInput"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.hangtracerd"))
 		(require-not (global-name "com.apple.UIKit.KeyboardManagement.hosted"))
-		(require-not (global-name "com.apple.linkd.autoShortcut"))
-		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
-		(require-not (global-name "com.apple.uiintelligencesupport.agent"))
-		(require-not (global-name "com.apple.ProgressReporting"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.inputanalyticsd"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
+		(require-not (global-name "com.apple.accessibility.gax.backboard"))
+		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.inputservice.keyboardui"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.dasd.end-prewarm"))
+		(require-not (global-name "com.apple.linkd.autoShortcut"))
+		(require-not (global-name "com.apple.accessibility.voices"))
+		(require-not (global-name "com.apple.springboard.services"))
+		(require-not (global-name "com.apple.backboard.display.services"))
+		(require-not (global-name "com.apple.uiintelligencesupport.agent"))
+		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.CarPlayApp.service"))
+		(require-not (global-name "com.apple.iohideventsystem"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
+		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
+		(require-not (global-name "com.apple.hangtracermonitor"))
+		(require-not (global-name "com.apple.gpumemd.source"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.backboard.hid.services"))
+		(require-not (global-name "com.apple.ProgressReporting"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AccessibilityUIServer"))
 		(require-not (system-attribute developer-mode))

 
 (deny socket-ioctl)
 
-(deny syscall-unix)
-(allow syscall-unix
-	(syscall-number
-		SYS_exit
-		SYS_read
-		SYS_write
-		SYS_open
-		SYS_close
-		SYS_unlink
-		SYS_getfsstat
-		SYS_getpid
-		SYS_getuid
-		SYS_geteuid
-		SYS_sendmsg
-		SYS_access
-		SYS_crossarch_trap
-		SYS_getppid
-		SYS_dup
-		SYS_getegid
-		SYS_getgid
-		SYS_ioctl
-		SYS_readlink
-		SYS_umask
-		SYS_munmap
-		SYS_mprotect
-		SYS_madvise
-		SYS_fcntl
-		SYS_fsync
-		SYS_socket
-		SYS_connect
-		SYS_gettimeofday
-		SYS_getrusage
-		SYS_readv
-		SYS_writev
-		SYS_fchmod
-		SYS_rename
-		SYS_sendto
-		SYS_mkdir
-		SYS_rmdir
-		SYS_pread
-		SYS_pwrite
-		SYS_statfs
-		SYS_fstatfs
-		SYS_csops
-		SYS_csops_audittoken
-		SYS_kdebug_typefilter
-		SYS_kdebug_trace_string
-		SYS_kdebug_trace64
-		SYS_kdebug_trace
-		SYS_thread_selfcounts
-		SYS_stat
-		SYS_fstat
-		SYS_lstat
-		SYS_pathconf
-		SYS_getrlimit
-		SYS_setrlimit
-		SYS_mmap
-		SYS_lseek
-		SYS_sysctl
-		SYS_getumask
-		SYS_open_dprotected_np
-		SYS_openat_dprotected_np
-		SYS_getattrlist
-		SYS_fgetattrlist
-		SYS_getxattr
-		SYS_fsetxattr
-		SYS_fsctl
-		SYS_shm_open
-		SYS_sem_open
-		SYS_sem_close
-		SYS_sysctlbyname
-		SYS_stat_extended
-		SYS_lstat_extended
-		SYS_fstat_extended
-		SYS_gettid
-		SYS_mkdir_extended
-		SYS_shared_region_check_np
-		SYS_psynch_rw_longrdlock
-		SYS_psynch_rw_yieldwrlock
-		SYS_psynch_rw_downgrade
-		SYS_psynch_rw_upgrade
-		SYS_psynch_mutexwait
-		SYS_psynch_mutexdrop
-		SYS_psynch_cvbroad
-		SYS_psynch_cvsignal
-		SYS_psynch_cvwait
-		SYS_psynch_rw_rdlock
-		SYS_psynch_rw_wrlock
-		SYS_psynch_rw_unlock
-		SYS_psynch_rw_unlock2
-		SYS_psynch_cvclrprepost
-		SYS_issetugid
-		SYS___pthread_kill
-		SYS___disable_threadsignal
-		SYS_proc_info
-		SYS_stat64
-		SYS_fstat64
-		SYS_lstat64
-		SYS_stat64_extended
-		SYS_lstat64_extended
-		SYS_fstat64_extended
-		SYS_getdirentries64
-		SYS_statfs64
-		SYS_fstatfs64
-		SYS_getfsstat64
-		SYS_bsdthread_create
-		SYS_bsdthread_terminate
-		SYS_kevent
-		SYS_bsdthread_register
-		SYS_workq_open
-		SYS_workq_kernreturn
-		SYS_kevent64
-		SYS_thread_selfid
-		SYS_kevent_qos
-		SYS_kevent_id
-		SYS___mac_syscall
-		SYS_read_nocancel
-		SYS_write_nocancel
-		SYS_open_nocancel
-		SYS_close_nocancel
-		SYS_sendmsg_nocancel
-		SYS_fcntl_nocancel
-		SYS_fsync_nocancel
-		SYS_connect_nocancel
-		SYS_readv_nocancel
-		SYS_writev_nocancel
-		SYS_sendto_nocancel
-		SYS_pread_nocancel
-		SYS_pwrite_nocancel
-		SYS_fsgetpath
-		SYS_memorystatus_control
-		SYS_guarded_close_np
-		SYS_change_fdguard_np
-		SYS_proc_rlimit_control
-		SYS_getattrlistbulk
-		SYS_openat
-		SYS_faccessat
-		SYS_fstatat
-		SYS_fstatat64
-		SYS_mkdirat
-		SYS_bsdthread_ctl
-		SYS_guarded_open_dprotected_np
-		SYS_guarded_write_np
-		SYS_guarded_pwrite_np
-		SYS_guarded_writev_np
-		SYS_persona
-		SYS_getentropy
-		SYS_necp_open
-		SYS_necp_client_action
-		SYS___channel_open
-		SYS___channel_get_info
-		SYS___channel_sync
-		SYS___channel_get_opt
-		SYS___channel_set_opt
-		SYS_ulock_wait
-		SYS_ulock_wake
-		SYS_terminate_with_payload
-		SYS_abort_with_payload
-		SYS_os_fault_with_payload
-		SYS_memorystatus_available_memory
-		SYS_preadv
-		SYS_pwritev
-		SYS_preadv_nocancel
-		SYS_pwritev_nocancel
-		SYS_ulock_wait2
-		SYS_proc_info_extended_id
-		SYS_map_with_linking_np)
+(deny syscall-unix
+	(require-all
+		(require-not (syscall-number
+			SYS_exit
+			SYS_read
+			SYS_write
+			SYS_open
+			SYS_close
+			SYS_unlink
+			SYS_getfsstat
+			SYS_getpid
+			SYS_getuid
+			SYS_geteuid
+			SYS_sendmsg
+			SYS_access
+			SYS_crossarch_trap
+			SYS_getppid
+			SYS_dup
+			SYS_getegid
+			SYS_sigaction
+			SYS_getgid
+			SYS_sigprocmask
+			SYS_sigpending
+			SYS_sigaltstack
+			SYS_ioctl
+			SYS_readlink
+			SYS_umask
+			SYS_munmap
+			SYS_mprotect
+			SYS_madvise
+			SYS_fcntl
+			SYS_fsync
+			SYS_socket
+			SYS_connect
+			SYS_sigsuspend
+			SYS_gettimeofday
+			SYS_getrusage
+			SYS_readv
+			SYS_writev
+			SYS_fchmod
+			SYS_rename
+			SYS_sendto
+			SYS_mkdir
+			SYS_rmdir
+			SYS_pread
+			SYS_pwrite
+			SYS_statfs
+			SYS_fstatfs
+			SYS_csops
+			SYS_csops_audittoken
+			SYS_kdebug_typefilter
+			SYS_kdebug_trace_string
+			SYS_kdebug_trace64
+			SYS_kdebug_trace
+			SYS_sigreturn
+			SYS_thread_selfcounts
+			SYS_stat
+			SYS_fstat
+			SYS_lstat
+			SYS_pathconf
+			SYS_getrlimit
+			SYS_setrlimit
+			SYS_mmap
+			SYS_lseek
+			SYS_sysctl
+			SYS_getumask
+			SYS_open_dprotected_np
+			SYS_openat_dprotected_np
+			SYS_getattrlist
+			SYS_fgetattrlist
+			SYS_getxattr
+			SYS_fsetxattr
+			SYS_fsctl
+			SYS_shm_open
+			SYS_sem_open
+			SYS_sem_close
+			SYS_sysctlbyname
+			SYS_stat_extended
+			SYS_lstat_extended
+			SYS_fstat_extended
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
+			SYS_issetugid
+			SYS___pthread_kill
+			SYS___sigwait
+			SYS___disable_threadsignal
+			SYS_proc_info
+			SYS_stat64
+			SYS_fstat64
+			SYS_lstat64
+			SYS_stat64_extended
+			SYS_lstat64_extended
+			SYS_fstat64_extended
+			SYS_getdirentries64
+			SYS_statfs64
+			SYS_fstatfs64
+			SYS_getfsstat64
+			SYS_bsdthread_create
+			SYS_bsdthread_terminate
+			SYS_kevent
+			SYS_bsdthread_register
+			SYS_workq_open
+			SYS_workq_kernreturn
+			SYS_kevent64
+			SYS_thread_selfid
+			SYS_kevent_qos
+			SYS_kevent_id
+			SYS___mac_syscall
+			SYS_read_nocancel
+			SYS_write_nocancel
+			SYS_open_nocancel
+			SYS_close_nocancel
+			SYS_sendmsg_nocancel
+			SYS_fcntl_nocancel
+			SYS_fsync_nocancel
+			SYS_connect_nocancel
+			SYS_sigsuspend_nocancel
+			SYS_readv_nocancel
+			SYS_writev_nocancel
+			SYS_sendto_nocancel
+			SYS_pread_nocancel
+			SYS_pwrite_nocancel
+			SYS___sigwait_nocancel
+			SYS_fsgetpath
+			SYS_memorystatus_control
+			SYS_guarded_open_np
+			SYS_guarded_close_np
+			SYS_change_fdguard_np
+			SYS_proc_rlimit_control
+			SYS_getattrlistbulk
+			SYS_openat
+			SYS_faccessat
+			SYS_fstatat
+			SYS_fstatat64
+			SYS_mkdirat
+			SYS_bsdthread_ctl
+			SYS_guarded_open_dprotected_np
+			SYS_guarded_write_np
+			SYS_guarded_pwrite_np
+			SYS_guarded_writev_np
+			SYS_persona
+			SYS_getentropy
+			SYS_necp_open
+			SYS_necp_client_action
+			SYS___channel_open
+			SYS___channel_get_info
+			SYS___channel_sync
+			SYS___channel_get_opt
+			SYS___channel_set_opt
+			SYS_ulock_wait
+			SYS_ulock_wake
+			SYS_terminate_with_payload
+			SYS_abort_with_payload
+			SYS_os_fault_with_payload
+			SYS_memorystatus_available_memory
+			SYS_preadv
+			SYS_pwritev
+			SYS_preadv_nocancel
+			SYS_pwritev_nocancel
+			SYS_ulock_wait2
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
+					SYS___pthread_kill
+					SYS_fsgetpath
+					SYS_abort_with_payload
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
+			(syscall-number SYS___pthread_sigmask)
+		)
+	)
 )
 
 (deny syscall-mach)

 			io_service_open_extended
 			io_connect_method
 			io_connect_async_method
+			io_service_add_interest_notification_64
 			io_registry_entry_get_registry_entry_id
 			io_server_version
 			io_service_get_matching_service_bin

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
```
