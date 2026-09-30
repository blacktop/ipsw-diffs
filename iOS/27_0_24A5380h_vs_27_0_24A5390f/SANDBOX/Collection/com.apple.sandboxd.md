## com.apple.sandboxd

> Group: ⬆️ Updated

```diff

 	(with report)
 )
 
-(allow iokit-get-properties)
+(allow iokit*)
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(extension "com.apple.security.exception.iokit-user-client-class")
 )
 
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(with report)
 )
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(%entitlement-is-present "com.apple.security.exception.iokit-user-client-class")
 )
 
+(allow ipc-posix-sem-wait
+	(ipc-posix-name "apple.shm.notification_center")
+)
+
 (allow ipc-posix-shm*
 	(ipc-posix-name "apple.shm.notification_center")
 )
 
-(allow isp-command-send)
+(allow ipc-sysv-shm)
 
-(deny job-creation)
+(deny isp-command-send)
 
-(deny lsopen
+(deny job-creation
 	(profile-flag "deny-lsopen")
 )
 
-(allow mach-bootstrap
+(allow mach*
 	(with report)
 )
 
-(allow mach-cross-domain-lookup
-	(with report)
-)
+(allow mach-cross-domain-lookup)
 
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
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")

 		(xpc-service-name "*")
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
 	(extension "com.apple.security.exception.mach-register.global-name")
 )
 
-(allow mach-task-exception-port-set)
+(allow mach-task*)
 
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
+(allow network-outbound
+	(with report)
+)
 
 (allow nvram*
 	(with report)
 )
 
-(allow process-codesigning)
+(allow process*)
+
+(allow process-fork
+	(with report)
+)
 
 (allow process-info*
 	(with report)
 )
-
-(allow process-info-codesignature
-	(with report)
-)
-(allow process-info-codesignature
-	(target self)
-)
-
-(allow process-info-dirtycontrol
-	(with report)
-)
-(allow process-info-dirtycontrol
+(allow process-info*
 	(target self)
 )
 
 (allow process-info-ledger
 	(with report)
 )
-(allow process-info-ledger
-	(target self)
-)
 
-(allow process-info-pidinfo)
-
-(allow process-info-pidfdinfo
-	(with report)
-)
-(allow process-info-pidfdinfo
-	(target self)
-)
-
-(allow process-info-pidfileportinfo
-	(with report)
-)
-(allow process-info-pidfileportinfo
-	(target self)
-)
-
-(allow process-info-rusage
-	(with report)
-)
-(allow process-info-rusage
-	(target self)
-)
-
-(allow process-info-setcontrol
-	(with report)
-)
-(allow process-info-setcontrol
-	(target self)
-)
-
-(allow process-iopolicy*)
-
-(allow process-legacy-codesigning-entitlements-der-blob-get
+(allow process-legacy-codesigning-entitlements-blob-get
 	(target others)
 )
 

 (allow system-privilege)
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
