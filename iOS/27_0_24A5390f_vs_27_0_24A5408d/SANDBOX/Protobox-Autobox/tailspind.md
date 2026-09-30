## tailspind

> Group: ⬆️ Updated

```diff

 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (xpc-service-name "com.apple.tailspin.symbolicationserver"))
 		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
+		(require-not (xpc-service-name "com.apple.tailspin.augmentationserver"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
