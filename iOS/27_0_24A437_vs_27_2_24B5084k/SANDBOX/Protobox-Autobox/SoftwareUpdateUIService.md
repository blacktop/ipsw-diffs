## SoftwareUpdateUIService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.dasd.end-prewarm"))
 		(require-not (global-name "com.apple.biometrickitd"))
+		(require-not (global-name "com.apple.muranod.listener"))
 		(require-not (require-any
 			(global-name "com.apple.remote-text-editing-legacy")
 			(global-name "com.apple.sharing.remote-text-editing")

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64

 				io_registry_create_iterator
 				io_registry_entry_from_path
 				io_registry_entry_get_name
+				io_registry_entry_get_child_iterator
 				io_registry_get_root_entry
 				io_service_open_extended
 				io_connect_method
```
