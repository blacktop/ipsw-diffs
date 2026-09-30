## MomentsUIService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.TextInput"))
 		(require-not (global-name "com.apple.TextInput.emoji"))
 		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
+		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))

 		(require-not (global-name "com.apple.mobilecheckpoint.checkpointd"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.dt.automationmode.reader"))
+		(require-not (global-name "com.apple.DragUI.druid.destination"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.UIKit.OverlayUI.services"))

 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.EventTimingProfileService"))
 		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
-		(require-not (global-name "com.apple.CARenderServer"))
-		(require-not (global-name "com.apple.DragUI.druid.destination"))
-		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.AccessibilityUIServer"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
+		(require-not (global-name "UIASTNotificationCenter"))
 		(require-not (global-name "PurplePPTServer"))
 		(require-not (system-attribute developer-mode))
 	)
```
