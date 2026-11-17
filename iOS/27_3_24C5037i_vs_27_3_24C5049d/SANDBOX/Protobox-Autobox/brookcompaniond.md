## brookcompaniond

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.biome.compute.source"))
 		(require-not (global-name "com.apple.coreduetd.knowledge"))

 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.routined.registration"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (system-attribute developer-mode))
```
