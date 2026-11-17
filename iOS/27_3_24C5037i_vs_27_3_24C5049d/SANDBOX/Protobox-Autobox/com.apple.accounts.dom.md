## com.apple.accounts.dom

> Group: ⬆️ Updated

```diff

 (allow iokit-open-service
 	(require-any
 		(iokit-registry-entry-class "AGXAccelerator")
+		(iokit-registry-entry-class "AppleJPEGDriver")
 		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
 		(iokit-registry-entry-class "AppleM2ScalerParavirtDriver")

 		io_registry_create_iterator
 		io_registry_entry_from_path
 		io_registry_entry_get_name
+		io_service_close
 		io_service_open_extended
 		io_connect_method
+		io_connect_async_method
+		io_registry_entry_get_registry_entry_id
 		io_server_version
 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
```
