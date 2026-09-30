## siriinferenced

> Group: ⬆️ Updated

```diff

 )
 
 (deny iokit-open-service)
+(allow iokit-open-service
+	(iokit-registry-entry-class "AppleKeyStore")
+)
 
 (deny iokit-set-properties)
 
 (deny ipc*)
 
+(deny ipc-posix-shm-read-data)
+(allow ipc-posix-shm-read-data
+	(require-any
+		(ipc-posix-name "apple.cfprefs.system.daemonv1")
+		(ipc-posix-name "apple.cfprefs.user.daemonv1")
+	)
+)
+
 (deny job-creation)
 
 (deny mach-issue-extension)

 		(require-not (global-name "com.apple.icloud.fmfd"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.lsd.icons"))
+		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
 		(require-not (global-name "com.apple.itunescloud.music-subscription-status-service"))
 		(require-not (global-name "com.apple.linkd.extension"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))

 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.coreduetd.knowledge"))
 		(require-not (global-name "com.apple.ak.auth.xpc"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.biomesyncd.sync"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.lsd.xpc"))
```
