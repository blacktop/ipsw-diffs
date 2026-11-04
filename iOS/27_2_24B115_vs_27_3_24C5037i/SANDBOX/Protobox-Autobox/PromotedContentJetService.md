## PromotedContentJetService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (xpc-service-name "com.apple.JetTracingSupport.JetTracingService"))
 		(require-not (global-name "com.apple.FileCoordination"))
+		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		SYS_read
 		SYS_write
 		SYS_open
+		SYS_close
 		SYS_getfsstat
 		SYS_getpid
 		SYS_getuid

 		SYS_sigaltstack
 		SYS_readlink
 		SYS_umask
+		SYS_munmap
 		SYS_mprotect
 		SYS_dup2
 		SYS_fcntl

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
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
