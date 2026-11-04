## Managed Background Assets Helper Service

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (xpc-service-name "com.apple.backgroundassets.managed.helper.fetching.service"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
 	)

 			SYS_psynch_rw_unlock
 			SYS_psynch_rw_unlock2
 			SYS_psynch_cvclrprepost
+			SYS_iopolicysys
 			SYS_issetugid
 			SYS___pthread_kill
 			SYS___pthread_sigmask

 			SYS_change_fdguard_np
 			SYS_openat
 			SYS_renameat
+			SYS_faccessat
 			SYS_fstatat
 			SYS_fstatat64
 			SYS_mkdirat

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
