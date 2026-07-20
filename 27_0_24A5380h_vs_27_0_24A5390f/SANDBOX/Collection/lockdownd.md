## lockdownd

> Group: ⬆️ Updated

```diff

 
 (allow fs-snapshot-mount)
 
-(allow iokit-get-properties)
+(allow iokit*)
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-any
 		(extension "com.apple.security.exception.iokit-user-client-class")
 		(iokit-registry-entry-class "ASPUserClient")

 	)
 )
 
-(allow iokit-open-service)
-
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-registry-entry-class "IOUSBDeviceController")
 		(iokit-property "USBDeviceCommand")
 	)
 )
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(ipc-posix-name "apple.shm.notification_center")
 		(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
 	)
 )
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(ipc-posix-name "/com.apple.AppSSO.version")
 )
 
+(allow ipc-sysv-shm)
+
 (allow isp-command-send)
 
-(allow job-creation)
-
-(deny lsopen
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
 		(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.internal.*")
 		(require-any

 		(system-attribute internal-build)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(require-any
 			(global-name "com.apple.Ancd.mobile")

 		(system-attribute internal-build)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")

 		(global-name #"com.apple.dietappleh([0-9])+camerad")
 	)
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(xpc-service-name "*")
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
-	(target self)
-)
-
-(allow mach-task-special-port*)
-
-(allow necp-client-open)
-
-(allow network*
+(allow necp-client-open
 	(require-any
 		(literal "/private/var/run/lockdown.sock")
 		(subpath "/private/var/run/lockdown")
 	)
 )
 
-(allow network-inbound
+(allow network*
 	(require-any
 		(literal "/private/var/run/lockdown.sock")
 		(local tcp "*:*")

 )
 
 (allow network-bind
-	(require-any
-		(literal "/private/var/run/lockdown.sock")
-		(local tcp "*:*")
-		(subpath "/private/var/run/lockdown")
-	)
-)
-
-(allow network-outbound
 	(require-any
 		(control-name "com.apple.flow-divert")
 		(control-name "com.apple.netsrc")

 	)
 )
 
-(allow nvram-get)
+(allow nvram-delete)
 
-(allow nvram-set
+(allow nvram-get
 	(nvram-variable "auto-boot")
 )
 
-(allow process-codesigning)
+(allow process*)
 
-(allow process-info*
+(allow process-fork
 	(target self)
 )
 
-(allow process-info-codesignature)
+(allow process-info-codesignature
+	(target self)
+)
 
-(allow process-iopolicy*)
+(allow process-info-dirtycontrol
+	(target self)
+)
+
+(allow process-info-ledger
+	(target self)
+)
+
+(allow process-info-listpids
+	(target self)
+)
+
+(allow process-info-pidinfo
+	(target self)
+)
+
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
 

 )
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
