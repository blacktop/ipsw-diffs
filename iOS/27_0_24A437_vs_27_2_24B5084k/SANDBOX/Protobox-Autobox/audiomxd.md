## audiomxd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
+		(require-not (global-name "com.apple.lsd.modifydb"))
 		(require-not (global-name "com.apple.systemstatus.publisher"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
 		(require-not (global-name "com.apple.relatived.public"))

 		mach_vm_inherit
 		mach_vm_write
 		mach_vm_copy
+		mach_vm_read_overwrite
 		mach_vm_behavior_set
 		mach_vm_map_external
 		mach_vm_machine_attribute
```
