## AccessibilityUIServer

> Group: ⬆️ Updated

```diff

 		))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
 		(require-not (global-name "com.apple.siri.activation.service"))
+		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.UIKit.statusbarserver"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))

 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (xpc-service-name "com.apple.AXMediaUtilitiesService"))
 		(require-not (xpc-service-name "com.apple.audio.AUCrashHandlerService"))
 		(require-not (xpc-service-name "com.iflytek.inputime.keyboard"))
 		(require-not (xpc-service-name "com.apple.extensionkitservice"))
```
