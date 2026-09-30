## blastdoor-thumbnails

> Group: ⬆️ Updated

```diff

 
 (allow coalition-info)
 
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
 	(global-name "com.apple.analyticsd")
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
 
-(allow process-legacy-codesigning-entitlements-blob-get)
+(deny process-info-pidfileportinfo)
 
-(allow process-legacy-codesigning-entitlements-der-blob-get)
+(deny process-info-sandbox-container)
 
-(allow process-legacy-codesigning-status-get)
+(deny process-iopolicy-set)
 
 (allow signal
 	(target self)

 						SYS_fsgetpath
 						SYS_change_fdguard_np
 						SYS_getattrlistbulk
+						SYS_renameat
 						SYS_faccessat
 						SYS_fstatat64
 						SYS_mkdirat
+						SYS_renameatx_np
 						SYS_setattrlistat
 						SYS_os_fault_with_payload
 						SYS_memorystatus_available_memory

 						SYS_fsgetpath
 						SYS_change_fdguard_np
 						SYS_getattrlistbulk
+						SYS_renameat
 						SYS_faccessat
 						SYS_fstatat64
 						SYS_mkdirat
+						SYS_renameatx_np
 						SYS_setattrlistat
 						SYS_os_fault_with_payload
 						SYS_memorystatus_available_memory
```
