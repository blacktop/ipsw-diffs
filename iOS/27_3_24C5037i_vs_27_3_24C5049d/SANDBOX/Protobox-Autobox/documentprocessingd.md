## documentprocessingd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.spotlight.SearchAgent.test"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
-		(require-not (global-name "com.apple.generativesearch.server.indexing"))
+		(require-not (require-any
+			(global-name "com.apple.generativesearch.server.indexing")
+			(global-name "com.apple.generativesearch.server.salientpostings")
+		))
+		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
+		(require-not (global-name "com.apple.cascade.donationrequest.Messages.MessageChunk"))
 		(require-not (global-name "com.apple.cache_delete.public"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (global-name "com.apple.agentmanager.server.itemStatus"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.spotlight.SearchAgent"))
-		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (system-attribute developer-mode))
```
