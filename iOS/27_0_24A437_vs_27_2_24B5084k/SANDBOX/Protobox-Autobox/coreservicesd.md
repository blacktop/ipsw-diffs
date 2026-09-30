## coreservicesd

> Group: ⬆️ Updated

```diff

 
 (deny ipc-posix-shm-read-data)
 (allow ipc-posix-shm-read-data
-	(ipc-posix-name "apple.shm.notification_center")
+	(require-any
+		(ipc-posix-name "apple.shm.notification_center")
+		(ipc-posix-name "com.apple.featureflags.shm")
+	)
 )
 
 (deny job-creation)
```
