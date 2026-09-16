## generativelearningd

> Group: ⬆️ Updated

```diff

 		(iokit-registry-entry-class "IOGPUDeviceUserClient")
 		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 		(iokit-registry-entry-class "IOSurfaceRootUserClient")
+		(iokit-registry-entry-class "RootDomainUserClient")
 	)
 )
 

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.linkd.registry"))
+		(require-not (global-name "com.apple.managedappdistributiond.xpc"))
 		(require-not (global-name "com.apple.mediaanalysisd.analysis"))
 		(require-not (global-name "com.apple.appleneuralengine"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.mobilemail.services.xpc"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.assistant.cdm"))
+		(require-not (global-name "com.apple.searchd"))
+		(require-not (global-name "com.apple.suggestd.events"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
+		(require-not (global-name "com.apple.proactive.ActionPrediction.predictions"))
+		(require-not (global-name "com.apple.generativesearch.server.indexing"))
+		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.linkd.autoShortcut"))
+		(require-not (global-name "com.apple.generativesearch.server.salientpostings"))
+		(require-not (global-name "com.apple.springboard.backgroundappservices"))
 		(require-not (global-name "com.apple.photos.service"))
+		(require-not (global-name "com.apple.intelligenceplatform.View"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
+		(require-not (global-name "com.apple.mediaremoted.xpc"))
+		(require-not (global-name "com.apple.email.maild"))
 		(require-not (global-name "com.apple.spotlightknowledged"))
+		(require-not (global-name "com.apple.itunescloudd.xpc"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.contactsd.support"))
+		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Contact"))
 		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
+		(require-not (global-name "com.apple.diagnosticpipeline.service"))
+		(require-not (global-name "com.apple.proactive.appDirectory"))
 		(require-not (global-name "com.apple.generativesearch.server.search"))
+		(require-not (global-name "com.apple.parsecd"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
 		(require-not (global-name "com.apple.intelligenceflow.contextTool"))
+		(require-not (global-name "com.apple.dmd.policy"))
 		(require-not (global-name "com.apple.spotlight.SearchAgent"))
 		(require-not (global-name "com.apple.contactsd"))
+		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
+		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))

 
 (deny socket-ioctl)
 (allow socket-ioctl
-	(ioctl-command CTLIOCGINFO)
+	(ioctl-command
+		CTLIOCGINFO
+		SIOCGIFCONSTRAINED
+		SIOCGIFDELEGATE
+		SIOCGIFEXPENSIVE
+		SIOCGIFFLAGS
+		SIOCGIFFUNCTIONALTYPE
+		SIOCGIFLINKQUALITYMETRIC
+		SIOCGIFMTU
+		SIOCGIFULTRACONSTRAINED)
 )
 
 (deny syscall-unix

 			SYS_sigsuspend
 			SYS_readv
 			SYS_writev
+			SYS_rename
 			SYS_flock
 			SYS_sendto
 			SYS_mkdir

 			SYS_getumask
 			SYS_open_dprotected_np
 			SYS_openat_dprotected_np
+			SYS_listxattr
 			SYS_fsctl
 			SYS_sysctlbyname
 			SYS_gettid

 			SYS_getfsstat64
 			SYS___pthread_chdir
 			SYS___pthread_fchdir
+			SYS_kqueue
 			SYS_thread_selfid
 			SYS___mac_syscall
 			SYS_read_nocancel

 			SYS_fileport_makefd
 			SYS_memorystatus_control
 			SYS_guarded_open_np
+			SYS_guarded_kqueue_np
 			SYS_change_fdguard_np
 			SYS_openat
 			SYS_faccessat

 		io_iterator_next
 		io_registry_create_iterator
 		io_registry_entry_from_path
+		io_registry_entry_get_name
 		io_service_open_extended
 		io_connect_method
 		io_service_add_interest_notification_64
 		io_server_version
 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
+		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf
 		mach_port_get_refs
 		mach_port_request_notification

 		F_GETFD
 		F_GETFL
 		F_SETFL
+		F_SETLK
 		F_RDADVISE
 		F_NOCACHE
 		F_GETPATH

 
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
+		(mac-syscall-number 0 1)
 		(require-not (mac-policy-name "vnguard"))
 	)
 )
```
