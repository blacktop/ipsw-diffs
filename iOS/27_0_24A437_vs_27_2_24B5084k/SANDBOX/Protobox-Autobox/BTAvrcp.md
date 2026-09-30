## BTAvrcp

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
+		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.mediaremoted.xpc"))

 		F_GETFD
 		F_SETFD
 		F_GETFL
+		F_RDADVISE
 		F_NOCACHE
 		F_GETPATH
 		F_GETPROTECTIONCLASS

 )
 
 (deny system-necp-client-action)
+(allow system-necp-client-action
+	(necp-client-action
+		NECP_CLIENT_ACTION_ADD
+		NECP_CLIENT_ACTION_ADD_FLOW
+		NECP_CLIENT_ACTION_COPY_AGENT
+		NECP_CLIENT_ACTION_COPY_INTERFACE
+		NECP_CLIENT_ACTION_COPY_RESULT
+		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_REMOVE)
+)
 
 (allow process-exec-update-label)
```
