## smbclientd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.FileProvider"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		SYS_psynch_rw_unlock
 		SYS_psynch_rw_unlock2
 		SYS_psynch_cvclrprepost
+		SYS_iopolicysys
 		SYS_issetugid
 		SYS___pthread_kill
 		SYS___pthread_sigmask

 
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
