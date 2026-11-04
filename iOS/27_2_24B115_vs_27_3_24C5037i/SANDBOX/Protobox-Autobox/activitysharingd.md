## activitysharingd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.cmfsyncagent.embedded.auth"))

 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.identityservicesd.nsxpc"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.imagent.embedded.auth"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.securityd"))

 
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
