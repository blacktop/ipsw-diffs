## ManagedStatusSubscriber

> Group: ⬆️ Updated

```diff

 			SYS_gettid
 			SYS_mkdir_extended
 			SYS_shared_region_check_np
+			SYS_psynch_rw_longrdlock
+			SYS_psynch_rw_yieldwrlock
+			SYS_psynch_rw_downgrade
+			SYS_psynch_rw_upgrade
+			SYS_psynch_mutexwait
+			SYS_psynch_mutexdrop
+			SYS_psynch_rw_rdlock
+			SYS_psynch_rw_wrlock
+			SYS_psynch_rw_unlock
+			SYS_psynch_rw_unlock2
 			SYS_issetugid
 			SYS___pthread_kill
 			SYS___pthread_sigmask

 		MSC_mach_reply_port
 		MSC_task_self_trap
 		MSC_host_self_trap
+		MSC_semaphore_wait_trap
+		MSC_semaphore_timedwait_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_mach_msg2_trap

 		mach_exception_raise_state
 		mach_exception_raise_state_identity
 		io_registry_entry_from_path
+		io_service_close
 		io_service_open_extended
+		io_connect_method
 		io_server_version
 		io_service_get_matching_service_bin
 		io_registry_entry_get_property_bin_buf
```
