## com.apple.MobileAsset.DownloadService.Builtin

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (xpc-service-name "com.apple.StreamingUnzipService"))
 		(require-not (xpc-service-name "com.apple.STExtractionService"))
+		(require-not (xpc-service-name "com.apple.StreamingUnzipService"))
 		(require-not (global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent"))
 		(require-not (system-attribute developer-mode))
 	)
```
