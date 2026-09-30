## devicecheckd

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.DeviceCheckInternal")
 			(subpath "${HOME}/Library/HTTPStorages/com.apple.DeviceCheckInternal")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.DeviceCheckInternal")
 			(subpath "${HOME}/Library/HTTPStorages/com.apple.DeviceCheckInternal")

 )
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.DeviceCheckInternal")
 	)
 )
```
