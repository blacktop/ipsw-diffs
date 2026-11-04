## DTServiceHub

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.iconservices"))
+		(require-not (global-name "com.apple.ClipServices.clipserviced"))
 		(require-not (global-name "com.apple.lsd.xpc"))
 		(require-not (global-name "com.apple.coresymbolicationd"))
 		(require-not (global-name "com.apple.PineBoardServices"))

 		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
-		(require-not (global-name "com.apple.ClipServices.clipserviced"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))
 	)

 			(sysctl-name "kperf.timer.action")
 			(sysctl-name "kperf.timer.period")
 		))
+		(require-not (sysctl-name "kpc.force_all_ctrs"))
 		(require-not (require-any
 			(sysctl-name "kperf.lightweight_pet")
 			(sysctl-name "kperf.timer.pet_timer")
 		))
-		(require-not (sysctl-name "kpc.force_all_ctrs"))
 		(require-not (sysctl-name "kern.memorystatus_vm_pressure_send"))
 		(require-not (sysctl-name "kern.grade_cputype"))
 		(require-not (sysctl-name "kern.wq_limit_cooperative_threads"))

 
 (deny system-kas-info)
 
-(with-filter (mac-policy-name "Sandbox")
-	(deny system-mac-syscall
-		(require-all
-			(require-not (mac-syscall-number 7))
-			(require-not (mac-syscall-number 6))
-			(require-not (mac-syscall-number 5))
-			(require-not (mac-syscall-number 4))
-			(require-not (mac-syscall-number 67))
-			(require-not (mac-syscall-number 2))
-		)
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
