## postersyncd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
+		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
+		(require-not (global-name "com.apple.commcenter.xpc"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
+		(require-not (global-name "com.apple.imagent.embedded.auth"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))
 		(require-not (global-name "com.apple.contacts.CNContactsTestsEnvironmentServer"))
 		(require-not (global-name "com.apple.contactsd"))
+		(require-not (global-name "com.apple.SystemConfiguration.configd"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		MSC_semaphore_signal_trap
 		MSC_semaphore_wait_trap
 		MSC_semaphore_timedwait_trap
+		MSC__kernelrpc_mach_port_get_attributes_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_mach_msg2_trap
```
