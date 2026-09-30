## remotemanagementd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.apsd"))

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.AuthenticationServices.ASConfigurationSubscriber")
+			(xpc-service-name "com.apple.CRShipModeDDMSubscriber")
 			(xpc-service-name "com.apple.remotemanagement.AccountSubscriber")
 			(xpc-service-name "com.apple.remotemanagement.InteractiveLegacyProfilesSubscriber")
 			(xpc-service-name "com.apple.remotemanagement.LegacyProfilesSubscriber")

 		SYS_os_fault_with_payload
 		SYS_memorystatus_available_memory
 		SYS_objc_bp_assist_cfg_np
+		SYS_shared_region_map_and_slide_2_np
 		SYS_preadv
 		SYS_pwritev
 		SYS_preadv_nocancel
```
