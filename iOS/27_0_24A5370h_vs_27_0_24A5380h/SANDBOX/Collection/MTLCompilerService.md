## MTLCompilerService

> Group: ⬆️ Updated

```diff

 
 (allow file-issue-extension
 	(require-all
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.MTLCompilerService")
-			(subpath "/private/var/tmp/com.apple.MTLCompilerService")
-		)
+		(subpath "/private/var/tmp/com.apple.MTLCompilerService")
+		(extension-class "com.apple.mediaserverd.read-write")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.MTLCompilerService")
 		(require-any
 			(extension-class "com.apple.aned.read-only")
 			(extension-class "com.apple.app-sandbox.read")
```
