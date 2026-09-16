## atc

> Group: ⬆️ Updated

```diff

 (deny iokit-open-service)
 (allow iokit-open-service
 	(require-any
+		(iokit-registry-entry-class "AppleBTM")
+		(iokit-registry-entry-class "AppleHIDTransportHIDDevice")
 		(iokit-registry-entry-class "AppleJPEGDriver")
 		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
 		(iokit-registry-entry-class "AppleM2ScalerParavirtDriver")
+		(iokit-registry-entry-class "AppleSPUHIDDevice")
+		(iokit-registry-entry-class "AppleUserHIDDevice")
 		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationDriver")
+		(iokit-registry-entry-class "IOHIDUserDevice")
 		(iokit-registry-entry-class "IOSurfaceRoot")
 		(iokit-registry-entry-class "com_apple_driver_FairPlayIOKit")
 	)

 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.StatusKit.subscribe"))

 		io_registry_entry_get_property_bytes
 		io_registry_entry_get_parent_iterator
 		io_service_close
+		io_registry_get_root_entry
 		io_registry_entry_create_iterator
 		io_iterator_is_valid
 		io_service_open_extended

 		io_server_version
 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
+		io_service_add_notification_bin_64
 		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf
+		mach_port_get_refs
 		mach_port_request_notification
 		mach_port_set_attributes
 		mach_port_get_context_from_user
```
