## securityd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.rtcreportingd"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
```
