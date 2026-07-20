## cfprefsd

> Group: ⬆️ Updated

```diff

 
 (allow fs-snapshot-mount)
 
-(allow iokit-get-properties)
+(allow iokit*)
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(extension "com.apple.security.exception.iokit-user-client-class")
 )
 
-(allow iokit-open-service)
-
-(allow ipc-posix-shm*
+(allow ipc-posix-sem-wait
 	(ipc-posix-name "apple.cfprefs.*")
 )
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(ipc-posix-name "apple.shm.notification_center")
 		(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
 	)
 )
+(allow ipc-posix-shm*
+	(ipc-posix-name "apple.cfprefs.*")
+)
+
 (allow ipc-posix-shm-read-data
 	(ipc-posix-name "apple.cfprefs.*")
 )
 
-(allow isp-command-send)
+(allow ipc-posix-shm-write*
+	(ipc-posix-name "apple.cfprefs.*")
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
+(allow mach-task-exception-port-set
+	(target self)
+)
 
 (allow mach-task-inspect
 	(target self)

 	(target self)
 )
 
-(allow mach-task-read
+(allow process*)
+
+(allow process-fork
 	(target self)
 )
 
-(allow mach-task-special-port*)
-
-(allow necp-client-open)
-
-(allow process-codesigning)
-
-(allow process-info*
+(allow process-info-codesignature
 	(target self)
 )
 
-(allow process-info-codesignature)
+(allow process-info-dirtycontrol
+	(target self)
+)
 
-(allow process-info-pidinfo)
+(allow process-info-ledger
+	(target self)
+)
 
-(allow process-info-sandbox-container)
+(allow process-info-pidinfo
+	(target self)
+)
 
-(allow process-iopolicy*)
+(allow process-info-pidfdinfo
+	(target self)
+)
+
+(allow process-info-pidfileportinfo
+	(target self)
+)
+
+(allow process-info-sandbox-container
+	(target self)
+)
 
 (allow sandbox-check)
 

 		SYS_unlinkat
 		SYS_mkdirat
 		SYS_guarded_open_dprotected_np
+		SYS_renameatx_np
 		SYS_persona
 		SYS_ulock_wait
 		SYS_ulock_wake

 (allow system-privilege)
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
