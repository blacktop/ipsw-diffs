## UsageTrackingAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.coreduetd.context"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.securityd"))

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
-				(require-not (global-name "com.apple.PowerManagement.control"))
 				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 				(require-not (global-name "com.apple.AppSSO.service-xpc"))

 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
-				(require-not (global-name "com.apple.PowerManagement.control"))
 				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 				(require-not (global-name "com.apple.AppSSO.service-xpc"))
```
