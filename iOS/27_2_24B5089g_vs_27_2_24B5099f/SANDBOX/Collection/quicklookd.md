## quicklookd

> Group: ⬆️ Updated

```diff

 		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
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
 		(global-name "com.apple.seserviced.session")

 		(%entitlement-is-present "com.apple.developer.journal.allow")
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.ServicesPaymentAngel")
-		(%entitlement-is-present "com.apple.private.applemediaservices")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.weatherkit.authservice")
-		(%entitlement-is-present "com.apple.developer.weatherkit")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.odi.assessmentService")

 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.weatherkit.authservice")
+		(%entitlement-is-present "com.apple.developer.weatherkit")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.merchantd.discovery")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.MusicKit.UI")
+		(global-name "com.apple.messages.critical-messaging")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.storekit.cloud-service-exempted-from-tcc-access")
-			(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+			(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
+			(%entitlement-is-present "com.apple.developer.upi-device-validation")
 		)
 	)
 )

 		(%entitlement-is-present "com.apple.private.device-configuration.effective-configuration-ids.read")
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.ServicesPaymentAngel")
+		(%entitlement-is-present "com.apple.private.applemediaservices")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.MusicKit.UI")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.storekit.cloud-service-exempted-from-tcc-access")
+			(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+		)
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.system.notification_center")

 		(xpc-service-name "com.apple.intents.intents-helper")
 		(xpc-service-name "com.apple.mscamerad-xpc")
 		(xpc-service-name "com.apple.siri.context.service")
+		(xpc-service-name "com.apple.siri.orchestration.capabilities")
 		(xpc-service-name "com.apple.textkit.nsattributedstringagent")
 		(xpc-service-name "com.apple.tonelibraryd")
 		(xpc-service-name "com.apple.uifoundation-bundle-helper")
```
