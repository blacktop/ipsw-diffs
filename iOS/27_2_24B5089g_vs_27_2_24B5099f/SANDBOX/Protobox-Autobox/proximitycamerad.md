## proximitycamerad

> Group: ⬆️ Updated

```diff

 
 (deny iokit-open-service)
 (allow iokit-open-service
-	(iokit-registry-entry-class "AppleKeyStore")
+	(require-any
+		(iokit-registry-entry-class "AppleJPEGDriver")
+		(iokit-registry-entry-class "AppleKeyStore")
+	)
 )
 
 (deny iokit-set-properties)

 		(require-not (global-name "com.apple.translation.text"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))

 		mach_exception_raise
 		mach_exception_raise_state
 		mach_exception_raise_state_identity
+		io_iterator_next
 		io_registry_entry_from_path
 		io_service_open_extended
 		io_connect_method
 		io_server_version
 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
+		io_registry_entry_get_property_bin_buf
 		mach_port_request_notification
 		mach_port_set_attributes
 		mach_port_get_context_from_user
```
