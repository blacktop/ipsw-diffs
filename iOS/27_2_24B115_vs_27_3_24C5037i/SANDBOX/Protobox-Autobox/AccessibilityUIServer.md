## AccessibilityUIServer

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.storekitd"))
 		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.naturallanguaged"))
+		(require-not (global-name "com.apple.webinspector"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.AutoFillSuggestions"))
 		(require-not (global-name "com.apple.osanalytics.osanalyticshelper"))

 		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
-		(require-not (global-name "com.apple.Carousel.CSLSDetentService"))
+		(require-not (require-any
+			(global-name "com.apple.Carousel.CSLSDetentService")
+			(global-name "com.apple.uikit.viewservice.com.apple.QuickboardViewService")
+		))
 		(require-not (global-name "com.apple.hangtelemetryd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))

 		(require-not (global-name "com.apple.TextInput.preferences"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.accessibility.AXSpringBoardServer"))
 		(require-not (global-name "com.apple.soundanalysisd"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))

 			(global-name "com.apple.accessibility.AXCarouselServer")
 			(global-name "com.apple.airplay.autoconnect.services")
 		))
-		(require-not (xpc-service-name "com.apple.SpeechRecognitionCore.brokerd"))
+		(require-not (xpc-service-name "com.apple.extensionkitservice"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.carkit.dnd.service"))

 		(require-not (global-name "com.apple.sirittsd"))
 		(require-not (global-name "com.apple.Carousel.ButtonTapAssertion"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.assistant.dictation"))
 		(require-not (global-name "com.apple.airplay.receiver.services"))
 		(require-not (global-name "com.apple.webprivacyd"))

 		(require-not (global-name "com.apple.internal.InputTester"))
 		(require-not (global-name "com.apple.accessibility.AXClarityBoardServer"))
 		(require-not (global-name "com.apple.healthlited"))
-		(require-not (xpc-service-name "com.swiftkey.SwiftKeyApp.Keyboard"))
+		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.pearld"))
 		(require-not (global-name "com.apple.GameController.gamecontrollerd.app"))

 		(require-not (global-name "com.apple.breadboardservices"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.coreduetd.context"))
-		(require-not (global-name "com.apple.uikit.viewservice.com.apple.QuickboardViewService"))
+		(require-not (xpc-service-name "com.apple.SpeechRecognitionCore.brokerd"))
 		(require-not (global-name "com.apple.rti-stagertool"))
 		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
 		(require-not (global-name "com.apple.carousel.backlightxpc"))

 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
 		(require-not (xpc-service-name "com.apple.AXMediaUtilitiesService"))
 		(require-not (xpc-service-name "com.apple.audio.AUCrashHandlerService"))
-		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
-		(require-not (xpc-service-name "com.apple.extensionkitservice"))
+		(require-not (xpc-service-name "com.swiftkey.SwiftKeyApp.Keyboard"))
 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 80))
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 67))
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

 		NECP_CLIENT_ACTION_REMOVE_FLOW
 		NECP_CLIENT_ACTION_UPDATE_CACHE)
 )
-
-(allow process-exec-update-label)
```
