## ptpd

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.ptpd")
-			(subpath "/private/var/tmp/com.apple.ptpd")
-		)
+		(subpath "${HOME}/Media/Photos")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.ptpd")
-			(subpath "/private/var/tmp/com.apple.ptpd")
-		)
+		(subpath "${HOME}/Media/Photos")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(subpath "${HOME}/Media/Photos")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${HOME}/Media/Photos")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.ptpd")
-			(subpath "/private/var/tmp/com.apple.ptpd")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.ptpd")
-			(subpath "/private/var/tmp/com.apple.ptpd")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
+			(require-all
+				(extension-class "com.apple.aned.read-only")
+				(extension "com.apple.assets.read")
+				(require-any
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
+				)
+			)
 			(require-any
 				(subpath "${PROCESS_TEMP_DIR}/com.apple.ptpd")
 				(subpath "/private/var/tmp/com.apple.ptpd")

 
 (allow file-write*
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.metal")
 	)
 )
 (allow file-write*
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.metal")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.ptpd")

 		(subpath "${HOME}/Library/Caches/com.apple.ptpd")
 		(subpath "${HOME}/Library/Logs/CrashReporter/DiagnosticLogs/Photos")
 		(subpath "${HOME}/Media")
-		(subpath "${HOME}/Media/DCIM")
-		(subpath "${HOME}/Media/PhotoData")
 		(subpath "${HOME}/Media/Photos")
 		(subpath "${PROCESS_TEMP_DIR}")
 		(subpath "/private/var/tmp")

 
 (allow file-write-create
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.metal")
 	)
 )

 )
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.metal")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.ptpd")

 		(subpath "${HOME}/Library/Caches/com.apple.ptpd")
 		(subpath "${HOME}/Library/Logs/CrashReporter/DiagnosticLogs/Photos")
 		(subpath "${HOME}/Media")
-		(subpath "${HOME}/Media/DCIM")
-		(subpath "${HOME}/Media/PhotoData")
 		(subpath "${HOME}/Media/Photos")
 		(subpath "${PROCESS_TEMP_DIR}")
 		(subpath "/private/var/tmp")

 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.metal")
 	)
 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.metal")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.ptpd")

 		(subpath "${HOME}/Library/Caches/com.apple.ptpd")
 		(subpath "${HOME}/Library/Logs/CrashReporter/DiagnosticLogs/Photos")
 		(subpath "${HOME}/Media")
-		(subpath "${HOME}/Media/DCIM")
-		(subpath "${HOME}/Media/PhotoData")
 		(subpath "${HOME}/Media/Photos")
 		(subpath "${PROCESS_TEMP_DIR}")
 		(subpath "/private/var/tmp")
```
