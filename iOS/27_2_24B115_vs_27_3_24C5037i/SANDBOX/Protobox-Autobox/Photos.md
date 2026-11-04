## Photos

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.systemstatus"))
 		(require-not (global-name "com.apple.contacts.donation.agent"))
 		(require-not (global-name "com.apple.TapToRadarKit.service"))
-		(require-not (require-any
-			(global-name "com.apple.findmy.findmylocate.friendshipservice")
-			(global-name "com.apple.findmy.findmylocate.settings")
-		))
+		(require-not (global-name "com.apple.findmy.findmylocate.friendshipservice"))
 		(require-not (global-name "com.apple.dmd.emergency-mode"))
 		(require-not (global-name "com.apple.appledepthd"))
 		(require-not (global-name "com.apple.mobileactivationd"))

 		(require-not (global-name "com.apple.DeviceConfigurationAgent.publisher"))
 		(require-not (global-name "com.apple.passd.payment"))
 		(require-not (global-name "com.apple.transparencyd"))
-		(require-not (require-any
-			(xpc-service-name "com.bitstrips.imoji.BitmojiKeyboard")
-			(xpc-service-name "com.codeway.AIKeyboard.custom-keyboard")
-			(xpc-service-name "com.grammarly.keyboard.extension")
-			(xpc-service-name "com.riffsy.RiffsyKeyboard.RiffsyGIFKeyboard")
-			(xpc-service-name "com.superduper.superwhisper-ios.superwhisper-keyboard")
-			(xpc-service-name "com.tackgyulee.dinggul.dinggulkeyboard")
-			(xpc-service-name "com.typeless.mobile.keyboard")
-			(xpc-service-name "com.wispr.flowapp.flowboard")
-		))
+		(require-not (global-name "com.apple.findmy.findmylocate.settings"))
 		(require-not (global-name "com.apple.audio.AudioUnitServer"))
 		(require-not (global-name "com.apple.ScreenTimeSettingsAgent.private"))
 		(require-not (global-name "com.apple.internal.InputTester"))

 		(require-not (global-name "com.apple.corefollowup.agent"))
 		(require-not (global-name "com.apple.siriactionsd.xpc"))
 		(require-not (global-name "com.apple.generativeexperiences.agentMediaStore"))
-		(require-not (require-any
-			(global-name "com.apple.proximitycamerad")
-			(global-name "com.apple.visualintelligence.daemon-status")
-		))
+		(require-not (global-name "com.apple.visualintelligence.daemon-status"))
 		(require-not (global-name "com.apple.rti-stagertool"))
 		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
 		(require-not (global-name "com.apple.imagent.embedded.auth"))

 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
 		(require-not (global-name "com.apple.passd.in-app-payment"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
+		(require-not (global-name "com.apple.proximitycamerad"))
 		(require-not (global-name "com.apple.siri.analytics.assistant"))
 		(require-not (global-name "com.apple.visualintelligence.visual-action-prediction"))
 		(require-not (global-name "com.apple.routined.registration"))

 		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.sharingd.pairedcontactmanager"))
 		(require-not (local-name "com.apple.accessibility.gax.client"))
-		(require-not (require-any
-			(xpc-service-name "com.scripting.ios.KeyboardExtension")
-			(xpc-service-name "com.willowvoice.ios.keyboard")
-		))
+		(require-not (xpc-service-name "com.willowvoice.ios.keyboard"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
-		(require-not (xpc-service-name "com.baidu.inputMethod.keyboard"))
+		(require-not (require-any
+			(xpc-service-name "com.bitstrips.imoji.BitmojiKeyboard")
+			(xpc-service-name "com.codeway.AIKeyboard.custom-keyboard")
+			(xpc-service-name "com.grammarly.keyboard.extension")
+			(xpc-service-name "com.riffsy.RiffsyKeyboard.RiffsyGIFKeyboard")
+			(xpc-service-name "com.scripting.ios.KeyboardExtension")
+			(xpc-service-name "com.superduper.superwhisper-ios.superwhisper-keyboard")
+			(xpc-service-name "com.tackgyulee.dinggul.dinggulkeyboard")
+			(xpc-service-name "com.typeless.mobile.keyboard")
+			(xpc-service-name "com.wispr.flowapp.flowboard")
+		))
 		(require-not (require-any
 			(xpc-service-name "com.clusterdev.malayalam.keyboard")
 			(xpc-service-name "com.evoafuture.bettertalk.keyboard")

 			(xpc-service-name "com.linecorp.LineEmoji.KeyboardExtension")
 			(xpc-service-name "ru.yandex.mobile.keyboard.extension")
 		))
-		(require-not (xpc-service-name "com.apple.CloudSharing.SPIHelper-iOS"))
+		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
 		(require-not (xpc-service-name "com.bytedance.ios.doubaoime.keyboardExtension"))
 		(require-not (require-any
 			(xpc-service-name "com.google.keyboard.KeyboardExtension")

 		))
 		(require-not (xpc-service-name "com.swiftkey.SwiftKeyApp.Keyboard"))
 		(require-not (xpc-service-name "com.navercorp.smartboard.extension"))
+		(require-not (xpc-service-name "com.apple.CloudSharing.SPIHelper-iOS"))
+		(require-not (xpc-service-name "com.baidu.inputMethod.keyboard"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
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
```
