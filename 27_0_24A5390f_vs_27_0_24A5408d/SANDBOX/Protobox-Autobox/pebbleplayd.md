## pebbleplayd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (global-name "com.apple.mobile.installd"))
```
