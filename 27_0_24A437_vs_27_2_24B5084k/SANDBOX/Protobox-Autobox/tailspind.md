## tailspind

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
-		(require-not (xpc-service-name "com.apple.tailspin.symbolicationserver"))
+		(require-not (require-any
+			(xpc-service-name "com.apple.tailspin.augmentationserver")
+			(xpc-service-name "com.apple.tailspin.symbolicationserver")
+		))
 		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
-		(require-not (xpc-service-name "com.apple.tailspin.augmentationserver"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))

 	(require-all
 		(require-not (literal "/usr/bin/tailspin"))
 		(require-not (literal "/usr/bin/plutil"))
+		(require-not (literal "/usr/bin/atos"))
 		(require-not (literal "/bin/sh"))
 	)
 )
```
