## homed

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.findmy.findmylocate.friendshipservice")
 			(global-name "com.apple.findmy.findmylocate.settings")
 		))
+		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.soundanalysisd"))
 		(require-not (global-name "com.apple.WirelessCoexManager"))
 		(require-not (global-name "com.apple.backlightd"))

 			(global-name "com.apple.uarp.endpoint.transport")
 		))
 		(require-not (global-name "com.apple.assistant.security"))
+		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (xpc-service-name "com.apple.itunescloud.music-subscription-status-service"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))

 		(require-not (global-name "com.apple.modelmanager"))
 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.accessibility.voices"))
 		(require-not (global-name "com.apple.nfcd.xpc.homed.uaevents"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.sessionservices"))

 		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.corespeech.corespeechservices"))
+		(require-not (global-name "com.apple.audio.AudioUnitServer"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
 		(require-not (xpc-service-name "com.apple.EnergyKitService"))

 		(require-not (global-name "com.apple.homed.xpc"))
 		(require-not (global-name "com.apple.seserviced"))
 		(require-not (global-name "com.apple.groupkitd.xpc.groupservice"))
+		(require-not (global-name "com.apple.ind.cloudfeatures"))
 		(require-not (global-name "com.apple.corefollowup.agent"))
 		(require-not (xpc-service-name "com.apple.WorkflowKit.BackgroundShortcutRunner"))
 		(require-not (global-name "com.apple.mediaanalysisd.homekitsession"))

 		(require-not (global-name "com.apple.siri.external_request"))
 		(require-not (global-name "com.apple.maps.destinationd.sources"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.audio.hapticd"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.airplay.receiver.mediaremote.services"))
 		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))

 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
 		SYS_persona
+		SYS_mach_eventlink_signal_wait_until
 		SYS_getentropy
 		SYS_necp_open
 		SYS_necp_client_action

 		mach_voucher_attr_command
 		UNDNotificationCreated_rpc
 		task_restartable_ranges_register
-		task_restartable_ranges_synchronize)
+		task_restartable_ranges_synchronize
+		mach_eventlink_create
+		mach_eventlink_destroy
+		mach_eventlink_associate)
 )
 
 (deny sysctl*

 		F_GETPROTECTIONCLASS
 		F_SETPROTECTIONCLASS
 		F_DUPFD_CLOEXEC
+		F_SETNOSIGPIPE
 		F_SINGLE_WRITER
 		F_BARRIERFSYNC
 		F_OFD_SETLK
```
