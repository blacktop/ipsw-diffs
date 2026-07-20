## appsso

> Group: ⬆️ Updated

```diff

 
 (allow fs-snapshot-mount)
 
-(allow iokit-get-properties)
+(allow iokit*)
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(extension "com.apple.security.exception.iokit-user-client-class")
 )
 
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(%entitlement-is-present "com.apple.security.exception.iokit-user-client-class")
 )
 
-(allow ipc-posix-shm*
+(allow ipc-posix-sem-wait
 	(ipc-posix-name "/com.apple.AppSSO.version")
 )
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(ipc-posix-name "apple.shm.notification_center")
 		(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
 	)
 )
+(allow ipc-posix-shm*
+	(ipc-posix-name "/com.apple.AppSSO.version")
+)
+
 (allow ipc-posix-shm-read-data
 	(ipc-posix-name "/com.apple.AppSSO.version")
 )
 
-(deny job-creation)
+(allow ipc-posix-shm-write*
+	(ipc-posix-name "/com.apple.AppSSO.version")
+)
 
-(deny lsopen
+(deny isp-command-send)
+
+(deny job-creation
 	(profile-flag "deny-lsopen")
 )
 
-(allow mach-bootstrap)
+(allow mach*)
 
-(allow mach-cross-domain-lookup)
-
-(allow mach-derive-port)
-
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.system.notification_center")
 		(%entitlement-is-bool-true "com.apple.security.on-demand-install-capable")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")

 		(global-name "com.apple.trustd")
 	)
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-any
 		(xpc-service-name "com.apple.CoreGraphics.CGPDFService")
 		(xpc-service-name "com.apple.WebKit.*")
 	)
 )
 
-(allow mach-register
+(allow mach-priv-task-port
 	(extension "com.apple.security.exception.mach-register.global-name")
 )
 
-(allow mach-task-exception-port-set)
-
-(allow mach-task-inspect
+(allow mach-task-exception-port-set
 	(target self)
 )
 
-(allow mach-task-name)
-
-(allow mach-task-read
+(allow mach-task-name
 	(target self)
 )
 
-(allow mach-task-special-port*)
-
-(allow necp-client-open)
-
-(allow process-codesigning)
-
-(allow process-info-codesignature)
-
-(allow process-info-pidinfo)
-
-(allow process-iopolicy*)
+(allow process*)
 
 (allow sandbox-check)
 

 )
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
