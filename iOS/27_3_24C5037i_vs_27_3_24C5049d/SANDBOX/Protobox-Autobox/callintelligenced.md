## callintelligenced

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.SocialHighlight"))
 		(require-not (global-name "com.apple.coremedia.routediscoverer.xpc"))

 		MSC_host_create_mach_voucher_trap
 		MSC__kernelrpc_mach_port_type_trap
 		MSC__kernelrpc_mach_port_request_notification_trap
+		MSC__exclaves_ctl_trap
 		MSC_mach_timebase_info_trap
 		MSC_mk_timer_create
 		MSC_mk_timer_destroy
```
