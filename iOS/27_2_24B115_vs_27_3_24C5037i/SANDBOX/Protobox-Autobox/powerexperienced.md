## powerexperienced

> Group: ⬆️ Updated

```diff

 		SYS_geteuid
 		SYS_sendmsg
 		SYS_access
+		SYS_kill
 		SYS_crossarch_trap
 		SYS_dup
 		SYS_getegid

 
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
