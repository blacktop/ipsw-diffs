## askpermissiond

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.people.agent"))
 		(require-not (global-name "com.apple.xpc.amsaccountsd"))
+		(require-not (global-name "com.apple.SharedWebCredentials"))
 		(require-not (global-name "com.apple.familycircle.agent"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))

 		SYS_unlinkat
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_thread_selfusage
 		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np

 		semaphore_create
 		semaphore_destroy
 		task_set_exc_guard_behavior
+		task_create_identity_token
 		thread_info
 		thread_policy
 		vm_remap_external
```
