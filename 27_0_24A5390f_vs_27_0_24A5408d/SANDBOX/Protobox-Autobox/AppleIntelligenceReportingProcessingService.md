## AppleIntelligenceReportingProcessingService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))

 		MSC__kernelrpc_mach_port_type_trap
 		MSC__kernelrpc_mach_port_request_notification_trap
 		MSC_mach_timebase_info_trap
-		MSC_mk_timer_create)
+		MSC_mk_timer_create
+		MSC_mk_timer_destroy)
 )
 
 (deny syscall-mig)
```
