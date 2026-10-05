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

 		(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.seserviced.session")
-		(%entitlement-is-present "com.apple.developer.carkey.session")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.merchantd.identity")
-		(%entitlement-is-present "com.apple.developer.proximity-reader.identity.read")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.coreidvd.digital-presentment.xpc")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(require-any

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.MomentsUIService")
-		(%entitlement-is-present "com.apple.developer.journal.allow")
+		(global-name "com.apple.merchantd.identity")
+		(%entitlement-is-present "com.apple.developer.proximity-reader.identity.read")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.ServicesPaymentAngel")
+		(%entitlement-is-present "com.apple.private.applemediaservices")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.coreidvd.digital-presentment.xpc")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
+	)
+)
+(allow mach-lookup
+	(require-all
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
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.seserviced.session")
+		(%entitlement-is-present "com.apple.developer.carkey.session")
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
-		(global-name "com.apple.messages.critical-messaging")
-		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.MusicKit.UI")

 		(%entitlement-is-present "com.apple.developer.declared-age-range")
 	)
 )
+(allow mach-lookup
+	(require-all
+		(system-attribute internal-build)
+		(require-any
+			(global-name "com.apple.EventTimingProfileService")
+			(global-name "com.apple.JetTracingSupport.JetTracingService")
+		)
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.ak.auth.xpc")

 		(system-attribute developer-mode)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(system-attribute internal-build)
-		(require-any
-			(global-name "com.apple.EventTimingProfileService")
-			(global-name "com.apple.JetTracingSupport.JetTracingService")
-		)
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.ExposureNotification")

 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.messages.critical-messaging")
+		(require-any
+			(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
+			(%entitlement-is-present "com.apple.developer.upi-device-validation")
+		)
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.callkit.networkextension.voip")

 		(xpc-service-name "com.apple.intents.intents-helper")
 		(xpc-service-name "com.apple.mscamerad-xpc")
 		(xpc-service-name "com.apple.siri.context.service")
+		(xpc-service-name "com.apple.siri.orchestration.capabilities")
 		(xpc-service-name "com.apple.textkit.nsattributedstringagent")
 		(xpc-service-name "com.apple.tonelibraryd")
 		(xpc-service-name "com.apple.uifoundation-bundle-helper")
```
