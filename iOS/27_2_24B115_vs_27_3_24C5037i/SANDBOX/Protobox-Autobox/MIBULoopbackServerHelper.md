## MIBULoopbackServerHelper

> Group: ⬆️ Updated

```diff

 	(ipc-posix-name "apple.shm.notification_center")
 )
 
+(deny ipc-posix-shm-write-data)
+(allow ipc-posix-shm-write-data
+	(ipc-posix-name "apple.cfprefs.user.daemonv1")
+)
+
 (deny job-creation)
 
 (deny mach-issue-extension)

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
