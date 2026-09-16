## communicationtrustd

> Group: ⬆️ Updated

```diff

 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.cmfsyncagent.embedded.auth"))
 		(require-not (global-name "com.apple.privacyaccountingd"))

 			SYS_writev
 			SYS_sendto
 			SYS_mkdir
+			SYS_rmdir
 			SYS_pread
 			SYS_pwrite
 			SYS_kdebug_typefilter

 			SYS_fgetattrlist
 			SYS_fsetattrlist
 			SYS_fgetxattr
+			SYS_listxattr
 			SYS_flistxattr
 			SYS_fsctl
 			SYS_sysctlbyname

 			SYS_memorystatus_control
 			SYS_guarded_open_np
 			SYS_openat
+			SYS_renameat
 			SYS_faccessat
 			SYS_fstatat
 			SYS_fstatat64
```
