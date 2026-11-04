## keychainsharingmessagingd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.security.kcsharing"))
 		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.security.kcsharing"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.diagnosticd"))

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 90 96)
-		(require-not (mac-policy-name "AMFI"))
+(with-filter (mac-policy-name "AMFI")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 96))
+			(require-not (mac-syscall-number 90))
+		)
 	)
 )
 (deny system-mac-syscall
```
