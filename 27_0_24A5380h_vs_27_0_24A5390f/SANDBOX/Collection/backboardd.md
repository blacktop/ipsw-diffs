## backboardd

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
 	(require-all
 		(system-attribute virtual-device)
 		(iokit-registry-entry-class "IOSurfaceAcceleratorParavirtClient")
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
 		(require-any
 			(iokit-property "GlobalConfig")

 		)
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "IOHIDResourceDeviceUserClient")
 		(require-any

 		)
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "IOPMrootDomain")
 		(require-any

 		)
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "AppleEmbeddedBluetoothHaptics")
 		(require-any

 		)
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-property "InSession")
 		(iokit-registry-entry-class "VaxholmDriver")
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-property "KeyboardBacklight")
 		(iokit-registry-entry-class "IOResources")
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-property "hid-merge-personality")
 		(iokit-registry-entry-class "AppleHIDTransportBootloaderHBPP")
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "AppleARMBacklight")
 		(require-any

 		)
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "AppleEmbeddedBluetoothForce")
 		(require-any

 		)
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "AppleMultitouchTimestampSyncUC")
 		(require-any

 		)
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "IOHIDLibUserClient")
 		(require-any

 		)
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "AppleMultitouchDevice")
 		(require-any

 		)
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(require-any
 			(iokit-property "AOTEnable")

 		)
 	)
 )
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-any
 		(iokit-registry-entry-class "IOHIDEventServiceUserClient")
 		(iokit-registry-entry-class "PSVR2SenseDeviceHIDEventServerUserClient")
 	)
 )
 
-(allow ipc-posix-sem*
+(allow ipc-posix*
 	(require-any
 		(extension "com.apple.sandbox.application-group")
 		(ipc-posix-name "backboardd.firstboot_check")

 	)
 )
 
+(allow ipc-posix-sem-wait
+	(require-any
+		(extension "com.apple.sandbox.application-group")
+		(ipc-posix-name "com.apple.AttentionAwareness")
+	)
+)
+
+(allow ipc-posix-shm*
+	(require-all
+		(ipc-posix-name "apple.shm.notification_center")
+		(%entitlement-is-bool-true "com.apple.security.on-demand-install-capable")
+	)
+)
 (allow ipc-posix-shm*
 	(require-any
 		(extension "com.apple.sandbox.application-group")

 	)
 )
 
-(allow ipc-posix-shm-read-data
-	(require-all
-		(ipc-posix-name "apple.shm.notification_center")
-		(%entitlement-is-bool-true "com.apple.security.on-demand-install-capable")
-	)
-)
 (allow ipc-posix-shm-read-data
 	(require-any
 		(extension "com.apple.sandbox.application-group")

 	)
 )
 
-(allow isp-command-send)
+(allow ipc-posix-shm-write*
+	(require-any
+		(extension "com.apple.sandbox.application-group")
+		(ipc-posix-name "com.apple.AttentionAwareness")
+	)
+)
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny lsopen
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
 		(extension "com.apple.sandbox.application-group")
 		(extension "com.apple.security.exception.mach-register.global-name")
 	)
 )
 
-(allow mach-task-exception-port-set)
-
-(allow mach-task-inspect
+(allow mach-task-exception-port-set
 	(target self)
 )
 
-(allow mach-task-name)
-
-(allow mach-task-read
+(allow mach-task-name
 	(target self)
 )
 
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
 
 (allow network-bind
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
 
-(allow nvram-get)
+(allow nvram-delete)
 
-(allow nvram-set
+(allow nvram-get
 	(require-any
 		(nvram-variable "40A0DDD2-77F8-4392-B4A3-1E7304206516:backlight-nits")
 		(nvram-variable "backlight-level")

 	)
 )
 
-(allow process-codesigning)
-
-(allow process-info-codesignature)
-
-(allow process-info-pidinfo)
-
-(allow process-iopolicy*)
+(allow process*)
 
 (allow sandbox-check)
 

 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
+		SYS_renameatx_np
 		SYS_persona
 		SYS_work_interval_ctl
 		SYS_necp_open

 )
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
