## CarPlay

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.abm.helper.mobile"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
 		(require-not (global-name "com.apple.siri.activation.service"))
+		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.UIKit.statusbarserver"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))

 			(global-name "com.apple.caraccessoryframework.gatekeeper")
 			(global-name "com.apple.caraccessoryframework.nowplaying")
 		))
+		(require-not (global-name "com.apple.campo"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
```
