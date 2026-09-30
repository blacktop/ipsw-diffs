## HomeUIService

> Group: ⬆️ Updated

```diff

 
 (deny generic-issue-extension)
 
-(deny iokit-issue-extension)
+(deny iokit-get-properties)
 
-(deny iokit-open-user-client)
-(allow iokit-open-user-client
+(deny iokit-open*)
+(allow iokit-open*
 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")

 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleANS3CGv2Controller")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
-(deny ipc-posix-sem-open)
-(allow ipc-posix-sem-open
+(deny ipc-posix-sem-create)
+(allow ipc-posix-sem-create
 	(ipc-posix-name "hangtelemetryd.onceatboot")
 )
 
-(deny ipc-posix-shm-read-data)
-(allow ipc-posix-shm-read-data
+(deny ipc-posix-shm*)
+(allow ipc-posix-shm*
 	(require-any
 		(ipc-posix-name "apple.cfprefs.daemonv1")
 		(ipc-posix-name "apple.cfprefs.system.daemonv1")

 	)
 )
 
-(deny job-creation)
+(allow ipc-sysv-shm)
 
-(deny mach-issue-extension)
+(deny isp-command-send)
 
-(deny mach-lookup
+(deny mach-host-special-port-set)
+
+(deny mach-issue-extension
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.storekitd"))

 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
-		(require-not (global-name "com.apple.exchangesyncd"))
+		(require-not (global-name "com.apple.calaccessd"))
 		(require-not (global-name "com.apple.matter.support.xpc"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))

 		(require-not (global-name "com.apple.mediaremoted.xpc"))
 		(require-not (global-name "com.apple.internal.studylogd"))
 		(require-not (global-name "com.apple.contactsd.launch-services-proxy"))
-		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
+		(require-not (global-name "com.apple.exchangesyncd"))
 		(require-not (global-name "com.apple.accessibility.heard"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.nfcd.hwmanager"))
-		(require-not (global-name "com.apple.calaccessd"))
+		(require-not (local-name "com.apple.iphone.axserver"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.coreduetd.people"))

 		(require-not (global-name "com.apple.stickers.api"))
 		(require-not (global-name "com.apple.homed.xpc"))
 		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
+		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.ind.cloudfeatures"))
 		(require-not (global-name "com.apple.contactsd.support"))

 		(require-not (global-name "com.apple.audio.AudioQueueServer"))
 		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
 		(require-not (global-name "com.apple.hangtracermonitor"))
-		(require-not (global-name "com.apple.contactsd"))
+		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.audio.hapticd"))
 		(require-not (global-name "com.apple.uikit.viewservice.com.apple.datadetectors.DDActionsSe"))
 		(require-not (global-name "com.apple.gpumemd.source"))

 		(require-not (global-name "com.apple.audio.SystemSoundServer-iOS"))
 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.siri.analytics.assistant"))
-		(require-not (local-name "com.apple.iphone.axserver"))
+		(require-not (local-name "com.apple.accessibility.gax.client"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
 		(require-not (global-name "com.apple.testmanagerd"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.player.xpc"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.visualintelligence.visual-action-prediction"))
 		(require-not (global-name "com.apple.corerecents.recentsd"))
-		(require-not (global-name "com.apple.audio.AURemoteIOServer"))
+		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.assistant.analytics"))
 		(require-not (global-name "com.apple.familycircle.agent"))

 		(require-not (global-name "com.apple.ScreenTimeAgent.private"))
 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
+		(require-not (global-name "com.apple.audio.AURemoteIOServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.AccessibilityUIServer"))
 		(require-not (global-name "PurplePPTServer"))

 	)
 )
 
+(deny process-codesigning)
+
 (deny process-exec*)
 
+(allow process-exec-interpreter)
+
 (deny socket-ioctl)
 (allow socket-ioctl
 	(ioctl-command
```
