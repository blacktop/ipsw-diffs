## CheckerBoard

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.networking.captivenetworksupport"))
 		(require-not (global-name "com.apple.hangtracerd"))
-		(require-not (global-name "com.apple.rti-screencontinuity"))
+		(require-not (require-any
+			(global-name "com.apple.remote-text-editing-legacy")
+			(global-name "com.apple.rti-screencontinuity")
+			(global-name "com.apple.sharing.remote-text-editing")
+		))
 		(require-not (global-name "com.apple.systemstatus"))
 		(require-not (global-name "com.apple.UIKit.KeyboardManagement.hosted"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))

 		(require-not (global-name "com.apple.dasd.end-prewarm"))
 		(require-not (global-name "com.apple.wifi.manager"))
 		(require-not (global-name "com.apple.sharing.sharesheet"))
-		(require-not (require-any
-			(global-name "com.apple.remote-text-editing-legacy")
-			(global-name "com.apple.sharing.remote-text-editing")
-		))
+		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.UIKit.statusbarserver"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.commcenter.xpc"))

 		(require-not (global-name "com.apple.assistant.dictation"))
 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.DragUI.druid.source"))
 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))

 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
-		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.AccessibilityUIServer"))
 		(require-not (system-attribute developer-mode))
```
