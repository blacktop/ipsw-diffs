## textcontextd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.TextInput.accessibility"))
 		(require-not (global-name "com.apple.CARenderServer"))
+		(require-not (global-name "com.apple.healthd.server"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))

 		io_connect_method
 		io_connect_async_method
 		io_connect_set_notification_port_64
+		io_service_add_interest_notification_64
 		io_registry_entry_get_registry_entry_id
 		io_service_get_matching_service
 		io_server_version

 		F_RDADVISE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
+		F_DUPFD_CLOEXEC
 		F_OFD_GETLK
 		F_ADDFILESIGS_RETURN
 		F_CHECK_LV)
```
