## maild

> Group: ⬆️ Updated

```diff

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.seserviced.credential.manager")
-		(%entitlement-is-present "com.apple.developer.secure-element-credential")
+		(global-name "com.apple.MomentsUIService")
+		(%entitlement-is-present "com.apple.developer.journal.allow")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ThreadNetwork.xpc")
-		(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
+		(require-any
+			(global-name "com.apple.ServicesPaymentAngel")
+			(global-name "com.apple.ServicesPaymentAngel.jetpackAssets")
+		)
+		(%entitlement-is-present "com.apple.private.applemediaservices")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.MomentsUIService")
-		(%entitlement-is-present "com.apple.developer.journal.allow")
+		(global-name "com.apple.seserviced.credential.manager")
+		(%entitlement-is-present "com.apple.developer.secure-element-credential")
 	)
 )
 (allow mach-lookup

 		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.ServicesPaymentAngel")
-		(%entitlement-is-present "com.apple.private.applemediaservices")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(require-any

 		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.ExposureNotification")
-		(%entitlement-is-present "com.apple.developer.exposure-notification")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.seserviced.session")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.family.ageRange.xpc")
-		(%entitlement-is-present "com.apple.developer.declared-age-range")
+		(global-name "com.apple.MusicKit.UI")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.storekit.cloud-service-exempted-from-tcc-access")
+			(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ak.auth.xpc")
-		(process-attribute is-apple-signed-executable)
+		(global-name "com.apple.family.ageRange.xpc")
+		(%entitlement-is-present "com.apple.developer.declared-age-range")
 	)
 )
 (allow mach-lookup

 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.ak.auth.xpc")
+		(process-attribute is-apple-signed-executable)
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.gputools.service")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.MusicKit.UI")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.storekit.cloud-service-exempted-from-tcc-access")
-			(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-		)
+		(global-name "com.apple.ExposureNotification")
+		(%entitlement-is-present "com.apple.developer.exposure-notification")
 	)
 )
 (allow mach-lookup

 	(require-all
 		(require-not (xpc-service-name "*"))
 		(require-any
+			(global-name "com.apple.lsd.advertisingidentifiers")
+			(global-name "com.apple.lsd.openurl")
 			(global-name "com.apple.tccd")
 			(require-all
 				(global-name "com.apple.system.notification_center")
 				(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
 			)
-			(require-any
-				(global-name "com.apple.lsd.advertisingidentifiers")
-				(global-name "com.apple.lsd.openurl")
-			)
 		)
 	)
 )

 		(global-name "com.apple.TextInput.preferences")
 		(global-name "com.apple.TextInput.rdt")
 		(global-name "com.apple.TextInput.shortcuts")
+		(global-name "com.apple.ThreadNetwork.xpc")
 		(global-name "com.apple.UIKit.KeyboardManagement.hosted")
 		(global-name "com.apple.UIKit.OverlayUI.services")
 		(global-name "com.apple.UIKit.SecureControlService")
```
