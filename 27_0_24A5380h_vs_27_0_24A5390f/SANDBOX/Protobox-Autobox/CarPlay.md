## CarPlay

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
 		(iokit-registry-entry-class "AppleANS2CGNVMeController")

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
 	(require-any
 		(ipc-posix-name "hangtelemetryd.onceatboot")
 		(ipc-posix-name "purplebuddy.sentinel")
 	)
 )
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "/FBW1:com.apple.CarPlayApp.non-")
 		(ipc-posix-name "/FBW2:com.apple.CarPlayApp.non-")

 	)
 )
 
-(deny ipc-posix-shm-write-create)
-(allow ipc-posix-shm-write-create
+(deny ipc-posix-shm-write*)
+(allow ipc-posix-shm-write*
 	(require-any
 		(ipc-posix-name "/FBW1:com.apple.CarPlayApp.non-")
 		(ipc-posix-name "/FBW2:com.apple.CarPlayApp.non-")
 	)
 )
 
-(deny ipc-posix-shm-write-unlink)
-(allow ipc-posix-shm-write-unlink
-	(require-any
-		(ipc-posix-name "/FBW1:com.apple.CarPlayApp.non-")
-		(ipc-posix-name "/FBW2:com.apple.CarPlayApp.non-")
-	)
-)
+(allow ipc-sysv-shm)
 
-(deny job-creation)
+(deny isp-command-send)
 
-(deny mach-issue-extension)
+(deny mach-host-special-port-set)
 
-(deny mach-lookup
+(deny mach-issue-extension
 	(require-all
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.linkd.registry"))

 		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.calaccessd"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
+		(require-not (local-name "com.apple.accessibility.gax.client"))
 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
 		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))

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
