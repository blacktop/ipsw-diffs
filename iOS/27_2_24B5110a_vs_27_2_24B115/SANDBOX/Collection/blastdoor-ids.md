## blastdoor-ids

> Group: ⬆️ Updated

```diff

 (deny mach-cross-domain-lookup)
 
 (deny mach-derive-port)
-(allow mach-derive-port
-	(global-name "com.apple.analyticsd")
-)
 
-(allow mach-lookup
-	(global-name "com.apple.analyticsd")
-)
 (deny mach-lookup
 	(with no-report)
 	(require-all
```
