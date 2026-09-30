## medialibraryd

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.medialibraryd")
 			(subpath "${HOME}/Library/Caches/com.apple.mediaplayer")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.mediaserverd.read")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.medialibraryd")
 			(subpath "${HOME}/Library/Caches/com.apple.mediaplayer")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.medialibraryd")
 			(subpath "${HOME}/Library/Caches/com.apple.mediaplayer")
```
