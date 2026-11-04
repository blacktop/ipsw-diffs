## lsd

> Group: ⬆️ Updated

```diff

 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (global-name "com.apple.coreservices.lsuseractivitymanager.xpc"))
+				(require-not (global-name "com.apple.timed.xpc"))
 				(require-not (global-name "com.apple.distributed_notifications@1v3"))
 				(require-not (global-name "com.apple.springboard.services"))
 				(require-not (global-name "com.apple.managedconfiguration.profiled.public"))

 				))
 				(require-not (xpc-service-name #"^com[.]apple[.].+[.]appremoval$"))
 				(require-not (global-name "com.apple.coreservices.lsuseractivitymanager.xpc"))
+				(require-not (global-name "com.apple.timed.xpc"))
 				(require-not (global-name "com.apple.distributed_notifications@1v3"))
 				(require-not (global-name "com.apple.springboard.services"))
 				(require-not (global-name "com.apple.managedconfiguration.profiled.public"))

 
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
