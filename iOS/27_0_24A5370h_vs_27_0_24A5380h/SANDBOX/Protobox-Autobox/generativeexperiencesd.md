## generativeexperiencesd

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

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.modelmanager"))
-		(require-not (global-name "com.apple.fairplayd.versioned"))
-		(require-not (global-name "com.apple.ind.cloudfeatures"))
-		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
-		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
-		(require-not (global-name "com.apple.mobile.installd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.locationd.synchronous"))
-		(require-not (global-name "com.apple.contactsd"))
-		(require-not (global-name "com.apple.nanoprefsync"))
-		(require-not (global-name "com.apple.calaccessd"))
+		(require-not (global-name "com.apple.biome.access.user"))
+		(require-not (global-name "com.apple.linkd.registry"))
+		(require-not (global-name "com.apple.naturallanguaged"))
+		(require-not (global-name "com.apple.TextInput.emoji"))
 		(require-not (require-any
 			(global-name "com.apple.proactive.PersonalizationPortrait.QuickType")
 			(global-name "com.apple.proactive.input.suggester")
 		))
-		(require-not (global-name "com.apple.generativeexperiences.ExternalProviderTCCUntrustedXPC"))
-		(require-not (global-name "com.apple.accountsd.accountmanager"))
-		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.gpumemd.source"))
-		(require-not (global-name "com.apple.controlcenter.remoteservice"))
-		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
-		(require-not (global-name "com.apple.contacts.poster.api"))
-		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
-		(require-not (global-name "com.apple.TextInput.emoji"))
-		(require-not (global-name "com.apple.inputservice.keyboardui"))
-		(require-not (global-name "com.apple.debug.telemetry"))
-		(require-not (global-name "com.apple.generativeexperiences.generativeexperiencessession"))
-		(require-not (global-name "com.apple.naturallanguaged"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.familycircle.agent"))
-		(require-not (global-name "com.apple.nehelper"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.linkd.transcript"))
-		(require-not (global-name "com.apple.eligibilityd"))
-		(require-not (global-name "com.apple.dnssd.service"))
-		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.softwareupdateservicesd"))
-		(require-not (global-name "com.apple.generativeexperiences.corefollowup"))
-		(require-not (global-name "com.apple.xpc.amsaccountsd"))
-		(require-not (global-name "com.apple.fairplaydeviceidentityd"))
-		(require-not (global-name "com.apple.locationd.registration"))
-		(require-not (global-name "com.apple.adid"))
+		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (require-any
 			(global-name "com.apple.private.GenerativeAgentsTransport.runtime.com.apple.gms.clientexamplesd")
 			(global-name "com.apple.private.GenerativeAgentsTransport.runtime.mach.com.apple.freeform.FreeformAgentService")
 			(global-name "com.apple.private.GenerativeAgentsTransport.runtime.mach.com.apple.gms.clientexamplesd")
 		))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.appstored.xpc.request"))
-		(require-not (global-name "com.apple.remindd"))
-		(require-not (global-name "com.apple.textcontextd.PersonalizationService"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.softwareupdateservicesd"))
+		(require-not (global-name "com.apple.biome.access.system"))
+		(require-not (global-name "com.apple.assistant.settings"))
+		(require-not (global-name "com.apple.mobile.installd"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.nanoprefsync"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.appleintelligencereporting.processing")
 			(xpc-service-name "com.apple.gms.TestClientExamplesAgentsXPCService")

 			(xpc-service-name "com.apple.private.GenerativeAgentsTransport.runtime.com.apple.mobileslideshow.PhotosAgentXPCService")
 			(xpc-service-name "com.apple.private.GenerativeAgentsTransport.runtime.com.apple.notes.NotesAgentXPCService")
 		))
-		(require-not (global-name "com.apple.uservault"))
+		(require-not (global-name "com.apple.TapToRadarKit.service"))
 		(require-not (global-name "com.apple.xpc.amsengagementd"))
-		(require-not (global-name "com.apple.appprotectiond.read"))
-		(require-not (global-name "com.apple.spotlightknowledged"))
-		(require-not (global-name "com.apple.siri.analytics.assistant"))
-		(require-not (global-name "com.apple.assistant.cdm"))
-		(require-not (global-name "com.apple.spotlight.IndexAgent"))
-		(require-not (global-name "com.apple.generativeexperiences.availabilityService"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.symptom_diagnostics"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
-		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
-		(require-not (global-name "com.apple.geod"))
-		(require-not (global-name "com.apple.erm.logging"))
-		(require-not (global-name "com.apple.userprofiles"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
-		(require-not (global-name "com.apple.assistant.settings"))
-		(require-not (global-name "com.apple.biome.compute.source.user"))
-		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (global-name "com.apple.ProgressReporting"))
-		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
-		(require-not (global-name "com.apple.modelcatalog.catalog"))
-		(require-not (global-name "com.apple.usernotifications.listener"))
-		(require-not (global-name "com.apple.featureaccessd"))
-		(require-not (global-name "com.apple.timed.xpc"))
-		(require-not (global-name "com.apple.appleneuralengine"))
-		(require-not (global-name "com.apple.frontboard.systemappservices"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (global-name "com.apple.linkd.registry"))
-		(require-not (global-name "com.apple.cloudsubscriptionfeaturesd"))
-		(require-not (global-name "com.apple.triald.namespace-management"))
-		(require-not (global-name "com.apple.generativeexperiences.ExternalProviderTCCManagingXPC"))
-		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
-		(require-not (global-name "com.apple.FileCoordination"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
+		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
+		(require-not (global-name "com.apple.linkd.transcript"))
+		(require-not (global-name "com.apple.userprofiles"))
+		(require-not (global-name "com.apple.assistant.cdm"))
+		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.generativeexperiences.availabilityService"))
+		(require-not (global-name "com.apple.uservault"))
+		(require-not (global-name "com.apple.geod"))
+		(require-not (global-name "com.apple.inputservice.keyboardui"))
+		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.usernotifications.listener"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.DeviceConfigurationAgent.consumer.async"))
+		(require-not (global-name "com.apple.spotlight.IndexAgent"))
+		(require-not (global-name "com.apple.timed.xpc"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
+		(require-not (global-name "com.apple.biome.compute.source.user"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (xpc-service-name "com.apple.PerfPowerTelemetryClientRegistrationService"))
+		(require-not (global-name "com.apple.modelmanager"))
+		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.eligibilityd"))
+		(require-not (global-name "com.apple.generativeexperiences.corefollowup"))
+		(require-not (global-name "com.apple.DeviceConfigurationAgent.publisher"))
+		(require-not (global-name "com.apple.controlcenter.remoteservice"))
+		(require-not (global-name "com.apple.modelcatalog.catalog"))
+		(require-not (global-name "com.apple.nehelper"))
+		(require-not (global-name "com.apple.locationd.synchronous"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.contacts.poster.api"))
+		(require-not (global-name "com.apple.cloudsubscriptionfeaturesd"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.spotlightknowledged"))
+		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.FileCoordination"))
+		(require-not (global-name "com.apple.generativeexperiences.ExternalProviderTCCManagingXPC"))
+		(require-not (global-name "com.apple.textcontextd.PersonalizationService"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.ind.cloudfeatures"))
+		(require-not (global-name "com.apple.corefollowup.agent"))
+		(require-not (global-name "com.apple.adid"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
+		(require-not (global-name "com.apple.SystemConfiguration.DNSConfiguration"))
+		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.generativeexperiences.generativeexperiencessession"))
+		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
+		(require-not (global-name "com.apple.featureaccessd"))
+		(require-not (global-name "com.apple.generativeexperiences.ExternalProviderTCCUntrustedXPC"))
+		(require-not (global-name "com.apple.appstored.xpc.request"))
+		(require-not (global-name "com.apple.triald.namespace-management"))
+		(require-not (global-name "com.apple.fairplaydeviceidentityd"))
+		(require-not (global-name "com.apple.gpumemd.source"))
+		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.remindd"))
+		(require-not (global-name "com.apple.siri.analytics.assistant"))
+		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.xpc.amsaccountsd"))
+		(require-not (global-name "com.apple.familycircle.agent"))
+		(require-not (global-name "com.apple.ProgressReporting"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.contactsd"))
+		(require-not (global-name "com.apple.calaccessd"))
+		(require-not (global-name "com.apple.appprotectiond.read"))
+		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))

 		SYS_open
 		SYS_close
 		SYS_unlink
+		SYS_chmod
 		SYS_getfsstat
 		SYS_getpid
 		SYS_getuid

 		SYS_fsync
 		SYS_socket
 		SYS_connect
+		SYS_setsockopt
 		SYS_sigsuspend
 		SYS_gettimeofday
 		SYS_readv

 		SYS_fsetattrlist
 		SYS_getxattr
 		SYS_fgetxattr
+		SYS_setxattr
 		SYS_fsetxattr
 		SYS_listxattr
 		SYS_flistxattr

 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_openat_nocancel
 		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat

 		F_OFD_GETLK
 		F_OFD_SETLKWTIMEOUT
 		F_SETCONFINED
+		F_GETCONFINED
 		F_ADDFILESIGS_RETURN
 		F_CHECK_LV)
 )
```
