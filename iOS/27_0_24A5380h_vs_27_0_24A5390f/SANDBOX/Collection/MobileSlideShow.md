## MobileSlideShow

> Group: ⬆️ Updated

```diff

 	(extension-class "com.apple.webkit.mach-bootstrap")
 )
 
-(allow iokit-get-properties)
+(allow iokit*)
 
-(allow iokit-issue-extension
+(allow iokit-get-properties
 	(extension-class "com.apple.webkit.extension.iokit")
 )
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "ANEClientHintsUserClient")
 		(%entitlement-is-bool-true "com.apple.private.ane.allow-set-client-hints")
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "IOHIDLibUserClient")
 		(process-attribute is-apple-signed-executable)
 	)
 )
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
 		(iokit-connection "IOGPU")

 	)
 )
 
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-any
 		(%entitlement-is-present "com.apple.security.exception.iokit-user-client-class")
 		(iokit-registry-entry-class "AGXAcceleratorG*")

 	)
 )
 
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "ANEClientHintsUserClient")
 		(%entitlement-is-bool-true "com.apple.private.ane.allow-set-client-hints")

 		)
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-property "QueueSize")
 		(iokit-registry-entry-class "IOHIDEventServiceFastPathUserClient")
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(require-any
 			(iokit-property "interval")

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
 
-(allow ipc-posix-shm-write-data
+(allow ipc-posix-shm-write-create
 	(require-any
 		(extension "com.apple.sandbox.application-group")
 		(ipc-posix-name "Apple MIDI in [0-9]")

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
-(allow mach-issue-extension
+(allow mach-host-special-port-set
 	(extension-class "com.apple.webkit.extension.mach")
 )
 
-(allow mach-lookup
+(allow mach-issue-extension
 	(with report)
 	(require-all
 		(signing-identifier "com.apple.mobileslideshow")

 			(global-name "com.apple.PowerManagement.control")
 			(global-name "com.apple.ProgressReporting")
 			(global-name "com.apple.SBUserNotification")
-			(global-name "com.apple.Safari.SafeBrowsing.Service")
 			(global-name "com.apple.ScreenTimeAgent")
 			(global-name "com.apple.SystemConfiguration.DNSConfiguration")
 			(global-name "com.apple.SystemConfiguration.DNSConfiguration")

 				(global-name "com.apple.ap.promotedcontent.attributionservice")
 				(global-name "com.apple.appprotectiond.extensioninfo")
 				(global-name "com.apple.appprotectiond.extensionmonitor")
-				(global-name "com.apple.appprotectiond.viewsubjectinfo")
 				(global-name "com.apple.appprotectiond.viewsubjectmonitor")
 				(global-name "com.apple.arkit.service.geoTracking")
 				(global-name "com.apple.arkit.service.location")

 				(global-name "com.apple.progressd")
 				(global-name "com.apple.rti-screencontinuity")
 			)
+			(require-any
+				(global-name "com.apple.Safari.SafeBrowsing.Service")
+				(global-name "com.apple.appprotectiond.viewsubjectinfo")
+			)
 			(require-any
 				(global-name "com.apple.SiriTTSService.TrialProxy")
 				(global-name "com.apple.shazamd")

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(signing-identifier "com.apple.camera")
 		(global-name "com.apple.storekitd")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(require-any
 			(signing-identifier "com.apple.Capture")

 		(global-name "com.apple.storekitd")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(signing-identifier "com.apple.mobileslideshow")
 		(require-any

 			(global-name "com.apple.PowerManagement.control")
 			(global-name "com.apple.ProgressReporting")
 			(global-name "com.apple.SBUserNotification")
-			(global-name "com.apple.Safari.SafeBrowsing.Service")
 			(global-name "com.apple.ScreenTimeAgent")
 			(global-name "com.apple.SystemConfiguration.DNSConfiguration")
 			(global-name "com.apple.SystemConfiguration.DNSConfiguration")

 				(global-name "com.apple.ap.promotedcontent.attributionservice")
 				(global-name "com.apple.appprotectiond.extensioninfo")
 				(global-name "com.apple.appprotectiond.extensionmonitor")
-				(global-name "com.apple.appprotectiond.viewsubjectinfo")
 				(global-name "com.apple.appprotectiond.viewsubjectmonitor")
 				(global-name "com.apple.arkit.service.geoTracking")
 				(global-name "com.apple.arkit.service.location")

 				(global-name "com.apple.progressd")
 				(global-name "com.apple.rti-screencontinuity")
 			)
+			(require-any
+				(global-name "com.apple.Safari.SafeBrowsing.Service")
+				(global-name "com.apple.appprotectiond.viewsubjectinfo")
+			)
 			(require-any
 				(global-name "com.apple.SiriTTSService.TrialProxy")
 				(global-name "com.apple.shazamd")

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")

 		(xpc-service-name "com.apple.WebKit.WebContent.EnhancedSecurity")
 	)
 )
-(deny mach-lookup)
-(deny mach-lookup
+(deny mach-issue-extension)
+(deny mach-issue-extension
 	(require-all
 		(signing-identifier "com.apple.mobileslideshow")
 		(require-any

 			(global-name "com.apple.PowerManagement.control")
 			(global-name "com.apple.ProgressReporting")
 			(global-name "com.apple.SBUserNotification")
-			(global-name "com.apple.Safari.SafeBrowsing.Service")
 			(global-name "com.apple.ScreenTimeAgent")
 			(global-name "com.apple.SystemConfiguration.DNSConfiguration")
 			(global-name "com.apple.SystemConfiguration.DNSConfiguration")

 				(global-name "com.apple.ap.promotedcontent.attributionservice")
 				(global-name "com.apple.appprotectiond.extensioninfo")
 				(global-name "com.apple.appprotectiond.extensionmonitor")
-				(global-name "com.apple.appprotectiond.viewsubjectinfo")
 				(global-name "com.apple.appprotectiond.viewsubjectmonitor")
 				(global-name "com.apple.arkit.service.geoTracking")
 				(global-name "com.apple.arkit.service.location")

 				(global-name "com.apple.progressd")
 				(global-name "com.apple.rti-screencontinuity")
 			)
+			(require-any
+				(global-name "com.apple.Safari.SafeBrowsing.Service")
+				(global-name "com.apple.appprotectiond.viewsubjectinfo")
+			)
 			(require-any
 				(global-name "com.apple.SiriTTSService.TrialProxy")
 				(global-name "com.apple.shazamd")

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
+		(signing-identifier "com.apple.camera.lockscreen")
+		(subpath "/private/var")
+		(extension "com.apple.sandbox.container")
+		(require-any
+			(require-all
+				(require-any
+					(subpath "${FRONT_USER_HOME}")
+					(subpath "${HOME}")
+				)
+				(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+			)
+			(require-all
+				(subpath "/private/var/PersonaVolumes")
+				(require-any
+					(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
+					(require-all
+						(require-any
+							(subpath "${FRONT_USER_HOME}")
+							(subpath "${HOME}")
+						)
+						(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
+					)
+				)
+			)
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
+		(extension "com.apple.sandbox.application-group")
+		(require-any
+			(require-all
+				(subpath "/private/var")
+				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/")
+				(subpath "${FRONT_USER_HOME}")
+			)
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+")
+		)
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
-		(signing-identifier "com.apple.camera.lockscreen")
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
-(allow network-inbound
-	(require-all
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-	)
-)
-(allow network-inbound
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
-		(signing-identifier "com.apple.camera.lockscreen")
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
-(allow network-bind
-	(require-all
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-	)
-)
-(allow network-bind
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
 

 (deny user-preference-write)
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
