## replayd

> Group: ⬆️ Updated

```diff

 
 (allow file-graft)
 
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.nsurlsessiond.readonly")
-		(extension "com.apple.sandbox.executable")
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.replayd.read-only")
+		(extension-class "com.apple.mediaserverd.read-write")
 		(subpath "${HOME}/Library/ReplayKit")
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.nsurlsessiond.readonly")
+		(extension "com.apple.sandbox.executable")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
 		(subpath "${HOME}/Library/ReplayKit")
 	)
 )

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
-		(require-any
-			(require-all
-				(extension-class "com.apple.mediaserverd.read")
-				(require-any
-					(extension "com.apple.security.exception.files.absolute-path.read-only")
-					(extension "com.apple.security.exception.files.absolute-path.read-write")
-					(extension "com.apple.security.exception.files.home-relative-path.read-only")
-					(extension "com.apple.security.exception.files.home-relative-path.read-write")
-					(require-any
-						(subpath "${PROCESS_TEMP_DIR}/com.apple.replayd")
-						(subpath "/private/var/tmp/com.apple.replayd")
-					)
-				)
-			)
-			(subpath "${HOME}/Library/ReplayKit")
-		)
+		(extension-class "com.apple.replayd.read-only")
+		(subpath "${HOME}/Library/ReplayKit")
 	)
 )
 (deny file-issue-extension
```
