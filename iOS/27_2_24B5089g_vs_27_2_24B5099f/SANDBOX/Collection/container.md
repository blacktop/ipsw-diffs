## container

> Group: ⬆️ Updated

```diff

 )
 (allow mach-lookup
 	(require-all
-		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
+		(global-name "com.apple.messages.critical-messaging")
 		(require-any
-			(global-name "com.apple.SystemConfiguration.DNSConfiguration")
-			(global-name "com.apple.SystemConfiguration.NetworkInformation")
-			(global-name "com.apple.SystemConfiguration.PPPController")
-			(global-name "com.apple.SystemConfiguration.SCNetworkReachability")
-			(global-name "com.apple.SystemConfiguration.configd")
-			(global-name "com.apple.SystemConfiguration.helper")
-			(global-name "com.apple.commcenter.cupolicy.xpc")
-			(global-name "com.apple.commcenter.xpc")
-			(global-name "com.apple.securityd")
-			(global-name "com.apple.symptoms.symptomsd.managed_events")
-			(global-name "com.apple.symptomsd")
-			(global-name "com.apple.trustd")
-			(global-name "com.apple.usymptomsd")
+			(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
+			(%entitlement-is-present "com.apple.developer.upi-device-validation")
 		)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.icfcallserver")
-		(%entitlement-is-bool-true "com.apple.private.icfcallserver")
+		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
+		(require-any
+			(global-name "com.apple.SystemConfiguration.DNSConfiguration")
+			(global-name "com.apple.SystemConfiguration.NetworkInformation")
+			(global-name "com.apple.SystemConfiguration.PPPController")
+			(global-name "com.apple.SystemConfiguration.SCNetworkReachability")
+			(global-name "com.apple.SystemConfiguration.configd")
+			(global-name "com.apple.SystemConfiguration.helper")
+			(global-name "com.apple.commcenter.cupolicy.xpc")
+			(global-name "com.apple.commcenter.xpc")
+			(global-name "com.apple.securityd")
+			(global-name "com.apple.symptoms.symptomsd.managed_events")
+			(global-name "com.apple.symptomsd")
+			(global-name "com.apple.trustd")
+			(global-name "com.apple.usymptomsd")
+		)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
+		(signing-identifier "com.apple.mobilemail")
 		(require-any
-			(global-name "com.apple.DeviceConfigurationAgent.consumer")
-			(global-name "com.apple.DeviceConfigurationAgent.consumer.async")
-			(global-name "com.apple.DeviceConfigurationAgent.publisher")
-			(global-name "com.apple.deviceconfigurationd.consumer")
-			(global-name "com.apple.deviceconfigurationd.consumer.async")
-			(global-name "com.apple.deviceconfigurationd.publisher")
+			(global-name "com.apple.backupd")
+			(global-name "com.apple.bulletindistributord.server")
+			(global-name "com.apple.harvestd.manager")
+			(global-name "com.apple.identityservicesd.embedded.auth")
+			(global-name "com.apple.mobilemail")
+			(global-name "com.apple.nanoprefsync")
+			(global-name "com.apple.routined.registration")
+			(global-name "com.apple.sharingd.nsxpc")
 		)
-		(%entitlement-is-present "com.apple.private.device-configuration.effective-configuration-ids.read")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.messages.critical-messaging")
-		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
+		(global-name "com.apple.icfcallserver")
+		(%entitlement-is-bool-true "com.apple.private.icfcallserver")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(signing-identifier "com.apple.mobilemail")
-		(require-any
-			(global-name "com.apple.backupd")
-			(global-name "com.apple.bulletindistributord.server")
-			(global-name "com.apple.harvestd.manager")
-			(global-name "com.apple.identityservicesd.embedded.auth")
-			(global-name "com.apple.mobilemail")
-			(global-name "com.apple.nanoprefsync")
-			(global-name "com.apple.routined.registration")
-			(global-name "com.apple.sharingd.nsxpc")
-		)
+		(global-name "com.apple.SystemConfiguration.PPPController-priv")
+		(%entitlement-is-present "com.apple.networking.vpn.configuration")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.SystemConfiguration.PPPController-priv")
-		(%entitlement-is-present "com.apple.networking.vpn.configuration")
+		(require-any
+			(global-name "com.apple.DeviceConfigurationAgent.consumer")
+			(global-name "com.apple.DeviceConfigurationAgent.consumer.async")
+			(global-name "com.apple.DeviceConfigurationAgent.publisher")
+			(global-name "com.apple.deviceconfigurationd.consumer")
+			(global-name "com.apple.deviceconfigurationd.consumer.async")
+			(global-name "com.apple.deviceconfigurationd.publisher")
+		)
+		(%entitlement-is-present "com.apple.private.device-configuration.effective-configuration-ids.read")
 	)
 )
 (allow mach-lookup

 		(xpc-service-name "com.apple.intents.intents-helper")
 		(xpc-service-name "com.apple.mscamerad-xpc")
 		(xpc-service-name "com.apple.siri.context.service")
+		(xpc-service-name "com.apple.siri.orchestration.capabilities")
 		(xpc-service-name "com.apple.textkit.nsattributedstringagent")
 		(xpc-service-name "com.apple.tonelibraryd")
 		(xpc-service-name "com.apple.uifoundation-bundle-helper")
```
