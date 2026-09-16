## speechmaintenanced

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.assistant.settings"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.modelcatalog.catalog"))
 		(require-not (global-name "com.apple.intelligenceplatform.View"))
 		(require-not (global-name "com.apple.speechmaintenanced"))

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_GETFL
 		F_RDADVISE
 		F_NOCACHE
```
