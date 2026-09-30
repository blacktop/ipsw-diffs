## blastdoor-thumbnails

> Group: ⬆️ Updated

```diff

 )
 (allow file-read*
 	(require-all
-		(require-not (literal "/private/var"))
+		(require-not (literal "/dev"))
 		(require-not (require-any
 			(subpath "/AppleInternal/Library/VideoCodecs")
 			(subpath "/private/xarts")
 			(subpath "/usr/standalone/firmware")
 		))
+		(require-not (subpath "/private/var/MobileSoftwareUpdate"))
 		(require-not (subpath "/private/var/wireless/baseband_data"))
 		(require-not (subpath "/private/var/hardware"))
-		(require-not (literal "/dev"))
-		(require-not (subpath "/private/var/MobileSoftwareUpdate"))
+		(require-not (literal "/private/var"))
 		(require-any
 			(extension "com.apple.sandbox.executable")
-			(literal "/dev/null")
 			(literal "/dev/random")
 			(literal "/dev/urandom")
-			(literal "/dev/zero")
 			(literal "/private/etc/fstab")
 			(literal "/private/etc/hosts")
 			(literal "/private/etc/passwd")

 			(require-all
 				(file-mode #o0004)
 				(require-any
-					(literal "/private/etc/hosts")
+					(require-any
+						(literal "/private/etc/group")
+						(literal "/private/etc/protocols")
+					)
 					(subpath "/System")
 					(subpath "/private/var/db/timezone")
 					(subpath "/usr/lib")

 				(literal "/private/preboot")
 				(process-attribute is-apple-signed-executable)
 			)
+			(require-any
+				(literal "/dev/null")
+				(literal "/dev/zero")
+			)
 			(require-any
 				(literal "/private/etc/group")
 				(literal "/private/etc/protocols")

 			(literal "/private/var/preferences/Logging/com.apple.diagnosticd.filter.plist")
 			(literal "/tmp")
 			(require-all
-				(require-not (literal "/private/var"))
+				(require-not (literal "/dev"))
 				(require-not (require-any
 					(subpath "/AppleInternal/Library/VideoCodecs")
 					(subpath "/private/xarts")
 					(subpath "/usr/standalone/firmware")
 				))
+				(require-not (subpath "/private/var/MobileSoftwareUpdate"))
 				(require-not (subpath "/private/var/wireless/baseband_data"))
 				(require-not (subpath "/private/var/hardware"))
-				(require-not (literal "/dev"))
-				(require-not (subpath "/private/var/MobileSoftwareUpdate"))
+				(require-not (literal "/private/var"))
 				(require-any
 					(extension "com.apple.sandbox.executable")
-					(literal "/dev/null")
 					(literal "/dev/random")
 					(literal "/dev/urandom")
-					(literal "/dev/zero")
 					(literal "/private/etc/fstab")
 					(literal "/private/etc/hosts")
 					(literal "/private/etc/passwd")

 					(require-all
 						(file-mode #o0004)
 						(require-any
-							(literal "/private/etc/hosts")
+							(require-any
+								(literal "/private/etc/group")
+								(literal "/private/etc/protocols")
+							)
 							(subpath "/System")
 							(subpath "/private/var/db/timezone")
 							(subpath "/usr/lib")

 						(literal "/private/preboot")
 						(process-attribute is-apple-signed-executable)
 					)
+					(require-any
+						(literal "/dev/null")
+						(literal "/dev/zero")
+					)
 					(require-any
 						(literal "/private/etc/group")
 						(literal "/private/etc/protocols")

 )
 
 (allow file-write-data
+	(require-any
+		(literal "/dev/null")
+		(literal "/dev/zero")
+	)
+)
+(deny file-write-data
 	(require-all
-		(require-not (literal "/dev/dtracehelper"))
 		(require-any
 			(literal "/dev/null")
 			(literal "/dev/zero")
 		)
+		(literal "/dev/dtracehelper")
 	)
 )
 

 	(require-all
 		(iokit-registry-entry-class "IOPlatformDevice")
 		(require-any
-			(iokit-property "artwork-scale-factor")
 			(iokit-property "iommu-present")
 			(iokit-property "product-id")
 			(iokit-property "soc-generation")

 				(iokit-property "artwork-device-subtype")
 				(iokit-property "artwork-display-gamut")
 				(iokit-property "artwork-dynamic-displaymode")
+				(iokit-property "artwork-scale-factor")
 				(iokit-property "compatible-device-fallback")
 				(iokit-property "device-perf-memory-class")
 				(iokit-property "graphics-featureset-class")

 	(with no-report)
 	(require-all
 		(require-not (xpc-service-name "*"))
-		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.CARenderServer"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.coremedia.mediaparserd.utilities"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(global-name "com.apple.mobilegestalt.xpc")
+		(global-name "com.apple.analyticsd")
 	)
 )
 (deny mach-lookup
 	(require-all
 		(require-not (xpc-service-name "*"))
-		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.CARenderServer"))
-		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.coremedia.mediaparserd.utilities"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(global-name "com.apple.mobilegestalt.xpc")
+		(global-name "com.apple.analyticsd")
 	)
 )
 

 		(require-not (syscall-number SYS_necp_open))
 		(require-not (syscall-number SYS_necp_client_action))
 		(require-any
+			(require-all
+				(require-not (syscall-number SYS_iopolicysys))
+				(require-any
+					(syscall-number SYS___mac_syscall)
+					(syscall-number SYS_crossarch_trap)
+					(syscall-number SYS_dup)
+					(syscall-number SYS_fstatat)
+					(syscall-number SYS_fstatat64)
+					(syscall-number SYS_getfsstat)
+					(syscall-number SYS_getfsstat64)
+					(syscall-number SYS_map_with_linking_np)
+					(syscall-number SYS_memorystatus_control)
+					(syscall-number SYS_open)
+					(syscall-number SYS_openat)
+				)
+			)
 			(require-all
 				(state-flag "blastdoor-post-launch")
 				(require-any
 					(require-all
-						(syscall-number
-							SYS_open
-							SYS_getfsstat
-							SYS_crossarch_trap
-							SYS_dup
-							SYS_getfsstat64
-							SYS___mac_syscall
-							SYS_memorystatus_control
-							SYS_openat
-							SYS_fstatat
-							SYS_fstatat64
-							SYS_map_with_linking_np)
 						(require-not (syscall-number SYS_iopolicysys))
+						(require-any
+							(syscall-number SYS___mac_syscall)
+							(syscall-number SYS_crossarch_trap)
+							(syscall-number SYS_dup)
+							(syscall-number SYS_fstatat)
+							(syscall-number SYS_fstatat64)
+							(syscall-number SYS_getfsstat)
+							(syscall-number SYS_getfsstat64)
+							(syscall-number SYS_map_with_linking_np)
+							(syscall-number SYS_memorystatus_control)
+							(syscall-number SYS_open)
+							(syscall-number SYS_openat)
+						)
 					)
 					(syscall-number
 						SYS_pipe

 						SYS_freadlink)
 				)
 			)
-			(require-all
-				(syscall-number
-					SYS_open
-					SYS_getfsstat
-					SYS_crossarch_trap
-					SYS_dup
-					SYS_getfsstat64
-					SYS___mac_syscall
-					SYS_memorystatus_control
-					SYS_openat
-					SYS_fstatat
-					SYS_fstatat64
-					SYS_map_with_linking_np)
-				(require-not (syscall-number SYS_iopolicysys))
-			)
 			(require-all
 				(syscall-number
 					SYS_sigsuspend

 		(require-not (syscall-number SYS_necp_open))
 		(require-not (syscall-number SYS_necp_client_action))
 		(require-any
+			(require-all
+				(require-not (syscall-number SYS_iopolicysys))
+				(require-any
+					(syscall-number SYS___mac_syscall)
+					(syscall-number SYS_crossarch_trap)
+					(syscall-number SYS_dup)
+					(syscall-number SYS_fstatat)
+					(syscall-number SYS_fstatat64)
+					(syscall-number SYS_getfsstat)
+					(syscall-number SYS_getfsstat64)
+					(syscall-number SYS_map_with_linking_np)
+					(syscall-number SYS_memorystatus_control)
+					(syscall-number SYS_open)
+					(syscall-number SYS_openat)
+				)
+			)
 			(require-all
 				(state-flag "blastdoor-post-launch")
 				(require-any
 					(require-all
-						(syscall-number
-							SYS_open
-							SYS_getfsstat
-							SYS_crossarch_trap
-							SYS_dup
-							SYS_getfsstat64
-							SYS___mac_syscall
-							SYS_memorystatus_control
-							SYS_openat
-							SYS_fstatat
-							SYS_fstatat64
-							SYS_map_with_linking_np)
 						(require-not (syscall-number SYS_iopolicysys))
+						(require-any
+							(syscall-number SYS___mac_syscall)
+							(syscall-number SYS_crossarch_trap)
+							(syscall-number SYS_dup)
+							(syscall-number SYS_fstatat)
+							(syscall-number SYS_fstatat64)
+							(syscall-number SYS_getfsstat)
+							(syscall-number SYS_getfsstat64)
+							(syscall-number SYS_map_with_linking_np)
+							(syscall-number SYS_memorystatus_control)
+							(syscall-number SYS_open)
+							(syscall-number SYS_openat)
+						)
 					)
 					(syscall-number
 						SYS_pipe

 						SYS_freadlink)
 				)
 			)
-			(require-all
-				(syscall-number
-					SYS_open
-					SYS_getfsstat
-					SYS_crossarch_trap
-					SYS_dup
-					SYS_getfsstat64
-					SYS___mac_syscall
-					SYS_memorystatus_control
-					SYS_openat
-					SYS_fstatat
-					SYS_fstatat64
-					SYS_map_with_linking_np)
-				(require-not (syscall-number SYS_iopolicysys))
-			)
 			(require-all
 				(syscall-number
 					SYS_sigsuspend

 (allow syscall-mach
 	(with report)
 	(machtrap-number
-		MSC__kernelrpc_mach_vm_purgable_control_trap
-		MSC__kernelrpc_mach_port_insert_member_trap
 		MSC__kernelrpc_mach_port_destruct_trap
-		MSC_semaphore_signal_trap
-		MSC_semaphore_wait_trap
-		MSC_semaphore_timedwait_trap
 		MSC__kernelrpc_mach_port_guard_trap
-		MSC_swtch_pri
-		MSC_syscall_thread_switch
-		MSC__kernelrpc_mach_port_type_trap
+		MSC__kernelrpc_mach_port_insert_member_trap
 		MSC__kernelrpc_mach_port_request_notification_trap
+		MSC__kernelrpc_mach_port_type_trap
+		MSC__kernelrpc_mach_vm_purgable_control_trap
 		MSC_mk_timer_create
-		MSC_mk_timer_destroy)
+		MSC_mk_timer_destroy
+		MSC_semaphore_signal_trap
+		MSC_semaphore_timedwait_trap
+		MSC_semaphore_wait_trap
+		MSC_swtch_pri
+		MSC_syscall_thread_switch)
 )
 (allow syscall-mach
 	(with report)

 				MSC_task_self_trap
 				MSC_mach_generate_activity_id
 				MSC_swtch_pri
-				MSC_syscall_thread_switch
 				MSC_host_create_mach_voucher_trap
 				MSC__kernelrpc_mach_port_type_trap
 				MSC_mach_timebase_info_trap)

 				MSC_task_self_trap
 				MSC_mach_generate_activity_id
 				MSC_swtch_pri
-				MSC_syscall_thread_switch
 				MSC_host_create_mach_voucher_trap
 				MSC__kernelrpc_mach_port_type_trap
 				MSC_mach_timebase_info_trap)

 		(require-any
 			(require-any
 				(sysctl-name "hw.activecpu")
+				(sysctl-name "hw.machine")
+				(sysctl-name "hw.memsize")
 				(sysctl-name "hw.ncpu")
+				(sysctl-name "kern.osproductversion")
 				(sysctl-name "kern.osvariant_status")
 				(sysctl-name "kern.secure_kernel")
 			)

 				(sysctl-name "hw.physicalcpu_max")
 				(sysctl-name "hw.product")
 			)
-			(require-any
-				(sysctl-name "hw.machine")
-				(sysctl-name "kern.osproductversion")
-			)
 			(require-any
 				(sysctl-name "hw.optional.arm.caps")
 				(sysctl-name "hw.optional.neon_fp16")

 				(sysctl-name "kern.maxfilesperproc")
 				(sysctl-name "kern.osversion")
 			)
-			(sysctl-name "hw.memsize")
 			(sysctl-name "hw.osenvironment")
 			(sysctl-name "hw.pagesize_compat")
 			(sysctl-name "hw.physicalcpu")
```
