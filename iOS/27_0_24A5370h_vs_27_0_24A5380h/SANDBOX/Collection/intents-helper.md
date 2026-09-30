## intents-helper

> Group: ⬆️ Updated

```diff

 		(subpath "${HOME}/Library/Caches/com.apple.metal")
 	)
 )
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(require-any
-			(subpath "/AppleInternal/Applications")
-			(subpath "/System/Developer/Applications")
-		)
-	)
-)
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(require-any
-			(subpath "/AppleInternal/Applications")
-			(subpath "/System/Developer/Applications")
-		)
+		(subpath "/AppleInternal/Applications")
 	)
 )
 (allow file-issue-extension

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "${HOME}/Library/Caches/com.apple.metal")
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "/AppleInternal/Applications")
 	)
 )
 (allow file-issue-extension

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
-			(require-any
-				(subpath "/AppleInternal/Applications")
-				(subpath "/System/Developer/Applications")
-			)
 			(require-any
 				(subpath "/private/var/factory_mount/[^/]+/Applications")
 				(subpath "/private/var/personalized_automation/Applications")

 			)
 			(subpath "${FRONT_USER_HOME}/Containers/Bundle")
 			(subpath "${HOME}/Library/Caches/com.apple.metal")
+			(subpath "/AppleInternal/Applications")
 			(subpath "/Applications")
 			(subpath "/Developer/Applications")
+			(subpath "/System/Developer/Applications")
 			(subpath "/private/var/containers/Bundle")
 		)
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read-write")
+		(extension-class "com.apple.app-sandbox.read-write")
 		(require-any
 			(require-all
 				(subpath "${HOME}/Library/Caches/com.apple.intents.intents-helper")
-				(extension-class "com.apple.mediaserverd.read-write")
+				(extension-class "com.apple.app-sandbox.read-write")
 			)
 			(subpath "${HOME}/Library/Caches/com.apple.metal")
 		)

 )
 (allow file-read*
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.metal")
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.intents.intents-helper")
 	)
 )
 (allow file-read*

 )
 (allow file-read*
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.intents.intents-helper")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.metal")

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.metal")
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.intents.intents-helper")
 	)
 )
 (allow file-read-metadata

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.intents.intents-helper")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.metal")

 
 (allow file-write*
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.metal")
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.intents.intents-helper")
 	)
 )
 (allow file-write*
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.intents.intents-helper")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.metal")

 )
 (allow file-write-create
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.metal")
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.intents.intents-helper")
 	)
 )
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.intents.intents-helper")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.metal")

 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type REGULAR-FILE)
-		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.metal")
+		(vnode-type DIRECTORY)
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.intents.intents-helper")
 	)
 )
 (allow file-write-unlink
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.intents.intents-helper")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.metal")
```
