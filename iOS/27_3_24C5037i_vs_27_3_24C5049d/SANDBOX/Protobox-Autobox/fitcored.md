## fitcored

> Group: ⬆️ Updated

```diff

 		SYS_fstatat64
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_thread_selfusage
 		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np

 				mach_vm_region_recurse
 				mach_vm_region
 				_mach_make_memory_entry
+				mach_vm_page_range_query
 				mach_vm_deferred_reclamation_buffer_flush
 				mach_vm_range_create
 				mach_vm_reallocate

 (deny system-necp-client-action)
 (allow system-necp-client-action
 	(necp-client-action
+		28
 		NECP_CLIENT_ACTION_ACQUIRE_AGENT_TOKEN
 		NECP_CLIENT_ACTION_ADD
 		NECP_CLIENT_ACTION_ADD_FLOW
```
