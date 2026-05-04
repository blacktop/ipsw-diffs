## Sandbox Profiles

### Collection

#### Changed (10)

##### MobileSlideShow

```diff

 					)
 				)
 			)
+			(require-all
+				(global-name "com.apple.ThreadNetwork.xpc")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
+					(xpc-service-name "com.apple.ImageIOXPCService")
+				)
+			)
 			(require-all
 				(global-name "com.apple.ak.anisette.xpc")
 				(process-attribute is-apple-signed-executable)

 				(global-name "com.apple.SpatialAudioProfileXPCService")
 				(global-name "com.apple.StoreKitUISceneService")
 				(global-name "com.apple.TelephonyTransferService")
-				(global-name "com.apple.ThreadNetwork.xpc")
 				(global-name "com.apple.UIKit.OverlayUI.services")
 				(global-name "com.apple.UIKit.SecureControlService")
 				(global-name "com.apple.USDKit.FormatLoader")

 					)
 				)
 			)
+			(require-all
+				(global-name "com.apple.ThreadNetwork.xpc")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
+					(xpc-service-name "com.apple.ImageIOXPCService")
+				)
+			)
 			(require-all
 				(global-name "com.apple.ak.anisette.xpc")
 				(process-attribute is-apple-signed-executable)

 				(global-name "com.apple.SpatialAudioProfileXPCService")
 				(global-name "com.apple.StoreKitUISceneService")
 				(global-name "com.apple.TelephonyTransferService")
-				(global-name "com.apple.ThreadNetwork.xpc")
 				(global-name "com.apple.UIKit.OverlayUI.services")
 				(global-name "com.apple.UIKit.SecureControlService")
 				(global-name "com.apple.USDKit.FormatLoader")

 					)
 				)
 			)
+			(require-all
+				(global-name "com.apple.ThreadNetwork.xpc")
+				(require-any
+					(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
+					(xpc-service-name "com.apple.ImageIOXPCService")
+				)
+			)
 			(require-all
 				(global-name "com.apple.ak.anisette.xpc")
 				(process-attribute is-apple-signed-executable)

 				(global-name "com.apple.SpatialAudioProfileXPCService")
 				(global-name "com.apple.StoreKitUISceneService")
 				(global-name "com.apple.TelephonyTransferService")
-				(global-name "com.apple.ThreadNetwork.xpc")
 				(global-name "com.apple.UIKit.OverlayUI.services")
 				(global-name "com.apple.UIKit.SecureControlService")
 				(global-name "com.apple.USDKit.FormatLoader")
```

##### app-extension-enhanced-security

```diff

 
 (allow mach-lookup
 	(require-any
-		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
```

##### apple-cloud-enhanced-security

```diff

 	(require-any
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")
-		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.cloudos.cb_bridged")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.logd.events")

 (deny mach-lookup
 	(require-any
 		(global-name "com.apple.CARenderServer")
+		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.audio.AudioComponentRegistrar")
 		(global-name "com.apple.coremedia.mediaparserd.utilities")
 		(global-name "com.apple.mobileassetd.v2")
```

##### blastdoor-airlock

```diff

 
 (allow mach-lookup
 	(require-any
-		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
```

##### blastdoor-ids

```diff

 	)
 )
 
-(allow mach-derive-port
-	(global-name "com.apple.analyticsd")
-)
-
 (allow mach-lookup
 	(require-any
-		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
```

##### blastdoor-messages

```diff

 
 (allow mach-lookup
 	(require-any
-		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
```

##### blastdoor-thumbnails

```diff

 
 (allow mach-lookup
 	(require-any
-		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)
```

##### container

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
 (allow mach-lookup
 	(require-all
-		(process-attribute is-apple-signed-executable)
-		(require-any
-			(global-name "com.apple.SharedWebCredentials")
-			(global-name "com.apple.dataaccess.dataaccessd")
-			(global-name "com.apple.exchangesyncd")
-			(xpc-service-name "com.apple.LORemoteUIPinService")
-			(xpc-service-name "com.apple.ctcategories.service")
-		)
+		(global-name "com.apple.coreidvd.digital-presentment.xpc")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.iokit.powerdxpc")
-		(signing-identifier "com.apple.shortcuts")
+		(global-name "com.apple.browserkitd")
+		(%entitlement-is-present "com.apple.developer.web-browser")
 	)
 )
 (allow mach-lookup
 	(require-all
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
+		(global-name "com.apple.seserviced.credential.manager")
+		(%entitlement-is-present "com.apple.developer.secure-element-credential")
 	)
 )
 (allow mach-lookup
 	(require-all
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
+		(global-name "com.apple.FileCoordination")
+		(signing-identifier "com.apple.Music")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.PowerManagement.control")
-		(signing-identifier "com.apple.shortcuts")
+		(global-name "com.apple.uikit.viewservice.*")
+		(require-any
+			(global-name "com.apple.cloudkit.partlycloudd")
+			(global-name #"^com[.]apple[.]uikit[.]viewservice[.].+")
+			(require-any
+				(global-name "com.apple.cloudd.debug")
+				(global-name "com.apple.cloudkit.partlycloudd.debug")
+			)
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(xpc-service-name "com.apple.StreamingUnzipService")
-		(require-any
-			(signing-identifier "com.apple.Home")
-			(signing-identifier "com.apple.Home.HomeControlService")
-		)
+		(global-name "com.apple.lsd.xpc")
+		(signing-identifier "com.apple.mobilesafari")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(signing-identifier "com.apple.Maps")
+		(process-attribute is-apple-signed-executable)
 		(require-any
-			(global-name "com.apple.PowerManagement.control")
-			(global-name "com.apple.assistant.analytics")
-			(global-name "com.apple.iokit.powerdxpc")
-			(global-name "com.apple.nanomaps.xpc.GeoServices.Navigation")
-			(global-name "com.apple.nanomaps.xpc.Navigation")
-			(global-name "com.apple.powerlog.plxpclogger.xpc")
+			(global-name "com.apple.SharedWebCredentials")
+			(global-name "com.apple.dataaccess.dataaccessd")
+			(global-name "com.apple.exchangesyncd")
+			(xpc-service-name "com.apple.LORemoteUIPinService")
+			(xpc-service-name "com.apple.ctcategories.service")
 		)
 	)
 )

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
+		(xpc-service-name "com.apple.StreamingUnzipService")
+		(require-any
+			(signing-identifier "com.apple.Home")
+			(signing-identifier "com.apple.Home.HomeControlService")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.messages.critical-messaging")
-		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
+		(signing-identifier "com.apple.mobilemail")
+		(require-any
+			(global-name "com.apple.backupd")
+			(global-name "com.apple.bulletindistributord.server")
+			(global-name "com.apple.harvestd.manager")
+			(global-name "com.apple.identityservicesd.embedded.auth")
+			(global-name "com.apple.mobilemail")
+			(global-name "com.apple.nanoprefsync")
+			(global-name "com.apple.routined.registration")
+			(global-name "com.apple.sharingd.nsxpc")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.uikit.viewservice.*")
-		(require-any
-			(global-name "com.apple.cloudkit.partlycloudd")
-			(global-name #"^com[.]apple[.]uikit[.]viewservice[.].+")
-			(require-any
-				(global-name "com.apple.cloudd.debug")
-				(global-name "com.apple.cloudkit.partlycloudd.debug")
-			)
-		)
+		(local-name "com.apple.iphone.axserver")
+		(%entitlement-is-bool-true "com.apple.accessibility.api")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.coreidvd.digital-presentment.xpc")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
+		(global-name "com.apple.cache_delete")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.mobile.deleted.AllowFreeSpace")
+			(%entitlement-is-present "com.apple.private.CacheDelete")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.cache_delete")
+		(signing-identifier "com.apple.Maps")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.mobile.deleted.AllowFreeSpace")
-			(%entitlement-is-present "com.apple.private.CacheDelete")
+			(global-name "com.apple.PowerManagement.control")
+			(global-name "com.apple.assistant.analytics")
+			(global-name "com.apple.iokit.powerdxpc")
+			(global-name "com.apple.nanomaps.xpc.GeoServices.Navigation")
+			(global-name "com.apple.nanomaps.xpc.Navigation")
+			(global-name "com.apple.powerlog.plxpclogger.xpc")
 		)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(signing-identifier "com.apple.mobilemail")
+		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
 		(require-any
-			(global-name "com.apple.backupd")
-			(global-name "com.apple.bulletindistributord.server")
-			(global-name "com.apple.harvestd.manager")
-			(global-name "com.apple.identityservicesd.embedded.auth")
-			(global-name "com.apple.mobilemail")
-			(global-name "com.apple.nanoprefsync")
-			(global-name "com.apple.routined.registration")
-			(global-name "com.apple.sharingd.nsxpc")
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
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.safarifetcherd")
-		(signing-identifier "com.apple.mobilesafari")
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
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.VideoSubscriberAccount.videosubscriptionsd")
+		(global-name "com.apple.nanoprefsync")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.developer.video-subscription-registration")
-			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.all-sources.read-only")
-			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.internal")
-			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.web-sources.read-write")
-			(%entitlement-is-bool-true "com.apple.smoot.subscriptionservice")
+			(signing-identifier "com.apple.Health")
+			(signing-identifier "com.apple.PassbookUIService")
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.nanoprefsync")
-		(require-any
-			(signing-identifier "com.apple.Health")
-			(signing-identifier "com.apple.PassbookUIService")
-		)
+		(global-name "com.apple.messages.critical-messaging")
+		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.nanoprefsync")
-		(signing-identifier "com.apple.Music")
+		(global-name "com.apple.merchantd.storage")
+		(require-any
+			(%entitlement-is-present "com.apple.developer.proximity-reader.payment.acceptance")
+			(require-all
+				(process-attribute is-apple-signed-executable)
+				(global-name "com.apple.dataaccess.dataaccessd")
+			)
+		)
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
-		(require-any
-			(%entitlement-is-present "com.apple.developer.proximity-reader.payment.acceptance")
-			(require-all
-				(process-attribute is-apple-signed-executable)
-				(global-name "com.apple.dataaccess.dataaccessd")
-			)
-		)
+		(global-name "com.apple.mobilestoredemod")
+		(%entitlement-is-present "com.apple.private.mobilestoredemo.enabledemo")
 	)
 )
 (allow mach-lookup

 			(global-name "com.apple.SpatialAudioProfileXPCService")
 			(global-name "com.apple.StoreKitUISceneService")
 			(global-name "com.apple.TelephonyTransferService")
-			(global-name "com.apple.ThreadNetwork.xpc")
 			(global-name "com.apple.UIKit.OverlayUI.services")
 			(global-name "com.apple.UIKit.SecureControlService")
 			(global-name "com.apple.USDKit.FormatLoader")
```

##### maild

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

 		)
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

 			(global-name "com.apple.SpatialAudioProfileXPCService")
 			(global-name "com.apple.StoreKitUISceneService")
 			(global-name "com.apple.TelephonyTransferService")
-			(global-name "com.apple.ThreadNetwork.xpc")
 			(global-name "com.apple.UIKit.OverlayUI.services")
 			(global-name "com.apple.UIKit.SecureControlService")
 			(global-name "com.apple.USDKit.FormatLoader")
```

##### quicklookd

```diff

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.messages.critical-messaging")
-		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
+		(global-name "com.apple.assessmentagent")
+		(%entitlement-is-present "com.apple.developer.automatic-assessment-configuration")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
-		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
+		(global-name "com.apple.seserviced.session")
+		(%entitlement-is-present "com.apple.developer.carkey.session")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.MomentsUIService")
-		(%entitlement-is-present "com.apple.developer.journal.allow")
+		(global-name "com.apple.messages.critical-messaging")
+		(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ExposureNotification")
-		(%entitlement-is-present "com.apple.developer.exposure-notification")
+		(global-name "com.apple.coreidvd.digital-presentment.xpc")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
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
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.SafetyKit")
+		(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.seserviced.session")
-		(%entitlement-is-present "com.apple.developer.carkey.session")
+		(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
+		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.SafetyKit")
-		(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
+		(global-name "com.apple.ExposureNotification")
+		(%entitlement-is-present "com.apple.developer.exposure-notification")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.coreidvd.digital-presentment.xpc")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
+		(global-name "com.apple.MomentsUIService")
+		(%entitlement-is-present "com.apple.developer.journal.allow")
 	)
 )
 (allow mach-lookup

 			(global-name "com.apple.SpatialAudioProfileXPCService")
 			(global-name "com.apple.StoreKitUISceneService")
 			(global-name "com.apple.TelephonyTransferService")
-			(global-name "com.apple.ThreadNetwork.xpc")
 			(global-name "com.apple.UIKit.OverlayUI.services")
 			(global-name "com.apple.UIKit.SecureControlService")
 			(global-name "com.apple.USDKit.FormatLoader")
```
