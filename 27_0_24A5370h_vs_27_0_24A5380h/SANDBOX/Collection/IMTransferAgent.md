## IMTransferAgent

> Group: ⬆️ Updated

```diff

 
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read")
-		(subpath "/private/var/tmp/com.apple.messages")
+		(extension-class "com.apple.app-sandbox.read-write")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
+			(subpath "/private/var/tmp/com.apple.messages")
+		)
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "/private/var/tmp/com.apple.messages")
+		(extension-class "com.apple.identityservices.send")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
+			(subpath "/private/var/tmp/com.apple.messages")
+		)
 	)
 )
 (allow file-issue-extension

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.identityservices.send")
+		(extension-class "com.apple.app-sandbox.read")
 		(require-any
 			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
 			(subpath "/private/var/tmp/com.apple.messages")

 			(extension-class "com.apple.mediaserverd.read")
 			(extension-class "com.apple.mediaserverd.read")
 			(extension-class "com.apple.mediaserverd.read-write")
-			(extension-class "com.apple.mediaserverd.read-write")
 		)
 	)
 )

 
 (allow file-write-create
 	(require-all
-		(vnode-type DIRECTORY REGULAR-FILE)
+		(vnode-type REGULAR-FILE)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.imtransferservices.IMTransferAgent")
 	)
 )
```
