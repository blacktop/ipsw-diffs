## healthappd

> Group: ⬆️ Updated

```diff

 		(require-not (require-any
 			(global-name "com.apple.agentmanager")
 			(global-name "com.apple.corepersonalization.server.insights")
-			(global-name "com.apple.corepersonalization.server.memory")
 			(global-name "com.apple.healthcontentd")
 		))
 		(require-not (global-name "com.apple.xpc.amsengagementd"))

 		(require-not (global-name "com.apple.modelmanager"))
 		(require-not (global-name "com.apple.symptom_analytics"))
 		(require-not (global-name "com.apple.erm.logging"))
-		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
+		(require-not (global-name "com.apple.corepersonalization.server.memory"))
 		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.fontservicesd"))
 		(require-not (global-name "com.apple.modelcatalog.catalog"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.healthrecordsd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
-		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))

 		(require-not (global-name "com.apple.generativesearch.server.search"))
 		(require-not (global-name "com.apple.xpc.amstoold"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.NPKCompanionAgent.library"))
 		(require-not (global-name "com.apple.seymour"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
 		(require-not (global-name "com.apple.debug.telemetry"))

 		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (global-name "com.apple.contactsd"))
+		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
+		(require-not (global-name "com.apple.NPKCompanionAgent.library"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))

 		MSC__kernelrpc_mach_port_construct_trap
 		MSC__kernelrpc_mach_port_destruct_trap
 		MSC_mach_reply_port
+		MSC_thread_self_trap
 		MSC_task_self_trap
 		MSC_host_self_trap
 		MSC_semaphore_signal_trap

 		mach_port_set_attributes
 		mach_port_get_context_from_user
 		mach_port_is_connection_for_service
+		task_threads_from_user
 		task_info_from_user
 		task_get_special_port_from_user
 		task_set_special_port

 		mach_vm_region_recurse
 		mach_vm_region
 		_mach_make_memory_entry
+		mach_vm_page_range_query
 		mach_vm_deferred_reclamation_buffer_flush
 		mach_vm_range_create
 		mach_vm_reallocate

 
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
