## IntelligentRoutingDaemonLLMService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.modelmanager"))
 		(require-not (global-name "com.apple.modelcatalog.catalog"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))

 (deny process-exec*)
 
 (deny socket-ioctl)
+(allow socket-ioctl
+	(ioctl-command CTLIOCGINFO)
+)
 
 (deny syscall-unix)
 (allow syscall-unix

 		SYS_getuid
 		SYS_geteuid
 		SYS_sendmsg
+		SYS_recvfrom
 		SYS_access
 		SYS_crossarch_trap
 		SYS_dup

 		SYS_fcntl
 		SYS_socket
 		SYS_connect
+		SYS_setsockopt
 		SYS_sigsuspend
 		SYS_gettimeofday
+		SYS_getsockopt
 		SYS_readv
 		SYS_writev
 		SYS_sendto

 		SYS_open_nocancel
 		SYS_close_nocancel
 		SYS_sendmsg_nocancel
+		SYS_recvfrom_nocancel
 		SYS_fcntl_nocancel
+		SYS_select_nocancel
 		SYS_connect_nocancel
 		SYS_sigsuspend_nocancel
 		SYS_readv_nocancel

 		SYS_fsgetpath
 		SYS_memorystatus_control
 		SYS_guarded_close_np
+		SYS_change_fdguard_np
 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat

 		SYS_guarded_writev_np
 		SYS_persona
 		SYS_getentropy
+		SYS_necp_open
+		SYS_necp_client_action
+		SYS___nexus_set_opt
+		SYS___channel_open
+		SYS___channel_get_info
+		SYS___channel_sync
 		SYS_ulock_wait
 		SYS_ulock_wake
 		SYS_terminate_with_payload

 		MSC_mach_reply_port
 		MSC_task_self_trap
 		MSC_host_self_trap
+		MSC_semaphore_signal_trap
+		MSC_semaphore_wait_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_mach_msg2_trap

 		task_get_special_port_from_user
 		task_set_special_port
 		semaphore_create
+		semaphore_destroy
 		task_set_exc_guard_behavior
 		task_create_identity_token
+		thread_policy
 		vm_remap_external
 		vm_reallocate
 		mach_vm_copy

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_SETFD
 		F_GETFL
+		F_SETFL
 		F_RDADVISE
 		F_GETPATH
 		F_GETPROTECTIONCLASS

 )
 
 (deny system-necp-client-action)
+(allow system-necp-client-action
+	(necp-client-action
+		NECP_CLIENT_ACTION_ADD
+		NECP_CLIENT_ACTION_ADD_FLOW
+		NECP_CLIENT_ACTION_COPY_AGENT
+		NECP_CLIENT_ACTION_COPY_INTERFACE
+		NECP_CLIENT_ACTION_COPY_RESULT
+		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_MAP_SYSCTLS
+		NECP_CLIENT_ACTION_REMOVE
+		NECP_CLIENT_ACTION_REMOVE_FLOW
+		NECP_CLIENT_ACTION_UPDATE_CACHE)
+)
 
 (allow process-exec-update-label)
```
