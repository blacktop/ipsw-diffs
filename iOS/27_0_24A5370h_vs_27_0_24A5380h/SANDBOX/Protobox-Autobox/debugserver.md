## debugserver

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (system-attribute developer-mode))
 	)

 		semaphore_create
 		semaphore_destroy
 		task_set_state
+		task_suspend2
+		task_resume2
 		task_map_corpse_info_64
 		task_set_exc_guard_behavior
 		task_dyld_process_info_notify_register
```
