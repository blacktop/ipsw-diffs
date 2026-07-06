## testmanagerd

> Group: ⬆️ Updated

```diff

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.aned.read-only")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.testmanagerd")
 			(subpath "${PROCESS_TEMP_DIR}/com.apple.testmanagerd")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.mediaserverd.read")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.testmanagerd")
 			(subpath "${PROCESS_TEMP_DIR}/com.apple.testmanagerd")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(extension "com.apple.sandbox.container")
 			(require-all
-				(extension-class "com.apple.mediaserverd.read")
+				(extension-class "com.apple.aned.read-only")
+				(extension "com.apple.assets.read")
 				(require-any
-					(extension "com.apple.security.exception.files.absolute-path.read-only")
-					(extension "com.apple.security.exception.files.absolute-path.read-write")
-					(extension "com.apple.security.exception.files.home-relative-path.read-only")
-					(extension "com.apple.security.exception.files.home-relative-path.read-write")
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
 				)
 			)
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
-				(subpath "${HOME}/Library/Caches/com.apple.testmanagerd")
-				(extension-class "com.apple.mediaserverd.read")
-			)
-		)
-	)
-)
 (deny file-issue-extension
 	(require-all
 		(require-not (extension "com.apple.app-sandbox.read"))

 
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.testmanagerd")
 	)
 )

 		(preference-domain "com.apple.Metal")
 		(preference-domain "com.apple.MobileAsset")
 		(preference-domain "com.apple.UIKit")
+		(preference-domain "com.apple.assistant.public")
 		(preference-domain "com.apple.assistant.support")
 		(preference-domain "com.apple.avfoundation")
 		(preference-domain "com.apple.backboardd")

 		(preference-domain "com.apple.Metal")
 		(preference-domain "com.apple.MobileAsset")
 		(preference-domain "com.apple.UIKit")
+		(preference-domain "com.apple.assistant.public")
 		(preference-domain "com.apple.assistant.support")
 		(preference-domain "com.apple.avfoundation")
 		(preference-domain "com.apple.backboardd")
```
