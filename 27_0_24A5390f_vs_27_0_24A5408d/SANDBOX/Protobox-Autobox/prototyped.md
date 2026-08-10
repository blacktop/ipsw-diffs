## prototyped

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
+		(require-not (local-name "com.apple.accessibility.gax.client"))
 		(require-not (xpc-service-name "com.apple.TranslationUIServices.TranslationUIService"))
 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))

 		SYS_munlock
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_setattrlist
 		SYS_fgetattrlist
```
