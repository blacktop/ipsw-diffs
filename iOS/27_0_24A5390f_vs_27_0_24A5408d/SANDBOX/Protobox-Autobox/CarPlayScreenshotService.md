## CarPlayScreenshotService

> Group: ⬆️ Updated

```diff

 
 (deny mach-lookup
 	(require-all
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
```
