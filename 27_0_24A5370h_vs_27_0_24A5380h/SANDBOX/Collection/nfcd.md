## nfcd

> Group: ⬆️ Updated

```diff

 	)
 )
 
+(allow file-issue-extension
+	(require-all
+		(extension-class "com.apple.aned.read-only")
+		(extension "com.apple.assets.read")
+		(require-any
+			(subpath "${HOME}/Library/Assets")
+			(subpath "/private/var/MobileAsset")
+		)
+	)
+)
+
 (allow file-link)
 
 (allow file-lock)
```
