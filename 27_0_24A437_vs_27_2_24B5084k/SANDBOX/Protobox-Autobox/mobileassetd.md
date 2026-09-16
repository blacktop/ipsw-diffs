## mobileassetd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.nand_task_scheduler"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.nsurlsessiond"))
 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.erm.logging"))

 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.spaceattributiond"))
-		(require-not (xpc-service-name "com.apple.STExtractionService"))
+		(require-not (require-any
+			(xpc-service-name "com.apple.STExtractionService")
+			(xpc-service-name "com.apple.STExtractionService.privileged")
+		))
 		(require-not (xpc-service-name "com.apple.StreamingUnzipService"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.MADownloadServiceBackported")

 			(xpc-service-name "com.apple.MobileAsset.ManifestStorageService")
 		))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
-		(require-not (xpc-service-name "com.apple.STExtractionService.privileged"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
 	)

 	(ioctl-command
 		CTLIOCGINFO
 		SIOCGCONNINFO
+		SIOCGIFAGENTDATA
 		SIOCGIFCONSTRAINED
 		SIOCGIFDELEGATE
 		SIOCGIFEXPENSIVE
```
