## CheckerBoard

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.TextInput.rdt"))
+		(require-not (global-name "com.apple.VoiceOverTouch"))
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc"))
 		(require-not (global-name "com.apple.bird.token"))

 		(require-not (global-name "com.apple.UIKit.OverlayUI.services"))
 		(require-not (global-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.bluetooth.xpc"))
+		(require-not (global-name "com.apple.accessibility.axassetsd.service"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.private.corewifi.internal-xpc"))
+		(require-not (global-name "com.apple.server.bluetooth.general.xpc"))
+		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
 		(require-not (global-name "com.apple.dasd.end-prewarm"))
 		(require-not (global-name "com.apple.wifi.manager"))
 		(require-not (global-name "com.apple.sharing.sharesheet"))

 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.figmetriceventtimeline.xpc"))
+		(require-not (global-name "com.apple.mediaremoted.xpc"))
+		(require-not (global-name "com.apple.accessibility.heard"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))
 		(require-not (global-name "com.apple.runningboard"))

 		(require-not (global-name "com.apple.misagent"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (global-name "com.apple.lsd.open"))
+		(require-not (global-name "com.apple.contactsd"))
 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
+		(require-not (global-name "com.apple.AccessibilityUIServer"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		SYS_munlock
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_setattrlist
 		SYS_fgetattrlist
```
