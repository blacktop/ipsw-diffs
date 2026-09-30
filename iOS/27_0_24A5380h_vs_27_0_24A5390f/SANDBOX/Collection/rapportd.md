## rapportd

> Group: ⬆️ Updated

```diff

 
 (allow fs-snapshot-mount)
 
-(allow iokit-get-properties)
+(allow iokit*)
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-any
 		(extension "com.apple.security.exception.iokit-user-client-class")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")

 	)
 )
 
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-any
 		(%entitlement-is-present "com.apple.security.exception.iokit-user-client-class")
 		(iokit-registry-entry-class "AppleKeyStore")

 	)
 )
 
-(allow ipc-posix-sem*
+(allow ipc-posix*
 	(extension "com.apple.sandbox.application-group")
 )
 
 (allow ipc-posix-shm*
-	(extension "com.apple.sandbox.application-group")
-)
-
-(allow ipc-posix-shm-read-data
 	(require-all
 		(ipc-posix-name "apple.shm.notification_center")
 		(%entitlement-is-bool-true "com.apple.security.on-demand-install-capable")
 	)
 )
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-any
 		(extension "com.apple.sandbox.application-group")
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
 		(global-name "com.apple.ak.auth.xpc")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.networkd_privileged")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.ak.anisette.xpc")
 		(process-attribute is-apple-signed-executable)
 	)
 )
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
 		(extension "com.apple.sandbox.application-group")
 		(extension "com.apple.security.exception.mach-lookup.global-name")

 		(xpc-service-name "com.apple.MediaPlayer.RemotePlayerService")
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
 	(require-any
 		(extension "com.apple.sandbox.application-group")
 		(extension "com.apple.security.exception.mach-register.global-name")
 	)
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
+(allow network*)
 
-(allow necp-client-open)
-
-(allow network-inbound)
-
-(allow network-bind)
-
-(allow network-outbound)
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
