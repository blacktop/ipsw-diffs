## SharingHUDService

> Group: ⬆️ Updated

```diff

 
 (allow file-graft)
 
-(allow file-issue-extension
-	(require-all
-		(subpath "${HOME}/Library/Caches/com.apple.Sharing.SharingHUDService")
-		(extension-class "com.apple.app-sandbox.read-write")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(require-any
 			(subpath "${PROCESS_TEMP_DIR}/com.apple.Sharing.SharingHUDService")
 			(subpath "/private/var/tmp/com.apple.Sharing.SharingHUDService")
 		)
+		(extension-class "com.apple.mediaserverd.read-write")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(subpath "${HOME}/Library/Caches/com.apple.Sharing.SharingHUDService")
 		(require-any
 			(extension-class "com.apple.aned.read-only")
 			(extension-class "com.apple.app-sandbox.read")

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.Sharing.SharingHUDService")
 	)
 )

 
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.Sharing.SharingHUDService")
 	)
 )
```
