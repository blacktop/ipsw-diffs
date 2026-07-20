## maild

> Group: ⬆️ Updated

```diff

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

 		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.seserviced.credential.manager")
+		(%entitlement-is-present "com.apple.developer.secure-element-credential")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.ExposureNotification")

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

 		(%entitlement-is-present "com.apple.developer.journal.allow")
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.MusicKit.UI")
+		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.ak.anisette.xpc")

 		)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
-		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.ak.auth.xpc")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.MusicKit.UI")
-		(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+		(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
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
