## callkit.calldirectory

> Group: ⬆️ Updated

```diff

 
 (allow file-issue-extension
 	(require-all
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.CallKit.CallDirectory")
-		(extension-class "com.apple.app-sandbox.read-write")
+		(subpath "/private/var/tmp/com.apple.CallKit.CallDirectory")
+		(extension-class "com.apple.mediaserverd.read-write")
 	)
 )
 (allow file-issue-extension
 	(require-all
-		(subpath "/private/var/tmp/com.apple.CallKit.CallDirectory")
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.CallKit.CallDirectory")
 		(require-any
 			(extension-class "com.apple.aned.read-only")
 			(extension-class "com.apple.app-sandbox.read")
```
