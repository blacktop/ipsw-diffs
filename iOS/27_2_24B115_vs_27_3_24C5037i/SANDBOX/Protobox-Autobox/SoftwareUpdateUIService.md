## SoftwareUpdateUIService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.remoted"))
 		(require-not (global-name "com.apple.fontservicesd"))
+		(require-not (global-name "com.apple.bioconvenienced"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))

 		SYS_sendmsg
 		SYS_recvfrom
 		SYS_access
+		SYS_kill
 		SYS_crossarch_trap
 		SYS_getppid
 		SYS_dup

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 5))
+			(require-not (mac-syscall-number 4))
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
