## Managed Background Assets Helper Service

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.appstored.xpc"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
-		(require-not (global-name "com.apple.xpc.amstoold"))
-		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.adid"))
-		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (global-name "com.apple.appstored.xpc"))
+		(require-not (global-name "com.apple.xpc.amstoold"))
+		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (xpc-service-name "com.apple.backgroundassets.managed.helper.fetching.service"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
```
