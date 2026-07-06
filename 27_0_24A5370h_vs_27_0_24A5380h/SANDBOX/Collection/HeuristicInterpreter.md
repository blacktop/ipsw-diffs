## HeuristicInterpreter

> Group: ⬆️ Updated

```diff

 
 (allow file-graft)
 
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
 (deny file-issue-extension
 	(require-all
 		(require-not (extension "com.apple.app-sandbox.read"))
```
