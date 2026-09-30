## generativelearningd

> Group: ⬆️ Updated

```diff

 		MSC__kernelrpc_mach_port_request_notification_trap
 		MSC_mach_timebase_info_trap
 		MSC_mk_timer_create
-		MSC_mk_timer_destroy)
+		MSC_mk_timer_destroy
+		MSC_mk_timer_arm
+		MSC_mk_timer_cancel)
 )
 
 (deny syscall-mig)

 		mach_exception_raise_state
 		mach_exception_raise_state_identity
 		io_iterator_next
+		io_registry_create_iterator
 		io_registry_entry_from_path
 		io_service_open_extended
 		io_connect_method

 		semaphore_destroy
 		task_set_exc_guard_behavior
 		task_create_identity_token
+		thread_suspend
 		thread_policy
 		vm_remap_external
 		vm_reallocate
```
