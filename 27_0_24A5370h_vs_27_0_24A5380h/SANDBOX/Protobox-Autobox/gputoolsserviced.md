## gputoolsserviced

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.gputools.GPUToolsReplayService"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.gputools.GPUToolsReplayService"))
 		(require-not (global-name "com.apple.gputools.service"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (require-any
```
