## corespeechd

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.homepodaccessorysettings.server")
 			(global-name "com.apple.siri.activation.horseman")
 		))
+		(require-not (global-name "com.apple.agentboardd.input"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.nsurlsessiond.NSURLSessionProxyService"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))

 
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
