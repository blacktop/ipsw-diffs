## ScreenTimeAgent

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
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "IOSurfaceRoot")
 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
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
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command

 		SYS_preadv_nocancel
 		SYS_pwritev_nocancel
 		SYS_ulock_wait2
+		SYS_proc_info_extended_id
 		SYS_map_with_linking_np)
 )
 

 		MSC__kernelrpc_mach_port_get_attributes_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
+		MSC_task_name_for_pid
 		MSC_pid_for_task
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port

 		NECP_CLIENT_ACTION_COPY_RESULT
 		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT_FINAL
 		NECP_CLIENT_ACTION_MAP_SYSCTLS
 		NECP_CLIENT_ACTION_REMOVE
 		NECP_CLIENT_ACTION_REMOVE_FLOW
```
