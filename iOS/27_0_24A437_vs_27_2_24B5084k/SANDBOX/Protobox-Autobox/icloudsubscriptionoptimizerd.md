## icloudsubscriptionoptimizerd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.storekitd"))
 		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))

 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.itunesstored.xpc"))
 		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.UsageTrackingAgent.private"))

 (deny process-exec*)
 
 (deny socket-ioctl)
+(allow socket-ioctl
+	(ioctl-command
+		CTLIOCGINFO
+		SIOCGIFCONSTRAINED
+		SIOCGIFDELEGATE
+		SIOCGIFEXPENSIVE
+		SIOCGIFFLAGS
+		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
+		SIOCGIFMTU
+		SIOCGIFULTRACONSTRAINED)
+)
 
 (deny syscall-unix)
 (allow syscall-unix

 		SYS_getuid
 		SYS_geteuid
 		SYS_sendmsg
+		SYS_recvfrom
 		SYS_access
 		SYS_chflags
 		SYS_fchflags

 		SYS_getentropy
 		SYS_necp_open
 		SYS_necp_client_action
+		SYS___nexus_set_opt
 		SYS___channel_open
 		SYS_ulock_wait
 		SYS_ulock_wake

 		semaphore_destroy
 		task_set_exc_guard_behavior
 		task_create_identity_token
+		thread_policy
 		vm_remap_external
 		vm_reallocate
 		mach_vm_copy

 		F_GETFD
 		F_SETFD
 		F_GETFL
+		F_SETFL
 		F_NOCACHE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
 		F_DUPFD_CLOEXEC
+		F_BARRIERFSYNC
 		F_OFD_GETLK
 		F_ADDFILESIGS_RETURN
 		F_CHECK_LV)

 
 (deny system-necp-client-action)
 (allow system-necp-client-action
-	(necp-client-action NECP_CLIENT_ACTION_ADD)
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
 )
 
 (allow process-exec-update-label)
```
