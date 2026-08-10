## mediaplaybackd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.HearingModeService"))
 		(require-not (global-name "com.apple.gputools.service"))
+		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.player.xpc"))
```
