## blastdoor-messages

> Group: ⬆️ Updated

```diff

 
 (deny mach-cross-domain-lookup)
 
-(allow mach-lookup
-	(global-name "com.apple.analyticsd")
-)
 (deny mach-lookup
 	(with no-report)
 	(require-all

 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port)
 )
+(allow syscall-mach
+	(require-all
+		(require-not (state-flag "blastdoor-post-launch"))
+		(require-any
+			(machtrap-number
+				MSC_mach_reply_port
+				MSC_task_self_trap
+				MSC_host_self_trap
+				MSC_mach_generate_activity_id
+				MSC_mach_msg2_trap
+				MSC_host_create_mach_voucher_trap
+				MSC_mach_timebase_info_trap)
+			(machtrap-number MSC_thread_get_special_reply_port)
+		)
+	)
+)
 (allow syscall-mach
 	(require-all
 		(machtrap-number

 		(state-flag "blastdoor-post-launch")
 	)
 )
-(allow syscall-mach
-	(require-all
-		(machtrap-number
-			MSC_mach_reply_port
-			MSC_task_self_trap
-			MSC_host_self_trap
-			MSC_mach_generate_activity_id
-			MSC_mach_msg2_trap
-			MSC_thread_get_special_reply_port
-			MSC_host_create_mach_voucher_trap
-			MSC_mach_timebase_info_trap)
-		(require-not (state-flag "blastdoor-post-launch"))
-	)
-)
 (allow syscall-mach
 	(require-all
 		(machtrap-number

 				MSC_host_self_trap
 				MSC_mach_generate_activity_id
 				MSC_mach_msg2_trap
-				MSC_thread_get_special_reply_port
 				MSC_host_create_mach_voucher_trap
 				MSC_mach_timebase_info_trap)
 			(state-flag "blastdoor-post-launch")
```
