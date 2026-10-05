## sensornetd

> Group: ⬆️ Updated

```diff

 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.sensornetd.transport"))
 		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.adpt.remoteinfoservice")
 			(xpc-service-name "com.apple.atoabenchtestdriver")

 		MSC_thread_self_trap
 		MSC_task_self_trap
 		MSC_host_self_trap
+		MSC__kernelrpc_mach_port_get_attributes_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
+		MSC_task_name_for_pid
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
 		MSC_swtch_pri
```
