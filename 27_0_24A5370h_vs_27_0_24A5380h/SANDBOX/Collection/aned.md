## aned

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(subpath "${HOME}/Library/Caches/com.apple.aned")
-		(extension-class "com.apple.app-sandbox.read-write")
+		(extension-class "com.apple.mediaserverd.read-write")
 	)
 )
 (allow file-issue-extension

 
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.aned")
 	)
 )
```
