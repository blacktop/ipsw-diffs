## wifianalyticsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.symptoms.symptomsd.managed_events"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.wifi.manager"))
+		(require-not (global-name "com.apple.modelmanager"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
 		(require-not (global-name "com.apple.usymptomsd"))

 		F_GETFL
 		F_SETFL
 		F_SETLKW
+		F_RDADVISE
 		F_NOCACHE
 		F_GETPATH
 		F_GETPROTECTIONCLASS

 
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
