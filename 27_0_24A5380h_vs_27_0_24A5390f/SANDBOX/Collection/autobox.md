## autobox

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
-		(%entitlement-is-bool-true "com.apple.security.network.client")
-	)
-)
-(allow iokit-open-service
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-		(iokit-registry-entry-class "AGXAcceleratorG*")
-	)
-)
-(allow iokit-open-service
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.framebuffer-access")
-		(iokit-registry-entry-class "AGXAcceleratorG*")
-	)
-)
-(allow iokit-open-service
-	(require-all
-		(iokit-registry-entry-class "AppleKeyStore")
-		(%entitlement-is-bool-true "com.apple.security.ts.mobile-keybag-access")
-	)
-)
-(allow iokit-open-service
-	(require-all
-		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
 		(require-any
-			(iokit-registry-entry-class "AGXAcceleratorG*")
-			(require-all
-				(%entitlement-is-bool-true "com.apple.security.ts.render-images")
-				(require-any
-					(iokit-registry-entry-class "AppleJPEGDriver")
-					(iokit-registry-entry-class "IOSurfaceRoot")
-				)
-			)
-			(require-any
-				(iokit-registry-entry-class "AppleCLCD*")
-				(iokit-registry-entry-class "AppleParavirtDisplay*")
-				(iokit-registry-entry-class "AppleParavirtGPU*")
-			)
+			(%entitlement-is-bool-true "com.apple.security.network.client")
+			(%entitlement-is-bool-true "com.apple.security.ts.mobile-keybag-access")
 		)
 	)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
+	(require-all
+		(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		(require-any
+			(iokit-registry-entry-class "AppleJPEGDriver")
+			(iokit-registry-entry-class "IOSurfaceRoot")
+		)
+	)
+)
+(allow iokit-open-user-client
+	(require-all
+		(iokit-registry-entry-class "AGXAcceleratorG*")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+	)
+)
+(allow iokit-open-user-client
 	(require-all
 		(%entitlement-is-bool-true "com.apple.security.ts.ane-client")
 		(require-any

 		)
 	)
 )
-(allow iokit-open-service
-	(require-all
-		(iokit-registry-entry-class "AppleJPEGDriver")
-		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
-	)
-)
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-all
 		(iokit-registry-entry-class "IOPMrootDomain")
 		(require-any
 			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-client")
 			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-receive-file")
 			(%entitlement-is-bool-true "com.apple.security.ts.identity-services-send-file")
-			(%entitlement-is-bool-true "com.apple.security.ts.power-assertions")
 		)
 	)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
+	(require-all
+		(iokit-registry-entry-class "AppleJPEGDriver")
+		(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+	)
+)
+(allow iokit-open-user-client
+	(require-all
+		(require-any
+			(iokit-registry-entry-class "AppleCLCD*")
+			(iokit-registry-entry-class "AppleParavirtDisplay*")
+			(iokit-registry-entry-class "AppleParavirtGPU*")
+		)
+		(require-any
+			(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
+			(%entitlement-is-bool-true "com.apple.security.ts.framebuffer-access")
+			(%entitlement-is-bool-true "com.apple.security.ts.render-images")
+		)
+	)
+)
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

 	(global-name "com.apple.identityservicesd.idquery.embedded.auth")
 	(%entitlement-is-bool-true "com.apple.security.ts.addressbook")
 ))
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 	(signing-identifier "com.apple.*")
 	(require-any

 	)
 )
 )
-(deny mach-lookup
+(deny mach-issue-extension
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
 	(require-all
 		(literal "/private/var/run/lockdown.sock")
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
+(allow process*)
+
+(allow process-info-listpids
+	(target self)
+)
+
+(allow process-info-sandbox-container
+	(target self)
+)
+
+(allow process-legacy-codesigning-entitlements-blob-get
+	(require-any
+		(%entitlement-is-bool-true "com.apple.security.ts.get-code-signing-data")
+		(target self)
 	)
 )
 
-(allow process-codesigning)
-
-(allow process-info-pidinfo
-	(target self)
-)
-
-(allow process-info-setcontrol
-	(target self)
-)
-
-(allow process-iopolicy*)
-
 (allow process-legacy-codesigning-entitlements-der-blob-get
 	(require-any
 		(%entitlement-is-bool-true "com.apple.security.ts.get-code-signing-data")

 	)
 )
 
-(allow process-legacy-codesigning-identity-get
-	(require-any
-		(%entitlement-is-bool-true "com.apple.security.ts.get-code-signing-data")
-		(target self)
-	)
-)
-
-(allow process-legacy-codesigning-status-get
+(allow process-legacy-codesigning-status*
 	(require-any
 		(%entitlement-is-bool-true "com.apple.security.ts.get-code-signing-data")
 		(target self)

 (deny user-preference-write)
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
