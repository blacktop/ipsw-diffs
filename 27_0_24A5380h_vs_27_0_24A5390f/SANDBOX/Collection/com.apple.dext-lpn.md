## com.apple.dext-lpn

> Group: ⬆️ Updated

```diff

 
 (allow fs-info)
 
-(allow isp-command-send)
+(allow ipc-sysv-shm)
 
-(deny job-creation)
+(deny isp-command-send)
 
-(allow mach-derive-port)
+(allow mach-cross-domain-lookup)
 
-(allow mach-task-exception-port-set)
+(allow mach-task*)
+
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
+(allow network*)
 
-(allow mach-task-special-port*)
-
-(allow necp-client-open)
-
-(allow network-inbound)
-
-(allow network-bind)
-
-(allow network-outbound)
-
-(allow process-codesigning)
-
-(allow process-info-sandbox-container)
-
-(allow process-iopolicy*)
+(allow process*)
 
 (allow sandbox-check)
 

 (allow system-privilege)
 
 (allow exception-entitlement)
-
-(allow process-exec-update-label)
```
