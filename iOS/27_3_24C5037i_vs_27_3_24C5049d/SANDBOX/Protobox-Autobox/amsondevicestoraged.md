## amsondevicestoraged

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.xpc.amstoold"))
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (system-attribute developer-mode))

 			SYS_fstatat
 			SYS_fstatat64
 			SYS_mkdirat
+			SYS_thread_selfusage
 			SYS_guarded_open_dprotected_np
 			SYS_guarded_write_np
 			SYS_guarded_pwrite_np
```
