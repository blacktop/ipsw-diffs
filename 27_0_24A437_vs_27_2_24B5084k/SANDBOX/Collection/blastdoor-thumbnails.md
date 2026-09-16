## blastdoor-thumbnails

> Group: ⬆️ Updated

```diff

 
 (deny mach-cross-domain-lookup)
 
+(allow mach-lookup
+	(global-name "com.apple.analyticsd")
+)
 (deny mach-lookup
 	(with no-report)
 	(require-all

 		SYS_abort_with_payload
 		SYS_pwritev
 		SYS_pwritev_nocancel
+		SYS_proc_info_extended_id
 		SYS_map_with_linking_np)
 )
 (allow syscall-unix
```
