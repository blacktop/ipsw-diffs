## Family

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
 
-(deny ipc-posix-sem-open)
-(allow ipc-posix-sem-open
+(deny ipc-posix-sem-create)
+(allow ipc-posix-sem-create
 	(ipc-posix-name "hangtelemetryd.onceatboot")
 )
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "/FBW1:com.apple.uikit.viewservi")
 		(ipc-posix-name "apple.cfprefs.*")

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
 		(require-not (global-name "com.apple.mobile.keybagd.xpc"))

 		(require-not (global-name "com.apple.ak.anisette.xpc"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc"))
 		(require-not (global-name "com.apple.networkscored"))
+		(require-not (require-any
+			(global-name "com.apple.ScreenTimeAgent.settings")
+			(global-name "com.apple.ScreenTimeSettingsAgent.public")
+			(global-name "com.apple.ak.puffin.xpc")
+			(global-name "com.apple.coremedia.sts")
+			(global-name "com.apple.uikit.viewservice.com.apple.family")
+		))
 		(require-not (require-any
 			(global-name "com.apple.appprotectiond.extensioninfo")
 			(global-name "com.apple.appprotectiond.extensionmonitor")

 		))
 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
 		(require-not (global-name "com.apple.iohideventsystem"))
-		(require-not (require-any
-			(global-name "com.apple.ScreenTimeAgent.settings")
-			(global-name "com.apple.ScreenTimeSettingsAgent.public")
-			(global-name "com.apple.ak.puffin.xpc")
-			(global-name "com.apple.coremedia.sts")
-			(global-name "com.apple.uikit.viewservice.com.apple.family")
-		))
 		(require-not (global-name "com.apple.itunescloudd.xpc"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.dnssd.service"))

 		(require-not (global-name "com.apple.calaccessd"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (local-name "com.apple.iphone.axserver"))
+		(require-not (local-name "com.apple.accessibility.gax.client"))
 		(require-not (xpc-service-name "*"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))
 		(require-not (global-name "com.apple.AccessibilityUIServer"))

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
