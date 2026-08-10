## SystemIntents

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.lsd.advertisingidentifiers"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
 		(require-not (global-name "com.apple.hangtracermonitor"))

 			SYS_proc_rlimit_control
 			SYS_getattrlistbulk
 			SYS_openat
+			SYS_renameat
 			SYS_faccessat
 			SYS_fstatat
 			SYS_fstatat64
+			SYS_unlinkat
 			SYS_mkdirat
 			SYS_bsdthread_ctl
 			SYS_guarded_open_dprotected_np

 			mach_exception_raise_state_identity
 			io_object_conforms_to
 			io_iterator_next
+			io_registry_create_iterator
 			io_registry_entry_from_path
 			io_registry_get_root_entry
 			io_service_open_extended
```
