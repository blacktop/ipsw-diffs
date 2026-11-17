## amsaccountsd

> Group: ⬆️ Updated

```diff

 		SYS_pwrite_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
+		SYS_fileport_makeport
 		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_open_np

 		SYS_fstatat64
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_thread_selfusage
 		SYS_csrctl
 		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np

 (deny system-necp-client-action)
 (allow system-necp-client-action
 	(necp-client-action
+		28
 		NECP_CLIENT_ACTION_ACQUIRE_AGENT_TOKEN
 		NECP_CLIENT_ACTION_ADD
 		NECP_CLIENT_ACTION_ADD_FLOW
```
