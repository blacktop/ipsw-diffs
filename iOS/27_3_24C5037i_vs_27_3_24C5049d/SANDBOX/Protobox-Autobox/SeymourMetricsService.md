## SeymourMetricsService

> Group: ⬆️ Updated

```diff

 			SYS_fstatat
 			SYS_fstatat64
 			SYS_mkdirat
+			SYS_thread_selfusage
 			SYS_guarded_open_dprotected_np
 			SYS_guarded_write_np
 			SYS_guarded_pwrite_np

 (deny system-necp-client-action)
 (allow system-necp-client-action
 	(necp-client-action
+		28
 		NECP_CLIENT_ACTION_ACQUIRE_AGENT_TOKEN
 		NECP_CLIENT_ACTION_ADD
 		NECP_CLIENT_ACTION_ADD_FLOW
```
