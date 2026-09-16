## assistivetouchd

> Group: ⬆️ Updated

```diff

 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleCredentialManager")
+		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
 		(iokit-registry-entry-class "AppleParavirtGPU")
 		(iokit-registry-entry-class "AppleUSBTopCaseHIDDriver")

 	(require-any
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")
 		(ipc-posix-name "apple.cfprefs.user.daemonv1")
+		(ipc-posix-name "apple.shm.notification_center")
 	)
 )
 

 
 (deny mach-lookup
 	(require-all
+		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.accessibility.AXPineBoardServer"))

 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.coreduetd.context"))
 		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
-		(require-not (require-any
-			(global-name "AXPerformanceTestReportingServer")
-			(global-name "PurplePPTServer")
-		))
+		(require-not (global-name "AXPerformanceTestReportingServer"))
 		(require-not (global-name "com.apple.audio.AudioQueueServer"))
 		(require-not (global-name "com.apple.hangtracermonitor"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled"))
 		(require-not (global-name "com.apple.chronoservices"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "PurplePPTServer"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))

 		MSC_mk_timer_destroy
 		MSC_mk_timer_arm
 		MSC_mk_timer_cancel
-		MSC_mk_timer_arm_leeway)
+		MSC_mk_timer_arm_leeway
+		MSC_iokit_user_client_trap)
 )
 
 (deny syscall-mig)

 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
-	(memorystatus-control-command MEMORYSTATUS_CMD_INCREASE_JETSAM_TASK_LIMIT)
+	(memorystatus-control-command
+		MEMORYSTATUS_CMD_GET_PROCESS_IS_FROZEN
+		MEMORYSTATUS_CMD_INCREASE_JETSAM_TASK_LIMIT)
 )
 
 (deny system-necp-client-action)
```
