## deferredmediad

> Group: ⬆️ Updated

```diff

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.deferredmediad")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.deferredmediad")
-			(subpath "/private/var/tmp/com.apple.deferredmediad")
-		)
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")

 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
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
-			(require-any
-				(subpath "${HOME}/Library/Caches/com.apple.deferredmediad")
-				(subpath "${PROCESS_TEMP_DIR}/com.apple.deferredmediad")
-				(subpath "/private/var/tmp/com.apple.deferredmediad")
-			)
+			(subpath "${HOME}/Library/Caches/com.apple.deferredmediad")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.deferredmediad")
+			(subpath "/private/var/tmp/com.apple.deferredmediad")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.deferredmediad")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.deferredmediad")
+			(subpath "/private/var/tmp/com.apple.deferredmediad")
 		)
 	)
 )

 
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.deferredmediad")
 	)
 )
```
