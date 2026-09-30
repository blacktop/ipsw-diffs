## container

> Group: ⬆️ Updated

```diff

 
 (allow iokit-open-user-client
 	(require-all
-		(iokit-registry-entry-class "AppleMobileFileIntegrityUserClient")
-		(%entitlement-is-bool-true "com.apple.private.amfi.can-load-cdhash")
+		(iokit-registry-entry-class "ANEClientHintsUserClient")
+		(%entitlement-is-bool-true "com.apple.private.ane.allow-set-client-hints")
 	)
 )
 (allow iokit-open-user-client
 	(require-all
-		(iokit-registry-entry-class "ANEClientHintsUserClient")
-		(%entitlement-is-bool-true "com.apple.private.ane.allow-set-client-hints")
+		(iokit-registry-entry-class "RootDomainUserClient")
+		(require-any
+			(require-any
+				(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+				(signing-identifier "com.apple.shortcuts.watch")
+			)
+			(signing-identifier "com.apple.Bridge")
+			(signing-identifier "com.apple.Maps")
+			(signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
+			(signing-identifier "com.apple.mobilemail")
+			(signing-identifier "com.apple.shortcuts")
+		)
 	)
 )
 (allow iokit-open-user-client

 		)
 	)
 )
+(allow iokit-open-user-client
+	(require-all
+		(iokit-registry-entry-class "AppleMobileFileIntegrityUserClient")
+		(%entitlement-is-bool-true "com.apple.private.amfi.can-load-cdhash")
+	)
+)
 (allow iokit-open-user-client
 	(require-all
 		(iokit-registry-entry-class "AppleSPUHIDDeviceUserClient")

 )
 (allow iokit-open-user-client
 	(require-all
-		(process-attribute is-apple-signed-executable)
-		(iokit-registry-entry-class "IOHIDLibUserClient")
+		(extension "com.apple.tcc.kTCCServiceMotionSensors")
+		(iokit-registry-entry-class "IOHIDEventServiceFastPathUserClient")
 	)
 )
 (allow iokit-open-user-client
 	(require-all
-		(iokit-registry-entry-class "RootDomainUserClient")
-		(require-any
-			(require-any
-				(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
-				(signing-identifier "com.apple.shortcuts.watch")
-			)
-			(signing-identifier "com.apple.Bridge")
-			(signing-identifier "com.apple.Maps")
-			(signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
-			(signing-identifier "com.apple.mobilemail")
-			(signing-identifier "com.apple.shortcuts")
-		)
+		(process-attribute is-apple-signed-executable)
+		(iokit-registry-entry-class "IOHIDLibUserClient")
 	)
 )
 (allow iokit-open-user-client

 		(iokit-registry-entry-class "IOAccelSharedUserClient2")
 		(iokit-registry-entry-class "IOAccelSubmitter2")
 		(iokit-registry-entry-class "IOGPUDeviceUserClient")
-		(iokit-registry-entry-class "IOHIDEventServiceFastPathUserClient")
 		(iokit-registry-entry-class "IOMobileFramebufferUserClient")
 		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(iokit-registry-entry-class "IOSurfaceRootUserClient")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.merchantd.engagement")
-		(%entitlement-is-present "com.apple.developer.proximity-reader.customer-engagement")
+		(signing-identifier "com.apple.Maps")
+		(require-any
+			(global-name "com.apple.PowerManagement.control")
+			(global-name "com.apple.assistant.analytics")
+			(global-name "com.apple.iokit.powerdxpc")
+			(global-name "com.apple.nanomaps.xpc.GeoServices.Navigation")
+			(global-name "com.apple.nanomaps.xpc.Navigation")
+			(global-name "com.apple.powerlog.plxpclogger.xpc")
+		)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.coreidvd.mobile-document-provider-registration.xpc")
-		(%entitlement-is-present "com.apple.developer.identity-document-services.document-provider.mobile-document-types")
+		(global-name "com.apple.sigmond")
+		(process-attribute is-apple-signed-executable)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.browserkitd")
-		(%entitlement-is-present "com.apple.developer.web-browser")
+		(global-name "com.apple.iokit.powerdxpc")
+		(require-any
+			(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+			(signing-identifier "com.apple.shortcuts.watch")
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
+		(global-name "com.apple.cache_delete")
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
+			(%entitlement-is-bool-true "com.apple.mobile.deleted.AllowFreeSpace")
+			(%entitlement-is-present "com.apple.private.CacheDelete")
 		)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.sigmond")
-		(process-attribute is-apple-signed-executable)
+		(global-name "com.apple.weatherkit.authservice")
+		(%entitlement-is-present "com.apple.developer.weatherkit")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.mobile.usermanagerd.xpc")
-		(process-attribute is-apple-signed-executable)
+		(global-name "com.apple.merchantd.engagement")
+		(%entitlement-is-present "com.apple.developer.proximity-reader.customer-engagement")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.PowerManagement.control")
+		(%entitlement-is-bool-true "com.apple.developer.networking.multicast")
 		(require-any
-			(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
-			(signing-identifier "com.apple.shortcuts.watch")
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
-		(global-name "com.apple.iokit.powerdxpc")
-		(require-any
-			(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
-			(signing-identifier "com.apple.shortcuts.watch")
-		)
+		(global-name "com.apple.seserviced.credential.manager")
+		(%entitlement-is-present "com.apple.developer.secure-element-credential")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.replayd")
+		(process-attribute is-plugin)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.merchantd.transaction")
+		(global-name "com.apple.financed.service.coredatastore")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.developer.proximity-reader.payment.acceptance")
-			(%entitlement-is-bool-true "com.apple.developer.proximity-reader.payment.acceptance-development")
+			(%entitlement-is-present "com.apple.developer.financekit")
+			(%entitlement-is-present "com.apple.finance.private")
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
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.odi.assessmentService")
-		(%entitlement-is-present "com.apple.developer.trustinsights.base")
+		(global-name "com.apple.StreamReceiverDisplay.sessions")
+		(%entitlement-is-bool-true "com.apple.developer.foveated-streaming-session")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(xpc-service-name "com.apple.StreamingUnzipService")
+		(global-name "com.apple.merchantd.transaction")
 		(require-any
-			(signing-identifier "com.apple.Home")
-			(signing-identifier "com.apple.Home.HomeControlService")
+			(%entitlement-is-bool-true "com.apple.developer.proximity-reader.payment.acceptance")
+			(%entitlement-is-bool-true "com.apple.developer.proximity-reader.payment.acceptance-development")
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.bulletinboard.observerconnection")
-		(%entitlement-is-bool-true "com.apple.bulletinboard.observer")
+		(global-name "com.apple.FileCoordination")
+		(signing-identifier "com.apple.Music")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.weatherkit.authservice")
-		(%entitlement-is-present "com.apple.developer.weatherkit")
+		(require-any
+			(global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.VerificationCodes")
+			(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
+		)
+		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
 	)
 )
 (allow mach-lookup

 		(%entitlement-is-bool-true "com.apple.managedconfiguration.profiled-access")
 	)
 )
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
-		(global-name "com.apple.lsd.xpc")
-		(signing-identifier "com.apple.mobilesafari")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.bulletinboard.systemstateconnection")
-		(%entitlement-is-bool-true "com.apple.bulletinboard.systemstate")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.replayd")
-		(process-attribute is-plugin)
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.arkit.service.focusRegion")
-		(%entitlement-is-bool-true "com.apple.developer.foveated-streaming-provider")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.coreidvd.digital-presentment.xpc")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
-		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.StreamReceiverDisplay.sessions")
-		(%entitlement-is-bool-true "com.apple.developer.foveated-streaming-session")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.coreduetd")
-		(process-attribute is-apple-signed-executable)
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.mobile.keybagd.xpc")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-			(signing-identifier "com.apple.WebContentFilter.remoteUI.WebContentAnalysisUI")
-		)
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.powerlog.plxpclogger.xpc")

 )
 (allow mach-lookup
 	(require-all
-		(signing-identifier "com.apple.mobilemail")
+		(global-name "com.apple.developer.wifi-infrastructure.WiFiNetworkSharingApp")
+		(%entitlement-is-present "com.apple.developer.wifi-infrastructure")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.PowerManagement.control")
 		(require-any
-			(global-name "com.apple.backupd")
-			(global-name "com.apple.bulletindistributord.server")
-			(global-name "com.apple.harvestd.manager")
-			(global-name "com.apple.identityservicesd.embedded.auth")
-			(global-name "com.apple.mobilemail")
-			(global-name "com.apple.nanoprefsync")
-			(global-name "com.apple.routined.registration")
-			(global-name "com.apple.sharingd.nsxpc")
+			(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+			(signing-identifier "com.apple.shortcuts.watch")
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.familycircle.agent")
-		(%entitlement-is-bool-true "com.apple.private.familycircle")
+		(global-name "com.apple.telephonyutilities.callservicesdaemon.ptt")
+		(%entitlement-is-bool-true "com.apple.developer.push-to-talk")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.nanoprefsync")
-		(signing-identifier "com.apple.Music")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.SafetyKit")
-		(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
+		(global-name "com.apple.arkit.service.focusRegion")
+		(%entitlement-is-bool-true "com.apple.developer.foveated-streaming-provider")
 	)
 )
 (allow mach-lookup

 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.lsd.xpc")
+		(signing-identifier "com.apple.mobilesafari")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.AOSNotification")
 		(%entitlement-is-bool-true "com.apple.aosnotification.aosnotifyd-access")
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.mobile.keybagd.xpc")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+			(signing-identifier "com.apple.WebContentFilter.remoteUI.WebContentAnalysisUI")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(xpc-service-name "com.apple.StreamingUnzipService")
+		(require-any
+			(signing-identifier "com.apple.Home")
+			(signing-identifier "com.apple.Home.HomeControlService")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.FileCoordination")
+		(require-any
+			(require-any
+				(signing-identifier "com.apple.Health")
+				(signing-identifier "com.apple.PassbookUIService")
+			)
+			(signing-identifier "com.apple.iBooks")
+			(signing-identifier "com.apple.stocks.watchkitextension")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.familycircle.agent")
+		(%entitlement-is-bool-true "com.apple.private.familycircle")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.identityservicesd.embedded.auth")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+			(signing-identifier "com.apple.Bridge")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.SafetyKit")
+		(%entitlement-is-present "com.apple.developer.severe-vehicular-crash-event")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.bulletinboard.systemstateconnection")
+		(%entitlement-is-bool-true "com.apple.bulletinboard.systemstate")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(global-name "com.apple.osanalytics.osanalyticshelper")
+			(require-any
+				(global-name "com.apple.ReportCrash")
+				(global-name "com.apple.ReportCrash.DirectoryService")
+				(global-name "com.apple.ReportCrash.SafetyNet")
+				(global-name "com.apple.ReportCrash.StackShot")
+			)
+		)
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.merchantd.identity")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.telephonyutilities.callservicesdaemon.ptt")
-		(%entitlement-is-bool-true "com.apple.developer.push-to-talk")
+		(global-name "com.apple.nanoprefsync")
+		(signing-identifier "com.apple.Music")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.seserviced.credential.manager")
-		(%entitlement-is-present "com.apple.developer.secure-element-credential")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.FileCoordination")
-		(signing-identifier "com.apple.Music")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.financed.service.coredatastore")
+		(global-name "com.apple.MusicKit.UI")
 		(require-any
-			(%entitlement-is-present "com.apple.developer.financekit")
-			(%entitlement-is-present "com.apple.finance.private")
+			(%entitlement-is-bool-true "com.apple.storekit.cloud-service-exempted-from-tcc-access")
+			(extension "com.apple.tcc.kTCCServiceMediaLibrary")
 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.mobile.usermanagerd.xpc")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.safarifetcherd")
+		(signing-identifier "com.apple.mobilesafari")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.assessmentagent")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ThreadNetwork.xpc")
-		(%entitlement-is-bool-true "com.apple.developer.networking.manage-thread-network-credentials")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.developer.wifi-infrastructure.WiFiNetworkSharingApp")
-		(%entitlement-is-present "com.apple.developer.wifi-infrastructure")
+		(global-name "com.apple.coreidvd.digital-presentment.xpc")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment")
+		(%entitlement-is-present "com.apple.developer.in-app-identity-presentment.merchant-identifiers")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(require-any
-			(global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.VerificationCodes")
-			(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
-		)
-		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
+		(global-name "com.apple.coreidvd.mobile-document-provider-registration.xpc")
+		(%entitlement-is-present "com.apple.developer.identity-document-services.document-provider.mobile-document-types")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.MusicKit.UI")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.storekit.cloud-service-exempted-from-tcc-access")
-			(extension "com.apple.tcc.kTCCServiceMediaLibrary")
-		)
+		(global-name "com.apple.coreduetd")
+		(process-attribute is-apple-signed-executable)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(process-attribute is-apple-signed-executable)
-		(require-any
-			(global-name "com.apple.osanalytics.osanalyticshelper")
-			(require-any
-				(global-name "com.apple.ReportCrash")
-				(global-name "com.apple.ReportCrash.DirectoryService")
-				(global-name "com.apple.ReportCrash.SafetyNet")
-				(global-name "com.apple.ReportCrash.StackShot")
-			)
-		)
+		(global-name "com.apple.browserkitd")
+		(%entitlement-is-present "com.apple.developer.web-browser")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.identityservicesd.embedded.auth")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-			(signing-identifier "com.apple.Bridge")
-		)
+		(global-name "com.apple.bulletinboard.observerconnection")
+		(%entitlement-is-bool-true "com.apple.bulletinboard.observer")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.safarifetcherd")
-		(signing-identifier "com.apple.mobilesafari")
+		(global-name "com.apple.odi.assessmentService")
+		(%entitlement-is-present "com.apple.developer.trustinsights.base")
 	)
 )
 (allow mach-lookup

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
-		(global-name "com.apple.SystemConfiguration.PPPController-priv")
-		(%entitlement-is-present "com.apple.networking.vpn.configuration")
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

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.FileCoordination")
-		(require-any
-			(require-any
-				(signing-identifier "com.apple.Health")
-				(signing-identifier "com.apple.PassbookUIService")
-			)
-			(signing-identifier "com.apple.iBooks")
-			(signing-identifier "com.apple.stocks.watchkitextension")
-		)
+		(global-name "com.apple.SystemConfiguration.PPPController-priv")
+		(%entitlement-is-present "com.apple.networking.vpn.configuration")
 	)
 )
 (allow mach-lookup

 		(global-name "com.apple.TextInput.preferences")
 		(global-name "com.apple.TextInput.rdt")
 		(global-name "com.apple.TextInput.shortcuts")
+		(global-name "com.apple.ThreadNetwork.xpc")
 		(global-name "com.apple.UIKit.KeyboardManagement.hosted")
 		(global-name "com.apple.UIKit.OverlayUI.services")
 		(global-name "com.apple.UIKit.SecureControlService")

 		(global-name "com.apple.ap.adprivacyd.attribution")
 		(global-name "com.apple.ap.adprivacyd.trackingtransparency")
 		(global-name "com.apple.ap.promotedcontent.attributionservice")
+		(global-name "com.apple.appledepthd")
 		(global-name "com.apple.appleneuralengine")
 		(global-name "com.apple.appleprofilepolicyd")
 		(global-name "com.apple.appprotectiond.extensioninfo")

 		(preference-domain "com.apple.mobile.SyncMigrator")
 		(preference-domain "com.apple.mobileipod")
 		(preference-domain "com.apple.mobileme.fmf.assistant")
-		(preference-domain "com.apple.mobileslideshow")
 		(preference-domain "com.apple.mobilestoresettings")
 		(preference-domain "com.apple.mobiletimer")
 		(preference-domain "com.apple.mobilevpn")

 		(preference-domain "com.apple.mobile.SyncMigrator")
 		(preference-domain "com.apple.mobileipod")
 		(preference-domain "com.apple.mobileme.fmf.assistant")
-		(preference-domain "com.apple.mobileslideshow")
 		(preference-domain "com.apple.mobilestoresettings")
 		(preference-domain "com.apple.mobiletimer")
 		(preference-domain "com.apple.mobilevpn")
```
