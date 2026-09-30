## safetyalertsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
```
