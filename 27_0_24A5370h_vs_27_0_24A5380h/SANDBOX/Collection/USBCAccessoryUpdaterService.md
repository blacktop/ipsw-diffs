## USBCAccessoryUpdaterService

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(subpath "${PROCESS_TEMP_DIR}/com.apple.MobileAccessoryUpdater")
 			(subpath "/private/var/tmp/com.apple.MobileAccessoryUpdater")
 		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension "com.apple.assets.read")
 		(require-any
-			(extension-class "com.apple.aned.read-only")
-			(extension-class "com.apple.app-sandbox.read")
-			(extension-class "com.apple.app-sandbox.read-write")
-			(extension-class "com.apple.mediaserverd.read")
-			(extension-class "com.apple.mediaserverd.read-write")
+			(require-all
+				(subpath "${HOME}/Library/Assets")
+				(extension-class "com.apple.aned.read-only")
+			)
+			(require-all
+				(subpath "/private/var/MobileAsset")
+				(extension-class "com.apple.aned.read-only")
+			)
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.app-sandbox.read")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.MobileAccessoryUpdater")
+			(subpath "/private/var/tmp/com.apple.MobileAccessoryUpdater")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.MobileAccessoryUpdater")
+			(subpath "/private/var/tmp/com.apple.MobileAccessoryUpdater")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.MobileAccessoryUpdater")
+			(subpath "/private/var/tmp/com.apple.MobileAccessoryUpdater")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.MobileAccessoryUpdater")
+			(subpath "/private/var/tmp/com.apple.MobileAccessoryUpdater")
 		)
 	)
 )
```
