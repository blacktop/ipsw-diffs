## SafariSafeBrowsing

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any
 			(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.Safari.SafeBrowsing")
 			(subpath "${HOME}/Library/HTTPStorages/com.apple.Safari.SafeBrowsing")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.Safari.SafeBrowsing")
 			(subpath "${HOME}/Library/HTTPStorages/com.apple.Safari.SafeBrowsing")

 
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type REGULAR-FILE)
 		(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.Safari.SafeBrowsing")
 	)
 )
```
