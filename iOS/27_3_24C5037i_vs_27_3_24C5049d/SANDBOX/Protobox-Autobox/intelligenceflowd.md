## intelligenceflowd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
 		(require-not (xpc-service-name "com.apple.appintents.LiveEntityService"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (require-any
-			(global-name "com.apple.generativeexperiences.ExternalPartnerCredentialStorage")
-			(global-name "com.apple.generativeexperiences.ExternalProviderService")
-		))
+		(require-not (global-name "com.apple.generativeexperiences.ExternalProviderService"))
 		(require-not (global-name "com.apple.TextInput.rdt"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc"))
 		(require-not (global-name "com.apple.translation.text"))

 		(require-not (global-name "com.apple.powerexperienced.resourceusage"))
 		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
+		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callprovidermanager"))
 		(require-not (global-name "com.apple.siriknowledged"))
 		(require-not (global-name "com.apple.proactive.ActionPrediction.predictions"))
 		(require-not (global-name "com.apple.powerd.lowpowermode"))
+		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
 		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.siri.sirireaderd"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))

 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.generativeexperiences.agentSessionStore"))
+		(require-not (require-any
+			(global-name "com.apple.ContextualUnderstanding.memory-retrieval")
+			(global-name "com.apple.products.productsd")
+			(global-name "com.apple.siri.flowtools_xpc_service")
+		))
 		(require-not (require-any
 			(global-name "com.apple.mediasetupd.server")
 			(global-name "com.apple.siri.orchestration.sirixagent")

 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.siriactionsd.xpc"))
 		(require-not (global-name "com.apple.contactsd.support"))
-		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
+		(require-not (global-name "com.apple.corespeech.corespeechd.xpc"))
 		(require-not (global-name "com.apple.generativeexperiences.agentMediaStore"))
 		(require-not (global-name "com.apple.adpt.corvidiad.xpc"))
 		(require-not (global-name "com.apple.adid"))
 		(require-not (local-name "com.apple.iphone.axserver"))
 		(require-not (global-name "com.apple.breadboardservices"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
-		(require-not (global-name "com.apple.audio.AURemoteIOServer"))
+		(require-not (global-name "com.apple.generativeexperiences.ExternalPartnerCredentialStorage"))
 		(require-not (global-name "com.apple.mediaexperience.systemmediacastingcontroller.xpc"))
 		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
 		(require-not (global-name "com.apple.iphone.axserver-systemwide"))

 		(require-not (global-name "com.apple.diagnosticpipeline.service"))
 		(require-not (global-name "com.apple.assistant.audio-session-event"))
 		(require-not (global-name "com.apple.FSEvents"))
-		(require-not (require-any
-			(global-name "com.apple.products.productsd")
-			(global-name "com.apple.siri.flowtools_xpc_service")
-		))
+		(require-not (global-name "com.apple.audio.AURemoteIOServer"))
 		(require-not (global-name "com.apple.triald.namespace-management"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled"))
 		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))

 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.intelligenceflow.contextTool"))
 		(require-not (global-name "com.apple.datamigrator"))
-		(require-not (global-name "com.apple.corespeech.corespeechd.xpc"))
+		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
 		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))

 		SYS_setattrlist
 		SYS_fgetattrlist
 		SYS_fsetattrlist
+		SYS_poll
 		SYS_getxattr
 		SYS_fgetxattr
 		SYS_setxattr
```
