## ArchiveService

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.desktopservices.ArchiveService")
 			(subpath "${PROCESS_TEMP_DIR}/com.apple.fileprovider.ArchiveService")
 			(subpath "/private/var/tmp/com.apple.desktopservices.ArchiveService")
 			(subpath "/private/var/tmp/com.apple.fileprovider.ArchiveService")
 		)
-		(extension-class "com.apple.app-sandbox.read-write")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.desktopservices.ArchiveService")
 		(require-any
 			(extension-class "com.apple.aned.read-only")
 			(extension-class "com.apple.app-sandbox.read")

 		(require-not (%entitlement-is-present "com.apple.private.oop-jit.loader"))
 	)
 )
+(allow file-read*
+	(require-any
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.desktopservices.ArchiveService")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.fileprovider.ArchiveService")
+		(subpath "/private/var/tmp/com.apple.desktopservices.ArchiveService")
+		(subpath "/private/var/tmp/com.apple.fileprovider.ArchiveService")
+	)
+)
 (allow file-read*
 	(require-all
 		(subpath "/AppleInternal")

 		(system-attribute carrier-build)
 	)
 )
-(allow file-read*
-	(require-any
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.desktopservices.ArchiveService")
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.fileprovider.ArchiveService")
-		(subpath "/private/var/tmp/com.apple.desktopservices.ArchiveService")
-		(subpath "/private/var/tmp/com.apple.fileprovider.ArchiveService")
-	)
-)
 (deny file-read*
 	(require-any
 		(literal "/System/Library/Caches/apticket.der")
```
