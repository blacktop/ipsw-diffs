## spotlightknowledged

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.FileProvider"))
-		(require-not (global-name "com.apple.corepersonalization.server.graphEmbedding"))
+		(require-not (require-any
+			(global-name "com.apple.corepersonalization.server.graphEmbedding")
+			(global-name "com.apple.spotlight.IndexAgent.test")
+		))
 		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))

 			(global-name "com.apple.corespotlight.receiver.corespotlight")
 			(global-name "com.apple.corespotlight.receiver.images")
 			(global-name "com.apple.corespotlight.receiver.textunderstandingd")
-			(global-name "com.apple.spotlight.SearchAgent.test")
 		))
 		(require-not (require-any
 			(global-name "com.apple.cascade.donationrequest.*")
 			(global-name "com.apple.searchd.test")
-			(global-name "com.apple.spotlight.IndexAgent.test")
 			(global-name "com.apple.suggestd.mail")
 			(global-name "com.apple.suggestd.messages")
 			(global-name "com.apple.suggestd.spotlightknowledged")
 		))
-		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (global-name "com.apple.spotlight.SearchAgent.test"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.corespotlight.scheduled.receiver.textunderstandingd"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))

 		(require-not (global-name "com.apple.generativesearch.server.indexing"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.corespotlight.powerlog"))
+		(require-not (global-name "com.apple.generativesearch.server.salientpostings"))
 		(require-not (global-name "com.apple.spotlight.SearchAgent"))
 		(require-not (global-name "com.apple.cache_delete.public"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))

 		(require-not (global-name "com.apple.TextUnderstanding.DocumentUnderstandingHarvesting"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
 		(require-not (global-name "com.apple.spotlight.resources.assets"))
 		(require-not (global-name "com.apple.gputools.producer"))
 		(require-not (global-name "com.apple.logd.admin"))
-		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.coreduetd.context"))
 		(require-not (global-name "com.apple.diagd"))

 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.gputools.service"))
 		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.research.adtcd"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.ERFoundationExtensionDaemon"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(with-filter (mac-policy-name "vnguard")
+	(deny system-mac-syscall
+		(require-not (mac-syscall-number 1))
 	)
 )
 (deny system-mac-syscall
```
