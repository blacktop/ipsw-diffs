## CoreServicesUIAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.TextInput"))
 		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
-		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.hangtracerd"))
 		(require-not (global-name "com.apple.UIKit.KeyboardManagement.hosted"))

 		(require-not (global-name "com.apple.dasd.end-prewarm"))
 		(require-not (global-name "com.apple.UIKit.statusbarserver"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "UIASTNotificationCenter"))
 		(require-not (global-name "com.apple.accessibility.voices"))
+		(require-not (global-name "com.apple.springboard.services"))
 		(require-not (global-name "com.apple.backboard.display.services"))
-		(require-not (global-name "com.apple.AccessibilityUIServer"))
 		(require-not (global-name "com.apple.uiintelligencesupport.agent"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.dt.xctestd.target"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
+		(require-not (global-name "com.apple.installcoordinationd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
+		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (local-name "com.apple.accessibility.gax.client"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
 		(require-not (xpc-service-name "com.apple.EventTimingProfileService"))
+		(require-not (global-name "com.apple.CARenderServer"))
+		(require-not (global-name "com.apple.AccessibilityUIServer"))
+		(require-not (global-name "UIASTNotificationCenter"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
