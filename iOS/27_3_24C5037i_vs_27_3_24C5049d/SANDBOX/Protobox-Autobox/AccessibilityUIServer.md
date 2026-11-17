## AccessibilityUIServer

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.hangtracerd"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (global-name "com.apple.healthd.server"))
-		(require-not (global-name "com.apple.rti-screencontinuity"))
+		(require-not (require-any
+			(global-name "com.apple.remote-text-editing-legacy")
+			(global-name "com.apple.rti-screencontinuity")
+			(global-name "com.apple.sharing.remote-text-editing")
+		))
 		(require-not (global-name "com.apple.systemstatus"))
 		(require-not (global-name "com.apple.assistant.settings"))
 		(require-not (global-name "com.apple.UIKit.KeyboardManagement.hosted"))

 			(global-name "com.apple.accessibility.AXCarouselServer")
 			(global-name "com.apple.airplay.autoconnect.services")
 		))
-		(require-not (xpc-service-name "com.apple.extensionkitservice"))
+		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.carkit.dnd.service"))

 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.sharing.sharesheet"))
 		(require-not (require-any
-			(global-name "com.apple.remote-text-editing-legacy")
-			(global-name "com.apple.sharing.remote-text-editing")
+			(global-name "com.apple.appprotectiond.viewsubjectinfo")
+			(global-name "com.apple.appprotectiond.viewsubjectmonitor")
 		))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
 		(require-not (global-name "com.apple.siri.activation.service"))

 		(require-not (global-name "com.apple.audio.AudioUnitServer"))
 		(require-not (global-name "com.apple.TextInput.image-cache-server"))
 		(require-not (global-name "com.apple.locationd.registration"))
-		(require-not (global-name "com.apple.appprotectiond.viewsubjectinfo"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.conversationmanager"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.sirittsd"))

 		(require-not (global-name "com.apple.internal.InputTester"))
 		(require-not (global-name "com.apple.accessibility.AXClarityBoardServer"))
 		(require-not (global-name "com.apple.healthlited"))
-		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.pearld"))
 		(require-not (global-name "com.apple.GameController.gamecontrollerd.app"))

 		(require-not (global-name "com.apple.breadboardservices"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.coreduetd.context"))
-		(require-not (xpc-service-name "com.apple.SpeechRecognitionCore.brokerd"))
 		(require-not (global-name "com.apple.rti-stagertool"))
 		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
 		(require-not (global-name "com.apple.carousel.backlightxpc"))

 		(require-not (xpc-service-name "com.apple.AXMediaUtilitiesService"))
 		(require-not (xpc-service-name "com.apple.audio.AUCrashHandlerService"))
 		(require-not (xpc-service-name "com.swiftkey.SwiftKeyApp.Keyboard"))
+		(require-not (xpc-service-name "com.apple.extensionkitservice"))
+		(require-not (xpc-service-name "com.apple.SpeechRecognitionCore.brokerd"))
 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
```
