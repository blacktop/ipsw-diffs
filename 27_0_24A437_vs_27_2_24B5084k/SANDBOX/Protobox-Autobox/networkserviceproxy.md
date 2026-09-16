## networkserviceproxy

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.networkd_privileged"))
 		(require-not (global-name "com.apple.rtcreportingd"))
 		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.private.corewifi-xpc"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
```
