## CallAudioService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.videoconference.camera"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (system-attribute developer-mode))

 		MSC_mach_generate_activity_id
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
+		MSC_swtch_pri
 		MSC_syscall_thread_switch
 		MSC_host_create_mach_voucher_trap
 		MSC__kernelrpc_mach_port_type_trap

 (with-filter (mac-policy-name "AMFI")
 	(deny system-mac-syscall
 		(require-all
-			(require-not (mac-syscall-number 102))
-			(require-not (mac-syscall-number 96))
 			(require-not (mac-syscall-number 90))
+			(require-not (mac-syscall-number 96))
+			(require-not (mac-syscall-number 102))
 		)
 	)
 )
```
