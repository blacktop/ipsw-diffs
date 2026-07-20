## quicklookd

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
 
-(allow iokit-open-service)
-
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
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(ipc-posix-name "apple.shm.notification_center")
 		(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
 	)
 )
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "Apple MIDI in [0-9]")
 		(ipc-posix-name "Apple MIDI out [0-9]")

 	)
 )
 
-(allow ipc-posix-shm-write-data
+(allow ipc-posix-shm-write-create
 	(require-any
 		(ipc-posix-name "Apple MIDI in [0-9]")
 		(ipc-posix-name "Apple MIDI out [0-9]")

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
-(allow mach-issue-extension
+(allow mach-host-special-port-set
 	(extension-class "com.apple.webkit.extension.mach")
 )
 
-(allow mach-lookup
+(allow mach-issue-extension
 	(with report)
 	(global-name "com.apple.sharingd.nsxpc")
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.appmanagedfeatures.restrictions")
 		(%entitlement-is-present "com.apple.developer.appmanagedfeatures")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.merchantd.engagement")
 		(%entitlement-is-present "com.apple.developer.proximity-reader.customer-engagement")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.coreidvd.digital-presentment.xpc")
 		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
 		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.merchantd.storage")
 		(%entitlement-is-present "com.apple.developer.proximity-reader.payment.acceptance")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.assessmentagent")
 		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.SafetyKit")
 		(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.callkit.networkextension.voip")
 		(%entitlement-is-present "com.apple.developer.networking.networkextension")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.seserviced.credential.manager")
 		(%entitlement-is-present "com.apple.developer.secure-element-credential")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.merchantd.identity")
 		(%entitlement-is-present "com.apple.developer.proximity-reader.identity.read")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.ExposureNotification")
 		(%entitlement-is-present "com.apple.developer.exposure-notification")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.family.ageRange.xpc")
 		(%entitlement-is-present "com.apple.developer.declared-age-range")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(require-any
 			(global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.VerificationCodes")

 		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.messages.critical-messaging")
 		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.seserviced.session")
 		(%entitlement-is-present "com.apple.developer.carkey.session")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.MomentsUIService")
 		(%entitlement-is-present "com.apple.developer.journal.allow")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.ServicesPaymentAngel")
 		(%entitlement-is-present "com.apple.private.applemediaservices")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.weatherkit.authservice")
 		(%entitlement-is-present "com.apple.developer.weatherkit")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.odi.assessmentService")
 		(%entitlement-is-present "com.apple.developer.trustinsights.base")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.financed.service.coredatastore")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.merchantd.discovery")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.MusicKit.UI")
 		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(require-any
 			(global-name "com.apple.DeviceConfigurationAgent.consumer")

 		(%entitlement-is-present "com.apple.private.device-configuration.effective-configuration-ids.read")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.uikit.viewservice.*")
 		(global-name #"^com[.]apple[.]uikit[.]viewservice[.].+")
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
 	(require-all
 		(global-name "com.apple.gputools.service")
 		(system-attribute developer-mode)
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
 	(require-all
 		(process-attribute is-apple-signed-executable)
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")

 		(xpc-service-name "com.apple.uifoundation-bundle-helper")
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
 		(extension "com.apple.security.exception.mach-register.global-name")
 		(local-name "com.apple.accessibility.gax.client")

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
-(allow network-inbound
+(allow network*
 	(require-all
 		(subpath "/private/var")
 		(require-any

 		)
 	)
 )
-(deny network-inbound
+(deny network*
 	(require-all
 		(extension "com.apple.librarian.ubiquity-container")
 		(require-any

 		)
 	)
 )
-(deny network-inbound
+(deny network*
 	(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
 )
-(deny network-inbound
+(deny network*
 	(require-all
 		(subpath "/private/var")
 		(require-any

 )
 
 (allow network-bind
-	(require-all
-		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-	)
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
-		(extension "com.apple.librarian.ubiquity-container")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(literal "/private/var/tmp/ubiquity.socket")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(require-any
-									(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-									)
-								)
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-							)
-						)
-					)
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-							(require-all
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(literal "/private/var/tmp/ubiquity.socket")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(require-any
-											(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-											)
-										)
-									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(subpath "${HOME}/Library/Mobile Documents")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-		)
-	)
-)
-(allow network-bind
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(literal "/private/var/tmp/ubiquity.socket")
-			(require-all
-				(extension "com.apple.sandbox.container")
-				(require-any
-					(literal "/private/var/tmp/ubiquity.socket")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(require-any
-							(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-					)
-				)
-			)
-		)
-	)
-)
-(deny network-bind
-	(require-all
-		(extension "com.apple.librarian.ubiquity-container")
-		(require-any
-			(require-all
-				(subpath "/private/var")
-				(require-any
-					(require-all
-						(extension "com.apple.sandbox.container")
-						(require-any
-							(literal "/private/var/tmp/ubiquity.socket")
-							(require-all
-								(require-any
-									(subpath "${FRONT_USER_HOME}")
-									(subpath "${HOME}")
-								)
-								(require-any
-									(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-									)
-								)
-							)
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-							)
-						)
-					)
-					(require-all
-						(subpath "${FRONT_USER_HOME}")
-						(require-any
-							(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-							(require-all
-								(extension "com.apple.sandbox.container")
-								(require-any
-									(literal "/private/var/tmp/ubiquity.socket")
-									(require-all
-										(require-any
-											(subpath "${FRONT_USER_HOME}")
-											(subpath "${HOME}")
-										)
-										(require-any
-											(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-											(require-all
-												(subpath "/private/var/PersonaVolumes")
-												(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-											)
-										)
-									)
-									(require-all
-										(subpath "/private/var/PersonaVolumes")
-										(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-									)
-								)
-							)
-						)
-					)
-				)
-			)
-			(subpath "${HOME}/Library/Mobile Documents")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-		)
-	)
-)
-(deny network-bind
-	(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
-)
-(deny network-bind
-	(require-all
-		(subpath "/private/var")
-		(require-any
-			(literal "/private/var/tmp/ubiquity.socket")
-			(require-all
-				(extension "com.apple.sandbox.container")
-				(require-any
-					(literal "/private/var/tmp/ubiquity.socket")
-					(require-all
-						(require-any
-							(subpath "${FRONT_USER_HOME}")
-							(subpath "${HOME}")
-						)
-						(require-any
-							(regex #"((((^/private/var/(mobile|euser[0-9]+)/Containers/(Temp/)?Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/[-0-9A-F]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+(/tmp|/Library)(/|$))|^/private/var/Users/[^/]+/Containers/(Temp/)?Data/[^/]+/[^/]+/Documents(/|$))")
-							(require-all
-								(subpath "/private/var/PersonaVolumes")
-								(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
-							)
-						)
-					)
-					(require-all
-						(subpath "/private/var/PersonaVolumes")
-						(regex #"^/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+((/tmp|/Library)|/Documents)(/|$)")
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
 		(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
 		(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
 	)
 )
-(allow network-outbound
+(allow network-bind
 	(require-all
 		(extension "com.apple.app-sandbox.read-write")
 		(require-any

 		)
 	)
 )
-(allow network-outbound
+(allow network-bind
 	(require-all
 		(extension "com.apple.librarian.ubiquity-container")
 		(require-any

 		)
 	)
 )
-(allow network-outbound
+(allow network-bind
 	(require-all
 		(subpath "/private/var")
 		(require-any

 		)
 	)
 )
-(deny network-outbound
+(deny network-bind
 	(require-all
 		(extension "com.apple.librarian.ubiquity-container")
 		(require-any

 		)
 	)
 )
-(deny network-outbound
+(deny network-bind
 	(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
 )
-(deny network-outbound
+(deny network-bind
 	(require-all
 		(subpath "/private/var")
 		(require-any

 	)
 )
 
+(allow network-outbound)
+
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
