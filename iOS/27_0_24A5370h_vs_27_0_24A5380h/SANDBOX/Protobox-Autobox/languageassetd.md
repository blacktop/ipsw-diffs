## languageassetd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.mobileassetd"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.mobileassetd.v2"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.nehelper"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.fontservicesd"))
-		(require-not (global-name "com.apple.dnssd.service"))
-		(require-not (global-name "com.apple.translationd"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.fontservicesd"))
+		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.mobileassetd"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.translationd"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (xpc-service-name "com.apple.DictionaryServiceHelper"))
 		(require-not (global-name "com.apple.TextInput.rdt"))
```
