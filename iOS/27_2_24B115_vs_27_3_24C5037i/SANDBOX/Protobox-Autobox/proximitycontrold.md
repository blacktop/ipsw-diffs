## proximitycontrold

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.userprofiles"))
 		(require-not (global-name "com.apple.TextInput.preferences"))
 		(require-not (global-name "com.apple.SiriVOXService.client"))
-		(require-not (require-any
-			(global-name "com.apple.findmy.findmylocate.friendshipservice")
-			(global-name "com.apple.findmy.findmylocate.settings")
-		))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
+		(require-not (global-name "com.apple.findmy.findmylocate.friendshipservice"))
 		(require-not (global-name "com.apple.announced.localplaybacksession"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.private.corewifi-xpc"))

 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.linkd.autoShortcut"))
 		(require-not (global-name "com.apple.accessibility.voices"))
 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
 		(require-not (global-name "com.apple.springboard.services"))

 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.mediaremoted.xpc"))
-		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (global-name "com.apple.findmy.findmylocate.settings"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.conversationmanager"))

 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.hangtracermonitor"))
 		(require-not (global-name "com.apple.audio.hapticd"))
+		(require-not (global-name "com.apple.linkd.application-service"))
 		(require-not (global-name "com.apple.airplay.receiver.mediaremote.services"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (require-any

 		(require-not (global-name "com.apple.backboard.hid.services"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.corerecents.recentsd"))
-		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
+		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (global-name "com.apple.ProgressReporting"))
 		(require-not (global-name "com.apple.logd"))

 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AccessibilityUIServer"))
 		(require-not (global-name "PurplePPTServer"))

 		SYS_socketpair
 		SYS_mkdir
 		SYS_rmdir
+		SYS_gethostuuid
 		SYS_pread
 		SYS_pwrite
 		SYS_statfs

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
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
