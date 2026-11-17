## healthcontentd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.cache_delete.public"))
 		(require-not (global-name "com.apple.amsservicesanalytics.xpc"))
 		(require-not (global-name "com.apple.adid"))
+		(require-not (global-name "com.apple.fairplayd"))
 		(require-not (global-name "com.apple.fairplaydeviceidentityd"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))

 			SYS_recvmsg
 			SYS_sendmsg
 			SYS_recvfrom
+			SYS_getsockname
 			SYS_crossarch_trap
 			SYS_dup
 			SYS_getegid

 			SYS_fstatat
 			SYS_fstatat64
 			SYS_mkdirat
+			SYS_thread_selfusage
 			SYS_guarded_open_dprotected_np
 			SYS_guarded_write_np
 			SYS_guarded_pwrite_np

 		semaphore_create
 		semaphore_destroy
 		task_set_exc_guard_behavior
+		task_create_identity_token
 		thread_policy
 		thread_policy_set
 		vm_remap_external
```
