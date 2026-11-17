## WiFiCloudAssetsXPCService

> Group: ⬆️ Updated

```diff

 	)
 )
 
+(deny ipc-posix-shm-write-data)
+(allow ipc-posix-shm-write-data
+	(ipc-posix-name "apple.cfprefs.daemonv1")
+)
+
 (deny job-creation)
 
 (deny mach-issue-extension)
```
