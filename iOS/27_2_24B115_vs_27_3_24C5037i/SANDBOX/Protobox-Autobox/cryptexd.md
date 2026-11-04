## cryptexd

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(iokit-registry-entry-class "AppleMobileFileIntegrityUserClient")
 		(iokit-registry-entry-class "IOHDIXControllerUserClient")
+		(iokit-registry-entry-class "Image4UserClient")
 	)
 )
 

 		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.remoted"))
 		(require-not (global-name "com.apple.installcoordinationd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (xpc-service-name "com.apple.diskimagescontroller"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (xpc-service-name "com.apple.diskimagescontroller"))
 		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
 	)

 
 (deny system-kas-info)
 
-(with-filter (mac-policy-name "Sandbox")
-	(deny system-mac-syscall
-		(require-all
-			(require-not (mac-syscall-number 67))
-			(require-not (mac-syscall-number 6))
-			(require-not (mac-syscall-number 4))
-			(require-not (mac-syscall-number 2))
-		)
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
