## adtrackingd

> Group: ⬆️ Updated

```diff

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.ap.adprivacyd")
-			(subpath "${HOME}/Library/HTTPStorages/com.apple.ap.adprivacyd")
-		)
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")

 		(extension "com.apple.sandbox.executable")
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(require-any
+			(require-all
+				(extension-class "com.apple.aned.read-only")
+				(extension "com.apple.assets.read")
+				(require-any
+					(subpath "${HOME}/Library/Assets")
+					(subpath "/private/var/MobileAsset")
+				)
+			)
+			(require-any
+				(subpath "${HOME}/Library/Caches/com.apple.ap.adprivacyd")
+				(subpath "${HOME}/Library/HTTPStorages/com.apple.ap.adprivacyd")
+			)
+		)
+	)
+)
 (deny file-issue-extension
 	(require-all
 		(require-not (extension "com.apple.app-sandbox.read"))

 
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.ap.adprivacyd")
 	)
 )
```
