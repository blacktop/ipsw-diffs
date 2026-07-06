## mediaparserd

> Group: ⬆️ Updated

```diff

 
 (allow file-issue-extension
 	(require-all
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.mediaparserd")
-			(subpath "/private/var/tmp/com.apple.mediaparserd")
-		)
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.mediaparserd")
+		(extension-class "com.apple.mediaserverd.read-write")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(subpath "/private/var/tmp/com.apple.mediaparserd")
 		(require-any
 			(extension-class "com.apple.aned.read-only")
 			(extension-class "com.apple.app-sandbox.read")
```
