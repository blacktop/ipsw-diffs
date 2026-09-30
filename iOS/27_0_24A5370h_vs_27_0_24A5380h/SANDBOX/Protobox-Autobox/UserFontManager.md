## UserFontManager

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.fontservicesd"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (xpc-service-name "com.apple.FontServices.UserFontServices"))
 		(require-not (global-name "com.apple.diagnosticd"))
```
