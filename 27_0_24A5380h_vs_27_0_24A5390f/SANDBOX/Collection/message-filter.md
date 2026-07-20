## message-filter

> Group: ⬆️ Updated

```diff

 
 (allow fs-snapshot-mount)
 
-(allow iokit-get-properties)
+(allow iokit*)
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "ANEClientHintsUserClient")
 		(%entitlement-is-bool-true "com.apple.private.ane.allow-set-client-hints")
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-any
 		(extension "com.apple.security.exception.iokit-user-client-class")
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")

 	)
 )
 
-(allow iokit-open-service)
-
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "ANEClientHintsUserClient")
 		(%entitlement-is-bool-true "com.apple.private.ane.allow-set-client-hints")

 	)
 )
 
-(deny ipc-posix-shm-read-data
+(deny ipc-posix-shm*
 	(with no-report)
 	(ipc-posix-name "apple.shm.notification_center")
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
 	(require-any
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")

 		(global-name "com.apple.appleneuralengine")
 	)
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(with no-report)
 	(require-all
 		(global-name "com.apple.logd")
 		(require-not (%entitlement-is-bool-true "get-task-allow"))
 	)
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(with no-report)
 	(require-all
 		(global-name "com.apple.logd.events")
 		(require-not (%entitlement-is-bool-true "get-task-allow"))
 	)
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(with no-report)
 	(global-name "com.apple.system.notification_center")
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
 		(subpath "/private/var")
 		(extension "com.apple.sandbox.container")

 	)
 )
 
+(allow network-bind
+	(control-name "com.apple.flow-divert")
+)
 (allow network-bind
 	(require-all
 		(subpath "/private/var")

 	)
 )
 
-(allow network-outbound
-	(control-name "com.apple.flow-divert")
-)
-(allow network-outbound
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
+(allow network-outbound)
 
 (allow nvram*)
 
-(allow process-codesigning)
+(allow process*)
 
-(allow process-info-codesignature)
+(allow process-info-codesignature
+	(target self)
+)
 
-(allow process-info-dirtycontrol
+(allow process-info-listpids
 	(target self)
 )
 

 	(target self)
 )
 
-(allow process-info-rusage
+(allow process-info-sandbox-container
 	(target self)
 )
 
-(allow process-info-setcontrol
-	(target self)
-)
-
-(allow process-iopolicy*)
-
 (allow sandbox-check)
 
 (allow signal

 (allow system-privilege)
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
