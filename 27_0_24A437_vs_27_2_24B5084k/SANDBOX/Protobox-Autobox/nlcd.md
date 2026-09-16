## nlcd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (system-attribute developer-mode))

 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command
+		SIOCGIFCONSTRAINED
+		SIOCGIFDELEGATE
+		SIOCGIFEXPENSIVE
+		SIOCGIFFLAGS
+		SIOCGIFFUNCTIONALTYPE
 		SIOCGIFLINKPARAMS
+		SIOCGIFLINKQUALITYMETRIC
+		SIOCGIFMTU
 		SIOCGIFNOTRAFFICSHAPING
 		SIOCGIFTYPE
+		SIOCGIFULTRACONSTRAINED
 		SIOCSIFLINKPARAMS)
 )
 

 		SYS_ulock_wake
 		SYS_terminate_with_payload
 		SYS_abort_with_payload
+		SYS_necp_session_open
+		SYS_necp_session_action
 		SYS_setattrlistat
 		SYS_os_fault_with_payload
 		SYS_kqueue_workloop_ctl

 )
 
 (deny system-necp-client-action)
+(allow system-necp-client-action
+	(necp-client-action
+		NECP_CLIENT_ACTION_ADD
+		NECP_CLIENT_ACTION_ADD_FLOW
+		NECP_CLIENT_ACTION_CLAIM
+		NECP_CLIENT_ACTION_COPY_AGENT
+		NECP_CLIENT_ACTION_COPY_INTERFACE
+		NECP_CLIENT_ACTION_COPY_PARAMETERS
+		NECP_CLIENT_ACTION_COPY_RESULT
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_REMOVE)
+)
 
 (allow process-exec-update-label)
```
