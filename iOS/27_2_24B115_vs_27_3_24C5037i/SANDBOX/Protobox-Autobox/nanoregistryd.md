## nanoregistryd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.rtcreportingd"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (global-name "com.apple.appconduitd.application-manager"))
 		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))

 		(require-not (global-name "com.apple.NPKNanoPassDaemonConnection.XPC"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.terminusd"))
+		(require-not (global-name "com.apple.EligibilityQuorum.com.apple.AudioIntelligence"))
 		(require-not (global-name "com.apple.seld.tsmmanager"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))

 		MSC_semaphore_signal_trap
 		MSC_semaphore_wait_trap
 		MSC_semaphore_timedwait_trap
+		MSC__kernelrpc_mach_port_get_attributes_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_task_name_for_pid

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
```
