## CategoriesService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.system.notification_center"))

 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.commcenter.xpc"))

 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.SystemConfiguration.DNSConfiguration"))
 		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.fairplaydeviceidentityd"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.amsprivateidentifiers"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.research.adtcd"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))

 		SYS_sigpending
 		SYS_sigaltstack
 		SYS_ioctl
+		SYS_symlink
 		SYS_readlink
 		SYS_umask
 		SYS_munmap

 		SYS_sysctl
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_fgetattrlist
 		SYS_getxattr
```
