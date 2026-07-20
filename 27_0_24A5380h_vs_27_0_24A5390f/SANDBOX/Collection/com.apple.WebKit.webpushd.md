## com.apple.WebKit.webpushd

> Group: ⬆️ Updated

```diff

 
 (allow coalition-info)
 
+(deny mach-lookup
+	(global-name "com.apple.webkit.camera")
+)
+
 (allow file*
 	(require-any
 		(subpath "${HOME}/Library/WebKit/WebPush")

 
 (allow fs-info)
 
-(allow iokit-open-user-client
+(allow iokit*)
+
+(deny iokit-get-properties)
+
+(allow iokit-open*
 	(iokit-registry-entry-class "AppleKeyStoreUserClient")
 )
 
-(allow ipc-posix-shm-read-data
+(deny iokit-open-service)
+
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.shm.notification_center")
 		(ipc-posix-name "com.apple.AppleDatabaseChanged")
 	)
 )
 
-(allow ipc-posix-shm-write-data
+(allow ipc-posix-shm-write-create
 	(ipc-posix-name "com.apple.AppleDatabaseChanged")
 )
 
-(allow isp-command-send)
+(allow ipc-sysv-shm)
 
-(allow lsopen)
+(allow job-creation)
 
-(allow mach-lookup
+(allow mach*)
+
+(deny mach-derive-port)
+
+(allow mach-issue-extension
 	(require-any
 		(global-name "com.apple.SecurityServer")
 		(global-name "com.apple.analyticsd")

 	)
 )
 
+(deny mach-task-exception-port-set)
+(allow mach-task-exception-port-set
+	(target self)
+)
+
 (allow mach-task-inspect
 	(target self)
 )

 	(target self)
 )
 
-(allow mach-task-read
-	(target self)
-)
+(deny necp-client-open)
+
+(allow network-outbound)
+
+(deny nvram-set)
+
+(allow process*)
+
+(deny process-codesigning)
+
+(deny process-iopolicy-set)
 
 (allow signal
 	(target self)
```
