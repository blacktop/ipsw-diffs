## backgroundassets.user

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.dmd.policy"))
 		(require-not (global-name "com.apple.misagent"))
 		(require-not (global-name "com.apple.aggregated"))
-		(require-not (xpc-service-name "com.apple.STExtractionService"))
-		(require-not (xpc-service-name "com.apple.STExtractionService.privileged"))
-		(require-not (xpc-service-name "com.apple.extensionkitservice"))
-		(require-not (xpc-service-name "com.apple.backgroundassets.managed.helper.service"))
+		(require-not (require-any
+			(xpc-service-name "com.apple.STExtractionService")
+			(xpc-service-name "com.apple.STExtractionService.privileged")
+		))
 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")

 			(require-all
 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
+				(require-not (xpc-service-name "com.apple.extensionkitservice"))
+				(require-not (xpc-service-name "com.apple.backgroundassets.managed.helper.service"))
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
 				(require-not (global-name "com.apple.PowerManagement.control"))
 				(require-not (global-name "com.apple.FileCoordination"))
```
