## intelligenceflowd

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
 		(iokit-registry-entry-class "AppleJPEGDriverUserClient")
+		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationUserClient")
 		(iokit-registry-entry-class "H11ANEInDirectPathClient")
 		(iokit-registry-entry-class "IOGPUDeviceUserClient")

 	)
 )
 
-(deny iokit-open-service)
-(allow iokit-open-service
+(deny iokit-open-user-client)
+(allow iokit-open-user-client
 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
 		(iokit-registry-entry-class "AppleKeyStore")

 	)
 )
 
+(deny iokit-open-service)
+
 (deny iokit-set-properties)
 
 (deny ipc*)
 
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
+		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.lsd.icons"))

 		(require-not (global-name "com.apple.siri.location"))
 		(require-not (global-name "com.apple.omniSearch.search"))
 		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
+		(require-not (global-name "com.apple.itunescloud.music-subscription-status-service"))
 		(require-not (global-name "com.apple.siri.audio_message_service.xpc"))
 		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.CARenderServer"))

 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.perceptiond.entitykit"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (require-any
 			(global-name "com.apple.fun_seat_nsxpc")
 			(global-name "com.apple.howtod.service")

 		(require-not (global-name "com.apple.xpc.amsengagementd"))
 		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
 		(require-not (global-name "com.apple.coresymbolicationd"))
+		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
+		(require-not (global-name "com.apple.chrono.widgetcenterconnection"))
 		(require-not (global-name "com.apple.coremedia.admin"))
 		(require-not (global-name "com.apple.userprofiles"))
 		(require-not (xpc-service-name "com.apple.textkit.nsattributedstringagent"))

 		(require-not (global-name "com.apple.bird"))
 		(require-not (global-name "com.apple.SiriVOXService.client"))
 		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.itunescloudd.tcchelper"))
 		(require-not (global-name "com.apple.searchd"))
 		(require-not (global-name "com.apple.backboardd.virtualframebuffer"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))

 		(require-not (global-name "com.apple.imagent.embedded.auth"))
 		(require-not (local-name "com.apple.iphone.axserver"))
 		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.medialibraryd.xpc"))
 		(require-not (global-name "com.apple.generativeexperiences.generativeexperiencessession"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Contact"))
 		(require-not (global-name "com.apple.intelligenceflow.toolbox"))

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

 		SYS_renameatx_np
 		SYS_persona
 		SYS_mach_eventlink_signal_wait_until
+		SYS_work_interval_ctl
 		SYS_getentropy
 		SYS_necp_open
 		SYS_necp_client_action
```
