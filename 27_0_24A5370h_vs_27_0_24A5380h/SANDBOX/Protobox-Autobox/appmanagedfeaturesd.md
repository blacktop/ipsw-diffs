## appmanagedfeaturesd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.icloud.findmydeviced"))
-		(require-not (global-name "com.apple.managedconfiguration.teslad"))
-		(require-not (global-name "com.apple.adid"))
-		(require-not (global-name "com.apple.mobileactivationd"))
-		(require-not (global-name "com.apple.dmd"))
-		(require-not (global-name "com.apple.installcoordinationd"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
-		(require-not (global-name "com.apple.manageddeviced"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.managedconfiguration.teslad"))
+		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.appstored.xpc"))
+		(require-not (global-name "com.apple.manageddeviced"))
+		(require-not (global-name "com.apple.installcoordinationd"))
+		(require-not (global-name "com.apple.dmd"))
+		(require-not (global-name "com.apple.adid"))
+		(require-not (global-name "com.apple.icloud.findmydeviced"))
 		(require-not (global-name "com.apple.ManagedSettingsAgent"))
 		(require-not (system-attribute developer-mode))
 	)

 		MSC_mach_generate_activity_id
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
+		MSC_swtch_pri
 		MSC_syscall_thread_switch
 		MSC_host_create_mach_voucher_trap
 		MSC__kernelrpc_mach_port_type_trap
```
