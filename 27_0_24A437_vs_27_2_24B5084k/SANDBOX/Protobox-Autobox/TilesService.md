## TilesService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.nsurlsessiond.NSURLSessionProxyService"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.networkscored"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.dnssd.service"))

 		SYS_open_dprotected_np
 		SYS_openat_dprotected_np
 		SYS_getattrlist
+		SYS_fgetattrlist
 		SYS_fsetattrlist
 		SYS_getxattr
 		SYS_fgetxattr
```
