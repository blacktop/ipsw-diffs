## Family

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.UIKit.OverlayUI.services"))
 		(require-not (global-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (require-any
+			(global-name "com.apple.ScreenTimeAgent.settings")
+			(global-name "com.apple.ak.puffin.xpc")
+			(global-name "com.apple.coremedia.sts")
+			(global-name "com.apple.uikit.viewservice.com.apple.family")
+		))
 		(require-not (require-any
 			(global-name "com.apple.remote-text-editing-legacy")
 			(global-name "com.apple.sharing.remote-text-editing")

 		(require-not (global-name "com.apple.ak.anisette.xpc"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.formatreader.xpc"))
 		(require-not (global-name "com.apple.networkscored"))
-		(require-not (require-any
-			(global-name "com.apple.ScreenTimeAgent.settings")
-			(global-name "com.apple.ScreenTimeSettingsAgent.public")
-			(global-name "com.apple.ak.puffin.xpc")
-			(global-name "com.apple.coremedia.sts")
-			(global-name "com.apple.uikit.viewservice.com.apple.family")
-		))
 		(require-not (require-any
 			(global-name "com.apple.appprotectiond.extensioninfo")
 			(global-name "com.apple.appprotectiond.extensionmonitor")

 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
 		(require-not (global-name "com.apple.coreservices.lsuseractivitymanager.xpc"))
 		(require-not (global-name "com.apple.biometrickitd"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.DataDeliveryServices.AssetService"))
 		(require-not (global-name "com.apple.sharing.sharesheet"))
 		(require-not (global-name "com.apple.proactive.ActionPrediction.predictions"))

 		(require-not (global-name "com.apple.accessibility.heard"))
 		(require-not (global-name "com.apple.synapse.backlink-service"))
 		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.siri.VoiceShortcuts.xpc"))
 		(require-not (global-name "com.apple.awdd"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.setup"))
 		(require-not (global-name "com.apple.AuthenticationServicesCore.AuthenticationServicesAgent"))
 		(require-not (global-name "com.apple.biome.compute.publisher.service"))
+		(require-not (global-name "com.apple.ScreenTimeSettingsAgent.public"))
 		(require-not (global-name "com.apple.coreidvd.digital-presentment.xpc"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.audio.AudioUnitServer"))
```
