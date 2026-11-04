## searchtoold

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.managedappdistributiond.xpc"))
 		(require-not (global-name "com.apple.mediaanalysisd.analysis"))
 		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
+		(require-not (global-name "com.apple.linkd.extension"))
 		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.Maps.xpc.connectionBroker.endpointRecorder"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (global-name "com.apple.healthd.server"))

 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.mobilemail.services.xpc"))
+		(require-not (global-name "com.apple.intelligenceplatform.EntityResolution"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.businessservicesd"))
+		(require-not (global-name "com.apple.lsd.xpc"))
 		(require-not (global-name "com.apple.PineBoardServices"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.linkd.transcript"))
 		(require-not (global-name "com.apple.userprofiles"))
+		(require-not (global-name "com.apple.assistant.cdm"))
 		(require-not (global-name "com.apple.bird"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
+		(require-not (global-name "com.apple.searchd"))
 		(require-not (global-name "com.apple.uservault"))
 		(require-not (global-name "com.apple.suggestd.events"))
 		(require-not (global-name "com.apple.geod"))

 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.modelmanager"))
 		(require-not (global-name "com.apple.symptom_analytics"))
+		(require-not (global-name "com.apple.linkd.autoShortcut"))
 		(require-not (global-name "com.apple.pasteboard.pasted"))
+		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.itunescloud.library-auth-token-provider"))
 		(require-not (global-name "com.apple.springboard.backgroundappservices"))
 		(require-not (global-name "com.apple.fontservicesd"))

 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.mediaremoted.xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.email.maild"))
 		(require-not (global-name "com.apple.fairplayd.xpc"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.itunescloudd.xpc"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.webprivacyd"))
 		(require-not (global-name "com.apple.mediaanalysisd.embeddingstore"))
 		(require-not (global-name "com.apple.searchd.background"))

 		(require-not (global-name "com.apple.generativeexperiences.generativeexperiencessession"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Contact"))
 		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
+		(require-not (global-name "com.apple.linkd.application-service"))
+		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.proactive.appDirectory"))

 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.generativesearch.server.search"))
 		(require-not (global-name "com.apple.parsecd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.remindd"))
 		(require-not (global-name "com.apple.siri.analytics.assistant"))
 		(require-not (global-name "com.apple.corerecents.recentsd"))

 		(require-not (xpc-service-name "com.apple.StocksKitService"))
 		(require-not (xpc-service-name "com.apple.FileBrowsingServices.PathResolver"))
 		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
-		(require-not (global-name "com.apple.FSEvents"))
+		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))
 	)

 		SYS_kdebug_trace_string
 		SYS_kdebug_trace64
 		SYS_kdebug_trace
+		SYS_seteuid
 		SYS_sigreturn
 		SYS_pathconf
 		SYS_getrlimit

 		SYS_listxattr
 		SYS_fsctl
 		SYS_posix_spawn
+		SYS_ffsctl
 		SYS_shm_open
 		SYS_sysctlbyname
 		SYS_gettid

 		host_info
 		host_get_io_master
 		host_get_clock_service
+		host_statistics_from_user
 		host_request_notification
 		host_get_special_port
 		clock_get_time

 		thread_suspend
 		thread_resume
 		thread_info
+		thread_set_exception_ports
+		thread_get_exception_ports_from_user
 		thread_policy
 		vm_remap_external
 		vm_reallocate

 
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
