## assetsubscriptiond

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.uservault"))
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
-		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
-		(require-not (global-name "com.apple.userprofiles"))
 		(require-not (global-name "com.apple.biome.access.system"))
+		(require-not (global-name "com.apple.userprofiles"))
+		(require-not (global-name "com.apple.uservault"))
+		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
+		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (system-attribute developer-mode))
```
