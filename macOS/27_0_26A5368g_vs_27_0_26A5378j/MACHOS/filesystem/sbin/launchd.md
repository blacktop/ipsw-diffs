## launchd

> `/sbin/launchd`

```diff

-  __TEXT.__text: 0x5965c
-  __TEXT.__auth_stubs: 0x2300
+  __TEXT.__text: 0x5a804
+  __TEXT.__auth_stubs: 0x2390
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x20c
-  __TEXT.__const: 0x490
+  __TEXT.__const: 0x4a0
   __TEXT.__launchd: 0x1
   __TEXT.__constg_swiftt: 0xf8
   __TEXT.__swift5_typeref: 0x5e

   __TEXT.__swift5_fieldmd: 0x60
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__cstring: 0x1686b
+  __TEXT.__cstring: 0x16afc
   __TEXT.__swift5_capture: 0x14
   __TEXT.__objc_methtype: 0xf
   __TEXT.__objc_classname: 0x212
   __TEXT.__objc_methname: 0x1c
+  __TEXT.__gcc_except_tab: 0xa8
+  __TEXT.__oslogstring: 0xd5
   __TEXT.__config: 0x3b2f
   __TEXT.__dof_launchd: 0x81d
-  __TEXT.__unwind_info: 0x1040
+  __TEXT.__unwind_info: 0x10b8
   __TEXT.__eh_frame: 0x210
-  __DATA_CONST.__const: 0x57e0
+  __DATA_CONST.__const: 0x58c8
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__auth_got: 0x1180
-  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__auth_got: 0x11d0
+  __DATA_CONST.__got: 0x210
   __DATA_CONST.__auth_ptr: 0x80
   __DATA.__objc_const: 0xdf0
   __DATA.__objc_selrefs: 0x8
   __DATA.__objc_data: 0x6e0
-  __DATA.__data: 0xa78
+  __DATA.__data: 0xa80
   __DATA.__os_assumes_log: 0x8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xd98
-  __DATA.__common: 0x808
+  __DATA.__common: 0x800
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libauditd.0.dylib
   - /usr/lib/libbsm.0.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftDarwin.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  Functions: 1438
-  Symbols:   645
-  CStrings:  2829
+  Functions: 1460
+  Symbols:   656
+  CStrings:  2851
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__dof_launchd : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__os_assumes_log : content changed
Symbols:
+ __Unwind_Resume
+ __ZSt9terminatev
+ ___assert_rtn
+ ___cxa_begin_catch
+ ___gxx_personality_v0
+ ___mac_syscall
+ __os_log_default
+ __os_log_impl
+ _fgetxattr
+ _malloc_type_free
+ _os_log_type_enabled
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YpZto6/Binaries/libxpc_executables/install/Symbols/launchd"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YpZto6/Sources/libxpc_executables/launchd/domain.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YpZto6/Sources/libxpc_executables/launchd/service_create.c"
+ "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Tue Jun 30 21:09:36 PDT 2026; root:libxpc_executables-3298.0.10~59/launchd/RELEASE_ARM64E"
+ "Darwin Bootstrapper Version 7.0.0: Tue Jun 30 21:09:36 PDT 2026; root:libxpc_executables-3298.0.10~59/launchd/RELEASE_ARM64E"
+ "DisableAllowed"
+ "Failed to pack event for downcall using ES syscall %d"
+ "Failed to submit event using ES syscall %d: %d %s"
+ "Ignoring disabled state because DisableAllowed=false: %s"
+ "Invalid enum value on pack: %d\n"
+ "Is this process entitled properly for submitting events to EndpointSecurity?"
+ "Maybe.h"
+ "PackedDataBuffer.cpp"
+ "Queue.h"
+ "SentinelA"
+ "_Quarantined"
+ "cannot spawn: service plist has the quarantine extended attribute"
+ "com.apple.quarantine"
+ "ess bootstrap_look_up: audit_token_for_pid(%d) → %d for service %s, JOB arm"
+ "ess bootstrap_look_up: endpoint owner == NULL for service %s"
+ "exists()"
+ "force-enabled"
+ "pushBackMulti"
+ "quarantined"
+ "size >= sizeof(uint64_t)"
+ "src != (A *)data_"
+ "team-identifier"
+ "v16@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{_launch_domain_s}^v^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^*****^v^v*^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}***Q**[16C]^v*I^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}^{dispatch_source_s}**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I^{dispatch_source_s}*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIiIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}IC{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b4b20CSib1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1C}^{_launch_attribution_node_s}ICIIiCC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8"
+ "v20@?0^{_launch_io_s={_launch_object_s=^vB}{?={_xpc_token_s=IIIIIiii}Q}{?=C*^{dispatch_data_s}^{_xpc_bundle_s}^v{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}i^{dispatch_queue_s}@?b1b1b1b1}}8i16"
+ "v20@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{_launch_domain_s}^v^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^*****^v^v*^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}***Q**[16C]^v*I^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}^{dispatch_source_s}**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I^{dispatch_source_s}*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIiIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}IC{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b4b20CSib1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1C}^{_launch_attribution_node_s}ICIIiCC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8i16"
+ "v28@?0^{_launch_domain_io_s={_launch_object_s=^vB}{?=*{_xpc_token_s=IIIIIiii}Q^{dispatch_queue_s}@?@?^{_launch_array_s}ICb1}}8^{_launch_io_s={_launch_object_s=^vB}{?={_xpc_token_s=IIIIIiii}Q}{?=C*^{dispatch_data_s}^{_xpc_bundle_s}^v{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}i^{dispatch_queue_s}@?b1b1b1b1}}16i24"
+ "v28@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{_launch_domain_s}^v^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^*****^v^v*^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}***Q**[16C]^v*I^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}^{dispatch_source_s}**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I^{dispatch_source_s}*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIiIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}IC{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b4b20CSib1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1C}^{_launch_attribution_node_s}ICIIiCC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8B16^{_launch_lint_s=@?*B}20"
+ "v32@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{_launch_domain_s}^v^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^*****^v^v*^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}***Q**[16C]^v*I^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}^{dispatch_source_s}**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I^{dispatch_source_s}*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIiIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}IC{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b4b20CSib1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1C}^{_launch_attribution_node_s}ICIIiCC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8*16^{_launch_lint_s=@?*B}24"
+ "v32@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{_launch_domain_s}^v^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^*****^v^v*^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}***Q**[16C]^v*I^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}^{dispatch_source_s}**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I^{dispatch_source_s}*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIiIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}IC{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b4b20CSib1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1C}^{_launch_attribution_node_s}ICIIiCC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8^v16^{_launch_lint_s=@?*B}24"
+ "v32@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{_launch_domain_s}^v^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^*****^v^v*^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}***Q**[16C]^v*I^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}^{dispatch_source_s}**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I^{dispatch_source_s}*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIiIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}IC{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b4b20CSib1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1C}^{_launch_attribution_node_s}ICIIiCC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8q16^{_launch_lint_s=@?*B}24"
+ "writeBytes"
+ "{Either<int, spar::Unit>=(Raw=i{Unit=})B}16@?0^v8"
+ "{Maybe<spar::Either<int, ess_auth_result_t>>={MaybeStore<spar::Either<int, ess_auth_result_t>>=(ReallyUnsafeMem<spar::Either<int, ess_auth_result_t>>={Either<int, ess_auth_result_t>=(Raw=ii)B})B}}16@?0r^i8"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SiUysI/Binaries/libxpc_executables/install/Symbols/launchd"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SiUysI/Sources/libxpc_executables/launchd/domain.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SiUysI/Sources/libxpc_executables/launchd/service_create.c"
- "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Sat Jun 13 22:20:12 PDT 2026; root:libxpc_executables-3298.0.4~137/launchd/RELEASE_ARM64E"
- "Darwin Bootstrapper Version 7.0.0: Sat Jun 13 22:20:12 PDT 2026; root:libxpc_executables-3298.0.4~137/launchd/RELEASE_ARM64E"
- "ForceEnabledServices"
- "Ignoring disabled state because service label is in force-enabled list: %s"
- "force-enabled services = {"
- "v16@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{_launch_domain_s}^v^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^*****^v^v*^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}***Q**[16C]^v*I^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}^{dispatch_source_s}**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I^{dispatch_source_s}*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIiIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}IC{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b4b20CSib1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1C}^{_launch_attribution_node_s}ICIIiCC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8"
- "v20@?0^{_launch_io_s={_launch_object_s=^vB}{?={_xpc_token_s=IIIIIiii}Q}{?=C*^{dispatch_data_s}^{_xpc_bundle_s}^v{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}i^{dispatch_queue_s}@?b1b1b1}}8i16"
- "v20@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{_launch_domain_s}^v^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^*****^v^v*^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}***Q**[16C]^v*I^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}^{dispatch_source_s}**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I^{dispatch_source_s}*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIiIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}IC{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b4b20CSib1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1C}^{_launch_attribution_node_s}ICIIiCC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8i16"
- "v28@?0^{_launch_domain_io_s={_launch_object_s=^vB}{?=*{_xpc_token_s=IIIIIiii}Q^{dispatch_queue_s}@?@?^{_launch_array_s}ICb1}}8^{_launch_io_s={_launch_object_s=^vB}{?={_xpc_token_s=IIIIIiii}Q}{?=C*^{dispatch_data_s}^{_xpc_bundle_s}^v{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}i^{dispatch_queue_s}@?b1b1b1}}16i24"
- "v28@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{_launch_domain_s}^v^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^*****^v^v*^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}***Q**[16C]^v*I^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}^{dispatch_source_s}**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I^{dispatch_source_s}*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIiIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}IC{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b4b20CSib1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1C}^{_launch_attribution_node_s}ICIIiCC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8B16^{_launch_lint_s=@?*B}20"
- "v32@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{_launch_domain_s}^v^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^*****^v^v*^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}***Q**[16C]^v*I^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}^{dispatch_source_s}**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I^{dispatch_source_s}*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIiIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}IC{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b4b20CSib1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1C}^{_launch_attribution_node_s}ICIIiCC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8*16^{_launch_lint_s=@?*B}24"
- "v32@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{_launch_domain_s}^v^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^*****^v^v*^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}***Q**[16C]^v*I^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}^{dispatch_source_s}**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I^{dispatch_source_s}*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIiIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}IC{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b4b20CSib1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1C}^{_launch_attribution_node_s}ICIIiCC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8^v16^{_launch_lint_s=@?*B}24"
- "v32@?0^{_launch_service_s={_launch_object_s=^vB}^{_launch_service_static_s}{?={?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}{?=^{_launch_service_s}^^{_launch_service_s}}}{?={?=^{_launch_event_subscription_s}}{?=^{_launch_event_provider_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_endpoint_s}}{?=^{_launch_socket_s}}{_instances_s=^{_launch_service_s}^^{_launch_service_s}{qm_trace=*i*i}}^{_launch_domain_s}^{_launch_service_s}II^v^{dispatch_group_s}iiis*^{_launch_coalition_s}^{_launch_coalition_s}^{_launch_domain_s}^v^{dispatch_group_s}^{dispatch_group_s}^{_launch_job_s}ICiib1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}{?={_xpc_token_s=IIIIIiii}[16C]CI^*****^v^v*^v^v{?=^{_launch_pended_request_s}}{_launch_service_delegate_s=^?^?^?^?^?^?^v}***Q**[16C]^v*I^v^v^v{?=^{_launch_service_semaphore_s}}{?=^{_launch_service_rlimit_s}}[3i]Iii^{dispatch_source_s}^{dispatch_source_s}**SQi^{dispatch_source_s}II^{_launch_diagnostic_thread_s}^{dispatch_source_s}^{dispatch_source_s}II^{dispatch_source_s}I^{dispatch_source_s}*II^{?}IiiiiiQIIIIIIII^{_launch_jetsam_stats_s}CQQ{?=^{_launch_envvar_s}}sCIiIISCQ{_launch_throttle_stats_s=BBIQ^v^v{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}}IC{?=*Qiii^{dispatch_source_s}^{dispatch_source_s}SSb8b4b20CSib1b1b1b1b1b1b1b1b1b1b1}{_launch_exit_status_s=C{proc_exitreasonbasicinfo=IQQI}iQQb1b1b1}{?=*^v*^v^{?}I^viisb1b1b1b1b1b1b1C}^{_launch_attribution_node_s}ICIIiCC**^{_os_opaque_64_map_s}b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}[0c]}8q16^{_launch_lint_s=@?*B}24"

```
