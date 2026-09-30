## findmybeaconingd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.nfcd.hwmanager"))
 		(require-not (global-name "com.apple.timed.xpc"))
+		(require-not (global-name "com.apple.nfcd.hwmanager"))
+		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
+		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.diagnosticd"))
```
