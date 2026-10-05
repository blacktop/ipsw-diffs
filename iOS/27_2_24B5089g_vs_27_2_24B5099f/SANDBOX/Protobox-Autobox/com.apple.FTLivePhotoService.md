## com.apple.FTLivePhotoService

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.videoconference.camera"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (require-any
 			(global-name "com.apple.facetimemessagestored.videomessaging")
 			(global-name "com.apple.telephonyutilities.callservicesdaemon.reportingcontroller")
```
