## playground-devtools

> Group: ⬆️ Updated

```diff

 
 (allow fs-snapshot-mount)
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "AppleMobileFileIntegrityUserClient")
 		(%entitlement-is-bool-true "com.apple.private.amfi.can-load-cdhash")
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(extension "com.apple.security.exception.iokit-user-client-class")
 )
 
-(allow iokit-open-service)
+(allow iokit-open-user-client)
 
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
 
-(allow isp-command-send)
+(allow ipc-sysv-shm)
 
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
 		(extension "com.apple.sandbox.application-group")
 		(extension "com.apple.security.exception.mach-lookup.global-name")

 		(xpc-service-name "*")
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
 	)
 )
-(allow network-inbound
+(allow network*
 	(require-all
 		(subpath "/private/var")
 		(extension "com.apple.sandbox.container")

 )
 
 (allow network-bind
-	(require-all
-		(extension "com.apple.sandbox.application-group")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(require-any
-									(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-									)
-								)
-							)
-						)
-					)
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
-							(require-all
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(require-any
-											(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-											(require-all
-												(require-any
-													(subpath "${FRONT_USER_HOME}")
-													(subpath "${HOME}")
-												)
-												(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-											)
-										)
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
-		)
-	)
-)
-(allow network-bind
-	(require-all
-		(subpath "/private/var")
-		(extension "com.apple.sandbox.container")
-		(require-any
-			(require-all
-				(require-any
-					(subpath "${FRONT_USER_HOME}")
-					(subpath "${HOME}")
-				)
-				(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-			)
-			(require-all
-				(subpath "/private/var/PersonaVolumes")
-				(require-any
-					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-					)
-				)
-			)
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
 )
-(allow network-outbound
+(allow network-bind
 	(require-all
 		(subpath "/private/var")
 		(extension "com.apple.sandbox.container")

 	)
 )
 
-(allow process-codesigning)
-
-(allow process-iopolicy*)
+(allow process*)
 
 (allow sandbox-check)
 

 (allow system-privilege)
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
