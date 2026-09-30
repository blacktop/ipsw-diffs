## akd

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.akd")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.akd")
-			(subpath "/private/var/tmp/com.apple.akd")
-		)
+		(subpath "${HOME}/Library/HTTPStorages/com.apple.akd")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.akd")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.akd")
-			(subpath "/private/var/tmp/com.apple.akd")
-		)
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.akd")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.akd")
-			(subpath "/private/var/tmp/com.apple.akd")
-		)
+		(subpath "${HOME}/Library/HTTPStorages/com.apple.akd")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.akd")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.akd")
-			(subpath "/private/var/tmp/com.apple.akd")
-		)
+		(subpath "${HOME}/Library/HTTPStorages/com.apple.akd")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${HOME}/Library/HTTPStorages/com.apple.akd")
 	)
 )
 (allow file-issue-extension

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(extension "com.apple.sandbox.container")
 			(require-any

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
-		(extension "com.apple.sandbox.container")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.quicklook.readonly")
 		(extension "com.apple.sandbox.container")
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(extension "com.apple.sandbox.container")
-			(require-all
-				(subpath "${HOME}/Library/Caches/com.apple.akd")
-				(extension-class "com.apple.mediaserverd.read")
-			)
-		)
-	)
-)
 (deny file-issue-extension
 	(require-all
 		(require-not (extension "com.apple.app-sandbox.read"))

 )
 (allow file-write*
 	(require-all
-		(subpath "/private/var")
 		(require-any
 			(subpath "${FRONT_USER_HOME}")
 			(subpath "${HOME}")
 		)
+		(subpath "/private/var")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.akd(/|$)")
 	)
 )

 
 (allow file-write-create
 	(require-all
-		(subpath "/private/var")
 		(require-any
 			(subpath "${FRONT_USER_HOME}")
 			(subpath "${HOME}")
 		)
+		(subpath "/private/var")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.akd(/|$)")
 	)
 )

 )
 (allow file-write-unlink
 	(require-all
-		(subpath "/private/var")
 		(require-any
 			(subpath "${FRONT_USER_HOME}")
 			(subpath "${HOME}")
 		)
+		(subpath "/private/var")
 		(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/SystemData/com\.apple\.akd(/|$)")
 	)
 )
```
