## diagnosticscheckupd

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.HomePodDisplayService.xpc"))
 		(require-not (global-name "com.apple.bluetooth.xpc"))
 		(require-not (global-name "com.apple.corerepair"))
 		(require-not (global-name "com.apple.homed.xpc"))
```
