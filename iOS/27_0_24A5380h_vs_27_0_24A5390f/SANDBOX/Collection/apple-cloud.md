## apple-cloud

> Group: ⬆️ Updated

```diff

 	)
 )
 
-(allow iokit-get-properties)
+(allow iokit*)
 
-(allow iokit-issue-extension
+(allow iokit-get-properties
 	(require-all
 		(extension-class "com.apple.webkit.extension.iokit")
 		(%entitlement-is-present "com.apple.security.ts.webkit-client")
 	)
 )
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(extension "com.apple.security.exception.iokit-user-client-class")
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "ANEClientHintsUserClient")
 		(%entitlement-is-bool-true "com.apple.private.ane.allow-set-client-hints")
 		(%entitlement-is-bool-true "com.apple.security.ts.ane-client")
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(%entitlement-is-bool-true "com.apple.security.network.client")
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "IOMobileFramebufferUserClient")
 		(%entitlement-is-bool-true "com.apple.security.ts.framebuffer-access")
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(%entitlement-is-bool-true "com.apple.security.ts.mobile-keybag-access")
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(require-any
 			(iokit-registry-entry-class "AppleVirtIONeuralEngineDeviceUserClient")

 		(%entitlement-is-bool-true "com.apple.security.ts.ane-client")
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "RootDomainUserClient")
 		(require-any

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
 
-(allow ipc-posix-sem*
+(allow ipc-posix*
 	(require-any
 		(extension "com.apple.sandbox.application-group")
 		(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-sem}")
 	)
 )
 
-(allow ipc-posix-shm*
+(allow ipc-posix-sem-wait
 	(require-any
 		(extension "com.apple.sandbox.application-group")
 		(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-shm}")
 	)
 )
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(ipc-posix-name "/com.apple.AppSSO.version")
 		(require-any

 		)
 	)
 )
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(ipc-posix-name "apple.shm.notification_center")
 		(%entitlement-is-bool-true "com.apple.security.on-demand-install-capable")
 	)
 )
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-any
 		(extension "com.apple.sandbox.application-group")
 		(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-shm.read-only}")

 	)
 )
 
-(allow isp-command-send)
+(allow ipc-posix-shm-read-data
+	(require-any
+		(extension "com.apple.sandbox.application-group")
+		(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-shm}")
+	)
+)
 
-(deny job-creation)
+(allow ipc-posix-shm-write*
+	(require-any
+		(extension "com.apple.sandbox.application-group")
+		(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-shm}")
+	)
+)
 
-(deny lsopen
+(allow ipc-sysv-shm)
+
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
-(allow mach-issue-extension
+(allow mach-host-special-port-set
 	(require-all
 		(extension-class "com.apple.webkit.extension.mach")
 		(%entitlement-is-present "com.apple.security.ts.webkit-client")
 	)
 )
 
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "com.apple.ImageIOXPCService")
 		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.AppSSO.service-xpc")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.networkscored")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.quicklook.ThumbnailsAgent")
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.dnssd.service")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name ".viewservice")
 		(%entitlement-is-bool-true "com.apple.security.ts.viewservice.client")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.nesessionmanager")
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.securityd")
 		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.trustd")
 		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.mobile.heartbeat")
 		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(require-any
 			(global-name "com.apple.cvmsServ")

 		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.locationd.spi")
 		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.cloudd")
 		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "com.apple.MTLCompilerService")
 		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.marco")
 		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.iokit.powerdxpc")
 		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.powerlog.plxpclogger.xpc")
 		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.geoanalyticsd")
 		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.locationd.synchronous")
 		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.locationd.registration")
 		(%entitlement-is-bool-true "com.apple.security.ts.location-services")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.appleneuralengine")
 		(%entitlement-is-bool-true "com.apple.security.ts.ane-client")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(require-any
 			(global-name "com.apple.geod")

 		(%entitlement-is-bool-true "com.apple.security.ts.geoservices")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "com.apple.AGXCompilerService*")
 		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.spotlight.IndexDelegateAgent")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.spotlight.IndexAgent")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.identityservicesd.idquery.embedded.auth")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.contactsd")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.accountsd.accountmanager")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.ABDatabaseDoctor")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "com.apple.ImageIOXPCService")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.cmfsyncagent.embedded.auth")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(require-any
 			(global-name "com.apple.ckdiscretionaryd")

 		(%entitlement-is-bool-true "com.apple.security.ts.cloudkit-client")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(process-attribute is-apple-signed-executable)
 		(global-name "com.apple.audioanalyticsd")
 		(%entitlement-is-bool-true "com.apple.security.ts.play-audio")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.power-assertions")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.identityservicesd.embedded.auth")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.play-audio")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.PowerManagement.control")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.play-media")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.springboard-services")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.revisiond")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.asset-access.with-media-playback")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.network.client")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(%entitlement-is-present "com.apple.security.ts.webkit-client")
 		(require-any

 		)
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
 
-(allow mach-priv-host-port
+(allow mach-priv*
 	(%entitlement-is-bool-true "com.apple.security.ts.mach-priv-host-port")
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
 	(require-any
 		(%entitlement-is-bool-true "com.apple.security.ts.mach-task-read")
 		(target self)
 	)
 )
 
-(allow mach-task-name
+(allow mach-task-inspect
 	(require-any
 		(%entitlement-is-bool-true "com.apple.security.ts.mach-task-name")
 		(%entitlement-is-bool-true "com.apple.security.ts.mach-task-read")

 	)
 )
 
-(allow mach-task-read
+(allow mach-task-name
 	(require-any
 		(%entitlement-is-bool-true "com.apple.security.ts.mach-task-read")
 		(target self)
 	)
 )
 
-(allow mach-task-special-port*)
-
-(allow necp-client-open)
-
-(deny network*
+(deny necp-client-open
 	(require-all
 		(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 	)
 )
-(deny network*
+(deny necp-client-open
 	(require-all
 		(literal "/private/var/tmp/ubiquity.socket")
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 	)
 )
 
-(allow network-inbound
+(allow network*
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.network.client")
 		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
 	)
 )
-(allow network-inbound
+(allow network*
 	(%entitlement-is-bool-true "com.apple.security.network.server")
 )
-(allow network-inbound
+(allow network*
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		(require-any

 		)
 	)
 )
-(allow network-inbound
+(allow network*
 	(require-all
 		(extension "com.apple.sandbox.application-group")
 		(require-any

 		)
 	)
 )
-(deny network-inbound
+(deny network*
 	(require-all
 		(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 	)
 )
-(deny network-inbound
+(deny network*
 	(require-all
 		(literal "/private/var/tmp/ubiquity.socket")
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")

 )
 
 (allow network-bind
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.network.client")
-		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
-	)
-)
-(allow network-bind
-	(%entitlement-is-bool-true "com.apple.security.network.server")
-)
-(allow network-bind
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-		(require-any
-			(require-all
-				(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-			)
-			(require-all
-				(extension "com.apple.app-sandbox.read-write")
-				(require-any
-					(require-all
-						(%entitlement-is-bool-true "com.apple.private.librarian.container-proxy")
-						(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					)
-					(subpath "${HOME}/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-				)
-			)
-			(require-all
-				(extension "com.apple.librarian.ubiquity-container")
-				(require-any
-					(require-all
-						(subpath "/private/var")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/Shared/AppGroup/[^/]+/File Provider Storage(/|$)")
-						(subpath "${FRONT_USER_HOME}")
-					)
-					(subpath "${HOME}/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/Library/Mobile Documents")
-					(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Shared/AppGroup/[^/]+/File Provider Storage")
-				)
-			)
-		)
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
-(deny network-bind
-	(require-all
-		(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-	)
-)
-(deny network-bind
-	(require-all
-		(literal "/private/var/tmp/ubiquity.socket")
-		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
-	)
-)
-
-(allow network-outbound
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.network.server")
 		(require-any

 		)
 	)
 )
-(allow network-outbound
+(allow network-bind
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-client")
 		(literal "/private/var/run/lockdown.sock")
 	)
 )
-(allow network-outbound
+(allow network-bind
 	(require-all
 		(literal "/private/var/run/lockdown/checkin*")
 		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-service")
 	)
 )
-(allow network-outbound
+(allow network-bind
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 		(require-any

 		)
 	)
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
 	(require-any
 		(%entitlement-is-bool-true "com.apple.security.network.client")
 		(control-name "com.apple.flow-divert")
 	)
 )
-(deny network-outbound
+(deny network-bind
 	(require-all
 		(literal "${FRONT_USER_HOME}/tmp/ubiquity.socket")
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 	)
 )
-(deny network-outbound
+(deny network-bind
 	(require-all
 		(literal "/private/var/tmp/ubiquity.socket")
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
 	)
 )
 
-(allow nvram-delete
+(allow nvram*
 	(require-all
 		(nvram-variable "${ENTITLEMENT:com.apple.security.ts.nvram-delete}")
 		(%entitlement-is-present "com.apple.security.ts.nvram-delete")
 	)
 )
 
-(allow nvram-get
+(allow nvram-delete
 	(require-all
 		(nvram-variable "${ENTITLEMENT:com.apple.security.ts.nvram-read}")
 		(%entitlement-is-present "com.apple.security.ts.nvram-read")
 	)
 )
+(allow nvram-delete
+	(require-all
+		(nvram-variable "${ENTITLEMENT:com.apple.security.ts.nvram-read-write}")
+		(%entitlement-is-present "com.apple.security.ts.nvram-read-write")
+	)
+)
+
 (allow nvram-get
 	(require-all
 		(nvram-variable "${ENTITLEMENT:com.apple.security.ts.nvram-read-write}")

 	)
 )
 
-(allow nvram-set
-	(require-all
-		(nvram-variable "${ENTITLEMENT:com.apple.security.ts.nvram-read-write}")
-		(%entitlement-is-present "com.apple.security.ts.nvram-read-write")
-	)
+(allow process*)
+
+(allow process-legacy-codesigning-entitlements-blob-get
+	(%entitlement-is-bool-true "com.apple.security.ts.get-code-signing-data")
 )
 
-(allow process-codesigning)
-
-(allow process-info-codesignature)
-
-(allow process-iopolicy*)
-
 (allow process-legacy-codesigning-entitlements-der-blob-get
 	(%entitlement-is-bool-true "com.apple.security.ts.get-code-signing-data")
 )
 
-(allow process-legacy-codesigning-identity-get
-	(%entitlement-is-bool-true "com.apple.security.ts.get-code-signing-data")
-)
-
-(allow process-legacy-codesigning-status-get
+(allow process-legacy-codesigning-status*
 	(%entitlement-is-bool-true "com.apple.security.ts.get-code-signing-data")
 )
 

 )
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
