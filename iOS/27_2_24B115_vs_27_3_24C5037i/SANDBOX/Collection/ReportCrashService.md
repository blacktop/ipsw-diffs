## ReportCrashService

> Group: 🆕 NEW

```scheme
(version 1)
(enable-profile-flag "common-apple-internal-rules")

(deny default)

(deny darwin-notification-post)

(deny dynamic-code-generation)

(deny file-clone)

(allow file-issue-extension
	(require-all
		(extension-class "com.apple.app-sandbox.read")
		(require-any
			(subpath "/System/Cryptexes")
			(subpath "/private/preboot/Cryptexes")
		)
	)
)

(deny file-link)

(deny file-map-executable)
(allow file-map-executable
	(require-all
		(require-any
			(subpath "/Developer/Library")
			(subpath "/System/Developer/Library")
		)
		(system-attribute developer-mode)
	)
)
(allow file-map-executable
	(require-any
		(extension "com.apple.sandbox.executable")
		(subpath "/System/Cryptexes")
		(subpath "/System/Library")
		(subpath "/private/preboot/Cryptexes")
		(subpath "/usr/lib")
	)
)
(deny file-map-executable)

(allow file-read*
	(require-all
		(require-not (literal "/dev"))
		(require-not (require-any
			(subpath "/AppleInternal/Library/VideoCodecs")
			(subpath "/private/xarts")
			(subpath "/usr/standalone/firmware")
		))
		(require-not (subpath "/private/var/MobileSoftwareUpdate"))
		(require-not (subpath "/private/var/wireless/baseband_data"))
		(require-not (subpath "/private/var/hardware"))
		(require-not (literal "/private/var"))
		(require-any
			(extension "com.apple.sandbox.executable")
			(literal "/dev/random")
			(literal "/dev/urandom")
			(literal "/private/etc/fstab")
			(literal "/private/etc/hosts")
			(literal "/private/etc/passwd")
			(literal "/private/etc/services")
			(require-all
				(file-mode #o0004)
				(require-any
					(require-any
						(literal "/private/etc/group")
						(literal "/private/etc/protocols")
					)
					(subpath "/System")
					(subpath "/private/var/db/timezone")
					(subpath "/usr/lib")
					(subpath "/usr/share")
				)
			)
			(require-all
				(literal "/System")
				(process-attribute is-apple-signed-executable)
			)
			(require-all
				(literal "/private")
				(process-attribute is-apple-signed-executable)
			)
			(require-all
				(literal "/private/preboot")
				(process-attribute is-apple-signed-executable)
			)
			(require-any
				(literal "/dev/null")
				(literal "/dev/zero")
			)
			(require-any
				(literal "/private/etc/group")
				(literal "/private/etc/protocols")
			)
			(require-any
				(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
				(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
			)
			(require-any
				(subpath "/System/Cryptexes")
				(subpath "/private/preboot/Cryptexes")
			)
			(subpath "/")
		)
	)
)
(allow file-read*
	(require-all
		(system-attribute developer-mode)
		(require-any
			(require-any
				(subpath "/Developer/Library")
				(subpath "/System/Developer/Library")
			)
			(require-any
				(subpath "/Developer/usr")
				(subpath "/System/Developer/usr")
			)
		)
	)
)
(allow file-read*
	(require-any
		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/EffectiveUserSettings.plist")
		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo/MCMeta.plist")
		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo/PublicEffectiveUserSettings.plist")
		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo/Truth.plist")
		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/EffectiveUserSettings.plist")
		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo/MCMeta.plist")
		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo/PublicEffectiveUserSettings.plist")
		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo/Truth.plist")
		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/EffectiveUserSettings.plist")
		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo/MCMeta.plist")
		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo/PublicEffectiveUserSettings.plist")
		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo/Truth.plist")
		(literal "/private/var/preferences/Logging/com.apple.diagnosticd.filter.plist")
		(subpath "${FRONT_USER_HOME}/Containers/Bundle")
		(subpath "/AppleInternal/Applications")
		(subpath "/Applications")
		(subpath "/Developer/Applications")
		(subpath "/System/Developer/Applications")
		(subpath "/System/Library")
		(subpath "/bin")
		(subpath "/private/var/containers/Bundle")
		(subpath "/private/var/factory_mount/[^/]+/Applications")
		(subpath "/private/var/mobile/Library/Logs/AppleSupport")
		(subpath "/private/var/mobile/Library/OSAnalytics/Preferences")
		(subpath "/private/var/mobile/tmp/com.apple.ReportCrashService")
		(subpath "/private/var/personalized_automation/Applications")
		(subpath "/private/var/personalized_debug/Applications")
		(subpath "/private/var/personalized_factory/[^/]+/Applications")
		(subpath "/sbin")
		(subpath "/usr/bin")
		(subpath "/usr/lib")
		(subpath "/usr/libexec")
		(subpath "/usr/sbin")
	)
)

(allow file-read-data
	(require-all
		(require-not (literal "/dev"))
		(require-not (require-any
			(subpath "/AppleInternal/Library/VideoCodecs")
			(subpath "/private/xarts")
			(subpath "/usr/standalone/firmware")
		))
		(require-not (subpath "/private/var/MobileSoftwareUpdate"))
		(require-not (subpath "/private/var/wireless/baseband_data"))
		(require-not (subpath "/private/var/hardware"))
		(require-not (literal "/private/var"))
		(require-any
			(extension "com.apple.sandbox.executable")
			(literal "/dev/random")
			(literal "/dev/urandom")
			(literal "/private/etc/fstab")
			(literal "/private/etc/hosts")
			(literal "/private/etc/passwd")
			(literal "/private/etc/services")
			(require-all
				(file-mode #o0004)
				(require-any
					(require-any
						(literal "/private/etc/group")
						(literal "/private/etc/protocols")
					)
					(subpath "/System")
					(subpath "/private/var/db/timezone")
					(subpath "/usr/lib")
					(subpath "/usr/share")
				)
			)
			(require-all
				(literal "/System")
				(process-attribute is-apple-signed-executable)
			)
			(require-all
				(literal "/private")
				(process-attribute is-apple-signed-executable)
			)
			(require-all
				(literal "/private/preboot")
				(process-attribute is-apple-signed-executable)
			)
			(require-any
				(literal "/dev/null")
				(literal "/dev/zero")
			)
			(require-any
				(literal "/private/etc/group")
				(literal "/private/etc/protocols")
			)
			(require-any
				(literal "/private/preboot/cryptex1/current/RestoreVersion.plist")
				(literal "/private/preboot/cryptex1/current/SystemVersion.plist")
			)
			(require-any
				(subpath "/System/Cryptexes")
				(subpath "/private/preboot/Cryptexes")
			)
			(subpath "/")
		)
	)
)
(allow file-read-data
	(require-all
		(system-attribute developer-mode)
		(require-any
			(require-any
				(subpath "/Developer/Library")
				(subpath "/System/Developer/Library")
			)
			(require-any
				(subpath "/Developer/usr")
				(subpath "/System/Developer/usr")
			)
		)
	)
)
(allow file-read-data
	(require-any
		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/EffectiveUserSettings.plist")
		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo/MCMeta.plist")
		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo/PublicEffectiveUserSettings.plist")
		(literal "${FRONT_USER_HOME}/Library/ConfigurationProfiles/PublicInfo/Truth.plist")
		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/EffectiveUserSettings.plist")
		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo/MCMeta.plist")
		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo/PublicEffectiveUserSettings.plist")
		(literal "${FRONT_USER_HOME}/Library/UserConfigurationProfiles/PublicInfo/Truth.plist")
		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/EffectiveUserSettings.plist")
		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo/MCMeta.plist")
		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo/PublicEffectiveUserSettings.plist")
		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/PublicInfo/Truth.plist")
		(literal "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist")
		(literal "/private/var/db/eligibilityd/eligibility.plist")
		(literal "/private/var/preferences/Logging/com.apple.diagnosticd.filter.plist")
		(subpath "${FRONT_USER_HOME}/Containers/Bundle")
		(subpath "/AppleInternal/Applications")
		(subpath "/Applications")
		(subpath "/Developer/Applications")
		(subpath "/System/Developer/Applications")
		(subpath "/System/Library")
		(subpath "/bin")
		(subpath "/private/var/containers/Bundle")
		(subpath "/private/var/factory_mount/[^/]+/Applications")
		(subpath "/private/var/mobile/Library/Logs/AppleSupport")
		(subpath "/private/var/mobile/Library/OSAnalytics/Preferences")
		(subpath "/private/var/mobile/tmp/com.apple.ReportCrashService")
		(subpath "/private/var/personalized_automation/Applications")
		(subpath "/private/var/personalized_debug/Applications")
		(subpath "/private/var/personalized_factory/[^/]+/Applications")
		(subpath "/sbin")
		(subpath "/usr/bin")
		(subpath "/usr/lib")
		(subpath "/usr/libexec")
		(subpath "/usr/sbin")
	)
)

(allow file-read-metadata)
(deny file-read-metadata
	(literal "/private/var/run/syslog")
)

(allow file-write*
	(require-any
		(subpath "/private/var/mobile/Library/Logs/AppleSupport")
		(subpath "/private/var/mobile/Library/OSAnalytics/Preferences")
		(subpath "/private/var/mobile/tmp/com.apple.ReportCrashService")
	)
)

(allow file-write-data
	(require-all
		(require-not (literal "/dev/dtracehelper"))
		(require-any
			(require-any
				(literal "/dev/null")
				(literal "/dev/zero")
			)
			(require-any
				(subpath "/private/var/mobile/Library/Logs/AppleSupport")
				(subpath "/private/var/mobile/Library/OSAnalytics/Preferences")
				(subpath "/private/var/mobile/tmp/com.apple.ReportCrashService")
			)
		)
	)
)

(deny fs-quota*)

(deny fs-snapshot-mount)

(deny iokit-get-properties)
(allow iokit-get-properties
	(iokit-registry-entry-class "AppleSmartBattery")
)

(allow iokit-open-user-client
	(require-any
		(iokit-registry-entry-class "AppleCredentialManagerUserClient")
		(iokit-registry-entry-class "AppleKeyStoreUserClient")
		(iokit-registry-entry-class "ApplePMGRUserClient")
	)
)

(deny iokit-open-service)
(allow iokit-open-service
	(require-any
		(iokit-registry-entry-class "AppleCredentialManager")
		(iokit-registry-entry-class "AppleKeyStore")
		(iokit-registry-entry-class "AppleT[0-9]")
		(iokit-registry-entry-class #"AppleT([0-9])+PMGR")
	)
)

(allow ipc-posix-shm-read-data
	(with report)
)

(allow ipc-posix-shm-write-data
	(ipc-posix-name "apple.cfprefs.daemonv1")
)

(deny mach-bootstrap)

(deny mach-cross-domain-lookup)

(allow mach-lookup
	(require-all
		(require-not (global-name "com.apple.distributed_notifications@1v3"))
		(require-any
			(global-name "com.apple.analyticsagent")
			(global-name "com.apple.analyticsd")
			(global-name "com.apple.mobilegestalt.xpc")
			(require-all
				(require-not (global-name "com.apple.tailspind"))
				(require-any
					(global-name "com.apple.OTATaskingAgent")
					(global-name "com.apple.ReportMemoryException")
					(global-name "com.apple.biome.PublicStreamAccessService")
					(global-name "com.apple.biome.access.system")
					(global-name "com.apple.commcenter.coretelephony.xpc")
					(global-name "com.apple.commcenter.xpc")
					(global-name "com.apple.containermanagerd.system")
					(global-name "com.apple.coreduetd.knowledge")
					(global-name "com.apple.coresymbolicationd")
					(global-name "com.apple.diagnosticservicesd")
					(global-name "com.apple.logd")
					(global-name "com.apple.lsd.advertisingidentifiers")
					(global-name "com.apple.lsd.mapdb")
					(global-name "com.apple.osanalytics.osanalyticshelper")
					(global-name "com.apple.runningboard")
					(global-name "com.apple.system.notification_center")
					(global-name "com.apple.timed.xpc")
					(global-name "com.apple.trial.status")
					(require-all
						(require-not (global-name "com.apple.CARenderServer"))
						(require-not (global-name "com.apple.mobileassetd.v2"))
						(require-not (global-name "com.apple.coremedia.mediaparserd.utilities"))
						(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
						(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
						(require-not (global-name "com.apple.system.logger"))
						(global-name "com.apple.analyticsd")
					)
					(require-any
						(global-name "com.apple.cfprefsd.daemon")
						(global-name "com.apple.cfprefsd.daemon.system")
					)
				)
			)
			(xpc-service-name "com.apple.ReportCrashService2")
		)
	)
)
(deny mach-lookup
	(with no-report)
	(require-all
		(require-not (global-name "com.apple.distributed_notifications@1v3"))
		(require-any
			(global-name "com.apple.analyticsagent")
			(global-name "com.apple.analyticsd")
			(global-name "com.apple.mobilegestalt.xpc")
			(require-all
				(require-not (global-name "com.apple.tailspind"))
				(require-any
					(global-name "com.apple.OTATaskingAgent")
					(global-name "com.apple.ReportMemoryException")
					(global-name "com.apple.biome.PublicStreamAccessService")
					(global-name "com.apple.biome.access.system")
					(global-name "com.apple.commcenter.coretelephony.xpc")
					(global-name "com.apple.commcenter.xpc")
					(global-name "com.apple.containermanagerd.system")
					(global-name "com.apple.coreduetd.knowledge")
					(global-name "com.apple.coresymbolicationd")
					(global-name "com.apple.diagnosticservicesd")
					(global-name "com.apple.logd")
					(global-name "com.apple.lsd.advertisingidentifiers")
					(global-name "com.apple.lsd.mapdb")
					(global-name "com.apple.osanalytics.osanalyticshelper")
					(global-name "com.apple.runningboard")
					(global-name "com.apple.system.notification_center")
					(global-name "com.apple.timed.xpc")
					(global-name "com.apple.trial.status")
					(require-all
						(require-not (global-name "com.apple.CARenderServer"))
						(require-not (global-name "com.apple.mobileassetd.v2"))
						(require-not (global-name "com.apple.coremedia.mediaparserd.utilities"))
						(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
						(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
						(require-not (global-name "com.apple.system.logger"))
						(global-name "com.apple.analyticsd")
					)
					(require-any
						(global-name "com.apple.cfprefsd.daemon")
						(global-name "com.apple.cfprefsd.daemon.system")
					)
				)
			)
			(xpc-service-name "com.apple.ReportCrashService2")
		)
	)
)
(deny mach-lookup
	(require-all
		(require-not (global-name "com.apple.distributed_notifications@1v3"))
		(require-any
			(global-name "com.apple.analyticsagent")
			(global-name "com.apple.analyticsd")
			(global-name "com.apple.mobilegestalt.xpc")
			(require-all
				(require-not (global-name "com.apple.tailspind"))
				(require-any
					(global-name "com.apple.OTATaskingAgent")
					(global-name "com.apple.ReportMemoryException")
					(global-name "com.apple.biome.PublicStreamAccessService")
					(global-name "com.apple.biome.access.system")
					(global-name "com.apple.commcenter.coretelephony.xpc")
					(global-name "com.apple.commcenter.xpc")
					(global-name "com.apple.containermanagerd.system")
					(global-name "com.apple.coreduetd.knowledge")
					(global-name "com.apple.coresymbolicationd")
					(global-name "com.apple.diagnosticservicesd")
					(global-name "com.apple.logd")
					(global-name "com.apple.lsd.advertisingidentifiers")
					(global-name "com.apple.lsd.mapdb")
					(global-name "com.apple.osanalytics.osanalyticshelper")
					(global-name "com.apple.runningboard")
					(global-name "com.apple.system.notification_center")
					(global-name "com.apple.timed.xpc")
					(global-name "com.apple.trial.status")
					(require-all
						(require-not (global-name "com.apple.CARenderServer"))
						(require-not (global-name "com.apple.mobileassetd.v2"))
						(require-not (global-name "com.apple.coremedia.mediaparserd.utilities"))
						(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
						(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
						(require-not (global-name "com.apple.system.logger"))
						(global-name "com.apple.analyticsd")
					)
					(require-any
						(global-name "com.apple.cfprefsd.daemon")
						(global-name "com.apple.cfprefsd.daemon.system")
					)
				)
			)
			(xpc-service-name "com.apple.ReportCrashService2")
		)
	)
)

(allow mach-task-inspect
	(target self)
)

(allow mach-task-name
	(target self)
)

(allow mach-task-read
	(target self)
)

(deny mach-task-special-port*)

(deny mach-task-special-port-get)
(allow mach-task-special-port-get
	(target self)
)

(deny mach-task-special-port-set)
(allow mach-task-special-port-set
	(require-all
		(task-special-port TASK_DEBUG_CONTROL_PORT)
		(target self)
	)
)
(deny mach-task-special-port-set)

(deny necp-client-open)

(deny network-outbound
	(with no-report)
	(literal "/private/var/run/syslog")
)
(deny network-outbound)

(deny nvram*)

(deny process-info*)

(allow process-info-codesignature)

(allow process-info-pidinfo)

(deny process-info-rusage)
(allow process-info-rusage
	(target self)
)

(allow process-info-sandbox-container)

(allow process-info-setcontrol)

(allow signal
	(target self)
)

(deny socket-ioctl)

(deny socket-option-get)

(deny socket-option-set)

(deny syscall-unix)
(allow syscall-unix
	(syscall-number
		SYS_exit
		SYS_read
		SYS_write
		SYS_open
		SYS_close
		SYS_unlink
		SYS_chmod
		SYS_chown
		SYS_getfsstat
		SYS_getpid
		SYS_getuid
		SYS_geteuid
		SYS_access
		SYS_chflags
		SYS_fchflags
		SYS_kill
		SYS_crossarch_trap
		SYS_dup
		SYS_getegid
		SYS_sigaction
		SYS_getgid
		SYS_ioctl
		SYS_umask
		SYS_munmap
		SYS_mprotect
		SYS_madvise
		SYS_fcntl
		SYS_sigsuspend
		SYS_writev
		SYS_fchown
		SYS_fchmod
		SYS_flock
		SYS_mkdir
		SYS_utimes
		SYS_futimes
		SYS_pread
		SYS_pwrite
		SYS_csops
		SYS_csops_audittoken
		SYS_kdebug_typefilter
		SYS_kdebug_trace_string
		SYS_kdebug_trace64
		SYS_pathconf
		SYS_getrlimit
		SYS_setrlimit
		SYS_mmap
		SYS_lseek
		SYS_sysctl
		SYS_getumask
		SYS_getattrlist
		SYS_getxattr
		SYS_fgetxattr
		SYS_setxattr
		SYS_fsetxattr
		SYS_removexattr
		SYS_fremovexattr
		SYS_shm_open
		SYS_sysctlbyname
		SYS_chmod_extended
		SYS_fchmod_extended
		SYS_gettid
		SYS_shared_region_check_np
		SYS_psynch_mutexwait
		SYS_psynch_mutexdrop
		SYS_psynch_cvsignal
		SYS_psynch_cvwait
		SYS_iopolicysys
		SYS_issetugid
		SYS___pthread_kill
		SYS___pthread_sigmask
		SYS___disable_threadsignal
		SYS___semwait_signal
		SYS_proc_info
		SYS_stat64
		SYS_fstat64
		SYS_lstat64
		SYS_getdirentries64
		SYS_statfs64
		SYS_getfsstat64
		SYS_bsdthread_create
		SYS_bsdthread_terminate
		SYS_lchown
		SYS_bsdthread_register
		SYS_workq_open
		SYS_workq_kernreturn
		SYS_thread_selfid
		SYS_kevent_qos
		SYS_kevent_id
		SYS___mac_syscall
		SYS_read_nocancel
		SYS_write_nocancel
		SYS_open_nocancel
		SYS_close_nocancel
		SYS_fcntl_nocancel
		SYS_sigsuspend_nocancel
		SYS_writev_nocancel
		SYS_pread_nocancel
		SYS_pwrite_nocancel
		SYS___semwait_signal_nocancel
		SYS_fsgetpath
		SYS_fileport_makefd
		SYS_memorystatus_control
		SYS_openat
		SYS_openat_nocancel
		SYS_fchmodat
		SYS_fchownat
		SYS_fstatat
		SYS_fstatat64
		SYS_unlinkat
		SYS_bsdthread_ctl
		SYS_stack_snapshot_with_config
		SYS_persona
		SYS_getentropy
		SYS_ulock_wait
		SYS_ulock_wake
		SYS_terminate_with_payload
		SYS_abort_with_payload
		SYS_pwritev
		SYS_pwritev_nocancel
		SYS_ulock_wait2
		SYS_proc_info_extended_id
		SYS_map_with_linking_np)
)

(deny syscall-mach)
(allow syscall-mach
	(machtrap-number
		MSC__kernelrpc_mach_vm_allocate_trap
		MSC__kernelrpc_mach_vm_purgable_control_trap
		MSC__kernelrpc_mach_vm_deallocate_trap
		MSC__kernelrpc_mach_vm_protect_trap
		MSC__kernelrpc_mach_vm_map_trap
		MSC__kernelrpc_mach_port_allocate_trap
		MSC__kernelrpc_mach_port_deallocate_trap
		MSC__kernelrpc_mach_port_mod_refs_trap
		MSC__kernelrpc_mach_port_insert_right_trap
		MSC__kernelrpc_mach_port_insert_member_trap
		MSC__kernelrpc_mach_port_extract_member_trap
		MSC__kernelrpc_mach_port_construct_trap
		MSC__kernelrpc_mach_port_destruct_trap
		MSC_mach_reply_port
		MSC_task_self_trap
		MSC_host_self_trap
		MSC_semaphore_signal_trap
		MSC_semaphore_wait_trap
		MSC_semaphore_timedwait_trap
		MSC__kernelrpc_mach_port_guard_trap
		MSC_mach_generate_activity_id
		MSC_pid_for_task
		MSC_mach_msg2_trap
		MSC_thread_get_special_reply_port
		MSC_host_create_mach_voucher_trap
		MSC__kernelrpc_mach_port_type_trap
		MSC__kernelrpc_mach_port_request_notification_trap
		MSC_mach_timebase_info_trap
		MSC_mk_timer_create
		MSC_iokit_user_client_trap)
)

(allow sysctl*
	(require-any
		(sysctl-name "vm.get_owned_vmobjects")
		(sysctl-name "vm.self_region_footprint")
		(sysctl-name "vm.self_region_page_size")
	)
)

(allow sysctl-read
	(require-all
		(require-not (sysctl-name "kern.bootargs"))
		(require-not (sysctl-name "kern.bootsessionuuid"))
		(require-not (sysctl-name "vm.footprint_suspend"))
		(require-any
			(require-any
				(sysctl-name "hw.activecpu")
				(sysctl-name "hw.machine")
				(sysctl-name "hw.memsize")
				(sysctl-name "hw.ncpu")
				(sysctl-name "kern.osproductversion")
				(sysctl-name "kern.osvariant_status")
				(sysctl-name "kern.secure_kernel")
			)
			(require-any
				(sysctl-name "hw.cachelinesize")
				(sysctl-name "hw.cpufamily")
				(sysctl-name "hw.l2cachesize")
				(sysctl-name "hw.perflevel*")
				(sysctl-name "kern.hv_vmm_present")
			)
			(require-any
				(sysctl-name "hw.logicalcpu")
				(sysctl-name "hw.nperflevels")
				(sysctl-name "sysctl.name2oid")
			)
			(require-any
				(sysctl-name "hw.logicalcpu_max")
				(sysctl-name "hw.model")
				(sysctl-name "hw.physicalcpu_max")
				(sysctl-name "hw.product")
			)
			(require-any
				(sysctl-name "hw.optional.arm.FEAT_FPACCOMBINE")
				(sysctl-name "hw.optional.arm.FEAT_MTE4")
				(sysctl-name "kern.argmax")
				(sysctl-name "kern.roots_installed")
				(sysctl-name "kern.wq_max_constrained_threads")
				(sysctl-name "kern.wq_max_threads")
				(sysctl-name "security.codesigning.monitor")
			)
			(require-any
				(sysctl-name "hw.optional.arm.caps")
				(sysctl-name "hw.optional.neon_fp16")
			)
			(require-any
				(sysctl-name "kern.maxfilesperproc")
				(sysctl-name "kern.osversion")
			)
			(require-any
				(sysctl-name "machdep.virtual_address_size")
				(sysctl-name "security.mac.amfi.developer_mode_status")
			)
			(require-any
				(sysctl-name "vm.get_owned_vmobjects")
				(sysctl-name "vm.self_region_footprint")
			)
			(sysctl-name "hw.osenvironment")
			(sysctl-name "hw.pagesize_compat")
			(sysctl-name "hw.physicalcpu")
			(sysctl-name "hw.target")
			(sysctl-name "kern.proc.pid.*")
			(sysctl-name "kern.procargs2.*")
			(sysctl-name "machdep.ptrauth_enabled")
			(sysctl-name "security.mac.lockdown_mode_state")
			(sysctl-name "vm.malloc_ranges")
		)
	)
)

(deny system-fcntl)
(allow system-fcntl
	(fcntl-command
		F_GETFD
		F_SETFD
		F_NOCACHE
		F_GETPATH
		F_GETPROTECTIONCLASS
		F_SETPROTECTIONCLASS
		F_DUPFD_CLOEXEC
		F_ADDFILESIGS_RETURN
		F_CHECK_LV
		F_SPECULATIVE_READ)
)

(allow system-info
	(info-type "vfs.disk-space")
)

(deny system-memorystatus-control)
(allow system-memorystatus-control
	(memorystatus-control-command MEMORYSTATUS_CMD_INCREASE_JETSAM_TASK_LIMIT)
)

(deny system-necp-client-action)

(allow user-preference-read
	(require-any
		(preference-domain "com.apple.ReportCrash")
		(preference-domain "com.apple.ReportCrashService")
		(preference-domain "com.apple.da")
		(preference-domain "com.apple.gms.availability")
		(preference-domain "com.apple.metrickitd")
		(preference-domain "com.apple.osanalytics")
		(preference-domain "com.apple.osanalytics.OTATaskingAgent")
		(preference-domain "com.apple.triald")
		(preference-domain "kCFPreferencesAnyApplication")
	)
)

(allow managed-preference-read
	(require-any
		(preference-domain "com.apple.ReportCrash")
		(preference-domain "com.apple.ReportCrashService")
		(preference-domain "com.apple.da")
		(preference-domain "com.apple.gms.availability")
		(preference-domain "com.apple.metrickitd")
		(preference-domain "com.apple.osanalytics")
		(preference-domain "com.apple.osanalytics.OTATaskingAgent")
		(preference-domain "com.apple.triald")
		(preference-domain "kCFPreferencesAnyApplication")
	)
)

(allow user-preference-write
	(require-any
		(preference-domain "com.apple.ReportCrash")
		(preference-domain "com.apple.ReportCrashService")
	)
)
```
