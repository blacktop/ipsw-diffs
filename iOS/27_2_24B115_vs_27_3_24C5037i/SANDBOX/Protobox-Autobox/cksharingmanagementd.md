## cksharingmanagementd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.identityservicesd.idquery.embedded.auth"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (require-any
 			(global-name "com.apple.cloudkit.audience-provider.com.apple.family")
 			(global-name "com.apple.cloudkit.audience-provider.com.apple.people.circles")
 		))
-		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.cloudd"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 			SYS_lseek
 			SYS_sysctl
 			SYS_getumask
+			SYS_open_dprotected_np
 			SYS_openat_dprotected_np
 			SYS_fgetattrlist
 			SYS_fgetxattr

 			SYS_fstatat
 			SYS_fstatat64
 			SYS_mkdirat
+			SYS_guarded_open_dprotected_np
 			SYS_persona
 			SYS_terminate_with_payload
 			SYS_abort_with_payload

 		(require-all
 			(require-not (mac-syscall-number 95))
 			(require-not (mac-syscall-number 96))
-			(require-not (mac-syscall-number 90))
 			(require-not (mac-syscall-number 102))
+			(require-not (mac-syscall-number 90))
 		)
 	)
 )
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 4)
+		(require-not (mac-policy-name "Sandbox"))
+	)
+)
 (deny system-mac-syscall
 	(require-any
 		(require-not (mac-policy-name "Sandbox"))
```
