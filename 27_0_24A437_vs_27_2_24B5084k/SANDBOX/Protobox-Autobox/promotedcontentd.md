## promotedcontentd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.appstored.xpc"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.modelmanager"))

 		host_info
 		host_get_io_master
 		host_get_clock_service
+		host_statistics_from_user
 		host_request_notification
 		host_get_special_port
 		clock_get_time
```
