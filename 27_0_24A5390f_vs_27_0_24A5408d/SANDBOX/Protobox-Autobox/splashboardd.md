## splashboardd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.fontservicesd"))
-		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (xpc-service-name "com.apple.Gestures.tracing.service.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.carkit.service"))
 		(require-not (global-name "com.apple.containermanagerd"))

 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
+		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
 		(require-not (global-name "com.apple.CarPlayApp.service"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))
```
