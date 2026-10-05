## announced

> Group: ⬆️ Updated

```diff

 (allow iokit-open-service
 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
+		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "IOSurfaceRoot")
 	)
 )

 		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
+		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (xpc-service-name "com.apple.appintents.LiveEntityService"))
 		(require-not (global-name "com.apple.commcenter.xpc"))
```
