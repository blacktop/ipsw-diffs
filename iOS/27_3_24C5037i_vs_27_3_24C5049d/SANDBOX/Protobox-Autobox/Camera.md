## Camera

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.contacts.donation.agent"))
 		(require-not (global-name "com.apple.internal.objc_trace"))
+		(require-not (require-any
+			(global-name "com.apple.ixda.voicecamd")
+			(global-name "com.apple.visualintelligence.nutrition-log-dispatch")
+		))
 		(require-not (global-name "com.apple.lsd.xpc"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
 		(require-not (global-name "com.apple.assetsd.keepDaemonAlive"))

 		(require-not (global-name "com.apple.parsecd"))
 		(require-not (global-name "com.apple.companion.camera"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.visualintelligence.nutrition-log-dispatch"))
+		(require-not (xpc-service-name "com.apple.Gestures.tracing.service.xpc"))
 		(require-not (global-name "com.apple.RemoteDisplay"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.visualintelligence.visual-action-prediction"))

 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.bytedance.ios.doubaoime.keyboardExtension"))
-		(require-not (xpc-service-name "com.apple.Gestures.tracing.service.xpc"))
-		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
+		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.CameraOverlayAngel.application-service"))
 		(require-not (global-name "PurplePPTServer"))
 		(require-not (system-attribute developer-mode))
```
