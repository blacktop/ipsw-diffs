## networkdiagnosticsd

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
 		(require-not (global-name "com.apple.lsd.mapdb"))

 	)
 )
 
-(deny process-exec*)
-(allow process-exec*
-	(require-any
-		(literal "/System/Library/Frameworks/SystemConfiguration.framework/get-network-info")
-		(literal "/System/Library/PrivateFrameworks/SystemConfiguration.framework/get-network-info")
-		(literal "/bin/launchctl")
-		(literal "/bin/sh")
-		(literal "/usr/bin/awk")
-		(literal "/usr/bin/defaults")
-		(literal "/usr/bin/log")
-		(literal "/usr/sbin/tcpdump")
+(deny process-codesigning
+	(require-all
+		(require-not (literal "/usr/sbin/sysctl"))
+		(require-not (literal "/usr/sbin/tcpdump"))
+		(require-any
+			(require-all
+				(literal "/usr/local/bin/ps")
+				(require-not (system-attribute internal-build))
+			)
+			(require-all
+				(require-not (literal "/System/Library/Frameworks/SystemConfiguration.framework/get-network-info"))
+				(require-not (literal "/bin/launchctl"))
+				(require-not (literal "/usr/bin/log"))
+				(require-not (literal "/usr/bin/awk"))
+				(require-not (literal "/bin/sh"))
+				(require-not (literal "/System/Library/PrivateFrameworks/SystemConfiguration.framework/get-network-info"))
+				(require-not (literal "/usr/bin/defaults"))
+			)
+		)
+	)
+)
+
+(deny process-exec*
+	(require-all
+		(require-not (literal "/usr/sbin/sysctl"))
+		(require-not (literal "/usr/sbin/tcpdump"))
+		(require-any
+			(require-all
+				(literal "/usr/local/bin/ps")
+				(require-not (system-attribute internal-build))
+			)
+			(require-all
+				(require-not (literal "/System/Library/Frameworks/SystemConfiguration.framework/get-network-info"))
+				(require-not (literal "/bin/launchctl"))
+				(require-not (literal "/usr/bin/log"))
+				(require-not (literal "/usr/bin/awk"))
+				(require-not (literal "/bin/sh"))
+				(require-not (literal "/System/Library/PrivateFrameworks/SystemConfiguration.framework/get-network-info"))
+				(require-not (literal "/usr/bin/defaults"))
+			)
+		)
 	)
 )
 
```
