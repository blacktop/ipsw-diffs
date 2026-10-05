## com.apple.photos.PCCService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.TapToRadarKit.service"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
