## com.apple.migrationpluginwrapper

> Group: ⬆️ Updated

```diff

 		(require-not (require-any
 			(global-name "com.apple.Safari.History.Service")
 			(global-name "com.apple.SafariBookmarksSyncAgent.TabGroups")
-			(global-name "com.apple.appmanagedfeatures.configuration")
 			(global-name "com.apple.atc.xpc.sessions")
 			(global-name "com.apple.safefinancing.activation")
 			(global-name "com.apple.syncdefaultsd")

 		(require-not (global-name "com.apple.assistant.multiuser.service"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationsettingsservice"))
 		(require-not (global-name "com.apple.biometrickitd"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.wifi.manager"))
 		(require-not (global-name "com.apple.purplebuddy.budd.xpc"))
+		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.carkit.app.service"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))

 		(require-not (global-name "com.apple.SecureBackupDaemon.concurrent"))
 		(require-not (global-name "com.apple.linkd.autoShortcut"))
 		(require-not (global-name "com.apple.accessibility.voices"))
+		(require-not (global-name "com.apple.appmanagedfeatures.configuration"))
 		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.eligibilityd"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))

 		mach_vm_remap_external
 		mach_vm_region_recurse
 		_mach_make_memory_entry
+		mach_vm_page_range_query
 		mach_vm_range_create
 		mach_vm_reallocate
 		mach_memory_entry_ownership
```
