## perceptiond

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.sigmond")
 			(global-name "com.apple.siri.LaviViz.xpc")
 			(global-name "com.apple.suncore")
+			(global-name "com.apple.sundae.services")
 			(global-name "com.apple.vpg.virtualoutdoors.frameService")
 			(global-name "sd")
 		))

 		(require-not (global-name "com.apple.perceptiond.api"))
 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
 		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.SharingServices"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.photos.service"))

 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
-		(require-not (global-name "com.apple.mediaremoted.xpc"))
 		(require-not (global-name "com.apple.milod.xpc.service"))
+		(require-not (global-name "com.apple.mediaremoted.xpc"))
 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
+		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.locationd.registration"))
-		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
+		(require-not (global-name "com.apple.arkit.service.NutritionService"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.remaker.xpc"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
 		(require-not (global-name "com.apple.dnssd.service"))
-		(require-not (global-name "com.apple.arkit.service.NutritionService"))
+		(require-not (global-name "com.apple.gputools.service"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.logd.admin"))
 		(require-not (global-name "com.apple.photoanalysisd"))
 		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
-		(require-not (global-name "com.apple.gputools.service"))
-		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.generativeexperiences.agentMediaStore"))
 		(require-not (global-name "com.apple.polaris.cache"))
 		(require-not (global-name "com.apple.breadboardservices"))
 		(require-not (global-name "com.apple.audio.AudioQueueServer"))
 		(require-not (global-name "com.apple.FSEvents"))
-		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.AccessorySensorManager"))
 		(require-not (system-attribute developer-mode))
 	)

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 5))
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
