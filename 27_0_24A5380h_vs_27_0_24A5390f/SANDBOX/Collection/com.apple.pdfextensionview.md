## com.apple.pdfextensionview

> Group: ⬆️ Updated

```diff

 
 (allow coalition-info)
 
+(deny mach-lookup
+	(global-name "com.apple.webkit.camera")
+)
+
 (deny darwin-notification-post)
 
 (deny dynamic-code-generation)

 
 (deny fs-snapshot-mount)
 
-(deny iokit-get-properties)
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-property "IOSurfaceAcceleratorCapabilitiesDict")
 		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-registry-entry-class "AGXAcceleratorG*")
 		(require-any

 		)
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-property "display-corner-radius")
 		(iokit-registry-entry-class "IOPlatformDevice")
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(require-any
 			(iokit-property "large-format-phone")

 		(iokit-registry-entry-class "IOPlatformDevice")
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
 		(iokit-property "device-colors")
 		(iokit-registry-entry-class "IOPlatformDevice")
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
 		(require-any
 			(iokit-property "compatible-app-variant")

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
 		(iokit-registry-entry-class "AGXDeviceUserClient")
 		(iokit-registry-entry-class "AppleJPEGDriverUserClient")

 		(iokit-registry-entry-class "IOSurfaceRootUserClient")
 	)
 )
-(autobox iokit-open-user-client)
+(autobox iokit-open*)
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AGXAcceleratorG*")
 		(iokit-registry-entry-class "AppleJPEGDriver")

 		(iokit-registry-entry-class "IOSurfaceRoot")
 	)
 )
+(autobox iokit-open-user-client)
+
 (autobox iokit-open-service)
 
-(autobox iokit-set-properties)
-
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.*")
 		(ipc-posix-name "apple.shm.notification_center")
 	)
 )
 
-(allow isp-command-send)
+(allow ipc-sysv-shm)
 
 (deny mach-bootstrap)
 
-(deny mach-cross-domain-lookup)
+(deny mach-derive-port)
 
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(global-name "com.apple.CARenderServer")
 		(global-name "com.apple.MTLCompilerService")

 		(global-name "com.apple.system.notification_center")
 	)
 )
-(autobox mach-lookup)
+(autobox mach-issue-extension)
 
-(allow mach-register
+(allow mach-priv-task-port
 	(local-name "com.apple.iphone.axserver")
 )
 
-(allow mach-task-inspect
+(allow mach-task*)
+
+(deny mach-task-exception-port-set)
+(allow mach-task-exception-port-set
 	(target self)
 )
 
-(allow mach-task-name
+(allow mach-task-inspect
 	(target others self)
 )
 
-(allow mach-task-read
+(allow mach-task-name
 	(target self)
 )
 
+(deny mach-task-special-port-set)
+
 (deny necp-client-open)
 
-(allow network-outbound
+(allow network-bind
 	(require-any
 		(control-name "com.apple.flow-divert")
 		(literal "/private/var/run/syslog")

 
 (deny nvram*)
 
-(deny nvram-get)
-(allow nvram-get
+(deny nvram-delete)
+(allow nvram-delete
 	(nvram-variable "emu")
 )
 
+(allow process*)
+
+(deny process-codesigning)
+
 (deny process-info*)
 
-(deny process-info-pidinfo)
-(allow process-info-pidinfo
+(deny process-info-listpids)
+(allow process-info-listpids
 	(target others self)
 )
 
-(allow process-info-sandbox-container)
+(deny process-info-sandbox-container)
+(allow process-info-sandbox-container
+	(target self)
+)
 
-(deny process-info-setcontrol)
-(allow process-info-setcontrol
+(deny process-iopolicy-set)
+
+(allow process-legacy-codesigning-entitlements-blob-get
 	(target self)
 )
 

 	(target self)
 )
 
-(allow process-legacy-codesigning-identity-get
-	(target self)
-)
-
-(allow process-legacy-codesigning-status-get
+(allow process-legacy-codesigning-status*
 	(target self)
 )
 

 		SYS_connectx
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fchmodat
 		SYS_fchownat

 		SYS_unlinkat
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_renameatx_np
 		SYS_persona
 		SYS_getentropy
 		SYS_ulock_wait
```
