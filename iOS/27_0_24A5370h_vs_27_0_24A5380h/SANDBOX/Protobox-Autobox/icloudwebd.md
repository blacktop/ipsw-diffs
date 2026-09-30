## icloudwebd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.mobileasset.autoasset"))
-		(require-not (global-name "com.apple.aa.daemon.xpc"))
-		(require-not (global-name "com.apple.bird"))
+		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.identityservicesd.idquery.embedded.auth"))
 		(require-not (global-name "com.apple.cdp.daemon"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.intelligenceplatform.EntityResolution"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.gpumemd.source"))
-		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
-		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.apsd"))
 		(require-not (global-name "com.apple.kvsd"))
 		(require-not (global-name "com.apple.assistant.cdm"))
+		(require-not (global-name "com.apple.bird"))
+		(require-not (global-name "com.apple.aa.daemon.xpc"))
 		(require-not (global-name "com.apple.intelligenceplatform.View"))
+		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.privacyaccountingd"))
 		(require-not (global-name "com.apple.proactive.PersonalizationPortrait.Contact"))
+		(require-not (global-name "com.apple.mediaanalysisd.service.public"))
+		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (system-attribute developer-mode))
 	)

 		MSC_pid_for_task
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
+		MSC_swtch_pri
 		MSC_syscall_thread_switch
 		MSC_host_create_mach_voucher_trap
 		MSC__kernelrpc_mach_port_type_trap
```
