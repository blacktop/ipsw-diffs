## PasteBoard

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(subpath "/private/var/tmp/com.apple.pasteboard.pasted")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.pasteboard.pasted")
+			(subpath "/private/var/tmp/com.apple.pasteboard.pasted")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "/private/var/tmp/com.apple.pasteboard.pasted")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "/private/var/tmp/com.apple.pasteboard.pasted")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.pasteboard.pasted")
+			(subpath "/private/var/tmp/com.apple.pasteboard.pasted")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "/private/var/tmp/com.apple.pasteboard.pasted")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.pasteboard.pasted")
+			(subpath "/private/var/tmp/com.apple.pasteboard.pasted")
+		)
 	)
 )
 (allow file-issue-extension

 		(subpath "${FRONT_USER_HOME}/Library/Caches/com.apple.Pasteboard")
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.pasteboard.pasted")
+			(subpath "/private/var/tmp/com.apple.pasteboard.pasted")
+		)
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
```
