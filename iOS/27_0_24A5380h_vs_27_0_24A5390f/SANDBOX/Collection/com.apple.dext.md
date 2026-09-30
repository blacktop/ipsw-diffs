## com.apple.dext

> Group: ⬆️ Updated

```diff

 
 (deny iokit-get-properties)
 
-(allow iokit-open-user-client
+(allow iokit-open*
 	(iokit-registry-entry-class "IOUserServer")
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(allow iokit-open-user-client
 	(iokit-registry-entry-class "IOPlatformExpertDevice")
 )
-(deny iokit-open-service
+(deny iokit-open-user-client
 	(require-all
 		(iokit-registry-entry-class "IOPlatformExpertDevice")
 		(state-flag "driverkit-post-launch")
 	)
 )
 
-(allow isp-command-send)
+(deny iokit-open-service)
+
+(allow ipc-sysv-shm)
 
 (deny mach-bootstrap)
 
-(deny mach-cross-domain-lookup)
+(deny mach-derive-port)
+
+(allow mach-task*)
+
+(deny mach-task-exception-port-set)
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
+(deny necp-client-open)
 
 (deny nvram*)
 
+(allow process*)
+
+(deny process-codesigning)
+
+(allow process-fork
+	(target self)
+)
+
 (deny process-info*)
 (allow process-info*
 	(target self)
 )
 
+(deny process-iopolicy-set)
+
 (allow signal
 	(target self)
 )
```
