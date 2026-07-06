## securityuploadd

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any
 			(subpath "${PROCESS_TEMP_DIR}/com.apple.securityuploadd")
 			(subpath "/private/var/tmp/com.apple.securityuploadd")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(subpath "${PROCESS_TEMP_DIR}/com.apple.securityuploadd")
 			(subpath "/private/var/tmp/com.apple.securityuploadd")

 		(subpath "${FRONT_USER_HOME}/Library/Logs/CrashReporter")
 		(subpath "${PROCESS_TEMP_DIR}/com.apple.securityuploadd")
 		(subpath "/private/var/Keychains")
+		(subpath "/private/var/Keychains/Analytics")
 		(subpath "/private/var/Keychains/SupplementalsAssets")
 		(subpath "/private/var/protected/sfanalytics")
 		(subpath "/private/var/protected/trustd/SupplementalsAssets")
```
