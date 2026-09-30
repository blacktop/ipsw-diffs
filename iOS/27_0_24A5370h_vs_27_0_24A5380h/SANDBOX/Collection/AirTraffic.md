## AirTraffic

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "/private/var/tmp")
+		(subpath "${HOME}/Library/Caches/com.apple.atc")
 	)
 )
 (allow file-issue-extension
```
