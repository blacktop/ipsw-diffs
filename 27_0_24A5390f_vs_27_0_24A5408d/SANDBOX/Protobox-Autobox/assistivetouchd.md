## assistivetouchd

> Group: ⬆️ Updated

```diff

 
 (deny ipc*)
 
+(deny ipc-posix-shm-read-data)
+(allow ipc-posix-shm-read-data
+	(require-any
+		(ipc-posix-name "apple.cfprefs.system.daemonv1")
+		(ipc-posix-name "apple.cfprefs.user.daemonv1")
+	)
+)
+
 (deny job-creation)
 
 (deny mach-issue-extension)

 		(require-not (global-name "com.apple.commandandcontrol"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
 		(require-not (global-name "com.apple.inputanalyticsd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.relatived.status"))
 		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
 		(require-not (global-name "com.apple.hangtelemetryd"))

 		(require-not (global-name "com.apple.relatived.public"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.mediaremoted.xpc"))
+		(require-not (global-name "com.apple.siri.VoiceShortcuts.xpc"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.accessibility.MagnifierAngel.mach"))
 		(require-not (global-name "com.apple.audio.AudioUnitServer"))

 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.coreduetd.context"))
 		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
-		(require-not (global-name "AXPerformanceTestReportingServer"))
+		(require-not (require-any
+			(global-name "AXPerformanceTestReportingServer")
+			(global-name "PurplePPTServer")
+		))
 		(require-not (global-name "com.apple.audio.AudioQueueServer"))
 		(require-not (global-name "com.apple.hangtracermonitor"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled"))
 		(require-not (global-name "com.apple.chronoservices"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "PurplePPTServer"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))

 		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
```
