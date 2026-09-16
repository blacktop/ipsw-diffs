## InputUI

> Group: ⬆️ Updated

```diff

 			(global-name "com.swiftkey.SwiftKeyApp.Keyboard.viewservice")
 		))
 		(require-not (global-name "com.apple.TextInput.emoji"))
+		(require-not (global-name "com.apple.dictationengined"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 		(require-not (local-name "com.apple.iphone.axserver"))
 		(require-not (global-name "com.apple.callkit.callcontrollerhost"))

 		(require-not (global-name "com.apple.passd.account"))
 		(require-not (global-name "com.apple.hangtelemetryd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (require-any
+			(global-name "com.apple.UIKit.MainMenuStateDelegate")
+			(global-name "com.apple.uikit.viewservice.mainmenustatedelegate")
+		))
 		(require-not (global-name "com.apple.uikit.viewservice.com.apple.SafariViewService"))
 		(require-not (global-name "com.apple.accessibility.gax.backboard"))
 		(require-not (global-name "com.apple.assistant.cdm"))

 			(global-name "com.apple.inputservice.keyboarduis")
 			(global-name "com.apple.inputservice.keyboarduiz")
 		))
+		(require-not (global-name "com.apple.quicklook.ThumbnailsAgent"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.DocumentManagerUICore.Service.viewservice"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
 		(require-not (global-name "com.apple.AuthenticationServices.AutoFill"))
-		(require-not (global-name "com.apple.quicklook.ThumbnailsAgent"))
 		(require-not (global-name "com.apple.spotlight.SearchAgent"))
+		(require-not (global-name "com.apple.handwritingd.pkanalytics"))
 		(require-not (global-name "com.apple.generativeexperiences.externaltextcomposition"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.handwritingd.remoterecognition"))

 		(require-not (global-name "com.apple.backboard.display.services"))
 		(require-not (global-name "com.apple.generativeexperiences.textcomposition"))
 		(require-not (global-name "com.apple.uiintelligencesupport.agent"))
+		(require-not (global-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.pasteboard.pasted"))
 		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))

 		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.dmd.policy"))
-		(require-not (global-name "com.apple.handwritingd.pkanalytics"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))
 		(require-not (global-name "com.apple.AccessibilityUIServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
```
