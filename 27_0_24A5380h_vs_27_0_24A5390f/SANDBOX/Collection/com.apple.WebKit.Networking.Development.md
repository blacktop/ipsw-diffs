## com.apple.WebKit.Networking.Development

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
 	(iokit-property "IORegistryEntryPropertyKeys")
 )
 
-(allow iokit-open-user-client
+(deny iokit-get-properties)
+
+(allow iokit-open*
 	(with report)
 	(system-attribute developer-mode)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(iokit-registry-entry-class "AppleKeyStoreUserClient")
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(with report)
 	(system-attribute developer-mode)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(iokit-registry-entry-class "AppleKeyStore")
 )
 
-(allow ipc-posix-sem-open
+(deny iokit-open-service)
+
+(allow ipc-posix-sem-create
 	(ipc-posix-name "containermanagerd.fb_check")
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
 	(system-attribute developer-mode)
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
 		(global-name "com.apple.imagent.EnhancedLinkSecurityStore")
 		(require-not (state-flag "BlockEnhancedSecurityLinks"))
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(global-name "com.apple.AppSSO.service-xpc")
 		(global-name "com.apple.FileProvider")

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
+(deny necp-client-open)
+(allow necp-client-open
+	(require-any
+		(local tcp "*:*")
+		(local udp "*:*")
+		(remote tcp "*:*")
+		(remote udp "*:*")
+	)
 )
 
 (allow network*

 	)
 )
 
-(allow network-outbound
+(allow network-bind
 	(require-any
 		(control-name "com.apple.flow-divert")
 		(control-name "com.apple.netsrc")

 
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
+(allow process-info*
+	(require-any
+		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
+		(target others self)
+	)
+)
 
 (deny process-info-codesignature)
 (allow process-info-codesignature

 	(system-attribute developer-mode)
 )
 (allow process-info-codesignature
-	(require-any
-		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
-		(target others self)
-	)
+	(target self)
 )
 
 (deny process-info-dirtycontrol)

 	(with report)
 	(system-attribute developer-mode)
 )
-(allow process-info-dirtycontrol
-	(target self)
+
+(deny process-info-ledger)
+(allow process-info-ledger
+	(with report)
+	(system-attribute developer-mode)
+)
+
+(deny process-info-pidinfo)
+(allow process-info-pidinfo
+	(with report)
+	(system-attribute developer-mode)
+)
+(allow process-info-pidinfo
+	(require-any
+		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
+		(target self)
+	)
 )
 
 (deny process-info-pidfdinfo)

 	)
 )
 
-(deny process-info-rusage)
-(allow process-info-rusage
+(deny process-info-sandbox-container)
+(allow process-info-sandbox-container
 	(with report)
 	(system-attribute developer-mode)
 )
-(allow process-info-rusage
-	(require-any
-		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
-		(target self)
-	)
-)
-
-(deny process-info-setcontrol)
-(allow process-info-setcontrol
-	(with report)
-	(system-attribute developer-mode)
-)
-(allow process-info-setcontrol
+(allow process-info-sandbox-container
 	(target self)
 )
 
+(deny process-iopolicy-set)
+
 (allow signal
 	(target self)
 )
```
