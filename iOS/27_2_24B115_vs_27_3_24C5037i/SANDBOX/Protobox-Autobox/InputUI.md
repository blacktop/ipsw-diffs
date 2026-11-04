## InputUI

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.iconservices"))
 		(require-not (global-name "com.apple.dt.xctestd.remote.target"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
+		(require-not (global-name "com.apple.lsd.xpc"))
 		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
 		(require-not (global-name "com.apple.passd.account"))
 		(require-not (global-name "com.apple.hangtelemetryd"))

 		(require-not (global-name "com.apple.UserNotifications.OneTimeCodeService"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.photos.service"))
+		(require-not (global-name "com.apple.campo"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.passd.payment"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 5))
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
