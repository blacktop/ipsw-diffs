## Family

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.mutablecomposition.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (require-any
+			(global-name "com.apple.UIKit.MainMenuStateDelegate")
+			(global-name "com.apple.uikit.viewservice.mainmenustatedelegate")
+		))
 		(require-not (global-name "com.apple.MobileTimer.alarmserver"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.figmetriceventtimeline.xpc"))

 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.passd.in-app-payment"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.generativesearch.server.search"))
 		(require-not (global-name "com.apple.xpc.amstoold"))
 		(require-not (global-name "com.apple.parsecd"))
 		(require-not (global-name "com.apple.amsprivateidentifiers"))

 				task_set_special_port
 				semaphore_create
 				semaphore_destroy
+				task_map_corpse_info_64
 				task_set_exc_guard_behavior
 				task_create_identity_token
 				task_register_hardened_exception_handler

 				vm_remap_external
 				vm_reallocate
 				mach_vm_copy
+				mach_vm_read_overwrite
 				mach_vm_map_external
 				mach_vm_remap_external
 				mach_vm_region_recurse
```
