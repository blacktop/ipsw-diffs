## configd

> Group: ⬆️ Updated

```diff

 
 (allow default)
 
-(deny asr-parser-enter
-	(require-any
-		(require-not (asr-parser-domain ASR_DOMAIN_IMAGES))
-		(require-not (asr-parser-name "com.apple.imageio.png"))
-	)
-)
+(deny asr-parser-enter)
 
 (deny file-ioctl)
 (allow file-ioctl

 		(require-not (global-name "com.apple.captiveagent"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.corefollowup.agent"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.SystemConfiguration.DNSConfiguration"))
 		(require-not (global-name "com.apple.diagd"))

 		(require-not (global-name "com.apple.nesessionmanager"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.nesessionmanager.flow-divert-token"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.IPConfiguration.IPConfigurationHelper")

 
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
