## IDSCredentialsAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.identityservicesd.idquery.embedded.auth"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.identityservicesd.nsxpc"))
 		(require-not (global-name "com.apple.logd.events"))

 
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
