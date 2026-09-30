## idleassetsd

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.TVIdleScreen")
 			(subpath "${HOME}/Library/Caches/com.apple.idleassetsd")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.TVIdleScreen")
 			(subpath "${HOME}/Library/Caches/com.apple.idleassetsd")
```
