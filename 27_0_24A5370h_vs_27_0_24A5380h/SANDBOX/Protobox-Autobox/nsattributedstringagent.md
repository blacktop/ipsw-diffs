## nsattributedstringagent

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
-		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
-		(require-not (global-name "com.apple.GameController.gamecontrollerd.app"))
-		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.backboard.display.services"))
-		(require-not (global-name "com.apple.gpumemd.source"))
-		(require-not (global-name "com.apple.audio.AudioSession"))
-		(require-not (global-name "com.apple.inputservice.keyboardui"))
-		(require-not (global-name "com.apple.familycircle.agent"))
-		(require-not (global-name "com.apple.fontservicesd"))
-		(require-not (global-name "com.apple.iconservices"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.accessibility.gax.backboard"))
-		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
-		(require-not (global-name "com.apple.backboard.hid.services"))
+		(require-not (global-name "com.apple.webinspector"))
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
+		(require-not (global-name "com.apple.TextInput"))
+		(require-not (global-name "com.apple.accessibility.mediaaccessibilityd"))
+		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (require-any
 			(global-name "com.apple.appprotectiond.extensioninfo")
 			(global-name "com.apple.appprotectiond.extensionmonitor")
 		))
-		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
-		(require-not (global-name "com.apple.accessibility.mediaaccessibilityd"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.iconservices"))
+		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
+		(require-not (global-name "com.apple.Safari.SafeBrowsing.Service"))
 		(require-not (global-name "com.apple.coremedia.admin"))
-		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.accessibility.gax.backboard"))
+		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
+		(require-not (global-name "com.apple.inputservice.keyboardui"))
+		(require-not (global-name "com.apple.audioanalyticsd"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.backboard.display.services"))
+		(require-not (global-name "com.apple.audio.AudioSession"))
+		(require-not (global-name "com.apple.fontservicesd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.webprivacyd"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.webinspector"))
-		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
+		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
+		(require-not (global-name "com.apple.GameController.gamecontrollerd.app"))
+		(require-not (global-name "com.apple.gpumemd.source"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
-		(require-not (global-name "com.apple.TextInput"))
+		(require-not (global-name "com.apple.backboard.hid.services"))
+		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.audioanalyticsd"))
-		(require-not (global-name "com.apple.backboard.hid-services.xpc"))
-		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
-		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.frontboard.systemappservices"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (global-name "com.apple.Safari.SafeBrowsing.Service"))
+		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
+		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AccessibilityUIServer"))
 		(require-not (system-attribute developer-mode))

 		SYS_getumask
 		SYS_getattrlist
 		SYS_fgetattrlist
+		SYS_fgetxattr
 		SYS_fsctl
 		SYS_shm_open
 		SYS_sem_open

 		MSC_mk_timer_arm_leeway)
 )
 
-(deny syscall-mig
-	(require-all
-		(require-not (kernel-mig-routine
-			host_info
-			host_get_io_master
-			host_get_clock_service
-			host_statistics_from_user
-			host_get_special_port
-			mach_exception_raise
-			mach_exception_raise_state
-			mach_exception_raise_state_identity
-			io_iterator_next
-			io_registry_create_iterator
-			io_registry_entry_from_path
-			io_registry_entry_get_name
-			io_service_close
-			io_service_open_extended
-			io_connect_method
-			io_connect_async_method
-			io_connect_set_notification_port_64
-			io_registry_entry_get_registry_entry_id
-			io_server_version
-			io_service_get_matching_service_bin
-			io_service_get_matching_services_bin
-			io_registry_entry_get_properties_bin_buf
-			io_registry_entry_get_property_bin_buf
-			mach_port_get_refs
-			mach_port_request_notification
-			mach_port_set_attributes
-			mach_port_get_context_from_user
-			mach_port_is_connection_for_service
-			task_info_from_user
-			task_get_special_port_from_user
-			task_set_special_port
-			semaphore_create
-			semaphore_destroy
-			task_set_exc_guard_behavior
-			thread_get_state_to_user
-			thread_suspend
-			thread_info
-			thread_policy_set
-			vm_remap_external
-			vm_reallocate
-			mach_vm_copy
-			mach_vm_map_external
-			mach_vm_remap_external
-			mach_vm_region
-			_mach_make_memory_entry
-			mach_vm_range_create
-			mach_vm_reallocate
-			mach_memory_entry_ownership
-			mach_voucher_attr_command
-			task_restartable_ranges_register
-			task_restartable_ranges_synchronize))
-		(require-any
-			(kernel-mig-routine mach_vm_region_recurse)
-			(require-all
-				(require-not (kernel-mig-routine
-					host_info
-					host_get_clock_service
-					mach_exception_raise
-					mach_exception_raise_state
-					mach_exception_raise_state_identity
-					mach_port_get_context_from_user))
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
+		host_get_io_master
+		host_get_clock_service
+		host_statistics_from_user
+		host_get_special_port
+		mach_exception_raise
+		mach_exception_raise_state
+		mach_exception_raise_state_identity
+		io_iterator_next
+		io_registry_create_iterator
+		io_registry_entry_from_path
+		io_registry_entry_get_name
+		io_service_close
+		io_service_open_extended
+		io_connect_method
+		io_connect_async_method
+		io_connect_set_notification_port_64
+		io_registry_entry_get_registry_entry_id
+		io_server_version
+		io_service_get_matching_service_bin
+		io_service_get_matching_services_bin
+		io_registry_entry_get_properties_bin_buf
+		io_registry_entry_get_property_bin_buf
+		mach_port_get_refs
+		mach_port_request_notification
+		mach_port_set_attributes
+		mach_port_get_context_from_user
+		mach_port_is_connection_for_service
+		task_info_from_user
+		task_get_special_port_from_user
+		task_set_special_port
+		semaphore_create
+		semaphore_destroy
+		task_set_exc_guard_behavior
+		thread_get_state_to_user
+		thread_suspend
+		thread_resume
+		thread_info
+		thread_policy_set
+		vm_remap_external
+		vm_reallocate
+		mach_vm_copy
+		mach_vm_map_external
+		mach_vm_remap_external
+		mach_vm_region_recurse
+		mach_vm_region
+		_mach_make_memory_entry
+		mach_vm_range_create
+		mach_vm_reallocate
+		mach_memory_entry_ownership
+		mach_voucher_attr_command
+		task_restartable_ranges_register
+		task_restartable_ranges_synchronize)
 )
 
 (deny sysctl*
```
