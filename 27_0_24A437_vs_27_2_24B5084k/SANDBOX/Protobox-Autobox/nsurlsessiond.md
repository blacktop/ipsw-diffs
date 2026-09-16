## nsurlsessiond

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
-		(require-not (xpc-service-name "com.apple.STExtractionService.privileged"))
+		(require-not (require-any
+			(xpc-service-name "com.apple.STExtractionService")
+			(xpc-service-name "com.apple.STExtractionService.privileged")
+		))
 		(require-not (xpc-service-name "com.apple.StreamingUnzipService"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))

 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (xpc-service-name "com.apple.STExtractionService"))
+		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.runningboard"))

 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.spaceattributiond"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
