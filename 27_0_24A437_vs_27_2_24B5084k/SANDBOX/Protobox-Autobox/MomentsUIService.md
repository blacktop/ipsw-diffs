## MomentsUIService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.chrono.widgetcenterconnection"))
 		(require-not (global-name "com.apple.usernotifications.remotenotificationservice"))
+		(require-not (require-any
+			(global-name "com.apple.UIKit.MainMenuStateDelegate")
+			(global-name "com.apple.uikit.viewservice.mainmenustatedelegate")
+		))
 		(require-not (global-name "com.apple.coremedia.admin"))
 		(require-not (global-name "com.apple.uikit.viewservice.com.apple.SafariViewService"))
 		(require-not (global-name "com.apple.accessibility.gax.backboard"))

 		(require-not (global-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc"))
+		(require-not (xpc-service-name "com.apple.MapKit.SnapshotService"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.sharing.sharesheet"))

 		(require-not (global-name "com.apple.backboard.display.services"))
 		(require-not (global-name "com.apple.generativeexperiences.textcomposition"))
 		(require-not (global-name "com.apple.uiintelligencesupport.agent"))
+		(require-not (global-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.pasteboard.pasted"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))

 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.runningboard"))
-		(require-not (xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner"))
+		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.TextInput.image-cache-server"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc"))
 		(require-not (global-name "com.apple.iohideventsystem"))

 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
 		(require-not (global-name "com.apple.stickers.api"))
 		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (xpc-service-name "com.apple.MapKit.SnapshotService"))
+		(require-not (xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.DragUI.druid.source"))
 		(require-not (global-name "com.apple.adid"))

 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.EventTimingProfileService"))
-		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.AccessibilityUIServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "UIASTNotificationCenter"))
```
