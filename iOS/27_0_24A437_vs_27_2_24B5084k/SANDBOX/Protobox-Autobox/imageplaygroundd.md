## imageplaygroundd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.biome.compute.publisher.service"))
 		(require-not (global-name "com.apple.posterboardservices.services"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.logd.events"))

 		SYS_fsetattrlist
 		SYS_getxattr
 		SYS_fgetxattr
+		SYS_setxattr
 		SYS_fsetxattr
 		SYS_listxattr
 		SYS_fsctl
```
