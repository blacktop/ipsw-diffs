## assistantd

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.siri.attendingstates.xpc")
 		))
 		(require-not (global-name "com.apple.announced.localplaybacksession"))
+		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.vpg.arachned.imageStore"))
 		(require-not (global-name "com.apple.generativeexperiences.availabilityService"))
 		(require-not (global-name "com.apple.WirelessCoexManager"))

 		(require-not (global-name "com.apple.itunescloud.library-auth-token-provider"))
 		(require-not (global-name "com.apple.cache_delete.public"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
+		(require-not (global-name "com.apple.DeviceConfigurationAgent.publisher"))
 		(require-not (global-name "com.apple.remoted"))
 		(require-not (global-name "com.apple.fontservicesd"))
 		(require-not (global-name "com.apple.photos.service"))

 		io_registry_create_iterator
 		io_registry_entry_from_path
 		io_registry_entry_get_name
+		io_registry_entry_get_property_bytes
 		io_registry_entry_get_child_iterator
 		io_registry_entry_get_parent_iterator
 		io_service_close

 		mach_vm_region_recurse
 		mach_vm_region
 		_mach_make_memory_entry
+		mach_vm_page_range_query
 		mach_vm_deferred_reclamation_buffer_flush
 		mach_vm_range_create
 		mach_vm_reallocate
```
