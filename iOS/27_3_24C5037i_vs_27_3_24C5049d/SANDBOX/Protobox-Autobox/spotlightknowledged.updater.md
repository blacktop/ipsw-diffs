## spotlightknowledged.updater

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.cascade.donationrequest.SensedUserContext.Pattern")
 			(global-name "com.apple.cascade.donationrequest.SensedUserContext.Person")
 			(global-name "com.apple.cascade.donationrequest.SensedUserContext.Place")
+			(global-name "com.apple.cascade.donationrequest.Siri.ConversationRecap")
 			(global-name "com.apple.cascade.donationrequest.Siri.Transcript.Turn")
 		))
 		(require-not (require-any

 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.ciphermld"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
-		(require-not (global-name "com.apple.generativesearch.server.indexing"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.generativesearch.server.salientpostings"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.cache_delete.public"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.TextUnderstanding.DocumentUnderstandingHarvesting"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.agentmanager.server.itemStatus"))
 		(require-not (global-name "com.apple.logd.admin"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.siri.uaf.subscription.service"))

 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (require-any
+			(global-name "com.apple.generativesearch.server.indexing")
+			(global-name "com.apple.generativesearch.server.salientpostings")
+		))
 		(require-not (global-name "com.apple.spotlight.SearchAgent"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
```
