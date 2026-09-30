## MusicUIService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (global-name "com.apple.contactsd"))
+		(require-not (local-name "com.apple.accessibility.gax.client"))
 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
