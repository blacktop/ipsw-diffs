## com.apple.WebKit.Networking

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
 	(iokit-property "IORegistryEntryPropertyKeys")
 )
 
-(allow iokit-open-user-client
+(deny iokit-get-properties)
+
+(allow iokit-open*
 	(iokit-registry-entry-class "AppleKeyStoreUserClient")
 )
 
-(deny iokit-open-service)
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
 	(require-all
 		(global-name "com.apple.imagent.EnhancedLinkSecurityStore")
 		(require-not (state-flag "BlockEnhancedSecurityLinks"))
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))
 		(require-not (global-name "com.apple.hangtracerd"))

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.diagnosticd")
 		(require-any

 		)
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
 	(control-name "com.apple.flow-divert")
 )
-(allow network-outbound
+(allow network-bind
 	(require-all
 		(require-not (remote tcp "localhost:62078"))
 		(require-any

 
 (deny nvram*)
 
-(deny process-info*)
+(allow process*)
 
-(deny process-info-codesignature)
-(allow process-info-codesignature
+(deny process-codesigning)
+
+(deny process-info*)
+(allow process-info*
 	(require-any
 		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
 		(target others self)
 	)
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
+	(require-any
+		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
+		(target self)
+	)
+)
 
 (deny process-info-pidfdinfo)
 (allow process-info-pidfdinfo

 	)
 )
 
-(deny process-info-rusage)
-(allow process-info-rusage
-	(require-any
-		(%entitlement-is-bool-true "com.apple.security.exception.process-info")
-		(target self)
-	)
-)
-
-(allow process-info-sandbox-container)
-
-(deny process-info-setcontrol)
-(allow process-info-setcontrol
+(deny process-info-sandbox-container)
+(allow process-info-sandbox-container
 	(target self)
 )
 
+(deny process-iopolicy-set)
+
 (allow signal
 	(target self)
 )
```
