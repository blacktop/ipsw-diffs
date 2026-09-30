## quicklookd

> Group: ⬆️ Updated

```diff

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.appmanagedfeatures.restrictions")
-		(%entitlement-is-present "com.apple.developer.appmanagedfeatures")
+		(global-name "com.apple.seserviced.credential.manager")
+		(%entitlement-is-present "com.apple.developer.secure-element-credential")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.assessmentagent")
-		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
+		(global-name "com.apple.ThreadNetwork.xpc")
+		(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.SafetyKit")
-		(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
+		(global-name "com.apple.appmanagedfeatures.restrictions")
+		(%entitlement-is-present "com.apple.developer.appmanagedfeatures")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.MomentsUIService")
+		(%entitlement-is-present "com.apple.developer.journal.allow")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.seserviced.credential.manager")
-		(%entitlement-is-present "com.apple.developer.secure-element-credential")
+		(global-name "com.apple.assessmentagent")
+		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
 	)
 )
 (allow mach-lookup

 		(%entitlement-is-present "com.apple.developer.proximity-reader.identity.read")
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
 		(global-name "com.apple.family.ageRange.xpc")

 )
 (allow mach-lookup
 	(require-all
-		(require-any
-			(global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.VerificationCodes")
-			(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
-		)
-		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
+		(global-name "com.apple.ExposureNotification")
+		(%entitlement-is-present "com.apple.developer.exposure-notification")
 	)
 )
 (allow mach-lookup

 		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.SafetyKit")
+		(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.seserviced.session")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.MomentsUIService")
-		(%entitlement-is-present "com.apple.developer.journal.allow")
+		(require-any
+			(global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.VerificationCodes")
+			(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
+		)
+		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
 	)
 )
 (allow mach-lookup

 		(global-name "com.apple.TextInput.preferences")
 		(global-name "com.apple.TextInput.rdt")
 		(global-name "com.apple.TextInput.shortcuts")
-		(global-name "com.apple.ThreadNetwork.xpc")
 		(global-name "com.apple.UIKit.KeyboardManagement.hosted")
 		(global-name "com.apple.UIKit.OverlayUI.services")
 		(global-name "com.apple.UIKit.SecureControlService")
```
