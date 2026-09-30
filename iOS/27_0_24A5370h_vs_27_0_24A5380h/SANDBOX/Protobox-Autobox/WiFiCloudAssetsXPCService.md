## WiFiCloudAssetsXPCService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.research.adtcd"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.mediaremoted.xpc"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
-		(require-not (global-name "com.apple.nehelper"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.mediaremoted.xpc"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.research.adtcd"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
```
