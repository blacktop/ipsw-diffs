## BTServer

> Group: ⬆️ Updated

```diff

 
 (allow fs-snapshot-mount)
 
-(allow iokit-get-properties)
+(allow iokit*)
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-all
 		(system-attribute virtual-device)
 		(require-any

 		)
 	)
 )
-(allow iokit-open-user-client
+(allow iokit-open*
 	(require-any
 		(extension "com.apple.security.exception.iokit-user-client-class")
 		(iokit-connection "IOGPU")

 	)
 )
 
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(require-any
 		(%entitlement-is-present "com.apple.security.exception.iokit-user-client-class")
 		(iokit-registry-entry-class "AGXAcceleratorG*")

 	)
 )
 
-(allow iokit-set-properties
+(allow iokit-open-service
 	(require-all
 		(iokit-property "IOPMUBootLPMFWOK")
 		(iokit-registry-entry-class "AppleDialogSPMIPMU")
 	)
 )
 
-(allow ipc-posix-shm*
+(allow ipc-posix-sem-wait
 	(require-any
 		(ipc-posix-name "..:..:..:..:..:..-tacl")
 		(ipc-posix-name "com.apple.bluetooth.magnet.shm")

 	)
 )
 
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-all
 		(ipc-posix-name "apple.shm.notification_center")
 		(%entitlement-is-bool-true "com.apple.security.on-demand-install-capable")
 	)
 )
-(allow ipc-posix-shm-read-data
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "..:..:..:..:..:..-tacl")
 		(ipc-posix-name "/com.apple.AppSSO.version")

 	)
 )
 
-(deny job-creation)
+(allow ipc-posix-shm-read-data
+	(require-any
+		(ipc-posix-name "..:..:..:..:..:..-tacl")
+		(ipc-posix-name "com.apple.bluetooth.magnet.shm")
+		(ipc-posix-name "shm_notif.tacl.R")
+		(ipc-posix-name "shm_notif.tacl.W")
+		(ipc-posix-name "shm_notif.tsco.R")
+		(ipc-posix-name "shm_notif.tsco.W")
+		(ipc-posix-name "shm_pcm_audio_sco_read")
+		(ipc-posix-name "shm_pcm_audio_sco_write")
+	)
+)
 
-(deny lsopen
+(allow ipc-posix-shm-write*
+	(require-any
+		(ipc-posix-name "..:..:..:..:..:..-tacl")
+		(ipc-posix-name "com.apple.bluetooth.magnet.shm")
+		(ipc-posix-name "shm_notif.tacl.R")
+		(ipc-posix-name "shm_notif.tacl.W")
+		(ipc-posix-name "shm_notif.tsco.R")
+		(ipc-posix-name "shm_notif.tsco.W")
+		(ipc-posix-name "shm_pcm_audio_sco_read")
+		(ipc-posix-name "shm_pcm_audio_sco_write")
+	)
+)
+
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
 		(global-name "com.apple.ak.auth.xpc")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.networkd_privileged")
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-all
 		(global-name "com.apple.ak.anisette.xpc")
 		(process-attribute is-apple-signed-executable)
 	)
 )
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

 		(xpc-service-name "com.apple.externalaccessory.WACEAService")
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
-	(target self)
-)
-
-(allow mach-task-special-port*)
-
-(allow necp-client-open)
-
-(allow network-inbound)
-
-(allow network-bind)
-
-(allow network-outbound)
+(allow network*)
 
 (allow nvram*)
 
-(allow process-codesigning)
-
-(allow process-info*)
-
-(allow process-iopolicy*)
-
-(allow pseudo-tty)
+(allow process*)
 
 (allow sandbox-check)
 

 )
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
