## quicklook-thumbnail-secure

> Group: ⬆️ Updated

```diff

 	(process-attribute is-apple-signed-executable)
 )
 
+(deny mach-lookup
+	(global-name "com.apple.webkit.camera")
+)
+
 (deny darwin-notification-post)
 
 (deny dynamic-code-generation)

 
 (allow fs-info)
 
-(deny iokit-get-properties)
-(allow iokit-get-properties
+(allow iokit*
 	(iokit-property "IORegistryEntryPropertyKeys")
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-property "AppleJPEGNumCores")
 		(iokit-registry-entry-class "AppleJPEGDriver")
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-property "platform-name")
 		(iokit-registry-entry-class "IOPlatformExpertDevice")
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-property "AVCSupported")
 		(iokit-registry-entry-class "AppleAVD")
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-property "IOSurfaceAcceleratorCapabilitiesDict")
 		(iokit-registry-entry-class "IOService")
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-property "product-id")
 		(iokit-registry-entry-class "IOPlatformDevice")
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-property "soc-generation")
 		(iokit-registry-entry-class "IOPlatformDevice")
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(require-any
 			(iokit-property "artwork-device-idiom")

 	)
 )
 
-(allow iokit-open-user-client
+(deny iokit-get-properties)
+
+(allow iokit-open*
 	(require-all
 		(system-attribute virtual-device)
 		(iokit-registry-entry-class "IOSurfaceAcceleratorParavirtClient")
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-any
 		(extension "com.apple.security.exception.iokit-user-client-class")
 		(iokit-registry-entry-class "AGXDevice")

 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-any
 		(%entitlement-is-present "com.apple.security.exception.iokit-user-client-class")
 		(iokit-registry-entry-class "AppleJPEGDriver")

 	)
 )
 
-(allow ipc-posix-shm-read-data
+(deny iokit-open-service)
+
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.*")
 		(ipc-posix-name "apple.shm.notification_center")
 	)
 )
 
-(allow isp-command-send)
+(allow ipc-sysv-shm)
 
-(deny mach-cross-domain-lookup)
+(allow mach*)
 
-(allow mach-lookup
+(deny mach-bootstrap)
+
+(deny mach-derive-port)
+
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "com.apple.WebKit.GPU")
 		(%entitlement-is-bool-true "com.apple.private.quicklook-thumbnail.webkit")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "com.apple.ThumbnailsBlastDoorService")
 		(%entitlement-is-bool-true "com.apple.private.quicklook-thumbnail.blastdoor")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "com.apple.runningboard")
 		(%entitlement-is-bool-true "com.apple.private.quicklook-thumbnail.blastdoor")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(require-any
 			(xpc-service-name "com.apple.WebKit.Networking")

 		(%entitlement-is-bool-true "com.apple.private.quicklook-thumbnail.webkit")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")

 	)
 )
 
-(allow mach-register
+(allow mach-priv-task-port
 	(extension "com.apple.security.exception.mach-register.global-name")
 )
 
+(deny mach-task-exception-port-set)
+(allow mach-task-exception-port-set
+	(target self)
+)
+
 (allow mach-task-inspect
 	(target self)
 )

 	(target self)
 )
 
-(allow mach-task-read
-	(target self)
-)
+(deny necp-client-open)
 
-(allow network-inbound
+(allow network*
 	(require-all
 		(subpath "/private/var")
 		(extension "com.apple.sandbox.container")

 )
 
 (allow network-bind
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
 		(subpath "/private/var")
 		(extension "com.apple.sandbox.container")

 
 (deny nvram*)
 
-(deny process-info*)
+(allow process*)
 
-(allow process-info-codesignature)
+(deny process-codesigning)
+
+(deny process-info-codesignature)
+(allow process-info-codesignature
+	(target self)
+)
 
 (deny process-info-dirtycontrol)
-(allow process-info-dirtycontrol
+
+(deny process-info-ledger)
+
+(deny process-info-listpids)
+(allow process-info-listpids
 	(target self)
 )
 
 (deny process-info-pidinfo)
-(allow process-info-pidinfo
-	(target self)
-)
 
-(allow process-info-sandbox-container)
+(deny process-info-pidfdinfo)
+
+(deny process-info-pidfileportinfo)
+
+(deny process-info-sandbox-container)
+
+(deny process-iopolicy-set)
 
 (allow signal
 	(target self)
```
