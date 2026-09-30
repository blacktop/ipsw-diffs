## intelligencetasksd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.userprofiles"))
+		(require-not (global-name "com.apple.uservault"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
 		(require-not (global-name "com.apple.spotlight.SearchAgent"))
-		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (system-attribute developer-mode))
 	)

 		MSC_semaphore_timedwait_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
+		MSC_task_name_for_pid
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
 		MSC_swtch_pri

 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
+			(require-not (mac-syscall-number 80))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 67))
 			(require-not (mac-syscall-number 2))
```
