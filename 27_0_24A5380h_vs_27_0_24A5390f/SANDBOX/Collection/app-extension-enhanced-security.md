## app-extension-enhanced-security

> Group: ⬆️ Updated

```diff

 	(process-attribute is-apple-signed-executable)
 )
 
+(deny mach-lookup
+	(global-name "com.apple.webkit.camera")
+)
+
 (deny darwin-notification-post)
 
 (deny dynamic-code-generation

 
 (deny fs-snapshot-mount)
 
-(deny iokit-get-properties)
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
 		(iokit-property "IOSurfaceAcceleratorCapabilitiesDict")
 		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
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
 		(iokit-registry-entry-class "AppleAVD")
 		(require-any

 		)
 	)
 )
-(deny iokit-get-properties
+(deny iokit*
 	(with no-report)
 )
 
-(deny iokit-open-user-client
+(deny iokit-get-properties)
+
+(deny iokit-open*
 	(with no-report)
 )
 
-(deny iokit-open-service
-	(with no-report)
-)
+(deny iokit-open-service)
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(ipc-posix-name "apple.shm.notification_center")
 )
 
-(allow isp-command-send)
+(allow ipc-sysv-shm)
 
-(allow mach-bootstrap
-	(apply-message-filter
-		(allow mach-message-send)
-	)
-)
+(deny mach-bootstrap)
 
-(deny mach-cross-domain-lookup)
+(deny mach-derive-port)
 
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(with no-report)
 	(require-all
 		(require-not (xpc-service-name "*"))

 		(global-name "com.apple.analyticsd")
 	)
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-all
 		(require-not (xpc-service-name "*"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 	)
 )
 
+(allow mach-task*)
+
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
+(deny mach-task-special-port*)
+(allow mach-task-special-port*
 	(target self)
 )
 
-(deny mach-task-special-port*)
-
 (deny mach-task-special-port-get)
-(allow mach-task-special-port-get
-	(target self)
-)
+
+(deny mach-task-special-port-set)
 
 (deny necp-client-open)
 
-(deny network-outbound
+(deny network-bind
 	(with no-report)
 	(literal "/private/var/run/syslog")
 )
-(deny network-outbound)
+(deny network-bind)
 
 (deny nvram*)
 
-(deny process-info*)
+(allow process*)
 
-(deny process-info-codesignature
+(deny process-codesigning)
+
+(deny process-info*
 	(with no-report)
 )
 
+(deny process-info-codesignature)
+(allow process-info-codesignature
+	(target self)
+)
+
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

 						SYS_sigsuspend_nocancel
 						SYS_change_fdguard_np
 						SYS_getattrlistbulk
+						SYS_renameat
 						SYS_faccessat
 						SYS_mkdirat
+						SYS_renameatx_np
 						SYS___channel_open
 						SYS_setattrlistat
 						SYS_os_fault_with_payload
```
