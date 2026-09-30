## pointeruid

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
+		(require-not (require-any
+			(global-name "com.apple.UIKit.MainMenuStateDelegate")
+			(global-name "com.apple.uikit.viewservice.mainmenustatedelegate")
+		))
 		(require-not (global-name "com.apple.UIKit.OverlayUI.services"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (xpc-service-name "com.apple.EventTimingProfileService"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.backboard.display.services"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))

 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
-		(require-not (xpc-service-name "com.apple.EventTimingProfileService"))
 		(require-not (global-name "com.apple.PrototypeTools.domainserver"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
```
