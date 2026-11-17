## bulletindistributord

> Group: ⬆️ Updated

```diff

 
 (deny iokit-open-service)
 (allow iokit-open-service
-	(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationDriver")
+	(require-any
+		(iokit-registry-entry-class "AppleM2ScalerCSCDriver")
+		(iokit-registry-entry-class "AppleM2ScalerParavirtDriver")
+		(iokit-registry-entry-class "AppleVideoToolboxParavirtualizationDriver")
+	)
 )
 
 (deny iokit-set-properties)

 		io_registry_create_iterator
 		io_registry_entry_from_path
 		io_registry_entry_get_name
+		io_service_close
 		io_service_open_extended
 		io_connect_method
 		io_connect_async_method
```
