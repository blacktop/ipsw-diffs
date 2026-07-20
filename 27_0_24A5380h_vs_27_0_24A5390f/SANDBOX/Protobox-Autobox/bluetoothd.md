## bluetoothd

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
 		(iokit-registry-entry-class "AppleBTHci")

 	)
 )
 
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-all
 		(iokit-property "errorCode")
 		(require-not (iokit-registry-entry-class "IOUserService"))
 	)
 )
-(deny iokit-set-properties
+(deny iokit-open-service
 	(require-any
 		(require-not (iokit-property "IOPMUBootLPMFWOK"))
 		(require-not (iokit-registry-entry-class "AppleDialogSPMIPMU"))
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
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")

 	)
 )
 
-(deny ipc-posix-shm-write-create)
-(allow ipc-posix-shm-write-create
+(deny ipc-posix-shm-write*)
+(allow ipc-posix-shm-write*
 	(ipc-posix-name "com.apple.bluetooth.magnet.shm")
 )
 
-(deny ipc-posix-shm-write-unlink)
-(allow ipc-posix-shm-write-unlink
-	(ipc-posix-name "com.apple.bluetooth.magnet.shm")
-)
+(allow ipc-sysv-shm)
 
-(deny job-creation)
+(deny isp-command-send)
 
-(deny mach-issue-extension)
+(deny mach-host-special-port-set)
 
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.biome.access.user"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command
```
