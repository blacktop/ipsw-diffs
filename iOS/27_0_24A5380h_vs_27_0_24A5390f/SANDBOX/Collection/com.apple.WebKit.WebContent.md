## com.apple.WebKit.WebContent

> Group: ⬆️ Updated

```diff

 
 (allow coalition-info)
 
+(deny mach-lookup
+	(global-name "com.apple.webkit.camera")
+)
+
 (deny darwin-notification-post)
 (allow darwin-notification-post
 	(require-any

 
 (deny fs-snapshot-mount)
 
-(deny iokit-get-properties)
-(allow iokit-get-properties
+(allow iokit*
 	(require-all
 		(iokit-registry-entry-class "IOMobileFramebuffer")
 		(require-any

 		)
 	)
 )
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
 
-(deny iokit-open-user-client
+(deny iokit-get-properties)
+
+(deny iokit-open*
 	(with no-report)
 	(iokit-registry-entry-class "AppleJPEGDriverUserClient")
 )
-(deny iokit-open-user-client)
+(deny iokit-open*)
 
-(deny iokit-open-service
+(deny iokit-open-user-client
 	(with no-report)
 )
 
-(allow isp-command-send)
+(deny iokit-open-service)
 
-(allow mach-bootstrap
-	(apply-message-filter
-		(allow mach-message-send)
-	)
-)
+(allow ipc-sysv-shm)
 
-(deny mach-cross-domain-lookup)
+(deny mach-bootstrap)
 
-(deny mach-lookup
+(deny mach-derive-port)
+
+(deny mach-issue-extension
 	(with no-report)
 	(require-all
 		(require-not (global-name "com.apple.lsd.mapdb"))

 		(global-name "com.apple.logd")
 	)
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-all
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.diagnosticd"))

 	)
 )
 
-(allow mach-register
+(allow mach-priv-task-port
 	(require-all
 		(extension "com.apple.webkit.mach-bootstrap")
 		(local-name "com.apple.iphone.axserver")
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
-	(target self)
-)
-
-(deny mach-task-special-port-get)
-(allow mach-task-special-port-get
+(deny mach-task-special-port*)
+(allow mach-task-special-port*
 	(require-any
 		(require-not (state-flag "local:WebContentProcessLaunched"))
 		(target self)
 	)
 )
 
-(deny mach-task-special-port-set)
-(allow mach-task-special-port-set)
-(deny mach-task-special-port-set
+(deny mach-task-special-port-get)
+(allow mach-task-special-port-get)
+(deny mach-task-special-port-get
 	(state-flag "local:WebContentProcessLaunched")
 )
 
+(deny mach-task-special-port-set)
+
 (deny necp-client-open)
 
-(allow network-outbound
+(allow network-bind
 	(control-name "com.apple.flow-divert")
 )
 
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
 

 	(target self)
 )
 
-(deny process-info-rusage)
-(allow process-info-rusage
+(deny process-info-sandbox-container)
+(allow process-info-sandbox-container
 	(target self)
 )
 
-(allow process-info-sandbox-container)
+(deny process-iopolicy*)
 
-(deny process-info-setcontrol)
-(allow process-info-setcontrol
+(allow process-legacy-codesigning-entitlements-der-blob-get
 	(target self)
 )
 
-(deny process-iopolicy-get)
-
-(deny process-iopolicy-set)
-
-(allow process-legacy-codesigning-entitlements-blob-get)
-
-(allow process-legacy-codesigning-entitlements-der-blob-get)
-
-(allow process-legacy-codesigning-identity-get
-	(target self)
-)
-
-(allow process-legacy-codesigning-status-get)
-
-(allow process-legacy-codesigning-status-set
+(allow process-legacy-codesigning-status-get
 	(target self)
 )
 
```
