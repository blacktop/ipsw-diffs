## searchd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.TextInput.rdt"))
 		(require-not (global-name "com.apple.coreduetd.knowledge"))
 		(require-not (global-name "com.apple.trustd"))
+		(require-not (require-any
+			(global-name "com.apple.corespotlight.receiver.corespotlight")
+			(global-name "com.apple.corespotlight.receiver.images")
+			(global-name "com.apple.corespotlight.receiver.textunderstandingd")
+		))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.siri.context.service"))

 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.dmd.emergency-mode"))
+		(require-not (global-name "com.apple.spotlight.SearchAgent.test"))
 		(require-not (global-name "com.apple.suggestd.events"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))

 		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.DataDeliveryServices.AssetService"))
 		(require-not (global-name "com.apple.proactive.ActionPrediction.predictions"))
-		(require-not (require-any
-			(global-name "com.apple.corespotlight.receiver.corespotlight")
-			(global-name "com.apple.corespotlight.receiver.images")
-			(global-name "com.apple.corespotlight.receiver.textunderstandingd")
-			(global-name "com.apple.spotlight.SearchAgent.test")
-		))
 		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.linkd.autoShortcut"))
 		(require-not (global-name "com.apple.foundationmodels.languagemodelservice"))
 		(require-not (global-name "com.apple.intelligenceplatform.Knosis"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))

 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Contact"))
 		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
+		(require-not (global-name "com.apple.linkd.application-service"))
 		(require-not (global-name "com.apple.diagnosticpipeline.service"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.triald.namespace-management"))

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
