## diagnosticservicesd

> Group: ⬆️ Updated

```diff

 			SYS_sysctl
 			SYS_getumask
 			SYS_fgetattrlist
+			SYS_listxattr
 			SYS_fsctl
 			SYS_sysctlbyname
 			SYS_gettid

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
```
