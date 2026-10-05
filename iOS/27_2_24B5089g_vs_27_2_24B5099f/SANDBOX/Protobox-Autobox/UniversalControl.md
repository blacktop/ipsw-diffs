## UniversalControl

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
+		(require-not (xpc-service-name "com.apple.EventTimingProfileService"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.DragUI.druid.destination"))
 		(require-not (global-name "com.apple.CARenderServer"))
```
