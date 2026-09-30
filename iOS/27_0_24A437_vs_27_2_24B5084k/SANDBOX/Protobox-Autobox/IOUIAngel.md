## IOUIAngel

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
 		(require-not (local-name "com.apple.iphone.axserver"))
+		(require-not (local-name "com.apple.accessibility.gax.client"))
 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))

 		MSC__kernelrpc_mach_port_request_notification_trap
 		MSC_mach_timebase_info_trap
 		MSC_mk_timer_create
+		MSC_mk_timer_destroy
 		MSC_mk_timer_arm
 		MSC_mk_timer_cancel
 		MSC_mk_timer_arm_leeway)
```
