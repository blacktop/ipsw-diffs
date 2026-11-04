## temporary-sandbox

> Group: ⬆️ Updated

```diff

 ;; (default) inherited from parent profile "baseline"
 (delegate default)
 
-(allow asr-parser-enter)
-
 (allow coalition-info)
 
 (allow consume-extension)

 
 (allow system-kas-info
 	(require-all
-		(system-attribute developer-mode)
 		(system-attribute internal-build)
 		(kas-info-selector KAS_INFO_KERNEL_TEXT_SLIDE_SELECTOR)
 		(process-path "/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/DTServiceHub")
+		(system-attribute developer-mode)
 	)
 )
 (deny system-kas-info)
```
