## MobileSlideShow

> Group: ⬆️ Updated

```diff

 					(xpc-service-name ".viewservice")
 				)
 			)
-			(require-all
-				(global-name "com.apple.ThreadNetwork.xpc")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
-					(xpc-service-name ".viewservice")
-				)
-			)
 			(require-all
 				(global-name "com.apple.ak.anisette.xpc")
 				(process-attribute is-apple-signed-executable)

 				(global-name "com.apple.SpatialAudioProfileXPCService")
 				(global-name "com.apple.StoreKitUISceneService")
 				(global-name "com.apple.TelephonyTransferService")
+				(global-name "com.apple.ThreadNetwork.xpc")
 				(global-name "com.apple.UIKit.OverlayUI.services")
 				(global-name "com.apple.UIKit.SecureControlService")
 				(global-name "com.apple.USDKit.FormatLoader")

 					(xpc-service-name ".viewservice")
 				)
 			)
-			(require-all
-				(global-name "com.apple.ThreadNetwork.xpc")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
-					(xpc-service-name ".viewservice")
-				)
-			)
 			(require-all
 				(global-name "com.apple.ak.anisette.xpc")
 				(process-attribute is-apple-signed-executable)

 				(global-name "com.apple.SpatialAudioProfileXPCService")
 				(global-name "com.apple.StoreKitUISceneService")
 				(global-name "com.apple.TelephonyTransferService")
+				(global-name "com.apple.ThreadNetwork.xpc")
 				(global-name "com.apple.UIKit.OverlayUI.services")
 				(global-name "com.apple.UIKit.SecureControlService")
 				(global-name "com.apple.USDKit.FormatLoader")

 					(xpc-service-name ".viewservice")
 				)
 			)
-			(require-all
-				(global-name "com.apple.ThreadNetwork.xpc")
-				(require-any
-					(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
-					(xpc-service-name ".viewservice")
-				)
-			)
 			(require-all
 				(global-name "com.apple.ak.anisette.xpc")
 				(process-attribute is-apple-signed-executable)

 				(global-name "com.apple.SpatialAudioProfileXPCService")
 				(global-name "com.apple.StoreKitUISceneService")
 				(global-name "com.apple.TelephonyTransferService")
+				(global-name "com.apple.ThreadNetwork.xpc")
 				(global-name "com.apple.UIKit.OverlayUI.services")
 				(global-name "com.apple.UIKit.SecureControlService")
 				(global-name "com.apple.USDKit.FormatLoader")
```
