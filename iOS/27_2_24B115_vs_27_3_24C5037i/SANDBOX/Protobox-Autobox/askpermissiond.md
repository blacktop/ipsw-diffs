## askpermissiond

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.PointerUI.pointeruid.service"))
+		(require-not (global-name "com.apple.ServicesPaymentAngel"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.adid"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))

 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.xpc.amstoold"))
 		(require-not (global-name "com.apple.amsprivateidentifiers"))
+		(require-not (global-name "com.apple.networkserviceproxy.fetch-token"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
 		(require-not (global-name "com.apple.system.logger"))

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
+				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 				(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 				(require-not (global-name "com.apple.CARenderServer"))
 				(require-not (global-name "com.apple.AppSSO.service-xpc"))

 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
+				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 				(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 				(require-not (global-name "com.apple.CARenderServer"))
 				(require-not (global-name "com.apple.AppSSO.service-xpc"))

 		MSC_semaphore_signal_trap
 		MSC_semaphore_wait_trap
 		MSC_semaphore_timedwait_trap
+		MSC__kernelrpc_mach_port_get_attributes_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_task_name_for_pid

 
 (deny system-kas-info)
 
+(with-filter (mac-policy-name "Sandbox")
+	(deny system-mac-syscall
+		(require-all
+			(require-not (mac-syscall-number 7))
+			(require-not (mac-syscall-number 67))
+			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 4))
+			(require-not (mac-syscall-number 2))
+		)
+	)
+)
 (deny system-mac-syscall
 	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
+(with-filter (mac-policy-name "vnguard")
+	(deny system-mac-syscall
+		(require-not (mac-syscall-number 1))
 	)
 )
 (deny system-mac-syscall
```
