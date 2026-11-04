## textunderstandingd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.TextInput.preferences"))
 		(require-not (global-name "com.apple.coremedia.endpoint.xpc"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.feedbackd.centralized-feedback"))
 		(require-not (global-name "com.apple.suggestd.events"))
 		(require-not (require-any
 			(global-name "com.apple.iap2d.ExternalAccessory.distributednotification.server")

 		(require-not (global-name "com.apple.modelmanager"))
 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.linkd.autoShortcut"))
 		(require-not (global-name "com.apple.intelligenceplatform.Knosis"))
 		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.cache_delete.public"))

 		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Contact"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession.xpc"))
+		(require-not (global-name "com.apple.linkd.application-service"))
 		(require-not (global-name "com.apple.passd.library"))
 		(require-not (global-name "com.apple.diagnosticpipeline.service"))
 		(require-not (global-name "com.apple.FSEvents"))

 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.proactive.appDirectory"))
 		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.generativesearch.server.search"))
 		(require-not (global-name "com.apple.parsecd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.remindd"))

 		(require-not (global-name "com.apple.spotlight.SearchAgent"))
 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.exchangesyncd"))
+		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))

 
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
