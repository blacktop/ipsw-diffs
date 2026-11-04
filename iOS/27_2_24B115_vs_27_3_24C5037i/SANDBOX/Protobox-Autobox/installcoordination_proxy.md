## installcoordination_proxy

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.installcoordinationd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (xpc-service-name "com.apple.StreamingUnzipService"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (xpc-service-name "com.apple.StreamingUnzipService"))
+		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 
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
 			(require-not (mac-syscall-number 7))
-			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 5))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 2))
```
