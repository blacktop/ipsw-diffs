## proactiveeventtrackerd

> Group: ⬆️ Updated

```diff

 
 (allow fs-snapshot-mount)
 
-(allow iokit-get-properties)
+(allow iokit*)
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(system-attribute internal-build)
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-any
 		(extension "com.apple.security.exception.iokit-user-client-class")
 		(iokit-registry-entry-class "RootDomainUserClient")
 	)
 )
 
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-all
 		(iokit-registry-entry-class "AppleKeyStore")
 		(system-attribute internal-build)
 	)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-any
 		(%entitlement-is-present "com.apple.security.exception.iokit-user-client-class")
 		(iokit-registry-entry-class "IOPMrootDomain")
 	)
 )
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(ipc-posix-name "apple.shm.notification_center")
 		(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
 	)
 )
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(system-attribute internal-build)
 		(ipc-posix-name "/com.apple.AppSSO.version")
 	)
 )
 
-(deny job-creation)
+(deny isp-command-send)
 
-(deny lsopen
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
 	(require-all
 		(system-attribute internal-build)
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")

 		(global-name "com.apple.tccd")
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
 		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
 		(system-attribute internal-build)

 )
 
 (allow network-bind
-	(require-all
-		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
-		(system-attribute internal-build)
-	)
-)
-
-(allow network-outbound
 	(require-any
 		(control-name "com.apple.flow-divert")
 		(system-attribute internal-build)
 	)
 )
 
-(allow process-codesigning)
-
-(allow process-info-codesignature)
-
-(allow process-iopolicy*)
+(allow process*)
 
 (allow sandbox-check)
 

 )
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
