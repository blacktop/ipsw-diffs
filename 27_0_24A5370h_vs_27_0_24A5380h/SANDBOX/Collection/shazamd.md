## shazamd

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.shazam.secure")
-			(subpath "${HOME}/Library/Caches/com.apple.shazamd")
-			(subpath "${HOME}/Library/Caches/com.apple.shazamlibrary.cloud")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.shazamd")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.shazamd")
-			(subpath "/private/var/tmp/com.apple.shazamd")
-		)
+		(subpath "${HOME}/Library/Cookies")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.shazam.secure")
-			(subpath "${HOME}/Library/Caches/com.apple.shazamd")
-			(subpath "${HOME}/Library/Caches/com.apple.shazamlibrary.cloud")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.shazamd")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.shazamd")
-			(subpath "/private/var/tmp/com.apple.shazamd")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.shazam.secure")
-			(subpath "${HOME}/Library/Caches/com.apple.shazamd")
-			(subpath "${HOME}/Library/Caches/com.apple.shazamlibrary.cloud")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.shazamd")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.shazamd")
-			(subpath "/private/var/tmp/com.apple.shazamd")
-		)
+		(subpath "${HOME}/Library/Cookies")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.shazam.secure")
-			(subpath "${HOME}/Library/Caches/com.apple.shazamd")
-			(subpath "${HOME}/Library/Caches/com.apple.shazamlibrary.cloud")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.shazamd")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.shazamd")
-			(subpath "/private/var/tmp/com.apple.shazamd")
-		)
+		(subpath "${HOME}/Library/Cookies")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${HOME}/Library/Cookies")
 	)
 )
 (allow file-issue-extension

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(extension "com.apple.security.exception.files.absolute-path.read-only")
-					(extension "com.apple.security.exception.files.absolute-path.read-write")
-					(extension "com.apple.security.exception.files.home-relative-path.read-only")
-					(extension "com.apple.security.exception.files.home-relative-path.read-write")
-				)
-			)
 			(require-any
 				(subpath "${HOME}/Library/Caches/com.apple.shazam.secure")
 				(subpath "${HOME}/Library/Caches/com.apple.shazamd")
```
