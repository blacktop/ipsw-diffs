## com.apple.WebKit.adattributiond

> Group: ⬆️ Updated

```diff

 
 (allow coalition-info)
 
+(deny mach-lookup
+	(global-name "com.apple.webkit.camera")
+)
+
 (allow file-read*
 	(require-all
 		(subpath "/private/var")

 
 (allow fs-info)
 
-(allow ipc-posix-shm-read-data
+(allow iokit*)
+
+(deny iokit-get-properties)
+
+(deny iokit-open-service)
+
+(allow ipc-posix-shm*
 	(require-all
 		(require-not (ipc-posix-name "/com.apple.AppSSO.version"))
 		(require-any

 	)
 )
 
-(allow ipc-posix-shm-write-data
+(allow ipc-posix-shm-write-create
 	(ipc-posix-name "com.apple.AppleDatabaseChanged")
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
 		(require-not (global-name "com.apple.SystemConfiguration.SCNetworkReachability"))
 		(require-not (global-name "com.apple.nsurlstorage-cache"))

 		)
 	)
 )
-(allow mach-lookup
+(allow mach-issue-extension
 	(require-any
 		(global-name "com.apple.AppSSO.service-xpc")
 		(global-name "com.apple.cfnetwork.cfnetworkagent")

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
-)
+(deny necp-client-open)
 
-(allow network-outbound
+(allow network-bind
 	(require-any
 		(control-name "com.apple.flow-divert")
 		(control-name "com.apple.netsrc")
 		(literal "/private/var/run/mDNSResponder")
 		(remote tcp "*:*")
+		(remote udp "*:*")
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
