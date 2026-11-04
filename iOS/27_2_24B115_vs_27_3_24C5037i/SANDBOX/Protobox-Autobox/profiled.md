## profiled

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.springboard.services"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
+		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.cache_delete.public"))
 		(require-not (global-name "com.apple.fontservicesd"))
+		(require-not (global-name "com.apple.bioconvenienced"))
 		(require-not (global-name "com.apple.photos.service"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))

 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.pearld"))
 		(require-not (global-name "com.apple.corefollowup.agent"))
+		(require-not (global-name "com.apple.deviceconfigurationd.consumer"))
 		(require-not (global-name "com.apple.managedconfiguration.mdmdservice"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
