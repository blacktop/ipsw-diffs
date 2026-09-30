## OverlayUI

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.dt.automationmode.reader"))
+		(require-not (global-name "com.apple.DragUI.druid.destination"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))

 		(require-not (global-name "com.apple.TextInput.image-cache-server"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.assistant.dictation"))
 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
 		(require-not (global-name "com.apple.stickers.api"))

 			(xpc-service-name "com.tencent.wetype.keyboard")
 		))
 		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.DragUI.druid.source"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.rti-stagertool"))

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
+		(require-not (xpc-service-name "com.swiftkey.SwiftKeyApp.Keyboard"))
 		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
-		(require-not (global-name "com.apple.FileCoordination"))
-		(require-not (global-name "com.apple.DragUI.druid.source"))
-		(require-not (global-name "com.apple.DragUI.druid.destination"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AccessibilityUIServer"))
+		(require-not (global-name "UIASTNotificationCenter"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
