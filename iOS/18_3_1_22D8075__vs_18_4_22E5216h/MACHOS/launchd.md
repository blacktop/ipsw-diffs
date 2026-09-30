## launchd

> `/sbin/launchd`

```diff

-2866.80.6.0.0
-  __TEXT.__text: 0x4fdec
-  __TEXT.__auth_stubs: 0x2060
+2894.100.80.0.0
+  __TEXT.__text: 0x512e8
+  __TEXT.__auth_stubs: 0x2110
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1f4
-  __TEXT.__const: 0x2e0
-  __TEXT.__cstring: 0x13f82
+  __TEXT.__const: 0x2f0
+  __TEXT.__cstring: 0x14783
   __TEXT.__launchd: 0x1
   __TEXT.__objc_methname: 0x8
   __TEXT.__objc_classname: 0x1ba

   __TEXT.__config: 0x2544
   __TEXT.__dof_launchd: 0x67c
   __TEXT.__unwind_info: 0x11b8
-  __DATA_CONST.__auth_got: 0x1030
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x4fa8
+  __DATA_CONST.__auth_got: 0x1088
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__auth_ptr: 0x30
+  __DATA_CONST.__const: 0x5270
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA.__objc_const: 0xbd0
   __DATA.__objc_selrefs: 0x8
   __DATA.__objc_data: 0x690
-  __DATA.__data: 0x880
+  __DATA.__data: 0x8d8
   __DATA.__os_assumes_log: 0x8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xe48
-  __DATA.__common: 0x584
+  __DATA.__bss: 0xe70
+  __DATA.__common: 0x804
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 1589
-  Symbols:   571
-  CStrings:  2570
+  Functions: 1633
+  Symbols:   582
+  CStrings:  2621
 
Symbols:
+ _fchown
+ _fstatat
+ _os_map_64_clear
+ _os_map_64_count
+ _os_map_64_delete
+ _os_map_64_destroy
+ _os_map_64_find
+ _os_map_64_foreach
+ _os_map_64_init
+ _os_map_64_insert
+ _proc_signal_delegate
+ _proc_terminate
+ _proc_terminate_delegate
+ _unlinkat
- _posix_spawnattr_set_use_sec_transition_shims_np
- _proc_signal_with_audittoken
- _proc_terminate_with_audittoken
CStrings:
+ " (initiated by %s)"
+ "#IfNotVariant"
+ "#IfVariant"
+ "%5d %10d   %-25s   %s"
+ "%s => (timeout = %hus, consecutive crash count = %hu/%hu)"
+ "%s: inserting zero urgent log submission key"
+ "%s: urgent log submission key already in map: 0x%llx"
+ "%s: urgent log submission key already in stats: 0x%llx"
+ "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Sat Feb 22 03:16:54 PST 2025; root:libxpc_executables-2894.100.80~21/launchd/RELEASE_ARM64E"
+ "Cannot remove old socket path; UIDs mismatch: socket owner = %d, path = %d"
+ "ConsecutiveCrashCount"
+ "Darwin Bootstrapper Version 7.0.0: Sat Feb 22 03:16:54 PST 2025; root:libxpc_executables-2894.100.80~21/launchd/RELEASE_ARM64E"
+ "Entitlements element not allowed"
+ "Expected string for a variant, got %s"
+ "Failed to bind() a socket: path=%s, error=%s (%d)"
+ "Failed to connect() a socket: path=%s, error=%s (%d)"
+ "Failed to fchown() secure socket directory: error=%s (%d)"
+ "Failed to fchownat() a socket: error=%s (%d)"
+ "Failed to fstatat() old socket path: path=%s, error=%s (%d)"
+ "Failed to unlinkat() old socket path: path=%s, error=%s (%d)"
+ "Improper type for %s"
+ "Invalid type given for bootstrap path sanitization"
+ "JETSAM_REASON_MEMORY_LONGIDLE_EXIT"
+ "Old socket path is not a socket; path=%s"
+ "Setting service %s to %s"
+ "SpawnConstraint is invalid - %d %s"
+ "SubmissionTimeout"
+ "UTC Time element not allowed"
+ "Unable to apply LWCR (spawn constraint) - %d %s"
+ "Unknown DER entitlements encoding"
+ "Unknown UTC Time encoding"
+ "Unknown numeric string encoding"
+ "XPC_USERSPACE_PIVOTEDROOT"
+ "_UrgentLogSubmission"
+ "after the userspace pivot & reboot, os_variant_is_basesystem() should not be true"
+ "auto-completing urgent log submission for pid = %d, version = %d"
+ "clearing pending urgent log submission for %s; pid = %d, version = %d"
+ "com.apple.private.xpc.launchd.allowed-complete-urgent-log-submission"
+ "completed urgent log submission for %s; pid = %d, version = %d, rtt = %llus"
+ "config = {"
+ "deferred services = {"
+ "der_decode_entitlements"
+ "der_decode_numeric_string"
+ "der_decode_utc_time"
+ "inserted pending urgent log submission; pid = %d, version = %d, pushout = %zus"
+ "kGUARD_EXC_DEALLOC_GAP"
+ "kGUARD_EXC_RECLAIM_COPYIO_FAILURE"
+ "kGUARD_EXC_RECLAIM_DEALLOCATE_FAILURE"
+ "kGUARD_EXC_RECLAIM_INDEX_FAILURE"
+ "kGUARD_EXC_SEC_ACCESS_FAULT"
+ "kGUARD_EXC_SEC_COPY_DENIED"
+ "kGUARD_EXC_SEC_LOOKUP_DENIED"
+ "kGUARD_EXC_SEC_RANGE_DENIED"
+ "kGUARD_EXC_SEC_SHARING_DENIED"
+ "lwcr"
+ "numeric string element not allowed"
+ "pending submissions = {"
+ "pid-version"
+ "post-upgrade"
+ "service spawn deferred by %llu seconds due to %s"
+ "spawning %zu deferred services"
+ "spawning after urgent log submission completion"
+ "throttle"
+ "urgent log submission"
+ "urgent log submission = {"
+ "urgent log submission completed, pushing out %llu more seconds"
+ "urgent log submission completion initiated by: %s (pid = %d, version = %d)"
+ "v20@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}ICIIC{?=II}**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8i16"
+ "v24@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}ICIIC{?=II}**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8^v16"
+ "v28@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}ICIIC{?=II}**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8B16^{_launch_lint_s=@?*B}20"
+ "v32@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}ICIIC{?=II}**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8*16^{_launch_lint_s=@?*B}24"
+ "v32@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}ICIIC{?=II}**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8^v16^{_launch_lint_s=@?*B}24"
+ "v32@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1}ICIIC{?=II}**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8q16^{_launch_lint_s=@?*B}24"
- "%s service %s"
- "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Mon Dec 16 16:01:34 PST 2024; root:libxpc_executables-2866.80.6~5/launchd/RELEASE_ARM64E"
- "Cannot remove old socket path; UIDs mismatch: socket = %d, path = %d"
- "Darwin Bootstrapper Version 7.0.0: Mon Dec 16 16:01:34 PST 2024; root:libxpc_executables-2866.80.6~5/launchd/RELEASE_ARM64E"
- "Disabling"
- "Enabling"
- "Failed to bind() a socket: error=%s (%d)"
- "Failed to chown() secure socket directory: error=%s (%d)"
- "Failed to fchown() a socket: error=%s (%d)"
- "Failed to remove old socket: error=%s (%d)"
- "Failed to stat() old socket path: path=%s, error=%s (%d)"
- "after the userspace reboot, os_variant_is_basesystem() should not be true"
- "attempting to enter REM"
- "enable sec_transition shim"
- "sec-transition"
- "service throttled by %llu seconds"
- "v20@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**Si^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1}ICIIC{?=II}**b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8i16"
- "v24@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**Si^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1}ICIIC{?=II}**b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8^v16"
- "v28@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**Si^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1}ICIIC{?=II}**b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8B16^{_launch_lint_s=@?*B}20"
- "v32@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**Si^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1}ICIIC{?=II}**b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8*16^{_launch_lint_s=@?*B}24"
- "v32@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**Si^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1}ICIIC{?=II}**b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8^v16^{_launch_lint_s=@?*B}24"
- "v32@?0^{_launch_service_s={_launch_obj_header_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^********^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}**Q*I*I^v^v^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}II[16I]i**Si^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I*II^{?}IiiiiiQIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}I{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b24b1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=I{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1}ICIIC{?=II}**b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8q16^{_launch_lint_s=@?*B}24"

```
