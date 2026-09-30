## nanosystemsettingsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.coreduetd.context"))
 		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
+		(require-not (global-name "com.apple.carousel.backlightxpc"))
 		(require-not (global-name "com.apple.terminusd"))
 		(require-not (global-name "com.apple.chronoservices"))
 		(require-not (global-name "com.apple.logd.events"))

 		SYS_getattrlistbulk
 		SYS_clonefileat
 		SYS_openat
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
