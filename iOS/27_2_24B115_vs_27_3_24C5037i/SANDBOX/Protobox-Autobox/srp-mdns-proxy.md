## srp-mdns-proxy

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.mDNSResponder_Helper"))
 		(require-not (global-name "com.apple.mDNSResponder.control"))
 		(require-not (global-name "com.apple.wpantund.xpc"))

 		SYS___pthread_fchdir
 		SYS_bsdthread_create
 		SYS_bsdthread_terminate
+		SYS_kqueue
 		SYS_kevent
 		SYS_bsdthread_register
 		SYS_workq_open

 
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 90 96)
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 90)
 		(require-not (mac-policy-name "AMFI"))
 	)
 )
```
