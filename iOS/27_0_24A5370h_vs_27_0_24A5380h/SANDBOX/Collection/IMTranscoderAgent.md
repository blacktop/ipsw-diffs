## IMTranscoderAgent

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(subpath "/private/var/tmp/com.apple.messages")
+		(subpath "${HOME}/Library/Caches/com.apple.imtranscoding.IMTranscoderAgent")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "/private/var/tmp/com.apple.messages")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "/private/var/tmp/com.apple.messages")
+		(subpath "${HOME}/Library/Caches/com.apple.imtranscoding.IMTranscoderAgent")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "/private/var/tmp/com.apple.messages")
+		(subpath "${HOME}/Library/Caches/com.apple.imtranscoding.IMTranscoderAgent")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${HOME}/Library/Caches/com.apple.imtranscoding.IMTranscoderAgent")
 	)
 )
 (allow file-issue-extension

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(require-all
-				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.aned.read-only")
+				(extension "com.apple.assets.read")
 				(require-any
-					(extension "com.apple.security.exception.files.absolute-path.read-only")
-					(extension "com.apple.security.exception.files.absolute-path.read-write")
-					(extension "com.apple.security.exception.files.home-relative-path.read-only")
-					(extension "com.apple.security.exception.files.home-relative-path.read-write")
-					(subpath "${HOME}/Library/SMS/Attachments")
-					(subpath "${HOME}/Media")
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
 				)
 			)
+			(require-any
+				(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
+				(subpath "/private/var/tmp/com.apple.messages")
+			)
 			(subpath "${HOME}/Library/Caches/com.apple.MobileSMS")
 			(subpath "${HOME}/Library/Caches/com.apple.imtranscoding.IMTranscoderAgent")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
-			(subpath "/private/var/tmp/com.apple.messages")
 		)
 	)
 )

 					(literal "${FRONT_USER_HOME}/Library/DeviceRegistry")
 					(require-all
 						(subpath "/private/var")
-						(subpath "${FRONT_USER_HOME}")
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+$")
+						(subpath "${FRONT_USER_HOME}")
 					)
 				)
 			)
```
