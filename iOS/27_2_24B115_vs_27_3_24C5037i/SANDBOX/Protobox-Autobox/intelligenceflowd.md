## intelligenceflowd

> Group: ⬆️ Updated

```diff

 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.linkd.registry"))
+		(require-not (global-name "com.apple.webinspector"))
 		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.managedappdistributiond.xpc"))

 		))
 		(require-not (global-name "com.apple.TextInput.rdt"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc"))
+		(require-not (global-name "com.apple.translation.text"))
 		(require-not (global-name "com.apple.appprotectiond.guard"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.mobilemail.services.xpc"))

 		(require-not (xpc-service-name "com.apple.SpeechRecognitionCore.brokerd"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (xpc-service-name "com.apple.textkit.nsattributedstringagent"))
+		(require-not (global-name "com.apple.lsd.xpc"))
 		(require-not (global-name "com.apple.TapToRadarKit.service"))
 		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))

 		(require-not (global-name "com.apple.bird"))
 		(require-not (global-name "com.apple.SiriVOXService.client"))
 		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.itunescloudd.tcchelper"))
 		(require-not (global-name "com.apple.searchd"))
 		(require-not (global-name "com.apple.backboardd.virtualframebuffer"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.backlightd"))
 		(require-not (global-name "com.apple.uservault"))
+		(require-not (global-name "com.apple.icloud.searchpartyd.beaconmanager.simplebeacon"))
 		(require-not (global-name "com.apple.suggestd.events"))
 		(require-not (global-name "com.apple.intelligentroutingd.xpc.media"))
 		(require-not (global-name "com.apple.perceptiond.peripheralSensing"))
 		(require-not (global-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (require-any
-			(global-name "com.apple.mediasetupd.server")
-			(global-name "com.apple.siri.localspeechrecognitionbridge.xpc")
-			(global-name "com.apple.siri.orchestration.sirixagent")
-		))
+		(require-not (global-name "com.apple.siri.localspeechrecognitionbridge.xpc"))
 		(require-not (global-name "com.apple.entitykit.service"))
 		(require-not (global-name "com.apple.intelligenceflow.context"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.assistant.multiuser.service"))
+		(require-not (global-name "com.apple.findmy.findmylocate.locationservice"))
 		(require-not (global-name "com.apple.powerexperienced.resourceusage"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.siriknowledged"))
 		(require-not (global-name "com.apple.proactive.ActionPrediction.predictions"))

 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
 		(require-not (global-name "com.apple.intelligenceplatform.Knosis"))
 		(require-not (global-name "com.apple.backboard.display.services"))
+		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.intelligenceplatform.InternalBiome"))
 		(require-not (global-name "com.apple.carousel.connectionstatusservice"))
 		(require-not (global-name "com.apple.springboard.backgroundappservices"))

 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))
+		(require-not (global-name "com.apple.findmy.findmylocate.settings"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.email.maild"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))

 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.generativeexperiences.agentSessionStore"))
-		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
+		(require-not (require-any
+			(global-name "com.apple.mediasetupd.server")
+			(global-name "com.apple.siri.orchestration.sirixagent")
+		))
 		(require-not (global-name "com.apple.replayd"))
 		(require-not (global-name "com.apple.webprivacyd"))
 		(require-not (global-name "com.apple.mediaanalysisd.embeddingstore"))

 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.siriactionsd.xpc"))
 		(require-not (global-name "com.apple.contactsd.support"))
-		(require-not (global-name "com.apple.corespeech.corespeechd.xpc"))
+		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
 		(require-not (global-name "com.apple.generativeexperiences.agentMediaStore"))
 		(require-not (global-name "com.apple.adpt.corvidiad.xpc"))
 		(require-not (global-name "com.apple.adid"))

 		))
 		(require-not (global-name "com.apple.triald.namespace-management"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled"))
+		(require-not (global-name "com.apple.findmy.findmylocate.fenceservice"))
 		(require-not (global-name "com.apple.donotdisturb.service.non-launching"))
 		(require-not (global-name "com.apple.proactive.appDirectory"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Topic.readOnly"))

 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.intelligenceflow.contextTool"))
 		(require-not (global-name "com.apple.datamigrator"))
-		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
+		(require-not (global-name "com.apple.corespeech.corespeechd.xpc"))
 		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.siri.orchestration.intelligencesession"))
 		(require-not (global-name "com.apple.dmd.policy"))
+		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))
 		(require-not (system-attribute developer-mode))
 	)

 		SYS_kdebug_trace_string
 		SYS_kdebug_trace64
 		SYS_kdebug_trace
+		SYS_seteuid
 		SYS_sigreturn
 		SYS_stat
 		SYS_fstat

 		F_SETFD
 		F_GETFL
 		F_SETFL
+		F_PREALLOCATE
 		F_RDADVISE
 		F_RDAHEAD
 		F_NOCACHE

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 67))
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
