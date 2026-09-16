## blastdoor-ids

> Group: ⬆️ Updated

```diff

 (deny mach-cross-domain-lookup)
 
 (deny mach-derive-port)
+(allow mach-derive-port
+	(global-name "com.apple.analyticsd")
+)
 
+(allow mach-lookup
+	(global-name "com.apple.analyticsd")
+)
 (deny mach-lookup
 	(with no-report)
 	(require-all

 		SYS_shared_region_map_and_slide_2_np
 		SYS_pwritev
 		SYS_pwritev_nocancel
+		SYS_proc_info_extended_id
 		SYS_map_with_linking_np)
 )
 (allow syscall-unix
```
