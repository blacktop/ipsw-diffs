## com.apple.PerformanceTrace.PerformanceTraceService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.logd.admin"))
-		(require-not (global-name "com.apple.geod"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.coresymbolicationd"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.geod"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
+		(require-not (global-name "com.apple.logd.admin"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (system-attribute developer-mode))

 )
 
 (deny process-exec*)
+(allow process-exec*
+	(literal "/bin/sh")
+)
 
 (deny socket-ioctl)
 

 		SYS_kill
 		SYS_crossarch_trap
 		SYS_dup
+		SYS_pipe
 		SYS_getegid
 		SYS_sigaction
 		SYS_getgid

 		SYS_listxattr
 		SYS_flistxattr
 		SYS_fsctl
+		SYS_posix_spawn
 		SYS_ffsctl
 		SYS_shm_open
 		SYS_sysctlbyname

 		SYS_write_nocancel
 		SYS_open_nocancel
 		SYS_close_nocancel
+		SYS_wait4_nocancel
 		SYS_sendmsg_nocancel
 		SYS_fcntl_nocancel
 		SYS_fsync_nocancel

 		MSC_semaphore_signal_trap
 		MSC_semaphore_wait_trap
 		MSC_semaphore_timedwait_trap
+		MSC__kernelrpc_mach_port_get_attributes_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_task_name_for_pid

 		io_connect_map_memory_into_task
 		io_connect_unmap_memory_from_task
 		io_connect_method
+		io_connect_set_notification_port_64
 		io_service_add_interest_notification_64
 		io_registry_entry_get_registry_entry_id
 		io_server_version

 		task_set_special_port
 		semaphore_create
 		semaphore_destroy
+		task_policy_get
 		task_suspend2
 		task_resume2
 		task_map_corpse_info_64
+		thread_info
 		thread_set_exception_ports
 		vm_copy
 		vm_read_overwrite

 			(sysctl-name "kperf.sampling")
 			(sysctl-name "kperf.timer.count")
 		))
-		(require-not (sysctl-name "kperf.lazy.cpu_action"))
-		(require-not (sysctl-name "kpc.force_all_ctrs"))
 		(require-not (require-any
 			(sysctl-name "kpc.period")
 			(sysctl-name "kperf.action.filter_by_pid")

 			(sysctl-name "kperf.timer.action")
 			(sysctl-name "kperf.timer.period")
 		))
+		(require-not (sysctl-name "kperf.lazy.cpu_action"))
+		(require-not (sysctl-name "kpc.force_all_ctrs"))
 		(require-not (require-any
 			(sysctl-name "kpc.actionid")
 			(sysctl-name "kpc.config")

 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_DUPFD_CLOEXEC
+		F_SETSTATICCONTENT
+		F_SET_GREEDY_MODE
 		F_ADDFILESIGS_RETURN
 		F_CHECK_LV)
 )

 
 (deny system-kas-info)
 (allow system-kas-info
-	(kas-info-selector KAS_INFO_KERNEL_TEXT_SLIDE_SELECTOR)
+	(kas-info-selector
+		KAS_INFO_KERNEL_TEXT_SLIDE_SELECTOR
+		KAS_INFO_SPTM_TEXT_SLIDE_SELECTOR
+		KAS_INFO_TXM_TEXT_SLIDE_SELECTOR)
 )
 
 (with-filter (mac-policy-name "Sandbox")

 )
 
 (deny system-necp-client-action)
-
-(allow process-exec-update-label)
```
