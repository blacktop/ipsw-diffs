## uia2unboxed

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
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "IOHIDResource")
 		(iokit-registry-entry-class "IOMobileFramebuffer")
 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-sem-open)
-(allow ipc-posix-sem-open
+(deny ipc-posix-sem-create)
+(allow ipc-posix-sem-create
 	(ipc-posix-name "purplebuddy.sentinel")
 )
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.daemonv1")
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")

 	)
 )
 
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
 		(require-not (global-name "com.apple.webinspector"))

 	)
 )
 
+(deny process-codesigning
+	(require-all
+		(require-not (literal "/bin/echo"))
+		(require-not (literal "/usr/bin/killall"))
+		(require-not (literal "/bin/sh"))
+		(require-any
+			(require-all
+				(require-not (require-any
+					(literal "/usr/local/bin/collectWiFiDebugInfo.sh")
+					(literal "/usr/local/bin/eventer")
+					(literal "/usr/local/bin/gestalt_query")
+					(literal "/usr/local/bin/hkctl")
+				))
+				(require-not (literal "/usr/local/bin/CADebug"))
+			)
+			(require-not (system-attribute internal-build))
+		)
+	)
+)
+
 (deny process-exec*
 	(require-all
 		(require-not (literal "/bin/echo"))
```
