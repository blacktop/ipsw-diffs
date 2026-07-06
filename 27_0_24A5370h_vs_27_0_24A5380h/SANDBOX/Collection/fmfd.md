## fmfd

> Group: ⬆️ Updated

```diff

 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.icloud.fmfd")
+		(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.app-sandbox.read-write")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.icloud.fmfd")
-	)
-)
-(allow file-issue-extension
-	(require-all
-		(extension-class "com.apple.aned.read-only")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.icloud.fmfd")
+		(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
 	)
 )
 (allow file-issue-extension
 	(require-all
 		(extension-class "com.apple.mediaserverd.read-write")
-		(subpath "${HOME}/Library/HTTPStorages/com.apple.icloud.fmfd")
+		(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
+	)
+)
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.mediaserverd.read")
+		(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
 	)
 )
 (allow file-issue-extension

 )
 (allow file-issue-extension
 	(require-all
-		(extension-class "com.apple.mediaserverd.read")
+		(extension-class "com.apple.aned.read-only")
 		(require-any
 			(subpath "${HOME}/Library/Caches/com.apple.AppleAccount")
 			(subpath "${HOME}/Library/Caches/com.apple.icloud.fmfd")

 )
 (allow file-read*
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.icloud.fmfd")
 	)
 )

 )
 (allow file-read*
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
-			)
+			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.icloud.fmfd")
 		)
 	)

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type REGULAR-FILE)
+		(vnode-type DIRECTORY)
 		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.icloud.fmfd")
 	)
 )

 )
 (allow file-read-metadata
 	(require-all
-		(vnode-type DIRECTORY)
+		(vnode-type REGULAR-FILE)
 		(require-any
-			(require-all
-				(vnode-type DIRECTORY)
-				(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
-			)
+			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
 			(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.icloud.fmfd")
 		)
 	)

 (allow file-write*
 	(require-all
 		(vnode-type REGULAR-FILE)
-		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.icloud.fmfd")
 	)
 )
 (allow file-write*

 				(vnode-type REGULAR-FILE)
 				(require-any
 					(subpath "${HOME}/Library/AddressBook")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.icloud.fmfd")
 				)
 			)
 			(subpath "${HOME}/Library/AddressBook/Delegates")

 				(vnode-type REGULAR-FILE)
 				(require-any
 					(subpath "${HOME}/Library/AddressBook")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.icloud.fmfd")
 				)
 			)
 			(subpath "${HOME}/Library/AddressBook/Delegates")

 (allow file-write-create
 	(require-all
 		(vnode-type REGULAR-FILE)
-		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.icloud.fmfd")
 	)
 )
 (allow file-write-create

 (allow file-write-unlink
 	(require-all
 		(vnode-type REGULAR-FILE)
-		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
+		(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.icloud.fmfd")
 	)
 )
 (allow file-write-unlink

 				(vnode-type REGULAR-FILE)
 				(require-any
 					(subpath "${HOME}/Library/AddressBook")
-					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.AppleAccount")
+					(subpath "${HOME}/Library/Caches/com.apple.nsurlsessiond/Downloads/com.apple.icloud.fmfd")
 				)
 			)
 			(subpath "${HOME}/Library/AddressBook/Delegates")
```
