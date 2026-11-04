## uarphidd

> Group: ⬆️ Updated

```diff

 			SYS_getumask
 			SYS_open_dprotected_np
 			SYS_openat_dprotected_np
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
