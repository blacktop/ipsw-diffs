## hangreporter

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
-		(require-not (xpc-service-name "com.apple.tailspin.symbolicationserver"))
+		(require-not (require-any
+			(xpc-service-name "com.apple.tailspin.augmentationserver")
+			(xpc-service-name "com.apple.tailspin.symbolicationserver")
+		))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.ERFoundationExtensionDaemon"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
```
