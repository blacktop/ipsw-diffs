## MusicUIService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.videotarget.xpc"))
 		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.DeviceAccess.xpc"))
 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))

 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.player.xpc"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
+		(require-not (global-name "com.apple.nesessionmanager"))
 		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
```
