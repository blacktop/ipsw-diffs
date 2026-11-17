## featureaccessd

> Group: ⬆️ Updated

```diff

 			SYS_lseek
 			SYS_sysctl
 			SYS_getumask
+			SYS_open_dprotected_np
+			SYS_openat_dprotected_np
 			SYS_fgetattrlist
 			SYS_fsctl
 			SYS_sysctlbyname

 			SYS_fstatat
 			SYS_fstatat64
 			SYS_mkdirat
+			SYS_guarded_open_dprotected_np
 			SYS_persona
 			SYS_necp_open
 			SYS_necp_client_action

 (deny system-necp-client-action)
 (allow system-necp-client-action
 	(necp-client-action
+		28
 		NECP_CLIENT_ACTION_ACQUIRE_AGENT_TOKEN
 		NECP_CLIENT_ACTION_ADD
 		NECP_CLIENT_ACTION_ADD_FLOW
```
