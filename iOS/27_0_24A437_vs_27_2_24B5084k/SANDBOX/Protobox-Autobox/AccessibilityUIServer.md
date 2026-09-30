## AccessibilityUIServer

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.accessibility.AXPineBoardServer"))
 		(require-not (global-name "com.apple.TextInput.accessibility"))
 		(require-not (global-name "com.apple.accessibility.mediaaccessibilityd"))
-		(require-not (require-any
-			(global-name "com.apple.Carousel.alertSuppression")
-			(global-name "com.apple.accessibility.AXCarouselServer")
-			(global-name "com.apple.airplay.autoconnect.services")
-		))
+		(require-not (global-name "com.apple.Carousel.alertSuppression"))
 		(require-not (global-name "com.apple.TextInput.emoji"))
 		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
 		(require-not (global-name "com.apple.appleneuralengine"))

 		(require-not (global-name "com.apple.shazamd"))
 		(require-not (global-name "com.apple.hangtracerd"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
+		(require-not (global-name "com.apple.healthd.server"))
 		(require-not (global-name "com.apple.rti-screencontinuity"))
 		(require-not (global-name "com.apple.systemstatus"))
 		(require-not (global-name "com.apple.assistant.settings"))

 		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
-		(require-not (require-any
-			(global-name "com.apple.Carousel.CSLSDetentService")
-			(global-name "com.apple.uikit.viewservice.com.apple.QuickboardViewService")
-		))
+		(require-not (global-name "com.apple.Carousel.CSLSDetentService"))
 		(require-not (global-name "com.apple.hangtelemetryd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.usernotifications.remotenotificationservice"))
+		(require-not (require-any
+			(global-name "com.apple.UIKit.MainMenuStateDelegate")
+			(global-name "com.apple.uikit.viewservice.mainmenustatedelegate")
+		))
 		(require-not (global-name "com.apple.kvsd"))
 		(require-not (global-name "com.apple.feedbacklogger"))
 		(require-not (global-name "com.apple.CompanionLink"))

 		(require-not (global-name "com.apple.coremedia.endpointuiagent.xpc"))
 		(require-not (global-name "com.apple.cloudkit.partlycloudd"))
 		(require-not (require-any
-			(global-name "com.apple.remote-text-editing-legacy")
-			(global-name "com.apple.sharing.remote-text-editing")
+			(global-name "com.apple.accessibility.AXCarouselServer")
+			(global-name "com.apple.airplay.autoconnect.services")
 		))
+		(require-not (xpc-service-name "com.apple.SpeechRecognitionCore.brokerd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.carkit.dnd.service"))

 		(require-not (global-name "com.apple.Carousel.wristmonitor"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.sharing.sharesheet"))
+		(require-not (require-any
+			(global-name "com.apple.remote-text-editing-legacy")
+			(global-name "com.apple.sharing.remote-text-editing")
+		))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
 		(require-not (global-name "com.apple.siri.activation.service"))
 		(require-not (global-name "com.apple.UIKit.statusbarserver"))

 		(require-not (global-name "com.apple.backboard.display.services"))
 		(require-not (global-name "com.apple.generativeexperiences.textcomposition"))
 		(require-not (global-name "com.apple.uiintelligencesupport.agent"))
+		(require-not (global-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.sessionservices"))
 		(require-not (global-name "com.apple.pasteboard.pasted"))

 		(require-not (global-name "com.apple.internal.InputTester"))
 		(require-not (global-name "com.apple.accessibility.AXClarityBoardServer"))
 		(require-not (global-name "com.apple.healthlited"))
+		(require-not (xpc-service-name "com.swiftkey.SwiftKeyApp.Keyboard"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.pearld"))
 		(require-not (global-name "com.apple.GameController.gamecontrollerd.app"))

 		(require-not (global-name "com.apple.breadboardservices"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.coreduetd.context"))
+		(require-not (global-name "com.apple.uikit.viewservice.com.apple.QuickboardViewService"))
 		(require-not (global-name "com.apple.rti-stagertool"))
 		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
 		(require-not (global-name "com.apple.carousel.backlightxpc"))

 		(require-not (global-name "com.apple.corespeech.corespeechd.xpc"))
 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.audio.AURemoteIOServer"))
+		(require-not (global-name "com.apple.DeviceConfigurationAgent.provider"))
 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.appprotectiond.read"))

 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
 		(require-not (xpc-service-name "com.apple.audio.AUCrashHandlerService"))
 		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
-		(require-not (xpc-service-name "com.swiftkey.SwiftKeyApp.Keyboard"))
 		(require-not (xpc-service-name "com.apple.extensionkitservice"))
-		(require-not (xpc-service-name "com.apple.SpeechRecognitionCore.brokerd"))
 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
```
