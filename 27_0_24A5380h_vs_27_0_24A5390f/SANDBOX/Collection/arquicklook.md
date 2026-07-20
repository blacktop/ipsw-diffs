## arquicklook

> Group: ⬆️ Updated

```diff

 	(extension-class "com.apple.webkit.mach-bootstrap")
 )
 
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-registry-entry-class "IOService")
 		(require-any

 		)
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
 		(iokit-registry-entry-class "IOPlatformDevice")
 		(require-any

 		)
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
 		(iokit-registry-entry-class "AppleJPEGDriver")
 		(require-any

 		)
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-registry-entry-class "AppleAVD")
 		(require-any

 		)
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-property "DeviceProperties")
 		(require-any

 		)
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-registry-entry-class "AppleJPEGDriver")
 		(require-any

 		)
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-property "ane-type")
 		(require-any

 		)
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-any
 		(iokit-property "AppleJPEGSupportsAppleInterchangeFormats")
 		(iokit-property "BaseAddressAlignmentRequirement")

 	)
 )
 
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
 
-(allow ipc-posix-sem-open
+(allow ipc-posix-sem-create
 	(ipc-posix-name "containermanagerd.fb_check")
 )
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.*")
 		(ipc-posix-name "apple.shm.notification_center")
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
 
-(allow mach-derive-port)
+(allow mach-cross-domain-lookup)
 
-(allow mach-issue-extension
+(allow mach-host-special-port-set
 	(extension-class "com.apple.webkit.extension.mach")
 )
 
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(xpc-service-name "com.apple.WebKit*")
 		(signing-identifier "com.apple.AssetViewer.ASVAssetViewer")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")

 		(global-name "com.apple.ak.authorizationservices.xpc")
 		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.appleneuralengine")
+		(global-name "com.apple.appprotectiond.viewsubjectinfo")
 		(global-name "com.apple.assistant.dictation")
 		(global-name "com.apple.audio.AURemoteIOServer")
 		(global-name "com.apple.audio.AudioComponentRegistrar")

 		(xpc-service-name "com.apple.MTLCompilerService")
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
 		(local-name "com.apple.iphone.axserver")
 	)
 )
 
-(allow mach-task-exception-port-set)
+(allow mach-task*)
+
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

 		)
 	)
 )
-(deny network-outbound
+(deny network-bind
 	(with no-report)
 	(literal "/private/var/run/syslog")
 )
 
-(allow process-codesigning)
+(allow process*)
 
-(allow process-info-dirtycontrol
+(allow process-info-codesignature
 	(target self)
 )
 
-(allow process-info-pidinfo
+(allow process-info-listpids
 	(target self)
 )
 
-(allow process-info-rusage
+(allow process-info-pidfileportinfo
 	(target self)
 )
 
-(allow process-info-setcontrol
+(allow process-info-sandbox-container
 	(target self)
 )
 
-(allow process-iopolicy*)
-
 (allow sandbox-check)
 
 (allow signal

 		SYS_connectx
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fchmodat
 		SYS_fchownat

 		SYS_bsdthread_ctl
 		SYS_csrctl
 		SYS_guarded_open_dprotected_np
+		SYS_renameatx_np
 		SYS_mremap_encrypted
 		SYS_persona
 		SYS_mach_eventlink_signal_wait_until

 )
 
 (allow user-preference-write
-	(preference-domain "com.apple.AssetViewer")
+	(require-any
+		(preference-domain "com.apple.AssetViewer")
+		(preference-domain "com.apple.AssetViewer.ASVAssetViewer")
+	)
 )
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
