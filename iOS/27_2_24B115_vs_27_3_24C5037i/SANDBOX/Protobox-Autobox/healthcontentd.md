## healthcontentd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.xpc.amstoold"))
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.FileCoordination"))
+		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 			SYS_open_dprotected_np
 			SYS_openat_dprotected_np
 			SYS_fgetattrlist
+			SYS_fsetattrlist
 			SYS_fgetxattr
 			SYS_listxattr
+			SYS_flistxattr
 			SYS_fsctl
 			SYS_sysctlbyname
 			SYS_gettid

 		F_SETFL
 		F_SETLKW
 		F_RDADVISE
+		F_NOCACHE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 80))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(with-filter (mac-policy-name "vnguard")
+	(deny system-mac-syscall
+		(require-not (mac-syscall-number 1))
 	)
 )
 (deny system-mac-syscall
```
