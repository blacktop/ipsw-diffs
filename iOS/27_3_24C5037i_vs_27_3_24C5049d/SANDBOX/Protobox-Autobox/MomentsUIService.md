## MomentsUIService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.hangtracerd"))
 		(require-not (global-name "com.apple.healthd.server"))
-		(require-not (global-name "com.apple.rti-screencontinuity"))
+		(require-not (require-any
+			(global-name "com.apple.remote-text-editing-legacy")
+			(global-name "com.apple.rti-screencontinuity")
+			(global-name "com.apple.sharing.remote-text-editing")
+		))
 		(require-not (global-name "com.apple.assistant.settings"))
 		(require-not (global-name "com.apple.UIKit.KeyboardManagement.hosted"))
 		(require-not (require-any

 		(require-not (global-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc"))
-		(require-not (xpc-service-name "com.apple.MapKit.SnapshotService"))
+		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.sharing.sharesheet"))
-		(require-not (require-any
-			(global-name "com.apple.remote-text-editing-legacy")
-			(global-name "com.apple.sharing.remote-text-editing")
-		))
+		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.Music.MPMusicPlayerControllerInternal"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))

 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.runningboard"))
-		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
+		(require-not (xpc-service-name "com.apple.EventTimingProfileService"))
 		(require-not (global-name "com.apple.TextInput.image-cache-server"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc"))
 		(require-not (global-name "com.apple.iohideventsystem"))

 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
 		(require-not (global-name "com.apple.stickers.api"))
 		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner"))
+		(require-not (xpc-service-name "com.apple.MapKit.SnapshotService"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.DragUI.druid.source"))
 		(require-not (global-name "com.apple.adid"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.rti-stagertool"))
+		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
 		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
 		(require-not (global-name "com.apple.medialibraryd.xpc"))
 		(require-not (global-name "com.apple.mediaanalysisd.service.public"))

 		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
-		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
+		(require-not (xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner"))
 		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.player.xpc"))

 		(require-not (xpc-service-name "com.apple.siri.context.service"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
-		(require-not (xpc-service-name "com.apple.EventTimingProfileService"))
 		(require-not (global-name "UIASTNotificationCenter"))
 		(require-not (global-name "PurplePPTServer"))
 		(require-not (system-attribute developer-mode))
```
