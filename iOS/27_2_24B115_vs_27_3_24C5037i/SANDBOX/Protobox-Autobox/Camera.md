## Camera

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 		(require-not (global-name "com.apple.itunescloud.music-subscription-status-service"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.networking.captivenetworksupport"))
 		(require-not (global-name "com.apple.hangtracerd"))
 		(require-not (global-name "com.apple.healthd.server"))
 		(require-not (global-name "com.apple.PrototypeTools.domainserver"))

 		(require-not (global-name "com.apple.assetsd.nebulad"))
 		(require-not (global-name "com.apple.assistant.cdm"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
-		(require-not (require-any
-			(global-name "com.apple.findmy.findmylocate.friendshipservice")
-			(global-name "com.apple.findmy.findmylocate.settings")
-		))
+		(require-not (global-name "com.apple.findmy.findmylocate.friendshipservice"))
 		(require-not (global-name "com.apple.accessibility.AXSpringBoardServer"))
 		(require-not (global-name "com.apple.maps.virtualgarage.server"))
 		(require-not (global-name "com.apple.diagnosticd"))

 		(require-not (global-name "com.apple.synapse.backlink-service"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))
+		(require-not (global-name "com.apple.findmy.findmylocate.settings"))
+		(require-not (global-name "com.apple.runningboard"))
 		(require-not (require-any
 			(xpc-service-name "com.google.keyboard.KeyboardExtension")
 			(xpc-service-name "com.sogou.sogouinput.basekeyboard")
 			(xpc-service-name "com.tencent.wetype.keyboard")
 		))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (xpc-service-name "com.apple.Gestures.tracing.service.xpc"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.communication"))
 		(require-not (global-name "com.apple.audio.AudioUnitServer"))
 		(require-not (global-name "com.apple.coreduetd.people"))

 		(require-not (global-name "com.apple.GameController.gamecontrollerd.app"))
 		(require-not (global-name "com.apple.ind.cloudfeatures"))
 		(require-not (global-name "com.apple.corefollowup.agent"))
+		(require-not (global-name "com.apple.siriactionsd.xpc"))
 		(require-not (global-name "com.apple.generativeexperiences.agentMediaStore"))
 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
 		(require-not (global-name "com.apple.coreduetd.context"))

 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.bytedance.ios.doubaoime.keyboardExtension"))
-		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
+		(require-not (xpc-service-name "com.apple.Gestures.tracing.service.xpc"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
 		(require-not (global-name "com.apple.CameraOverlayAngel.application-service"))
 		(require-not (global-name "PurplePPTServer"))
 		(require-not (system-attribute developer-mode))

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 5))
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
