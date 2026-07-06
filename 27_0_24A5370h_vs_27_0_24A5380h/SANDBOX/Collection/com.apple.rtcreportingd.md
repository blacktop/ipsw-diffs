## com.apple.rtcreportingd

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(subpath "${HOME}/Library/Caches/com.apple.rtcreporting")
-		(extension-class "com.apple.app-sandbox.read-write")
+		(extension-class "com.apple.mediaserverd.read-write")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(subpath "${HOME}/Library/HTTPStorages/com.apple.rtcreportingd")
-		(extension-class "com.apple.app-sandbox.read-write")
+		(extension-class "com.apple.mediaserverd.read-write")
 	)
 )
 (allow file-issue-extension

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Library/Cookies")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(subpath "${HOME}/Library/Caches/com.apple.rtcreporting")
-			)
-			(subpath "${HOME}/Library/Cookies")
-		)
+		(subpath "${HOME}/Library/Cookies")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(subpath "${HOME}/Library/Cookies")
 	)
 )
 (allow file-issue-extension
```
