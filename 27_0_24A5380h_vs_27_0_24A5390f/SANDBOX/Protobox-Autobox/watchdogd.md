## watchdogd

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
 		(iokit-registry-entry-class "AppleAPFSContainer")
 		(iokit-registry-entry-class "AppleARMWatchdogTimer")

 	)
 )
 
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-not (require-any
 		(iokit-property "IOPMUBootAppName")
 		(iokit-property "IOPMUBootStage")
 	))
 )
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-all
 		(require-not (iokit-registry-entry-class "AppleDialogSPMIPMU"))
 		(require-not (iokit-registry-entry-class "AppleDialogPMU"))
 	)
 )
 
+(deny iokit-set-properties)
+
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
 
-(deny mach-issue-extension)
+(allow ipc-sysv-shm)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.biome.access.user"))

 	)
 )
 
+(deny process-codesigning)
+(allow process-codesigning
+	(require-any
+		(literal "/usr/bin/tailspin")
+		(literal "/usr/sbin/kextstat")
+	)
+)
+
 (deny process-exec*)
 (allow process-exec*
 	(require-any
```
