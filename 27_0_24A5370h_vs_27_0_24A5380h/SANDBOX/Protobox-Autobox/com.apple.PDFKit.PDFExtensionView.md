## com.apple.PDFKit.PDFExtensionView

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.ind.cloudfeatures"))
-		(require-not (global-name "com.apple.mobileasset.autoasset"))
-		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
-		(require-not (global-name "com.apple.carkit.app.service"))
-		(require-not (global-name "com.apple.accessibility.voices"))
-		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
-		(require-not (global-name "com.apple.pluginkit.pkd"))
-		(require-not (global-name "com.apple.hangtracerd"))
-		(require-not (global-name "com.apple.accountsd.accountmanager"))
-		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.gpumemd.source"))
-		(require-not (global-name "com.apple.audio.AudioSession"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
-		(require-not (global-name "com.apple.TextInput.preferences"))
-		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
-		(require-not (global-name "com.apple.hangtracermonitor"))
-		(require-not (global-name "com.apple.mobileassetd.v2"))
-		(require-not (global-name "com.apple.iapd.xpc"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
-		(require-not (global-name "com.apple.coremedia.endpoint.xpc"))
-		(require-not (global-name "com.apple.siri.context.service"))
-		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.ExternalAccessory.distributednotification.server"))
-		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
+		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
+		(require-not (global-name "com.apple.appleneuralengine"))
+		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
+		(require-not (global-name "com.apple.hangtracerd"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
-		(require-not (global-name "com.apple.generativeexperiences.textcomposition"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
+		(require-not (global-name "com.apple.TextInput.rdt"))
+		(require-not (global-name "com.apple.siri.context.service"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.iokit.powerdxpc"))
+		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.TextInput.preferences"))
+		(require-not (global-name "com.apple.coremedia.endpoint.xpc"))
+		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (require-any
 			(global-name "com.apple.iap2d.ExternalAccessory.distributednotification.server")
 			(global-name "com.apple.iaptransportd.ExternalAccessory.distributednotification.server")
 		))
-		(require-not (global-name "com.apple.pasteboard.pasted"))
-		(require-not (global-name "com.apple.iokit.powerdxpc"))
-		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.PowerManagement.control"))
-		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
-		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
-		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.UIKit.OverlayUI.services"))
-		(require-not (global-name "com.apple.TextInput.image-cache-server"))
-		(require-not (global-name "com.apple.lsd.open"))
-		(require-not (global-name "com.apple.DragUI.druid.source"))
-		(require-not (global-name "com.apple.audio.hapticd"))
 		(require-not (global-name "com.apple.audioanalyticsd"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.carkit.app.service"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.handwritingd.remoterecognition"))
-		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
+		(require-not (global-name "com.apple.accessibility.voices"))
+		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))
+		(require-not (global-name "com.apple.generativeexperiences.textcomposition"))
 		(require-not (global-name "com.apple.uiintelligencesupport.agent"))
-		(require-not (global-name "com.apple.tccd"))
-		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
-		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
-		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
-		(require-not (global-name "com.apple.appleneuralengine"))
-		(require-not (global-name "com.apple.sage.textcomposition"))
-		(require-not (global-name "com.apple.TextInput.rdt"))
-		(require-not (xpc-service-name "com.apple.siri.context.service"))
+		(require-not (global-name "com.apple.pasteboard.pasted"))
+		(require-not (global-name "com.apple.iapd.xpc"))
+		(require-not (global-name "com.apple.pluginkit.pkd"))
+		(require-not (global-name "com.apple.audio.AudioSession"))
+		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
-		(require-not (xpc-service-name "com.apple.speech.localspeechrecognition"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
+		(require-not (global-name "com.apple.TextInput.image-cache-server"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.ind.cloudfeatures"))
+		(require-not (global-name "com.apple.DragUI.druid.source"))
+		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
+		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
+		(require-not (global-name "com.apple.hangtracermonitor"))
+		(require-not (global-name "com.apple.audio.hapticd"))
+		(require-not (global-name "com.apple.gpumemd.source"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.sage.textcomposition"))
+		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
+		(require-not (global-name "com.apple.lsd.open"))
+		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
+		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
+		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
+		(require-not (xpc-service-name "com.apple.siri.context.service"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))
+		(require-not (xpc-service-name "com.apple.speech.localspeechrecognition"))
 		(require-not (global-name "com.apple.AccessibilityUIServer"))
 		(require-not (system-attribute developer-mode))
 	)

 		MSC_mach_timebase_info_trap)
 )
 
-(deny syscall-mig
-	(require-all
-		(require-not (kernel-mig-routine
-			host_info
-			host_get_clock_service
-			host_statistics_from_user
-			mach_exception_raise
-			mach_exception_raise_state
-			mach_exception_raise_state_identity
-			io_registry_create_iterator
-			io_registry_entry_get_name
-			io_registry_entry_get_property_bytes
-			io_service_open_extended
-			io_service_add_interest_notification_64
-			io_service_add_notification_bin_64
-			io_registry_entry_get_properties_bin_buf
-			mach_port_get_refs
-			mach_port_get_context_from_user
-			task_info_from_user
-			semaphore_create
-			task_create_identity_token
-			thread_suspend
-			thread_resume
-			thread_info
-			vm_remap_external
-			vm_reallocate
-			mach_vm_range_create
-			mach_vm_reallocate
-			mach_memory_entry_ownership
-			task_restartable_ranges_register
-			task_restartable_ranges_synchronize))
-		(require-any
-			(kernel-mig-routine mach_vm_region_recurse)
-			(kernel-mig-routine task_set_exc_guard_behavior)
-			(require-all
-				(require-not (kernel-mig-routine
-					host_info
-					host_get_clock_service
-					mach_exception_raise
-					mach_exception_raise_state
-					mach_exception_raise_state_identity))
-				(require-not (kernel-mig-routine task_restartable_ranges_register))
-				(require-not (kernel-mig-routine task_restartable_ranges_synchronize))
-				(require-not (kernel-mig-routine semaphore_create))
-				(require-not (kernel-mig-routine mach_vm_reallocate))
-				(require-not (kernel-mig-routine task_info_from_user))
-				(require-not (kernel-mig-routine vm_remap_external))
-				(require-not (kernel-mig-routine io_service_open_extended))
-				(require-not (kernel-mig-routine vm_reallocate))
-			)
-		)
-	)
+(deny syscall-mig)
+(allow syscall-mig
+	(kernel-mig-routine
+		host_info
+		host_get_clock_service
+		host_statistics_from_user
+		mach_exception_raise
+		mach_exception_raise_state
+		mach_exception_raise_state_identity
+		io_registry_create_iterator
+		io_registry_entry_get_name
+		io_registry_entry_get_property_bytes
+		io_service_open_extended
+		io_service_add_interest_notification_64
+		io_service_add_notification_bin_64
+		io_registry_entry_get_properties_bin_buf
+		mach_port_get_refs
+		mach_port_get_context_from_user
+		task_info_from_user
+		semaphore_create
+		task_create_identity_token
+		thread_suspend
+		thread_resume
+		thread_info
+		vm_remap_external
+		vm_reallocate
+		mach_vm_range_create
+		mach_vm_reallocate
+		mach_memory_entry_ownership
+		task_restartable_ranges_register
+		task_restartable_ranges_synchronize)
 )
 
 (deny sysctl*
```
