## remotemanagementd

> Group: ⬆️ Updated

```diff

 
 (deny ipc*)
 
+(deny ipc-posix-shm-read-data)
+(allow ipc-posix-shm-read-data
+	(ipc-posix-name "apple.shm.notification_center")
+)
+
 (deny job-creation)
 
 (deny mach-issue-extension)
```
