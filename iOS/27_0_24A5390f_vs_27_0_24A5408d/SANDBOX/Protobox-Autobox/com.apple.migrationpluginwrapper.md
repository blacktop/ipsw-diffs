## com.apple.migrationpluginwrapper

> Group: ⬆️ Updated

```diff

 		(require-not (require-any
 			(global-name "com.apple.Safari.History.Service")
 			(global-name "com.apple.SafariBookmarksSyncAgent.TabGroups")
+			(global-name "com.apple.appmanagedfeatures.configuration")
 			(global-name "com.apple.atc.xpc.sessions")
 			(global-name "com.apple.safefinancing.activation")
 			(global-name "com.apple.syncdefaultsd")

 		(require-not (global-name "com.apple.securityd.general"))
 		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
+		(require-not (global-name "com.apple.ManagedSettingsAgent"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.coremedia.admin"))
+		(require-not (global-name "com.apple.DeviceConfigurationAgent.consumer"))
 		(require-not (global-name "com.apple.amfi.xpc"))
 		(require-not (global-name "com.apple.coremedia.endpoint.xpc"))
 		(require-not (global-name "com.apple.SBUserNotification"))

 		NECP_CLIENT_ACTION_COPY_RESULT
 		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT_FINAL
 		NECP_CLIENT_ACTION_MAP_SYSCTLS
 		NECP_CLIENT_ACTION_REMOVE
 		NECP_CLIENT_ACTION_REMOVE_FLOW
```
