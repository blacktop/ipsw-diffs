## contactsd

> Group: ⬆️ Updated

```diff

 
 (deny mach-lookup
 	(require-all
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.mobileasset.autoasset"))
-		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
-		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
-		(require-not (global-name "com.apple.lsd.icons"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.commcenter.xpc"))
-		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
-		(require-not (global-name "com.apple.gpumemd.source"))
-		(require-not (global-name "com.apple.contacts.poster.api"))
-		(require-not (global-name "com.apple.CellularPlanDaemon.xpc"))
-		(require-not (global-name "com.apple.mobileassetd.v2"))
-		(require-not (global-name "com.apple.debug.telemetry"))
-		(require-not (global-name "com.apple.SBUserNotification"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.ak.auth.xpc"))
-		(require-not (global-name "com.apple.kvsd"))
-		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.CompanionLink"))
-		(require-not (global-name "com.apple.mobileactivationd"))
-		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
-		(require-not (global-name "com.apple.appprotectiond.read"))
-		(require-not (global-name "com.apple.exchangesyncd"))
 		(require-not (global-name "com.apple.biome.access.user"))
-		(require-not (global-name "com.apple.coremedia.admin"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.linkd.registry"))
+		(require-not (global-name "com.apple.lsd.icons"))
+		(require-not (global-name "com.apple.appleneuralengine"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.compressionsession"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
-		(require-not (global-name "com.apple.privacyaccountingd"))
-		(require-not (global-name "com.apple.contactsd.support"))
+		(require-not (global-name "com.apple.ak.auth.xpc"))
+		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
+		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
+		(require-not (global-name "com.apple.kvsd"))
+		(require-not (global-name "com.apple.coremedia.admin"))
+		(require-not (global-name "com.apple.CompanionLink"))
+		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
+		(require-not (global-name "com.apple.mobileactivationd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
+		(require-not (global-name "com.apple.mobileasset.autoasset"))
+		(require-not (global-name "com.apple.privacyaccountingd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.CellularPlanDaemon.xpc"))
+		(require-not (global-name "com.apple.contacts.poster.api"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.contactsd.support"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.gpumemd.source"))
+		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
+		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.datamigrator"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.asktod"))
 		(require-not (global-name "com.apple.lsd.open"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.datamigrator"))
-		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
-		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.appleneuralengine"))
-		(require-not (global-name "com.apple.frontboard.systemappservices"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (global-name "com.apple.linkd.registry"))
-		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
+		(require-not (global-name "com.apple.exchangesyncd"))
+		(require-not (global-name "com.apple.appprotectiond.read"))
+		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.ContactsBackgroundColorService"))
 		(require-not (xpc-service-name "com.apple.imdpersistence.IMDPersistenceAgent"))
-		(require-not (xpc-service-name "com.apple.datamigrator"))
-		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
-		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (xpc-service-name "com.apple.extensionkitservice"))
+		(require-not (xpc-service-name "com.apple.datamigrator"))
 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")

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
```
