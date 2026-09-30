## NetworkExtensionSubscriber

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.nehelper"))
+		(require-not (global-name "com.apple.securityd"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
