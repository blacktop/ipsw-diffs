## MessagesViewService

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.uikit.viewservice.com.apple.iMessageAppsViewService")
 		))
 		(require-not (global-name "com.apple.biome.access.user"))
+		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.naturallanguaged"))
 		(require-not (global-name "com.apple.icloud.fmfd"))
 		(require-not (global-name "com.apple.webinspector"))

 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
-		(require-not (require-any
-			(global-name "com.apple.findmy.findmylocate.friendshipservice")
-			(global-name "com.apple.findmy.findmylocate.settings")
-		))
+		(require-not (global-name "com.apple.findmy.findmylocate.friendshipservice"))
 		(require-not (global-name "com.apple.siri.vocabularyupdates"))
 		(require-not (global-name "com.apple.dmd.emergency-mode"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.SocialHighlight"))

 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.coremedia.customurlloader.xpc"))
-		(require-not (global-name "com.apple.contactsd"))
+		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))

 		(require-not (global-name "com.apple.awdd"))
 		(require-not (local-name "com.apple.assistant.contextprovider.com.apple.mobilesms.compose"))
 		(require-not (global-name "com.apple.coremedia.assetimagegenerator.xpc"))
-		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
+		(require-not (global-name "com.apple.findmy.findmylocate.settings"))
 		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.spotlight.SearchAgent"))
+		(require-not (global-name "com.apple.quicklook.ThumbnailsAgent"))
 		(require-not (global-name "com.apple.dprivacyd"))
 		(require-not (global-name "com.apple.fairplayd.xpc"))
-		(require-not (global-name "com.apple.quicklook.ThumbnailsAgent"))
-		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
-		(require-not (global-name "com.apple.coremedia.compressionsession"))
+		(require-not (global-name "com.apple.contactsd"))
+		(require-not (global-name "com.apple.spotlight.SearchAgent"))
+		(require-not (global-name "com.apple.aggregated"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.communication"))
 		(require-not (global-name "com.apple.identityservicesd.nsxpc"))

 		(require-not (global-name "com.apple.internal.InputTester"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon.libxpc"))
 		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.aggregated"))
+		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.GameController.gamecontrollerd.app"))
 		(require-not (global-name "com.apple.ind.cloudfeatures"))

 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.dmd.policy"))
-		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
+		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (global-name "com.apple.translationd"))
-		(require-not (global-name "com.apple.lsd.open"))
+		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
 		(require-not (global-name "com.apple.asktod"))
 		(require-not (global-name "com.apple.handwritingd.pkanalytics"))
 		(require-not (global-name "com.apple.coremedia.sandboxserver.xpc"))

 		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.backboard.TouchDeliveryPolicyServer"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.private"))
+		(require-not (global-name "com.apple.coremedia.compressionsession"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))
 		(require-not (global-name "com.apple.AccessibilityUIServer"))
 		(require-not (global-name "UIASTNotificationCenter"))

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7 65 67))
+			(require-not (mac-syscall-number 5 6))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 12))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(with-filter (mac-policy-name "vnguard")
+	(deny system-mac-syscall
+		(require-not (mac-syscall-number 1))
 	)
 )
 (deny system-mac-syscall
```
