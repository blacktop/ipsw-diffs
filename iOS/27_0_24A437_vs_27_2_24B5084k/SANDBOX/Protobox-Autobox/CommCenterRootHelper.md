## CommCenterRootHelper

> Group: ⬆️ Updated

```diff

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

 		MSC__kernelrpc_mach_port_request_notification_trap
 		MSC_mach_timebase_info_trap
 		MSC_mk_timer_create
+		MSC_mk_timer_destroy
 		MSC_debug_control_port_for_pid)
 )
 

 		F_GETFD
 		F_SETFD
 		F_GETFL
+		F_SETFL
 		F_PREALLOCATE
 		F_GETPATH
+		F_GETPROTECTIONCLASS
 		F_ADDFILESIGS_RETURN
 		F_CHECK_LV)
 )

 	(necp-client-action
 		NECP_CLIENT_ACTION_ADD
 		NECP_CLIENT_ACTION_ADD_FLOW
+		NECP_CLIENT_ACTION_AGENT
 		NECP_CLIENT_ACTION_COPY_AGENT
 		NECP_CLIENT_ACTION_COPY_INTERFACE
 		NECP_CLIENT_ACTION_COPY_RESULT

 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
 		NECP_CLIENT_ACTION_MAP_SYSCTLS
 		NECP_CLIENT_ACTION_REMOVE
+		NECP_CLIENT_ACTION_REMOVE_FLOW
 		NECP_CLIENT_ACTION_UPDATE_CACHE)
 )
 
```
