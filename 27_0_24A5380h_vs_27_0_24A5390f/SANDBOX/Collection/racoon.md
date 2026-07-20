## racoon

> Group: ⬆️ Updated

```diff

 
 (allow coalition-info)
 
+(deny mach-lookup
+	(global-name "com.apple.webkit.camera")
+)
+
 (allow file-ioctl
 	(require-any
 		(literal "/dev/aes_0")

 
 (allow fs-info)
 
-(allow iokit-open-user-client
+(allow iokit*)
+
+(deny iokit-get-properties)
+
+(allow iokit-open*
 	(iokit-registry-entry-class "RootDomainUserClient")
 )
 
-(allow ipc-posix-shm-read-data
+(deny iokit-open-service)
+
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.*")
 		(ipc-posix-name "apple.shm.notification_center")
 	)
 )
 
-(allow isp-command-send)
+(allow ipc-sysv-shm)
 
-(allow mach-lookup
+(allow mach*)
+
+(deny mach-derive-port)
+
+(allow mach-issue-extension
 	(require-all
 		(require-not (xpc-service-name "com.apple.WebKit.*"))
 		(require-any

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(global-name "com.apple.SystemConfiguration.configd")
 		(global-name "com.apple.aggregated")

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
+		(literal "/private/var/run/racoon.sock")
+		(local udp "*:4500")
+		(local udp "*:500")
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
 		(control-name "com.apple.net.ipsec_control")

 	)
 )
 
+(allow network-outbound)
+
+(deny nvram-set)
+
+(allow process*)
+
+(deny process-codesigning)
+
+(deny process-iopolicy-set)
+
 (allow signal
 	(target self)
 )
```
