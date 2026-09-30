## mediaremoted

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.coremedia.endpoint.xpc"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.intelligentroutingd.xpc.media"))

 	(ioctl-command
 		CTLIOCGINFO
 		SIOCGCONNINFO
+		SIOCGIFAGENTDATA
 		SIOCGIFCONSTRAINED
 		SIOCGIFDELEGATE
 		SIOCGIFEXPENSIVE

 		io_server_version
 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
+		io_service_add_notification_bin_64
 		io_device_tree_entry_exists_with_name
 		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf

 		NECP_CLIENT_ACTION_COPY_RESULT
 		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
+		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT_FINAL
 		NECP_CLIENT_ACTION_MAP_SYSCTLS
 		NECP_CLIENT_ACTION_REMOVE
 		NECP_CLIENT_ACTION_REMOVE_FLOW
```
