## com.apple.WebKit.WebContent.Development

> Group: ⬆️ Updated

```diff

 
 (allow coalition-info)
 
+(deny mach-lookup
+	(global-name "com.apple.webkit.camera")
+)
+
 (deny darwin-notification-post)
 (allow darwin-notification-post
 	(with report)

 
 (deny fs-snapshot-mount)
 
-(deny iokit-get-properties)
-(allow iokit-get-properties
+(allow iokit*
 	(with report)
 	(system-attribute developer-mode)
 )
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
 		(iokit-registry-entry-class "IOPlatformDevice")
 		(iokit-property "home-button-type")
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
 
-(allow iokit-open-user-client
+(deny iokit-get-properties)
+
+(allow iokit-open*
 	(with report)
 	(system-attribute developer-mode)
 )
 
 (deny iokit-open-service)
-(allow iokit-open-service
+
+(allow ipc-sysv-shm)
+
+(deny mach-bootstrap)
+
+(deny mach-derive-port)
+
+(allow mach-issue-extension
 	(with report)
 	(system-attribute developer-mode)
 )
 
-(allow isp-command-send)
-
-(allow mach-bootstrap
-	(apply-message-filter
-		(allow mach-message-send)
-	)
-)
-
-(deny mach-cross-domain-lookup)
-
-(allow mach-lookup
-	(with report)
-	(system-attribute developer-mode)
-)
-
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
+(deny mach-task-special-port*)
+(allow mach-task-special-port*
+	(with report)
+	(system-attribute developer-mode)
+)
+(allow mach-task-special-port*
+	(require-any
+		(require-not (state-flag "local:WebContentProcessLaunched"))
+		(target self)
+	)
 )
 
 (deny mach-task-special-port-get)

 	(with report)
 	(system-attribute developer-mode)
 )
-(allow mach-task-special-port-get
-	(require-any
-		(require-not (state-flag "local:WebContentProcessLaunched"))
-		(target self)
-	)
+(allow mach-task-special-port-get)
+(deny mach-task-special-port-get
+	(state-flag "local:WebContentProcessLaunched")
 )
 
 (deny mach-task-special-port-set)
-(allow mach-task-special-port-set
-	(with report)
-	(system-attribute developer-mode)
-)
-(allow mach-task-special-port-set)
-(deny mach-task-special-port-set
-	(state-flag "local:WebContentProcessLaunched")
-)
 
 (deny necp-client-open)
 
 (deny nvram*)
 
+(allow process*)
+
+(deny process-codesigning)
+
+(allow process-fork
+	(with report)
+	(system-attribute developer-mode)
+)
+
 (deny process-info*)
 (allow process-info*
 	(with report)
 	(system-attribute developer-mode)
 )
 
-(deny process-info-dirtycontrol)
-(allow process-info-dirtycontrol
+(deny process-info-codesignature)
+(allow process-info-codesignature
 	(with report)
 	(system-attribute developer-mode)
 )
-(allow process-info-dirtycontrol
+(allow process-info-codesignature
+	(target self)
+)
+
+(deny process-info-listpids)
+(allow process-info-listpids
+	(with report)
+	(system-attribute developer-mode)
+)
+(allow process-info-listpids
 	(target self)
 )
 

 	(target self)
 )
 
-(deny process-info-rusage)
-(allow process-info-rusage
+(deny process-info-sandbox-container)
+(allow process-info-sandbox-container
 	(with report)
 	(system-attribute developer-mode)
 )
-(allow process-info-rusage
+(allow process-info-sandbox-container
 	(target self)
 )
 
-(deny process-info-setcontrol)
-(allow process-info-setcontrol
+(deny process-iopolicy-set)
+(allow process-iopolicy-set
 	(with report)
 	(system-attribute developer-mode)
 )
-(allow process-info-setcontrol
-	(target self)
-)
 
 (allow process-legacy-codesigning*
 	(with report)
 	(system-attribute developer-mode)
 )
 
-(allow process-legacy-codesigning-entitlements-blob-get)
-
-(allow process-legacy-codesigning-entitlements-der-blob-get)
-
-(allow process-legacy-codesigning-identity-get
+(allow process-legacy-codesigning-entitlements-der-blob-get
 	(with report)
 	(system-attribute developer-mode)
 )
-(allow process-legacy-codesigning-identity-get
+(allow process-legacy-codesigning-entitlements-der-blob-get
 	(target self)
 )
 
-(allow process-legacy-codesigning-status-get)
-
-(allow process-legacy-codesigning-status-set
+(allow process-legacy-codesigning-status-get
 	(with report)
 	(system-attribute developer-mode)
 )
-(allow process-legacy-codesigning-status-set
+(allow process-legacy-codesigning-status-get
 	(target self)
 )
 
```
