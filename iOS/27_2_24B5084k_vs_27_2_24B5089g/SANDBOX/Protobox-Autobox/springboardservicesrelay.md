## springboardservicesrelay

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))
 	)
```
