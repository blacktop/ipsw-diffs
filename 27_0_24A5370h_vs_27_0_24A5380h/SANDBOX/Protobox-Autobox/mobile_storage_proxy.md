## mobile_storage_proxy

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.nehelper"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.security.cryptexd"))
-		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.mobile.storage_mounter.xpc"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.security.cryptexd"))
+		(require-not (global-name "com.apple.mobile.storage_mounter.xpc"))
+		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (system-attribute developer-mode))
```
