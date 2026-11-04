## accountsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.itunescloudd.tcchelper"))
-		(require-not (require-any
-			(global-name "com.apple.findmy.findmylocate.friendshipservice")
-			(global-name "com.apple.findmy.findmylocate.settings")
-		))
+		(require-not (global-name "com.apple.findmy.findmylocate.friendshipservice"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))

 		(require-not (global-name "com.apple.xpc.amstreatmentstoreservice"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.SafariBookmarksSyncAgent"))
-		(require-not (global-name "com.apple.lsd.open"))
+		(require-not (global-name "com.apple.findmy.findmylocate.settings"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.xpc.amsserverdatacacheservice"))
 		(require-not (global-name "com.apple.calaccessd"))

 		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.private"))
 		(require-not (global-name "com.apple.aggregated"))
+		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))
 		(require-not (system-attribute developer-mode))

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
