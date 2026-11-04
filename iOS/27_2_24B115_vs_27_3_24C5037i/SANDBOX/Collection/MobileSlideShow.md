## MobileSlideShow

> Group: ⬆️ Updated

```diff

 ;; (default) inherited from parent profile "baseline"
 (delegate default)
 
-(allow asr-parser-enter)
-
 (allow coalition-info)
 
 (allow consume-extension)

 			(global-name "com.apple.frontboard.systemappservices")
 			(global-name "com.apple.frontboard.workspace")
 			(global-name "com.apple.geoanalyticsd")
+			(global-name "com.apple.gputools.producer")
 			(global-name "com.apple.handwritingd.remoterecognition")
 			(global-name "com.apple.icloud.fmfd")
 			(global-name "com.apple.iconservices")

 			(global-name "com.apple.locationd.registration")
 			(global-name "com.apple.locationd.spi")
 			(global-name "com.apple.locationd.synchronous")
+			(global-name "com.apple.lsd.advertisingidentifiers")
+			(global-name "com.apple.lsd.openurl")
 			(global-name "com.apple.lsd.xpc")
 			(global-name "com.apple.marco")
 			(global-name "com.apple.mediaanalysisd.analysis")

 				(global-name "com.apple.SafetyKit")
 				(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
 			)
-			(require-all
-				(global-name "com.apple.ServicesPaymentAngel")
-				(require-any
-					(%entitlement-is-present "com.apple.private.applemediaservices")
-					(xpc-service-name ".viewservice")
-				)
-			)
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

 				)
 				(%entitlement-is-present "com.apple.private.device-configuration.effective-configuration-ids.read")
 			)
+			(require-all
+				(require-any
+					(global-name "com.apple.ServicesPaymentAngel")
+					(global-name "com.apple.ServicesPaymentAngel.jetpackAssets")
+				)
+				(require-any
+					(%entitlement-is-present "com.apple.private.applemediaservices")
+					(xpc-service-name ".viewservice")
+				)
+			)
 			(require-all
 				(require-any
 					(global-name "com.apple.cloudd.debug")

 				(global-name "com.apple.SpatialAudioProfileXPCService")
 				(global-name "com.apple.StoreKitUISceneService")
 				(global-name "com.apple.TelephonyTransferService")
+				(global-name "com.apple.ThreadNetwork.xpc")
 				(global-name "com.apple.UIKit.OverlayUI.services")
 				(global-name "com.apple.UIKit.SecureControlService")
 				(global-name "com.apple.USDKit.FormatLoader")

 				(global-name "com.apple.fullkeyboardaccess.drag.xpc")
 				(global-name "com.apple.gamesaved")
 				(global-name "com.apple.generativeexperiences.externaltextcomposition")
-				(global-name "com.apple.gputools.producer")
 				(global-name "com.apple.handwritingd.pkanalytics")
 				(global-name "com.apple.handwritingd.pksettings")
 				(global-name "com.apple.homed.xpc.accessory-setup")

 				(global-name "com.apple.iap2d.xpc")
 				(global-name "com.apple.iapd.xpc")
 			)
-			(require-any
-				(global-name "com.apple.lsd.advertisingidentifiers")
-				(global-name "com.apple.lsd.openurl")
-			)
 			(require-any
 				(global-name "com.apple.timesync.expositor")
 				(global-name "com.apple.timesync.manager")

 			(global-name "com.apple.frontboard.systemappservices")
 			(global-name "com.apple.frontboard.workspace")
 			(global-name "com.apple.geoanalyticsd")
+			(global-name "com.apple.gputools.producer")
 			(global-name "com.apple.handwritingd.remoterecognition")
 			(global-name "com.apple.icloud.fmfd")
 			(global-name "com.apple.iconservices")

 			(global-name "com.apple.locationd.registration")
 			(global-name "com.apple.locationd.spi")
 			(global-name "com.apple.locationd.synchronous")
+			(global-name "com.apple.lsd.advertisingidentifiers")
+			(global-name "com.apple.lsd.openurl")
 			(global-name "com.apple.lsd.xpc")
 			(global-name "com.apple.marco")
 			(global-name "com.apple.mediaanalysisd.analysis")

 				(global-name "com.apple.SafetyKit")
 				(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
 			)
-			(require-all
-				(global-name "com.apple.ServicesPaymentAngel")
-				(require-any
-					(%entitlement-is-present "com.apple.private.applemediaservices")
-					(xpc-service-name ".viewservice")
-				)
-			)
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

 				)
 				(%entitlement-is-present "com.apple.private.device-configuration.effective-configuration-ids.read")
 			)
+			(require-all
+				(require-any
+					(global-name "com.apple.ServicesPaymentAngel")
+					(global-name "com.apple.ServicesPaymentAngel.jetpackAssets")
+				)
+				(require-any
+					(%entitlement-is-present "com.apple.private.applemediaservices")
+					(xpc-service-name ".viewservice")
+				)
+			)
 			(require-all
 				(require-any
 					(global-name "com.apple.cloudd.debug")

 				(global-name "com.apple.SpatialAudioProfileXPCService")
 				(global-name "com.apple.StoreKitUISceneService")
 				(global-name "com.apple.TelephonyTransferService")
+				(global-name "com.apple.ThreadNetwork.xpc")
 				(global-name "com.apple.UIKit.OverlayUI.services")
 				(global-name "com.apple.UIKit.SecureControlService")
 				(global-name "com.apple.USDKit.FormatLoader")

 				(global-name "com.apple.fullkeyboardaccess.drag.xpc")
 				(global-name "com.apple.gamesaved")
 				(global-name "com.apple.generativeexperiences.externaltextcomposition")
-				(global-name "com.apple.gputools.producer")
 				(global-name "com.apple.handwritingd.pkanalytics")
 				(global-name "com.apple.handwritingd.pksettings")
 				(global-name "com.apple.homed.xpc.accessory-setup")

 				(global-name "com.apple.iap2d.xpc")
 				(global-name "com.apple.iapd.xpc")
 			)
-			(require-any
-				(global-name "com.apple.lsd.advertisingidentifiers")
-				(global-name "com.apple.lsd.openurl")
-			)
 			(require-any
 				(global-name "com.apple.timesync.expositor")
 				(global-name "com.apple.timesync.manager")

 			(global-name "com.apple.frontboard.systemappservices")
 			(global-name "com.apple.frontboard.workspace")
 			(global-name "com.apple.geoanalyticsd")
+			(global-name "com.apple.gputools.producer")
 			(global-name "com.apple.handwritingd.remoterecognition")
 			(global-name "com.apple.icloud.fmfd")
 			(global-name "com.apple.iconservices")

 			(global-name "com.apple.locationd.registration")
 			(global-name "com.apple.locationd.spi")
 			(global-name "com.apple.locationd.synchronous")
+			(global-name "com.apple.lsd.advertisingidentifiers")
+			(global-name "com.apple.lsd.openurl")
 			(global-name "com.apple.lsd.xpc")
 			(global-name "com.apple.marco")
 			(global-name "com.apple.mediaanalysisd.analysis")

 				(global-name "com.apple.SafetyKit")
 				(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
 			)
-			(require-all
-				(global-name "com.apple.ServicesPaymentAngel")
-				(require-any
-					(%entitlement-is-present "com.apple.private.applemediaservices")
-					(xpc-service-name ".viewservice")
-				)
-			)
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

 				)
 				(%entitlement-is-present "com.apple.private.device-configuration.effective-configuration-ids.read")
 			)
+			(require-all
+				(require-any
+					(global-name "com.apple.ServicesPaymentAngel")
+					(global-name "com.apple.ServicesPaymentAngel.jetpackAssets")
+				)
+				(require-any
+					(%entitlement-is-present "com.apple.private.applemediaservices")
+					(xpc-service-name ".viewservice")
+				)
+			)
 			(require-all
 				(require-any
 					(global-name "com.apple.cloudd.debug")

 				(global-name "com.apple.SpatialAudioProfileXPCService")
 				(global-name "com.apple.StoreKitUISceneService")
 				(global-name "com.apple.TelephonyTransferService")
+				(global-name "com.apple.ThreadNetwork.xpc")
 				(global-name "com.apple.UIKit.OverlayUI.services")
 				(global-name "com.apple.UIKit.SecureControlService")
 				(global-name "com.apple.USDKit.FormatLoader")

 				(global-name "com.apple.fullkeyboardaccess.drag.xpc")
 				(global-name "com.apple.gamesaved")
 				(global-name "com.apple.generativeexperiences.externaltextcomposition")
-				(global-name "com.apple.gputools.producer")
 				(global-name "com.apple.handwritingd.pkanalytics")
 				(global-name "com.apple.handwritingd.pksettings")
 				(global-name "com.apple.homed.xpc.accessory-setup")

 				(global-name "com.apple.iap2d.xpc")
 				(global-name "com.apple.iapd.xpc")
 			)
-			(require-any
-				(global-name "com.apple.lsd.advertisingidentifiers")
-				(global-name "com.apple.lsd.openurl")
-			)
 			(require-any
 				(global-name "com.apple.timesync.expositor")
 				(global-name "com.apple.timesync.manager")
```
