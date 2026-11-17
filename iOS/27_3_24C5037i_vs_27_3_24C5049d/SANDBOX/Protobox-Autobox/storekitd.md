## storekitd

> Group: ⬆️ Updated

```diff

 		(require-not (xpc-service-name "com.apple.extensionkitservice"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon"))

 		SYS_fstatat64
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_thread_selfusage
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
