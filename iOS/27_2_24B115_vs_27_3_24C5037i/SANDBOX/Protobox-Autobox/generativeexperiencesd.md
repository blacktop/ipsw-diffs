## generativeexperiencesd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.naturallanguaged"))
+		(require-not (global-name "com.apple.replicatorservices"))
 		(require-not (global-name "com.apple.TextInput.emoji"))
 		(require-not (require-any
 			(global-name "com.apple.proactive.PersonalizationPortrait.QuickType")

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
