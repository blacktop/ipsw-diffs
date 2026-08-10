## navd

> Group: ⬆️ Updated

```diff

 		SYS_getpid
 		SYS_getuid
 		SYS_geteuid
+		SYS_recvmsg
 		SYS_sendmsg
+		SYS_recvfrom
 		SYS_access
 		SYS_crossarch_trap
 		SYS_dup

 		SYS_madvise
 		SYS_dup2
 		SYS_fcntl
+		SYS_select
 		SYS_fsync
 		SYS_socket
 		SYS_connect

 		SYS_kevent_qos
 		SYS_kevent_id
 		SYS___mac_syscall
+		SYS_pselect
+		SYS_pselect_nocancel
 		SYS_read_nocancel
 		SYS_write_nocancel
 		SYS_open_nocancel
 		SYS_close_nocancel
+		SYS_recvmsg_nocancel
 		SYS_sendmsg_nocancel
+		SYS_recvfrom_nocancel
 		SYS_fcntl_nocancel
+		SYS_select_nocancel
 		SYS_fsync_nocancel
 		SYS_connect_nocancel
 		SYS_sigsuspend_nocancel

 		SYS_getentropy
 		SYS_necp_open
 		SYS_necp_client_action
+		SYS___nexus_set_opt
 		SYS_ulock_wait
 		SYS_ulock_wake
 		SYS_terminate_with_payload

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_SETFD
 		F_GETFL
 		F_SETFL

 		F_SINGLE_WRITER
 		F_OFD_SETLK
 		F_OFD_GETLK
+		F_OFD_SETLKWTIMEOUT
 		F_SETCONFINED
 		F_GETCONFINED
 		F_ADDFILESIGS_RETURN

 	(necp-client-action
 		NECP_CLIENT_ACTION_ADD
 		NECP_CLIENT_ACTION_ADD_FLOW
+		NECP_CLIENT_ACTION_AGENT
 		NECP_CLIENT_ACTION_COPY_AGENT
 		NECP_CLIENT_ACTION_COPY_INTERFACE
 		NECP_CLIENT_ACTION_COPY_RESULT
 		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
-		NECP_CLIENT_ACTION_REMOVE)
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT_FINAL
+		NECP_CLIENT_ACTION_MAP_SYSCTLS
+		NECP_CLIENT_ACTION_REMOVE
+		NECP_CLIENT_ACTION_REMOVE_FLOW)
 )
 
 (allow process-exec-update-label)
```
