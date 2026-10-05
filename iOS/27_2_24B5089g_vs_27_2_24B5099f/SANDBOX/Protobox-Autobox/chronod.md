## chronod

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.shortcuts.systemshortcutservice")
 			(global-name "com.apple.siri.VoiceShortcuts.xpc;")
 		))
+		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (global-name "com.apple.carkit.app.service"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))

 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.parsecd"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
```
