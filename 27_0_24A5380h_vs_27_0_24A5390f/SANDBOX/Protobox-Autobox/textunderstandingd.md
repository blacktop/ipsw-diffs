## textunderstandingd

> Group: ⬆️ Updated

```diff

 	(extension-class "com.apple.webkit.mach-bootstrap")
 )
 
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
 		(iokit-registry-entry-class "AppleJPEGDriver")

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
 		(require-not (global-name "com.apple.biome.access.user"))

 		(require-not (global-name "com.apple.TextInput.rdt"))
 		(require-not (global-name "com.apple.coreduetd.knowledge"))
 		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.inputanalyticsd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.mobilemail.services.xpc"))

 		(require-not (global-name "com.apple.corerecents.recentsd"))
 		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.progressd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.routined.registration"))
 		(require-not (global-name "com.apple.containermanagerd.system"))

 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (global-name "com.apple.spotlight.SearchAgent"))
 		(require-not (global-name "com.apple.contactsd"))
+		(require-not (global-name "com.apple.exchangesyncd"))
 		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))

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
