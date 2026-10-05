## uarphidd

> Group: ⬆️ Updated

```diff

 
 (deny mach-issue-extension)
 
-(deny mach-lookup)
+(deny mach-lookup
+	(require-all
+		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.FileCoordination"))
+		(require-not (system-attribute developer-mode))
+	)
+)
 
 (deny process-exec*)
 

 		mach_exception_raise_state_identity
 		io_object_conforms_to
 		io_iterator_next
+		io_service_close
 		io_connect_map_memory
 		io_registry_get_root_entry
 		io_service_add_interest_notification
```
