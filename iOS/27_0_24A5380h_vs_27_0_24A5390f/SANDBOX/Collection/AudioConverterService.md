## AudioConverterService

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
 	(require-all
 		(iokit-registry-entry-class "ANEClientHintsUserClient")
 		(%entitlement-is-bool-true "com.apple.private.ane.allow-set-client-hints")
 		(%entitlement-is-bool-true "com.apple.security.ts.ane-client")
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
+	(require-all
+		(iokit-registry-entry-class "AppleKeyStoreUserClient")
+		(%entitlement-is-bool-true "com.apple.security.network.client")
+	)
+)
+(allow iokit-open*
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
+	(require-all
+		(iokit-registry-entry-class "AppleKeyStoreUserClient")
+		(require-any
+			(signing-identifier "com.apple.audio.AudioConverterService")
+			(signing-identifier "com.apple.audio.AudioConverterService.Hardened")
+		)
+	)
+)
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
 )
-(deny iokit-open-user-client
-	(iokit-registry-entry-class "AppleKeyStoreUserClient")
+(deny iokit-open*
+	(require-all
+		(iokit-registry-entry-class "AppleKeyStoreUserClient")
+		(require-any
+			(signing-identifier "com.apple.audio.AudioConverterService")
+			(signing-identifier "com.apple.audio.AudioConverterService.Hardened")
+		)
+	)
 )
 
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-all
-		(iokit-registry-entry-class "AGXAcceleratorG*")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(iokit-registry-entry-class "com_apple_driver_FairPlayIOKit")
+		(signing-identifier "com.apple.audio.AudioConverterService")
 	)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
+	(require-all
+		(iokit-registry-entry-class "IOPMrootDomain")
+		(%entitlement-is-bool-true "com.apple.security.ts.power-assertions")
+	)
+)
+(allow iokit-open-user-client
 	(require-all
 		(iokit-registry-entry-class "AppleKeyStore")
-		(%entitlement-is-bool-true "com.apple.security.ts.mobile-keybag-access")
+		(require-any
+			(require-all
+				(iokit-registry-entry-class "AppleKeyStore")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.security.network.client")
+					(%entitlement-is-bool-true "com.apple.security.ts.mobile-keybag-access")
+				)
+			)
+			(signing-identifier "com.apple.audio.AudioConverterService")
+			(signing-identifier "com.apple.audio.AudioConverterService.Hardened")
+		)
 	)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
+	(require-all
+		(iokit-registry-entry-class "AGXAcceleratorG*")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+	)
+)
+(allow iokit-open-user-client
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.ane-client")
+		(require-any
+			(iokit-registry-entry-class "AppleVirtIONeuralEngineDevice")
+			(iokit-registry-entry-class "H11ANEIn")
+			(iokit-registry-entry-class "H1xANELoadBalancer")
+		)
+	)
+)
+(allow iokit-open-user-client
+	(require-all
+		(iokit-registry-entry-class "IOPMrootDomain")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
+			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
+			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
+		)
+	)
+)
+(allow iokit-open-user-client
+	(require-all
+		(iokit-registry-entry-class "AppleJPEGDriver")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+	)
+)
+(allow iokit-open-user-client
 	(require-all
 		(require-any
 			(iokit-registry-entry-class "AppleCLCD*")

 		)
 	)
 )
-(allow iokit-open-service
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.ane-client")
-		(require-any
-			(iokit-registry-entry-class "AppleVirtIONeuralEngineDevice")
-			(iokit-registry-entry-class "H11ANEIn")
-			(iokit-registry-entry-class "H1xANELoadBalancer")
-		)
-	)
-)
-(allow iokit-open-service
-	(require-all
-		(iokit-registry-entry-class "AppleJPEGDriver")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-	)
-)
-(allow iokit-open-service
-	(require-all
-		(iokit-registry-entry-class "IOPMrootDomain")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
-			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
-			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
-			(%entitlement-is-bool-true "com.apple.security.ts.power-assertions")
-		)
-	)
-)
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-all
 		(iokit-registry-entry-class "AppleKeyStore")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-all
 		(iokit-registry-entry-class "IOSurfaceRoot")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(deny iokit-open-service
-	(require-any
+(deny iokit-open-user-client
+	(require-all
 		(iokit-registry-entry-class "AppleKeyStore")
-		(iokit-registry-entry-class "com_apple_driver_FairPlayIOKit")
+		(require-any
+			(require-all
+				(iokit-registry-entry-class "AppleKeyStore")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.security.network.client")
+					(%entitlement-is-bool-true "com.apple.security.ts.mobile-keybag-access")
+				)
+			)
+			(signing-identifier "com.apple.audio.AudioConverterService")
+			(signing-identifier "com.apple.audio.AudioConverterService.Hardened")
+		)
 	)
 )
 
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "ANEClientHintsUserClient")
 		(%entitlement-is-bool-true "com.apple.private.ane.allow-set-client-hints")

 	)
 )
 
-(allow ipc-posix-sem*
+(allow ipc-posix*
 	(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-sem}")
 )
 
-(allow ipc-posix-shm*
+(allow ipc-posix-sem-wait
 	(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-shm}")
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
 		(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-shm.read-only}")
 		(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-shm}")
 	)
 )
 
-(deny job-creation)
+(allow ipc-posix-shm-read-data
+	(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-shm}")
+)
 
-(deny lsopen
+(allow ipc-posix-shm-write*
+	(ipc-posix-name "${ENTITLEMENT:com.apple.security.ts.ipc-posix-shm}")
+)
+
+(deny isp-command-send)
+
+(deny job-creation
 	(profile-flag "deny-lsopen")
 )
 
-(allow mach-derive-port)
+(allow mach-cross-domain-lookup)
 
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
-		(xpc-service-name "com.apple.AGXCompilerService*")
-		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
+		(global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
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
-	(require-all
-		(xpc-service-name "com.apple.ImageIOXPCService")
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(xpc-service-name ".viewservice")
-		(%entitlement-is-bool-true "com.apple.security.ts.viewservice.client")
-	)
-)
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
-		(global-name "com.apple.contactsd")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(xpc-service-name ".viewservice")
+		(%entitlement-is-bool-true "com.apple.security.ts.viewservice.client")
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.cmfsyncagent.embedded.auth")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.play-audio")
-		(require-any
-			(global-name "com.apple.audio.AURemoteIOServer")
-			(xpc-service-name "com.apple.audio.AudioConverterService")
-			(xpc-service-name "com.apple.audio.AudioConverterService.HighCapacity")
-			(xpc-service-name "com.apple.audio.analytics.service")
-		)
-	)
-)
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
 		(global-name "com.apple.ABDatabaseDoctor")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
-		(global-name "com.apple.identityservicesd.idquery.embedded.auth")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+		(%entitlement-is-bool-true "com.apple.security.ts.play-audio")
+		(require-any
+			(global-name "com.apple.audio.AURemoteIOServer")
+			(xpc-service-name "com.apple.audio.AudioConverterService")
+			(xpc-service-name "com.apple.audio.AudioConverterService.HighCapacity")
+			(xpc-service-name "com.apple.audio.analytics.service")
+		)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.spotlight.IndexDelegateAgent")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.system.notification_center")
-		(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
-	)
-)
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "com.apple.ImageIOXPCService")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
+	(require-all
+		(global-name "com.apple.system.notification_center")
+		(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
+	)
+)
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.spotlight.IndexAgent")
 		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
+	(require-all
+		(global-name "com.apple.identityservicesd.idquery.embedded.auth")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+	)
+)
+(allow mach-issue-extension
+	(require-all
+		(global-name "com.apple.spotlight.IndexDelegateAgent")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+	)
+)
+(allow mach-issue-extension
+	(require-all
+		(global-name "com.apple.cmfsyncagent.embedded.auth")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+	)
+)
+(allow mach-issue-extension
+	(require-all
+		(xpc-service-name "com.apple.AGXCompilerService*")
+		(%entitlement-is-bool-true "com.apple.security.ts.opengl-or-metal")
+	)
+)
+(allow mach-issue-extension
+	(require-all
+		(xpc-service-name "com.apple.ImageIOXPCService")
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+	)
+)
+(allow mach-issue-extension
+	(require-all
+		(signing-identifier "com.apple.audio.AudioConverterService")
+		(require-any
+			(global-name "com.apple.fairplayd.versioned")
+			(global-name "com.apple.fairplayd.xpc")
+			(require-any
+				(global-name "com.apple.lskdd")
+				(global-name "com.apple.lskdd.xpc")
+			)
+		)
+	)
+)
+(allow mach-issue-extension
+	(require-all
+		(global-name "com.apple.contactsd")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+	)
+)
+(allow mach-issue-extension
 	(require-any
 		(global-name "com.apple.audio.AudioComponentRegistrar")
 		(global-name "com.apple.audioanalyticsd")

 		(global-name "com.apple.system.notification_center")
 	)
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-any
 		(global-name "*")
 		(global-name "com.apple.analyticsd")

 	)
 )
 
-(allow mach-task-exception-port-set)
+(allow mach-task*)
 
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
 	(%entitlement-is-bool-true "com.apple.security.network.server")
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
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.ubiquity")
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
-	(%entitlement-is-bool-true "com.apple.security.network.server")
-)
-(allow network-bind
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.network.client")
-		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
-	)
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
 		(literal "/private/var/run/lockdown.sock")
 		(%entitlement-is-bool-true "com.apple.security.ts.lockdown-client")
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
 

 		(%entitlement-is-bool-true "com.apple.security.network.client")
 	)
 )
+(allow syscall-unix
+	(require-all
+		(syscall-number SYS_fgetattrlist SYS_issetugid SYS_proc_info_extended_id)
+		(signing-identifier "com.apple.audio.AudioConverterService")
+	)
+)
 (allow syscall-unix
 	(require-all
 		(syscall-number SYS_flock)

 
 (deny system-kas-info)
 
+(allow system-mac-syscall
+	(require-all
+		(mac-syscall-number 65)
+		(signing-identifier "com.apple.audio.AudioConverterService")
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(allow system-mac-syscall
 		(require-all

 )
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
