## com.apple.WebKit.GPU

> Group: ⬆️ Updated

```diff

 
 (deny fs-snapshot-mount)
 
-(deny iokit-get-properties)
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-property "home-button-type")
 		(iokit-registry-entry-class "IOPlatformDevice")
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-registry-entry-class "IOPlatformExpertDevice")
 		(require-any

 		)
 	)
 )
-(allow iokit-get-properties
+(allow iokit*
 	(require-any
 		(iokit-property "AAPL,DisplayPipe")
 		(iokit-property "AAPL,IOGraphics_LER")

 	)
 )
 
-(allow iokit-open*
+(deny iokit-get-properties)
+
+(allow iokit-issue-extension
 	(iokit-connection "IOGPU")
 )
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(iokit-registry-entry-class "IOSurfaceRootUserClient")
 	(apply-message-filter
 		(allow iokit-async-external-method)

 		(allow iokit-external-trap)
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(state-flag "local:tested_version_2.0")

 		(allow iokit-external-trap)
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(state-flag "local:tested_version_2.0")
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-any
 		(iokit-connection "IOGPU")
 		(iokit-registry-entry-class "AGXDeviceUserClient")
 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-any
 		(iokit-connection "IOGPU")
 		(iokit-registry-entry-class "AGXAcceleratorG*")

 	)
 )
 
-(allow ipc-posix-sem-open
+(deny iokit-open-service)
+
+(allow ipc-posix-sem-create
 	(require-any
 		(ipc-posix-name "containermanagerd.fb_check")
 		(ipc-posix-name "purplebuddy.sentinel")
 	)
 )
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(ipc-posix-name "apple.shm.notification_center")
 )
 
-(allow isp-command-send)
+(allow ipc-sysv-shm)
 
-(deny mach-cross-domain-lookup)
+(allow mach*)
 
-(allow mach-lookup
+(deny mach-bootstrap)
+
+(deny mach-derive-port)
+
+(allow mach-issue-extension
 	(with report)
 	(require-any
 		(global-name "com.apple.coremedia.routingsessionmanager.xpc")
 		(global-name "com.apple.coremedia.sts")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.replayd")
 		(extension "com.apple.webkit.extension.mach")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.audio.PhaseXPCServer")
 		(extension "com.apple.webkit.microphone")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.springboard.statusbarservices")
 		(extension "com.apple.webkit.microphone")
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.diagnosticd")
 		(require-not (process-attribute is-apple-signed-executable))
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(require-not (xpc-service-name "com.apple.audio.toolbox.reporting.service"))
 		(require-not (xpc-service-name "*"))

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(global-name "com.apple.CARenderServer")
 		(global-name "com.apple.accessibility.mediaaccessibilityd")

 	)
 )
 
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
-	(target self)
-)
+(deny mach-task-special-port-set)
 
 (deny necp-client-open)
 
-(allow network-outbound
+(allow network-bind
 	(control-name "com.apple.flow-divert")
 )
 
 (deny nvram*)
 
-(deny process-info*)
+(allow process*)
 
-(deny process-info-codesignature)
-(allow process-info-codesignature
+(deny process-codesigning)
+
+(deny process-info*)
+(allow process-info*
 	(target others self)
 )
 
-(deny process-info-dirtycontrol)
-(allow process-info-dirtycontrol
+(deny process-info-codesignature)
+(allow process-info-codesignature
 	(target self)
 )
 
-(allow process-info-pidinfo)
+(deny process-info-dirtycontrol)
+
+(deny process-info-ledger)
+
+(deny process-info-pidinfo)
+(allow process-info-pidinfo
+	(target self)
+)
 
 (deny process-info-pidfdinfo)
 (allow process-info-pidfdinfo

 	(target self)
 )
 
-(deny process-info-rusage)
-(allow process-info-rusage
+(deny process-info-sandbox-container)
+(allow process-info-sandbox-container
 	(target self)
 )
 
-(allow process-info-sandbox-container)
-
-(deny process-info-setcontrol)
-(allow process-info-setcontrol
-	(target self)
-)
+(deny process-iopolicy-set)
 
 (allow signal
 	(target self)
```
