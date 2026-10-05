## pcapd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.pcapd-local"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.nehelper"))
+		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.aggregated"))

 		SYS_writev
 		SYS_rename
 		SYS_sendto
+		SYS_shutdown
 		SYS_socketpair
 		SYS_mkdir
 		SYS_pread

 		NECP_CLIENT_ACTION_COPY_AGENT
 		NECP_CLIENT_ACTION_COPY_INTERFACE
 		NECP_CLIENT_ACTION_COPY_RESULT
+		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
-		NECP_CLIENT_ACTION_REMOVE)
+		NECP_CLIENT_ACTION_REMOVE
+		NECP_CLIENT_ACTION_REMOVE_FLOW)
 )
```
