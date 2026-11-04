## ClarityBoard

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.CarPlayApp.non-launching-service"))
 		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
 		(require-not (global-name "com.apple.assistant.client"))
-		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.MobileTimer.timerserver"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))
 		(require-not (global-name "com.apple.fullkeyboardaccess"))

 		(require-not (global-name "com.apple.coreduetd.knowledge"))
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc"))
+		(require-not (global-name "com.apple.geoanalyticsd"))
 		(require-not (global-name "com.apple.assistant.uibridge-service"))
 		(require-not (require-any
 			(global-name "com.apple.assistant.request-dispatcher.uibridge-service")

 		(require-not (global-name "com.apple.coremedia.endpoint.xpc"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.dmd.emergency-mode"))
 		(require-not (global-name "com.apple.accessibility.AXSpringBoardServer"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.backlightd"))

 		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.modelmanager"))
+		(require-not (global-name "com.apple.linkd.autoShortcut"))
 		(require-not (global-name "com.apple.accessibility.voices"))
 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
 		(require-not (global-name "com.apple.springboard.services"))

 		(require-not (global-name "com.apple.dt.xctestd.target"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.campo"))
+		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.installcoordinationd"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.carkit.service"))
 		(require-not (global-name "com.apple.assistivetouchd"))
+		(require-not (global-name "com.apple.transparencyd"))
 		(require-not (global-name "com.apple.MobileTimer.alarmserver"))
 		(require-not (global-name "com.apple.wirelessproxd"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.figmetriceventtimeline.xpc"))
 		(require-not (global-name "com.apple.mediaremoted.xpc"))
 		(require-not (global-name "com.apple.accessibility.heard"))
+		(require-not (global-name "com.apple.synapse.backlink-service"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.fairplayd.xpc"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
+		(require-not (global-name "com.apple.ScreenTimeAgent.communication"))
 		(require-not (global-name "com.apple.TextInput.image-cache-server"))
 		(require-not (global-name "com.apple.coreduetd.people"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.conversationmanager"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.audioprocessingtap.xpc"))
 		(require-not (global-name "com.apple.iohideventsystem"))
-		(require-not (global-name "com.apple.AttentionAwareness"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.FileCoordination"))

 		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
 		(require-not (global-name "com.apple.hangtracermonitor"))
 		(require-not (global-name "com.apple.audio.hapticd"))
+		(require-not (global-name "com.apple.linkd.application-service"))
 		(require-not (global-name "com.apple.passd.library"))
 		(require-not (global-name "com.apple.diagnosticpipeline.service"))
 		(require-not (global-name "com.apple.systemstatus.activityattribution"))

 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.itunesstored.xpc"))
+		(require-not (global-name "com.apple.remindd"))
 		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.siri.analytics.assistant"))

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
+				(require-not (global-name "com.apple.CARenderServer"))
+				(require-not (global-name "com.apple.AttentionAwareness"))
+				(require-not (global-name "com.apple.ABDatabaseDoctor"))
 				(require-not (global-name "com.apple.AccessibilityUIServer"))
 				(require-not (global-name "com.apple.AppSSO.service-xpc"))
 				(require-not (global-name "UIASTNotificationCenter"))

 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
+				(require-not (global-name "com.apple.CARenderServer"))
+				(require-not (global-name "com.apple.AttentionAwareness"))
+				(require-not (global-name "com.apple.ABDatabaseDoctor"))
 				(require-not (global-name "com.apple.AccessibilityUIServer"))
 				(require-not (global-name "com.apple.AppSSO.service-xpc"))
 				(require-not (global-name "UIASTNotificationCenter"))

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 4 5 6 7 15 67))
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
