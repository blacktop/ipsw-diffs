## geod

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.Maps.Suggestions")
-			(subpath "${HOME}/Library/Caches/com.apple.geod")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.geod")
-		)
+		(subpath "${HOME}/Library/Cookies")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.Maps.Suggestions")
-			(subpath "${HOME}/Library/Caches/com.apple.geod")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.geod")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.Maps.Suggestions")
-			(subpath "${HOME}/Library/Caches/com.apple.geod")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.geod")
-		)
+		(subpath "${HOME}/Library/Cookies")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.Maps.Suggestions")
-			(subpath "${HOME}/Library/Caches/com.apple.geod")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.geod")
-		)
+		(subpath "${HOME}/Library/Cookies")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${HOME}/Library/Cookies")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.Maps.Suggestions")
```
