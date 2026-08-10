## resourcegrabberd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.iconservices"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.coremedia.endpoint.xpc"))
 		(require-not (require-any
 			(global-name "com.apple.iap2d.ExternalAccessory.distributednotification.server")

 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.appconduitd.device-connection"))
 		(require-not (global-name "com.apple.wifi.manager"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.carkit.app.service"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.iapd.xpc"))
+		(require-not (global-name "com.apple.modelcatalog.catalog"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
 		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
+		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.logd.events"))

 		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.FileCoordination"))
-		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.ExternalAccessory.distributednotification.server"))
 		(require-not (global-name "com.apple.CARenderServer"))
+		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		SYS_change_fdguard_np
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64

 (allow syscall-mach
 	(machtrap-number
 		MSC__kernelrpc_mach_vm_allocate_trap
+		MSC__kernelrpc_mach_vm_purgable_control_trap
 		MSC__kernelrpc_mach_vm_deallocate_trap
 		MSC_task_dyld_process_info_notify_get
 		MSC__kernelrpc_mach_vm_protect_trap

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_SETFD
 		F_GETFL
 		F_NOCACHE
```
