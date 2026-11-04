## online-auth-agent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.misagent"))
 		(require-not (xpc-service-name "com.apple.AppleVirtualPlatform.IdentityService"))
 		(require-not (xpc-service-name "com.apple.pvappidentityservice"))
+		(require-not (xpc-service-name "com.apple.BinaryAssetTagService"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon"))

 
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
