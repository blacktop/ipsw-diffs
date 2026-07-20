## com.apple.quicklook.QLThumbnailsService

> Group: ⬆️ Updated

```diff

 
 (allow fs-snapshot-mount)
 
-(allow iokit-get-properties)
+(allow iokit*)
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(system-attribute virtual-device)
 		(require-any

 		)
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-any
 		(extension "com.apple.security.exception.iokit-user-client-class")
 		(iokit-registry-entry-class "AGXCommandQueue")

 	)
 )
 
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-any
 		(%entitlement-is-present "com.apple.security.exception.iokit-user-client-class")
 		(iokit-registry-entry-class "AGXAcceleratorG*")

 	)
 )
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(ipc-posix-name "apple.shm.notification_center")
 		(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
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
 	(require-any
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")

 		(xpc-service-name "com.apple.coremedia.decompressionsession.xpc")
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
-(deny network*
+(deny necp-client-open
 	(require-any
 		(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
 		(literal "/private/var/tmp/ubiquity.socket")
 	)
 )
 
-(allow network-inbound
+(allow network*
 	(require-all
 		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
 	)
 )
-(allow network-inbound
+(allow network*
 	(require-all
 		(extension "com.apple.app-sandbox.read-write")
 		(require-any

 		)
 	)
 )
-(allow network-inbound
+(allow network*
 	(require-all
 		(extension "com.apple.librarian.ubiquity-container")
 		(require-any

 		)
 	)
 )
-(deny network-inbound
+(deny network*
 	(require-any
 		(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
 		(literal "/private/var/tmp/ubiquity.socket")
 	)
 )
 
+(allow network-bind
+	(control-name "com.apple.flow-divert")
+)
 (allow network-bind
 	(require-all
 		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")

 	)
 )
 
-(allow network-outbound
-	(control-name "com.apple.flow-divert")
-)
-(allow network-outbound
-	(require-all
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-	)
-)
-(allow network-outbound
-	(require-all
-		(extension "com.apple.app-sandbox.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Mobile Documents")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-		)
-	)
-)
-(allow network-outbound
-	(require-all
-		(extension "com.apple.librarian.ubiquity-container")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-				(subpath "${FRONT_USER_HOME}")
-			)
-			(subpath "${HOME}/Library/Mobile Documents")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-		)
-	)
-)
-(deny network-outbound
-	(require-any
-		(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
-		(literal "/private/var/tmp/ubiquity.socket")
-	)
-)
+(allow network-outbound)
 
 (allow nvram*)
 
-(allow process-codesigning)
-
-(allow process-info*)
-
-(allow process-iopolicy*)
+(allow process*)
 
 (allow sandbox-check)
 

 )
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
