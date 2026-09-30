## blastdoor-messages

> Group: ⬆️ Updated

```diff

 (deny file-clone)
 (allow file-clone
 	(require-all
-		(extension "com.apple.blastdoor.read-write")
+		(extension "com.apple.app-sandbox.read-write")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/PassPreview")
-			(subpath "/private/var/tmp/com.apple.messages/PassPreview")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/Wallpapers")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FinanceUIService")
+			(subpath "/private/var/tmp/com.apple.messages/Wallpapers")
 		)
 	)
 )
 (allow file-clone
 	(require-all
-		(extension "com.apple.app-sandbox.read-write")
+		(extension "com.apple.blastdoor.read-write")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/tmp/com\.apple\.FinanceUIService($|/)")
 			)
 			(require-any

 			)
 			(require-any
 				(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/Wallpapers")
-				(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/Wallpapers/private/var/tmp/com.apple.messages/Wallpapers")
-				(subpath "${PROCESS_TEMP_DIR}/private/var/tmp/com.apple.messages/Wallpapers")
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FinanceUIService")
 				(subpath "/private/var/tmp/com.apple.messages/Wallpapers")
 			)

 )
 (allow file-read*
 	(require-all
-		(subpath "/private/var/tmp/com.apple.TelephonyUtilities/SharePlayActivityImages")
+		(extension "com.apple.app-sandbox.read-write")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/Wallpapers")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FinanceUIService")
+			(subpath "/private/var/tmp/com.apple.messages/Wallpapers")
+		)
+	)
+)
+(allow file-read*
+	(require-all
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.TelephonyUtilities/SharePlayActivityImages")
+			(subpath "/private/var/tmp/com.apple.TelephonyUtilities/SharePlayActivityImages")
+		)
 		(extension "com.apple.app-sandbox.read")
 	)
 )
 (allow file-read*
 	(require-all
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.imtransferagent")
+		(subpath "/private/var/tmp/com.apple.identityservicesd")
 		(extension "com.apple.app-sandbox.read")
 	)
 )

 )
 (allow file-read*
 	(require-all
-		(extension "com.apple.blastdoor.read-write")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/PassPreview")
-			(subpath "/private/var/tmp/com.apple.messages/PassPreview")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
+			(subpath "/private/var/tmp/com.apple.messages")
 		)
-	)
-)
-(allow file-read*
-	(require-all
-		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.identityservicesd")
-			(subpath "/private/var/tmp/com.apple.identityservicesd")
-		)
-		(extension "com.apple.app-sandbox.read")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "${PROCESS_TEMP_DIR}/com.apple.messages")
-		(extension "com.apple.app-sandbox.read")
-	)
-)
-(allow file-read*
-	(require-all
-		(require-any
-			(subpath "${HOME}/Library/Caches/${PROCESS_TEMP_DIR}/com.apple.CallKit.CallDirectory/LiveCallerID")
-			(subpath "${HOME}/Library/Caches/PassKit/PeerPaymentReceipts")
-			(subpath "${HOME}/Library/Caches/com.apple.businessservicesd/temp")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.CallKit.CallDirectory/LiveCallerID")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.facetimemessagestored/IncomingVideoVoiceMail")
-			(subpath "/private/var/tmp/com.apple.CallKit.CallDirectory/LiveCallerID")
-			(subpath "/private/var/tmp/com.apple.facetimemessagestored/IncomingVideoVoiceMail")
-		)
-		(extension "com.apple.app-sandbox.read")
-	)
-)
-(allow file-read*
-	(require-all
-		(subpath "/private/var/tmp/com.apple.imtransferagent")
 		(extension "com.apple.app-sandbox.read")
 	)
 )

 		(require-any
 			(subpath "${HOME}/Library/Photos/Libraries/Syndication.photoslibrary/scopes/syndication/originals")
 			(subpath "${HOME}/Media/PhotoData/UBF/scopes/syndication/originals")
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.TelephonyUtilities/SharePlayActivityImages")
 		)
 		(extension "com.apple.app-sandbox.read")
 	)
 )
 (allow file-read*
 	(require-all
-		(subpath "/private/var/tmp/com.apple.messages")
+		(require-any
+			(literal "${PROCESS_TEMP_DIR}/com.apple.facetimemessagestored/IncomingVideoVoiceMail")
+			(subpath "${HOME}/Library/Caches/PassKit/PeerPaymentReceipts${PROCESS_TEMP_DIR}/com.apple.CallKit.CallDirectory/LiveCallerID")
+			(subpath "/private/var/tmp/com.apple.facetimemessagestored/IncomingVideoVoiceMail")
+		)
 		(extension "com.apple.app-sandbox.read")
 	)
 )
 (allow file-read*
 	(require-all
-		(extension "com.apple.app-sandbox.read-write")
+		(require-any
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.imtransferagent")
+			(subpath "/private/var/tmp/com.apple.imtransferagent")
+		)
+		(extension "com.apple.app-sandbox.read")
+	)
+)
+(allow file-read*
+	(require-all
+		(subpath "${PROCESS_TEMP_DIR}/com.apple.identityservicesd")
+		(extension "com.apple.app-sandbox.read")
+	)
+)
+(allow file-read*
+	(require-all
+		(extension "com.apple.blastdoor.read-write")
 		(require-any
 			(require-all
 				(subpath "/private/var")

 			)
 			(require-any
 				(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/Wallpapers")
-				(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/Wallpapers/private/var/tmp/com.apple.messages/Wallpapers")
-				(subpath "${PROCESS_TEMP_DIR}/private/var/tmp/com.apple.messages/Wallpapers")
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FinanceUIService")
 				(subpath "/private/var/tmp/com.apple.messages/Wallpapers")
 			)

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

 				(extension "com.apple.app-sandbox.read")
 			)
 			(require-all
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

 		(literal "${FRONT_USER_HOME}")
 		(literal "${FRONT_USER_HOME}/Library/Preferences")
 		(require-not (literal "/private/var/run/syslog"))
-		(subpath "/Library/Preferences")
 	)
 )
 
 (allow file-write*
 	(require-all
-		(extension "com.apple.blastdoor.read-write")
+		(extension "com.apple.app-sandbox.read-write")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/PassPreview")
-			(subpath "/private/var/tmp/com.apple.messages/PassPreview")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/Wallpapers")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FinanceUIService")
+			(subpath "/private/var/tmp/com.apple.messages/Wallpapers")
 		)
 	)
 )
 (allow file-write*
 	(require-all
-		(extension "com.apple.app-sandbox.read-write")
+		(extension "com.apple.blastdoor.read-write")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/tmp/com\.apple\.FinanceUIService($|/)")
 			)
 			(require-any

 			)
 			(require-any
 				(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/Wallpapers")
-				(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/Wallpapers/private/var/tmp/com.apple.messages/Wallpapers")
-				(subpath "${PROCESS_TEMP_DIR}/private/var/tmp/com.apple.messages/Wallpapers")
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FinanceUIService")
 				(subpath "/private/var/tmp/com.apple.messages/Wallpapers")
 			)

 
 (allow file-write-data
 	(require-all
-		(extension "com.apple.blastdoor.read-write")
+		(extension "com.apple.app-sandbox.read-write")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/PassPreview")
-			(subpath "/private/var/tmp/com.apple.messages/PassPreview")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/Wallpapers")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FinanceUIService")
+			(subpath "/private/var/tmp/com.apple.messages/Wallpapers")
 		)
 	)
 )
 (allow file-write-data
 	(require-all
-		(extension "com.apple.app-sandbox.read-write")
+		(require-any
+			(literal "/dev/null")
+			(literal "/dev/zero")
+		)
+		(require-not (literal "/dev/dtracehelper"))
+	)
+)
+(allow file-write-data
+	(require-all
+		(extension "com.apple.blastdoor.read-write")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/tmp/com\.apple\.FinanceUIService($|/)")
 			)
 			(require-any

 			)
 			(require-any
 				(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/Wallpapers")
-				(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/Wallpapers/private/var/tmp/com.apple.messages/Wallpapers")
-				(subpath "${PROCESS_TEMP_DIR}/private/var/tmp/com.apple.messages/Wallpapers")
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FinanceUIService")
 				(subpath "/private/var/tmp/com.apple.messages/Wallpapers")
 			)
 		)
 	)
 )
-(allow file-write-data
-	(require-any
-		(literal "/dev/null")
-		(literal "/dev/zero")
-	)
-)
 
 (allow file-write-flags
 	(require-all
-		(extension "com.apple.blastdoor.read-write")
+		(extension "com.apple.app-sandbox.read-write")
 		(require-any
-			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/PassPreview")
-			(subpath "/private/var/tmp/com.apple.messages/PassPreview")
+			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/Wallpapers")
+			(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FinanceUIService")
+			(subpath "/private/var/tmp/com.apple.messages/Wallpapers")
 		)
 	)
 )
 (allow file-write-flags
 	(require-all
-		(extension "com.apple.app-sandbox.read-write")
+		(extension "com.apple.blastdoor.read-write")
 		(require-any
 			(require-all
-				(subpath "/private/var")
 				(require-any
 					(subpath "${FRONT_USER_HOME}")
 					(subpath "${HOME}")
 				)
+				(subpath "/private/var")
 				(regex #"^/private/var/(((mobile|euser[0-9]+)|[-0-9A-F]+)|Users/[^/]+)/Containers/(Temp/)?Data/[^/]+/[^/]+/tmp/com\.apple\.FinanceUIService($|/)")
 			)
 			(require-any

 			)
 			(require-any
 				(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/Wallpapers")
-				(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/Wallpapers/private/var/tmp/com.apple.messages/Wallpapers")
-				(subpath "${PROCESS_TEMP_DIR}/private/var/tmp/com.apple.messages/Wallpapers")
 				(subpath "/private/var/PersonaVolumes/[^/]+/Containers/Data/[^/]+/[^/]+/tmp/com.apple.FinanceUIService")
 				(subpath "/private/var/tmp/com.apple.messages/Wallpapers")
 			)

 			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/PassPreview")
 			(subpath "/private/var/tmp/com.apple.messages/PassPreview")
 		)
-		(require-not (extension "com.apple.blastdoor.read-write"))
-		(extension "com.apple.app-sandbox.read-write")
+		(require-not (extension "com.apple.app-sandbox.read-write"))
+		(extension "com.apple.blastdoor.read-write")
 	)
 )
 (deny file-write-flags

 			(subpath "${PROCESS_TEMP_DIR}/com.apple.messages/PassPreview")
 			(subpath "/private/var/tmp/com.apple.messages/PassPreview")
 		)
-		(require-not (extension "com.apple.blastdoor.read-write"))
-		(extension "com.apple.app-sandbox.read-write")
+		(require-not (extension "com.apple.app-sandbox.read-write"))
+		(extension "com.apple.blastdoor.read-write")
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
 

 		SYS_unlinkat
 		SYS_bsdthread_ctl
 		SYS_getentropy
+		SYS_ulock_wait
+		SYS_ulock_wake
 		SYS_fclonefileat
 		SYS_terminate_with_payload
 		SYS_abort_with_payload

 		SYS_shared_region_map_and_slide_2_np
 		SYS_pwritev
 		SYS_pwritev_nocancel
+		SYS_ulock_wait2
 		SYS_freadlink)
 )
 (allow syscall-unix

 					SYS_read
 					SYS_getpid
 					SYS_getuid
-					SYS_geteuid
 					SYS_crossarch_trap
 					SYS_getegid
 					SYS_sigaction
 					SYS_getgid
+					SYS_sigprocmask
 					SYS_readlink
 					SYS_munmap
 					SYS_mprotect

 					SYS_mkdir
 					SYS_pread
 					SYS_kdebug_typefilter
-					SYS_kdebug_trace_string
 					SYS_kdebug_trace64
 					SYS_getrlimit
 					SYS_mmap
 					SYS_lseek
 					SYS_getattrlist
+					SYS_shm_open
 					SYS_gettid
 					SYS_shared_region_check_np
 					SYS_issetugid

 					SYS_stat64_extended
 					SYS_getdirentries64
 					SYS_statfs64
+					SYS_getfsstat64
 					SYS_bsdthread_register
+					SYS_kevent_qos
 					SYS_kevent_id
 					SYS_read_nocancel
 					SYS_fsgetpath

 					SYS_persona
 					SYS_getentropy
 					SYS_os_fault_with_payload
+					SYS_shared_region_map_and_slide_2_np
 					SYS_map_with_linking_np
 					SYS_freadlink)
 				(require-not (state-flag "blastdoor-post-launch"))

 					SYS_rename
 					SYS_rmdir
 					SYS_pathconf
+					SYS_setrlimit
 					SYS_fsetattrlist
 					SYS_getxattr
+					SYS_fgetxattr
 					SYS_flistxattr
 					SYS_ffsctl
 					SYS_psynch_mutexwait

 					SYS_faccessat
 					SYS_mkdirat
 					SYS___channel_open
-					SYS_ulock_wait
-					SYS_ulock_wake
-					SYS_memorystatus_available_memory
-					SYS_ulock_wait2)
+					SYS_memorystatus_available_memory)
 				(state-flag "blastdoor-post-launch")
 			)
 		)

 		MSC__kernelrpc_mach_port_allocate_trap
 		MSC__kernelrpc_mach_port_construct_trap
 		MSC__kernelrpc_mach_port_deallocate_trap
+		MSC__kernelrpc_mach_port_guard_trap
 		MSC__kernelrpc_mach_port_insert_right_trap
 		MSC__kernelrpc_mach_port_mod_refs_trap
 		MSC__kernelrpc_mach_port_request_notification_trap

 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port)
 )
-(allow syscall-mach
-	(require-all
-		(require-not (state-flag "blastdoor-post-launch"))
-		(require-any
-			(machtrap-number
-				MSC_host_self_trap
-				MSC_mach_generate_activity_id
-				MSC_mach_msg2_trap
-				MSC_host_create_mach_voucher_trap)
-			(machtrap-number
-				MSC_mach_reply_port
-				MSC_task_self_trap
-				MSC_thread_get_special_reply_port
-				MSC_mach_timebase_info_trap)
-		)
-	)
-)
 (allow syscall-mach
 	(require-all
 		(machtrap-number
 			MSC__kernelrpc_mach_port_destruct_trap
-			MSC__kernelrpc_mach_port_insert_member_trap
 			MSC__kernelrpc_mach_port_type_trap
 			MSC__kernelrpc_mach_vm_purgable_control_trap
 			MSC_mk_timer_create
-			MSC_mk_timer_destroy
 			MSC_semaphore_signal_trap
 			MSC_semaphore_timedwait_trap
 			MSC_semaphore_wait_trap
-			MSC_syscall_thread_switch)
+			MSC_thread_get_special_reply_port)
 		(state-flag "blastdoor-post-launch")
 	)
 )
 (allow syscall-mach
 	(require-all
-		(machtrap-number MSC__kernelrpc_mach_port_guard_trap)
+		(machtrap-number
+			MSC_mach_reply_port
+			MSC_task_self_trap
+			MSC_host_self_trap
+			MSC_mach_generate_activity_id
+			MSC_mach_msg2_trap
+			MSC_thread_get_special_reply_port
+			MSC_host_create_mach_voucher_trap
+			MSC_mach_timebase_info_trap)
+		(require-not (state-flag "blastdoor-post-launch"))
+	)
+)
+(allow syscall-mach
+	(require-all
+		(machtrap-number
+			MSC__kernelrpc_mach_port_insert_member_trap
+			MSC_mach_msg2_trap
+			MSC_syscall_thread_switch
+			MSC_mk_timer_destroy)
 		(require-any
 			(machtrap-number
+				MSC_mach_reply_port
+				MSC_task_self_trap
 				MSC_host_self_trap
 				MSC_mach_generate_activity_id
 				MSC_mach_msg2_trap
-				MSC_host_create_mach_voucher_trap)
+				MSC_thread_get_special_reply_port
+				MSC_host_create_mach_voucher_trap
+				MSC_mach_timebase_info_trap)
 			(state-flag "blastdoor-post-launch")
 		)
 	)

 (deny syscall-mig)
 (allow syscall-mig
 	(kernel-mig-routine
+		host_info
 		host_get_io_master
 		mach_exception_raise
 		mach_exception_raise_state
 		mach_exception_raise_state_identity
 		io_server_version
 		io_registry_entry_get_property_bin_buf
+		mach_port_get_context_from_user
 		task_info_from_user
 		task_get_special_port_from_user
 		semaphore_create

 					io_registry_entry_from_path
 					mach_port_request_notification
 					mach_port_set_attributes
-					mach_port_get_context_from_user
 					mach_port_is_connection_for_service
 					semaphore_destroy
 					thread_info
 					thread_policy_set
 					mach_vm_copy
-					mach_vm_region)
+					mach_vm_region
+					mach_vm_reallocate)
 				(state-flag "blastdoor-post-launch")
 			)
 			(require-all
 				(require-not (state-flag "blastdoor-post-launch"))
 				(require-any
 					(kernel-mig-routine
+						host_info
 						host_get_io_master
+						host_get_clock_service
 						host_get_special_port
+						io_iterator_next
 						io_registry_create_iterator
 						io_registry_entry_get_name
 						io_registry_entry_get_property_bytes
-						mach_ports_lookup)
-					(kernel-mig-routine
-						host_info
-						host_get_clock_service
-						io_object_conforms_to
-						io_iterator_next
 						io_server_version
 						io_registry_entry_get_property_bin_buf
 						task_info_from_user

 						task_set_special_port
 						semaphore_create
 						mach_vm_map_external
-						mach_vm_range_create
 						task_restartable_ranges_register
 						task_restartable_ranges_synchronize)
+					(kernel-mig-routine io_object_conforms_to)
+					(kernel-mig-routine mach_ports_lookup)
+					(kernel-mig-routine mach_vm_range_create)
 				)
 			)
 		)

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
