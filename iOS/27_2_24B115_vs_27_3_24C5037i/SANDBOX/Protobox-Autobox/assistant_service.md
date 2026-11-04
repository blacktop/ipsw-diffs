## assistant_service

> Group: ⬆️ Updated

```diff

 		(require-not (require-any
 			(global-name "com.apple.CascadeSetsDifferentialUpdateService")
 			(global-name "com.apple.TextUnderstanding.SmartReplies.Inference")
+			(global-name "com.apple.agentboardd.telemetry")
 			(global-name "com.apple.assistant.flow_service")
 			(global-name "com.apple.assistant.notification_service")
 			(global-name "com.apple.itunescloud.delegate-account-store")
 			(global-name "com.apple.itunescloud.delegation-provider")
 			(global-name "com.apple.maps.destinationd.predictions")
+			(global-name "com.apple.otlpd")
 			(global-name "com.apple.proactive.PersonalizationPortrait.Topic.readWrite")
 			(global-name "com.apple.relevanced.ConsiderateVolume")
 			(global-name "com.apple.searchparty.btfindingsession")

 		(require-not (global-name "com.apple.ak.auth.xpc"))
 		(require-not (global-name "com.apple.commandandcontrol"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
+		(require-not (global-name "com.apple.inputanalyticsd"))
 		(require-not (global-name "com.apple.appprotectiond.guard"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))

 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.itunescloudd.tcchelper"))
+		(require-not (global-name "com.apple.findmy.findmylocate.friendshipservice"))
 		(require-not (global-name "com.apple.siri.morphunassetsupdaterd"))
 		(require-not (global-name "com.apple.dmd.emergency-mode"))
 		(require-not (global-name "com.apple.accessibility.AXSpringBoardServer"))

 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.accessibility.heard"))
 		(require-not (global-name "com.apple.caraccessoryframework.cardata"))
+		(require-not (global-name "com.apple.synapse.backlink-service"))
 		(require-not (global-name "com.apple.xpc.amstreatmentstoreservice"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.siri.VoiceShortcuts.xpc"))
 		(require-not (global-name "com.apple.accessibility.AXVoiceOverServer"))
 		(require-not (global-name "com.apple.awdd"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))
+		(require-not (global-name "com.apple.findmy.findmylocate.settings"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.facetimemessagestored.service"))
 		(require-not (global-name "com.apple.runningboard"))

 		(require-not (global-name "com.apple.icloud.searchpartyd.securelocations"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
-		(require-not (require-any
-			(global-name "com.apple.findmy.findmylocate.friendshipservice")
-			(global-name "com.apple.findmy.findmylocate.settings")
-		))
 		(require-not (global-name "com.apple.pearld"))
 		(require-not (global-name "com.apple.DistributedTimers"))
 		(require-not (global-name "com.apple.contactsd.support"))

 		(require-not (global-name "com.apple.AppDistributionLaunchAngel"))
 		(require-not (global-name "com.apple.Maps.xpc.SharedTrip"))
 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
+		(require-not (global-name "com.apple.lsd.advertisingidentifiers"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.breadboardservices"))
 		(require-not (global-name "com.apple.siri.client_lite"))

 		(require-not (global-name "com.apple.xpc.amstoold"))
 		(require-not (global-name "com.apple.parsecd"))
 		(require-not (global-name "com.apple.amsprivateidentifiers"))
+		(require-not (global-name "com.apple.networkserviceproxy.fetch-token"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.voicemail.vmd"))
 		(require-not (global-name "com.apple.itunesstored.xpc"))

 		SYS_kdebug_trace_string
 		SYS_kdebug_trace64
 		SYS_kdebug_trace
+		SYS_seteuid
 		SYS_sigreturn
 		SYS_pathconf
 		SYS_fpathconf

 
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
