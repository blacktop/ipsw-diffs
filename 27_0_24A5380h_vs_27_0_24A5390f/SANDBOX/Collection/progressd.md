## progressd

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
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(ipc-posix-name "apple.shm.notification_center")
 		(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
 	)
 )
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(ipc-posix-name "/com.apple.AppSSO.version")
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
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")

 		(global-name "com.apple.usymptomsd")
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
+(deny necp-client-open
+	(require-any
+		(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
+		(literal "/private/var/tmp/ubiquity.socket")
+	)
 )
 
-(allow mach-task-special-port*)
-
-(allow necp-client-open)
-
+(allow network*
+	(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
+)
+(allow network*
+	(require-all
+		(extension "com.apple.app-sandbox.read-write")
+		(require-any
+			(subpath "${HOME}/Library/Mobile Documents")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+		)
+	)
+)
+(allow network*
+	(require-all
+		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
+		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+	)
+)
+(allow network*
+	(require-all
+		(extension "com.apple.librarian.ubiquity-container")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
+				(subpath "${FRONT_USER_HOME}")
+			)
+			(subpath "${HOME}/Library/Mobile Documents")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
+		)
+	)
+)
 (deny network*
 	(require-any
 		(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")

 	)
 )
 
-(allow network-inbound
-	(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
-)
-(allow network-inbound
-	(require-all
-		(extension "com.apple.app-sandbox.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Mobile Documents")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-		)
-	)
-)
-(allow network-inbound
-	(require-all
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-	)
-)
-(allow network-inbound
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
-(deny network-inbound
-	(require-any
-		(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
-		(literal "/private/var/tmp/ubiquity.socket")
-	)
-)
-
-(allow network-bind
-	(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
-)
-(allow network-bind
-	(require-all
-		(extension "com.apple.app-sandbox.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Mobile Documents")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-		)
-	)
-)
-(allow network-bind
-	(require-all
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-	)
-)
-(allow network-bind
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
-(deny network-bind
-	(require-any
-		(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
-		(literal "/private/var/tmp/ubiquity.socket")
-	)
-)
+(allow network-bind)
 
 (allow network-outbound)
 
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
