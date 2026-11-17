## DTServiceHub

> Group: ⬆️ Updated

```diff

 			(xpc-service-name "com.apple.dt.DTConditionInducerSupportService")
 			(xpc-service-name "com.apple.dt.DTMLModelRunnerService")
 			(xpc-service-name "com.apple.dt.DTScreenshotService")
-			(xpc-service-name "com.apple.dt.instruments.dtsecurity.xpc")
 		))
 		(require-not (global-name "com.apple.carousel.backlightxpc"))
 		(require-not (global-name "com.apple.diagd"))

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
-		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
+		(require-not (xpc-service-name "com.apple.dt.instruments.dtsecurity.xpc"))
 		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))
 	)
```
