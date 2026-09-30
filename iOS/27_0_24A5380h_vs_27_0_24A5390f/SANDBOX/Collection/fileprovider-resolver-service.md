## fileprovider-resolver-service

> Group: ⬆️ Updated

```diff

 
 (allow fs-info)
 
-(deny iokit-open-user-client
+(deny iokit-open*
 	(iokit-registry-entry-class "*")
 )
 
-(allow ipc-posix-sem*
+(allow ipc-posix*
 	(extension "com.apple.sandbox.application-group")
 )
 
 (allow ipc-posix-shm*
 	(extension "com.apple.sandbox.application-group")
 )
-
-(allow ipc-posix-shm-read-data
-	(extension "com.apple.sandbox.application-group")
-)
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(ipc-posix-name "apple.shm.notification_center")
 		(%entitlement-is-bool-true "com.apple.security.on-demand-install-capable")
 	)
 )
 
-(deny job-creation)
+(deny isp-command-send)
 
-(deny lsopen
+(deny job-creation
 	(profile-flag "deny-lsopen")
 )
 
-(allow mach-derive-port)
+(allow mach-cross-domain-lookup)
 
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.FileProviderResolver.Service")
 		(signing-identifier "com.apple.FileProviderResolver.TestingHarness")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.backboard.display.services")
 		(signing-identifier "com.apple.FileProviderResolver.TestingHarness")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(extension "com.apple.sandbox.application-group")
 		(global-name "com.apple.FileProvider")

 		(global-name "com.apple.system.notification_center")
 	)
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-any
 		(global-name "*")
 		(xpc-service-name "*")
 	)
 )
 
-(allow mach-register
+(allow mach-priv-task-port
 	(extension "com.apple.sandbox.application-group")
 )
 
-(allow mach-task-exception-port-set)
+(allow mach-task*)
+
+(allow mach-task-exception-port-set
+	(target self)
+)
 
 (allow mach-task-inspect
 	(target self)

 	(target self)
 )
 
-(allow mach-task-read
-	(target self)
-)
-
-(allow mach-task-special-port*)
-
-(allow necp-client-open)
-
-(allow network-inbound
+(allow network*
 	(require-all
 		(extension "com.apple.sandbox.application-group")
 		(require-any

 )
 
 (allow network-bind
-	(require-all
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-				(subpath "${FRONT_USER_HOME}")
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-		)
-	)
-)
-
-(allow network-outbound
 	(control-name "com.apple.flow-divert")
 )
-(allow network-outbound
+(allow network-bind
 	(require-all
 		(extension "com.apple.sandbox.application-group")
 		(require-any

 	)
 )
 
-(allow process-codesigning)
-
-(allow process-info-codesignature)
-
-(allow process-info-pidinfo)
-
-(allow process-iopolicy*)
+(allow process*)
 
 (allow sandbox-check)
 

 (allow system-privilege)
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
