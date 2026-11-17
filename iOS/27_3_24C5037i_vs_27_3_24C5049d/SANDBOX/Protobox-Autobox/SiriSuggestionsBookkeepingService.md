## SiriSuggestionsBookkeepingService

> Group: ⬆️ Updated

```diff

 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+		(iokit-registry-entry-class "IOSurfaceAcceleratorClient")
 	)
 )
 
 (deny iokit-open-service)
+(allow iokit-open-service
+	(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
+)
 
 (deny iokit-set-properties)
 

 		io_registry_entry_from_path
 		io_registry_entry_get_name
 		io_registry_entry_get_parent_iterator
+		io_service_close
 		io_registry_entry_create_iterator
 		io_iterator_is_valid
 		io_service_open_extended
```
