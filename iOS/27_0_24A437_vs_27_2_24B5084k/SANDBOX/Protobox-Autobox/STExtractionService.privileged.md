## STExtractionService.privileged

> Group: ⬆️ Updated

```diff

 		(require-not (xpc-service-name "com.apple.StreamingUnzipService"))
 		(require-not (xpc-service-name "com.apple.backgroundassets.managed.relay.service"))
 		(require-not (xpc-service-name "com.apple.backgroundassets.managed.helper.service"))
+		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		mach_exception_raise_state_identity
 		io_iterator_next
 		io_service_get_matching_services
+		io_registry_entry_from_path
 		io_service_open_extended
 		io_connect_method
 		io_server_version
 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
+		io_registry_entry_get_property_bin_buf
 		mach_port_set_attributes
 		mach_port_get_context_from_user
 		mach_port_is_connection_for_service
```
