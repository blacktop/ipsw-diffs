## mediaremoted

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.mediaremoted")
-			(subpath "/private/var/tmp/com.apple.mediaremoted")
-		)
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.mediaremoted")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.mediaremoted")
-			(subpath "/private/var/tmp/com.apple.mediaremoted")
-		)
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.mediaremoted")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.mediaremoted")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.mediaremoted")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.nsurlsessiond.readonly")
+		(extension "com.apple.sandbox.executable")
 	)
 )
 (allow file-issue-extension

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.mediaremoted")
-			(subpath "/private/var/tmp/com.apple.mediaremoted")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.mediaremoted")
-			(subpath "/private/var/tmp/com.apple.mediaremoted")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.nsurlsessiond.readonly")
-		(extension "com.apple.sandbox.executable")
-	)
-)
 (deny file-issue-extension
 	(require-all
 		(require-not (extension "com.apple.app-sandbox.read"))
```
