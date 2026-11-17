## OverlayUI

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.hangtracerd"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
-		(require-not (global-name "com.apple.rti-screencontinuity"))
+		(require-not (require-any
+			(global-name "com.apple.remote-text-editing-legacy")
+			(global-name "com.apple.rti-screencontinuity")
+			(global-name "com.apple.sharing.remote-text-editing")
+		))
 		(require-not (global-name "com.apple.UIKit.KeyboardManagement.hosted"))
 		(require-not (global-name "com.apple.PrototypeTools.domainserver"))
 		(require-not (require-any

 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
 		(require-not (global-name "com.apple.dasd.end-prewarm"))
 		(require-not (require-any
-			(global-name "com.apple.remote-text-editing-legacy")
-			(global-name "com.apple.sharing.remote-text-editing")
+			(xpc-service-name "com.google.keyboard.KeyboardExtension")
+			(xpc-service-name "com.sogou.sogouinput.basekeyboard")
+			(xpc-service-name "com.tencent.wetype.keyboard")
 		))
 		(require-not (global-name "com.apple.handwritingd.remoterecognition"))
 		(require-not (global-name "com.apple.accessibility.voices"))

 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
 		(require-not (global-name "com.apple.stickers.api"))
 		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (require-any
-			(xpc-service-name "com.google.keyboard.KeyboardExtension")
-			(xpc-service-name "com.sogou.sogouinput.basekeyboard")
-			(xpc-service-name "com.tencent.wetype.keyboard")
-		))
+		(require-not (xpc-service-name "com.swiftkey.SwiftKeyApp.Keyboard"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.DragUI.druid.source"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.rti-stagertool"))
+		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
 		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
 		(require-not (global-name "com.apple.audio.AudioQueueServer"))
 		(require-not (global-name "com.apple.hangtracermonitor"))

 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
-		(require-not (xpc-service-name "com.swiftkey.SwiftKeyApp.Keyboard"))
+		(require-not (xpc-service-name "com.navercorp.smartboard.extension"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.player.xpc"))
 		(require-not (global-name "com.apple.assistant.analytics"))

 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
-		(require-not (xpc-service-name "com.navercorp.smartboard.extension"))
 		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AccessibilityUIServer"))
```
