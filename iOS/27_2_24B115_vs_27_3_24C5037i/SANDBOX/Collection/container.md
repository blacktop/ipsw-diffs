## container

> Group: ⬆️ Updated

```diff

 (version 1)
 (%extends-builtin "baseline")
+(accept-profile-extension)
 (enable-profile-flag "common-rules")
 (enable-profile-flag "common-syscall-rules")
 (enable-profile-flag "common-apple-internal-rules")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.merchantd.engagement")
-		(%entitlement-is-present "com.apple.developer.proximity-reader.customer-engagement")
+		(global-name "com.apple.AOSNotification")
+		(%entitlement-is-bool-true "com.apple.aosnotification.aosnotifyd-access")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.coreidvd.mobile-document-provider-registration.xpc")
-		(%entitlement-is-present "com.apple.developer.identity-document-services.document-provider.mobile-document-types")
+		(global-name "com.apple.MusicKit.UI")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.storekit.cloud-service-exempted-from-tcc-access")
+			(extension "com.apple.tcc.kTCCServiceMediaLibrary")
+		)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.browserkitd")
-		(%entitlement-is-present "com.apple.developer.web-browser")
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(global-name "com.apple.ReportCrash")
+			(global-name "com.apple.osanalytics.osanalyticshelper")
+			(require-any
+				(global-name "com.apple.ReportCrash.DirectoryService")
+				(global-name "com.apple.ReportCrash.SafetyNet")
+				(global-name "com.apple.ReportCrash.StackShot")
+			)
+		)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.idsremoteurlconnectionagent.embedded.auth")
+		(global-name "com.apple.identityservicesd.embedded.auth")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.private.ids.remoteurlconnection")
-			(%entitlement-is-bool-true "com.apple.private.imcore.imremoteurlconnection")
+			(require-any
+				(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+				(signing-identifier "com.apple.shortcuts.watch")
+			)
+			(signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
+			(signing-identifier "com.apple.shortcuts")
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.siri.vocabularyupdates")
+		(signing-identifier "com.apple.Maps")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.developer.siri")
-			(%entitlement-is-bool-true "com.apple.siri.synapse")
+			(global-name "com.apple.PowerManagement.control")
+			(global-name "com.apple.assistant.analytics")
+			(global-name "com.apple.iokit.powerdxpc")
+			(global-name "com.apple.nanomaps.xpc.GeoServices.Navigation")
+			(global-name "com.apple.nanomaps.xpc.Navigation")
+			(global-name "com.apple.powerlog.plxpclogger.xpc")
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.sigmond")
-		(process-attribute is-apple-signed-executable)
+		(global-name "com.apple.sirievaluationd")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+			(system-attribute developer-mode)
+		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.mobile.usermanagerd.xpc")
-		(process-attribute is-apple-signed-executable)
+		(global-name "com.apple.merchantd.storage")
+		(%entitlement-is-present "com.apple.developer.proximity-reader.payment.acceptance")
 	)
 )
 (allow mach-lookup

 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.financed.service.coredatastore")
+		(require-any
+			(%entitlement-is-present "com.apple.developer.financekit")
+			(%entitlement-is-present "com.apple.finance.private")
+		)
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
+		(require-any
+			(global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.VerificationCodes")
+			(global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent.CredentialExchange")
+		)
+		(%entitlement-is-present "com.apple.developer.authentication-services.autofill-credential-provider")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.nanoprefsync")
+		(signing-identifier "com.apple.iBooks")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.VideoSubscriberAccount.videosubscriptionsd")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.developer.video-subscription-registration")
+			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.all-sources.read-only")
+			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.internal")
+			(%entitlement-is-bool-true "com.apple.private.subscriptionservice.web-sources.read-write")
+			(%entitlement-is-bool-true "com.apple.smoot.subscriptionservice")
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
+		(global-name "com.apple.messages.critical-messaging")
+		(require-any
+			(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
+			(%entitlement-is-present "com.apple.developer.upi-device-validation")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.bulletinboard.utilitiesconnection")
+		(%entitlement-is-bool-true "com.apple.bulletinboard.utilities")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.nanoprefsync")
+		(signing-identifier "com.apple.Music")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.coreduetd")
+		(process-attribute is-apple-signed-executable)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.weatherkit.authservice")
+		(%entitlement-is-present "com.apple.developer.weatherkit")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.mobilestoredemod")
+		(%entitlement-is-present "com.apple.private.mobilestoredemo.enabledemo")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.merchantd.engagement")
+		(%entitlement-is-present "com.apple.developer.proximity-reader.customer-engagement")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.merchantd.transaction")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.developer.proximity-reader.payment.acceptance")
+			(%entitlement-is-bool-true "com.apple.developer.proximity-reader.payment.acceptance-development")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.bulletinboard.observerconnection")
+		(%entitlement-is-bool-true "com.apple.bulletinboard.observer")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.enterprise.licensing")

 		)
 	)
 )
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.siri.vocabularyupdates")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.developer.siri")
+			(%entitlement-is-bool-true "com.apple.siri.synapse")
+		)
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
+		(global-name "com.apple.safarifetcherd")
+		(signing-identifier "com.apple.mobilesafari")
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
+		(global-name "com.apple.icfcallserver")
+		(%entitlement-is-bool-true "com.apple.private.icfcallserver")
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.developer.wifi-infrastructure.WiFiNetworkSharingApp")
+		(%entitlement-is-present "com.apple.developer.wifi-infrastructure")
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.PowerManagement.control")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.nanoprefsync")
-		(signing-identifier "com.apple.iBooks")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.merchantd.transaction")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.developer.proximity-reader.payment.acceptance")
-			(%entitlement-is-bool-true "com.apple.developer.proximity-reader.payment.acceptance-development")
-		)
+		(global-name "com.apple.arkit.service.focusRegion")
+		(%entitlement-is-bool-true "com.apple.developer.foveated-streaming-provider")
 	)
 )
 (allow mach-lookup
 	(require-all
+		(global-name "com.apple.sigmond")
 		(process-attribute is-apple-signed-executable)
-		(require-any
-			(global-name "com.apple.SharedWebCredentials")
-			(global-name "com.apple.dataaccess.dataaccessd")
-			(global-name "com.apple.exchangesyncd")
-			(xpc-service-name "com.apple.LORemoteUIPinService")
-			(xpc-service-name "com.apple.ctcategories.service")
-		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.odi.assessmentService")
-		(%entitlement-is-present "com.apple.developer.trustinsights.base")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.bulletinboard.utilitiesconnection")
-		(%entitlement-is-bool-true "com.apple.bulletinboard.utilities")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(signing-identifier "com.apple.Bridge")
-		(require-any
-			(global-name "com.apple.PowerManagement.control")
-			(global-name "com.apple.iokit.powerdxpc")
-			(global-name "com.apple.powerlog.plxpclogger.xpc")
-		)
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.icloud.findmydeviced")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.aosnotification.aosnotifyd-access")
-			(%entitlement-is-bool-true "com.apple.icloud.findmydeviced.access")
-		)
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.merchantd.storage")
-		(%entitlement-is-present "com.apple.developer.proximity-reader.payment.acceptance")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.mobilestoredemod")
-		(%entitlement-is-present "com.apple.private.mobilestoredemo.enabledemo")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.callkit.networkextension.voip")
-		(%entitlement-is-present "com.apple.developer.networking.networkextension")
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
-		(global-name "com.apple.bulletinboard.observerconnection")
-		(%entitlement-is-bool-true "com.apple.bulletinboard.observer")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(local-name "com.apple.iphone.axserver")
-		(%entitlement-is-bool-true "com.apple.accessibility.api")
-	)
-)
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
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.icfcallserver")
-		(%entitlement-is-bool-true "com.apple.private.icfcallserver")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.messages.critical-messaging")
-		(require-any
-			(%entitlement-is-present "com.apple.developer.messages.critical-messaging")
-			(%entitlement-is-present "com.apple.developer.upi-device-validation")
-		)
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.managedconfiguration.profiled")
-		(%entitlement-is-bool-true "com.apple.managedconfiguration.profiled-access")
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.cache_delete")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.mobile.deleted.AllowFreeSpace")
-			(%entitlement-is-present "com.apple.private.CacheDelete")
-		)
+		(global-name "com.apple.StreamReceiverDisplay.sessions")
+		(%entitlement-is-bool-true "com.apple.developer.foveated-streaming-session")
 	)
 )
 (allow mach-lookup

 		(signing-identifier "com.apple.mobilesafari")
 	)
 )
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
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.coreidvd.digital-presentment.xpc")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.StreamReceiverDisplay.sessions")
-		(%entitlement-is-bool-true "com.apple.developer.foveated-streaming-session")
+		(global-name "com.apple.replayd")
+		(process-attribute is-plugin)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.coreduetd")
+		(global-name "com.apple.mobile.usermanagerd.xpc")
 		(process-attribute is-apple-signed-executable)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.mobile.keybagd.xpc")
-		(require-any
-			(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-			(signing-identifier "com.apple.WebContentFilter.remoteUI.WebContentAnalysisUI")
-		)
-	)
-)
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.powerlog.plxpclogger.xpc")
-		(require-any
-			(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
-			(signing-identifier "com.apple.shortcuts.watch")
-		)
-	)
-)
-(allow mach-lookup
-	(require-all
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
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.familycircle.agent")

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.nanoprefsync")
-		(signing-identifier "com.apple.Music")
+		(global-name "com.apple.identityservicesd.embedded.auth")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+			(signing-identifier "com.apple.Bridge")
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.internal.sirievaluationd")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+			(require-all
+				(system-attribute internal-build)
+				(system-attribute developer-mode)
+			)
+		)
+	)
+)
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.bulletinboard.systemstateconnection")
+		(%entitlement-is-bool-true "com.apple.bulletinboard.systemstate")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.identityservicesd.embedded.auth")
+		(global-name "com.apple.idsremoteurlconnectionagent.embedded.auth")
 		(require-any
-			(require-any
-				(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
-				(signing-identifier "com.apple.shortcuts.watch")
-			)
-			(signing-identifier "com.apple.WorkflowKit.BackgroundShortcutRunner")
-			(signing-identifier "com.apple.shortcuts")
+			(%entitlement-is-bool-true "com.apple.private.ids.remoteurlconnection")
+			(%entitlement-is-bool-true "com.apple.private.imcore.imremoteurlconnection")
 		)
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.AOSNotification")
-		(%entitlement-is-bool-true "com.apple.aosnotification.aosnotifyd-access")
+		(global-name "com.apple.bulletinboard.settingsconnection")
+		(%entitlement-is-bool-true "com.apple.bulletinboard.settings")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.bulletinboard.settingsconnection")
-		(%entitlement-is-bool-true "com.apple.bulletinboard.settings")
+		(global-name "com.apple.telephonyutilities.callservicesdaemon.ptt")
+		(%entitlement-is-bool-true "com.apple.developer.push-to-talk")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.telephonyutilities.callservicesdaemon.ptt")
-		(%entitlement-is-bool-true "com.apple.developer.push-to-talk")
+		(global-name "com.apple.callkit.networkextension.voip")
+		(%entitlement-is-present "com.apple.developer.networking.networkextension")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.FileCoordination")
-		(signing-identifier "com.apple.Music")
+		(global-name "com.apple.odi.assessmentService")
+		(%entitlement-is-present "com.apple.developer.trustinsights.base")
 	)
 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.financed.service.coredatastore")
-		(require-any
-			(%entitlement-is-present "com.apple.developer.financekit")
-			(%entitlement-is-present "com.apple.finance.private")
-		)
+		(local-name "com.apple.iphone.axserver")
+		(%entitlement-is-bool-true "com.apple.accessibility.api")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.ServicesPaymentAngel")
-		(%entitlement-is-present "com.apple.private.applemediaservices")
+		(process-attribute is-apple-signed-executable)
+		(require-any
+			(global-name "com.apple.SharedWebCredentials")
+			(global-name "com.apple.dataaccess.dataaccessd")
+			(global-name "com.apple.exchangesyncd")
+			(xpc-service-name "com.apple.LORemoteUIPinService")
+			(xpc-service-name "com.apple.ctcategories.service")
+		)
 	)
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
+		(global-name "com.apple.mobile.keybagd.xpc")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
+			(signing-identifier "com.apple.WebContentFilter.remoteUI.WebContentAnalysisUI")
+		)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.weatherkit.authservice")
-		(%entitlement-is-present "com.apple.developer.weatherkit")
+		(global-name "com.apple.powerlog.plxpclogger.xpc")
+		(require-any
+			(signing-identifier "com.apple.WorkflowKit.ShortcutsIntents")
+			(signing-identifier "com.apple.shortcuts.watch")
+		)
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
+		(global-name "com.apple.browserkitd")
+		(%entitlement-is-present "com.apple.developer.web-browser")
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(process-attribute is-apple-signed-executable)
+		(signing-identifier "com.apple.Bridge")
 		(require-any
-			(global-name "com.apple.osanalytics.osanalyticshelper")
-			(require-any
-				(global-name "com.apple.ReportCrash")
-				(global-name "com.apple.ReportCrash.DirectoryService")
-				(global-name "com.apple.ReportCrash.SafetyNet")
-				(global-name "com.apple.ReportCrash.StackShot")
-			)
+			(global-name "com.apple.PowerManagement.control")
+			(global-name "com.apple.iokit.powerdxpc")
+			(global-name "com.apple.powerlog.plxpclogger.xpc")
 		)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.identityservicesd.embedded.auth")
+		(signing-identifier "com.apple.mobilemail")
 		(require-any
-			(%entitlement-is-bool-true "com.apple.private.amfi.can-execute-cdhash")
-			(signing-identifier "com.apple.Bridge")
+			(global-name "com.apple.backupd")
+			(global-name "com.apple.bulletindistributord.server")
+			(global-name "com.apple.harvestd.manager")
+			(global-name "com.apple.identityservicesd.embedded.auth")
+			(global-name "com.apple.mobilemail")
+			(global-name "com.apple.nanoprefsync")
+			(global-name "com.apple.routined.registration")
+			(global-name "com.apple.sharingd.nsxpc")
 		)
 	)
 )

 )
 (allow mach-lookup
 	(require-all
-		(global-name "com.apple.safarifetcherd")
-		(signing-identifier "com.apple.mobilesafari")
+		(global-name "com.apple.icloud.findmydeviced")
+		(require-any
+			(%entitlement-is-bool-true "com.apple.aosnotification.aosnotifyd-access")
+			(%entitlement-is-bool-true "com.apple.icloud.findmydeviced.access")
+		)
 	)
 )
 (allow mach-lookup

 )
 (allow mach-lookup
 	(require-all
-		(signing-identifier "com.apple.Maps")
-		(require-any
-			(global-name "com.apple.PowerManagement.control")
-			(global-name "com.apple.assistant.analytics")
-			(global-name "com.apple.iokit.powerdxpc")
-			(global-name "com.apple.nanomaps.xpc.GeoServices.Navigation")
-			(global-name "com.apple.nanomaps.xpc.Navigation")
-			(global-name "com.apple.powerlog.plxpclogger.xpc")
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
+			(global-name "com.apple.ServicesPaymentAngel")
+			(global-name "com.apple.ServicesPaymentAngel.jetpackAssets")
+		)
+		(%entitlement-is-present "com.apple.private.applemediaservices")
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

 		(global-name "com.apple.coremedia.mediaplaybackd.player.xpc")
 		(global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc")
 		(global-name "com.apple.coremedia.mediaplaybackd.samplebufferaudiorenderer.xpc")
+		(global-name "com.apple.coremedia.mediaplaybackd.samplebufferprovider.xpc")
 		(global-name "com.apple.coremedia.mediaplaybackd.samplebufferrendersynchronizer.xpc")
 		(global-name "com.apple.coremedia.mediaplaybackd.samplegenerator.xpc")
 		(global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc")

 
 (allow sysctl-read
 	(require-all
-		(require-any
-			(sysctl-name "kern.proc.*")
-			(sysctl-name "kern.procargs2.*")
-		)
+		(sysctl-name "kern.proc.*")
+		(%entitlement-is-bool-true "com.apple.DiagnosticExtensions.extension")
+	)
+)
+(allow sysctl-read
+	(require-all
+		(sysctl-name "kern.procargs2.*")
 		(%entitlement-is-bool-true "com.apple.DiagnosticExtensions.extension")
 	)
 )
```
