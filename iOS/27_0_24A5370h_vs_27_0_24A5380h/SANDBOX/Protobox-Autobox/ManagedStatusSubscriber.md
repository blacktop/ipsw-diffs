## ManagedStatusSubscriber

> Group: ⬆️ Updated

```diff

 )
 
 (deny iokit-open-service)
+(allow iokit-open-service
+	(iokit-registry-entry-class "AppleKeyStore")
+)
 
 (deny iokit-set-properties)
 

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.mobilerepaird"))
+		(require-not (global-name "com.apple.enhancedloggingd.xpc"))
 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.managedconfiguration.mdmdservice"))
-		(require-not (global-name "com.apple.enhancedloggingd.xpc"))
+		(require-not (global-name "com.apple.mobilerepaird"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		io_registry_entry_from_path
 		io_service_open_extended
 		io_server_version
+		io_service_get_matching_service_bin
 		io_registry_entry_get_property_bin_buf
 		mach_port_request_notification
 		mach_port_set_attributes
```
