## mstreamd

> Group: ⬆️ Updated

```diff

 )
 
 (deny iokit-open-service)
+(allow iokit-open-service
+	(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
+)
 
 (deny iokit-set-properties)
 

 		io_registry_create_iterator
 		io_registry_entry_from_path
 		io_registry_entry_get_name
+		io_service_close
 		io_service_open_extended
 		io_connect_method
 		io_service_add_interest_notification_64
```
