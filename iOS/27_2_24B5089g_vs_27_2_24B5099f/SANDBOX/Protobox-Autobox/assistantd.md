## assistantd

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.assistant_data_sync")
 			(global-name "com.apple.assistant_service")
 			(global-name "com.apple.corespeech.corespeechd.attending.service")
-			(global-name "com.apple.corespeech.corespeechd.endpointer.service")
 			(global-name "com.apple.corespeech.corespeechd.rchandling.service")
 			(global-name "com.apple.corespeech.corespeechd.ssr.service")
 			(global-name "com.apple.corespeech.corespeechd.voiceid.xpc")

 		(require-not (global-name "com.apple.iconservices"))
 		(require-not (global-name "com.apple.relatived.status"))
 		(require-not (global-name "com.apple.lsd.xpc"))
+		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
 		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.tccd"))

 		(require-not (global-name "com.apple.linkd.transcript"))
 		(require-not (global-name "com.apple.userprofiles"))
 		(require-not (global-name "com.apple.assistant.cdm"))
+		(require-not (global-name "com.apple.corespeech.corespeechd.endpointer.service"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.siri.morphunassetsupdaterd"))

 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.conversationprovidermanager"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.generativeexperiences.agentSessionStore"))
 		(require-not (require-any
 			(global-name "com.apple.corespeech.speechmodeltraining.xpc")

 		(require-not (global-name "com.apple.DistributedTimers"))
 		(require-not (global-name "com.apple.contactsd.support"))
 		(require-not (global-name "com.apple.siri.uaf.service"))
+		(require-not (global-name "com.apple.mobilestoredemod"))
 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.breadboardservices"))

 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.medialibraryd.xpc"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
+		(require-not (global-name "com.apple.terminusd"))
 		(require-not (global-name "com.apple.audio.AudioQueueServer"))
 		(require-not (global-name "com.apple.intelligenceflow.toolbox"))
 		(require-not (global-name "com.apple.mediaanalysisd.service.public"))

 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.xpc.amstoold"))
 		(require-not (global-name "com.apple.parsecd"))
 		(require-not (global-name "com.apple.soundboardservices.server"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))

 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Topic.readOnly"))
 		(require-not (global-name "com.apple.calaccessd"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
+		(require-not (local-name "com.apple.assistant.contextprovider.com.apple.springboard"))
 		(require-not (local-name "com.apple.assistant.contextprovider.*"))
 		(require-not (xpc-service-name "com.apple.StreamingUnzipService"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
```
