## ClarityBoard

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.hangtracerd"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (global-name "com.apple.healthd.server"))
-		(require-not (global-name "com.apple.rti-screencontinuity"))
 		(require-not (global-name "com.apple.systemstatus"))
 		(require-not (global-name "com.apple.biome.access.system"))
 		(require-not (global-name "com.apple.assistant.settings"))

 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.sandboxserver.xpc"))
 		(require-not (global-name "com.apple.geoanalyticsd"))
+		(require-not (require-any
+			(global-name "com.apple.remote-text-editing-legacy")
+			(global-name "com.apple.rti-screencontinuity")
+			(global-name "com.apple.sharing.remote-text-editing")
+		))
 		(require-not (global-name "com.apple.assistant.uibridge-service"))
 		(require-not (require-any
 			(global-name "com.apple.assistant.request-dispatcher.uibridge-service")

 		(require-not (global-name "com.apple.SharingServices"))
 		(require-not (global-name "com.apple.dt.xctestd.target"))
 		(require-not (global-name "com.apple.audio.AudioSession"))
+		(require-not (global-name "com.apple.bioconvenienced"))
 		(require-not (global-name "com.apple.campo"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.installcoordinationd"))

 		(require-not (global-name "com.apple.CarPlayApp.status-bar-service"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
 		(require-not (global-name "com.apple.coreduetd.context"))
+		(require-not (global-name "com.apple.rti-stagertool"))
 		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
 		(require-not (global-name "com.apple.imagent.embedded.auth"))
 		(require-not (global-name "com.apple.audio.AudioQueueServer"))

 		MSC_host_create_mach_voucher_trap
 		MSC__kernelrpc_mach_port_type_trap
 		MSC__kernelrpc_mach_port_request_notification_trap
+		MSC__exclaves_ctl_trap
 		MSC_mach_timebase_info_trap
 		MSC_mk_timer_create
 		MSC_mk_timer_destroy
```
