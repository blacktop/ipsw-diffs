## healthd

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${HOME}/Library/Caches/com.apple.healthd")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.healthd")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.healthd")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "${HOME}/Library/Caches/com.apple.healthd")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Library/Caches/com.apple.healthd")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.healthd")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.healthd")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "${HOME}/Library/Caches/com.apple.healthd")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.healthd")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.healthd")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.healthd")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.healthd")
+		)
 	)
 )
 (allow file-issue-extension

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.healthd")
 			(subpath "${HOME}/Library/HTTPStorages/com.apple.healthd")

 )
 (allow file-write*
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type DIRECTORY REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.healthd")
 	)
 )

 )
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type DIRECTORY REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.healthd")
 	)
 )

 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type DIRECTORY REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.healthd")
 	)
 )
```
