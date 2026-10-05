## SiriHeadlessService

> Group: ⬆️ Updated

```diff

 		SYS_sysctl
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
+		SYS_setxattr
 		SYS_fsctl
 		SYS_shm_open
 		SYS_shm_unlink

 		F_GETPATH
 		F_OFD_SETLK
 		F_SETCONFINED
+		F_GETCONFINED
 		F_ADDFILESIGS_RETURN
 		F_CHECK_LV)
 )

 		(require-not (mac-policy-name "AMFI"))
 	)
 )
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 1)
+		(require-not (mac-policy-name "vnguard"))
+	)
+)
 (deny system-mac-syscall
 	(require-any
 		(require-not (mac-policy-name "Sandbox"))
```
