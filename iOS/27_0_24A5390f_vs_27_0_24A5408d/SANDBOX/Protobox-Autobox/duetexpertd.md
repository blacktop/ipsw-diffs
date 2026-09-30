## duetexpertd

> Group: ⬆️ Updated

```diff

 		SYS_listxattr
 		SYS_flistxattr
 		SYS_fsctl
+		SYS_posix_spawn
 		SYS_ffsctl
 		SYS_shm_open
 		SYS_sysctlbyname

 (allow system-necp-client-action
 	(necp-client-action
 		NECP_CLIENT_ACTION_ADD
+		NECP_CLIENT_ACTION_ADD_FLOW
 		NECP_CLIENT_ACTION_COPY_AGENT
 		NECP_CLIENT_ACTION_COPY_INTERFACE
 		NECP_CLIENT_ACTION_COPY_RESULT
+		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
 		NECP_CLIENT_ACTION_REMOVE)
 )
```
