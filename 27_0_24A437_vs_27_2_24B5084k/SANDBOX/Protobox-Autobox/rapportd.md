## rapportd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.userprofiles"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.homehubd.manage"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))

 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.findmy.findmylocate.locationservice"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.sharing.airdrop.service"))

 		io_server_version
 		io_service_get_matching_service_bin
 		io_service_get_matching_services_bin
+		io_service_add_notification_bin_64
 		io_registry_entry_get_properties_bin_buf
 		io_registry_entry_get_property_bin_buf
 		mach_port_destroy
```
