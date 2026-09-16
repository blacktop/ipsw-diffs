## druid

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.TextInput"))
+		(require-not (global-name "com.apple.dictationengined"))
 		(require-not (require-any
 			(global-name "com.apple.DragUI.druid.system")
 			(global-name "com.apple.ensemble.dragserver")

 		SYS_memorystatus_control
 		SYS_guarded_close_np
 		SYS_guarded_kqueue_np
+		SYS_change_fdguard_np
 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_clonefileat
```
