## apsd

> Group: ⬆️ Updated

```diff

 		)
 	)
 )
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.nsurlsessiond.readonly")
+		(extension "com.apple.sandbox.executable")
+	)
+)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.aned.read-only")
+		(subpath "${HOME}/Library/Caches/com.apple.persistentconnection")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension "com.apple.assets.read")
 		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.apsd")
-			(subpath "${HOME}/Library/Caches/com.apple.persistentconnection")
+			(require-all
+				(subpath "${HOME}/Library/Assets")
+				(extension-class "com.apple.aned.read-only")
+			)
+			(require-all
+				(subpath "/private/var/MobileAsset")
+				(extension-class "com.apple.aned.read-only")
+			)
 		)
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.apsd")
-			(subpath "${HOME}/Library/Caches/com.apple.persistentconnection")
-		)
+		(subpath "${HOME}/Library/Caches/com.apple.persistentconnection")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(require-any
-			(subpath "${HOME}/Library/Caches/com.apple.apsd")
-			(subpath "${HOME}/Library/Caches/com.apple.persistentconnection")
-		)
+		(subpath "${HOME}/Library/Caches/com.apple.persistentconnection")
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.nsurlsessiond.readonly")
-		(extension "com.apple.sandbox.executable")
+		(extension-class "com.apple.mediaserverd.read-write")
+		(subpath "${HOME}/Library/Caches/com.apple.persistentconnection")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(require-any
+			(require-all
+				(subpath "${HOME}/Library/Caches/com.apple.apsd")
+				(extension-class "com.apple.mediaserverd.read")
+			)
+			(subpath "${HOME}/Library/Caches/com.apple.persistentconnection")
+		)
 	)
 )
 (deny file-issue-extension

 	)
 )
 
-(allow file-read*
-	(require-all
-		(%entitlement-is-present "com.apple.private.networkextension.configuration")
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
-	)
-)
 (allow file-read*
 	(require-all
 		(extension "com.apple.assets.read")

 		)
 	)
 )
+(allow file-read*
+	(require-all
+		(%entitlement-is-present "com.apple.private.networkextension.configuration")
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
+	)
+)
 (allow file-read*
 	(require-all
 		(subpath "/private/var")

 	)
 )
 
-(allow file-read-metadata
-	(require-all
-		(%entitlement-is-present "com.apple.private.networkextension.configuration")
-		(literal "/private/var/preferences/com.apple.networkextension.plist")
-	)
-)
 (allow file-read-metadata
 	(require-all
 		(extension "com.apple.assets.read")

 		)
 	)
 )
+(allow file-read-metadata
+	(require-all
+		(%entitlement-is-present "com.apple.private.networkextension.configuration")
+		(literal "/private/var/preferences/com.apple.networkextension.plist")
+	)
+)
 (allow file-read-metadata
 	(require-all
 		(subpath "/private/var")
```
