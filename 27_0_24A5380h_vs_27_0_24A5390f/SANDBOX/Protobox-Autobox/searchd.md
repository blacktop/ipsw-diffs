## searchd

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
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleKeyStore")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.*")
 		(ipc-posix-name "apple.cfprefs.daemonv1")

 	)
 )
 
-(deny ipc-posix-shm-write-create)
-(allow ipc-posix-shm-write-create
+(deny ipc-posix-shm-write*)
+(allow ipc-posix-shm-write*
 	(ipc-posix-name "/powerHUDEntries")
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
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.linkd.registry"))

 	)
 )
 
+(deny process-codesigning)
+(allow process-codesigning
+	(require-any
+		(literal "/bin/sh")
+		(literal "/usr/bin/gcore")
+	)
+)
+
 (deny process-exec*)
 (allow process-exec*
 	(require-any
```
