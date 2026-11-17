## StatusKitAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.familycircled.sharing"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.homed.xpc"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		SYS_open_dprotected_np
 		SYS_openat_dprotected_np
 		SYS_getattrlist
+		SYS_setattrlist
 		SYS_fgetattrlist
 		SYS_getxattr
 		SYS_setxattr
```
