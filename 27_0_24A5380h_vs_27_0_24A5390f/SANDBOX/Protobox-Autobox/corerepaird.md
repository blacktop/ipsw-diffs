## corerepaird

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
 		(iokit-registry-entry-class "AppleBiometricServices")
 		(iokit-registry-entry-class "AppleH10CamIn")

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
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.lsd.icons"))
+		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.system.notification_center"))

 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.CheckerBoard.services"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (xpc-service-name "com.apple.ACCHWComponentAuthService"))
 		(require-not (xpc-service-name "com.apple.ZhuGeService"))
 		(require-not (xpc-service-name "com.apple.CoreRepairCoreNetworkXPCService"))
 		(require-not (xpc-service-name "com.apple.AppleDeviceQueryService"))
-		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
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
