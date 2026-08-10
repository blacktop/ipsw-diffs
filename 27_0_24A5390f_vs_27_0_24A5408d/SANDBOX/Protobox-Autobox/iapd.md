## iapd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.mobileipod.gsEvents"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.carkit.app.service"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))

 		SYS_sendto
 		SYS_socketpair
 		SYS_mkdir
+		SYS_rmdir
 		SYS_pread
 		SYS_pwrite
 		SYS_statfs

 		SYS_guarded_writev_np
 		SYS_persona
 		SYS_getentropy
+		SYS_necp_open
+		SYS_necp_client_action
 		SYS_ulock_wait
 		SYS_ulock_wake
 		SYS_terminate_with_payload

 )
 
 (deny system-necp-client-action)
+(allow system-necp-client-action
+	(necp-client-action NECP_CLIENT_ACTION_ADD)
+)
 
 (allow process-exec-update-label)
```
