## ExtensibleSSOSubscriber

> Group: ⬆️ Updated

```diff

 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.AppSSO.ddm-configuration-xpc"))
 		(require-not (global-name "com.apple.CARenderServer"))
-		(require-not (global-name "com.apple.inputservice.keyboardui"))
-		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
+		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (system-attribute developer-mode))
 	)

 		mach_vm_copy
 		mach_vm_behavior_set
 		mach_vm_map_external
+		mach_vm_remap_external
 		mach_vm_region_recurse
 		mach_vm_region
 		_mach_make_memory_entry
```
