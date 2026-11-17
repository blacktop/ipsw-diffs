## studentd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
+		(require-not (global-name "com.apple.private.corewifi-xpc"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.mobileactivationd"))

 	(ioctl-command
 		CTLIOCGINFO
 		SIOCGCONNINFO
+		SIOCGIFAGENTDATA
 		SIOCGIFCONSTRAINED
 		SIOCGIFDELEGATE
 		SIOCGIFEXPENSIVE
```
