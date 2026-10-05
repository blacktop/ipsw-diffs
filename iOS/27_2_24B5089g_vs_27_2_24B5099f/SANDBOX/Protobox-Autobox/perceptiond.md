## perceptiond

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.arkit.service.NutritionService"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.logd.admin"))
 		(require-not (global-name "com.apple.photoanalysisd"))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
```
