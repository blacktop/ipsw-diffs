## Photos

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
 		(require-not (global-name "com.apple.passd.in-app-payment"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (require-any
-			(xpc-service-name "com.google.keyboard.KeyboardExtension")
-			(xpc-service-name "com.sogou.sogouinput.basekeyboard")
-			(xpc-service-name "com.tencent.wetype.keyboard")
-		))
+		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
 		(require-not (global-name "com.apple.siri.analytics.assistant"))
 		(require-not (global-name "com.apple.visualintelligence.visual-action-prediction"))
 		(require-not (global-name "com.apple.asktod"))
 		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.sharingd.pairedcontactmanager"))
 		(require-not (local-name "com.apple.accessibility.gax.client"))
+		(require-not (require-any
+			(xpc-service-name "com.navercorp.smartboard.extension")
+			(xpc-service-name "com.willowvoice.ios.keyboard")
+		))
+		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
+		(require-not (xpc-service-name "com.apple.CloudSharing.SPIHelper-iOS"))
 		(require-not (require-any
 			(xpc-service-name "com.clusterdev.malayalam.keyboard")
 			(xpc-service-name "com.evoafuture.bettertalk.keyboard")

 			(xpc-service-name "com.jeethukthomas.ezhuthaani.manglish")
 			(xpc-service-name "com.jimmy54.SuperWubi.Keyboard")
 			(xpc-service-name "com.linecorp.LineEmoji.KeyboardExtension")
-			(xpc-service-name "com.navercorp.smartboard.extension")
-			(xpc-service-name "com.willowvoice.ios.keyboard")
 		))
-		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
-		(require-not (xpc-service-name "com.apple.CloudSharing.SPIHelper-iOS"))
 		(require-not (xpc-service-name "com.swiftkey.SwiftKeyApp.Keyboard"))
-		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
 		(require-not (xpc-service-name "com.bytedance.ios.doubaoime.keyboardExtension"))
+		(require-not (require-any
+			(xpc-service-name "com.google.keyboard.KeyboardExtension")
+			(xpc-service-name "com.sogou.sogouinput.basekeyboard")
+			(xpc-service-name "com.tencent.wetype.keyboard")
+		))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
