## CategoriesService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.siri.context.service"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.xpc.amsengagementd"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.networkd_privileged"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))

 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.cfnetwork.AuthBrokerAgent"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.nehelper"))

 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
+		(require-not (global-name "com.apple.adid"))
+		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
+		(require-not (global-name "com.apple.SystemConfiguration.DNSConfiguration"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.amsprivateidentifiers"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.research.adtcd"))

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
-		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.GSSCred"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))

 		MSC__kernelrpc_mach_port_request_notification_trap
 		MSC_mach_timebase_info_trap
 		MSC_mk_timer_create
+		MSC_mk_timer_destroy
 		MSC_mk_timer_arm
 		MSC_mk_timer_cancel)
 )
```
