## gputoolsserviced

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
+		(require-not (global-name "com.apple.coresymbolicationd"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.gputools.GPUToolsReplayService"))

 			(xpc-service-name "com.apple.gputools.GPUToolsReplayService")
 			(xpc-service-name "com.apple.gputools.MLReplayService")
 		))
-		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (system-attribute developer-mode))

 		mach_exception_raise_state
 		mach_exception_raise_state_identity
 		io_iterator_next
+		io_registry_entry_from_path
 		io_connect_set_notification_port
 		io_service_open_extended
 		io_connect_method
```
