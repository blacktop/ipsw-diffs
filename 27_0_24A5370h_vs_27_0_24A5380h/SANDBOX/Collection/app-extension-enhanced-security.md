## app-extension-enhanced-security

> Group: ⬆️ Updated

```diff

 (deny file-clone)
 (allow file-clone
 	(require-all
-		(subpath "/private/var")
 		(require-any
 			(subpath "${FRONT_USER_HOME}")
 			(subpath "${HOME}")
 		)
+		(subpath "/private/var")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/")
 		(extension "com.apple.app-sandbox.read-write")
 	)

 )
 (allow file-read*
 	(require-all
-		(require-not (literal "/private/var"))
+		(require-not (literal "/dev"))
 		(require-not (require-any
 			(subpath "/AppleInternal/Library/VideoCodecs")
 			(subpath "/private/xarts")
 			(subpath "/usr/standalone/firmware")
 		))
+		(require-not (subpath "/private/var/MobileSoftwareUpdate"))
 		(require-not (subpath "/private/var/wireless/baseband_data"))
 		(require-not (subpath "/private/var/hardware"))
-		(require-not (literal "/dev"))
-		(require-not (subpath "/private/var/MobileSoftwareUpdate"))
+		(require-not (literal "/private/var"))
 		(require-any
 			(extension "com.apple.sandbox.executable")
-			(literal "/dev/null")
 			(literal "/dev/random")
 			(literal "/dev/urandom")
-			(literal "/dev/zero")
 			(literal "/private/etc/fstab")
 			(literal "/private/etc/hosts")
 			(literal "/private/etc/passwd")

 			(require-all
 				(file-mode #o0004)
 				(require-any
-					(literal "/private/etc/hosts")
+					(require-any
+						(literal "/private/etc/group")
+						(literal "/private/etc/protocols")
+					)
 					(subpath "/System")
 					(subpath "/private/var/db/timezone")
 					(subpath "/usr/lib")

 				(literal "/private/preboot")
 				(process-attribute is-apple-signed-executable)
 			)
+			(require-any
+				(literal "/dev/null")
+				(literal "/dev/zero")
+			)
 			(require-any
 				(literal "/private/etc/group")
 				(literal "/private/etc/protocols")

 						)
 					)
 					(require-all
+						(require-not (subpath "/private/var/MobileSoftwareUpdate"))
 						(require-not (subpath "/private/var/wireless/baseband_data"))
 						(require-not (subpath "/private/var/hardware"))
-						(require-not (literal "/dev"))
-						(require-not (subpath "/private/var/MobileSoftwareUpdate"))
+						(require-not (literal "/private/var"))
 						(require-any
 							(extension "com.apple.sandbox.executable")
-							(literal "/dev/null")
 							(literal "/dev/random")
 							(literal "/dev/urandom")
-							(literal "/dev/zero")
 							(literal "/private/etc/fstab")
 							(literal "/private/etc/hosts")
 							(literal "/private/etc/passwd")

 							(require-all
 								(file-mode #o0004)
 								(require-any
-									(literal "/private/etc/hosts")
+									(require-any
+										(literal "/private/etc/group")
+										(literal "/private/etc/protocols")
+									)
 									(subpath "/System")
 									(subpath "/private/var/db/timezone")
 									(subpath "/usr/lib")

 								(literal "/private/preboot")
 								(process-attribute is-apple-signed-executable)
 							)
+							(require-any
+								(literal "/dev/null")
+								(literal "/dev/zero")
+							)
 							(require-any
 								(literal "/private/etc/group")
 								(literal "/private/etc/protocols")

 				)
 			)
 			(require-all
+				(require-not (subpath "/private/var/MobileSoftwareUpdate"))
 				(require-not (subpath "/private/var/wireless/baseband_data"))
 				(require-not (subpath "/private/var/hardware"))
-				(require-not (literal "/dev"))
-				(require-not (subpath "/private/var/MobileSoftwareUpdate"))
+				(require-not (literal "/private/var"))
 				(require-any
 					(extension "com.apple.sandbox.executable")
-					(literal "/dev/null")
 					(literal "/dev/random")
 					(literal "/dev/urandom")
-					(literal "/dev/zero")
 					(literal "/private/etc/fstab")
 					(literal "/private/etc/hosts")
 					(literal "/private/etc/passwd")

 					(require-all
 						(file-mode #o0004)
 						(require-any
-							(literal "/private/etc/hosts")
+							(require-any
+								(literal "/private/etc/group")
+								(literal "/private/etc/protocols")
+							)
 							(subpath "/System")
 							(subpath "/private/var/db/timezone")
 							(subpath "/usr/lib")

 						(literal "/private/preboot")
 						(process-attribute is-apple-signed-executable)
 					)
+					(require-any
+						(literal "/dev/null")
+						(literal "/dev/zero")
+					)
 					(require-any
 						(literal "/private/etc/group")
 						(literal "/private/etc/protocols")

 		(literal "${FRONT_USER_HOME}")
 		(literal "${FRONT_USER_HOME}/Library/Preferences")
 		(require-not (literal "/private/var/run/syslog"))
-		(subpath "/Library/Preferences")
 	)
 )
 
 (allow file-write*
 	(require-all
-		(subpath "/private/var")
 		(require-any
 			(subpath "${FRONT_USER_HOME}")
 			(subpath "${HOME}")
 		)
+		(subpath "/private/var")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/")
 		(extension "com.apple.app-sandbox.read-write")
 	)

 
 (allow file-write-data
 	(require-all
-		(subpath "/private/var")
 		(require-any
 			(subpath "${FRONT_USER_HOME}")
 			(subpath "${HOME}")
 		)
+		(subpath "/private/var")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/")
 		(extension "com.apple.app-sandbox.read-write")
 	)

 	)
 )
 (allow file-write-data
-	(require-any
-		(literal "/dev/null")
-		(literal "/dev/zero")
+	(require-all
+		(require-any
+			(literal "/dev/null")
+			(literal "/dev/zero")
+		)
+		(require-not (literal "/dev/dtracehelper"))
 	)
 )
 

 	(require-all
 		(iokit-registry-entry-class "IOPlatformDevice")
 		(require-any
-			(iokit-property "artwork-scale-factor")
 			(iokit-property "iommu-present")
 			(iokit-property "product-id")
 			(iokit-property "soc-generation")

 				(iokit-property "artwork-device-subtype")
 				(iokit-property "artwork-display-gamut")
 				(iokit-property "artwork-dynamic-displaymode")
+				(iokit-property "artwork-scale-factor")
 				(iokit-property "compatible-device-fallback")
 				(iokit-property "device-perf-memory-class")
 				(iokit-property "graphics-featureset-class")

 	(with no-report)
 	(require-all
 		(require-not (xpc-service-name "*"))
-		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.CARenderServer"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.coremedia.mediaparserd.utilities"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(global-name "com.apple.mobilegestalt.xpc")
+		(global-name "com.apple.analyticsd")
 	)
 )
 (deny mach-lookup
 	(require-all
 		(require-not (xpc-service-name "*"))
-		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.CARenderServer"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.coremedia.mediaparserd.utilities"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(global-name "com.apple.mobilegestalt.xpc")
+		(global-name "com.apple.analyticsd")
 	)
 )
 

 		SYS_dup
 		SYS_getegid
 		SYS_getgid
-		SYS_sigprocmask
 		SYS_ioctl
 		SYS_umask
 		SYS_fcntl

 		SYS_writev
 		SYS_fchown
 		SYS_fchmod
+		SYS_mkdir
 		SYS_utimes
 		SYS_futimes
 		SYS_pwrite

 		SYS_kdebug_trace_string
 		SYS_kdebug_trace64
 		SYS_getrlimit
+		SYS_setrlimit
 		SYS_sysctl
 		SYS_getumask
 		SYS_getattrlist

 		SYS_chmod_extended
 		SYS_fchmod_extended
 		SYS_gettid
-		SYS_psynch_cvwait
+		SYS_psynch_mutexwait
+		SYS_psynch_rw_unlock
 		SYS_issetugid
 		SYS___pthread_kill
 		SYS___pthread_sigmask

 		SYS_proc_info
 		SYS_fstat64
 		SYS_getdirentries64
+		SYS_statfs64
 		SYS_fstatfs64
 		SYS_getfsstat64
 		SYS_bsdthread_create

 		SYS_open_nocancel
 		SYS_close_nocancel
 		SYS_fcntl_nocancel
-		SYS_sigsuspend_nocancel
 		SYS_writev_nocancel
 		SYS_pwrite_nocancel
 		SYS___semwait_signal_nocancel

 		SYS_fclonefileat
 		SYS_terminate_with_payload
 		SYS_abort_with_payload
-		SYS_shared_region_map_and_slide_2_np
 		SYS_pwritev
 		SYS_pwritev_nocancel
 		SYS_ulock_wait2

 		(require-not (syscall-number SYS_necp_open))
 		(require-not (syscall-number SYS_necp_client_action))
 		(require-any
+			(require-all
+				(require-not (syscall-number SYS_iopolicysys))
+				(require-any
+					(syscall-number SYS___mac_syscall)
+					(syscall-number SYS_crossarch_trap)
+					(syscall-number SYS_dup)
+					(syscall-number SYS_fstatat)
+					(syscall-number SYS_fstatat64)
+					(syscall-number SYS_getfsstat)
+					(syscall-number SYS_getfsstat64)
+					(syscall-number SYS_map_with_linking_np)
+					(syscall-number SYS_memorystatus_control)
+					(syscall-number SYS_open)
+					(syscall-number SYS_openat)
+				)
+			)
 			(require-all
 				(state-flag "blastdoor-post-launch")
 				(require-any

 						(syscall-number
 							SYS_read
 							SYS_sigaction
+							SYS_sigprocmask
 							SYS_sigaltstack
 							SYS_readlink
 							SYS_munmap
 							SYS_mprotect
 							SYS_madvise
 							SYS_socket
-							SYS_mkdir
 							SYS_pread
 							SYS_pathconf
-							SYS_setrlimit
 							SYS_mmap
 							SYS_lseek
 							SYS_shared_region_check_np
-							SYS_psynch_mutexwait
 							SYS_psynch_mutexdrop
 							SYS_psynch_cvbroad
 							SYS_psynch_cvsignal
+							SYS_psynch_cvwait
 							SYS_psynch_rw_rdlock
 							SYS_psynch_rw_wrlock
-							SYS_psynch_rw_unlock
 							SYS_psynch_cvclrprepost
 							SYS_process_policy
 							SYS_stat64
 							SYS_lstat64
 							SYS_stat64_extended
-							SYS_statfs64
 							SYS_workq_open
 							SYS_workq_kernreturn
 							SYS_thread_selfid
 							SYS_read_nocancel
+							SYS_sigsuspend_nocancel
 							SYS_os_fault_with_payload
 							SYS_kqueue_workloop_ctl
-							SYS_objc_bp_assist_cfg_np)
+							SYS_objc_bp_assist_cfg_np
+							SYS_shared_region_map_and_slide_2_np
+							SYS_map_with_linking_np)
 						(require-not (state-flag "blastdoor-post-launch"))
 					)
 					(syscall-number
 						SYS_read
 						SYS_pipe
+						SYS_sigprocmask
 						SYS_readlink
 						SYS_munmap
 						SYS_mprotect

 						SYS_socket
 						SYS_getrusage
 						SYS_rename
-						SYS_mkdir
 						SYS_rmdir
 						SYS_pread
 						SYS_quotactl
 						SYS_pathconf
 						SYS_fpathconf
-						SYS_setrlimit
 						SYS_mmap
 						SYS_lseek
 						SYS_setattrlist

 						SYS_psynch_rw_yieldwrlock
 						SYS_psynch_rw_downgrade
 						SYS_psynch_rw_upgrade
-						SYS_psynch_mutexwait
 						SYS_psynch_mutexdrop
 						SYS_psynch_cvbroad
 						SYS_psynch_cvsignal
+						SYS_psynch_cvwait
 						SYS_psynch_rw_rdlock
 						SYS_psynch_rw_wrlock
-						SYS_psynch_rw_unlock
 						SYS_psynch_rw_unlock2
 						SYS_psynch_cvclrprepost
 						SYS_process_policy

 						SYS_stat64_extended
 						SYS_lstat64_extended
 						SYS_fstat64_extended
-						SYS_statfs64
 						SYS___pthread_chdir
 						SYS___pthread_fchdir
 						SYS_workq_open
 						SYS_workq_kernreturn
 						SYS_thread_selfid
 						SYS_read_nocancel
+						SYS_sigsuspend_nocancel
 						SYS_change_fdguard_np
 						SYS_getattrlistbulk
 						SYS_faccessat

 						SYS_setattrlistat
 						SYS_os_fault_with_payload
 						SYS_memorystatus_available_memory
-						SYS_objc_bp_assist_cfg_np)
+						SYS_objc_bp_assist_cfg_np
+						SYS_shared_region_map_and_slide_2_np)
 				)
 			)
-			(require-all
-				(syscall-number
-					SYS_open
-					SYS_getfsstat
-					SYS_crossarch_trap
-					SYS_dup
-					SYS_getfsstat64
-					SYS___mac_syscall
-					SYS_memorystatus_control
-					SYS_openat
-					SYS_fstatat
-					SYS_fstatat64
-					SYS_map_with_linking_np)
-				(require-not (syscall-number SYS_iopolicysys))
-			)
 			(require-all
 				(syscall-number
 					SYS_read
 					SYS_sigaction
+					SYS_sigprocmask
 					SYS_sigaltstack
 					SYS_readlink
 					SYS_munmap
 					SYS_mprotect
 					SYS_madvise
 					SYS_socket
-					SYS_mkdir
 					SYS_pread
 					SYS_pathconf
-					SYS_setrlimit
 					SYS_mmap
 					SYS_lseek
 					SYS_shared_region_check_np
-					SYS_psynch_mutexwait
 					SYS_psynch_mutexdrop
 					SYS_psynch_cvbroad
 					SYS_psynch_cvsignal
+					SYS_psynch_cvwait
 					SYS_psynch_rw_rdlock
 					SYS_psynch_rw_wrlock
-					SYS_psynch_rw_unlock
 					SYS_psynch_cvclrprepost
 					SYS_process_policy
 					SYS_stat64
 					SYS_lstat64
 					SYS_stat64_extended
-					SYS_statfs64
 					SYS_workq_open
 					SYS_workq_kernreturn
 					SYS_thread_selfid
 					SYS_read_nocancel
+					SYS_sigsuspend_nocancel
 					SYS_os_fault_with_payload
 					SYS_kqueue_workloop_ctl
-					SYS_objc_bp_assist_cfg_np)
+					SYS_objc_bp_assist_cfg_np
+					SYS_shared_region_map_and_slide_2_np
+					SYS_map_with_linking_np)
 				(require-not (state-flag "blastdoor-post-launch"))
 			)
 		)

 	(require-all
 		(kernel-mig-routine mach_vm_range_create)
 		(require-not (kernel-mig-routine thread_terminate))
-		(require-not (kernel-mig-routine mach_memory_entry_ownership))
-		(require-not (kernel-mig-routine io_service_get_matching_services_bin))
-		(require-not (kernel-mig-routine thread_resume))
+		(require-not (kernel-mig-routine thread_suspend))
 		(require-not (kernel-mig-routine mach_port_deallocate))
+		(require-not (kernel-mig-routine io_service_get_matching_services_bin))
 		(require-not (kernel-mig-routine io_service_get_matching_service_bin))
 		(require-not (state-flag "blastdoor-post-launch"))
 	)

 	(require-all
 		(kernel-mig-routine mach_vm_range_create)
 		(require-not (kernel-mig-routine thread_terminate))
-		(require-not (kernel-mig-routine mach_memory_entry_ownership))
-		(require-not (kernel-mig-routine io_service_get_matching_services_bin))
-		(require-not (kernel-mig-routine thread_resume))
+		(require-not (kernel-mig-routine thread_suspend))
 		(require-not (kernel-mig-routine mach_port_deallocate))
+		(require-not (kernel-mig-routine io_service_get_matching_services_bin))
 		(require-not (kernel-mig-routine io_service_get_matching_service_bin))
 		(require-not (state-flag "blastdoor-post-launch"))
 	)

 		(require-any
 			(require-any
 				(sysctl-name "hw.activecpu")
+				(sysctl-name "hw.machine")
+				(sysctl-name "hw.memsize")
 				(sysctl-name "hw.ncpu")
+				(sysctl-name "kern.osproductversion")
 				(sysctl-name "kern.osvariant_status")
 				(sysctl-name "kern.secure_kernel")
 			)

 				(sysctl-name "hw.physicalcpu_max")
 				(sysctl-name "hw.product")
 			)
-			(require-any
-				(sysctl-name "hw.machine")
-				(sysctl-name "kern.osproductversion")
-			)
 			(require-any
 				(sysctl-name "hw.optional.arm.caps")
 				(sysctl-name "hw.optional.neon_fp16")

 				(sysctl-name "kern.maxfilesperproc")
 				(sysctl-name "kern.osversion")
 			)
-			(sysctl-name "hw.memsize")
 			(sysctl-name "hw.osenvironment")
 			(sysctl-name "hw.pagesize_compat")
 			(sysctl-name "hw.physicalcpu")
```
