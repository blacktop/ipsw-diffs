## healthcontentd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.coremedia.mediaplaybackd.assetcacheinspector.xpc"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.figcpecryptor.xpc"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.customurlloader.xpc"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))

 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.asset.xpc"))
 		(require-not (global-name "com.apple.xpc.amsengagementd"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.coremedia.figcontentkeyboss.xpc"))
+		(require-not (global-name "com.apple.cache_delete.public"))
 		(require-not (global-name "com.apple.amsservicesanalytics.xpc"))
 		(require-not (global-name "com.apple.fairplaydeviceidentityd"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))

 			SYS_change_fdguard_np
 			SYS_openat
 			SYS_renameat
+			SYS_faccessat
 			SYS_fstatat
 			SYS_fstatat64
 			SYS_mkdirat

 		io_connect_unmap_memory_from_task
 		io_connect_method
 		io_connect_set_notification_port_64
+		io_service_add_interest_notification_64
 		io_service_set_authorization_id
 		io_server_version
 		io_service_get_matching_service_bin

 (deny system-fsctl)
 (allow system-fsctl
 	(fsctl-command
+		APFSIOC_DIR_STATS_OP
 		APFSIOC_GET_CLONE_INFO
 		APFSIOC_GET_PURGEABLE_FILE_FLAGS
 		APFSIOC_PURGEABLE_GET_FILE_INFO
```
