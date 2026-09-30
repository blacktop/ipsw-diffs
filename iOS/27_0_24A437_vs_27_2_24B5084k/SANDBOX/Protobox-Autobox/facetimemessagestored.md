## facetimemessagestored

> Group: ⬆️ Updated

```diff

 
 (allow default)
 
+(deny asr-parser-enter
+	(require-any
+		(require-not (asr-parser-domain ASR_DOMAIN_IMAGES))
+		(require-not (asr-parser-name "com.apple.imageio.atx"))
+	)
+)
+
 (deny file-ioctl)
 (allow file-ioctl
 	(ioctl-command (_IO "h" 4))

 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.TextUnderstanding.process"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))

 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.communication"))
+		(require-not (global-name "com.apple.identityservicesd.nsxpc"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.logd.events"))
```
