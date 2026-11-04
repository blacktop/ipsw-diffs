## terminusd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.identityservicesd.nsxpc"))
 		(require-not (global-name "com.apple.locationd.registration"))
-		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
 		(require-not (global-name "com.apple.terminusd"))
 		(require-not (global-name "com.apple.logd.events"))

 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.server.bluetooth.le.pipe.xpc"))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (deny system-mac-syscall
 	(require-all
 		(mac-syscall-number 1)

 (deny system-necp-client-action)
 (allow system-necp-client-action
 	(necp-client-action
+		29
+		NECP_CLIENT_ACTION_ACQUIRE_AGENT_TOKEN
 		NECP_CLIENT_ACTION_ADD
-		NECP_CLIENT_ACTION_REMOVE
-		NECP_CLIENT_ACTION_COPY_PARAMETERS
-		NECP_CLIENT_ACTION_COPY_RESULT
+		NECP_CLIENT_ACTION_ADD_FLOW
 		NECP_CLIENT_ACTION_AGENT
 		NECP_CLIENT_ACTION_COPY_AGENT
 		NECP_CLIENT_ACTION_COPY_INTERFACE
+		NECP_CLIENT_ACTION_COPY_PARAMETERS
+		NECP_CLIENT_ACTION_COPY_RESULT
 		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
-		NECP_CLIENT_ACTION_MAP_SYSCTLS
-		NECP_CLIENT_ACTION_UPDATE_CACHE
 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
-		NECP_CLIENT_ACTION_ADD_FLOW
-		NECP_CLIENT_ACTION_REMOVE_FLOW
-		NECP_CLIENT_ACTION_GET_INTERFACE_ADDRESS
-		NECP_CLIENT_ACTION_ACQUIRE_AGENT_TOKEN
 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT_FINAL
-		29)
+		NECP_CLIENT_ACTION_GET_INTERFACE_ADDRESS
+		NECP_CLIENT_ACTION_MAP_SYSCTLS
+		NECP_CLIENT_ACTION_REMOVE
+		NECP_CLIENT_ACTION_REMOVE_FLOW
+		NECP_CLIENT_ACTION_UPDATE_CACHE)
 )
 
 (allow process-exec-update-label)
```
