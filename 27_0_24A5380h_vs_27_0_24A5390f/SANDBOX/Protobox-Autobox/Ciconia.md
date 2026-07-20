## Ciconia

> Group: ⬆️ Updated

```diff

 
 (deny generic-issue-extension)
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
 	)
 )
 
+(deny iokit-open-user-client)
+
 (deny iokit-open-service)
 
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.system.notification_center"))

 	)
 )
 
+(deny process-codesigning
+	(require-all
+		(require-not (literal "/usr/bin/fileproviderctl"))
+		(require-not (literal "/usr/bin/env"))
+		(require-not (literal "/usr/bin/awk"))
+	)
+)
+(deny process-codesigning
+	(require-all
+		(literal "/usr/local/bin/dastool")
+		(require-not (system-attribute internal-build))
+	)
+)
+
 (deny process-exec*
 	(require-all
 		(require-not (literal "/usr/bin/fileproviderctl"))
```
