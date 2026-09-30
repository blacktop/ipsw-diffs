## blastdoor-thumbnails

> Group: ⬆️ Updated

```diff

 
 (deny mach-cross-domain-lookup)
 
-(allow mach-lookup
-	(global-name "com.apple.analyticsd")
-)
 (deny mach-lookup
 	(with no-report)
 	(require-all
```
