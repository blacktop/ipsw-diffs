## nanotimekitcompaniond

> Group: ⬆️ Updated

```diff

 (deny process-exec*)
 
 (deny socket-ioctl)
+(allow socket-ioctl
+	(ioctl-command CTLIOCGINFO)
+)
 
 (deny syscall-unix)
 (allow syscall-unix

 		SYS_clonefileat
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64

 		SYS_getentropy
 		SYS_necp_open
 		SYS_necp_client_action
+		SYS___nexus_set_opt
 		SYS_ulock_wait
 		SYS_ulock_wake
 		SYS_terminate_with_payload

 		semaphore_destroy
 		task_set_exc_guard_behavior
 		task_create_identity_token
+		thread_policy
 		thread_policy_set
 		vm_remap_external
 		vm_reallocate

 		NECP_CLIENT_ACTION_COPY_AGENT
 		NECP_CLIENT_ACTION_COPY_INTERFACE
 		NECP_CLIENT_ACTION_COPY_RESULT
+		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_MAP_SYSCTLS
 		NECP_CLIENT_ACTION_REMOVE
 		NECP_CLIENT_ACTION_REMOVE_FLOW)
 )
```
