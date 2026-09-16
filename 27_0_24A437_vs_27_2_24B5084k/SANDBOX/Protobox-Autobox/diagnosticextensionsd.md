## diagnosticextensionsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
 		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.PairingManager"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.debug.telemetry"))

 		semaphore_create
 		semaphore_destroy
 		task_set_exc_guard_behavior
+		thread_get_state_to_user
 		thread_info
 		thread_policy
 		vm_copy

 		vm_reallocate
 		mach_vm_write
 		mach_vm_copy
+		mach_vm_read_overwrite
 		mach_vm_behavior_set
 		mach_vm_map_external
 		mach_vm_remap_external

 (deny system-necp-client-action)
 (allow system-necp-client-action
 	(necp-client-action
+		NECP_CLIENT_ACTION_ACQUIRE_AGENT_TOKEN
 		NECP_CLIENT_ACTION_ADD
 		NECP_CLIENT_ACTION_ADD_FLOW
 		NECP_CLIENT_ACTION_AGENT
```
