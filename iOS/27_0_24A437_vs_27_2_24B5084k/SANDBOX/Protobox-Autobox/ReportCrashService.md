## ReportCrashService

> Group: ⬆️ Updated

```diff

 
 (allow default)
 
+(deny asr-parser-enter)
+
 (deny file-ioctl)
 
 (deny generic-issue-extension)

 		(iokit-registry-entry-class "AppleCredentialManager")
 		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AppleSoCMisc")
+		(iokit-registry-entry-class "AppleT6021PMGR")
 		(iokit-registry-entry-class "AppleT7000PMGR")
 		(iokit-registry-entry-class "AppleT8006PMGR")
 		(iokit-registry-entry-class "AppleT8020PMGR")

 		(require-not (global-name "com.apple.rtcreportingd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.OTATaskingAgent"))
+		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.ReportMemoryException"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.commcenter.xpc"))

 		task_suspend2
 		task_resume2
 		task_map_corpse_info_64
+		task_inspect
 		task_set_exc_guard_behavior
 		mach_task_is_self
 		task_dyld_process_info_notify_register
```
