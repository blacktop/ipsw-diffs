## bulletindistributord

> Group: ⬆️ Updated

```diff

 						(extension-class "com.apple.mediaserverd.read-write")
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/BulletinDistributor($|/)")
 					)
-					(require-all
-						(extension-class "com.apple.mediaserverd.read-write")
-						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/DeviceRegistry/[-0-9A-Z]+/BulletinDistributor($|/)")
-					)
 					(require-all
 						(extension-class "com.apple.quicklook.readonly")
 						(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Library/UserNotifications/[^/]+/Attachments(/|$)")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.app-sandbox.read")
 		(subpath "${HOME}/Library/Caches/com.apple.itunesstored")
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.app-sandbox.read-write")
+		(subpath "${HOME}/Library/Caches/com.apple.itunesstored")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(extension "com.apple.security.exception.files.absolute-path.read-only")
+			(extension "com.apple.security.exception.files.absolute-path.read-write")
+			(extension "com.apple.security.exception.files.home-relative-path.read-only")
+			(extension "com.apple.security.exception.files.home-relative-path.read-write")
+			(subpath "${HOME}/Library/Caches/com.apple.itunesstored")
+		)
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read-write")
+		(require-any
+			(extension "com.apple.security.exception.files.absolute-path.read-write")
+			(subpath "${HOME}/Library/Caches/com.apple.itunesstored")
+		)
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(subpath "/private/var")

 		)
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(subpath "${HOME}/Library/Caches/com.apple.bulletindistributord")
-		(extension-class "com.apple.app-sandbox.read-write")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(extension "com.apple.security.exception.files.absolute-path.read-only")
-			(extension "com.apple.security.exception.files.absolute-path.read-write")
-			(extension "com.apple.security.exception.files.home-relative-path.read-only")
-			(extension "com.apple.security.exception.files.home-relative-path.read-write")
-			(subpath "${HOME}/Library/Caches/com.apple.itunesstored")
-		)
+		(subpath "${HOME}/Library/Caches/com.apple.itunesstored")
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(subpath "${HOME}/Library/Caches/com.apple.itunesstored")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(extension-class "com.apple.aned.read-only")
-			(extension-class "com.apple.app-sandbox.read")
-			(extension-class "com.apple.app-sandbox.read-write")
-			(extension-class "com.apple.mediaserverd.read")
-			(extension-class "com.apple.mediaserverd.read-write")
+			(require-all
+				(subpath "${HOME}/Library/Caches/com.apple.bulletindistributord")
+				(extension-class "com.apple.aned.read-only")
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.itunesstored")
 		)
 	)
 )
```
