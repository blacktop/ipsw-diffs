## apple-cloud-enhanced-security

> Group: ⬆️ Updated

```diff

 	(require-any
 		(extension "com.apple.security.exception.mach-lookup.global-name")
 		(extension "com.apple.security.exception.mach-lookup.local-name")
-		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.cloudos.cb_bridged")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.logd.events")

 	(with no-report)
 	(require-any
 		(global-name "com.apple.CARenderServer")
+		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.audio.AudioComponentRegistrar")
 		(global-name "com.apple.coremedia.mediaparserd.utilities")
 		(global-name "com.apple.mobileassetd.v2")
```
