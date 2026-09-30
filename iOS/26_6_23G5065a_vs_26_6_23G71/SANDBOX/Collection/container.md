## container

> Group: ⬆️ Updated

```diff

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

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ak.anisette.xpc")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.authkit.client")
-			(%entitlement-is-bool-true "com.apple.authkit.client.internal")
-			(%entitlement-is-bool-true "com.apple.authkit.client.private")
-			(process-attribute is-apple-signed-executable)
-		)
+		(global-name "com.apple.powerlog.plxpclogger.xpc")
+		(signing-identifier "com.apple.shortcuts")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.browserkitd")
-		(%entitlement-is-present "com.apple.developer.web-browser")
+		(global-name "com.apple.PowerManagement.control")
+		(signing-identifier "com.apple.shortcuts")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.identityservicesd.embedded.auth")
+		(global-name "com.apple.VideoSubscriberAccount.videosubscriptionsd")
 		(require-any
-			(require-any
-				(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
-				(signing-identifier "com.apple.shortcuts.watch")
-			)
-			(signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
-			(signing-identifier "com.apple.shortcuts")
+			(%entitlement-is-bool-true "com.apple.developer.video-subscription-registration")
+			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.all-sources.read-only")
+			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.internal")
+			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.web-sources.read-write")
+			(%entitlement-is-bool-true "com.apple.smoot.subscriptionservice")
 		)
 	)
 )

 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.coreidvd.digital-presentment.xpc")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.browserkitd")
+		(%entitlement-is-present "com.apple.developer.web-browser")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.seserviced.credential.manager")
+		(%entitlement-is-present "com.apple.developer.secure-element-credential")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.FileCoordination")
+		(signing-identifier "com.apple.Music")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.uikit.viewservice.*")
+		(require-any
+			(global-name "com.apple.cloudd.debug")
+			(global-name "com.apple.cloudkit.partlycloudd.debug")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.lsd.xpc")
+		(signing-identifier "com.apple.mobilesafari")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(process-attribute is-apple-signed-executable)

 		)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.iokit.powerdxpc")
-		(signing-identifier "com.apple.shortcuts")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.enterprise.licensing")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.developer.arkit.barcode-detection.allow")
-			(%entitlement-is-bool-true "com.apple.developer.arkit.camera-region.allow")
-			(%entitlement-is-bool-true "com.apple.developer.arkit.main-camera-access.allow")
-			(%entitlement-is-bool-true "com.apple.developer.arkit.object-tracking-parameter-adjustment.allow")
-			(%entitlement-is-bool-true "com.apple.developer.arkit.shared-coordinate-space.allow")
-			(%entitlement-is-bool-true "com.apple.developer.avfoundation.uvc-device-access")
-			(%entitlement-is-bool-true "com.apple.developer.coreml.neural-engine-access")
-			(%entitlement-is-bool-true "com.apple.developer.protected-content")
-			(%entitlement-is-bool-true "com.apple.developer.screen-capture.include-passthrough")
-			(%entitlement-is-bool-true "com.apple.developer.window-body-follow")
-			(%entitlement-is-present "com.apple.developer.app-compute-category")
-		)
-	)
-)
-(allow mach-lookup
-	(require-all
-		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
-		(require-any
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
-		)
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.PowerManagement.control")
-		(signing-identifier "com.apple.shortcuts")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(xpc-service-name "com.apple.StreamingUnzipService")
-		(require-any
-			(signing-identifier "com.apple.Home")
-			(signing-identifier "com.apple.Home.HomeControlService")
-		)
-	)
-)
-(allow mach-lookup
-	(require-all
-		(signing-identifier "com.apple.Maps")
-		(require-any
-			(global-name "com.apple.PowerManagement.control")
-			(global-name "com.apple.assistant.analytics")
-			(global-name "com.apple.iokit.powerdxpc")
-			(global-name "com.apple.nanomaps.xpc.GeoServices.Navigation")
-			(global-name "com.apple.nanomaps.xpc.Navigation")
-			(global-name "com.apple.powerlog.plxpclogger.xpc")
-		)
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.idsremoteurlconnectionagent.embedded.auth")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.mobilestoredemod")
-		(%entitlement-is-present "com.apple.private.mobilestoredemo.enabledemo")
+		(global-name "com.apple.nanoprefsync")
+		(signing-identifier "com.apple.Music")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.FileCoordination")
-		(signing-identifier "com.apple.Music")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.messages.critical-messaging")
-		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.uikit.viewservice.*")
+		(xpc-service-name "com.apple.StreamingUnzipService")
 		(require-any
-			(global-name "com.apple.cloudd.debug")
-			(global-name "com.apple.cloudkit.partlycloudd.debug")
+			(signing-identifier "com.apple.Home")
+			(signing-identifier "com.apple.Home.HomeControlService")
 		)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.icfcallserver")
-		(%entitlement-is-bool-true "com.apple.private.icfcallserver")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.coreidvd.digital-presentment.xpc")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.cache_delete")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.mobile.deleted.AllowFreeSpace")
-			(%entitlement-is-present "com.apple.private.CacheDelete")
-		)
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.managedconfiguration.profiled")
-		(%entitlement-is-bool-true "com.apple.managedconfiguration.profiled-access")
-	)
-)
 (allow mach-lookup
 	(require-all
 		(signing-identifier "com.apple.mobilemail")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.safarifetcherd")
-		(signing-identifier "com.apple.mobilesafari")
+		(local-name "com.apple.iphone.axserver")
+		(%entitlement-is-bool-true "com.apple.accessibility.api")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.icfcallserver")
+		(%entitlement-is-bool-true "com.apple.private.icfcallserver")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.cache_delete")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.mobile.deleted.AllowFreeSpace")
+			(%entitlement-is-present "com.apple.private.CacheDelete")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(signing-identifier "com.apple.Maps")
+		(require-any
+			(global-name "com.apple.PowerManagement.control")
+			(global-name "com.apple.assistant.analytics")
+			(global-name "com.apple.iokit.powerdxpc")
+			(global-name "com.apple.nanomaps.xpc.GeoServices.Navigation")
+			(global-name "com.apple.nanomaps.xpc.Navigation")
+			(global-name "com.apple.powerlog.plxpclogger.xpc")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.managedconfiguration.profiled")
+		(%entitlement-is-bool-true "com.apple.managedconfiguration.profiled-access")
+	)
+)
+(allow mach-lookup
+	(require-all
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
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.identityservicesd.embedded.auth")
+		(require-any
+			(require-any
+				(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+				(signing-identifier "com.apple.shortcuts.watch")
+			)
+			(signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
+			(signing-identifier "com.apple.shortcuts")
+		)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.lsd.xpc")
-		(signing-identifier "com.apple.mobilesafari")
+		(global-name "com.apple.enterprise.licensing")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.developer.arkit.barcode-detection.allow")
+			(%entitlement-is-bool-true "com.apple.developer.arkit.camera-region.allow")
+			(%entitlement-is-bool-true "com.apple.developer.arkit.main-camera-access.allow")
+			(%entitlement-is-bool-true "com.apple.developer.arkit.object-tracking-parameter-adjustment.allow")
+			(%entitlement-is-bool-true "com.apple.developer.arkit.shared-coordinate-space.allow")
+			(%entitlement-is-bool-true "com.apple.developer.avfoundation.uvc-device-access")
+			(%entitlement-is-bool-true "com.apple.developer.coreml.neural-engine-access")
+			(%entitlement-is-bool-true "com.apple.developer.protected-content")
+			(%entitlement-is-bool-true "com.apple.developer.screen-capture.include-passthrough")
+			(%entitlement-is-bool-true "com.apple.developer.window-body-follow")
+			(%entitlement-is-present "com.apple.developer.app-compute-category")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(local-name "com.apple.iphone.axserver")
-		(%entitlement-is-bool-true "com.apple.accessibility.api")
+		(global-name "com.apple.ak.anisette.xpc")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.authkit.client")
+			(%entitlement-is-bool-true "com.apple.authkit.client.internal")
+			(%entitlement-is-bool-true "com.apple.authkit.client.private")
+			(process-attribute is-apple-signed-executable)
+		)
 	)
 )
 (allow mach-lookup

 		)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.VideoSubscriberAccount.videosubscriptionsd")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.developer.video-subscription-registration")
-			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.all-sources.read-only")
-			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.internal")
-			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.web-sources.read-write")
-			(%entitlement-is-bool-true "com.apple.smoot.subscriptionservice")
-		)
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.nanoprefsync")

 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.messages.critical-messaging")
+		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.familycircle.agent")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.nanoprefsync")
-		(signing-identifier "com.apple.Music")
+		(global-name "com.apple.merchantd.storage")
+		(%entitlement-is-present "com.apple.developer.proximity-reader.payment.acceptance")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.seserviced.credential.manager")
-		(%entitlement-is-present "com.apple.developer.secure-element-credential")
+		(global-name "com.apple.safarifetcherd")
+		(signing-identifier "com.apple.mobilesafari")
 	)
 )
 (allow mach-lookup

 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.assessmentagent")
+		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.personad.xpc")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.powerlog.plxpclogger.xpc")
+		(global-name "com.apple.iokit.powerdxpc")
 		(signing-identifier "com.apple.shortcuts")
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.merchantd.storage")
-		(%entitlement-is-present "com.apple.developer.proximity-reader.payment.acceptance")
+		(global-name "com.apple.mobilestoredemod")
+		(%entitlement-is-present "com.apple.private.mobilestoredemo.enabledemo")
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
