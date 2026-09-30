## gputoolsd

> Group: ⬆️ Updated

```diff

 
 (allow fs-snapshot-mount)
 
-(allow iokit-get-properties)
+(allow iokit*)
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-any
 		(extension "com.apple.security.exception.iokit-user-client-class")
 		(iokit-connection "IOGPU")

 	)
 )
 
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(%entitlement-is-present "com.apple.security.exception.iokit-user-client-class")
 )
 
-(allow ipc-posix-shm*
+(allow ipc-posix-sem-wait
 	(ipc-posix-name "gdt-*")
 )
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(ipc-posix-name "apple.shm.notification_center")
 		(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
 	)
 )
+(allow ipc-posix-shm*
+	(ipc-posix-name "gdt-*")
+)
+
 (allow ipc-posix-shm-read-data
 	(ipc-posix-name "gdt-*")
 )
 
-(deny job-creation)
+(allow ipc-posix-shm-write*
+	(ipc-posix-name "gdt-*")
+)
 
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

 		(xpc-service-name "com.apple.MTLCompilerService")
 	)
 )
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-any
 		(xpc-service-name "com.apple.CoreGraphics.CGPDFService")
 		(xpc-service-name "com.apple.WebKit.*")
 	)
 )
 
-(allow mach-priv-task-port)
-
-(allow mach-register
+(allow mach-priv-task-port
 	(extension "com.apple.security.exception.mach-register.global-name")
 )
 
-(allow mach-task-exception-port-set)
-
-(allow mach-task-inspect)
-
-(allow mach-task-name)
-
-(allow mach-task-read)
-
-(allow mach-task-special-port*)
-
-(allow necp-client-open)
-
-(allow network-outbound
+(allow network-bind
 	(require-any
 		(control-name "com.apple.flow-divert")
 		(literal "/private/var/run/gputoolsdhelper.sock")

 	)
 )
 
+(allow network-outbound)
+
 (allow nvram*)
 
-(allow process-codesigning)
+(allow process*)
+
+(allow process-codesigning
+	(require-any
+		(literal "/Developer/usr/libexec/gputoolsd")
+		(literal "/System/Developer/usr/libexec/gputoolsd")
+	)
+)
 
 (allow process-exec*
 	(require-any

 	)
 )
 
-(allow process-info*)
-
-(allow process-iopolicy*)
-
 (allow sandbox-check)
 
 (allow signal)

 )
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
