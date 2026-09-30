## com.apple.WebKit.WebContent

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.sharing.airdrop.readonly")
+		(extension-class "com.apple.mediaserverd.read")
 		(extension "com.apple.app-sandbox.read")
 	)
 )

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.sharing.airdrop.readonly")
 		(require-any
 			(extension "com.apple.app-sandbox.read")
 			(extension "com.apple.app-sandbox.read-write")
 			(extension "com.apple.sharing.airdrop.readonly")
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(require-all
-						(extension "com.apple.assets.read")
-						(require-any
-							(subpath "${HOME}/Library/Assets")
-							(subpath "/private/var/MobileAsset")
-						)
-					)
-					(subpath "/System/Cryptexes/OS/System/Library")
-					(subpath "/System/Library")
-					(subpath "/private/preboot/Cryptexes/OS/System/Library")
-				)
-			)
 		)
 	)
 )

 					(literal "${HOME}/Library/Caches/com.apple.itunesstored/url-resolution.plist")
 					(literal "${HOME}/Library/Preferences/com.apple.avfoundation.videoperformancehud.plist")
 					(literal "${HOME}/Library/Preferences/com.apple.security.plist")
-					(literal "/dev/null")
-					(literal "/dev/zero")
+					(literal "/dev/random")
+					(literal "/dev/urandom")
 					(literal "/private/etc/fstab")
 					(literal "/private/etc/hosts")
 					(literal "/private/etc/passwd")

 					(require-all
 						(extension "com.apple.assets.read")
 						(require-any
+							(require-any
+								(subpath "${HOME}/Library/Assets/com_apple_MobileAsset_VoiceServicesVocalizerVoice")
+								(subpath "${HOME}/Library/VoiceServices/Assets")
+							)
 							(subpath "${HOME}/Library/Assets")
 							(subpath "/private/var/MobileAsset")
-							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
 						)
 					)
 					(require-all

 						(literal "${HOME}/Library/Preferences/com.apple.itunesstored.plist")
 						(literal "${HOME}/Library/Preferences/com.apple.mediaremote.plist")
 					)
+					(require-any
+						(literal "/dev/null")
+						(literal "/dev/zero")
+					)
 					(require-any
 						(literal "/private/etc/group")
 						(literal "/private/etc/protocols")

 		(subpath "/System/Library")
 		(subpath "/private/preboot/Cryptexes/App")
 		(subpath "/private/preboot/Cryptexes/OS")
-		(subpath "/private/preboot/Cryptexes/OS/System/Library")
 		(subpath "/private/var/db/timezone")
 		(subpath "/private/var/preferences/Logging")
 		(subpath "/usr/lib")

 					(literal "${HOME}/Library/Caches/com.apple.itunesstored/url-resolution.plist")
 					(literal "${HOME}/Library/Preferences/com.apple.avfoundation.videoperformancehud.plist")
 					(literal "${HOME}/Library/Preferences/com.apple.security.plist")
-					(literal "/dev/null")
-					(literal "/dev/zero")
+					(literal "/dev/random")
+					(literal "/dev/urandom")
 					(literal "/private/etc/fstab")
 					(literal "/private/etc/hosts")
 					(literal "/private/etc/passwd")

 					(require-all
 						(extension "com.apple.assets.read")
 						(require-any
+							(require-any
+								(subpath "${HOME}/Library/Assets/com_apple_MobileAsset_VoiceServicesVocalizerVoice")
+								(subpath "${HOME}/Library/VoiceServices/Assets")
+							)
 							(subpath "${HOME}/Library/Assets")
 							(subpath "/private/var/MobileAsset")
-							(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
 						)
 					)
 					(require-all

 						(literal "${HOME}/Library/Preferences/com.apple.itunesstored.plist")
 						(literal "${HOME}/Library/Preferences/com.apple.mediaremote.plist")
 					)
+					(require-any
+						(literal "/dev/null")
+						(literal "/dev/zero")
+					)
 					(require-any
 						(literal "/private/etc/group")
 						(literal "/private/etc/protocols")

 		(subpath "/System/Library")
 		(subpath "/private/preboot/Cryptexes/App")
 		(subpath "/private/preboot/Cryptexes/OS")
-		(subpath "/private/preboot/Cryptexes/OS/System/Library")
 		(subpath "/private/var/db/timezone")
 		(subpath "/private/var/preferences/Logging")
 		(subpath "/usr/lib")

 
 (allow file-read-metadata
 	(require-any
-		(literal "${HOME}")
 		(literal "${HOME}/Library/Caches/powerlog.launchd")
+		(literal "${HOME}/Library/Preferences")
 		(require-not (literal "/private/var/db/MobileIdentityData/Version.plist"))
 		(vnode-type DIRECTORY SYMLINK)
 	)

 							(literal "${HOME}/Library/Caches/com.apple.itunesstored/url-resolution.plist")
 							(literal "${HOME}/Library/Preferences/com.apple.avfoundation.videoperformancehud.plist")
 							(literal "${HOME}/Library/Preferences/com.apple.security.plist")
-							(literal "/dev/null")
-							(literal "/dev/zero")
+							(literal "/dev/random")
+							(literal "/dev/urandom")
 							(literal "/private/etc/fstab")
 							(literal "/private/etc/hosts")
 							(literal "/private/etc/passwd")

 							(require-all
 								(extension "com.apple.assets.read")
 								(require-any
+									(require-any
+										(subpath "${HOME}/Library/Assets/com_apple_MobileAsset_VoiceServicesVocalizerVoice")
+										(subpath "${HOME}/Library/VoiceServices/Assets")
+									)
 									(subpath "${HOME}/Library/Assets")
 									(subpath "/private/var/MobileAsset")
-									(subpath "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.icloud.findmydevice.managed/Library")
 								)
 							)
 							(require-all

 								(literal "${HOME}/Library/Preferences/com.apple.itunesstored.plist")
 								(literal "${HOME}/Library/Preferences/com.apple.mediaremote.plist")
 							)
+							(require-any
+								(literal "/dev/null")
+								(literal "/dev/zero")
+							)
 							(require-any
 								(literal "/private/etc/group")
 								(literal "/private/etc/protocols")

 			(subpath "${FRONT_USER_HOME}/XcodeBuiltProducts")
 			(subpath "/Library/RegionFeatures")
 			(subpath "/System/Library")
-			(subpath "/private/preboot/Cryptexes/OS/System/Library")
 			(subpath "/private/var/db/timezone")
 			(subpath "/private/var/preferences/Logging")
 			(subpath "/usr/lib")

 		(require-not (literal "/dev/random"))
 		(require-any
 			(extension "com.apple.app-sandbox.read-write")
-			(literal "/dev/null")
-			(literal "/dev/zero")
 			(require-all
 				(extension "com.apple.sandbox.container")
 				(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")

 				(require-not (subpath "${HOME}/Library/Preferences"))
 			)
 			(require-all
-				(literal "/dev/dtracehelper")
-				(extension "com.apple.app-sandbox.read-write")
+				(require-any
+					(literal "/dev/null")
+					(literal "/dev/zero")
+				)
+				(require-not (literal "/dev/dtracehelper"))
 			)
 		)
 	)

 		(require-not (literal "/dev/random"))
 		(require-any
 			(extension "com.apple.app-sandbox.read-write")
-			(literal "/dev/null")
-			(literal "/dev/zero")
 			(require-all
 				(extension "com.apple.sandbox.container")
 				(subpath "/private/var/mobile/Containers/Data/PluginKitPlugin/[^/]+/tmp")

 				(require-not (subpath "${HOME}/Library/Preferences"))
 			)
 			(require-all
-				(literal "/dev/dtracehelper")
-				(extension "com.apple.app-sandbox.read-write")
+				(require-any
+					(literal "/dev/null")
+					(literal "/dev/zero")
+				)
+				(require-not (literal "/dev/dtracehelper"))
 			)
 		)
 	)

 (deny mach-lookup
 	(with no-report)
 	(require-all
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.SystemConfiguration.configd"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
-		(require-not (global-name "com.apple.fontservicesd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.SystemConfiguration.configd"))
+		(require-not (global-name "com.apple.fontservicesd"))
 		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (xpc-service-name "com.apple.audio.toolbox.reporting.service"))

 )
 (deny mach-lookup
 	(require-all
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.SystemConfiguration.configd"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
-		(require-not (global-name "com.apple.fontservicesd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.SystemConfiguration.configd"))
+		(require-not (global-name "com.apple.fontservicesd"))
 		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (xpc-service-name "com.apple.audio.toolbox.reporting.service"))

 (allow syscall-unix
 	(require-all
 		(require-not (syscall-number SYS_persona))
-		(require-not (syscall-number SYS_socket))
 		(require-not (syscall-number SYS_connect))
-		(require-not (syscall-number SYS_sigreturn))
+		(require-not (syscall-number SYS_socket))
 		(require-not (syscall-number SYS_crossarch_trap))
+		(require-not (syscall-number SYS_sigreturn))
 		(require-any
-			(require-all
-				(state-flag "EnableQuickLookSandboxResources")
-				(syscall-number
-					SYS_exit
-					SYS_read
-					SYS_write
-					SYS_open
-					SYS_close
-					SYS_unlink
-					SYS_getuid
-					SYS_geteuid
-					SYS_access
-					SYS_dup
-					SYS_getegid
-					SYS_getgid
-					SYS_sigprocmask
-					SYS_ioctl
-					SYS_readlink
-					SYS_umask
-					SYS_msync
-					SYS_munmap
-					SYS_mprotect
-					SYS_madvise
-					SYS_fcntl
-					SYS_fsync
-					SYS_gettimeofday
-					SYS_getrusage
-					SYS_writev
-					SYS_rename
-					SYS_flock
-					SYS_sendto
-					SYS_mkdir
-					SYS_rmdir
-					SYS_pread
-					SYS_csops
-					SYS_csops_audittoken
-					SYS_pathconf
-					SYS_getrlimit
-					SYS_setrlimit
-					SYS_mmap
-					SYS_lseek
-					SYS_ftruncate
-					SYS_sysctl
-					SYS_open_dprotected_np
-					SYS_getattrlist
-					SYS_fgetattrlist
-					SYS_fsetattrlist
-					SYS_getxattr
-					SYS_fgetxattr
-					SYS_fsetxattr
-					SYS_listxattr
-					SYS_shm_open
-					SYS_sem_open
-					SYS_sem_close
-					SYS_sysctlbyname
-					SYS_gettid
-					SYS_psynch_mutexwait
-					SYS_psynch_mutexdrop
-					SYS_psynch_cvbroad
-					SYS_psynch_cvsignal
-					SYS_psynch_cvwait
-					SYS_psynch_rw_rdlock
-					SYS_psynch_rw_wrlock
-					SYS_psynch_rw_unlock
-					SYS_psynch_cvclrprepost
-					SYS_issetugid
-					SYS___pthread_kill
-					SYS___pthread_sigmask
-					SYS___disable_threadsignal
-					SYS___semwait_signal
-					SYS_proc_info
-					SYS_stat64
-					SYS_fstat64
-					SYS_lstat64
-					SYS_fstat64_extended
-					SYS_getdirentries64
-					SYS_statfs64
-					SYS_fstatfs64
-					SYS_getfsstat64
-					SYS_bsdthread_create
-					SYS_bsdthread_terminate
-					SYS_kqueue
-					SYS_workq_kernreturn
-					SYS_thread_selfid
-					SYS_kevent_qos
-					SYS_kevent_id
-					SYS___mac_syscall
-					SYS_read_nocancel
-					SYS_write_nocancel
-					SYS_open_nocancel
-					SYS_close_nocancel
-					SYS_fcntl_nocancel
-					SYS_pread_nocancel
-					SYS_fileport_makefd
-					SYS_memorystatus_control
-					SYS_guarded_open_np
-					SYS_guarded_close_np
-					SYS_change_fdguard_np
-					SYS_getattrlistbulk
-					SYS_openat
-					SYS_openat_nocancel
-					SYS_faccessat
-					SYS_fstatat64
-					SYS_mkdirat
-					SYS_bsdthread_ctl
-					SYS_thread_selfusage
-					SYS_guarded_open_dprotected_np
-					SYS_guarded_pwrite_np
-					SYS_getentropy
-					SYS_ulock_wait
-					SYS_ulock_wake
-					SYS_abort_with_payload
-					SYS_os_fault_with_payload
-					SYS_kqueue_workloop_ctl
-					SYS_shared_region_map_and_slide_2_np
-					SYS_ulock_wait2)
-			)
 			(require-all
 				(state-flag "ParentProcessCanEnableQuickLookStateFlag")
-				(syscall-number
-					SYS_exit
-					SYS_read
-					SYS_write
-					SYS_open
-					SYS_close
-					SYS_unlink
-					SYS_getuid
-					SYS_geteuid
-					SYS_access
-					SYS_dup
-					SYS_getegid
-					SYS_getgid
-					SYS_sigprocmask
-					SYS_ioctl
-					SYS_readlink
-					SYS_umask
-					SYS_msync
-					SYS_munmap
-					SYS_mprotect
-					SYS_madvise
-					SYS_fcntl
-					SYS_fsync
-					SYS_gettimeofday
-					SYS_getrusage
-					SYS_writev
-					SYS_rename
-					SYS_flock
-					SYS_sendto
-					SYS_mkdir
-					SYS_rmdir
-					SYS_pread
-					SYS_csops
-					SYS_csops_audittoken
-					SYS_pathconf
-					SYS_getrlimit
-					SYS_setrlimit
-					SYS_mmap
-					SYS_lseek
-					SYS_ftruncate
-					SYS_sysctl
-					SYS_open_dprotected_np
-					SYS_getattrlist
-					SYS_fgetattrlist
-					SYS_fsetattrlist
-					SYS_getxattr
-					SYS_fgetxattr
-					SYS_fsetxattr
-					SYS_listxattr
-					SYS_shm_open
-					SYS_sem_open
-					SYS_sem_close
-					SYS_sysctlbyname
-					SYS_gettid
-					SYS_psynch_mutexwait
-					SYS_psynch_mutexdrop
-					SYS_psynch_cvbroad
-					SYS_psynch_cvsignal
-					SYS_psynch_cvwait
-					SYS_psynch_rw_rdlock
-					SYS_psynch_rw_wrlock
-					SYS_psynch_rw_unlock
-					SYS_psynch_cvclrprepost
-					SYS_issetugid
-					SYS___pthread_kill
-					SYS___pthread_sigmask
-					SYS___disable_threadsignal
-					SYS___semwait_signal
-					SYS_proc_info
-					SYS_stat64
-					SYS_fstat64
-					SYS_lstat64
-					SYS_fstat64_extended
-					SYS_getdirentries64
-					SYS_statfs64
-					SYS_fstatfs64
-					SYS_getfsstat64
-					SYS_bsdthread_create
-					SYS_bsdthread_terminate
-					SYS_kqueue
-					SYS_workq_kernreturn
-					SYS_thread_selfid
-					SYS_kevent_qos
-					SYS_kevent_id
-					SYS___mac_syscall
-					SYS_read_nocancel
-					SYS_write_nocancel
-					SYS_open_nocancel
-					SYS_close_nocancel
-					SYS_fcntl_nocancel
-					SYS_pread_nocancel
-					SYS_fileport_makefd
-					SYS_memorystatus_control
-					SYS_guarded_open_np
-					SYS_guarded_close_np
-					SYS_change_fdguard_np
-					SYS_getattrlistbulk
-					SYS_openat
-					SYS_openat_nocancel
-					SYS_faccessat
-					SYS_fstatat64
-					SYS_mkdirat
-					SYS_bsdthread_ctl
-					SYS_thread_selfusage
-					SYS_guarded_open_dprotected_np
-					SYS_guarded_pwrite_np
-					SYS_getentropy
-					SYS_ulock_wait
-					SYS_ulock_wake
-					SYS_abort_with_payload
-					SYS_os_fault_with_payload
-					SYS_kqueue_workloop_ctl
-					SYS_shared_region_map_and_slide_2_np
-					SYS_ulock_wait2)
-				(require-not (syscall-number SYS_openat_nocancel))
-				(require-not (syscall-number SYS_pread_nocancel))
-				(require-not (syscall-number SYS_sendto))
-				(require-not (syscall-number SYS_thread_selfusage))
-				(require-not (syscall-number SYS_rmdir))
-				(require-not (syscall-number SYS_unlink))
-				(require-not (syscall-number SYS_mkdirat))
+				(require-any
+					(require-all
+						(state-flag "EnableQuickLookSandboxResources")
+						(syscall-number SYS_sendto)
+					)
+					(require-all
+						(syscall-number
+							SYS_exit
+							SYS_read
+							SYS_write
+							SYS_open
+							SYS_close
+							SYS_unlink
+							SYS_getuid
+							SYS_geteuid
+							SYS_access
+							SYS_dup
+							SYS_getegid
+							SYS_getgid
+							SYS_sigprocmask
+							SYS_ioctl
+							SYS_readlink
+							SYS_umask
+							SYS_msync
+							SYS_munmap
+							SYS_mprotect
+							SYS_madvise
+							SYS_fcntl
+							SYS_fsync
+							SYS_gettimeofday
+							SYS_getrusage
+							SYS_writev
+							SYS_rename
+							SYS_flock
+							SYS_mkdir
+							SYS_rmdir
+							SYS_pread
+							SYS_csops
+							SYS_csops_audittoken
+							SYS_pathconf
+							SYS_getrlimit
+							SYS_setrlimit
+							SYS_mmap
+							SYS_lseek
+							SYS_ftruncate
+							SYS_sysctl
+							SYS_open_dprotected_np
+							SYS_getattrlist
+							SYS_fgetattrlist
+							SYS_fsetattrlist
+							SYS_getxattr
+							SYS_fgetxattr
+							SYS_fsetxattr
+							SYS_listxattr
+							SYS_shm_open
+							SYS_sem_open
+							SYS_sem_close
+							SYS_sysctlbyname
+							SYS_gettid
+							SYS_psynch_mutexwait
+							SYS_psynch_mutexdrop
+							SYS_psynch_cvbroad
+							SYS_psynch_cvsignal
+							SYS_psynch_cvwait
+							SYS_psynch_rw_rdlock
+							SYS_psynch_rw_wrlock
+							SYS_psynch_rw_unlock
+							SYS_psynch_cvclrprepost
+							SYS_issetugid
+							SYS___pthread_kill
+							SYS___pthread_sigmask
+							SYS___disable_threadsignal
+							SYS___semwait_signal
+							SYS_proc_info
+							SYS_stat64
+							SYS_fstat64
+							SYS_lstat64
+							SYS_fstat64_extended
+							SYS_getdirentries64
+							SYS_statfs64
+							SYS_fstatfs64
+							SYS_getfsstat64
+							SYS_bsdthread_create
+							SYS_bsdthread_terminate
+							SYS_kqueue
+							SYS_workq_kernreturn
+							SYS_thread_selfid
+							SYS_kevent_qos
+							SYS_kevent_id
+							SYS___mac_syscall
+							SYS_read_nocancel
+							SYS_write_nocancel
+							SYS_open_nocancel
+							SYS_close_nocancel
+							SYS_fcntl_nocancel
+							SYS_pread_nocancel
+							SYS_fileport_makefd
+							SYS_memorystatus_control
+							SYS_guarded_open_np
+							SYS_guarded_close_np
+							SYS_change_fdguard_np
+							SYS_getattrlistbulk
+							SYS_openat
+							SYS_openat_nocancel
+							SYS_faccessat
+							SYS_fstatat64
+							SYS_mkdirat
+							SYS_bsdthread_ctl
+							SYS_thread_selfusage
+							SYS_guarded_open_dprotected_np
+							SYS_guarded_pwrite_np
+							SYS_getentropy
+							SYS_ulock_wait
+							SYS_ulock_wake
+							SYS_abort_with_payload
+							SYS_os_fault_with_payload
+							SYS_kqueue_workloop_ctl
+							SYS_shared_region_map_and_slide_2_np
+							SYS_ulock_wait2)
+						(require-not (syscall-number SYS_sendto))
+						(require-not (syscall-number SYS_unlink))
+						(require-not (syscall-number SYS_rmdir))
+						(require-not (syscall-number SYS_openat_nocancel))
+						(require-not (syscall-number SYS_thread_selfusage))
+						(require-not (syscall-number SYS_mkdirat))
+						(require-not (syscall-number SYS_pread_nocancel))
+					)
+				)
 			)
 			(require-all
 				(syscall-number

 				SYS_writev
 				SYS_rename
 				SYS_flock
-				SYS_sendto
 				SYS_mkdir
 				SYS_rmdir
 				SYS_pread

 				SYS_kqueue_workloop_ctl
 				SYS_shared_region_map_and_slide_2_np
 				SYS_ulock_wait2)
+			(syscall-number SYS_sendto)
 		)
 	)
 )

 			)
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
 				(sysctl-name "kern.hostname")
+				(sysctl-name "kern.ostype")
 				(sysctl-name "kern.version")
 			)
 			(require-any

 				(sysctl-name "kern.osversion")
 			)
 			(sysctl-name "hw.cpusubfamily")
-			(sysctl-name "hw.memsize")
 			(sysctl-name "hw.pagesize_compat")
 			(sysctl-name "hw.physicalcpu")
 			(sysctl-name "kern.bootargs")
 			(sysctl-name "kern.bootsessionuuid")
 			(sysctl-name "kern.osrelease")
-			(sysctl-name "kern.ostype")
 			(sysctl-name "kern.willshutdown")
 			(sysctl-name "vm.footprint_suspend")
 		)

 			)
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
 				(sysctl-name "kern.hostname")
+				(sysctl-name "kern.ostype")
 				(sysctl-name "kern.version")
 			)
 			(require-any

 				(sysctl-name "kern.osversion")
 			)
 			(sysctl-name "hw.cpusubfamily")
-			(sysctl-name "hw.memsize")
 			(sysctl-name "hw.pagesize_compat")
 			(sysctl-name "hw.physicalcpu")
 			(sysctl-name "kern.bootargs")
 			(sysctl-name "kern.bootsessionuuid")
 			(sysctl-name "kern.osrelease")
-			(sysctl-name "kern.ostype")
 			(sysctl-name "kern.willshutdown")
 			(sysctl-name "vm.footprint_suspend")
 		)

 			)
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
 				(sysctl-name "kern.hostname")
+				(sysctl-name "kern.ostype")
 				(sysctl-name "kern.version")
 			)
 			(require-any

 				(sysctl-name "kern.osversion")
 			)
 			(sysctl-name "hw.cpusubfamily")
-			(sysctl-name "hw.memsize")
 			(sysctl-name "hw.pagesize_compat")
 			(sysctl-name "hw.physicalcpu")
 			(sysctl-name "kern.bootargs")
 			(sysctl-name "kern.bootsessionuuid")
 			(sysctl-name "kern.osrelease")
-			(sysctl-name "kern.ostype")
 			(sysctl-name "kern.willshutdown")
 			(sysctl-name "vm.footprint_suspend")
 		)
```
