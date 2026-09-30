## mobileactivationd

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileactivationd")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.mobileactivationd")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileactivationd")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileactivationd")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileactivationd")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.mobileactivationd")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileactivationd")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileactivationd")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.mobileactivationd")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileactivationd")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(subpath "${HOME}/Library/Caches/com.apple.mobileactivationd")
+			(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileactivationd")
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
-			(subpath "${HOME}/Library/Caches/com.apple.mobileactivationd")
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.mobileactivationd")
+				(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileactivationd")
+			)
 			(subpath "${HOME}/Library/Cookies")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.mobileactivationd")
 		)
 	)
 )

 
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.mobileactivationd")
 	)
 )
```
